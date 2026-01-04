/**
 * DOE25 Tentaplugg - Task-specifika Quiz
 * 20+ quiz per task, pedagogiskt fokuserade med variation i rätt svar (A-D)
 * Inkluderar scenario-baserade frågor för praktisk tillämpning
 */

export interface TaskQuizQuestion {
    id: string
    question: string
    options: [string, string, string, string] // A, B, C, D
    correctIndex: 0 | 1 | 2 | 3 // 0=A, 1=B, 2=C, 3=D
    explanation: string
    difficulty: 'G' | 'VG'
    category: string
    scenario?: string // Optional scenario context for practical questions
    isScenario?: boolean // Flag for scenario-based questions
}

export interface TaskQuizSet {
    taskId: string
    taskTitle: string
    questions: TaskQuizQuestion[]
}

// =============================================================================
// TASK 1: SUBNETTING & NÄTVERK (20 quiz)
// =============================================================================

const TASK_1_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't1-q1',
        question: 'Hur många bitar består en IPv4-adress av?',
        options: ['16 bitar', '32 bitar', '64 bitar', '128 bitar'],
        correctIndex: 1, // B
        explanation: 'En IPv4-adress består av 32 bitar uppdelade i 4 oktetter om 8 bitar vardera.',
        difficulty: 'G',
        category: 'IPv4 Grunder'
    },
    {
        id: 't1-q2',
        question: 'Vad är subnätmasken för ett /24 nätverk?',
        options: ['255.0.0.0', '255.255.0.0', '255.255.255.0', '255.255.255.255'],
        correctIndex: 2, // C
        explanation: '/24 betyder 24 nätverksbitar = 255.255.255.0 (tre fulla oktetter av ettor).',
        difficulty: 'G',
        category: 'CIDR'
    },
    {
        id: 't1-q3',
        question: 'Hur många hosts kan finnas i ett /24 nätverk?',
        options: ['254', '255', '256', '252'],
        correctIndex: 0, // A
        explanation: '2^(32-24) - 2 = 256 - 2 = 254 hosts (minus nätverks- och broadcast-adress).',
        difficulty: 'G',
        category: 'Subnätberäkning'
    },
    {
        id: 't1-q4',
        question: 'Vilken IP-range är reserverad för loopback?',
        options: ['10.0.0.0/8', '192.168.0.0/16', '127.0.0.0/8', '172.16.0.0/12'],
        correctIndex: 2, // C
        explanation: '127.0.0.0/8 är reserverat för loopback. 127.0.0.1 är localhost.',
        difficulty: 'G',
        category: 'Reserverade adresser'
    },
    {
        id: 't1-q5',
        question: 'Vad visar kommandot "ip addr show"?',
        options: ['Routing-tabellen', 'Nätverkskonfiguration', 'DNS-inställningar', 'Brandväggsregler'],
        correctIndex: 1, // B
        explanation: '"ip addr show" (eller "ip a") visar nätverksgränssnitt med IP-adresser.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't1-q6',
        question: 'Vad är broadcast-adressen för 192.168.1.0/24?',
        options: ['192.168.1.0', '192.168.1.1', '192.168.1.254', '192.168.1.255'],
        correctIndex: 3, // D
        explanation: 'Broadcast är den sista adressen i subnätet där alla hostbitar är 1.',
        difficulty: 'G',
        category: 'Subnätberäkning'
    },
    {
        id: 't1-q7',
        question: 'Vilka av dessa är privata IP-adresser enligt RFC 1918?',
        options: ['8.8.8.8', '192.168.1.100', '1.1.1.1', '203.0.113.50'],
        correctIndex: 1, // B
        explanation: '192.168.0.0/16 är ett privat adressrum. De andra är publika IP-adresser.',
        difficulty: 'G',
        category: 'Reserverade adresser'
    },
    {
        id: 't1-q8',
        question: 'Vad gör kommandot "ping"?',
        options: ['Visar routing', 'Testar nätverksanslutning', 'Konfigurerar IP', 'Listar portar'],
        correctIndex: 1, // B
        explanation: 'ping skickar ICMP echo-paket för att testa om en host är nåbar.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't1-q9',
        question: 'Vad står CIDR för?',
        options: ['Computer Internet Domain Routing', 'Classless Inter-Domain Routing', 'Central IP Distribution Registry', 'Common Interface Data Rate'],
        correctIndex: 1, // B
        explanation: 'CIDR = Classless Inter-Domain Routing, ersatte gamla IP-klasserna.',
        difficulty: 'G',
        category: 'CIDR'
    },
    {
        id: 't1-q10',
        question: 'Vad är nätverksadressen för 10.20.30.40/8?',
        options: ['10.0.0.0', '10.20.0.0', '10.20.30.0', '10.20.30.40'],
        correctIndex: 0, // A
        explanation: '/8 betyder att bara första oktetten är nätverksdel, resten nollställs.',
        difficulty: 'G',
        category: 'Subnätberäkning'
    },
    {
        id: 't1-q11',
        question: 'Hur många hosts ryms i ett /30 nätverk?',
        options: ['4', '2', '6', '30'],
        correctIndex: 1, // B
        explanation: '2^(32-30) - 2 = 4 - 2 = 2 hosts. Används för punkt-till-punkt-länkar.',
        difficulty: 'VG',
        category: 'Subnätberäkning'
    },
    {
        id: 't1-q12',
        question: 'Vad är broadcast-adressen för 10.0.0.0/8?',
        options: ['10.0.0.255', '10.0.255.255', '10.255.255.255', '255.255.255.255'],
        correctIndex: 2, // C
        explanation: 'Med /8 är bara första oktetten nätverksdel, resten blir 255 för broadcast.',
        difficulty: 'VG',
        category: 'Subnätberäkning'
    },
    {
        id: 't1-q13',
        question: 'Du behöver minst 500 hosts. Vilken prefix-längd krävs?',
        options: ['/24 (254 hosts)', '/23 (510 hosts)', '/22 (1022 hosts)', '/25 (126 hosts)'],
        correctIndex: 1, // B
        explanation: '/23 ger 2^9 - 2 = 510 hosts, precis tillräckligt. /24 ger bara 254.',
        difficulty: 'VG',
        category: 'Subnätberäkning'
    },
    {
        id: 't1-q14',
        question: 'Vad gör kommandot "traceroute"?',
        options: ['Konfigurerar routing', 'Visar vägen till en destination', 'Rensar routing-cache', 'Testar bandbredd'],
        correctIndex: 1, // B
        explanation: 'traceroute visar alla hopp (routrar) på vägen till en destination.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't1-q15',
        question: 'Vilken subnätmask motsvarar /16?',
        options: ['255.0.0.0', '255.255.0.0', '255.255.255.0', '255.255.128.0'],
        correctIndex: 1, // B
        explanation: '/16 = 16 ettor = 255.255.0.0 (två fulla oktetter).',
        difficulty: 'G',
        category: 'CIDR'
    },
    {
        id: 't1-q16',
        question: 'Kan 192.168.1.50/24 och 192.168.2.50/24 kommunicera direkt?',
        options: ['Ja, samma nätverk', 'Nej, olika subnät', 'Bara med VPN', 'Bara via UDP'],
        correctIndex: 1, // B
        explanation: 'De är i olika subnät (192.168.1.0 vs 192.168.2.0). Kräver router.',
        difficulty: 'VG',
        category: 'Nätverkskoncept'
    },
    {
        id: 't1-q17',
        question: 'Vad är default gateway?',
        options: ['DNS-server', 'Router för trafik utanför lokalt nät', 'DHCP-server', 'Brandvägg'],
        correctIndex: 1, // B
        explanation: 'Default gateway är routern som hanterar trafik till andra nätverk.',
        difficulty: 'G',
        category: 'Nätverkskoncept'
    },
    {
        id: 't1-q18',
        question: 'Om du delar 192.168.1.0/24 i 4 subnät, vilken prefix får de?',
        options: ['/25', '/26', '/27', '/28'],
        correctIndex: 1, // B
        explanation: '4 subnät = 2^2, alltså 2 extra bitar. /24 + 2 = /26.',
        difficulty: 'VG',
        category: 'Subnätberäkning'
    },
    {
        id: 't1-q19',
        question: 'Vad visar kommandot "ip route show"?',
        options: ['IP-adresser', 'Routing-tabellen', 'ARP-cache', 'DNS-poster'],
        correctIndex: 1, // B
        explanation: '"ip route show" visar routing-tabellen med default gateway.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't1-q20',
        question: 'Vad är nätverksadressen för 10.20.30.40/22?',
        options: ['10.20.30.0', '10.20.28.0', '10.20.0.0', '10.20.32.0'],
        correctIndex: 1, // B
        explanation: '/22 = 255.255.252.0. Tredje oktetten: 30 AND 252 = 28. Svar: 10.20.28.0',
        difficulty: 'VG',
        category: 'Subnätberäkning'
    },
    // SCENARIO-BASERADE FRÅGOR
    {
        id: 't1-s1',
        question: 'Din chef säger: "Vi har 200 anställda som behöver IP-adresser." Vilken subnätmask rekommenderar du?',
        options: ['/25 (126 hosts)', '/24 (254 hosts)', '/23 (510 hosts)', '/22 (1022 hosts)'],
        correctIndex: 1, // B
        explanation: '/24 ger 254 hosts - precis lagom för 200 anställda med lite marginal.',
        difficulty: 'VG',
        category: 'Praktisk tillämpning',
        scenario: 'Du är nätverkstekniker och planerar företagets nya kontor.',
        isScenario: true
    },
    {
        id: 't1-s2',
        question: 'Server A (192.168.1.50/24) kan inte pinga Server B (192.168.2.50/24). Vad är troligaste orsaken?',
        options: ['Fel subnätmask', 'De är på olika subnät - behöver router', 'DNS-fel', 'Brandvägg blockerar'],
        correctIndex: 1, // B
        explanation: 'De är på olika nätverk (192.168.1.0 vs 192.168.2.0) och behöver en router för att kommunicera.',
        difficulty: 'VG',
        category: 'Felsökning',
        scenario: 'Du felsöker nätverksproblem i serverrummet.',
        isScenario: true
    },
    {
        id: 't1-s3',
        question: 'Du får 10.0.0.0/8 och ska skapa 4 avdelningar. Vilken prefix ger mest hosts per avdelning?',
        options: ['/10 (4M hosts)', '/9 (8M hosts)', '/11 (2M hosts)', '/12 (1M hosts)'],
        correctIndex: 0, // A
        explanation: '4 subnät = 2 extra bitar. /8 + 2 = /10. Varje /10 ger ~4 miljoner hosts.',
        difficulty: 'VG',
        category: 'Subnetting design',
        scenario: 'Du designar nätverksarkitekturen för ett stort företag.',
        isScenario: true
    },
    {
        id: 't1-s4',
        question: 'Nätverksteamet rapporterar: "ipcalc 192.168.5.130/26". Vad är broadcast-adressen?',
        options: ['192.168.5.127', '192.168.5.191', '192.168.5.255', '192.168.5.159'],
        correctIndex: 1, // B
        explanation: '/26 = 64 adresser. 130 ligger i 128-191 blocket. Broadcast = 191.',
        difficulty: 'VG',
        category: 'Beräkning',
        scenario: 'Du dubbelkollar en kollegas nätverksberäkning.',
        isScenario: true
    },
    {
        id: 't1-s5',
        question: 'En klient har IP 172.16.50.100/20. Kan den kommunicera med 172.16.60.100 utan router?',
        options: ['Ja, samma subnät', 'Nej, olika subnät', 'Beror på gateway', 'Endast via VPN'],
        correctIndex: 0, // A
        explanation: '/20 ger range 172.16.48.0-172.16.63.255. Båda 50 och 60 ligger i detta intervall.',
        difficulty: 'VG',
        category: 'Felsökning',
        scenario: 'Du verifierar nätverksanslutningar före lansering.',
        isScenario: true
    }
]

// =============================================================================
// TASK 2: LINUX FILSYSTEM (20 quiz)
// =============================================================================

const TASK_2_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't2-q1',
        question: 'Var lagras systemkonfigurationsfiler i Linux?',
        options: ['/var', '/etc', '/usr', '/opt'],
        correctIndex: 1, // B
        explanation: '/etc innehåller systemkonfiguration som passwd, shadow, fstab, ssh/',
        difficulty: 'G',
        category: 'Viktiga kataloger'
    },
    {
        id: 't2-q2',
        question: 'Vilken katalog innehåller systemloggar?',
        options: ['/etc/log', '/var/log', '/log', '/usr/log'],
        correctIndex: 1, // B
        explanation: '/var/log innehåller systemloggar som syslog, auth.log, kern.log.',
        difficulty: 'G',
        category: 'Viktiga kataloger'
    },
    {
        id: 't2-q3',
        question: 'Vad står FHS för?',
        options: ['File Handling System', 'Filesystem Hierarchy Standard', 'Fast Host Storage', 'Folder Hash Structure'],
        correctIndex: 1, // B
        explanation: 'FHS = Filesystem Hierarchy Standard, definierar Linux katalogstruktur.',
        difficulty: 'G',
        category: 'FHS Grunder'
    },
    {
        id: 't2-q4',
        question: 'Var finns roots hemkatalog?',
        options: ['/home/root', '/root', '/usr/root', '/etc/root'],
        correctIndex: 1, // B
        explanation: 'Root-användaren har /root som hemkatalog, inte /home/root.',
        difficulty: 'G',
        category: 'Viktiga kataloger'
    },
    {
        id: 't2-q5',
        question: 'Kommando för att visa nuvarande katalog?',
        options: ['cd', 'pwd', 'ls', 'dir'],
        correctIndex: 1, // B
        explanation: 'pwd = Print Working Directory, visar nuvarande katalog.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't2-q6',
        question: 'Vad innehåller katalogen /tmp?',
        options: ['Systemloggar', 'Temporära filer', 'Templates', 'Kernel-moduler'],
        correctIndex: 1, // B
        explanation: '/tmp innehåller temporära filer som rensas vid omstart.',
        difficulty: 'G',
        category: 'Viktiga kataloger'
    },
    {
        id: 't2-q7',
        question: 'Vilket tecken representerar en katalog i ls -l output?',
        options: ['-', 'd', 'l', 'c'],
        correctIndex: 1, // B (d)
        explanation: 'd = directory. - = vanlig fil, l = symbolisk länk.',
        difficulty: 'G',
        category: 'Filtyper'
    },
    {
        id: 't2-q8',
        question: 'Vad visar kommandot "df -h"?',
        options: ['Filrättigheter', 'Diskutrymme per filsystem', 'Katalogstorlek', 'Dolda filer'],
        correctIndex: 1, // B
        explanation: 'df -h visar diskutrymme per filsystem i human-readable format.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't2-q9',
        question: 'Vad innehåller /dev?',
        options: ['Development-filer', 'Device-filer', 'Dokumentation', 'Drivrutiner'],
        correctIndex: 1, // B
        explanation: '/dev innehåller device-filer som representerar hårdvara.',
        difficulty: 'G',
        category: 'Viktiga kataloger'
    },
    {
        id: 't2-q10',
        question: 'Vad är skillnaden mellan absolut och relativ sökväg?',
        options: ['Ingen skillnad', 'Absolut börjar från /, relativ från nuvarande katalog', 'Relativ är snabbare', 'Absolut är kortare'],
        correctIndex: 1, // B
        explanation: 'Absolut: /etc/ssh. Relativ: ../etc (från nuvarande position).',
        difficulty: 'G',
        category: 'Navigation'
    },
    {
        id: 't2-q11',
        question: 'Vad innehåller filen /etc/passwd?',
        options: ['Krypterade lösenord', 'Användarinformation', 'Lösenordspolicy', 'SSH-nycklar'],
        correctIndex: 1, // B
        explanation: '/etc/passwd har användarinfo. Krypterade lösenord är i /etc/shadow.',
        difficulty: 'VG',
        category: 'Konfigurationsfiler'
    },
    {
        id: 't2-q12',
        question: 'Vad är /proc?',
        options: ['Program-katalog', 'Virtuellt filsystem med processinfo', 'Processor-drivrutiner', 'Procedur-skript'],
        correctIndex: 1, // B
        explanation: '/proc är ett virtuellt filsystem med process- och systeminformation.',
        difficulty: 'VG',
        category: 'Viktiga kataloger'
    },
    {
        id: 't2-q13',
        question: 'Skillnad mellan hård och symbolisk länk?',
        options: ['Ingen skillnad', 'Hård länk är snabbare', 'Symbolisk bryts om original tas bort', 'Symbolisk tar mer plats'],
        correctIndex: 2, // C
        explanation: 'Symbolisk länk pekar på filnamn och bryts. Hård länk delar inode.',
        difficulty: 'VG',
        category: 'Filtyper'
    },
    {
        id: 't2-q14',
        question: 'Vad gör kommandot "du -sh /var/log"?',
        options: ['Visar disk usage', 'Tar bort katalog', 'Duplicerar katalog', 'Dekomprimerar'],
        correctIndex: 0, // A
        explanation: 'du -sh visar total storlek (-s) i human-readable format (-h).',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't2-q15',
        question: 'Vad är /dev/null?',
        options: ['Tom enhet', 'Svart hål som slänger data', 'Null-modem', 'Nätverksenhet'],
        correctIndex: 1, // B
        explanation: '/dev/null är ett svart hål - all data som skrivs dit försvinner.',
        difficulty: 'VG',
        category: 'Device-filer'
    },
    {
        id: 't2-q16',
        question: 'Var installeras tredjepartsprogram enligt FHS?',
        options: ['/usr/local', '/opt', 'Båda A och B är korrekta', '/bin'],
        correctIndex: 2, // C
        explanation: 'Tredjepartsprogram kan installeras i /opt eller /usr/local.',
        difficulty: 'VG',
        category: 'FHS Grunder'
    },
    {
        id: 't2-q17',
        question: 'Vad innehåller /etc/fstab?',
        options: ['Filsystem att mounta vid boot', 'Fast boot-inställningar', 'Filsystemstatistik', 'Fabriksinställningar'],
        correctIndex: 0, // A
        explanation: '/etc/fstab definierar vilka filsystem som ska monteras automatiskt.',
        difficulty: 'VG',
        category: 'Konfigurationsfiler'
    },
    {
        id: 't2-q18',
        question: 'Kommando för att söka efter filer i realtid?',
        options: ['locate', 'find', 'search', 'grep'],
        correctIndex: 1, // B
        explanation: 'find söker i realtid. locate använder en databas (snabbare men kan vara inaktuell).',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't2-q19',
        question: 'Vad är en inode?',
        options: ['Filnamn', 'Datastruktur med filmetadata', 'Nätverksnod', 'Index-nod för databaser'],
        correctIndex: 1, // B
        explanation: 'En inode innehåller metadata om en fil (rättigheter, ägare, storlek) men EJ filnamnet.',
        difficulty: 'VG',
        category: 'Filsystem internals'
    },
    {
        id: 't2-q20',
        question: 'Vad gör sticky bit på /tmp?',
        options: ['Gör filer skrivskyddade', 'Bara ägaren kan ta bort sina filer', 'Komprimerar automatiskt', 'Krypterar filer'],
        correctIndex: 1, // B
        explanation: 'Sticky bit (chmod +t) gör att bara filägaren kan ta bort sin fil i katalogen.',
        difficulty: 'VG',
        category: 'Rättigheter'
    },
    // SCENARIO-BASERADE FRÅGOR
    {
        id: 't2-s1',
        question: 'Servern är full! Var börjar du leta efter stora logfiler?',
        options: ['/home', '/var/log', '/etc', '/usr'],
        correctIndex: 1, // B
        explanation: '/var/log växer ofta okontrollerat med systemloggar, särskilt auth.log och syslog.',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'Du får larm: "Disk 95% full" på produktionsservern.',
        isScenario: true
    },
    {
        id: 't2-s2',
        question: 'Du ska redigera SSH-konfigurationen. Vilken fil öppnar du?',
        options: ['/etc/ssh/sshd_config', '/var/ssh/config', '/home/ssh/settings', '/usr/ssh/sshd'],
        correctIndex: 0, // A
        explanation: 'Alla tjänsters konfiguration ligger i /etc. SSH-demon = /etc/ssh/sshd_config.',
        difficulty: 'G',
        category: 'Praktisk tillämpning',
        scenario: 'Säkerhetsteamet vill ändra SSH-port från 22 till 2222.',
        isScenario: true
    },
    {
        id: 't2-s3',
        question: 'En ny disk /dev/sdb1 är monterad på /data. Var lägger du mount-info för att överleva omstart?',
        options: ['/etc/mount.conf', '/etc/fstab', '/var/mount/auto', '/boot/mount'],
        correctIndex: 1, // B
        explanation: '/etc/fstab (File System Table) definierar automatisk montering vid boot.',
        difficulty: 'VG',
        category: 'Praktisk tillämpning',
        scenario: 'Du har lagt till en ny datadisk som ska monteras automatiskt.',
        isScenario: true
    },
    {
        id: 't2-s4',
        question: 'Applikationen loggar inte alls. Var skapar du loggkatalogen enligt FHS?',
        options: ['/home/app/logs', '/var/log/appname', '/etc/logs/app', '/opt/logs'],
        correctIndex: 1, // B
        explanation: '/var/log är standardplatsen för alla typer av loggar enligt FHS.',
        difficulty: 'G',
        category: 'Best practices',
        scenario: 'Du installerar en ny applikation och ska konfigurera loggning.',
        isScenario: true
    },
    {
        id: 't2-s5',
        question: 'df -h visar /dev/sda1 på 100%. Vilket kommando visar vilka mappar är störst?',
        options: ['ls -la /', 'du -sh /* | sort -h', 'cat /proc/diskstats', 'free -h'],
        correctIndex: 1, // B
        explanation: 'du -sh /* visar storlek per toppkatalog, sort -h sorterar human-readable.',
        difficulty: 'VG',
        category: 'Felsökning',
        scenario: 'Du ska hitta vad som fyller disken.',
        isScenario: true
    }
]

// =============================================================================
// TASK 3: BASH GRUNDER (20 quiz questions)
// =============================================================================

const TASK_3_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't3-q1',
        question: 'Vad är korrekt shebang för ett bash-skript?',
        options: ['#/bin/bash', '#!/bin/bash', '!/bin/bash', '##/bin/bash'],
        correctIndex: 1, // B
        explanation: 'Shebang börjar alltid med #! följt av sökvägen till tolken.',
        difficulty: 'G',
        category: 'Skriptstruktur'
    },
    {
        id: 't3-q2',
        question: 'Vilket kommando gör ett skript körbart?',
        options: ['chmod +r skript.sh', 'chmod +x skript.sh', 'chmod +w skript.sh', 'chmod 644 skript.sh'],
        correctIndex: 1, // B
        explanation: 'chmod +x lägger till execute-rättighet som krävs för att köra skript.',
        difficulty: 'G',
        category: 'Köra skript'
    },
    {
        id: 't3-q3',
        question: 'Vad betyder exit code 0?',
        options: ['Fel uppstod', 'Kommandot hittades inte', 'Framgång', 'Permission denied'],
        correctIndex: 2, // C
        explanation: 'Exit code 0 betyder alltid att kommandot/skriptet lyckades utan fel.',
        difficulty: 'G',
        category: 'Exit codes'
    },
    {
        id: 't3-q4',
        question: 'Hur kontrollerar du senaste kommandots exit code?',
        options: ['echo $!', 'echo $#', 'echo $?', 'echo $$'],
        correctIndex: 2, // C
        explanation: '$? innehåller exit code från det senast körda kommandot.',
        difficulty: 'G',
        category: 'Exit codes'
    },
    {
        id: 't3-q5',
        question: 'Vilket kommando läser input från användaren?',
        options: ['input variabel', 'read variabel', 'get variabel', 'scan variabel'],
        correctIndex: 1, // B
        explanation: 'read läser en rad input och sparar i angiven variabel.',
        difficulty: 'G',
        category: 'I/O'
    },
    {
        id: 't3-q6',
        question: 'Vad betyder exit code 127?',
        options: ['Permission denied', 'Syntax error', 'Command not found', 'Timeout'],
        correctIndex: 2, // C
        explanation: 'Exit code 127 indikerar att kommandot inte kunde hittas i PATH.',
        difficulty: 'G',
        category: 'Exit codes'
    },
    {
        id: 't3-q7',
        question: 'Hur skriver du en kommentar i bash?',
        options: ['// kommentar', '/* kommentar */', '# kommentar', '-- kommentar'],
        correctIndex: 2, // C
        explanation: 'I bash börjar kommentarer med # och allt efter ignoreras.',
        difficulty: 'G',
        category: 'Skriptstruktur'
    },
    {
        id: 't3-q8',
        question: 'Vilken är en fördel med #!/usr/bin/env bash?',
        options: ['Snabbare exekvering', 'Mer portabel', 'Bättre felhantering', 'Stödjer fler funktioner'],
        correctIndex: 1, // B
        explanation: 'env hittar bash via PATH, fungerar även om bash är installerad på annan plats.',
        difficulty: 'G',
        category: 'Shebang'
    },
    {
        id: 't3-q9',
        question: 'Skillnad mellan ./skript.sh och source skript.sh?',
        options: ['Ingen skillnad', './skript.sh kör i subshell', 'source kör i subshell', './skript.sh är snabbare'],
        correctIndex: 1, // B
        explanation: './skript.sh kör i en ny subshell, source kör i nuvarande shell.',
        difficulty: 'VG',
        category: 'Köra skript'
    },
    {
        id: 't3-q10',
        question: 'Vad gör && mellan två kommandon?',
        options: ['Kör båda alltid', 'Kör andra endast om första lyckas', 'Kör andra endast om första misslyckas', 'Kör i parallell'],
        correctIndex: 1, // B
        explanation: '&& (AND) kör nästa kommando endast om det förra hade exit code 0.',
        difficulty: 'G',
        category: 'Kommandokedjning'
    },
    {
        id: 't3-q11',
        question: 'Vad gör || mellan två kommandon?',
        options: ['Kör båda alltid', 'Kör andra endast om första lyckas', 'Kör andra endast om första misslyckas', 'Väljer slumpmässigt'],
        correctIndex: 2, // C
        explanation: '|| (OR) kör nästa kommando endast om det förra misslyckades.',
        difficulty: 'VG',
        category: 'Kommandokedjning'
    },
    {
        id: 't3-q12',
        question: 'Hur fångar du output från ett kommando i en variabel?',
        options: ['result = kommando', 'result=$(kommando)', 'result->kommando', 'kommando > result'],
        correctIndex: 1, // B
        explanation: '$(kommando) kör kommandot och returnerar dess output för tilldelning.',
        difficulty: 'VG',
        category: 'Kommandosubstitution'
    },
    {
        id: 't3-q13',
        question: 'Vad gör set -e i ett skript?',
        options: ['Aktiverar debug-läge', 'Avslutar vid fel', 'Exporterar alla variabler', 'Aktiverar echo'],
        correctIndex: 1, // B
        explanation: 'set -e gör att skriptet avslutas omedelbart om ett kommando misslyckas.',
        difficulty: 'VG',
        category: 'Skriptstruktur'
    },
    {
        id: 't3-q14',
        question: 'Vad gör set -x i ett skript?',
        options: ['Avslutar vid fel', 'Skriver ut kommandon innan de körs', 'Exporterar variabler', 'Aktiverar strict mode'],
        correctIndex: 1, // B
        explanation: 'set -x (xtrace) skriver ut varje kommando för debugging.',
        difficulty: 'VG',
        category: 'Skriptstruktur'
    },
    {
        id: 't3-q15',
        question: 'Vad betyder exit code 126?',
        options: ['Syntax error', 'Command not found', 'Permission denied (ej körbart)', 'Out of memory'],
        correctIndex: 2, // C
        explanation: 'Exit code 126 betyder att filen finns men inte är körbar.',
        difficulty: 'VG',
        category: 'Exit codes'
    },
    {
        id: 't3-q16',
        question: 'Hur kör du ett kommando i bakgrunden?',
        options: ['kommando &', 'kommando --bg', 'bg kommando', 'kommando -d'],
        correctIndex: 0, // A
        explanation: '& i slutet av ett kommando startar det i bakgrunden.',
        difficulty: 'G',
        category: 'Processhantering'
    },
    {
        id: 't3-q17',
        question: 'Vad gör trap i bash?',
        options: ['Loggar fel', 'Fångar signaler', 'Skapar loopar', 'Definierar funktioner'],
        correctIndex: 1, // B
        explanation: 'trap fångar signaler (som SIGINT) och kör specificerad kod.',
        difficulty: 'VG',
        category: 'Signalhantering'
    },
    {
        id: 't3-q18',
        question: 'Vilken signal kan INTE fångas med trap?',
        options: ['SIGTERM', 'SIGINT', 'SIGKILL', 'SIGHUP'],
        correctIndex: 2, // C
        explanation: 'SIGKILL (kill -9) kan aldrig fångas eller ignoreras.',
        difficulty: 'VG',
        category: 'Signalhantering'
    },
    {
        id: 't3-q19',
        question: 'Vad innehåller $$?',
        options: ['Exit code', 'Antal argument', 'Processens PID', 'Senaste bakgrundsprocessens PID'],
        correctIndex: 2, // C
        explanation: '$$ innehåller PID (Process ID) för nuvarande shell eller skript.',
        difficulty: 'VG',
        category: 'Specialvariabler'
    },
    {
        id: 't3-q20',
        question: 'Vad gör tee-kommandot?',
        options: ['Skapar temporära filer', 'Skriver till fil OCH stdout', 'Sorterar output', 'Tar bort dubbletter'],
        correctIndex: 1, // B
        explanation: 'tee skriver input till både en fil och standard output samtidigt.',
        difficulty: 'VG',
        category: 'I/O'
    },
    // SCENARIO-BASERADE FRÅGOR
    {
        id: 't3-s1',
        question: 'Ditt skript körs men visar "Permission denied". Vad har du glömt?',
        options: ['Shebang', 'chmod +x', 'sudo', 'Variabeldeklaration'],
        correctIndex: 1, // B
        explanation: 'Skriptfiler måste vara exekverbara. chmod +x script.sh löser problemet.',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'Du skrev ett nytt backup-skript men det vägrar köra.',
        isScenario: true
    },
    {
        id: 't3-s2',
        question: 'Skriptet fungerar med bash script.sh men inte ./script.sh. Varför?',
        options: ['Fel filnamn', 'Saknar shebang #!/bin/bash', 'Syntax error', 'Saknar variabel'],
        correctIndex: 1, // B
        explanation: 'Utan shebang vet systemet inte vilken tolk som ska användas vid ./körning.',
        difficulty: 'VG',
        category: 'Felsökning',
        scenario: 'En kollega frågar varför skriptet bara fungerar på ett sätt.',
        isScenario: true
    },
    {
        id: 't3-s3',
        question: 'Du vill logga output och felmeddelanden till samma fil. Vad använder du?',
        options: ['> logfil', '>> logfil', '&> logfil', '2> logfil'],
        correctIndex: 2, // C
        explanation: '&> redirectar både stdout (1) och stderr (2) till samma fil.',
        difficulty: 'VG',
        category: 'Praktisk tillämpning',
        scenario: 'Ditt nattliga cronjob behöver komplett loggning.',
        isScenario: true
    },
    {
        id: 't3-s4',
        question: 'Skriptet avslutades utan fel men föregående kommando misslyckades. Vad returnerar echo $?',
        options: ['0', '1', 'error', 'null'],
        correctIndex: 0, // A
        explanation: 'echo lyckades (exit 0) - $? visar SENASTE kommandots exit code, inte tidigare.',
        difficulty: 'VG',
        category: 'Felsökning',
        scenario: 'Du debuggar ett skript som inte fångar fel korrekt.',
        isScenario: true
    },
    {
        id: 't3-s5',
        question: 'Du vill att skriptet ska avbryta vid första felet. Vilken rad lägger du till?',
        options: ['set -x', 'set -e', 'trap error', 'exit 1'],
        correctIndex: 1, // B
        explanation: 'set -e gör att skriptet avslutar direkt om något kommando returnerar != 0.',
        difficulty: 'VG',
        category: 'Best practices',
        scenario: 'Produktionsskriptet fortsätter trots att ett steg misslyckas.',
        isScenario: true
    }
]

// =============================================================================
// TASK 4: VARIABLER & DATATYPER (20 quiz questions)
// =============================================================================

const TASK_4_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't4-q1',
        question: 'Vilken är KORREKT variabeltilldelning i bash?',
        options: ['namn = "värde"', 'namn="värde"', 'set namn="värde"', '$namn="värde"'],
        correctIndex: 1, // B
        explanation: 'I bash får det INTE finnas mellanslag runt = vid tilldelning.',
        difficulty: 'G',
        category: 'Variabler'
    },
    {
        id: 't4-q2',
        question: 'Hur läser du värdet av en variabel?',
        options: ['variabel', '%variabel%', '$variabel', '&variabel'],
        correctIndex: 2, // C
        explanation: 'I bash används $ före variabelnamnet för att läsa dess värde.',
        difficulty: 'G',
        category: 'Variabler'
    },
    {
        id: 't4-q3',
        question: 'Vilken miljövariabel innehåller hemkatalogen?',
        options: ['$HOMEDIR', '$HOME', '$USERDIR', '$HOUSE'],
        correctIndex: 1, // B
        explanation: '$HOME innehåller sökvägen till användarens hemkatalog.',
        difficulty: 'G',
        category: 'Miljövariabler'
    },
    {
        id: 't4-q4',
        question: 'Vilket kommando visar alla miljövariabler?',
        options: ['vars', 'env', 'show', 'list'],
        correctIndex: 1, // B
        explanation: 'env eller printenv visar alla definierade miljövariabler.',
        difficulty: 'G',
        category: 'Miljövariabler'
    },
    {
        id: 't4-q5',
        question: 'Vad gör export variabel?',
        options: ['Sparar till fil', 'Gör tillgänglig för barnprocesser', 'Kopierar variabeln', 'Tar bort variabeln'],
        correctIndex: 1, // B
        explanation: 'export gör att variabeln ärvs av processer som startas från det aktuella shellt.',
        difficulty: 'G',
        category: 'Miljövariabler'
    },
    {
        id: 't4-q6',
        question: 'Hur får du längden av en sträng i variabeln str?',
        options: ['len(str)', '${#str}', 'str.length', '${str.len}'],
        correctIndex: 1, // B
        explanation: '${#variabel} returnerar antalet tecken i variabelns värde.',
        difficulty: 'G',
        category: 'Stränghantering'
    },
    {
        id: 't4-q7',
        question: 'Vad innehåller $PATH?',
        options: ['Nuvarande katalog', 'Hemkatalogen', 'Sökvägar för kommandon', 'Temporära filer'],
        correctIndex: 2, // C
        explanation: '$PATH är en lista med kataloger där systemet letar efter körbara program.',
        difficulty: 'G',
        category: 'Miljövariabler'
    },
    {
        id: 't4-q8',
        question: 'Hur deklarerar du en array i bash?',
        options: ['array = [1,2,3]', 'array=(1 2 3)', 'array{1,2,3}', '@array = (1,2,3)'],
        correctIndex: 1, // B
        explanation: 'I bash separeras arrayelement med mellanslag inom parenteser.',
        difficulty: 'G',
        category: 'Arrayer'
    },
    {
        id: 't4-q9',
        question: 'Hur kommer du åt första elementet i en array?',
        options: ['${array[1]}', '${array[0]}', '$array[0]', 'array(0)'],
        correctIndex: 1, // B
        explanation: 'Bash-arrayer är 0-indexerade, första elementet är [0].',
        difficulty: 'G',
        category: 'Arrayer'
    },
    {
        id: 't4-q10',
        question: 'Vad innehåller $# i ett skript?',
        options: ['Skriptets PID', 'Exit code', 'Antal argument', 'Första argumentet'],
        correctIndex: 2, // C
        explanation: '$# innehåller antalet argument som skickades till skriptet.',
        difficulty: 'G',
        category: 'Specialvariabler'
    },
    {
        id: 't4-q11',
        question: 'Hur tar du ut de första 5 tecknen från variabeln str?',
        options: ['${str:5}', '${str:0:5}', '${str[0:5]}', 'str.substring(0,5)'],
        correctIndex: 1, // B
        explanation: '${variabel:start:längd} ger en substring.',
        difficulty: 'VG',
        category: 'Stränghantering'
    },
    {
        id: 't4-q12',
        question: 'Hur ersätter du ALLA förekomster av "old" med "new" i variabeln?',
        options: ['${var/old/new}', '${var//old/new}', '${var:old:new}', 'replace(var,old,new)'],
        correctIndex: 1, // B
        explanation: '// ersätter alla förekomster, / ersätter bara första.',
        difficulty: 'VG',
        category: 'Stränghantering'
    },
    {
        id: 't4-q13',
        question: 'Hur får du alla element i en array?',
        options: ['$array', '${array}', '${array[@]}', 'array[*]'],
        correctIndex: 2, // C
        explanation: '${array[@]} expanderar till alla element i arrayen.',
        difficulty: 'VG',
        category: 'Arrayer'
    },
    {
        id: 't4-q14',
        question: 'Hur får du antalet element i en array?',
        options: ['${array.length}', '${#array}', '${#array[@]}', 'count(array)'],
        correctIndex: 2, // C
        explanation: '${#array[@]} kombinerar # (längd) med [@] (alla element).',
        difficulty: 'VG',
        category: 'Arrayer'
    },
    {
        id: 't4-q15',
        question: 'Vad innehåller $0 i ett skript?',
        options: ['Första argumentet', 'Skriptets namn', 'Exit code', 'Noll'],
        correctIndex: 1, // B
        explanation: '$0 innehåller namnet/sökvägen till själva skriptet.',
        difficulty: 'G',
        category: 'Specialvariabler'
    },
    {
        id: 't4-q16',
        question: 'Hur skapar du ett associativt array (hash)?',
        options: ['array={}', 'declare -A array', 'hash array', 'array=()'],
        correctIndex: 1, // B
        explanation: 'declare -A skapar ett associativt array med nyckel-värde par.',
        difficulty: 'VG',
        category: 'Arrayer'
    },
    {
        id: 't4-q17',
        question: 'Vad gör ${variabel:-default}?',
        options: ['Subtraherar default', 'Returnerar default om variabel är tom', 'Sätter variabeln till default', 'Jämför med default'],
        correctIndex: 1, // B
        explanation: ':- returnerar default om variabeln är odefinierad eller tom, men sätter den inte.',
        difficulty: 'VG',
        category: 'Parameterexpansion'
    },
    {
        id: 't4-q18',
        question: 'Skillnad mellan $@ och $* (inom citattecken)?',
        options: ['Ingen skillnad', '$@ ger separata argument, $* ger en sträng', '$* ger separata argument', 'Båda ger arrayer'],
        correctIndex: 1, // B
        explanation: '"$@" expanderar till separata ord, "$*" till en enda sträng.',
        difficulty: 'VG',
        category: 'Specialvariabler'
    },
    {
        id: 't4-q19',
        question: 'Hur tar du bort filändelsen från variabeln fil="test.txt"?',
        options: ['${fil%.txt}', '${fil#.txt}', '${fil/.txt/}', '${fil:0:-4}'],
        correctIndex: 0, // A
        explanation: '% tar bort matchande suffix. ${fil%.*} tar bort sista filändelsen.',
        difficulty: 'VG',
        category: 'Stränghantering'
    },
    {
        id: 't4-q20',
        question: 'Hur gör du en variabel readonly?',
        options: ['lock variabel', 'readonly variabel', 'const variabel', 'final variabel'],
        correctIndex: 1, // B
        explanation: 'readonly eller declare -r gör att variabeln inte kan ändras.',
        difficulty: 'VG',
        category: 'Variabler'
    },
    // SCENARIO-BASERADE FRÅGOR
    {
        id: 't4-s1',
        question: 'Skriptet skriver ut "Hello " utan namn fast du angav det. Koden är: echo "Hello $name". Vad är fel?',
        options: ['Glömt export', 'Variabeln är tom/odefinierad', 'Fel citattecken', 'echo fungerar inte så'],
        correctIndex: 1, // B
        explanation: 'Variabeln $name är inte tilldelad. Använd ${name:-"default"} för fallback.',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'Du debuggar ett skript som inte visar användarnamnet.',
        isScenario: true
    },
    {
        id: 't4-s2',
        question: 'echo \'$HOME\' skriver ut "$HOME" bokstavligt. Varför?',
        options: ['Fel variabelnamn', 'Single quotes expanderar inte variabler', 'HOME är inte exporterad', 'Måste använda ${}'],
        correctIndex: 1, // B
        explanation: 'Single quotes (\'\') gör att allt tolkas bokstavligt. Använd double quotes ("").',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'En kollega undrar varför PATH inte visas i skriptet.',
        isScenario: true
    },
    {
        id: 't4-s3',
        question: 'Du vill spara kommandooutput: files=ls. Men $files är tom. Varför?',
        options: ['ls finns inte', 'Måste använda files=$(ls)', 'Fel variabelnamn', 'Behöver export'],
        correctIndex: 1, // B
        explanation: 'Command substitution kräver $(kommando) eller `kommando` för att fånga output.',
        difficulty: 'VG',
        category: 'Felsökning',
        scenario: 'Skriptet ska lista filer men variabeln är alltid tom.',
        isScenario: true
    }
]

// =============================================================================
// TASK 5: REGULJÄRA UTTRYCK - REGEX (20 quiz questions)
// =============================================================================

const TASK_5_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't5-q1',
        question: 'Vad matchar . (punkt) i regex?',
        options: ['Endast punkt', 'Ett valfritt tecken', 'Noll eller fler tecken', 'Början av rad'],
        correctIndex: 1, // B
        explanation: '. matchar exakt ETT valfritt tecken (utom newline).',
        difficulty: 'G',
        category: 'Metatecken'
    },
    {
        id: 't5-q2',
        question: 'Vad betyder ^ i regex?',
        options: ['Slutet av rad', 'Början av rad', 'Exponent', 'Negation'],
        correctIndex: 1, // B
        explanation: '^ förankrar mönstret till början av raden.',
        difficulty: 'G',
        category: 'Ankare'
    },
    {
        id: 't5-q3',
        question: 'Vad betyder $ i regex?',
        options: ['Variabel', 'Början av rad', 'Slutet av rad', 'Pengar'],
        correctIndex: 2, // C
        explanation: '$ förankrar mönstret till slutet av raden.',
        difficulty: 'G',
        category: 'Ankare'
    },
    {
        id: 't5-q4',
        question: 'Vad matchar * i regex?',
        options: ['Exakt ett tecken', 'Ett eller fler', 'Noll eller fler', 'Valfritt tecken'],
        correctIndex: 2, // C
        explanation: '* matchar noll eller fler av föregående tecken.',
        difficulty: 'G',
        category: 'Kvantifierare'
    },
    {
        id: 't5-q5',
        question: 'Vad matchar + i regex?',
        options: ['Noll eller fler', 'Ett eller fler', 'Exakt ett', 'Addition'],
        correctIndex: 1, // B
        explanation: '+ matchar ett eller fler av föregående tecken (minst en).',
        difficulty: 'G',
        category: 'Kvantifierare'
    },
    {
        id: 't5-q6',
        question: 'Vad gör [abc] i regex?',
        options: ['Matchar "abc"', 'Matchar a, b eller c', 'Matchar alla utom abc', 'Gruppering'],
        correctIndex: 1, // B
        explanation: '[] är en teckenklass som matchar ETT av de angivna tecknen.',
        difficulty: 'G',
        category: 'Teckenklasser'
    },
    {
        id: 't5-q7',
        question: 'Vad gör grep -i?',
        options: ['Invertera matchning', 'Case insensitive', 'Visa radnummer', 'Rekursiv sökning'],
        correctIndex: 1, // B
        explanation: '-i gör sökningen case insensitive (ignorerar versaler/gemener).',
        difficulty: 'G',
        category: 'grep'
    },
    {
        id: 't5-q8',
        question: 'Hur matchar du rader som börjar med # med grep?',
        options: ['grep "#" fil', 'grep "^#" fil', 'grep "#$" fil', 'grep -# fil'],
        correctIndex: 1, // B
        explanation: '^# betyder "# i början av raden".',
        difficulty: 'G',
        category: 'grep'
    },
    {
        id: 't5-q9',
        question: 'Vad gör [^abc] i regex?',
        options: ['Matchar abc i början', 'Matchar allt utom a, b, c', 'Matchar ^abc', 'Syntax-fel'],
        correctIndex: 1, // B
        explanation: '[^...] är en negerad teckenklass som matchar allt UTOM angivna tecken.',
        difficulty: 'VG',
        category: 'Teckenklasser'
    },
    {
        id: 't5-q10',
        question: 'Vad gör | i regex?',
        options: ['Pipe', 'OR (alternativ)', 'AND', 'NOT'],
        correctIndex: 1, // B
        explanation: '| betyder OR - matchar antingen vänster eller höger sida.',
        difficulty: 'G',
        category: 'Operatorer'
    },
    {
        id: 't5-q11',
        question: 'Vad matchar a{3} i regex?',
        options: ['Tre valfria a', 'Minst tre a', 'Exakt tre a', 'Max tre a'],
        correctIndex: 2, // C
        explanation: '{n} matchar exakt n förekomster.',
        difficulty: 'VG',
        category: 'Kvantifierare'
    },
    {
        id: 't5-q12',
        question: 'Vad gör grep -v?',
        options: ['Verbose', 'Version', 'Invertera matchning', 'Validate'],
        correctIndex: 2, // C
        explanation: '-v inverterar matchningen och visar rader som INTE matchar.',
        difficulty: 'G',
        category: 'grep'
    },
    {
        id: 't5-q13',
        question: 'Hur matchar du tomma rader med grep?',
        options: ['grep "" fil', 'grep "^$" fil', 'grep " " fil', 'grep -empty fil'],
        correctIndex: 1, // B
        explanation: '^$ matchar rader där start (^) och slut ($) är samma = tom rad.',
        difficulty: 'VG',
        category: 'grep'
    },
    {
        id: 't5-q14',
        question: 'Vad gör grep -E?',
        options: ['Error mode', 'Extended regex', 'Exact match', 'Export'],
        correctIndex: 1, // B
        explanation: '-E aktiverar Extended Regular Expressions med +, ?, |, () utan escape.',
        difficulty: 'VG',
        category: 'grep'
    },
    {
        id: 't5-q15',
        question: 'Vad gör grep -n?',
        options: ['Antal matchningar', 'Visar radnummer', 'Negativ matchning', 'Numeric sort'],
        correctIndex: 1, // B
        explanation: '-n visar radnummer före varje matchande rad.',
        difficulty: 'G',
        category: 'grep'
    },
    {
        id: 't5-q16',
        question: 'Hur söker du rekursivt i kataloger med grep?',
        options: ['grep -a', 'grep -r', 'grep -s', 'grep -d'],
        correctIndex: 1, // B
        explanation: '-r (eller -R) söker rekursivt genom underkataloger.',
        difficulty: 'VG',
        category: 'grep'
    },
    {
        id: 't5-q17',
        question: 'Vad matchar colou?r i regex?',
        options: ['Endast colour', 'Endast color', 'color eller colour', 'colouur'],
        correctIndex: 2, // C
        explanation: '? gör föregående tecken valfritt - matchar med eller utan.',
        difficulty: 'VG',
        category: 'Kvantifierare'
    },
    {
        id: 't5-q18',
        question: 'Vad gör \\b i regex?',
        options: ['Backspace', 'Ordgräns (word boundary)', 'Backslash', 'Break'],
        correctIndex: 1, // B
        explanation: '\\b markerar ordgräns - \\bword\\b matchar hela ord.',
        difficulty: 'VG',
        category: 'Ankare'
    },
    {
        id: 't5-q19',
        question: 'Vad matchar [0-9]{1,3} i regex?',
        options: ['Exakt 3 siffror', '1 till 3 siffror', 'Siffran 1, 2 eller 3', 'Max 9 siffror'],
        correctIndex: 1, // B
        explanation: '{1,3} betyder mellan 1 och 3 förekomster av föregående.',
        difficulty: 'VG',
        category: 'Kvantifierare'
    },
    {
        id: 't5-q20',
        question: 'Vad gör grep -l?',
        options: ['Långa radnamn', 'Visa endast filnamn', 'Line count', 'List mode'],
        correctIndex: 1, // B
        explanation: '-l visar endast namnen på filer som innehåller matchningar.',
        difficulty: 'VG',
        category: 'grep'
    }
]

// =============================================================================
// TASK 6: SED - STREAM EDITOR (20 quiz questions)
// =============================================================================

const TASK_6_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't6-q1',
        question: 'Vad är sed?',
        options: ['Text editor', 'Stream Editor', 'System Editor', 'String Editor'],
        correctIndex: 1, // B
        explanation: 'sed står för Stream Editor och processar text rad för rad.',
        difficulty: 'G',
        category: 'Grundläggande'
    },
    {
        id: 't6-q2',
        question: 'Vad gör sed "s/old/new/" fil.txt?',
        options: ['Raderar old', 'Ersätter första old med new på varje rad', 'Söker efter old', 'Ersätter alla old'],
        correctIndex: 1, // B
        explanation: 's/old/new/ ersätter första förekomsten av old med new på varje rad.',
        difficulty: 'G',
        category: 'Substitution'
    },
    {
        id: 't6-q3',
        question: 'Vad gör g-flaggan i sed "s/old/new/g"?',
        options: ['Global search', 'Ersätt alla förekomster', 'Grep mode', 'Generate output'],
        correctIndex: 1, // B
        explanation: 'g (global) ersätter ALLA förekomster på varje rad, inte bara första.',
        difficulty: 'G',
        category: 'Flaggor'
    },
    {
        id: 't6-q4',
        question: 'Vad gör sed -i?',
        options: ['Interactive', 'In-place editing', 'Ignore case', 'Insert mode'],
        correctIndex: 1, // B
        explanation: '-i ändrar filen direkt (in-place) istället för att skriva till stdout.',
        difficulty: 'G',
        category: 'Flaggor'
    },
    {
        id: 't6-q5',
        question: 'Hur raderar du rader som innehåller "error" med sed?',
        options: ['sed "s/error//" fil', 'sed "/error/d" fil', 'sed "error" fil', 'sed -d error fil'],
        correctIndex: 1, // B
        explanation: 'd-kommandot raderar matchande rader. /pattern/d raderar rader med pattern.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't6-q6',
        question: 'Hur raderar du rad 5 med sed?',
        options: ['sed "5d" fil', 'sed "d5" fil', 'sed "-5" fil', 'sed "5" fil'],
        correctIndex: 0, // A
        explanation: 'Radnummer före d-kommandot anger vilken rad som ska raderas.',
        difficulty: 'G',
        category: 'Adressering'
    },
    {
        id: 't6-q7',
        question: 'Vad gör sed -n "5p" fil.txt?',
        options: ['Raderar rad 5', 'Visar endast rad 5', 'Printar 5 gånger', 'Visar rad 1-5'],
        correctIndex: 1, // B
        explanation: '-n suppress output, p printar. Tillsammans visas endast rad 5.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't6-q8',
        question: 'Hur raderar du tomma rader med sed?',
        options: ['sed "/^$/d" fil', 'sed "/empty/d" fil', 'sed "/ /d" fil', 'sed -blank fil'],
        correctIndex: 0, // A
        explanation: '^$ matchar tomma rader (start direkt följt av slut).',
        difficulty: 'VG',
        category: 'Mönster'
    },
    {
        id: 't6-q9',
        question: 'Hur gör du backup med sed -i?',
        options: ['sed -i -b fil', 'sed -i.bak fil', 'sed -backup fil', 'sed -i --save fil'],
        correctIndex: 1, // B
        explanation: 'sed -i.bak skapar en backup-fil med .bak extension före ändring.',
        difficulty: 'VG',
        category: 'Flaggor'
    },
    {
        id: 't6-q10',
        question: 'Hur använder du | som delimiter istället för /?',
        options: ['sed "s|old|new|" fil', 'sed -d "|" "s/old/new/" fil', 'sed "s/old/new/" -d | fil', 'Går inte'],
        correctIndex: 0, // A
        explanation: 'Vilket tecken som helst kan användas som delimiter efter s.',
        difficulty: 'VG',
        category: 'Syntax'
    },
    {
        id: 't6-q11',
        question: 'Hur raderar du rad 1-10 med sed?',
        options: ['sed "1,10d" fil', 'sed "1-10d" fil', 'sed "d1-10" fil', 'sed "-1 -10 d" fil'],
        correctIndex: 0, // A
        explanation: 'Kommaseparerad range 1,10 anger radintervall.',
        difficulty: 'VG',
        category: 'Adressering'
    },
    {
        id: 't6-q12',
        question: 'Hur kör du flera sed-kommandon?',
        options: ['sed "s/a/b/ s/c/d/" fil', 'sed -e "s/a/b/" -e "s/c/d/" fil', 'sed "s/a/b/" "s/c/d/" fil', 'sed --multi fil'],
        correctIndex: 1, // B
        explanation: '-e flaggan tillåter flera kommandon, eller separera med ;',
        difficulty: 'VG',
        category: 'Syntax'
    },
    {
        id: 't6-q13',
        question: 'Vad gör i-flaggan i sed "s/old/new/gi"?',
        options: ['Insert', 'In-place', 'Case insensitive', 'Interactive'],
        correctIndex: 2, // C
        explanation: 'i-flaggan (efter /) gör matchningen case insensitive.',
        difficulty: 'VG',
        category: 'Flaggor'
    },
    {
        id: 't6-q14',
        question: 'Hur ersätter du endast på rader som matchar "error"?',
        options: ['sed "s/error/s/old/new/" fil', 'sed "/error/s/old/new/" fil', 'sed "error s/old/new/" fil', 'sed -m error "s/old/new/" fil'],
        correctIndex: 1, // B
        explanation: '/pattern/ före s begränsar ersättningen till matchande rader.',
        difficulty: 'VG',
        category: 'Adressering'
    },
    {
        id: 't6-q15',
        question: 'Hur raderar du kommentarer (rader som börjar med #)?',
        options: ['sed "/#/d" fil', 'sed "/^#/d" fil', 'sed "s/#//" fil', 'sed "#d" fil'],
        correctIndex: 1, // B
        explanation: '^# matchar # i början av raden, d raderar hela raden.',
        difficulty: 'G',
        category: 'Mönster'
    },
    {
        id: 't6-q16',
        question: 'Vad gör sed -E eller sed -r?',
        options: ['Error mode', 'Extended regex', 'Recursive', 'Read mode'],
        correctIndex: 1, // B
        explanation: '-E/-r aktiverar Extended regex där +, ?, |, () inte behöver escape.',
        difficulty: 'VG',
        category: 'Flaggor'
    },
    {
        id: 't6-q17',
        question: 'Hur infogar du text före rad 1?',
        options: ['sed "0i text" fil', 'sed "1i\\text" fil', 'sed "insert 1 text" fil', 'sed "-i 1 text" fil'],
        correctIndex: 1, // B
        explanation: 'i-kommandot (insert) infogar text före angiven rad.',
        difficulty: 'VG',
        category: 'Kommandon'
    },
    {
        id: 't6-q18',
        question: 'Vad gör & i sed ersättning?',
        options: ['AND-operator', 'Hela matchningen', 'Append', 'Address'],
        correctIndex: 1, // B
        explanation: '& representerar hela den matchade strängen i ersättningen.',
        difficulty: 'VG',
        category: 'Avancerat'
    },
    {
        id: 't6-q19',
        question: 'Hur ersätter du endast andra förekomsten på varje rad?',
        options: ['sed "s/old/new/2" fil', 'sed "s2/old/new/" fil', 'sed "s/old/new/" -n 2 fil', 'sed "2s/old/new/" fil'],
        correctIndex: 0, // A
        explanation: 'Siffra efter sista / anger vilken förekomst som ska ersättas.',
        difficulty: 'VG',
        category: 'Flaggor'
    },
    {
        id: 't6-q20',
        question: 'Hur raderar du från rad 10 till slutet av filen?',
        options: ['sed "10-$d" fil', 'sed "10,$d" fil', 'sed "10:$d" fil', 'sed "10-end d" fil'],
        correctIndex: 1, // B
        explanation: '$ representerar sista raden, 10,$ är range från rad 10 till slut.',
        difficulty: 'VG',
        category: 'Adressering'
    }
]

// =============================================================================
// TASK 7: AWK - TEXTBEARBETNING (20 quiz questions)
// =============================================================================

const TASK_7_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't7-q1',
        question: 'Vad är awk?',
        options: ['Text editor', 'Kolumnbaserad textbearbetning', 'Filkomprimering', 'Nätverksverktyg'],
        correctIndex: 1, // B
        explanation: 'awk är ett verktyg för att processa text kolumnvis (fält för fält).',
        difficulty: 'G',
        category: 'Grundläggande'
    },
    {
        id: 't7-q2',
        question: 'Vad representerar $0 i awk?',
        options: ['Första fältet', 'Sista fältet', 'Hela raden', 'Radnummer'],
        correctIndex: 2, // C
        explanation: '$0 innehåller hela raden, medan $1, $2 etc är individuella fält.',
        difficulty: 'G',
        category: 'Fält'
    },
    {
        id: 't7-q3',
        question: 'Vad representerar $NF i awk?',
        options: ['Antal fält', 'Första fältet', 'Sista fältet', 'Radnummer'],
        correctIndex: 2, // C
        explanation: '$NF är sista fältet. NF = Number of Fields, $NF = värdet av sista.',
        difficulty: 'G',
        category: 'Fält'
    },
    {
        id: 't7-q4',
        question: 'Hur ändrar du fältseparatorn till : i awk?',
        options: ['awk -s ":" ...', 'awk -F: ...', 'awk --sep=":" ...', 'awk -d ":" ...'],
        correctIndex: 1, // B
        explanation: '-F anger field separator. awk -F: för kolon som separator.',
        difficulty: 'G',
        category: 'Syntax'
    },
    {
        id: 't7-q5',
        question: 'Vad gör NR i awk?',
        options: ['Number of Records (radnummer)', 'Next Record', 'No Result', 'New Row'],
        correctIndex: 0, // A
        explanation: 'NR håller reda på aktuellt radnummer under processning.',
        difficulty: 'G',
        category: 'Variabler'
    },
    {
        id: 't7-q6',
        question: 'Hur skriver du ut kolumn 1 och 3 med awk?',
        options: ['awk "{print $1 $3}" fil', 'awk "{print $1, $3}" fil', 'awk "$1 $3" fil', 'awk -c "1,3" fil'],
        correctIndex: 1, // B
        explanation: 'Komma mellan fält ger mellanslag i output.',
        difficulty: 'G',
        category: 'Syntax'
    },
    {
        id: 't7-q7',
        question: 'Vad gör NF (utan $) i awk?',
        options: ['Sista fältets värde', 'Antal fält på raden', 'Första fältet', 'Filnamn'],
        correctIndex: 1, // B
        explanation: 'NF = Number of Fields (antal). $NF = värdet av sista fältet.',
        difficulty: 'G',
        category: 'Variabler'
    },
    {
        id: 't7-q8',
        question: 'Vad gör BEGIN-blocket i awk?',
        options: ['Körs före varje rad', 'Körs en gång före första raden', 'Startar om processen', 'Nollställer variabler'],
        correctIndex: 1, // B
        explanation: 'BEGIN körs EN gång innan någon rad processas.',
        difficulty: 'VG',
        category: 'Block'
    },
    {
        id: 't7-q9',
        question: 'Vad gör END-blocket i awk?',
        options: ['Avslutar programmet', 'Körs efter varje rad', 'Körs en gång efter sista raden', 'Felhantering'],
        correctIndex: 2, // C
        explanation: 'END körs EN gång efter att alla rader har processats.',
        difficulty: 'VG',
        category: 'Block'
    },
    {
        id: 't7-q10',
        question: 'Hur summerar du kolumn 1 med awk?',
        options: ['awk "{sum($1)}"', 'awk "{sum += $1} END {print sum}"', 'awk "SUM $1"', 'awk -sum 1'],
        correctIndex: 1, // B
        explanation: 'Ackumulera i variabel per rad, skriv ut summan i END.',
        difficulty: 'VG',
        category: 'Beräkning'
    },
    {
        id: 't7-q11',
        question: 'Hur filtrerar du rader där kolumn 3 > 100?',
        options: ['awk "$3 > 100" fil', 'awk "if $3 > 100" fil', 'awk -filter "$3>100" fil', 'awk "{$3 > 100}" fil'],
        correctIndex: 0, // A
        explanation: 'Villkor utan {} fungerar som filter - visa matchande rader.',
        difficulty: 'VG',
        category: 'Filtrering'
    },
    {
        id: 't7-q12',
        question: 'Hur hoppar du över första raden (header) i awk?',
        options: ['awk "SKIP 1" fil', 'awk "NR > 1" fil', 'awk "{next}" fil', 'awk -h fil'],
        correctIndex: 1, // B
        explanation: 'NR > 1 matchar alla rader utom den första.',
        difficulty: 'VG',
        category: 'Filtrering'
    },
    {
        id: 't7-q13',
        question: 'Hur räknar du antal rader med awk?',
        options: ['awk "COUNT" fil', 'awk "{count++}" fil', 'awk "END {print NR}" fil', 'awk -c fil'],
        correctIndex: 2, // C
        explanation: 'NR i END-blocket innehåller totala antalet processade rader.',
        difficulty: 'VG',
        category: 'Beräkning'
    },
    {
        id: 't7-q14',
        question: 'Vad gör OFS i awk?',
        options: ['Original Field Separator', 'Output Field Separator', 'Optional Field', 'Object Format'],
        correctIndex: 1, // B
        explanation: 'OFS definierar vad som skrivs mellan fält i output.',
        difficulty: 'VG',
        category: 'Variabler'
    },
    {
        id: 't7-q15',
        question: 'Hur hittar du unika värden i kolumn 1 med awk?',
        options: ['awk "UNIQUE $1" fil', 'awk "!seen[$1]++" fil', 'awk "{unique($1)}" fil', 'awk -u 1 fil'],
        correctIndex: 1, // B
        explanation: '!seen[$1]++ använder associativ array för att tracka sedda värden.',
        difficulty: 'VG',
        category: 'Avancerat'
    },
    {
        id: 't7-q16',
        question: 'Hur använder du printf i awk för formaterad output?',
        options: ['awk "{format $1}" fil', 'awk "{printf "%s", $1}" fil', 'awk -f "%s" fil', 'awk "{print -f $1}" fil'],
        correctIndex: 1, // B
        explanation: 'printf fungerar som i C - formatsträngar med %s, %d, etc.',
        difficulty: 'VG',
        category: 'Formatering'
    },
    {
        id: 't7-q17',
        question: 'Hur kör du awk med mönstermatchning?',
        options: ['awk "match /error/" fil', 'awk "/error/ {print}" fil', 'awk -m "error" fil', 'awk "{grep error}" fil'],
        correctIndex: 1, // B
        explanation: '/pattern/ före {} matchar rader som innehåller pattern.',
        difficulty: 'VG',
        category: 'Filtrering'
    },
    {
        id: 't7-q18',
        question: 'Hur definierar du en variabel utifrån i awk?',
        options: ['awk "var=100" fil', 'awk -v var=100 "{print var}" fil', 'awk --set var=100 fil', 'awk "{var=100}" fil'],
        correctIndex: 1, // B
        explanation: '-v variabel=värde sätter variabel innan processning.',
        difficulty: 'VG',
        category: 'Variabler'
    },
    {
        id: 't7-q19',
        question: 'Vad gör FILENAME i awk?',
        options: ['Sätter filnamn', 'Innehåller nuvarande filnamn', 'Filter på filnamn', 'Felmeddelande'],
        correctIndex: 1, // B
        explanation: 'FILENAME innehåller namnet på filen som just nu processas.',
        difficulty: 'VG',
        category: 'Variabler'
    },
    {
        id: 't7-q20',
        question: 'Hur grupperar och räknar du förekomster med awk?',
        options: ['awk "GROUP BY $1" fil', 'awk "{count[$1]++} END {for (k in count) print k, count[k]}" fil', 'awk -g 1 fil', 'awk "{group($1)}" fil'],
        correctIndex: 1, // B
        explanation: 'Associativ array räknar per nyckel, loop i END skriver ut.',
        difficulty: 'VG',
        category: 'Avancerat'
    }
]

// =============================================================================
// TASK 8: VILLKOR (IF/ELSE) (20 quiz questions)
// =============================================================================

const TASK_8_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't8-q1',
        question: 'Hur avslutar du ett if-block i bash?',
        options: ['end', 'endif', 'fi', '}'],
        correctIndex: 2, // C
        explanation: 'fi avslutar if-satser i bash (if baklänges).',
        difficulty: 'G',
        category: 'Syntax'
    },
    {
        id: 't8-q2',
        question: 'Varför behövs mellanslag i [ $x = 5 ]?',
        options: ['Estetik', '[ är ett kommando', 'Bash-bugg', 'Behövs inte'],
        correctIndex: 1, // B
        explanation: '[ är faktiskt ett kommando (alias för test), så mellanslag är obligatoriskt.',
        difficulty: 'G',
        category: 'Syntax'
    },
    {
        id: 't8-q3',
        question: 'Hur testar du om en fil existerar?',
        options: ['[ -e fil ]', '[ exists fil ]', '[ fil ]', '[ ? fil ]'],
        correctIndex: 0, // A
        explanation: '-e testar om filen existerar (exists).',
        difficulty: 'G',
        category: 'Filtest'
    },
    {
        id: 't8-q4',
        question: 'Hur testar du om något är en katalog?',
        options: ['[ -f path ]', '[ -d path ]', '[ dir path ]', '[ folder path ]'],
        correctIndex: 1, // B
        explanation: '-d testar om path är en katalog (directory).',
        difficulty: 'G',
        category: 'Filtest'
    },
    {
        id: 't8-q5',
        question: 'Hur testar du om en sträng är tom?',
        options: ['[ -e "$str" ]', '[ -z "$str" ]', '[ empty "$str" ]', '[ "$str" = "" ]'],
        correctIndex: 1, // B
        explanation: '-z testar om strängen har zero length (tom).',
        difficulty: 'G',
        category: 'Strängar'
    },
    {
        id: 't8-q6',
        question: 'Hur testar du om $a är lika med $b (numeriskt)?',
        options: ['[ $a = $b ]', '[ $a -eq $b ]', '[ $a == $b ]', '[ $a equals $b ]'],
        correctIndex: 1, // B
        explanation: '-eq (equal) används för numerisk jämförelse.',
        difficulty: 'G',
        category: 'Numeriskt'
    },
    {
        id: 't8-q7',
        question: 'Hur testar du om $x är större än 10?',
        options: ['[ $x > 10 ]', '[ $x -gt 10 ]', '[ $x greater 10 ]', '[ $x >> 10 ]'],
        correctIndex: 1, // B
        explanation: '-gt (greater than) används. > är redirect i shell!',
        difficulty: 'G',
        category: 'Numeriskt'
    },
    {
        id: 't8-q8',
        question: 'Hur testar du om $x är mindre än 5?',
        options: ['[ $x < 5 ]', '[ $x -lt 5 ]', '[ $x less 5 ]', '[ $x -less 5 ]'],
        correctIndex: 1, // B
        explanation: '-lt (less than) används för "mindre än".',
        difficulty: 'G',
        category: 'Numeriskt'
    },
    {
        id: 't8-q9',
        question: 'Vad gör -ne i test?',
        options: ['New equal', 'Not equal', 'Numeric equal', 'Next'],
        correctIndex: 1, // B
        explanation: '-ne (not equal) testar om värden är olika.',
        difficulty: 'G',
        category: 'Numeriskt'
    },
    {
        id: 't8-q10',
        question: 'Hur testar du om fil är läsbar?',
        options: ['[ -r fil ]', '[ -read fil ]', '[ readable fil ]', '[ -R fil ]'],
        correctIndex: 0, // A
        explanation: '-r testar om filen är läsbar (readable).',
        difficulty: 'G',
        category: 'Filtest'
    },
    {
        id: 't8-q11',
        question: 'Vad gör -ge i test?',
        options: ['Get equal', 'Greater or equal', 'General equal', 'Global'],
        correctIndex: 1, // B
        explanation: '-ge (greater or equal) testar >=.',
        difficulty: 'VG',
        category: 'Numeriskt'
    },
    {
        id: 't8-q12',
        question: 'Hur kombinerar du två villkor med AND?',
        options: ['[ a AND b ]', '[ a ] && [ b ]', '[ a + b ]', '[ a & b ]'],
        correctIndex: 1, // B
        explanation: '&& mellan separata test-kommandon för AND.',
        difficulty: 'VG',
        category: 'Logik'
    },
    {
        id: 't8-q13',
        question: 'Hur kombinerar du två villkor med OR?',
        options: ['[ a OR b ]', '[ a ] || [ b ]', '[ a | b ]', '[ a -or b ]'],
        correctIndex: 1, // B
        explanation: '|| mellan separata test-kommandon för OR.',
        difficulty: 'VG',
        category: 'Logik'
    },
    {
        id: 't8-q14',
        question: 'Hur negerar du ett villkor?',
        options: ['[ NOT x ]', '[ !x ]', '[ ! x ]', '[ -not x ]'],
        correctIndex: 2, // C
        explanation: '! före villkoret negerar det. Mellanslag behövs!',
        difficulty: 'VG',
        category: 'Logik'
    },
    {
        id: 't8-q15',
        question: 'Vad testar [ -s fil ]?',
        options: ['Fil är symbolic link', 'Fil existerar och har storlek > 0', 'Fil är speciell', 'Fil är säker'],
        correctIndex: 1, // B
        explanation: '-s (size) testar att fil finns OCH inte är tom.',
        difficulty: 'VG',
        category: 'Filtest'
    },
    {
        id: 't8-q16',
        question: 'Skillnad mellan [ ] och [[ ]]?',
        options: ['Ingen skillnad', '[[ ]] är bash-specifikt med fler funktioner', '[ ] är nyare', '[[ ]] är långsammare'],
        correctIndex: 1, // B
        explanation: '[[ ]] är bash-specifikt, stödjer &&, || inuti och regex.',
        difficulty: 'VG',
        category: 'Avancerat'
    },
    {
        id: 't8-q17',
        question: 'Hur använder du regex i villkor?',
        options: ['[ $str ~ regex ]', '[[ $str =~ regex ]]', '[ regex $str ]', '[ -r $str regex ]'],
        correctIndex: 1, // B
        explanation: '=~ i [[ ]] används för regex-matchning.',
        difficulty: 'VG',
        category: 'Avancerat'
    },
    {
        id: 't8-q18',
        question: 'Vad gör (( )) i bash?',
        options: ['Subshell', 'Aritmetisk kontext', 'Gruppering', 'Array'],
        correctIndex: 1, // B
        explanation: '(( )) tillåter vanlig aritmetisk syntax: (( x > 5 ))',
        difficulty: 'VG',
        category: 'Avancerat'
    },
    {
        id: 't8-q19',
        question: 'Hur testar du om fil1 är nyare än fil2?',
        options: ['[ fil1 -newer fil2 ]', '[ fil1 -nt fil2 ]', '[ fil1 > fil2 ]', '[ newer fil1 fil2 ]'],
        correctIndex: 1, // B
        explanation: '-nt (newer than) jämför modifieringstider.',
        difficulty: 'VG',
        category: 'Filtest'
    },
    {
        id: 't8-q20',
        question: 'Hur testar du om en variabel är satt (bash 4.2+)?',
        options: ['[ -e $var ]', '[ -v var ]', '[ -set var ]', '[ defined var ]'],
        correctIndex: 1, // B
        explanation: '-v testar om variabeln är satt (defined).',
        difficulty: 'VG',
        category: 'Avancerat'
    },
    // SCENARIO-BASERADE FRÅGOR
    {
        id: 't8-s1',
        question: 'Skriptet ger "[: -eq: unary operator expected". Vad är troligaste felet?',
        options: ['Syntaxfel i jämförelse', 'Variabeln är tom - bör citeras', 'Fel operator', '-eq finns inte'],
        correctIndex: 1, // B
        explanation: 'Om $var är tom blir [ $var -eq 5 ] till [ -eq 5 ]. Citera: [ "$var" -eq 5 ].',
        difficulty: 'VG',
        category: 'Felsökning',
        scenario: 'Ditt skript kraschar på ett if-statement.',
        isScenario: true
    },
    {
        id: 't8-s2',
        question: 'Du vill kolla om filen /etc/config finns. Vilket test använder du?',
        options: ['[ -e /etc/config ]', '[ -f /etc/config ]', '[ -r /etc/config ]', 'Alla ovan fungerar'],
        correctIndex: 3, // D
        explanation: '-e = exists, -f = regular file, -r = readable. Alla fungerar, men -f är säkrast för filer.',
        difficulty: 'G',
        category: 'Praktisk',
        scenario: 'Du skriver ett setup-skript som behöver en config-fil.',
        isScenario: true
    },
    {
        id: 't8-s3',
        question: 'if [ $status = "ok" ] && [ $count -gt 0 ]; then... Vad händer om status är tom?',
        options: ['Fungerar fint', 'Syntaxfel - too many arguments', 'Hoppar till else', 'Kör if-blocket ändå'],
        correctIndex: 1, // B
        explanation: 'Tom $status blir [ = "ok" ] = syntaxfel. Citera: [ "$status" = "ok" ].',
        difficulty: 'VG',
        category: 'Felsökning',
        scenario: 'Skriptet fungerar ibland men kraschar oregelbundet.',
        isScenario: true
    }
]

// =============================================================================
// EXPORT
// =============================================================================
// TASK 9: INTERAKTIVA SKRIPT (20 quiz questions)
// =============================================================================

const TASK_9_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't9-q1',
        question: 'Hur läser du input från användaren i bash?',
        options: ['input variabel', 'read variabel', 'get variabel', 'scan variabel'],
        correctIndex: 1, // B
        explanation: 'read läser en rad input och sparar i angiven variabel.',
        difficulty: 'G',
        category: 'read'
    },
    {
        id: 't9-q2',
        question: 'Hur visar du en prompt med read?',
        options: ['read --prompt "Text" var', 'read -p "Text" var', 'read "Text" var', 'prompt "Text"; read var'],
        correctIndex: 1, // B
        explanation: '-p (prompt) visar text före input.',
        difficulty: 'G',
        category: 'read'
    },
    {
        id: 't9-q3',
        question: 'Hur läser du lösenord utan att visa det?',
        options: ['read -h var', 'read -s var', 'read --hidden var', 'read -p var'],
        correctIndex: 1, // B
        explanation: '-s (silent) döljer input - perfekt för lösenord.',
        difficulty: 'G',
        category: 'read'
    },
    {
        id: 't9-q4',
        question: 'Hur sätter du timeout på read (10 sekunder)?',
        options: ['read -w 10 var', 'read -t 10 var', 'read --timeout=10 var', 'timeout 10 read var'],
        correctIndex: 1, // B
        explanation: '-t anger timeout i sekunder.',
        difficulty: 'G',
        category: 'read'
    },
    {
        id: 't9-q5',
        question: 'Vad gör select i bash?',
        options: ['Väljer filer', 'Skapar numrerad meny', 'Selekterar text', 'Väljer databas'],
        correctIndex: 1, // B
        explanation: 'select skapar automatiskt en numrerad meny för användaren.',
        difficulty: 'G',
        category: 'select'
    },
    {
        id: 't9-q6',
        question: 'Hur avslutar du en select-loop?',
        options: ['exit', 'break', 'quit', 'end'],
        correctIndex: 1, // B
        explanation: 'break avslutar loopen och fortsätter efter done.',
        difficulty: 'G',
        category: 'select'
    },
    {
        id: 't9-q7',
        question: 'Hur avslutar du ett case-block?',
        options: ['end case', 'done', 'esac', ';;'],
        correctIndex: 2, // C
        explanation: 'esac avslutar case (case baklänges).',
        difficulty: 'G',
        category: 'case'
    },
    {
        id: 't9-q8',
        question: 'Vad gör ;; i case?',
        options: ['Kommentar', 'Fortsätt till nästa', 'Avsluta case-block', 'Avsluta pattern'],
        correctIndex: 3, // D
        explanation: ';; avslutar ett pattern-block och hoppar till esac.',
        difficulty: 'G',
        category: 'case'
    },
    {
        id: 't9-q9',
        question: 'Hur hanterar du "default" i case?',
        options: ['default)', 'else)', '*)', 'other)'],
        correctIndex: 2, // C
        explanation: '*) matchar allt annat som inte matchats tidigare.',
        difficulty: 'G',
        category: 'case'
    },
    {
        id: 't9-q10',
        question: 'Hur läser du input till en array?',
        options: ['read -l array', 'read -a array', 'read --array array', 'read [] array'],
        correctIndex: 1, // B
        explanation: '-a läser input och splittar på IFS till array.',
        difficulty: 'VG',
        category: 'read'
    },
    {
        id: 't9-q11',
        question: 'Hur begränsar du input till 1 tecken?',
        options: ['read -c 1 var', 'read -n 1 var', 'read -1 var', 'read --char var'],
        correctIndex: 1, // B
        explanation: '-n anger max antal tecken att läsa.',
        difficulty: 'VG',
        category: 'read'
    },
    {
        id: 't9-q12',
        question: 'Vad gör read -r?',
        options: ['Recursive', 'Raw (ingen escape-tolkning)', 'Required', 'Retry'],
        correctIndex: 1, // B
        explanation: '-r läser raw input utan att tolka backslash.',
        difficulty: 'VG',
        category: 'read'
    },
    {
        id: 't9-q13',
        question: 'Vad är IFS i bash?',
        options: ['Input File System', 'Internal Field Separator', 'Initial Field String', 'Input Format Standard'],
        correctIndex: 1, // B
        explanation: 'IFS definierar hur input splittas - default är space/tab/newline.',
        difficulty: 'VG',
        category: 'Variabler'
    },
    {
        id: 't9-q14',
        question: 'Hur ändrar du select-prompten?',
        options: ['SELECT_PROMPT=', 'PS3=', 'PROMPT=', 'SP='],
        correctIndex: 1, // B
        explanation: 'PS3 är prompten som visas i select-menyn.',
        difficulty: 'VG',
        category: 'select'
    },
    {
        id: 't9-q15',
        question: 'Hur matchar du flera patterns i case?',
        options: ['a AND b)', 'a, b)', 'a|b)', 'a b)'],
        correctIndex: 2, // C
        explanation: '| separerar alternativa patterns i case.',
        difficulty: 'VG',
        category: 'case'
    },
    {
        id: 't9-q16',
        question: 'Hur validerar du att input är ett nummer?',
        options: ['[ -n "$var" ]', '[[ $var =~ ^[0-9]+$ ]]', '[ $var -gt 0 ]', 'test -num $var'],
        correctIndex: 1, // B
        explanation: 'Regex i [[ ]] kontrollerar att input endast är siffror.',
        difficulty: 'VG',
        category: 'Validering'
    },
    {
        id: 't9-q17',
        question: 'Vad innehåller $REPLY efter read utan variabel?',
        options: ['Ingenting', 'Användarens input', 'Exit code', 'Prompt-text'],
        correctIndex: 1, // B
        explanation: 'Om ingen variabel anges sparas input i REPLY.',
        difficulty: 'VG',
        category: 'read'
    },
    {
        id: 't9-q18',
        question: 'Hur läser du tangent utan att behöva trycka Enter?',
        options: ['read -i var', 'read -n 1 var', 'read --noenter var', 'read -e var'],
        correctIndex: 1, // B
        explanation: '-n 1 läser exakt ett tecken utan att vänta på Enter.',
        difficulty: 'VG',
        category: 'read'
    },
    {
        id: 't9-q19',
        question: 'Hur sätter du default-värde om input är tom?',
        options: ['read -d "default" var', 'var=${var:-default}', 'read --default="default" var', 'var = default || read var'],
        correctIndex: 1, // B
        explanation: 'Parameter expansion ${var:-default} ger default om tom.',
        difficulty: 'VG',
        category: 'Validering'
    },
    {
        id: 't9-q20',
        question: 'Vad gör ;& i case (bash 4+)?',
        options: ['Avsluta case', 'Fall through till nästa pattern', 'Kommentar', 'Fel syntax'],
        correctIndex: 1, // B
        explanation: ';& fortsätter till nästa pattern utan att testa det.',
        difficulty: 'VG',
        category: 'case'
    }
]

// =============================================================================
// TASK 10: LOOPAR (FOR/WHILE) (20 quiz questions)
// =============================================================================

const TASK_10_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't10-q1',
        question: 'Grundläggande for-loop syntax i bash?',
        options: ['for (i in list)', 'for i in list; do', 'foreach i list', 'for i = list'],
        correctIndex: 1, // B
        explanation: 'for variabel in lista; do ... done är bash-syntax.',
        difficulty: 'G',
        category: 'for'
    },
    {
        id: 't10-q2',
        question: 'Hur loopar du genom siffror 1-5?',
        options: ['for i in 1-5', 'for i in {1..5}', 'for i in (1,5)', 'for i = 1 to 5'],
        correctIndex: 1, // B
        explanation: '{start..slut} är brace expansion för sekvenser.',
        difficulty: 'G',
        category: 'for'
    },
    {
        id: 't10-q3',
        question: 'Hur loopar du genom alla .txt-filer?',
        options: ['for f in *.txt', 'for f in txt files', 'foreach *.txt as f', 'for f = *.txt'],
        correctIndex: 0, // A
        explanation: 'Glob-mönster expanderas automatiskt i for-loopar.',
        difficulty: 'G',
        category: 'for'
    },
    {
        id: 't10-q4',
        question: 'Grundläggande while-loop syntax?',
        options: ['while condition', 'while [ condition ]; do', 'while (condition)', 'loop while condition'],
        correctIndex: 1, // B
        explanation: 'while [ villkor ]; do ... done är korrekt syntax.',
        difficulty: 'G',
        category: 'while'
    },
    {
        id: 't10-q5',
        question: 'Hur gör du en oändlig loop?',
        options: ['while forever', 'while true; do', 'infinite loop', 'for ever'],
        correctIndex: 1, // B
        explanation: 'while true (eller while :) skapar oändlig loop.',
        difficulty: 'G',
        category: 'while'
    },
    {
        id: 't10-q6',
        question: 'Hur avbryter du en loop?',
        options: ['exit', 'break', 'stop', 'end'],
        correctIndex: 1, // B
        explanation: 'break avslutar loopen helt.',
        difficulty: 'G',
        category: 'Kontroll'
    },
    {
        id: 't10-q7',
        question: 'Hur hoppar du till nästa iteration?',
        options: ['next', 'continue', 'skip', 'pass'],
        correctIndex: 1, // B
        explanation: 'continue hoppar över resten och börjar nästa varv.',
        difficulty: 'G',
        category: 'Kontroll'
    },
    {
        id: 't10-q8',
        question: 'Skillnad mellan while och until?',
        options: ['Ingen skillnad', 'while kör medan sant, until kör tills sant', 'until är snabbare', 'while är deprecated'],
        correctIndex: 1, // B
        explanation: 'while kör så länge villkor är sant, until tills det blir sant.',
        difficulty: 'G',
        category: 'Loop-typer'
    },
    {
        id: 't10-q9',
        question: 'Hur loopar du med steg 2 (0, 2, 4, 6)?',
        options: ['for i in {0..6} step 2', 'for i in {0..6..2}', 'for i in 0-6/2', 'for i = 0; i += 2'],
        correctIndex: 1, // B
        explanation: '{start..slut..steg} anger steglängd i brace expansion.',
        difficulty: 'VG',
        category: 'for'
    },
    {
        id: 't10-q10',
        question: 'C-style for-loop i bash?',
        options: ['for (i=0; i<5; i++)', 'for ((i=0; i<5; i++))', 'for [i=0; i<5; i++]', 'for i=0:5:1'],
        correctIndex: 1, // B
        explanation: 'Dubbla parenteser (( )) tillåter C-style syntax.',
        difficulty: 'VG',
        category: 'for'
    },
    {
        id: 't10-q11',
        question: 'Hur läser du fil rad för rad?',
        options: ['for line in file.txt', 'while read line; do ... done < file.txt', 'cat file.txt | for line', 'read file.txt into lines'],
        correctIndex: 1, // B
        explanation: 'while read med redirect är bästa metoden.',
        difficulty: 'VG',
        category: 'while'
    },
    {
        id: 't10-q12',
        question: 'Hur ökar du en variabel i loop?',
        options: ['i++', '((i++))', 'i += 1', 'Alla fungerar'],
        correctIndex: 1, // B
        explanation: '((i++)) är korrekt syntax för inkrement i bash.',
        difficulty: 'VG',
        category: 'while'
    },
    {
        id: 't10-q13',
        question: 'Hur avbryter du 2 nivåer av nästlade loopar?',
        options: ['break break', 'break 2', 'exit 2', 'break --levels=2'],
        correctIndex: 1, // B
        explanation: 'break N avbryter N nivåer av nästlade loopar.',
        difficulty: 'VG',
        category: 'Kontroll'
    },
    {
        id: 't10-q14',
        question: 'Hur loopar du genom array-element?',
        options: ['for e in $array', 'for e in "${array[@]}"', 'for e in array[]', 'foreach array as e'],
        correctIndex: 1, // B
        explanation: '"${array[@]}" expanderar till alla element korrekt.',
        difficulty: 'VG',
        category: 'for'
    },
    {
        id: 't10-q15',
        question: 'Hur loopar du baklänges (5,4,3,2,1)?',
        options: ['for i in {5..1} --reverse', 'for i in {5..1}', 'for i in reverse(1..5)', 'for i in 5-1'],
        correctIndex: 1, // B
        explanation: '{start..slut} fungerar även baklänges.',
        difficulty: 'VG',
        category: 'for'
    },
    {
        id: 't10-q16',
        question: 'Problem med: cat fil | while read line; do count=$((count+1)); done?',
        options: ['Syntax-fel', 'while körs i subshell - count försvinner', 'Filen läses fel', 'Inget problem'],
        correctIndex: 1, // B
        explanation: 'Pipe skapar subshell - variabeländringar påverkar inte parent.',
        difficulty: 'VG',
        category: 'Avancerat'
    },
    {
        id: 't10-q17',
        question: 'Hur undviker du subshell-problemet med pipe?',
        options: ['Går inte', 'while read ... done < <(kommando)', 'while read | kommando', 'kommando >> while'],
        correctIndex: 1, // B
        explanation: 'Process substitution < <(cmd) undviker subshell.',
        difficulty: 'VG',
        category: 'Avancerat'
    },
    {
        id: 't10-q18',
        question: 'Hur kör du loop-iterationer parallellt?',
        options: ['for i in ...; do cmd & done', 'parallel for', 'for -j4 i in ...', 'async for'],
        correctIndex: 0, // A
        explanation: '& i bakgrunden startar processer parallellt.',
        difficulty: 'VG',
        category: 'Avancerat'
    },
    {
        id: 't10-q19',
        question: 'Hur väntar du på alla bakgrundsprocesser?',
        options: ['sync', 'wait', 'join', 'finish'],
        correctIndex: 1, // B
        explanation: 'wait väntar på alla bakgrundsprocesser.',
        difficulty: 'VG',
        category: 'Avancerat'
    },
    {
        id: 't10-q20',
        question: 'Hur loopar du rekursivt genom alla filer?',
        options: ['for f in -r *', 'shopt -s globstar; for f in **/*', 'for f in recurse(*)', 'find | for'],
        correctIndex: 1, // B
        explanation: 'globstar möjliggör ** för rekursiv matchning.',
        difficulty: 'VG',
        category: 'Avancerat'
    }
]

// =============================================================================
// TASK 11: SKRIPTPARAMETRAR (20 quiz questions)
// =============================================================================

const TASK_11_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't11-q1',
        question: 'Vad innehåller $0 i ett skript?',
        options: ['Första argumentet', 'Skriptets namn', 'Exit-kod', 'Antal argument'],
        correctIndex: 1, // B
        explanation: '$0 innehåller skriptets namn eller sökväg.',
        difficulty: 'G',
        category: 'Positionella'
    },
    {
        id: 't11-q2',
        question: 'Vad innehåller $# i ett skript?',
        options: ['Första argumentet', 'Alla argument', 'Antal argument', 'Skriptets PID'],
        correctIndex: 2, // C
        explanation: '$# ger antalet argument som skickades till skriptet.',
        difficulty: 'G',
        category: 'Specialvariabler'
    },
    {
        id: 't11-q3',
        question: 'Vad gör kommandot shift?',
        options: ['Sorterar argument', 'Flyttar $2→$1, $3→$2 osv', 'Skiftar till versaler', 'Byter användare'],
        correctIndex: 1, // B
        explanation: 'shift tar bort $1 och flyttar alla andra ett steg.',
        difficulty: 'G',
        category: 'shift'
    },
    {
        id: 't11-q4',
        question: 'Vad innehåller $? efter ett kommando?',
        options: ['Senaste argumentet', 'Exit-koden', 'Kommandot själv', 'Antal processer'],
        correctIndex: 1, // B
        explanation: '$? innehåller exit-koden (0=lyckat, annat=fel).',
        difficulty: 'G',
        category: 'Specialvariabler'
    },
    {
        id: 't11-q5',
        question: 'Vad innehåller $$?',
        options: ['Senaste exit-kod', 'Skriptets PID', 'Alla argument', 'Parent PID'],
        correctIndex: 1, // B
        explanation: '$$ är skriptets process-ID.',
        difficulty: 'G',
        category: 'Specialvariabler'
    },
    {
        id: 't11-q6',
        question: 'Hur får du alla argument som separata ord?',
        options: ['$*', '$@', '$#', '$0'],
        correctIndex: 1, // B
        explanation: '"$@" bevarar varje argument som separat ord.',
        difficulty: 'G',
        category: 'Specialvariabler'
    },
    {
        id: 't11-q7',
        question: 'Vad gör ${1:-default}?',
        options: ['Subtraherar', 'Ger default om $1 saknas', 'Tar bort default', 'Jämför med default'],
        correctIndex: 1, // B
        explanation: '${var:-default} returnerar default om variabeln är tom/odefinierad.',
        difficulty: 'G',
        category: 'Default'
    },
    {
        id: 't11-q8',
        question: 'Vad innehåller $!?',
        options: ['Senaste fel', 'PID för bakgrundsprocess', 'Negation', 'Senaste argument'],
        correctIndex: 1, // B
        explanation: '$! ger PID för senaste bakgrundsprocess.',
        difficulty: 'G',
        category: 'Specialvariabler'
    },
    {
        id: 't11-q9',
        question: 'Skillnad mellan "$@" och "$*"?',
        options: ['Ingen skillnad', '$@ separata ord, $* en sträng', '$* separata ord, $@ en sträng', '$@ bara positiva'],
        correctIndex: 1, // B
        explanation: '"$@" bevarar varje arg separat, "$*" slår ihop till en sträng.',
        difficulty: 'VG',
        category: 'Specialvariabler'
    },
    {
        id: 't11-q10',
        question: 'Hur shiftar du 3 steg på en gång?',
        options: ['shift shift shift', 'shift 3', 'shift -n 3', 'shift --steps=3'],
        correctIndex: 1, // B
        explanation: 'shift N tar bort N första argumenten.',
        difficulty: 'VG',
        category: 'shift'
    },
    {
        id: 't11-q11',
        question: 'Vad är getopts?',
        options: ['Hämta optioner', 'Inbyggd flagg-parser', 'Get options-fil', 'GNU options'],
        correctIndex: 1, // B
        explanation: 'getopts är inbyggt kommando för att parsa korta flaggor.',
        difficulty: 'VG',
        category: 'getopts'
    },
    {
        id: 't11-q12',
        question: 'Vad betyder : efter bokstav i getopts "f:"?',
        options: ['Flaggan är valfri', 'Flaggan kräver argument', 'Flaggan är deprecated', 'Flaggan ger verbose'],
        correctIndex: 1, // B
        explanation: ': betyder att flaggan kräver ett argument.',
        difficulty: 'VG',
        category: 'getopts'
    },
    {
        id: 't11-q13',
        question: 'Vad innehåller OPTARG i getopts?',
        options: ['Optionens namn', 'Argument till flaggan', 'Antal optioner', 'Option index'],
        correctIndex: 1, // B
        explanation: 'OPTARG innehåller argumentet som gavs till flaggan.',
        difficulty: 'VG',
        category: 'getopts'
    },
    {
        id: 't11-q14',
        question: 'Vad innehåller OPTIND?',
        options: ['Option index', 'Nästa argument att processa', 'Antal flaggor', 'Option indentation'],
        correctIndex: 1, // B
        explanation: 'OPTIND är index för nästa argument efter flaggorna.',
        difficulty: 'VG',
        category: 'getopts'
    },
    {
        id: 't11-q15',
        question: 'Hur hanterar du okänd flagga i getopts?',
        options: ['default)', 'unknown)', '\\?)', '*?)'],
        correctIndex: 2, // C
        explanation: '\\?) fångar okända flaggor i case-satsen.',
        difficulty: 'VG',
        category: 'getopts'
    },
    {
        id: 't11-q16',
        question: 'Hur får du återstående args efter getopts?',
        options: ['$REST', 'shift $OPTIND', 'shift $((OPTIND-1))', 'getopts --rest'],
        correctIndex: 2, // C
        explanation: 'shift $((OPTIND-1)) tar bort processade flaggor.',
        difficulty: 'VG',
        category: 'getopts'
    },
    {
        id: 't11-q17',
        question: 'Hur parsar du --help (lång flagga)?',
        options: ['getopts "--help"', 'case $1 in --help)', 'getopts stödjer det ej', 'Både B och C'],
        correctIndex: 3, // D
        explanation: 'getopts stödjer ej långa flaggor - använd case eller getopt.',
        difficulty: 'VG',
        category: 'Långa flaggor'
    },
    {
        id: 't11-q18',
        question: 'Vad gör set -- "a" "b"?',
        options: ['Sätter variabler', 'Ersätter $1, $2 med nya värden', 'Skapar array', 'Sätter options'],
        correctIndex: 1, // B
        explanation: 'set -- ersätter positionella parametrar med nya värden.',
        difficulty: 'VG',
        category: 'set'
    },
    {
        id: 't11-q19',
        question: 'Hur validerar du att argument är en fil?',
        options: ['[ -f "$1" ]', '[ -d "$1" ]', '[ -e "$1" ]', 'file "$1"'],
        correctIndex: 0, // A
        explanation: '[ -f ] testar om argumentet är en vanlig fil.',
        difficulty: 'VG',
        category: 'Validering'
    },
    {
        id: 't11-q20',
        question: 'Vad gör ${1:?Felmeddelande}?',
        options: ['Ger frågetecken', 'Avslutar om $1 saknas', 'Frågar användaren', 'Returnerar null'],
        correctIndex: 1, // B
        explanation: ':? ger felmeddelande och avslutar om variabeln saknas.',
        difficulty: 'VG',
        category: 'Validering'
    }
]

// =============================================================================
// TASK 12: FUNKTIONER (20 quiz questions)
// =============================================================================

const TASK_12_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't12-q1',
        question: 'Hur definierar du en funktion i bash?',
        options: ['def minFunktion:', 'minFunktion() { }', 'func minFunktion() { }', 'function: minFunktion'],
        correctIndex: 1, // B
        explanation: 'namn() { kommandon } är standard bash-syntax.',
        difficulty: 'G',
        category: 'Syntax'
    },
    {
        id: 't12-q2',
        question: 'Hur anropar du en funktion?',
        options: ['call minFunktion', 'minFunktion()', 'minFunktion', 'invoke minFunktion'],
        correctIndex: 2, // C
        explanation: 'Bara funktionsnamnet - inga parenteser vid anrop.',
        difficulty: 'G',
        category: 'Anrop'
    },
    {
        id: 't12-q3',
        question: 'Hur skickar du argument till en funktion?',
        options: ['minFunktion(arg1, arg2)', 'minFunktion arg1 arg2', 'call minFunktion with arg1', 'minFunktion --args arg1'],
        correctIndex: 1, // B
        explanation: 'Argument separeras med mellanslag, precis som kommandon.',
        difficulty: 'G',
        category: 'Argument'
    },
    {
        id: 't12-q4',
        question: 'Vad innehåller $1 inuti en funktion?',
        options: ['Skriptets första argument', 'Funktionens första argument', 'Funktionsnamnet', 'Returvärdet'],
        correctIndex: 1, // B
        explanation: '$1, $2 etc refererar till funktionens argument inuti funktionen.',
        difficulty: 'G',
        category: 'Argument'
    },
    {
        id: 't12-q5',
        question: 'Hur returnerar en funktion ett numeriskt värde?',
        options: ['return värde', 'exit värde', 'yield värde', 'give värde'],
        correctIndex: 0, // A
        explanation: 'return N sätter exit-kod (0-255).',
        difficulty: 'G',
        category: 'Return'
    },
    {
        id: 't12-q6',
        question: 'Hur returnerar du text från funktion?',
        options: ['return "text"', 'echo "text" + fånga med $()', 'yield "text"', 'print "text"'],
        correctIndex: 1, // B
        explanation: 'echo i funktion + result=$(funktion) är standardmönstret.',
        difficulty: 'G',
        category: 'Output'
    },
    {
        id: 't12-q7',
        question: 'Vad är default returvärde för funktion?',
        options: ['0', '1', 'Exit-kod från sista kommandot', 'null'],
        correctIndex: 2, // C
        explanation: 'Om ingen return anges används sista kommandots exit-kod.',
        difficulty: 'G',
        category: 'Return'
    },
    {
        id: 't12-q8',
        question: 'Var måste funktionen definieras?',
        options: ['Var som helst', 'Innan första anropet', 'I slutet av skriptet', 'I separat fil'],
        correctIndex: 1, // B
        explanation: 'Bash läser uppifrån-ner - funktionen måste finnas före anrop.',
        difficulty: 'G',
        category: 'Ordning'
    },
    {
        id: 't12-q9',
        question: 'Vad gör local i en funktion?',
        options: ['Exporterar variabel', 'Skapar lokal variabel', 'Låser variabel', 'Tar bort variabel'],
        correctIndex: 1, // B
        explanation: 'local skapar variabel som bara syns i funktionen.',
        difficulty: 'VG',
        category: 'Scope'
    },
    {
        id: 't12-q10',
        question: 'Vad händer utan local i funktion?',
        options: ['Variabeln är lokal', 'Variabeln blir global', 'Syntax-fel', 'Variabeln tas bort'],
        correctIndex: 1, // B
        explanation: 'Utan local är variabeln global och kan läcka ut.',
        difficulty: 'VG',
        category: 'Scope'
    },
    {
        id: 't12-q11',
        question: 'Hur exporterar du funktion till subshell?',
        options: ['export minFunktion', 'export -f minFunktion', 'global minFunktion', 'share minFunktion'],
        correctIndex: 1, // B
        explanation: 'export -f gör funktionen tillgänglig i subprocesser.',
        difficulty: 'VG',
        category: 'Export'
    },
    {
        id: 't12-q12',
        question: 'Hur listar du alla definierade funktioner?',
        options: ['functions', 'declare -F', 'list functions', 'show -f'],
        correctIndex: 1, // B
        explanation: 'declare -F listar alla funktionsnamn.',
        difficulty: 'VG',
        category: 'Debug'
    },
    {
        id: 't12-q13',
        question: 'Hur visar du en funktions definition?',
        options: ['cat -f funktion', 'declare -f funktion', 'show funktion', 'type -f funktion'],
        correctIndex: 1, // B
        explanation: 'declare -f funktionsnamn visar hela definitionen.',
        difficulty: 'VG',
        category: 'Debug'
    },
    {
        id: 't12-q14',
        question: 'Hur tar du bort en funktion?',
        options: ['delete funktion', 'rm -f funktion', 'unset -f funktion', 'remove funktion'],
        correctIndex: 2, // C
        explanation: 'unset -f tar bort funktionsdefinitionen.',
        difficulty: 'VG',
        category: 'Hantering'
    },
    {
        id: 't12-q15',
        question: 'Hur tar du emot array som argument?',
        options: ['func(arr[])', 'func() { local arr=("$@") }', 'func @array', 'func --array arr'],
        correctIndex: 1, // B
        explanation: 'Alla argument kan sparas som array med ("$@").',
        difficulty: 'VG',
        category: 'Arrays'
    },
    {
        id: 't12-q16',
        question: 'Vad är nameref (bash 4.3+)?',
        options: ['Namn på referens', 'Pekare till variabel', 'Namnvalidering', 'Referensräknare'],
        correctIndex: 1, // B
        explanation: 'local -n ref=$1 skapar pekare till variabel med namn $1.',
        difficulty: 'VG',
        category: 'Avancerat'
    },
    {
        id: 't12-q17',
        question: 'Skillnad function f vs f()?',
        options: ['Ingen skillnad', 'function är snabbare', 'f() är POSIX, function är bash-specifik', 'function returnerar annat'],
        correctIndex: 2, // C
        explanation: 'namn() är POSIX-kompatibel och föredras.',
        difficulty: 'VG',
        category: 'Syntax'
    },
    {
        id: 't12-q18',
        question: 'Hur sourcar du funktionsbibliotek?',
        options: ['import lib.sh', 'source lib.sh', 'include lib.sh', 'require lib.sh'],
        correctIndex: 1, // B
        explanation: 'source (eller .) läser in filen i aktuell shell.',
        difficulty: 'VG',
        category: 'Bibliotek'
    },
    {
        id: 't12-q19',
        question: 'Vad gör ${@:2} i funktion?',
        options: ['Argument 2', 'Alla argument från position 2', 'De 2 sista', 'Varannat argument'],
        correctIndex: 1, // B
        explanation: '${@:N} ger alla argument från position N och framåt.',
        difficulty: 'VG',
        category: 'Slicing'
    },
    {
        id: 't12-q20',
        question: 'Kan funktioner vara rekursiva i bash?',
        options: ['Nej', 'Ja men med maxdjup', 'Ja utan begränsning', 'Bara med -r flagga'],
        correctIndex: 2, // C
        explanation: 'Ja, funktioner kan anropa sig själva (varning: ingen tail-call opt).',
        difficulty: 'VG',
        category: 'Rekursion'
    }
]

// =============================================================================
// TASK 19: LAGRING & LVM (20 quiz)
// =============================================================================

const TASK_19_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't19-q1',
        question: 'Vilket kommando visar blockenheter?',
        options: ['fdisk', 'lsblk', 'blkid', 'df'],
        correctIndex: 1, // B
        explanation: 'lsblk listar alla blockenheter (diskar och partitioner) i trädformat.',
        difficulty: 'G',
        category: 'Grunder'
    },
    {
        id: 't19-q2',
        question: 'Vad visar kommandot df?',
        options: ['Filstorlekar', 'Diskutrymme', 'UUID', 'Partitionstyp'],
        correctIndex: 1, // B
        explanation: 'df (disk free) visar ledigt/använt diskutrymme per filsystem.',
        difficulty: 'G',
        category: 'Grunder'
    },
    {
        id: 't19-q3',
        question: 'Vilken katalog används för manuella mounts?',
        options: ['/media', '/mnt', '/dev', '/var'],
        correctIndex: 1, // B
        explanation: '/mnt används traditionellt för manuella mounts, /media för automatiska.',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 't19-q4',
        question: 'Hur monterar du /dev/sdb1 till /mnt/disk?',
        options: ['mount /mnt/disk /dev/sdb1', 'mount /dev/sdb1 /mnt/disk', 'mnt /dev/sdb1 /mnt/disk', 'attach /dev/sdb1 /mnt/disk'],
        correctIndex: 1, // B
        explanation: 'mount <enhet> <mountpunkt> - enheten först, sedan destination.',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 't19-q5',
        question: 'Vilken fil definierar automatiska mounts vid boot?',
        options: ['/etc/mount.conf', '/etc/fstab', '/etc/disks', '/etc/volumes'],
        correctIndex: 1, // B
        explanation: '/etc/fstab (file system table) definierar mounts som utförs vid systemstart.',
        difficulty: 'G',
        category: 'fstab'
    },
    {
        id: 't19-q6',
        question: 'Vad står LVM för?',
        options: ['Linux Virtual Memory', 'Logical Volume Manager', 'Linux Volume Mount', 'Large Volume Mode'],
        correctIndex: 1, // B
        explanation: 'LVM = Logical Volume Manager för flexibel diskhantering.',
        difficulty: 'G',
        category: 'LVM'
    },
    {
        id: 't19-q7',
        question: 'Vilka tre lager har LVM?',
        options: ['Disk, Partition, Mount', 'PV, VG, LV', 'Raw, Block, File', 'Primary, Extended, Logical'],
        correctIndex: 1, // B
        explanation: 'PV (Physical Volume), VG (Volume Group), LV (Logical Volume).',
        difficulty: 'G',
        category: 'LVM'
    },
    {
        id: 't19-q8',
        question: 'Hur skapar du ext4-filsystem på /dev/sdb1?',
        options: ['format ext4 /dev/sdb1', 'mkfs.ext4 /dev/sdb1', 'create ext4 /dev/sdb1', 'newfs ext4 /dev/sdb1'],
        correctIndex: 1, // B
        explanation: 'mkfs.ext4 (make filesystem) skapar ext4-filsystem.',
        difficulty: 'G',
        category: 'Filsystem'
    },
    {
        id: 't19-q9',
        question: 'Vad visar blkid?',
        options: ['Blockstorlek', 'UUID och filsystemtyp', 'Disktemperatur', 'Ledigt utrymme'],
        correctIndex: 1, // B
        explanation: 'blkid visar UUID, filsystemtyp och labels för blockenheter.',
        difficulty: 'G',
        category: 'Verktyg'
    },
    {
        id: 't19-q10',
        question: 'Hur avmonterar du en enhet?',
        options: ['dismount', 'unmount', 'umount', 'detach'],
        correctIndex: 2, // C
        explanation: 'umount (utan n!) avmonterar enheter.',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 't19-q11',
        question: 'Hur skapar du Physical Volume i LVM?',
        options: ['vgcreate /dev/sdb', 'lvcreate /dev/sdb', 'pvcreate /dev/sdb', 'mkpv /dev/sdb'],
        correctIndex: 2, // C
        explanation: 'pvcreate initialiserar en disk som Physical Volume.',
        difficulty: 'VG',
        category: 'LVM'
    },
    {
        id: 't19-q12',
        question: 'Hur skapar du Volume Group "myvg" med /dev/sdb?',
        options: ['vgcreate myvg /dev/sdb', 'vgcreate /dev/sdb myvg', 'mkvg myvg /dev/sdb', 'vg create myvg'],
        correctIndex: 0, // A
        explanation: 'vgcreate <vgnamn> <pv> skapar Volume Group.',
        difficulty: 'VG',
        category: 'LVM'
    },
    {
        id: 't19-q13',
        question: 'Hur skapar du 10GB Logical Volume "data" i vg1?',
        options: ['lvcreate -L 10G -n data vg1', 'lvcreate vg1 data 10G', 'mklv 10G data vg1', 'lv create data 10G'],
        correctIndex: 0, // A
        explanation: 'lvcreate -L <storlek> -n <namn> <vg> skapar Logical Volume.',
        difficulty: 'VG',
        category: 'LVM'
    },
    {
        id: 't19-q14',
        question: 'Hur utökar du LV med 5GB?',
        options: ['lvgrow +5G /dev/vg/lv', 'lvextend -L +5G /dev/vg/lv', 'lvresize 5G /dev/vg/lv', 'lvadd 5G /dev/vg/lv'],
        correctIndex: 1, // B
        explanation: 'lvextend -L +<storlek> utökar Logical Volume.',
        difficulty: 'VG',
        category: 'LVM'
    },
    {
        id: 't19-q15',
        question: 'Vilket kommando växer filsystemet efter lvextend?',
        options: ['fsextend', 'resize2fs', 'growfs', 'expand'],
        correctIndex: 1, // B
        explanation: 'resize2fs expanderar ext2/3/4-filsystem efter volymutökning.',
        difficulty: 'VG',
        category: 'LVM'
    },
    {
        id: 't19-q16',
        question: 'Vad är fördelen med UUID i fstab?',
        options: ['Snabbare boot', 'Säkrare vid disknamnändring', 'Bättre kompression', 'Större diskstöd'],
        correctIndex: 1, // B
        explanation: 'UUID är unikt och ändras inte om diskar läggs till/tas bort.',
        difficulty: 'VG',
        category: 'fstab'
    },
    {
        id: 't19-q17',
        question: 'Skillnad mellan MBR och GPT?',
        options: ['MBR är nyare', 'GPT stödjer större diskar och fler partitioner', 'MBR är snabbare', 'GPT kräver Windows'],
        correctIndex: 1, // B
        explanation: 'GPT: 128 partitioner, inga storleksgränser. MBR: 4 primära, 2TB max.',
        difficulty: 'VG',
        category: 'Partitioner'
    },
    {
        id: 't19-q18',
        question: 'Hur testar du fstab utan reboot?',
        options: ['fstab -t', 'mount -a', 'test-mount', 'fstab --test'],
        correctIndex: 1, // B
        explanation: 'mount -a monterar allt i fstab som inte redan är monterat.',
        difficulty: 'VG',
        category: 'fstab'
    },
    {
        id: 't19-q19',
        question: 'Hur skapar du LVM-snapshot?',
        options: ['lvcreate -s -n snap /dev/vg/lv', 'lvsnap /dev/vg/lv', 'snapshot -c /dev/vg/lv', 'lv snap create'],
        correctIndex: 0, // A
        explanation: 'lvcreate -s (snapshot) skapar en snapshot av befintlig LV.',
        difficulty: 'VG',
        category: 'LVM'
    },
    {
        id: 't19-q20',
        question: 'Vad gör noatime mount-option?',
        options: ['Snabbare läsning', 'Uppdaterar inte access time', 'Krypterar data', 'Komprimerar filer'],
        correctIndex: 1, // B
        explanation: 'noatime skippar access time-uppdatering, bra för SSD-prestanda.',
        difficulty: 'VG',
        category: 'Mount'
    }
]

// =============================================================================
// TASK 20: BACKUP (20 quiz)
// =============================================================================

const TASK_20_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't20-q1',
        question: 'Hur skapar du tar-arkiv av mappen "data"?',
        options: ['tar data arkiv.tar', 'tar -cvf arkiv.tar data/', 'tar -x arkiv.tar data/', 'tar create data'],
        correctIndex: 1, // B
        explanation: 'tar -cvf <arkiv> <källa> skapar arkiv (-c=create, -v=verbose, -f=file).',
        difficulty: 'G',
        category: 'tar'
    },
    {
        id: 't20-q2',
        question: 'Vilken flagga packar upp tar-arkiv?',
        options: ['-c', '-t', '-x', '-u'],
        correctIndex: 2, // C
        explanation: '-x (extract) packar upp arkivinnehåll.',
        difficulty: 'G',
        category: 'tar'
    },
    {
        id: 't20-q3',
        question: 'Hur komprimerar du tar med gzip?',
        options: ['tar -cvgf', 'tar -cvzf', 'tar -cvbf', 'tar -cvjf'],
        correctIndex: 1, // B
        explanation: '-z = gzip-komprimering (ger .tar.gz).',
        difficulty: 'G',
        category: 'tar'
    },
    {
        id: 't20-q4',
        question: 'Vad gör rsync?',
        options: ['Komprimerar filer', 'Synkroniserar filer/kataloger', 'Krypterar backup', 'Partitionerar disk'],
        correctIndex: 1, // B
        explanation: 'rsync synkroniserar filer och kopierar bara ändringar (effektivt).',
        difficulty: 'G',
        category: 'rsync'
    },
    {
        id: 't20-q5',
        question: 'Grundläggande rsync-syntax för lokal kopiering?',
        options: ['rsync mål/ källa/', 'rsync -av källa/ mål/', 'rsync copy källa mål', 'rsync --sync källa mål'],
        correctIndex: 1, // B
        explanation: 'rsync -av <källa> <mål> synkroniserar med arkivläge.',
        difficulty: 'G',
        category: 'rsync'
    },
    {
        id: 't20-q6',
        question: 'Vad är inkrementell backup?',
        options: ['Kopierar alla filer', 'Kopierar bara ändringar', 'Komprimerar backup', 'Krypterar backup'],
        correctIndex: 1, // B
        explanation: 'Inkrementell backup kopierar endast filer som ändrats sedan senast.',
        difficulty: 'G',
        category: 'Koncept'
    },
    {
        id: 't20-q7',
        question: 'Hur listar du innehåll i tar-arkiv?',
        options: ['tar -lvf', 'tar -tvf', 'tar --list', 'tar -dir'],
        correctIndex: 1, // B
        explanation: '-t (list) visar arkivets innehåll utan att packa upp.',
        difficulty: 'G',
        category: 'tar'
    },
    {
        id: 't20-q8',
        question: 'Vad är 3-2-1 backup-regeln?',
        options: ['3 diskar, 2 servrar, 1 moln', '3 kopior, 2 medier, 1 offsite', '3 TB, 2 partitioner, 1 RAID', '3 dagliga, 2 veckoliga, 1 månadsbackup'],
        correctIndex: 1, // B
        explanation: '3 kopior av data, på 2 olika medier, varav 1 offsite (annan plats).',
        difficulty: 'G',
        category: 'Best Practice'
    },
    {
        id: 't20-q9',
        question: 'Vilken flagga ger bzip2-komprimering i tar?',
        options: ['-z', '-b', '-j', '-x'],
        correctIndex: 2, // C
        explanation: '-j = bzip2-komprimering (bättre än gzip men långsammare).',
        difficulty: 'G',
        category: 'tar'
    },
    {
        id: 't20-q10',
        question: 'Vad gör dd?',
        options: ['Tar bort dubbletter', 'Kopierar rå data bit-för-bit', 'Dekrypterar filer', 'Deduplicerar backup'],
        correctIndex: 1, // B
        explanation: 'dd (disk duplicator) kopierar rå data, används för diskkloning.',
        difficulty: 'G',
        category: 'dd'
    },
    {
        id: 't20-q11',
        question: 'Hur kopierar du rsync över SSH?',
        options: ['rsync -ssh källa/ host:/mål/', 'rsync -avz -e ssh källa/ user@host:/mål/', 'rsync --remote källa host:mål', 'rsync -net ssh källa mål'],
        correctIndex: 1, // B
        explanation: '-e ssh anger SSH som transport för rsync.',
        difficulty: 'VG',
        category: 'rsync'
    },
    {
        id: 't20-q12',
        question: 'Vad gör rsync --delete?',
        options: ['Tar bort källfiler', 'Tar bort målfiler som inte finns i källa', 'Raderar backup', 'Avbryter vid fel'],
        correctIndex: 1, // B
        explanation: '--delete gör målet identiskt med källan (tar bort extra filer).',
        difficulty: 'VG',
        category: 'rsync'
    },
    {
        id: 't20-q13',
        question: 'Hur testar du rsync utan att köra?',
        options: ['rsync --test', 'rsync -n eller --dry-run', 'rsync --simulate', 'rsync -t'],
        correctIndex: 1, // B
        explanation: '-n/--dry-run visar vad som skulle hända utan att göra något.',
        difficulty: 'VG',
        category: 'rsync'
    },
    {
        id: 't20-q14',
        question: 'Hur skapar du disk image med dd?',
        options: ['dd if=/dev/sda to=disk.img', 'dd if=/dev/sda of=disk.img', 'dd copy /dev/sda disk.img', 'dd clone sda disk.img'],
        correctIndex: 1, // B
        explanation: 'dd if=<input> of=<output> skapar exakt kopia.',
        difficulty: 'VG',
        category: 'dd'
    },
    {
        id: 't20-q15',
        question: 'Hur schemalägger du daglig backup kl 02:00?',
        options: ['cron 2 backup.sh', '0 2 * * * /scripts/backup.sh i crontab', 'schedule 02:00 backup', 'at 02:00 daily backup'],
        correctIndex: 1, // B
        explanation: 'Cron-format: minut timme dag månad veckodag. 0 2 * * * = 02:00 varje dag.',
        difficulty: 'VG',
        category: 'Schemaläggning'
    },
    {
        id: 't20-q16',
        question: 'Vad gör rsync --exclude?',
        options: ['Inkluderar bara matchande', 'Exkluderar matchande mönster', 'Exkluderar tomma filer', 'Hoppar över stora filer'],
        correctIndex: 1, // B
        explanation: '--exclude="mönster" skippar filer som matchar.',
        difficulty: 'VG',
        category: 'rsync'
    },
    {
        id: 't20-q17',
        question: 'Hur packar du upp specifik fil från tar?',
        options: ['tar -xvf arkiv.tar fil.txt', 'tar --only fil.txt arkiv.tar', 'tar -extract fil arkiv', 'tar -single fil arkiv.tar'],
        correctIndex: 0, // A
        explanation: 'Ange filnamn efter arkivet för att extrahera specifik fil.',
        difficulty: 'VG',
        category: 'tar'
    },
    {
        id: 't20-q18',
        question: 'Vad är rsnapshot?',
        options: ['Snapshotverktyg för LVM', 'Rotationsbackup med hard links', 'RAM-snapshot', 'rsync-plugin'],
        correctIndex: 1, // B
        explanation: 'rsnapshot gör rotationsbackuper med hard links för att spara utrymme.',
        difficulty: 'VG',
        category: 'Verktyg'
    },
    {
        id: 't20-q19',
        question: 'Vad gör rsync --link-dest?',
        options: ['Skapar symboliska länkar', 'Hard links till oförändrade filer', 'Länkar till remote', 'Destination för länkar'],
        correctIndex: 1, // B
        explanation: '--link-dest skapar hard links till oförändrade filer från tidigare backup.',
        difficulty: 'VG',
        category: 'rsync'
    },
    {
        id: 't20-q20',
        question: 'Vilken flagga ger xz-komprimering i tar?',
        options: ['-z', '-j', '-J', '-x'],
        correctIndex: 2, // C
        explanation: '-J = xz-komprimering (bäst kompression, långsammast).',
        difficulty: 'VG',
        category: 'tar'
    }
]

// =============================================================================
// TASK 13: SIGNALER (20 quiz questions)
// =============================================================================

const TASK_13_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't13-q1',
        question: 'Vad är en signal i Linux?',
        options: ['En ljudvarning', 'Asynkron notifiering till process', 'Nätverkspaket', 'Filtyp'],
        correctIndex: 1, // B
        explanation: 'Signaler är asynkrona notifieringar för processkontroll.',
        difficulty: 'G',
        category: 'Grunder'
    },
    {
        id: 't13-q2',
        question: 'Vilken signal skickas av Ctrl+C?',
        options: ['SIGTERM', 'SIGINT', 'SIGKILL', 'SIGSTOP'],
        correctIndex: 1, // B
        explanation: 'SIGINT (signal 2) skickas vid Ctrl+C.',
        difficulty: 'G',
        category: 'Vanliga'
    },
    {
        id: 't13-q3',
        question: 'Vilken signal är standardsignal för kill?',
        options: ['SIGKILL', 'SIGTERM', 'SIGHUP', 'SIGINT'],
        correctIndex: 1, // B
        explanation: 'kill utan flagga skickar SIGTERM (signal 15).',
        difficulty: 'G',
        category: 'kill'
    },
    {
        id: 't13-q4',
        question: 'Vilken signal kan INTE fångas?',
        options: ['SIGTERM', 'SIGINT', 'SIGKILL', 'SIGHUP'],
        correctIndex: 2, // C
        explanation: 'SIGKILL (9) och SIGSTOP kan inte fångas eller ignoreras.',
        difficulty: 'G',
        category: 'Signaler'
    },
    {
        id: 't13-q5',
        question: 'Hur dödar du process med PID 1234?',
        options: ['stop 1234', 'kill 1234', 'end 1234', 'terminate 1234'],
        correctIndex: 1, // B
        explanation: 'kill PID skickar SIGTERM till processen.',
        difficulty: 'G',
        category: 'kill'
    },
    {
        id: 't13-q6',
        question: 'Hur tvingar du processdöd?',
        options: ['kill -f PID', 'kill -9 PID', 'kill --force PID', 'kill -hard PID'],
        correctIndex: 1, // B
        explanation: 'kill -9 (SIGKILL) tvingar omedelbar avslutning.',
        difficulty: 'G',
        category: 'kill'
    },
    {
        id: 't13-q7',
        question: 'Vad gör trap i bash?',
        options: ['Fångar filer', 'Fångar signaler', 'Fångar fel', 'Skapar fällor'],
        correctIndex: 1, // B
        explanation: 'trap fångar signaler och kör angivet kommando.',
        difficulty: 'G',
        category: 'trap'
    },
    {
        id: 't13-q8',
        question: 'Hur listar du alla signaler?',
        options: ['signals', 'kill -l', 'list signals', 'trap --list'],
        correctIndex: 1, // B
        explanation: 'kill -l listar alla signalnamn och nummer.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't13-q9',
        question: 'Grundläggande trap-syntax?',
        options: ['trap SIGNAL "kommando"', 'trap "kommando" SIGNAL', 'catch SIGNAL kommando', 'on SIGNAL kommando'],
        correctIndex: 1, // B
        explanation: 'trap "kommando" SIGNAL är korrekt syntax.',
        difficulty: 'VG',
        category: 'trap'
    },
    {
        id: 't13-q10',
        question: 'Hur städar du vid skriptavslut?',
        options: ['trap cleanup STOP', 'trap cleanup EXIT', 'on exit cleanup', 'finally cleanup'],
        correctIndex: 1, // B
        explanation: 'trap kommando EXIT körs vid skriptavslut.',
        difficulty: 'VG',
        category: 'trap'
    },
    {
        id: 't13-q11',
        question: 'Hur ignorerar du en signal?',
        options: ['trap ignore SIGINT', 'trap "" SIGINT', 'trap skip SIGINT', 'ignore SIGINT'],
        correctIndex: 1, // B
        explanation: 'Tom sträng i trap ignorerar signalen.',
        difficulty: 'VG',
        category: 'trap'
    },
    {
        id: 't13-q12',
        question: 'Hur återställer du trap till default?',
        options: ['trap reset SIGINT', 'trap - SIGINT', 'trap default SIGINT', 'unset trap SIGINT'],
        correctIndex: 1, // B
        explanation: 'trap - SIGNAL återställer till default-hantering.',
        difficulty: 'VG',
        category: 'trap'
    },
    {
        id: 't13-q13',
        question: 'Vad gör Ctrl+Z?',
        options: ['Dödar processen', 'Pausar processen (SIGTSTP)', 'Avslutar shell', 'Ångrar kommando'],
        correctIndex: 1, // B
        explanation: 'Ctrl+Z skickar SIGTSTP och pausar processen.',
        difficulty: 'VG',
        category: 'Vanliga'
    },
    {
        id: 't13-q14',
        question: 'Hur dödar du processer med namn?',
        options: ['kill processnamn', 'pkill processnamn', 'stop processnamn', 'end processnamn'],
        correctIndex: 1, // B
        explanation: 'pkill och killall dödar processer baserat på namn.',
        difficulty: 'VG',
        category: 'kill'
    },
    {
        id: 't13-q15',
        question: 'Vad är ERR i trap?',
        options: ['Error signal', 'Pseudo-signal vid fel', 'Extern error', 'Error redirect'],
        correctIndex: 1, // B
        explanation: 'ERR triggas vid kommandon med non-zero exit.',
        difficulty: 'VG',
        category: 'trap'
    },
    {
        id: 't13-q16',
        question: 'Vad är SIGHUP ofta använd för?',
        options: ['Avsluta process', 'Reload konfiguration', 'Pausa process', 'Starta om system'],
        correctIndex: 1, // B
        explanation: 'Många daemons laddar om config vid SIGHUP.',
        difficulty: 'VG',
        category: 'Signaler'
    },
    {
        id: 't13-q17',
        question: 'Hur fortsätter du stoppad process?',
        options: ['kill -START PID', 'kill -CONT PID', 'resume PID', 'continue PID'],
        correctIndex: 1, // B
        explanation: 'SIGCONT fortsätter en stoppad process.',
        difficulty: 'VG',
        category: 'Signaler'
    },
    {
        id: 't13-q18',
        question: 'Vad är DEBUG trap?',
        options: ['Felsökningsläge', 'Körs före varje kommando', 'Visar debug-info', 'Loggar fel'],
        correctIndex: 1, // B
        explanation: 'DEBUG trap körs före varje kommando i skriptet.',
        difficulty: 'VG',
        category: 'trap'
    },
    {
        id: 't13-q19',
        question: 'Hur propagerar du signalnummer vid exit?',
        options: ['exit SIGNAL', 'exit $((128+signal))', 'return SIGNAL', 'Går ej'],
        correctIndex: 1, // B
        explanation: 'Convention: exit 128+signalnummer (ex: 130 för SIGINT).',
        difficulty: 'VG',
        category: 'Best Practice'
    },
    {
        id: 't13-q20',
        question: 'Ärvs traps till subshells?',
        options: ['Ja alltid', 'Nej aldrig', 'Bara EXIT', 'Bara om exporterade'],
        correctIndex: 1, // B
        explanation: 'Traps ärvs INTE till subshells.',
        difficulty: 'VG',
        category: 'Avancerat'
    }
]

// =============================================================================
// TASK 14: ANVÄNDARHANTERING (20 quiz questions)
// =============================================================================

const TASK_14_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't14-q1',
        question: 'Vilken fil innehåller användarinformation?',
        options: ['/etc/users', '/etc/passwd', '/etc/accounts', '/etc/login'],
        correctIndex: 1, // B
        explanation: '/etc/passwd innehåller grundläggande användarinfo.',
        difficulty: 'G',
        category: 'Filer'
    },
    {
        id: 't14-q2',
        question: 'Vilken fil innehåller lösenordshashar?',
        options: ['/etc/passwd', '/etc/shadow', '/etc/passwords', '/etc/secure'],
        correctIndex: 1, // B
        explanation: '/etc/shadow innehåller hashade lösenord (endast root).',
        difficulty: 'G',
        category: 'Filer'
    },
    {
        id: 't14-q3',
        question: 'Hur skapar du en ny användare?',
        options: ['newuser username', 'useradd username', 'createuser username', 'mkuser username'],
        correctIndex: 1, // B
        explanation: 'useradd (eller adduser) skapar nya användare.',
        difficulty: 'G',
        category: 'useradd'
    },
    {
        id: 't14-q4',
        question: 'Hur tar du bort en användare?',
        options: ['deluser username', 'userdel username', 'rmuser username', 'removeuser username'],
        correctIndex: 1, // B
        explanation: 'userdel tar bort användaren.',
        difficulty: 'G',
        category: 'userdel'
    },
    {
        id: 't14-q5',
        question: 'Hur ändrar du ditt lösenord?',
        options: ['password', 'passwd', 'chpass', 'setpass'],
        correctIndex: 1, // B
        explanation: 'passwd ändrar lösenord för aktuell användare.',
        difficulty: 'G',
        category: 'passwd'
    },
    {
        id: 't14-q6',
        question: 'Hur skapar du en grupp?',
        options: ['newgroup namn', 'groupadd namn', 'mkgroup namn', 'addgroup namn'],
        correctIndex: 1, // B
        explanation: 'groupadd skapar nya grupper.',
        difficulty: 'G',
        category: 'groupadd'
    },
    {
        id: 't14-q7',
        question: 'Hur lägger du användare i en grupp?',
        options: ['adduser user group', 'usermod -aG grupp user', 'groupadd user grupp', 'useradd -g grupp user'],
        correctIndex: 1, // B
        explanation: 'usermod -aG lägger till användare i supplementary group.',
        difficulty: 'G',
        category: 'usermod'
    },
    {
        id: 't14-q8',
        question: 'Vilket UID har root?',
        options: ['1', '0', '1000', '-1'],
        correctIndex: 1, // B
        explanation: 'root har alltid UID 0.',
        difficulty: 'G',
        category: 'Grunder'
    },
    {
        id: 't14-q9',
        question: 'Hur skapar du användare med hemkatalog?',
        options: ['useradd -h username', 'useradd -m username', 'useradd -d username', 'useradd --home username'],
        correctIndex: 1, // B
        explanation: '-m (make home) skapar hemkatalog.',
        difficulty: 'VG',
        category: 'useradd'
    },
    {
        id: 't14-q10',
        question: 'Hur sätter du default shell?',
        options: ['useradd -b /bin/bash', 'useradd -s /bin/bash', 'useradd --shell /bin/bash', 'Både B och C'],
        correctIndex: 3, // D
        explanation: '-s eller --shell anger login shell.',
        difficulty: 'VG',
        category: 'useradd'
    },
    {
        id: 't14-q11',
        question: 'Hur låser du en användare?',
        options: ['passwd -l user', 'usermod -l user', 'lock user', 'disable user'],
        correctIndex: 0, // A
        explanation: 'passwd -l (lock) eller usermod -L låser kontot.',
        difficulty: 'VG',
        category: 'Säkerhet'
    },
    {
        id: 't14-q12',
        question: 'Hur visar du grupptillhörigheter?',
        options: ['showgroups user', 'groups user', 'listgroups user', 'usergroups user'],
        correctIndex: 1, // B
        explanation: 'groups eller id visar grupptillhörigheter.',
        difficulty: 'VG',
        category: 'Kommandon'
    },
    {
        id: 't14-q13',
        question: 'Vad betyder -a i usermod -aG?',
        options: ['Admin', 'Append', 'All', 'Add'],
        correctIndex: 1, // B
        explanation: '-a = append, lägger till utan att ta bort andra grupper.',
        difficulty: 'VG',
        category: 'usermod'
    },
    {
        id: 't14-q14',
        question: 'Vad är /etc/skel?',
        options: ['Skeleton directory för nya hemkataloger', 'Skelett-logg', 'System kernel', 'Security kernel'],
        correctIndex: 0, // A
        explanation: 'Filer i /etc/skel kopieras till nya hemkataloger.',
        difficulty: 'VG',
        category: 'Konfiguration'
    },
    {
        id: 't14-q15',
        question: 'Hur sätter du lösenordsutgång?',
        options: ['passwd -e user', 'chage -M dagar user', 'expire user dagar', 'passexp user dagar'],
        correctIndex: 1, // B
        explanation: 'chage -M sätter max antal dagar för lösenord.',
        difficulty: 'VG',
        category: 'chage'
    },
    {
        id: 't14-q16',
        question: 'Hur tvingar du lösenordsbyte vid nästa login?',
        options: ['passwd -f user', 'chage -d 0 user', 'forcepass user', 'expirepass user'],
        correctIndex: 1, // B
        explanation: 'chage -d 0 eller passwd -e tvingar byte.',
        difficulty: 'VG',
        category: 'chage'
    },
    {
        id: 't14-q17',
        question: 'Hur skapar du systemanvändare?',
        options: ['useradd -s user', 'useradd -r user', 'useradd --system user', 'Både B och C'],
        correctIndex: 3, // D
        explanation: '-r skapar system user med lågt UID.',
        difficulty: 'VG',
        category: 'useradd'
    },
    {
        id: 't14-q18',
        question: 'Vad är nologin shell?',
        options: ['Shell som loggar allt', 'Shell som förhindrar login', 'Shell utan features', 'Shell för nätverk'],
        correctIndex: 1, // B
        explanation: '/sbin/nologin eller /bin/false förhindrar interaktiv login.',
        difficulty: 'VG',
        category: 'Säkerhet'
    },
    {
        id: 't14-q19',
        question: 'Hur tar du bort användare inklusive hemkatalog?',
        options: ['userdel user', 'userdel -r user', 'userdel -h user', 'userdel --home user'],
        correctIndex: 1, // B
        explanation: '-r (remove) tar även bort hemkatalog och mail.',
        difficulty: 'VG',
        category: 'userdel'
    },
    {
        id: 't14-q20',
        question: 'Hur verifierar du /etc/passwd integritet?',
        options: ['checkpasswd', 'pwck', 'verifypasswd', 'passwd --check'],
        correctIndex: 1, // B
        explanation: 'pwck verifierar passwd och shadow-filer.',
        difficulty: 'VG',
        category: 'Verktyg'
    },
    // SCENARIO-BASERADE FRÅGOR
    {
        id: 't14-s1',
        question: 'Ny utvecklare kan inte logga in. useradd john kördes. Vad glömdes troligen?',
        options: ['Lösenord sattes aldrig', 'Hemkatalog saknas', 'Användaren är låst', 'Alla ovan kan vara problemet'],
        correctIndex: 3, // D
        explanation: 'Vanliga problem: inget lösenord (passwd john), ingen hemkatalog (-m), eller låst konto.',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'HR ringer - ny anställd kan inte logga in.',
        isScenario: true
    },
    {
        id: 't14-s2',
        question: 'Användare behöver sudo-rättigheter. Enklaste sättet på Ubuntu?',
        options: ['Redigera /etc/sudoers direkt', 'usermod -aG sudo username', 'chmod +s /bin/bash', 'passwd -S username'],
        correctIndex: 1, // B
        explanation: 'Lägg till i sudo-gruppen med usermod -aG sudo. Redigera ALDRIG sudoers direkt utan visudo!',
        difficulty: 'G',
        category: 'Praktisk',
        scenario: 'Ny DevOps-ingenjör behöver köra administrativa kommandon.',
        isScenario: true
    },
    {
        id: 't14-s3',
        question: 'Du ska sätta samma lösenord för 50 nya användare temporärt. Vilken approach?',
        options: ['passwd för varje', 'echo "password" | passwd --stdin username', 'chpasswd med fil', 'Skapa utan lösenord'],
        correctIndex: 2, // C
        explanation: 'chpasswd läser user:password par från fil/stdin. echo "user1:pass" | chpasswd',
        difficulty: 'VG',
        category: 'Automation',
        scenario: 'Du sätter upp 50 studentkonton för en kurs.',
        isScenario: true
    }
]

// =============================================================================
// TASK 15: RÄTTIGHETER & ACL (20 quiz questions)
// =============================================================================

const TASK_15_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't15-q1',
        question: 'Vad betyder r-rättighet för en fil?',
        options: ['Run', 'Read (läsa innehåll)', 'Recursive', 'Root'],
        correctIndex: 1, // B
        explanation: 'r = read, tillåter läsning av filinnehåll.',
        difficulty: 'G',
        category: 'Grunder'
    },
    {
        id: 't15-q2',
        question: 'Vad betyder x-rättighet för en katalog?',
        options: ['Execute files in it', 'cd in i katalogen', 'Delete katalogen', 'Exportera'],
        correctIndex: 1, // B
        explanation: 'x på katalog tillåter att gå in i den (cd).',
        difficulty: 'G',
        category: 'Grunder'
    },
    {
        id: 't15-q3',
        question: 'Vilket oktalt värde har rwx?',
        options: ['3', '5', '7', '9'],
        correctIndex: 2, // C
        explanation: 'r=4, w=2, x=1. rwx = 4+2+1 = 7.',
        difficulty: 'G',
        category: 'Oktalt'
    },
    {
        id: 't15-q4',
        question: 'Hur gör du fil exekverbar?',
        options: ['chmod exec fil', 'chmod +x fil', 'chmod run fil', 'chmod -e fil'],
        correctIndex: 1, // B
        explanation: 'chmod +x lägger till execute-rättighet.',
        difficulty: 'G',
        category: 'chmod'
    },
    {
        id: 't15-q5',
        question: 'Hur ändrar du ägare på fil?',
        options: ['owner user fil', 'chown user fil', 'setowner user fil', 'chmod user fil'],
        correctIndex: 1, // B
        explanation: 'chown (change owner) ändrar ägare.',
        difficulty: 'G',
        category: 'chown'
    },
    {
        id: 't15-q6',
        question: 'Vad betyder 644 i rättigheter?',
        options: ['rwxrwxr--', 'rw-r--r--', 'rwxr--r--', 'rw-rw-r--'],
        correctIndex: 1, // B
        explanation: '6=rw-, 4=r--, 4=r--. Alltså rw-r--r--.',
        difficulty: 'G',
        category: 'Oktalt'
    },
    {
        id: 't15-q7',
        question: 'Vad är u, g, o i chmod?',
        options: ['user, global, other', 'user, group, others', 'unix, gnu, open', 'up, go, out'],
        correctIndex: 1, // B
        explanation: 'u=user/ägare, g=group, o=others.',
        difficulty: 'G',
        category: 'chmod'
    },
    {
        id: 't15-q8',
        question: 'Hur sätter du rättigheter rekursivt?',
        options: ['chmod -a 755 dir', 'chmod -R 755 dir', 'chmod --all 755 dir', 'chmod -r 755 dir'],
        correctIndex: 1, // B
        explanation: '-R (recursive) applicerar på alla filer/kataloger.',
        difficulty: 'G',
        category: 'chmod'
    },
    {
        id: 't15-q9',
        question: 'Vad är 755 i rättigheter?',
        options: ['rwx-wx-wx', 'rwxr-xr-x', 'rw-r-xr-x', 'rwxrwxr-x'],
        correctIndex: 1, // B
        explanation: '7=rwx, 5=r-x, 5=r-x. Alltså rwxr-xr-x.',
        difficulty: 'VG',
        category: 'Oktalt'
    },
    {
        id: 't15-q10',
        question: 'Vad är SUID-bit?',
        options: ['Super User ID', 'Set User ID - kör som ägare', 'System UID', 'Secure UID'],
        correctIndex: 1, // B
        explanation: 'SUID gör att fil körs med ägarens rättigheter.',
        difficulty: 'VG',
        category: 'Special'
    },
    {
        id: 't15-q11',
        question: 'Vad är Sticky bit på katalog?',
        options: ['Filer klistras fast', 'Endast ägare kan ta bort sina filer', 'Katalogen kan ej tas bort', 'Alla kan skriva'],
        correctIndex: 1, // B
        explanation: 'Sticky bit förhindrar att andra tar bort dina filer.',
        difficulty: 'VG',
        category: 'Special'
    },
    {
        id: 't15-q12',
        question: 'Vad är umask?',
        options: ['User mask', 'Default rättighetsmask för nya filer', 'Unix mask', 'Ultimate mask'],
        correctIndex: 1, // B
        explanation: 'umask definierar vilka rättigheter som INTE ges.',
        difficulty: 'VG',
        category: 'umask'
    },
    {
        id: 't15-q13',
        question: 'Vad ger umask 022 för nya filer?',
        options: ['755', '644', '777', '022'],
        correctIndex: 1, // B
        explanation: 'Filer: 666-022=644 (kataloger: 777-022=755).',
        difficulty: 'VG',
        category: 'umask'
    },
    {
        id: 't15-q14',
        question: 'Hur visar du ACL för fil?',
        options: ['showacl fil', 'getfacl fil', 'lsacl fil', 'acl fil'],
        correctIndex: 1, // B
        explanation: 'getfacl visar Access Control List.',
        difficulty: 'VG',
        category: 'ACL'
    },
    {
        id: 't15-q15',
        question: 'Hur sätter du ACL för specifik användare?',
        options: ['acl -u user:rwx fil', 'setfacl -m u:user:rwx fil', 'chmod acl user:rwx fil', 'addacl user:rwx fil'],
        correctIndex: 1, // B
        explanation: 'setfacl -m modifierar ACL entry.',
        difficulty: 'VG',
        category: 'ACL'
    },
    {
        id: 't15-q16',
        question: 'Vad indikerar + i ls -l output?',
        options: ['Symbolisk länk', 'ACL finns', 'Extended attributes', 'Skrivrättighet'],
        correctIndex: 1, // B
        explanation: '+ efter rättigheter indikerar ACL.',
        difficulty: 'VG',
        category: 'ACL'
    },
    {
        id: 't15-q17',
        question: 'Hur tar du bort alla ACL från fil?',
        options: ['setfacl -d fil', 'setfacl -b fil', 'setfacl --remove fil', 'delacl fil'],
        correctIndex: 1, // B
        explanation: '-b tar bort alla ACL entries.',
        difficulty: 'VG',
        category: 'ACL'
    },
    {
        id: 't15-q18',
        question: 'Hur sätter du default ACL på katalog?',
        options: ['setfacl -D u:user:rwx dir', 'setfacl -d -m u:user:rwx dir', 'setfacl --default u:user:rwx dir', 'Både B och C'],
        correctIndex: 3, // D
        explanation: '-d eller --default sätter default ACL för nya filer.',
        difficulty: 'VG',
        category: 'ACL'
    },
    {
        id: 't15-q19',
        question: 'Hur hittar du alla SUID-filer?',
        options: ['find / -suid', 'find / -perm -4000', 'find / -type suid', 'locate suid'],
        correctIndex: 1, // B
        explanation: '-perm -4000 hittar filer med SUID-bit.',
        difficulty: 'VG',
        category: 'Sökning'
    },
    {
        id: 't15-q20',
        question: 'Vad gör chmod 4755 fil?',
        options: ['Normal 755', 'SUID + 755 (rwsr-xr-x)', 'SGID + 755', 'Sticky + 755'],
        correctIndex: 1, // B
        explanation: '4=SUID, så 4755 = SUID med rwxr-xr-x.',
        difficulty: 'VG',
        category: 'Special'
    },
    // SCENARIO-BASERADE FRÅGOR
    {
        id: 't15-s1',
        question: 'Webservern kan inte läsa /var/www/html/index.html. ls visar -rw-------. Vad gör du?',
        options: ['chmod 777', 'chmod 644', 'chown www-data', 'rm och skapa ny'],
        correctIndex: 1, // B
        explanation: '644 (rw-r--r--) ger ägaren skriv, och alla andra läsrättighet - standard för webbfiler.',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'Webbsidan visar 403 Forbidden.',
        isScenario: true
    },
    {
        id: 't15-s2',
        question: 'Du skapade ett skript men kollegan kan inte köra det. ls visar -rw-r--r--. Vad fattas?',
        options: ['Skrivrättighet', 'Exekveringsrättighet', 'Läsrättighet', 'SUID-bit'],
        correctIndex: 1, // B
        explanation: 'Skript behöver x-rättighet. chmod +x script.sh eller chmod 755 löser det.',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'Kollegans backup-skript vägrar köra.',
        isScenario: true
    },
    {
        id: 't15-s3',
        question: 'Säkerhetsteamet säger att /tmp har för öppna rättigheter. Vad är korrekt för /tmp?',
        options: ['755', '777', '1777 (sticky bit)', '700'],
        correctIndex: 2, // C
        explanation: '1777 = rwxrwxrwt. Sticky bit gör att bara ägaren kan ta bort sina filer.',
        difficulty: 'VG',
        category: 'Best practices',
        scenario: 'Du granskar säkerheten på en server.',
        isScenario: true
    },
    {
        id: 't15-s4',
        question: 'ls -l visar -rwxr-sr-x. Vad betyder det lilla s:et?',
        options: ['SUID är satt', 'SGID är satt', 'Sticky bit', 'Symbolisk länk'],
        correctIndex: 1, // B
        explanation: 's i gruppens x-position = SGID. Filer körs med gruppens rättigheter.',
        difficulty: 'VG',
        category: 'Analys',
        scenario: 'Du granskar rättigheter på ett delat program.',
        isScenario: true
    },
    {
        id: 't15-s5',
        question: 'Applikationen kör som user "app" men kan inte skriva till /data som ägs av root. Bästa lösningen?',
        options: ['chmod 777 /data', 'chown app:app /data', 'Kör app som root', 'Skapa symlink'],
        correctIndex: 1, // B
        explanation: 'Ändra ägare till app-användaren. 777 är en säkerhetsrisk!',
        difficulty: 'VG',
        category: 'Best practices',
        scenario: 'Du deployer en ny applikation.',
        isScenario: true
    }
]

// =============================================================================
// TASK 16: SSH (20 quiz questions)
// =============================================================================

const TASK_16_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't16-q1',
        question: 'Vilken port använder SSH som standard?',
        options: ['21', '22', '23', '25'],
        correctIndex: 1, // B
        explanation: 'SSH använder port 22 som standard.',
        difficulty: 'G',
        category: 'Grunder'
    },
    {
        id: 't16-q2',
        question: 'Hur ansluter du till server som user?',
        options: ['ssh server user', 'ssh user@server', 'connect user server', 'ssh -u user server'],
        correctIndex: 1, // B
        explanation: 'ssh user@host är standardsyntax.',
        difficulty: 'G',
        category: 'Grundläggande'
    },
    {
        id: 't16-q3',
        question: 'Var lagras SSH-nycklar lokalt?',
        options: ['/etc/ssh/', '~/.ssh/', '/var/ssh/', '~/.keys/'],
        correctIndex: 1, // B
        explanation: '~/.ssh/ innehåller användarens nycklar.',
        difficulty: 'G',
        category: 'Nycklar'
    },
    {
        id: 't16-q4',
        question: 'Hur genererar du SSH-nyckelpar?',
        options: ['ssh-gen', 'ssh-keygen', 'ssh-create', 'keygen ssh'],
        correctIndex: 1, // B
        explanation: 'ssh-keygen skapar nya nyckelpar.',
        difficulty: 'G',
        category: 'Nycklar'
    },
    {
        id: 't16-q5',
        question: 'Var läggs auktoriserade nycklar på servern?',
        options: ['~/.ssh/keys', '~/.ssh/authorized_keys', '/etc/ssh/keys', '~/.authorized'],
        correctIndex: 1, // B
        explanation: 'authorized_keys innehåller tillåtna publika nycklar.',
        difficulty: 'G',
        category: 'Nycklar'
    },
    {
        id: 't16-q6',
        question: 'Hur kopierar du publik nyckel till server?',
        options: ['scp ~/.ssh/id_rsa.pub server:', 'ssh-copy-id user@server', 'ssh-send-key user@server', 'ssh-key-copy user@server'],
        correctIndex: 1, // B
        explanation: 'ssh-copy-id kopierar publik nyckel till authorized_keys.',
        difficulty: 'G',
        category: 'Nycklar'
    },
    {
        id: 't16-q7',
        question: 'Vilken fil konfigurerar SSH-servern?',
        options: ['/etc/sshd.conf', '/etc/ssh/sshd_config', '~/.ssh/server_config', '/etc/ssh.conf'],
        correctIndex: 1, // B
        explanation: 'sshd_config konfigurerar SSH-daemonen.',
        difficulty: 'G',
        category: 'Konfiguration'
    },
    {
        id: 't16-q8',
        question: 'Hur kopierar du fil till server?',
        options: ['cp -ssh fil server:', 'scp fil user@server:/path', 'ssh cp fil server', 'copy -r fil server'],
        correctIndex: 1, // B
        explanation: 'scp (secure copy) kopierar via SSH.',
        difficulty: 'G',
        category: 'scp'
    },
    {
        id: 't16-q9',
        question: 'Hur ansluter du på annan port (2222)?',
        options: ['ssh user@server 2222', 'ssh -p 2222 user@server', 'ssh --port 2222 user@server', 'ssh user@server:2222'],
        correctIndex: 1, // B
        explanation: '-p anger vilken port som ska användas.',
        difficulty: 'VG',
        category: 'Portar'
    },
    {
        id: 't16-q10',
        question: 'Hur inaktiverar du lösenordsinloggning?',
        options: ['DisablePassword yes', 'PasswordAuthentication no', 'NoPassword yes', 'AuthPassword no'],
        correctIndex: 1, // B
        explanation: 'PasswordAuthentication no i sshd_config.',
        difficulty: 'VG',
        category: 'Säkerhet'
    },
    {
        id: 't16-q11',
        question: 'Hur inaktiverar du root-login via SSH?',
        options: ['RootLogin no', 'PermitRootLogin no', 'DisableRoot yes', 'NoRootAccess yes'],
        correctIndex: 1, // B
        explanation: 'PermitRootLogin no blockerar root SSH.',
        difficulty: 'VG',
        category: 'Säkerhet'
    },
    {
        id: 't16-q12',
        question: 'Vilka rättigheter krävs på ~/.ssh/?',
        options: ['755', '700', '644', '600'],
        correctIndex: 1, // B
        explanation: '.ssh/ måste ha 700, nycklar 600.',
        difficulty: 'VG',
        category: 'Säkerhet'
    },
    {
        id: 't16-q13',
        question: 'Vad är ssh-agent?',
        options: ['SSH-proxy', 'Cachar nyckel-lösenord', 'SSH-monitor', 'Automatisk anslutning'],
        correctIndex: 1, // B
        explanation: 'ssh-agent håller dekrypterade nycklar i minnet.',
        difficulty: 'VG',
        category: 'Agent'
    },
    {
        id: 't16-q14',
        question: 'Hur skapar du lokal port tunnel?',
        options: ['ssh -T local:remote', 'ssh -L localport:host:remoteport', 'ssh --tunnel local:remote', 'ssh -p local:remote'],
        correctIndex: 1, // B
        explanation: '-L skapar local port forwarding.',
        difficulty: 'VG',
        category: 'Tunnlar'
    },
    {
        id: 't16-q15',
        question: 'Vad är known_hosts?',
        options: ['Lista över servrar', 'Sparade server-fingerprints', 'Blockerade hosts', 'DNS-cache'],
        correctIndex: 1, // B
        explanation: 'known_hosts sparar fingerprints för MITM-skydd.',
        difficulty: 'VG',
        category: 'Säkerhet'
    },
    {
        id: 't16-q16',
        question: 'Hur kör du kommando på remote server?',
        options: ['ssh server run command', 'ssh user@server "command"', 'ssh -c command server', 'ssh exec server command'],
        correctIndex: 1, // B
        explanation: 'Kommando efter host körs remote.',
        difficulty: 'VG',
        category: 'Kommandon'
    },
    {
        id: 't16-q17',
        question: 'Hur använder du specifik nyckel?',
        options: ['ssh -k key user@host', 'ssh -i keyfile user@host', 'ssh --key keyfile user@host', 'ssh -f keyfile user@host'],
        correctIndex: 1, // B
        explanation: '-i (identity) anger vilken nyckel som ska användas.',
        difficulty: 'VG',
        category: 'Flaggor'
    },
    {
        id: 't16-q18',
        question: 'Hur skapar du SOCKS-proxy med SSH?',
        options: ['ssh -S 1080 server', 'ssh -D 1080 server', 'ssh --socks 1080 server', 'ssh -proxy 1080 server'],
        correctIndex: 1, // B
        explanation: '-D skapar dynamic (SOCKS) port forwarding.',
        difficulty: 'VG',
        category: 'Tunnlar'
    },
    {
        id: 't16-q19',
        question: 'Hur gör du SSH via jump host?',
        options: ['ssh -j jump dest', 'ssh -J jumphost dest', 'ssh --jump jumphost dest', 'ssh -via jumphost dest'],
        correctIndex: 1, // B
        explanation: '-J (ProxyJump) hoppar via mellanserver.',
        difficulty: 'VG',
        category: 'Avancerat'
    },
    {
        id: 't16-q20',
        question: 'Hur debuggar du SSH-anslutning?',
        options: ['ssh --debug user@host', 'ssh -v user@host', 'ssh -d user@host', 'ssh --verbose user@host'],
        correctIndex: 1, // B
        explanation: '-v (verbose), -vv/-vvv för mer detalj.',
        difficulty: 'VG',
        category: 'Debug'
    },
    // SCENARIO-BASERADE FRÅGOR
    {
        id: 't16-s1',
        question: 'SSH säger "Permission denied (publickey)". Vad kollar du först?',
        options: ['DNS-inställningar', 'Att nyckeln finns i ~/.ssh/authorized_keys på servern', 'Brandväggsregler', 'SSH-version'],
        correctIndex: 1, // B
        explanation: 'Publik nyckel måste finnas i serverns authorized_keys för nyckelautentisering.',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'Du kan inte logga in på produktionsservern.',
        isScenario: true
    },
    {
        id: 't16-s2',
        question: 'SSH fungerade igår men idag får du "Host key verification failed". Vad hände?',
        options: ['Lösenord ändrat', 'Serverns host key ändrades (ny server/reinstall)', 'Fel användarnamn', 'Nätverksfel'],
        correctIndex: 1, // B
        explanation: 'Servern har ny identitet. Ta bort gammal nyckel: ssh-keygen -R hostname',
        difficulty: 'VG',
        category: 'Felsökning',
        scenario: 'Efter helgens underhåll fungerar inte SSH.',
        isScenario: true
    },
    {
        id: 't16-s3',
        question: 'Säkerhetsteamet kräver att root-login stängs av. Vilken fil och rad ändrar du?',
        options: ['/etc/ssh/ssh_config: PermitRoot no', '/etc/ssh/sshd_config: PermitRootLogin no', '/etc/passwd: root:x:0', '~/.ssh/config: NoRoot yes'],
        correctIndex: 1, // B
        explanation: 'sshd_config är serverns config. PermitRootLogin no stänger av root SSH.',
        difficulty: 'VG',
        category: 'Konfiguration',
        scenario: 'Du härdar säkerheten på alla servrar.',
        isScenario: true
    },
    {
        id: 't16-s4',
        question: 'Du vill kopiera din publika nyckel till ny server. Snabbaste sättet?',
        options: ['scp ~/.ssh/id_rsa.pub', 'ssh-copy-id user@server', 'cat id_rsa.pub | ssh user@server', 'rsync ~/.ssh/'],
        correctIndex: 1, // B
        explanation: 'ssh-copy-id kopierar automatiskt publik nyckel till rätt plats med rätt rättigheter.',
        difficulty: 'G',
        category: 'Best practices',
        scenario: 'Du sätter upp lösenordsfri inloggning.',
        isScenario: true
    },
    {
        id: 't16-s5',
        question: 'SSH säger "Permissions 0644 for id_rsa are too open". Lösning?',
        options: ['chmod 755 id_rsa', 'chmod 600 id_rsa', 'chmod 777 id_rsa', 'chown root id_rsa'],
        correctIndex: 1, // B
        explanation: 'Privata nycklar MÅSTE vara 600 (endast ägaren kan läsa). SSH vägrar annars.',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'Din SSH-nyckel fungerar inte efter att du kopierat den.',
        isScenario: true
    }
]

// =============================================================================
// TASK 17: UFW FIREWALL (20 quiz questions)
// =============================================================================

const TASK_17_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't17-q1',
        question: 'Vad står UFW för?',
        options: ['Ubuntu Firewall', 'Uncomplicated Firewall', 'Unix Firewall', 'Universal Firewall'],
        correctIndex: 1, // B
        explanation: 'UFW = Uncomplicated Firewall, ett enkelt iptables-frontend.',
        difficulty: 'G',
        category: 'Grunder'
    },
    {
        id: 't17-q2',
        question: 'Hur aktiverar du UFW?',
        options: ['ufw start', 'sudo ufw enable', 'systemctl start ufw', 'ufw on'],
        correctIndex: 1, // B
        explanation: 'sudo ufw enable aktiverar brandväggen.',
        difficulty: 'G',
        category: 'Grundläggande'
    },
    {
        id: 't17-q3',
        question: 'Hur visar du UFW-status?',
        options: ['ufw show', 'sudo ufw status', 'ufw list', 'ufw --status'],
        correctIndex: 1, // B
        explanation: 'sudo ufw status visar aktiva regler.',
        difficulty: 'G',
        category: 'Status'
    },
    {
        id: 't17-q4',
        question: 'Hur tillåter du SSH (port 22)?',
        options: ['ufw add ssh', 'sudo ufw allow 22', 'ufw open 22', 'ufw permit ssh'],
        correctIndex: 1, // B
        explanation: 'ufw allow 22 eller ufw allow ssh öppnar SSH.',
        difficulty: 'G',
        category: 'Regler'
    },
    {
        id: 't17-q5',
        question: 'Hur blockerar du en port?',
        options: ['ufw block 80', 'sudo ufw deny 80', 'ufw reject 80', 'ufw close 80'],
        correctIndex: 1, // B
        explanation: 'deny blockerar trafik till porten.',
        difficulty: 'G',
        category: 'Regler'
    },
    {
        id: 't17-q6',
        question: 'Vad är UFW default policy för incoming?',
        options: ['allow', 'deny', 'reject', 'drop'],
        correctIndex: 1, // B
        explanation: 'Default: deny incoming, allow outgoing.',
        difficulty: 'G',
        category: 'Policy'
    },
    {
        id: 't17-q7',
        question: 'Hur tar du bort en regel?',
        options: ['ufw remove 22', 'sudo ufw delete allow 22', 'ufw drop 22', 'ufw unset 22'],
        correctIndex: 1, // B
        explanation: 'delete + regelns exakta syntax tar bort den.',
        difficulty: 'G',
        category: 'Regler'
    },
    {
        id: 't17-q8',
        question: 'Hur återställer du UFW till default?',
        options: ['ufw default', 'sudo ufw reset', 'ufw factory', 'ufw clear'],
        correctIndex: 1, // B
        explanation: 'ufw reset tar bort alla regler.',
        difficulty: 'G',
        category: 'Reset'
    },
    {
        id: 't17-q9',
        question: 'Hur tillåter du specifik IP?',
        options: ['ufw allow ip 1.2.3.4', 'sudo ufw allow from 1.2.3.4', 'ufw permit 1.2.3.4', 'ufw accept 1.2.3.4'],
        correctIndex: 1, // B
        explanation: 'allow from IP tillåter all trafik från den IPn.',
        difficulty: 'VG',
        category: 'IP-regler'
    },
    {
        id: 't17-q10',
        question: 'Hur anger du protokoll (TCP)?',
        options: ['ufw allow 80 tcp', 'sudo ufw allow 80/tcp', 'ufw allow tcp:80', 'ufw allow --tcp 80'],
        correctIndex: 1, // B
        explanation: 'port/protokoll (80/tcp) anger specifikt protokoll.',
        difficulty: 'VG',
        category: 'Protokoll'
    },
    {
        id: 't17-q11',
        question: 'Hur tillåter du portintervall 6000-6010?',
        options: ['ufw allow 6000-6010', 'sudo ufw allow 6000:6010/tcp', 'ufw allow range 6000 6010', 'ufw allow [6000-6010]'],
        correctIndex: 1, // B
        explanation: 'start:slut/protokoll anger portintervall.',
        difficulty: 'VG',
        category: 'Regler'
    },
    {
        id: 't17-q12',
        question: 'Hur visar du numrerade regler?',
        options: ['ufw status numbers', 'sudo ufw status numbered', 'ufw list numbered', 'ufw show numbers'],
        correctIndex: 1, // B
        explanation: 'numbered visar radnummer för enkel borttagning.',
        difficulty: 'VG',
        category: 'Status'
    },
    {
        id: 't17-q13',
        question: 'Hur aktiverar du loggning?',
        options: ['ufw log on', 'sudo ufw logging on', 'ufw enable logging', 'ufw --log'],
        correctIndex: 1, // B
        explanation: 'ufw logging on aktiverar brandväggsloggning.',
        difficulty: 'VG',
        category: 'Loggning'
    },
    {
        id: 't17-q14',
        question: 'Var sparas UFW-loggar?',
        options: ['/var/log/firewall.log', '/var/log/ufw.log', '/var/log/iptables.log', '/var/log/syslog'],
        correctIndex: 1, // B
        explanation: 'UFW loggar till /var/log/ufw.log.',
        difficulty: 'VG',
        category: 'Loggning'
    },
    {
        id: 't17-q15',
        question: 'Hur tillåter du IP till specifik port?',
        options: ['ufw allow 1.2.3.4 port 22', 'sudo ufw allow from 1.2.3.4 to any port 22', 'ufw allow 1.2.3.4:22', 'ufw allow --source 1.2.3.4 --port 22'],
        correctIndex: 1, // B
        explanation: 'from IP to any port X är korrekt syntax.',
        difficulty: 'VG',
        category: 'IP-regler'
    },
    {
        id: 't17-q16',
        question: 'Vad gör limit-regeln?',
        options: ['Begränsar bandbredd', 'Rate limit - blockerar vid för många anslutningar', 'Begränsar filstorlek', 'Tidsbegränsning'],
        correctIndex: 1, // B
        explanation: 'limit blockerar efter 6 anslutningar på 30 sek.',
        difficulty: 'VG',
        category: 'Säkerhet'
    },
    {
        id: 't17-q17',
        question: 'Hur använder du application profiles?',
        options: ['ufw app allow Nginx', 'sudo ufw allow "Nginx Full"', 'ufw profile Nginx', 'ufw service nginx'],
        correctIndex: 1, // B
        explanation: 'Fördefinierade app-profiler i /etc/ufw/applications.d/.',
        difficulty: 'VG',
        category: 'Profiler'
    },
    {
        id: 't17-q18',
        question: 'Hur listar du tillgängliga app-profiler?',
        options: ['ufw apps', 'sudo ufw app list', 'ufw profiles', 'ufw --list-apps'],
        correctIndex: 1, // B
        explanation: 'app list visar alla installerade profiler.',
        difficulty: 'VG',
        category: 'Profiler'
    },
    {
        id: 't17-q19',
        question: 'Hur infogar du regel på specifik position?',
        options: ['ufw add 1 deny', 'sudo ufw insert 1 deny from 1.2.3.4', 'ufw prepend deny', 'ufw position 1 deny'],
        correctIndex: 1, // B
        explanation: 'insert N lägger till regel på position N.',
        difficulty: 'VG',
        category: 'Regler'
    },
    {
        id: 't17-q20',
        question: 'Hur tillåter du interface-specifik trafik?',
        options: ['ufw allow eth0', 'sudo ufw allow in on eth0', 'ufw interface eth0 allow', 'ufw --interface eth0 allow'],
        correctIndex: 1, // B
        explanation: 'in on INTERFACE begränsar till specifikt nätverkskort.',
        difficulty: 'VG',
        category: 'Interface'
    },
    // SCENARIO-BASERADE FRÅGOR
    {
        id: 't17-s1',
        question: 'Du körde ufw enable och nu kan du inte SSHa in. Vad hände troligen?',
        options: ['SSH-tjänsten stoppades', 'Du glömde ufw allow ssh före enable', 'Servern omstartade', 'UFW blockerade utgående'],
        correctIndex: 1, // B
        explanation: 'UFW default nekar allt inkommande. ALLTID tillåt SSH före enable!',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'Servern blev oåtkomlig efter brandväggskonfiguration.',
        isScenario: true
    },
    {
        id: 't17-s2',
        question: 'Webservern svarar inte på port 443. ufw status visar endast port 80 tillåten. Fix?',
        options: ['ufw allow https', 'ufw allow 443/tcp', 'ufw allow 443', 'Alla ovan fungerar'],
        correctIndex: 3, // D
        explanation: 'Alla tre fungerar. https är alias för 443/tcp.',
        difficulty: 'G',
        category: 'Praktisk',
        scenario: 'HTTPS fungerar inte trots korrekt nginx-config.',
        isScenario: true
    },
    {
        id: 't17-s3',
        question: 'Du vill tillåta SSH endast från kontorets IP 10.0.1.50. Rätt kommando?',
        options: ['ufw allow ssh from 10.0.1.50', 'ufw allow from 10.0.1.50 to any port 22', 'ufw limit from 10.0.1.50', 'ufw allow 22 --source 10.0.1.50'],
        correctIndex: 1, // B
        explanation: 'ufw allow from IP to any port PORT är korrekt syntax för IP-begränsning.',
        difficulty: 'VG',
        category: 'Avancerat',
        scenario: 'Säkerhetsteamet kräver SSH-åtkomst endast från kontoret.',
        isScenario: true
    }
]

// =============================================================================
// TASK 18: FIREWALLD (20 quiz questions)
// =============================================================================

const TASK_18_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't18-q1',
        question: 'Vad är firewalld?',
        options: ['Statisk brandvägg', 'Dynamisk zonbaserad brandvägg', 'Proxy-server', 'VPN-tjänst'],
        correctIndex: 1, // B
        explanation: 'firewalld är dynamisk och använder zoner för säkerhetsnivåer.',
        difficulty: 'G',
        category: 'Grunder'
    },
    {
        id: 't18-q2',
        question: 'Hur visar du firewalld status?',
        options: ['firewalld status', 'sudo firewall-cmd --state', 'firewall-cmd status', 'systemctl state firewalld'],
        correctIndex: 1, // B
        explanation: '--state visar om firewalld är running.',
        difficulty: 'G',
        category: 'Status'
    },
    {
        id: 't18-q3',
        question: 'Vad är en zon i firewalld?',
        options: ['Tidszon', 'Fördefinierad säkerhetsnivå', 'Nätverkssegment', 'DNS-zon'],
        correctIndex: 1, // B
        explanation: 'Zoner har olika säkerhetsnivåer (public, trusted, etc.).',
        difficulty: 'G',
        category: 'Zoner'
    },
    {
        id: 't18-q4',
        question: 'Hur listar du alla zoner?',
        options: ['firewall-cmd --zones', 'sudo firewall-cmd --get-zones', 'firewall-cmd list zones', 'firewall-cmd --show-zones'],
        correctIndex: 1, // B
        explanation: '--get-zones listar alla tillgängliga zoner.',
        difficulty: 'G',
        category: 'Zoner'
    },
    {
        id: 't18-q5',
        question: 'Hur tillåter du en tjänst?',
        options: ['firewall-cmd --allow ssh', 'sudo firewall-cmd --add-service=ssh', 'firewall-cmd --service ssh', 'firewall-cmd --enable ssh'],
        correctIndex: 1, // B
        explanation: '--add-service=namn lägger till tjänst.',
        difficulty: 'G',
        category: 'Tjänster'
    },
    {
        id: 't18-q6',
        question: 'Hur tillåter du en port?',
        options: ['firewall-cmd --allow 80', 'sudo firewall-cmd --add-port=80/tcp', 'firewall-cmd --port 80', 'firewall-cmd --open 80'],
        correctIndex: 1, // B
        explanation: '--add-port=port/protokoll öppnar porten.',
        difficulty: 'G',
        category: 'Portar'
    },
    {
        id: 't18-q7',
        question: 'Vad gör --permanent?',
        options: ['Låser regeln', 'Sparar regeln permanent', 'Gör regeln oföränderlig', 'Aktiverar permanent läge'],
        correctIndex: 1, // B
        explanation: '--permanent sparar regeln så den överlever reboot.',
        difficulty: 'G',
        category: 'Permanent'
    },
    {
        id: 't18-q8',
        question: 'Hur laddar du om firewalld?',
        options: ['firewall-cmd --restart', 'sudo firewall-cmd --reload', 'systemctl reload firewall', 'firewall-cmd --refresh'],
        correctIndex: 1, // B
        explanation: '--reload läser in permanenta ändringar.',
        difficulty: 'G',
        category: 'Reload'
    },
    {
        id: 't18-q9',
        question: 'Hur visar du aktiva zoner?',
        options: ['firewall-cmd --zones', 'sudo firewall-cmd --get-active-zones', 'firewall-cmd --active', 'firewall-cmd --list-zones'],
        correctIndex: 1, // B
        explanation: '--get-active-zones visar zoner med interface.',
        difficulty: 'VG',
        category: 'Zoner'
    },
    {
        id: 't18-q10',
        question: 'Hur listar du alla regler i default-zonen?',
        options: ['firewall-cmd --rules', 'sudo firewall-cmd --list-all', 'firewall-cmd --show', 'firewall-cmd --dump'],
        correctIndex: 1, // B
        explanation: '--list-all visar alla inställningar för zonen.',
        difficulty: 'VG',
        category: 'Regler'
    },
    {
        id: 't18-q11',
        question: 'Hur anger du specifik zon för regel?',
        options: ['--zone public', 'sudo firewall-cmd --zone=public --add-service=http', '--in-zone public', '--target public'],
        correctIndex: 1, // B
        explanation: '--zone=zonnamn anger vilken zon som påverkas.',
        difficulty: 'VG',
        category: 'Zoner'
    },
    {
        id: 't18-q12',
        question: 'Hur ändrar du default-zon?',
        options: ['firewall-cmd --default public', 'sudo firewall-cmd --set-default-zone=public', 'firewall-cmd --change-default public', 'firewall-cmd --zone-default public'],
        correctIndex: 1, // B
        explanation: '--set-default-zone=namn ändrar standard.',
        difficulty: 'VG',
        category: 'Zoner'
    },
    {
        id: 't18-q13',
        question: 'Hur tar du bort en tjänst?',
        options: ['firewall-cmd --delete-service', 'sudo firewall-cmd --remove-service=http', 'firewall-cmd --drop-service', 'firewall-cmd --disable-service'],
        correctIndex: 1, // B
        explanation: '--remove-service=namn tar bort tjänsten.',
        difficulty: 'VG',
        category: 'Tjänster'
    },
    {
        id: 't18-q14',
        question: 'Hur listar du tillgängliga tjänster?',
        options: ['firewall-cmd --services', 'sudo firewall-cmd --get-services', 'firewall-cmd --list-services', 'firewall-cmd --show-services'],
        correctIndex: 1, // B
        explanation: '--get-services listar fördefinierade tjänster.',
        difficulty: 'VG',
        category: 'Tjänster'
    },
    {
        id: 't18-q15',
        question: 'Vad är rich rules?',
        options: ['Rika användares regler', 'Avancerade regler med fler villkor', 'Betalda regler', 'Krypterade regler'],
        correctIndex: 1, // B
        explanation: 'Rich rules tillåter komplexa villkor (IP, loggning etc.).',
        difficulty: 'VG',
        category: 'Rich Rules'
    },
    {
        id: 't18-q16',
        question: 'Vad är panic mode?',
        options: ['Stänger av systemet', 'Blockerar ALL nätverkstrafik', 'Startar om brandväggen', 'Skickar alarm'],
        correctIndex: 1, // B
        explanation: '--panic-on blockerar allt - endast för nödsituationer!',
        difficulty: 'VG',
        category: 'Säkerhet'
    },
    {
        id: 't18-q17',
        question: 'Hur flyttar du interface till annan zon?',
        options: ['firewall-cmd --move-interface', 'sudo firewall-cmd --zone=trusted --change-interface=eth1', 'firewall-cmd --interface eth1 --zone trusted', 'firewall-cmd --set-interface'],
        correctIndex: 1, // B
        explanation: '--zone=X --change-interface=Y flyttar interface.',
        difficulty: 'VG',
        category: 'Interface'
    },
    {
        id: 't18-q18',
        question: 'Hur aktiverar du port forwarding?',
        options: ['firewall-cmd --forward', 'sudo firewall-cmd --add-forward-port=port=80:proto=tcp:toport=8080', 'firewall-cmd --port-forward', 'firewall-cmd --nat'],
        correctIndex: 1, // B
        explanation: '--add-forward-port konfigurerar port forwarding.',
        difficulty: 'VG',
        category: 'Forwarding'
    },
    {
        id: 't18-q19',
        question: 'Var lagras firewalld-konfiguration?',
        options: ['/etc/firewall/', '/etc/firewalld/', '/var/firewalld/', '/usr/firewalld/'],
        correctIndex: 1, // B
        explanation: '/etc/firewalld/ innehåller användarkonfiguration.',
        difficulty: 'VG',
        category: 'Konfiguration'
    },
    {
        id: 't18-q20',
        question: 'Hur synkar du runtime-regler till permanent?',
        options: ['firewall-cmd --save', 'sudo firewall-cmd --runtime-to-permanent', 'firewall-cmd --persist', 'firewall-cmd --commit'],
        correctIndex: 1, // B
        explanation: '--runtime-to-permanent sparar alla aktiva ändringar.',
        difficulty: 'VG',
        category: 'Synk'
    }
]

// =============================================================================
// TASK 21: SYSTEMD (20 quiz)
// =============================================================================

const TASK_21_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't21-q1',
        question: 'Vad är systemd?',
        options: ['Filhanterare', 'Init-system och servicehanterare', 'Texteditor', 'Nätverksprotokoll'],
        correctIndex: 1, // B
        explanation: 'systemd är init-system (PID 1) och hanterar tjänster.',
        difficulty: 'G',
        category: 'Grunder'
    },
    {
        id: 't21-q2',
        question: 'Hur startar du nginx-tjänsten?',
        options: ['start nginx', 'service nginx start', 'systemctl start nginx', 'nginx --start'],
        correctIndex: 2, // C
        explanation: 'systemctl start <tjänst> startar en systemd-tjänst.',
        difficulty: 'G',
        category: 'Tjänster'
    },
    {
        id: 't21-q3',
        question: 'Hur visar du status för en tjänst?',
        options: ['systemctl info nginx', 'systemctl status nginx', 'systemctl show nginx', 'systemctl check nginx'],
        correctIndex: 1, // B
        explanation: 'systemctl status visar state, PID och senaste loggar.',
        difficulty: 'G',
        category: 'Status'
    },
    {
        id: 't21-q4',
        question: 'Hur aktiverar du tjänst vid systemstart?',
        options: ['systemctl boot nginx', 'systemctl autostart nginx', 'systemctl enable nginx', 'systemctl startup nginx'],
        correctIndex: 2, // C
        explanation: 'systemctl enable skapar symlink för autostart vid boot.',
        difficulty: 'G',
        category: 'Boot'
    },
    {
        id: 't21-q5',
        question: 'Var finns systemd unit-filer?',
        options: ['/var/systemd/', '/etc/systemd/system/', '/usr/systemd/', '/opt/systemd/'],
        correctIndex: 1, // B
        explanation: '/etc/systemd/system/ för custom units, /lib/systemd/system/ för default.',
        difficulty: 'G',
        category: 'Filer'
    },
    {
        id: 't21-q6',
        question: 'Hur listar du alla tjänster?',
        options: ['systemctl list-all', 'systemctl list-units --type=service', 'systemctl services', 'systemctl --list'],
        correctIndex: 1, // B
        explanation: 'list-units --type=service visar alla servicetjänster.',
        difficulty: 'G',
        category: 'Listing'
    },
    {
        id: 't21-q7',
        question: 'Vad gör systemctl daemon-reload?',
        options: ['Startar om alla tjänster', 'Laddar om unit-filer', 'Stänger av systemd', 'Rensar loggar'],
        correctIndex: 1, // B
        explanation: 'daemon-reload läser in ändringar i unit-filer.',
        difficulty: 'G',
        category: 'Reload'
    },
    {
        id: 't21-q8',
        question: 'Hur stoppar du en tjänst?',
        options: ['systemctl kill nginx', 'systemctl stop nginx', 'systemctl end nginx', 'systemctl quit nginx'],
        correctIndex: 1, // B
        explanation: 'systemctl stop skickar SIGTERM för graceful shutdown.',
        difficulty: 'G',
        category: 'Tjänster'
    },
    {
        id: 't21-q9',
        question: 'Hur startar OCH aktiverar du tjänst samtidigt?',
        options: ['systemctl start enable nginx', 'systemctl enable --now nginx', 'systemctl start+enable nginx', 'systemctl autorun nginx'],
        correctIndex: 1, // B
        explanation: 'enable --now aktiverar för boot OCH startar direkt.',
        difficulty: 'G',
        category: 'Boot'
    },
    {
        id: 't21-q10',
        question: 'Vad är en unit i systemd?',
        options: ['En användare', 'Resursobjekt (service, timer, mount)', 'En loggfil', 'En katalog'],
        correctIndex: 1, // B
        explanation: 'Units är resurser: .service, .timer, .mount, .socket etc.',
        difficulty: 'G',
        category: 'Koncept'
    },
    {
        id: 't21-q11',
        question: 'Hur visar du loggar för en tjänst?',
        options: ['systemctl log nginx', 'journalctl -u nginx', 'systemd-log nginx', 'logctl nginx'],
        correctIndex: 1, // B
        explanation: 'journalctl -u <tjänst> visar loggar från journald.',
        difficulty: 'VG',
        category: 'Logging'
    },
    {
        id: 't21-q12',
        question: 'Vad gör [Install] sektionen i unit-fil?',
        options: ['Installerar programvara', 'Definierar när tjänst aktiveras', 'Listar beroenden', 'Sätter miljövariabler'],
        correctIndex: 1, // B
        explanation: '[Install] definierar WantedBy/RequiredBy för enable/disable.',
        difficulty: 'VG',
        category: 'Unit-fil'
    },
    {
        id: 't21-q13',
        question: 'Hur visar du misslyckade tjänster?',
        options: ['systemctl --errors', 'systemctl --failed', 'systemctl list-errors', 'journalctl --failed'],
        correctIndex: 1, // B
        explanation: 'systemctl --failed listar tjänster i failed state.',
        difficulty: 'VG',
        category: 'Status'
    },
    {
        id: 't21-q14',
        question: 'Vad gör Restart=always i [Service]?',
        options: ['Startar om vid uppdatering', 'Startar om automatiskt vid krasch', 'Kräver manuell restart', 'Ignorerar fel'],
        correctIndex: 1, // B
        explanation: 'Restart=always startar om tjänsten oavsett hur den avslutas.',
        difficulty: 'VG',
        category: 'Unit-fil'
    },
    {
        id: 't21-q15',
        question: 'Hur skapar du systemd timer?',
        options: ['crontab -e', 'Skapa .timer unit-fil', 'systemctl create timer', 'at-kommandot'],
        correctIndex: 1, // B
        explanation: 'Timer units (.timer) ersätter cron i systemd.',
        difficulty: 'VG',
        category: 'Timer'
    },
    {
        id: 't21-q16',
        question: 'Hur maskerar du en tjänst helt?',
        options: ['systemctl hide nginx', 'systemctl mask nginx', 'systemctl disable --force nginx', 'systemctl block nginx'],
        correctIndex: 1, // B
        explanation: 'mask förhindrar att tjänsten kan startas alls.',
        difficulty: 'VG',
        category: 'Säkerhet'
    },
    {
        id: 't21-q17',
        question: 'Vad är multi-user.target?',
        options: ['Grafiskt läge', 'Textläge med nätverk', 'Single user mode', 'Maintenance mode'],
        correctIndex: 1, // B
        explanation: 'multi-user.target ≈ runlevel 3 (text, nätverk, ingen GUI).',
        difficulty: 'VG',
        category: 'Targets'
    },
    {
        id: 't21-q18',
        question: 'Hur ser du aktuellt default target?',
        options: ['systemctl target', 'systemctl get-default', 'systemctl show-target', 'systemctl default'],
        correctIndex: 1, // B
        explanation: 'get-default visar vilket target som startas vid boot.',
        difficulty: 'VG',
        category: 'Targets'
    },
    {
        id: 't21-q19',
        question: 'Hur sätter du environment i unit-fil?',
        options: ['ENV=value', 'Environment="VAR=value"', 'export VAR=value', 'set VAR value'],
        correctIndex: 1, // B
        explanation: 'Environment= i [Service] sätter miljövariabler.',
        difficulty: 'VG',
        category: 'Config'
    },
    {
        id: 't21-q20',
        question: 'Vad gör journalctl -f?',
        options: ['Filtrerar loggar', 'Följer loggar live', 'Formaterar output', 'Visar fullständiga loggar'],
        correctIndex: 1, // B
        explanation: '-f (follow) visar nya loggar i realtid.',
        difficulty: 'VG',
        category: 'Logging'
    },
    // SCENARIO-BASERADE FRÅGOR
    {
        id: 't21-s1',
        question: 'Du ändrade en .service-fil men restart tar inte effekt. Vad glömde du?',
        options: ['systemctl reload', 'systemctl daemon-reload före restart', 'chmod +x på filen', 'Starta om servern'],
        correctIndex: 1, // B
        explanation: 'Efter att ändra unit-filer MÅSTE du köra daemon-reload så systemd läser om dem.',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'Tjänsten använder fortfarande gamla inställningar.',
        isScenario: true
    },
    {
        id: 't21-s2',
        question: 'Tjänsten startar vid boot men kraschar direkt. Hur felsöker du?',
        options: ['cat /var/log/service.log', 'journalctl -u tjänstnamn', 'systemctl debug tjänst', 'tail /etc/systemd/logs'],
        correctIndex: 1, // B
        explanation: 'journalctl -u tjänst visar tjänstens loggar inklusive startfel.',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'Applikationen fungerar manuellt men inte som service.',
        isScenario: true
    },
    {
        id: 't21-s3',
        question: 'Du vill att tjänsten startar automatiskt EFTER att nätverket är uppe. Var konfigurerar du det?',
        options: ['[Service] After=network.target', '[Unit] After=network.target', '[Install] WantedBy=network', 'I /etc/rc.local'],
        correctIndex: 1, // B
        explanation: 'I [Unit]-sektionen anger After= beroenden som måste starta först.',
        difficulty: 'VG',
        category: 'Konfiguration',
        scenario: 'Tjänsten kraschar vid boot men fungerar om du startar den manuellt efteråt.',
        isScenario: true
    }
]

// =============================================================================
// TASK 22: DOCKER GRUNDER (20 quiz)
// =============================================================================

const TASK_22_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't22-q1',
        question: 'Vad är huvudskillnaden mellan container och VM?',
        options: ['Containers är snabbare', 'Containers delar värdkärna, VM har eget OS', 'VM är gratis', 'Containers kräver mer minne'],
        correctIndex: 1, // B
        explanation: 'Containers delar Linux-kärnan, VM kör helt eget operativsystem.',
        difficulty: 'G',
        category: 'Koncept'
    },
    {
        id: 't22-q2',
        question: 'Hur startar du en nginx-container?',
        options: ['docker start nginx', 'docker run nginx', 'docker create nginx', 'docker launch nginx'],
        correctIndex: 1, // B
        explanation: 'docker run skapar och startar container från image.',
        difficulty: 'G',
        category: 'run'
    },
    {
        id: 't22-q3',
        question: 'Hur listar du körande containers?',
        options: ['docker list', 'docker ps', 'docker show', 'docker containers'],
        correctIndex: 1, // B
        explanation: 'docker ps (process status) visar körande containers.',
        difficulty: 'G',
        category: 'Listing'
    },
    {
        id: 't22-q4',
        question: 'Vilken flagga kör container i bakgrunden?',
        options: ['-b', '-d', '-r', '-bg'],
        correctIndex: 1, // B
        explanation: '-d (detached) kör container i bakgrunden.',
        difficulty: 'G',
        category: 'run'
    },
    {
        id: 't22-q5',
        question: 'Hur stoppar du en container?',
        options: ['docker kill myapp', 'docker stop myapp', 'docker end myapp', 'docker quit myapp'],
        correctIndex: 1, // B
        explanation: 'docker stop skickar SIGTERM för graceful shutdown.',
        difficulty: 'G',
        category: 'Lifecycle'
    },
    {
        id: 't22-q6',
        question: 'Hur tar du bort en container?',
        options: ['docker delete', 'docker rm', 'docker remove', 'docker destroy'],
        correctIndex: 1, // B
        explanation: 'docker rm tar bort stoppade containers.',
        difficulty: 'G',
        category: 'Lifecycle'
    },
    {
        id: 't22-q7',
        question: 'Hur listar du alla containers inklusive stoppade?',
        options: ['docker ps --all', 'docker ps -a', 'docker ps -s', 'docker list all'],
        correctIndex: 1, // B
        explanation: '-a (all) visar alla containers oavsett state.',
        difficulty: 'G',
        category: 'Listing'
    },
    {
        id: 't22-q8',
        question: 'Hur namnger du en container?',
        options: ['docker run -n myapp image', 'docker run --name myapp image', 'docker run --id myapp image', 'docker run myapp image'],
        correctIndex: 1, // B
        explanation: '--name ger containern ett specifikt namn.',
        difficulty: 'G',
        category: 'run'
    },
    {
        id: 't22-q9',
        question: 'Hur visar du container-loggar?',
        options: ['docker output', 'docker logs', 'docker show', 'docker print'],
        correctIndex: 1, // B
        explanation: 'docker logs visar stdout/stderr från containern.',
        difficulty: 'G',
        category: 'Logs'
    },
    {
        id: 't22-q10',
        question: 'Hur listar du Docker images?',
        options: ['docker list images', 'docker images', 'docker show images', 'docker img'],
        correctIndex: 1, // B
        explanation: 'docker images listar alla lokala images.',
        difficulty: 'G',
        category: 'Images'
    },
    {
        id: 't22-q11',
        question: 'Hur mappar du port 8080 på host till 80 i container?',
        options: ['docker run -p 80:8080', 'docker run -p 8080:80', 'docker run --port 8080=80', 'docker run -P 8080:80'],
        correctIndex: 1, // B
        explanation: '-p HOST:CONTAINER, så 8080:80 = host 8080 → container 80.',
        difficulty: 'VG',
        category: 'Networking'
    },
    {
        id: 't22-q12',
        question: 'Hur kör du interaktiv bash i container?',
        options: ['docker run -i bash image', 'docker run -it image bash', 'docker bash image', 'docker exec bash image'],
        correctIndex: 1, // B
        explanation: '-it (interactive + tty) ger interaktiv terminal.',
        difficulty: 'VG',
        category: 'run'
    },
    {
        id: 't22-q13',
        question: 'Hur monterar du katalog från host?',
        options: ['docker run -m /host:/cont', 'docker run -v /host:/container', 'docker run --mount /host /container', 'docker run -d /host:/cont'],
        correctIndex: 1, // B
        explanation: '-v HOST:CONTAINER monterar host-katalog i container.',
        difficulty: 'VG',
        category: 'Volumes'
    },
    {
        id: 't22-q14',
        question: 'Hur sätter du miljövariabel i container?',
        options: ['docker run -v VAR=val', 'docker run -e VAR=value', 'docker run --set VAR=val', 'docker run -E VAR=val'],
        correctIndex: 1, // B
        explanation: '-e (environment) sätter miljövariabler.',
        difficulty: 'VG',
        category: 'Config'
    },
    {
        id: 't22-q15',
        question: 'Hur kör du kommando i körande container?',
        options: ['docker run -it container bash', 'docker exec -it container bash', 'docker attach container bash', 'docker shell container'],
        correctIndex: 1, // B
        explanation: 'docker exec kör nytt kommando i existerande container.',
        difficulty: 'VG',
        category: 'exec'
    },
    {
        id: 't22-q16',
        question: 'Vad gör --rm flaggan?',
        options: ['Tar bort image', 'Tar bort container när den avslutas', 'Startar om container', 'Tar bort volymer'],
        correctIndex: 1, // B
        explanation: '--rm tar automatiskt bort containern vid exit.',
        difficulty: 'VG',
        category: 'run'
    },
    {
        id: 't22-q17',
        question: 'Hur begränsar du minne till 512MB?',
        options: ['docker run -mem 512', 'docker run -m 512m', 'docker run --memory-limit 512', 'docker run -r 512mb'],
        correctIndex: 1, // B
        explanation: '-m/--memory begränsar containerns minnesanvändning.',
        difficulty: 'VG',
        category: 'Resurser'
    },
    {
        id: 't22-q18',
        question: 'Hur inspekterar du container-metadata?',
        options: ['docker info container', 'docker inspect container', 'docker show container', 'docker meta container'],
        correctIndex: 1, // B
        explanation: 'docker inspect visar all metadata som JSON.',
        difficulty: 'VG',
        category: 'Info'
    },
    {
        id: 't22-q19',
        question: 'Hur skapar du eget nätverk?',
        options: ['docker net create mynet', 'docker network create mynet', 'docker create network mynet', 'docker new network mynet'],
        correctIndex: 1, // B
        explanation: 'docker network create skapar isolerat nätverk.',
        difficulty: 'VG',
        category: 'Networking'
    },
    {
        id: 't22-q20',
        question: 'Hur visar du resursanvändning live?',
        options: ['docker top', 'docker stats', 'docker usage', 'docker monitor'],
        correctIndex: 1, // B
        explanation: 'docker stats visar CPU, minne, nätverk i realtid.',
        difficulty: 'VG',
        category: 'Monitoring'
    },
    // SCENARIO-BASERADE FRÅGOR
    {
        id: 't22-s1',
        question: 'Container startar men avslutas direkt. Hur ser du vad som hände?',
        options: ['docker ps', 'docker logs <container>', 'docker top', 'docker info'],
        correctIndex: 1, // B
        explanation: 'docker logs visar stdout/stderr från containern, även efter att den stoppat.',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'Din nginx-container kraschar direkt vid start.',
        isScenario: true
    },
    {
        id: 't22-s2',
        question: 'Du vill debugga inuti en körande container. Vilket kommando?',
        options: ['docker run -it container bash', 'docker exec -it container bash', 'docker attach container', 'docker debug container'],
        correctIndex: 1, // B
        explanation: 'docker exec -it startar ny process inuti körande container. -it ger interaktiv terminal.',
        difficulty: 'G',
        category: 'Felsökning',
        scenario: 'Du behöver kolla config-filer inuti containern.',
        isScenario: true
    },
    {
        id: 't22-s3',
        question: 'Containern tar för mycket minne. Hur begränsar du den till max 512MB?',
        options: ['docker run --memory=512m', 'docker run --ram=512m', 'docker run --limit-mem=512m', 'docker run -m 512'],
        correctIndex: 0, // A
        explanation: '--memory=512m (eller -m 512m) sätter minnestak för containern.',
        difficulty: 'VG',
        category: 'Resurser',
        scenario: 'En container äter allt RAM på servern.',
        isScenario: true
    },
    {
        id: 't22-s4',
        question: 'Du vill att containern startar automatiskt om servern bootar om. Vilken flagga?',
        options: ['--autostart', '--restart=always', '--boot=yes', '--daemon'],
        correctIndex: 1, // B
        explanation: '--restart=always gör att Docker alltid startar containern, även efter reboot.',
        difficulty: 'VG',
        category: 'Konfiguration',
        scenario: 'Databasen måste starta automatiskt efter strömavbrott.',
        isScenario: true
    },
    {
        id: 't22-s5',
        question: 'Port 80 på hosten är upptagen. Hur mappar du nginx till port 8080 istället?',
        options: ['-p 80:8080', '-p 8080:80', '--port 8080=80', '-expose 8080'],
        correctIndex: 1, // B
        explanation: '-p host:container. 8080:80 = hostens 8080 mappas till containerns 80.',
        difficulty: 'G',
        category: 'Nätverk',
        scenario: 'Apache kör redan på port 80 på servern.',
        isScenario: true
    }
]

// =============================================================================
// TASK 23: DOCKER IMAGES (20 quiz)
// =============================================================================

const TASK_23_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't23-q1',
        question: 'Vad är en Dockerfile?',
        options: ['Container-logg', 'Instruktionsfil för att bygga image', 'Konfigurationsfil för Docker', 'Nätverkskonfiguration'],
        correctIndex: 1, // B
        explanation: 'Dockerfile innehåller instruktioner för att bygga en Docker image.',
        difficulty: 'G',
        category: 'Grunder'
    },
    {
        id: 't23-q2',
        question: 'Hur bygger du image med taggen "myapp:1.0"?',
        options: ['docker build myapp:1.0', 'docker build -t myapp:1.0 .', 'docker create -t myapp:1.0', 'docker make myapp:1.0'],
        correctIndex: 1, // B
        explanation: 'docker build -t <tag> <context> bygger och taggar image.',
        difficulty: 'G',
        category: 'Build'
    },
    {
        id: 't23-q3',
        question: 'Vad gör FROM i Dockerfile?',
        options: ['Kopierar filer', 'Anger basimage', 'Kör kommando', 'Sätter port'],
        correctIndex: 1, // B
        explanation: 'FROM anger vilken basimage som ska användas.',
        difficulty: 'G',
        category: 'Dockerfile'
    },
    {
        id: 't23-q4',
        question: 'Vad gör RUN i Dockerfile?',
        options: ['Startar container', 'Kör kommando vid build', 'Anger startkommando', 'Kopierar filer'],
        correctIndex: 1, // B
        explanation: 'RUN kör kommandon under image-bygget.',
        difficulty: 'G',
        category: 'Dockerfile'
    },
    {
        id: 't23-q5',
        question: 'Vad gör COPY i Dockerfile?',
        options: ['Klonar repository', 'Kopierar filer till image', 'Kopierar från annan image', 'Skapar backup'],
        correctIndex: 1, // B
        explanation: 'COPY kopierar filer från build context till image.',
        difficulty: 'G',
        category: 'Dockerfile'
    },
    {
        id: 't23-q6',
        question: 'Vad gör CMD i Dockerfile?',
        options: ['Kör vid build', 'Anger default-kommando vid run', 'Kommentar', 'Kontrollerar minne'],
        correctIndex: 1, // B
        explanation: 'CMD anger vad som körs när containern startar.',
        difficulty: 'G',
        category: 'Dockerfile'
    },
    {
        id: 't23-q7',
        question: 'Vad gör WORKDIR i Dockerfile?',
        options: ['Skapar katalog på host', 'Sätter arbetskatalog i image', 'Monterar volym', 'Anger byggkatalog'],
        correctIndex: 1, // B
        explanation: 'WORKDIR sätter arbetskatalog för efterföljande kommandon.',
        difficulty: 'G',
        category: 'Dockerfile'
    },
    {
        id: 't23-q8',
        question: 'Hur pushar du image till Docker Hub?',
        options: ['docker upload image', 'docker push user/image', 'docker send image', 'docker publish image'],
        correctIndex: 1, // B
        explanation: 'docker push skickar image till registry (kräver login).',
        difficulty: 'G',
        category: 'Registry'
    },
    {
        id: 't23-q9',
        question: 'Vad är .dockerignore?',
        options: ['Lista över ignorerade containers', 'Exkluderar filer från build', 'Ignorerade nätverk', 'Blockerade images'],
        correctIndex: 1, // B
        explanation: '.dockerignore exkluderar filer/kataloger från build context.',
        difficulty: 'G',
        category: 'Build'
    },
    {
        id: 't23-q10',
        question: 'Hur tar du bort en image?',
        options: ['docker delete image', 'docker rmi image', 'docker remove image', 'docker rm image'],
        correctIndex: 1, // B
        explanation: 'docker rmi (remove image) tar bort images.',
        difficulty: 'G',
        category: 'Cleanup'
    },
    {
        id: 't23-q11',
        question: 'Skillnad mellan COPY och ADD?',
        options: ['Ingen skillnad', 'ADD kan URL och untar automatiskt', 'COPY är snabbare', 'ADD är säkrare'],
        correctIndex: 1, // B
        explanation: 'ADD har extra features: URL-nedladdning och auto-untar.',
        difficulty: 'VG',
        category: 'Dockerfile'
    },
    {
        id: 't23-q12',
        question: 'Skillnad mellan CMD och ENTRYPOINT?',
        options: ['Ingen skillnad', 'CMD kan överskridas, ENTRYPOINT är fixerat', 'ENTRYPOINT körs vid build', 'CMD är obligatoriskt'],
        correctIndex: 1, // B
        explanation: 'ENTRYPOINT är huvudkommando, CMD ger default-argument.',
        difficulty: 'VG',
        category: 'Dockerfile'
    },
    {
        id: 't23-q13',
        question: 'Vad är image layers?',
        options: ['Säkerhetslager', 'Varje instruktion skapar cachbart lager', 'Nätverkslager', 'Behörighetsnivåer'],
        correctIndex: 1, // B
        explanation: 'Varje Dockerfile-instruktion skapar ett cachat lager.',
        difficulty: 'VG',
        category: 'Koncept'
    },
    {
        id: 't23-q14',
        question: 'Vad gör ARG i Dockerfile?',
        options: ['Argument vid runtime', 'Build-time variabel', 'Array-definition', 'Arkivering'],
        correctIndex: 1, // B
        explanation: 'ARG definierar variabler som kan sättas vid build.',
        difficulty: 'VG',
        category: 'Dockerfile'
    },
    {
        id: 't23-q15',
        question: 'Hur bygger du utan cache?',
        options: ['docker build --fresh', 'docker build --no-cache', 'docker build --clean', 'docker build --rebuild'],
        correctIndex: 1, // B
        explanation: '--no-cache bygger alla lager från scratch.',
        difficulty: 'VG',
        category: 'Build'
    },
    {
        id: 't23-q16',
        question: 'Vad är multi-stage build?',
        options: ['Bygga parallellt', 'Flera FROM för mindre slutimage', 'Bygga i steg', 'Multi-arkitektur'],
        correctIndex: 1, // B
        explanation: 'Multi-stage: bygg i ett steg, kopiera resultat till liten image.',
        difficulty: 'VG',
        category: 'Optimering'
    },
    {
        id: 't23-q17',
        question: 'Hur kör du som non-root i container?',
        options: ['RUN sudo', 'USER appuser efter skapande', 'ROOT false', 'NONROOT true'],
        correctIndex: 1, // B
        explanation: 'Skapa användare med RUN, sedan USER <user> för säkerhet.',
        difficulty: 'VG',
        category: 'Säkerhet'
    },
    {
        id: 't23-q18',
        question: 'Vad gör HEALTHCHECK i Dockerfile?',
        options: ['Kontrollerar Dockerfile-syntax', 'Definierar hälsokontroll för container', 'Verifierar image', 'Testar nätverk'],
        correctIndex: 1, // B
        explanation: 'HEALTHCHECK låter Docker kontrollera om containern är frisk.',
        difficulty: 'VG',
        category: 'Dockerfile'
    },
    {
        id: 't23-q19',
        question: 'Hur sparar du image till fil?',
        options: ['docker export image > file.tar', 'docker save image > file.tar', 'docker backup image file.tar', 'docker dump image file.tar'],
        correctIndex: 1, // B
        explanation: 'docker save sparar image med alla lager till tar.',
        difficulty: 'VG',
        category: 'Export'
    },
    {
        id: 't23-q20',
        question: 'Vad är scratch image?',
        options: ['Skadad image', 'Tom basimage', 'Temporär image', 'Test-image'],
        correctIndex: 1, // B
        explanation: 'FROM scratch ger helt tom image för minimala containers.',
        difficulty: 'VG',
        category: 'Optimering'
    }
]

// =============================================================================
// TASK 24: DOCKER COMPOSE (20 quiz)
// =============================================================================

const TASK_24_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't24-q1',
        question: 'Vad är Docker Compose?',
        options: ['Image-byggare', 'Verktyg för multi-container applikationer', 'Container-monitor', 'Nätverkshanterare'],
        correctIndex: 1, // B
        explanation: 'Docker Compose definierar och kör multi-container apps.',
        difficulty: 'G',
        category: 'Grunder'
    },
    {
        id: 't24-q2',
        question: 'Hur startar du compose i bakgrunden?',
        options: ['docker compose start', 'docker compose up -d', 'docker compose run -d', 'docker compose bg'],
        correctIndex: 1, // B
        explanation: 'docker compose up -d kör i detached mode.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't24-q3',
        question: 'Vad heter standard compose-filen?',
        options: ['compose.json', 'docker-compose.yml', 'docker.yaml', 'containers.yml'],
        correctIndex: 1, // B
        explanation: 'docker-compose.yml eller compose.yaml är standard.',
        difficulty: 'G',
        category: 'Konfiguration'
    },
    {
        id: 't24-q4',
        question: 'Hur stoppar och tar du bort compose-containers?',
        options: ['docker compose stop', 'docker compose down', 'docker compose remove', 'docker compose delete'],
        correctIndex: 1, // B
        explanation: 'docker compose down stoppar och tar bort containers.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't24-q5',
        question: 'Hur visar du loggar för alla tjänster?',
        options: ['docker compose output', 'docker compose logs', 'docker compose show', 'docker compose print'],
        correctIndex: 1, // B
        explanation: 'docker compose logs visar output från alla tjänster.',
        difficulty: 'G',
        category: 'Logs'
    },
    {
        id: 't24-q6',
        question: 'Hur listar du compose-tjänster?',
        options: ['docker compose list', 'docker compose ps', 'docker compose show', 'docker compose services'],
        correctIndex: 1, // B
        explanation: 'docker compose ps visar status för alla tjänster.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't24-q7',
        question: 'Var definieras tjänster i compose?',
        options: ['containers:', 'services:', 'apps:', 'instances:'],
        correctIndex: 1, // B
        explanation: 'services: är huvudsektionen för tjänstdefinitioner.',
        difficulty: 'G',
        category: 'YAML'
    },
    {
        id: 't24-q8',
        question: 'Hur bygger du images med compose?',
        options: ['docker compose make', 'docker compose build', 'docker compose create', 'docker compose generate'],
        correctIndex: 1, // B
        explanation: 'docker compose build bygger alla images definierade med build:.',
        difficulty: 'G',
        category: 'Build'
    },
    {
        id: 't24-q9',
        question: 'Hur kör du kommando i en tjänst?',
        options: ['docker compose run service cmd', 'docker compose exec service cmd', 'docker compose cmd service', 'docker compose shell service'],
        correctIndex: 1, // B
        explanation: 'docker compose exec kör kommando i körande tjänst.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 't24-q10',
        question: 'Hur definierar du portmappning i compose?',
        options: ['port: "8080:80"', 'ports:\n  - "8080:80"', 'expose: "8080:80"', 'mapping: "8080:80"'],
        correctIndex: 1, // B
        explanation: 'ports: är en lista med HOST:CONTAINER-mappningar.',
        difficulty: 'G',
        category: 'YAML'
    },
    {
        id: 't24-q11',
        question: 'Hur definierar du beroende mellan tjänster?',
        options: ['requires:', 'depends_on:', 'needs:', 'after:'],
        correctIndex: 1, // B
        explanation: 'depends_on: anger vilka tjänster som måste starta först.',
        difficulty: 'VG',
        category: 'Dependencies'
    },
    {
        id: 't24-q12',
        question: 'Hur definierar du named volume?',
        options: ['Bara under services', 'Under volumes: på toppnivå', 'I Dockerfile', 'Med docker volume create'],
        correctIndex: 1, // B
        explanation: 'Named volumes definieras på toppnivå under volumes:.',
        difficulty: 'VG',
        category: 'Volumes'
    },
    {
        id: 't24-q13',
        question: 'Hur sätter du miljövariabler?',
        options: ['vars:', 'environment:', 'env:', 'variables:'],
        correctIndex: 1, // B
        explanation: 'environment: eller env_file: för miljövariabler.',
        difficulty: 'VG',
        category: 'Config'
    },
    {
        id: 't24-q14',
        question: 'Hur skalar du en tjänst till 3 instanser?',
        options: ['docker compose scale web=3', 'docker compose up --scale web=3', 'docker compose replicate web 3', 'docker compose run -n 3 web'],
        correctIndex: 1, // B
        explanation: '--scale tjänst=antal skapar flera instanser.',
        difficulty: 'VG',
        category: 'Scaling'
    },
    {
        id: 't24-q15',
        question: 'Hur anger du restart policy?',
        options: ['restart: auto', 'restart: always', 'autorestart: true', 'policy: restart'],
        correctIndex: 1, // B
        explanation: 'restart: always/on-failure/unless-stopped/no.',
        difficulty: 'VG',
        category: 'Config'
    },
    {
        id: 't24-q16',
        question: 'Hur tar du bort volymer med down?',
        options: ['docker compose down --volumes', 'docker compose down -v', 'docker compose down --remove-volumes', 'docker compose down -rm'],
        correctIndex: 1, // B
        explanation: '-v tar bort named volumes definierade i compose.',
        difficulty: 'VG',
        category: 'Cleanup'
    },
    {
        id: 't24-q17',
        question: 'Hur använder du .env-fil?',
        options: ['Importera explicit', 'Placera i samma katalog, läses automatiskt', 'Ange med --env', 'Definiera i compose.yml'],
        correctIndex: 1, // B
        explanation: '.env i samma katalog läses automatiskt av compose.',
        difficulty: 'VG',
        category: 'Config'
    },
    {
        id: 't24-q18',
        question: 'Hur definierar du healthcheck?',
        options: ['check:', 'healthcheck:', 'health:', 'liveness:'],
        correctIndex: 1, // B
        explanation: 'healthcheck: definierar test, interval, timeout etc.',
        difficulty: 'VG',
        category: 'Health'
    },
    {
        id: 't24-q19',
        question: 'Hur använder du flera compose-filer?',
        options: ['docker compose -f a.yml -f b.yml up', 'docker compose --files a.yml,b.yml up', 'docker compose merge a.yml b.yml', 'docker compose up a.yml b.yml'],
        correctIndex: 0, // A
        explanation: 'Flera -f flaggor mergar compose-filer i ordning.',
        difficulty: 'VG',
        category: 'Config'
    },
    {
        id: 't24-q20',
        question: 'Skillnad docker compose vs docker-compose?',
        options: ['Samma sak', 'docker compose är V2 (plugin), docker-compose är V1 (standalone)', 'docker-compose är nyare', 'docker compose kräver root'],
        correctIndex: 1, // B
        explanation: 'docker compose (V2) är integrerad plugin, docker-compose (V1) är gammal.',
        difficulty: 'VG',
        category: 'Version'
    },
    // SCENARIO-BASERADE FRÅGOR
    {
        id: 't24-s1',
        question: 'App-containern startar före databasen är redo och kraschar. Hur löser du det?',
        options: ['depends_on: db', 'depends_on + healthcheck på db', 'Lägg in sleep i app', 'Starta db manuellt först'],
        correctIndex: 1, // B
        explanation: 'depends_on väntar bara på att containern startar, inte att den är redo. Healthcheck + depends_on condition löser det.',
        difficulty: 'VG',
        category: 'Felsökning',
        scenario: 'Connection refused till databas vid docker-compose up.',
        isScenario: true
    },
    {
        id: 't24-s2',
        question: 'Databasdata försvinner vid docker-compose down. Hur bevarar du den?',
        options: ['Använd --no-rm flagga', 'Definiera en namngiven volym', 'Kör down utan -v', 'Backup före down'],
        correctIndex: 1, // B
        explanation: 'Namngivna volymer (volumes: db_data:) bevaras mellan down/up. Anonyma volymer försvinner.',
        difficulty: 'G',
        category: 'Volymer',
        scenario: 'All data försvann efter en omstart av stacken.',
        isScenario: true
    },
    {
        id: 't24-s3',
        question: 'Du har lösenord i docker-compose.yml och det hamnade i Git. Bättre lösning?',
        options: ['Använd .env fil + .gitignore', 'Kryptera docker-compose.yml', 'Hårdkoda i Dockerfile', 'Använd config-filer'],
        correctIndex: 0, // A
        explanation: '.env-fil med secrets + lägg till i .gitignore. Referera med ${VARIABEL} i compose.',
        difficulty: 'VG',
        category: 'Säkerhet',
        scenario: 'Säkerhetsscan hittade credentials i repot.',
        isScenario: true
    }
]

// =============================================================================
// TASK 25: GIT (20 quiz)
// =============================================================================

const TASK_25_QUIZ: TaskQuizQuestion[] = [
    {
        id: 't25-q1',
        question: 'Vad är Git?',
        options: ['Textredigerare', 'Distribuerat versionshanteringssystem', 'Programmeringsspråk', 'Webbserver'],
        correctIndex: 1, // B
        explanation: 'Git är ett distribuerat VCS för att spåra kodändringar.',
        difficulty: 'G',
        category: 'Grunder'
    },
    {
        id: 't25-q2',
        question: 'Hur skapar du nytt Git-repo?',
        options: ['git create', 'git init', 'git new', 'git start'],
        correctIndex: 1, // B
        explanation: 'git init skapar .git-katalog och initierar repo.',
        difficulty: 'G',
        category: 'Init'
    },
    {
        id: 't25-q3',
        question: 'Hur klonar du ett repo?',
        options: ['git copy url', 'git clone url', 'git download url', 'git fetch url'],
        correctIndex: 1, // B
        explanation: 'git clone kopierar hela repot inklusive historik.',
        difficulty: 'G',
        category: 'Clone'
    },
    {
        id: 't25-q4',
        question: 'Hur lägger du till alla filer för commit?',
        options: ['git add *', 'git add .', 'git stage all', 'git include .'],
        correctIndex: 1, // B
        explanation: 'git add . lägger till alla ändringar i aktuell katalog.',
        difficulty: 'G',
        category: 'Staging'
    },
    {
        id: 't25-q5',
        question: 'Hur committar du med meddelande?',
        options: ['git commit "msg"', 'git commit -m "msg"', 'git save -m "msg"', 'git store "msg"'],
        correctIndex: 1, // B
        explanation: 'git commit -m "meddelande" skapar commit med meddelande.',
        difficulty: 'G',
        category: 'Commit'
    },
    {
        id: 't25-q6',
        question: 'Hur pushar du till remote?',
        options: ['git send', 'git push', 'git upload', 'git sync'],
        correctIndex: 1, // B
        explanation: 'git push skickar commits till remote repository.',
        difficulty: 'G',
        category: 'Push'
    },
    {
        id: 't25-q7',
        question: 'Hur hämtar och mergar du ändringar?',
        options: ['git fetch', 'git pull', 'git get', 'git download'],
        correctIndex: 1, // B
        explanation: 'git pull = git fetch + git merge.',
        difficulty: 'G',
        category: 'Pull'
    },
    {
        id: 't25-q8',
        question: 'Hur visar du commit-historik?',
        options: ['git history', 'git log', 'git commits', 'git show'],
        correctIndex: 1, // B
        explanation: 'git log visar commit-historik.',
        difficulty: 'G',
        category: 'Log'
    },
    {
        id: 't25-q9',
        question: 'Hur skapar du ny branch?',
        options: ['git new branch', 'git branch namn', 'git create branch', 'git make branch'],
        correctIndex: 1, // B
        explanation: 'git branch <namn> skapar ny branch.',
        difficulty: 'G',
        category: 'Branches'
    },
    {
        id: 't25-q10',
        question: 'Hur visar du aktuell status?',
        options: ['git info', 'git status', 'git state', 'git check'],
        correctIndex: 1, // B
        explanation: 'git status visar ändrade, stagade och ospårade filer.',
        difficulty: 'G',
        category: 'Status'
    },
    {
        id: 't25-q11',
        question: 'Hur byter du till branch "feature"?',
        options: ['git switch feature', 'git checkout feature', 'git change feature', 'git branch feature'],
        correctIndex: 1, // B
        explanation: 'git checkout <branch> byter branch (eller git switch).',
        difficulty: 'VG',
        category: 'Branches'
    },
    {
        id: 't25-q12',
        question: 'Hur mergar du feature-branch till main?',
        options: ['git merge feature (på main)', 'git combine feature main', 'git join feature', 'git merge main feature'],
        correctIndex: 0, // A
        explanation: 'Stå på main, kör git merge feature.',
        difficulty: 'VG',
        category: 'Merge'
    },
    {
        id: 't25-q13',
        question: 'Vad gör git stash?',
        options: ['Tar bort ändringar', 'Sparar ändringar temporärt', 'Committar automatiskt', 'Skapar branch'],
        correctIndex: 1, // B
        explanation: 'git stash sparar undan ändringar för senare.',
        difficulty: 'VG',
        category: 'Stash'
    },
    {
        id: 't25-q14',
        question: 'Hur ångrar du senaste unstaged ändringar i fil?',
        options: ['git undo fil', 'git restore fil', 'git reset fil', 'git revert fil'],
        correctIndex: 1, // B
        explanation: 'git restore <fil> återställer till senaste commit.',
        difficulty: 'VG',
        category: 'Ångra'
    },
    {
        id: 't25-q15',
        question: 'Hur tar du bort branch lokalt?',
        options: ['git branch -d namn', 'git delete branch namn', 'git remove namn', 'git branch --remove namn'],
        correctIndex: 0, // A
        explanation: 'git branch -d <branch> tar bort branch.',
        difficulty: 'VG',
        category: 'Branches'
    },
    {
        id: 't25-q16',
        question: 'Skillnad merge vs rebase?',
        options: ['Ingen skillnad', 'Merge bevarar historik, rebase skapar linjär', 'Rebase är säkrare', 'Merge är snabbare'],
        correctIndex: 1, // B
        explanation: 'Merge skapar merge commit, rebase skriver om historiken.',
        difficulty: 'VG',
        category: 'Koncept'
    },
    {
        id: 't25-q17',
        question: 'Hur ändrar du senaste commit-meddelande?',
        options: ['git edit -m "ny"', 'git commit --amend', 'git change -m "ny"', 'git modify commit'],
        correctIndex: 1, // B
        explanation: 'git commit --amend ändrar senaste commit.',
        difficulty: 'VG',
        category: 'Commit'
    },
    {
        id: 't25-q18',
        question: 'Hur ångrar du senaste commit men behåller ändringar?',
        options: ['git undo HEAD', 'git reset --soft HEAD~1', 'git revert HEAD', 'git uncommit'],
        correctIndex: 1, // B
        explanation: '--soft behåller ändringar i staging area.',
        difficulty: 'VG',
        category: 'Ångra'
    },
    {
        id: 't25-q19',
        question: 'Vad är .gitignore?',
        options: ['Lista över ignorerade commits', 'Fil som anger vad Git ska ignorera', 'Konfigurationsfil', 'Loggfil'],
        correctIndex: 1, // B
        explanation: '.gitignore listar filer/kataloger Git ska ignorera.',
        difficulty: 'VG',
        category: 'Config'
    },
    {
        id: 't25-q20',
        question: 'Hur skapar du annoterad tag?',
        options: ['git tag v1.0', 'git tag -a v1.0 -m "Release"', 'git label v1.0', 'git mark v1.0'],
        correctIndex: 1, // B
        explanation: '-a skapar annoterad tag med meddelande och metadata.',
        difficulty: 'VG',
        category: 'Tags'
    },
    // SCENARIO-BASERADE FRÅGOR
    {
        id: 't25-s1',
        question: 'Du har gjort ändringar men vill byta branch. Git säger att du har uncommitted changes. Snabbaste lösningen?',
        options: ['git commit', 'git stash', 'git reset --hard', 'git checkout --force'],
        correctIndex: 1, // B
        explanation: 'git stash sparar ändringar temporärt. git stash pop återställer dem senare.',
        difficulty: 'G',
        category: 'Workflow',
        scenario: 'En brådskande bugg måste fixas på annan branch.',
        isScenario: true
    },
    {
        id: 't25-s2',
        question: 'Du pushade känslig data (lösenord) av misstag. Vad gör du?',
        options: ['git revert', 'git commit --amend + force push + rotera lösenord', 'git reset', 'Ignorera det'],
        correctIndex: 1, // B
        explanation: 'Ändra historik med amend/force push OCH rotera lösenordet - det kan finnas kopierat.',
        difficulty: 'VG',
        category: 'Säkerhet',
        scenario: 'Du upptäcker API-nycklar i senaste commit.',
        isScenario: true
    },
    {
        id: 't25-s3',
        question: 'Din branch har 15 commits, men du vill merga till main med EN commit. Vad gör du?',
        options: ['git merge --single', 'git merge --squash', 'git commit --all', 'git combine'],
        correctIndex: 1, // B
        explanation: '--squash kombinerar alla commits till en enda vid merge.',
        difficulty: 'VG',
        category: 'Workflow',
        scenario: 'Teamet kräver clean git history i main-branchen.',
        isScenario: true
    },
    {
        id: 't25-s4',
        question: 'git pull ger konflikt i config.yaml. Hur löser du det?',
        options: ['git reset --hard origin/main', 'Redigera filen, ta bort konfliktmarkeringar, git add, git commit', 'git pull --force', 'git ignore config.yaml'],
        correctIndex: 1, // B
        explanation: 'Öppna filen, välj rätt version manuellt, ta bort <<<<< ===== >>>>>, sedan add+commit.',
        difficulty: 'G',
        category: 'Konflikthantering',
        scenario: 'Både du och kollega ändrade samma fil.',
        isScenario: true
    },
    {
        id: 't25-s5',
        question: 'Du vill se exakt vad som ändrades mellan två branches. Kommando?',
        options: ['git log main..feature', 'git diff main..feature', 'git compare main feature', 'git show main feature'],
        correctIndex: 1, // B
        explanation: 'git diff branch1..branch2 visar alla skillnader mellan brancherna.',
        difficulty: 'G',
        category: 'Analys',
        scenario: 'Du granskar en kollegas ändringar före merge.',
        isScenario: true
    }
]

// =============================================================================
// EXPORT
// =============================================================================

export const DOE25_TASK_QUIZ: TaskQuizSet[] = [
    {
        taskId: 'doe25-0-1-subnetting',
        taskTitle: '0.1 Subnetting & Nätverk',
        questions: TASK_1_QUIZ
    },
    {
        taskId: 'doe25-0-2-filsystem',
        taskTitle: '0.2 Linux Filsystem',
        questions: TASK_2_QUIZ
    },
    {
        taskId: 'doe25-1-1-bash-grunder',
        taskTitle: '1.1 Bash Grunder',
        questions: TASK_3_QUIZ
    },
    {
        taskId: 'doe25-1-2-variabler',
        taskTitle: '1.2 Variabler & Datatyper',
        questions: TASK_4_QUIZ
    },
    {
        taskId: 'doe25-1-3-regex',
        taskTitle: '1.3 Reguljära Uttryck (Regex)',
        questions: TASK_5_QUIZ
    },
    {
        taskId: 'doe25-1-4-sed',
        taskTitle: '1.4 sed - Stream Editor',
        questions: TASK_6_QUIZ
    },
    {
        taskId: 'doe25-1-5-awk',
        taskTitle: '1.5 awk - Textbearbetning',
        questions: TASK_7_QUIZ
    },
    {
        taskId: 'doe25-1-6-villkor',
        taskTitle: '1.6 Villkor (if/else)',
        questions: TASK_8_QUIZ
    },
    {
        taskId: 'doe25-1-7-interaktiva',
        taskTitle: '1.7 Interaktiva Skript',
        questions: TASK_9_QUIZ
    },
    {
        taskId: 'doe25-1-8-loopar',
        taskTitle: '1.8 Loopar (for/while)',
        questions: TASK_10_QUIZ
    },
    {
        taskId: 'doe25-1-9-parametrar',
        taskTitle: '1.9 Skriptparametrar',
        questions: TASK_11_QUIZ
    },
    {
        taskId: 'doe25-1-10-funktioner',
        taskTitle: '1.10 Funktioner',
        questions: TASK_12_QUIZ
    },
    {
        taskId: 'doe25-1-11-signals',
        taskTitle: '1.11 Signaler & Trap',
        questions: TASK_13_QUIZ
    },
    {
        taskId: 'doe25-2-1-users',
        taskTitle: '2.1 Användarhantering',
        questions: TASK_14_QUIZ
    },
    {
        taskId: 'doe25-2-2-permissions',
        taskTitle: '2.2 Rättigheter & ACL',
        questions: TASK_15_QUIZ
    },
    {
        taskId: 'doe25-2-3-ssh',
        taskTitle: '2.3 SSH',
        questions: TASK_16_QUIZ
    },
    {
        taskId: 'doe25-2-4-ufw',
        taskTitle: '2.4 UFW Firewall',
        questions: TASK_17_QUIZ
    },
    {
        taskId: 'doe25-2-5-firewalld',
        taskTitle: '2.5 Firewalld',
        questions: TASK_18_QUIZ
    },
    {
        taskId: 'doe25-2-6-lagring',
        taskTitle: '2.6 Lagring & LVM',
        questions: TASK_19_QUIZ
    },
    {
        taskId: 'doe25-2-7-backup',
        taskTitle: '2.7 Backup',
        questions: TASK_20_QUIZ
    },
    {
        taskId: 'doe25-2-8-systemd',
        taskTitle: '2.8 Systemd',
        questions: TASK_21_QUIZ
    },
    {
        taskId: 'doe25-3-1-docker-grunder',
        taskTitle: '3.1 Docker Grunder',
        questions: TASK_22_QUIZ
    },
    {
        taskId: 'doe25-3-2-docker-images',
        taskTitle: '3.2 Docker Images',
        questions: TASK_23_QUIZ
    },
    {
        taskId: 'doe25-3-3-docker-compose',
        taskTitle: '3.3 Docker Compose',
        questions: TASK_24_QUIZ
    },
    {
        taskId: 'doe25-3-4-git',
        taskTitle: '3.4 Git',
        questions: TASK_25_QUIZ
    }
]

// Helper functions
export function getQuizForTask(taskId: string): TaskQuizQuestion[] {
    const set = DOE25_TASK_QUIZ.find(s => s.taskId === taskId)
    return set?.questions || []
}

export function getAllDOE25Quiz(): TaskQuizQuestion[] {
    return DOE25_TASK_QUIZ.flatMap(s => s.questions)
}
