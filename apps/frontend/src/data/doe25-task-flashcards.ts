/**
 * DOE25 Tentaplugg - Task-specifika Flashcards
 * 30 flashcards per task, pedagogiskt fokuserade för tentaplugg
 */

export interface TaskFlashcard {
    id: string
    front: string
    back: string
    category: string
    difficulty: 'G' | 'VG'
}

export interface TaskFlashcardSet {
    taskId: string
    taskTitle: string
    flashcards: TaskFlashcard[]
}

// =============================================================================
// TASK 1: SUBNETTING & NÄTVERK (30 flashcards)
// =============================================================================

const TASK_1_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    {
        id: 't1-1',
        front: 'Hur många bitar består en IPv4-adress av?',
        back: '32 bitar, uppdelade i 4 oktetter (8 bitar vardera)',
        category: 'IPv4 Grunder',
        difficulty: 'G'
    },
    {
        id: 't1-2',
        front: 'Vad är värdeintervallet för en oktett i en IPv4-adress?',
        back: '0-255 (eftersom 8 bitar = 2⁸ = 256 möjliga värden)',
        category: 'IPv4 Grunder',
        difficulty: 'G'
    },
    {
        id: 't1-3',
        front: 'Vad betyder /24 i CIDR-notation?',
        back: '24 av 32 bitar är nätverksdelen. Motsvarar subnätmask 255.255.255.0',
        category: 'CIDR',
        difficulty: 'G'
    },
    {
        id: 't1-4',
        front: 'Vilken IP-range är reserverad för loopback (localhost)?',
        back: '127.0.0.0 - 127.255.255.255 (oftast 127.0.0.1)',
        category: 'Reserverade adresser',
        difficulty: 'G'
    },
    {
        id: 't1-5',
        front: 'Vad är kommandot för att visa nätverkskonfiguration i Linux?',
        back: 'ip addr show (eller ip a)\nÄldre alternativ: ifconfig',
        category: 'Kommandon',
        difficulty: 'G'
    },
    {
        id: 't1-6',
        front: 'Vad är en broadcast-adress?',
        back: 'Den sista adressen i ett subnät. Används för att skicka till ALLA enheter i nätverket.',
        category: 'Nätverkskoncept',
        difficulty: 'G'
    },
    {
        id: 't1-7',
        front: 'Vad är en nätverksadress?',
        back: 'Den första adressen i ett subnät (alla hostbitar = 0). Identifierar själva nätverket.',
        category: 'Nätverkskoncept',
        difficulty: 'G'
    },
    {
        id: 't1-8',
        front: 'Kommando för att testa nätverksanslutning till en host?',
        back: 'ping <ip-adress eller hostname>\nEx: ping -c 3 google.com',
        category: 'Kommandon',
        difficulty: 'G'
    },
    {
        id: 't1-9',
        front: 'Vad visar kommandot "ip route show"?',
        back: 'Routingtabellen - visar hur nätverkstrafik dirigeras, inklusive default gateway.',
        category: 'Kommandon',
        difficulty: 'G'
    },
    {
        id: 't1-10',
        front: 'Vad står CIDR för?',
        back: 'Classless Inter-Domain Routing - ersatte de gamla IP-klasserna för mer flexibel adressering.',
        category: 'CIDR',
        difficulty: 'G'
    },
    // Medium (12)
    {
        id: 't1-11',
        front: 'Hur många hosts kan finnas i ett /24 nätverk?',
        back: '254 hosts\nFormel: 2^(32-24) - 2 = 2^8 - 2 = 256 - 2 = 254\n(-2 för nätverks- och broadcast-adress)',
        category: 'Subnätberäkning',
        difficulty: 'G'
    },
    {
        id: 't1-12',
        front: 'Vad är subnätmasken för /16?',
        back: '255.255.0.0\n16 ettor följt av 16 nollor i binärt.',
        category: 'CIDR',
        difficulty: 'G'
    },
    {
        id: 't1-13',
        front: 'Givet 192.168.1.100/24 - vad är nätverksadressen?',
        back: '192.168.1.0\nDe första 24 bitarna behålls, resten sätts till 0.',
        category: 'Subnätberäkning',
        difficulty: 'G'
    },
    {
        id: 't1-14',
        front: 'Givet 192.168.1.100/24 - vad är broadcast-adressen?',
        back: '192.168.1.255\nDe första 24 bitarna behålls, resten sätts till 1.',
        category: 'Subnätberäkning',
        difficulty: 'G'
    },
    {
        id: 't1-15',
        front: 'Vilka IP-adresser är privata (RFC 1918)?',
        back: '• 10.0.0.0/8 (Klass A)\n• 172.16.0.0/12 (Klass B)\n• 192.168.0.0/16 (Klass C)',
        category: 'Reserverade adresser',
        difficulty: 'G'
    },
    {
        id: 't1-16',
        front: 'Vad är default gateway?',
        back: 'Routern som hanterar trafik till nätverk utanför det lokala subnätet. Typiskt första eller sista användbara IP i subnätet.',
        category: 'Nätverkskoncept',
        difficulty: 'G'
    },
    {
        id: 't1-17',
        front: 'Hur många hosts i ett /30 nätverk?',
        back: '2 hosts\n2^(32-30) - 2 = 2^2 - 2 = 4 - 2 = 2\nAnvänds för punkt-till-punkt-länkar.',
        category: 'Subnätberäkning',
        difficulty: 'G'
    },
    {
        id: 't1-18',
        front: 'Kommando för att se subnätinformation med beräkningar?',
        back: 'ipcalc <ip/prefix>\nEx: ipcalc 192.168.1.100/24',
        category: 'Kommandon',
        difficulty: 'G'
    },
    {
        id: 't1-19',
        front: 'Vad var Klass A nätverk enligt gamla IP-klasserna?',
        back: 'Första oktett: 1-126\nDefault mask: 255.0.0.0 (/8)\nStor mängd hosts per nätverk.',
        category: 'IP-klasser',
        difficulty: 'G'
    },
    {
        id: 't1-20',
        front: 'Vad var Klass C nätverk enligt gamla IP-klasserna?',
        back: 'Första oktett: 192-223\nDefault mask: 255.255.255.0 (/24)\nSmå nätverk med max 254 hosts.',
        category: 'IP-klasser',
        difficulty: 'G'
    },
    {
        id: 't1-21',
        front: 'Vad gör kommandot traceroute?',
        back: 'Visar vägen (alla hopp/routrar) som paket tar för att nå en destination.\ntraceroute google.com',
        category: 'Kommandon',
        difficulty: 'G'
    },
    {
        id: 't1-22',
        front: 'Formel för antal hosts i ett subnät?',
        back: '2^(32 - prefix) - 2\n\nEx /24: 2^(32-24) - 2 = 2^8 - 2 = 254\n-2 för nätverks- och broadcast-adress',
        category: 'Subnätberäkning',
        difficulty: 'G'
    },
    // Hard (8)
    {
        id: 't1-23',
        front: 'Givet 10.0.0.0/8 - vad är broadcast-adressen?',
        back: '10.255.255.255\nEndast första oktetten är nätverksdel, resten (3 oktetter) blir 255.',
        category: 'Subnätberäkning',
        difficulty: 'VG'
    },
    {
        id: 't1-24',
        front: 'Du behöver 500 hosts. Vilken prefix-längd krävs minst?',
        back: '/23 (510 hosts)\n2^9 - 2 = 510 hosts\n/24 ger bara 254 hosts (för lite)',
        category: 'Subnätberäkning',
        difficulty: 'VG'
    },
    {
        id: 't1-25',
        front: 'Vad är 172.16.0.0/12 i subnätmask-format?',
        back: '255.240.0.0\nBinärt: 11111111.11110000.00000000.00000000\n(12 ettor)',
        category: 'CIDR',
        difficulty: 'VG'
    },
    {
        id: 't1-26',
        front: 'Kan två enheter på 192.168.1.50/24 och 192.168.2.50/24 kommunicera direkt?',
        back: 'NEJ - de är i olika subnät.\n192.168.1.0 vs 192.168.2.0\nKräver router för kommunikation.',
        category: 'Nätverkskoncept',
        difficulty: 'VG'
    },
    {
        id: 't1-27',
        front: 'Dela upp 192.168.1.0/24 i 4 lika stora subnät - vilka prefix får de?',
        back: '/26 (64 adresser per subnät)\n• 192.168.1.0/26\n• 192.168.1.64/26\n• 192.168.1.128/26\n• 192.168.1.192/26',
        category: 'Subnätberäkning',
        difficulty: 'VG'
    },
    {
        id: 't1-28',
        front: 'Vad är skillnaden mellan NAT och PAT?',
        back: 'NAT: Network Address Translation - mappar privata till publika IP:n.\nPAT: Port Address Translation - flera privata IP:n delar EN publik IP via olika portar.',
        category: 'Nätverkskoncept',
        difficulty: 'VG'
    },
    {
        id: 't1-29',
        front: 'Vad är VLSM och varför används det?',
        back: 'Variable Length Subnet Masking - tillåter olika subnätstorlekar i samma nätverk för effektivare IP-användning.',
        category: 'Subnätberäkning',
        difficulty: 'VG'
    },
    {
        id: 't1-30',
        front: 'Givet 10.20.30.40/22 - vad är nätverksadressen?',
        back: '10.20.28.0\n/22 = 255.255.252.0\n30 & 252 = 28 (tredje oktetten)',
        category: 'Subnätberäkning',
        difficulty: 'VG'
    }
]

// =============================================================================
// TASK 2: LINUX FILSYSTEM (30 flashcards)
// =============================================================================

const TASK_2_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    {
        id: 't2-1',
        front: 'Vad är rotkatalogen i Linux och hur betecknas den?',
        back: '/ (forward slash)\nToppen av filsystemhierarkin - alla kataloger utgår härifrån.',
        category: 'FHS Grunder',
        difficulty: 'G'
    },
    {
        id: 't2-2',
        front: 'Var lagras systemkonfigurationsfiler i Linux?',
        back: '/etc\nInnehåller konfigurationsfiler som passwd, shadow, fstab, hosts, ssh/',
        category: 'Viktiga kataloger',
        difficulty: 'G'
    },
    {
        id: 't2-3',
        front: 'Var finns användarnas hemkataloger?',
        back: '/home\nVarje användare har /home/användarnamn (utom root som har /root)',
        category: 'Viktiga kataloger',
        difficulty: 'G'
    },
    {
        id: 't2-4',
        front: 'Var lagras systemloggar i Linux?',
        back: '/var/log\nInnehåller syslog, auth.log, kern.log, messages, etc.',
        category: 'Viktiga kataloger',
        difficulty: 'G'
    },
    {
        id: 't2-5',
        front: 'Vad är FHS?',
        back: 'Filesystem Hierarchy Standard\nStandard som definierar katalogstrukturen i Linux/Unix.',
        category: 'FHS Grunder',
        difficulty: 'G'
    },
    {
        id: 't2-6',
        front: 'Kommando för att lista alla filer (inklusive dolda) med detaljer?',
        back: 'ls -la\n-l = lång format, -a = alla (inklusive dolda filer som börjar med .)',
        category: 'Kommandon',
        difficulty: 'G'
    },
    {
        id: 't2-7',
        front: 'Vad innehåller /tmp?',
        back: 'Temporära filer som rensas vid omstart.\nAlla användare kan skriva här.',
        category: 'Viktiga kataloger',
        difficulty: 'G'
    },
    {
        id: 't2-8',
        front: 'Vad innehåller /bin och /sbin?',
        back: '/bin: Grundläggande användarkommandon (ls, cp, mv)\n/sbin: Systemadministrationskommandon (fdisk, iptables)',
        category: 'Viktiga kataloger',
        difficulty: 'G'
    },
    {
        id: 't2-9',
        front: 'Kommando för att visa nuvarande arbetskatalog?',
        back: 'pwd\n(Print Working Directory)',
        category: 'Kommandon',
        difficulty: 'G'
    },
    {
        id: 't2-10',
        front: 'Skillnad mellan absolut och relativ sökväg?',
        back: 'Absolut: Börjar från / (t.ex. /etc/ssh/sshd_config)\nRelativ: Utgår från nuvarande katalog (t.ex. ../lib)',
        category: 'Navigation',
        difficulty: 'G'
    },
    // Medium (12)
    {
        id: 't2-11',
        front: 'Vilka 7 filtyper finns i Linux? (visa med ls -l)',
        back: '- : Vanlig fil\nd : Katalog\nl : Symbolisk länk\nc : Character device\nb : Block device\ns : Socket\np : Named pipe (FIFO)',
        category: 'Filtyper',
        difficulty: 'G'
    },
    {
        id: 't2-12',
        front: 'Vad innehåller /proc?',
        back: 'Virtuellt filsystem med processinformation och systemstatus.\nFiler som /proc/cpuinfo, /proc/meminfo, /proc/[pid]/',
        category: 'Viktiga kataloger',
        difficulty: 'G'
    },
    {
        id: 't2-13',
        front: 'Vad är /dev och vad innehåller den?',
        back: 'Device-filer - representerar hårdvara.\nEx: /dev/sda (disk), /dev/tty (terminal), /dev/null, /dev/zero',
        category: 'Viktiga kataloger',
        difficulty: 'G'
    },
    {
        id: 't2-14',
        front: 'Vad är skillnaden mellan /bin och /usr/bin?',
        back: '/bin: Essentiella kommandon för boot och single-user mode\n/usr/bin: Icke-essentiella användarprogram',
        category: 'FHS Grunder',
        difficulty: 'G'
    },
    {
        id: 't2-15',
        front: 'Kommando för att hitta filer efter namn?',
        back: 'find <sökväg> -name "mönster"\nEx: find /etc -name "*.conf"',
        category: 'Kommandon',
        difficulty: 'G'
    },
    {
        id: 't2-16',
        front: 'Vad gör kommandot df -h?',
        back: 'Visar diskutrymme per filsystem i human-readable format.\n-h = storlekar som KB, MB, GB',
        category: 'Kommandon',
        difficulty: 'G'
    },
    {
        id: 't2-17',
        front: 'Vad gör kommandot du -sh?',
        back: 'Visar total storlek på en katalog.\n-s = summary (total), -h = human-readable',
        category: 'Kommandon',
        difficulty: 'G'
    },
    {
        id: 't2-18',
        front: 'Vad innehåller filen /etc/passwd?',
        back: 'Användarinformation:\nusername:x:UID:GID:GECOS:home:shell\n(x = lösenord i shadow)',
        category: 'Konfigurationsfiler',
        difficulty: 'G'
    },
    {
        id: 't2-19',
        front: 'Vad innehåller filen /etc/fstab?',
        back: 'Filsystem som ska monteras vid boot.\nFormat: device mountpoint fstype options dump pass',
        category: 'Konfigurationsfiler',
        difficulty: 'G'
    },
    {
        id: 't2-20',
        front: 'Vad är /opt för katalog?',
        back: 'Optional - för tredjepartsprogram som inte följer FHS.\nEx: /opt/google/chrome',
        category: 'Viktiga kataloger',
        difficulty: 'G'
    },
    {
        id: 't2-21',
        front: 'Skillnad mellan locate och find?',
        back: 'locate: Snabb sökning i databas (uppdateras med updatedb)\nfind: Realtidssökning, långsammare men alltid aktuell',
        category: 'Kommandon',
        difficulty: 'G'
    },
    {
        id: 't2-22',
        front: 'Vad gör kommandot tree?',
        back: 'Visar katalogstruktur som träd.\ntree -L 2 = max 2 nivåer djupt',
        category: 'Kommandon',
        difficulty: 'G'
    },
    // Hard (8)
    {
        id: 't2-23',
        front: 'Vad är skillnaden mellan /dev/null och /dev/zero?',
        back: '/dev/null: Slänger all data (svart hål)\n/dev/zero: Producerar oändligt med nollor (för att skapa tomma filer)',
        category: 'Device-filer',
        difficulty: 'VG'
    },
    {
        id: 't2-24',
        front: 'Vad är en inode och vad innehåller den?',
        back: 'Datastruktur med metadata om en fil:\n• Filtyp och rättigheter\n• Ägare/grupp\n• Storlek\n• Tidsmarkörer\n• Pekare till datablockFiler, EJ filnamnet!',
        category: 'Filsystem internals',
        difficulty: 'VG'
    },
    {
        id: 't2-25',
        front: 'Skillnad mellan hård och symbolisk länk?',
        back: 'Hård länk: Samma inode, fungerar om original tas bort\nSymbolisk länk: Pekare till filnamn, bryts om original tas bort',
        category: 'Filtyper',
        difficulty: 'VG'
    },
    {
        id: 't2-26',
        front: 'Vad gör sticky bit på en katalog?',
        back: 'Endast filägaren (och root) kan ta bort filer.\nAnvänds på /tmp för att skydda andras filer.\nSätts med chmod +t',
        category: 'Rättigheter',
        difficulty: 'VG'
    },
    {
        id: 't2-27',
        front: 'Vad innehåller /sys?',
        back: 'Virtuellt filsystem (sysfs) som exponerar kernel-information.\nEnhetsinformation, drivrutiner, bus-information.',
        category: 'Viktiga kataloger',
        difficulty: 'VG'
    },
    {
        id: 't2-28',
        front: 'Hur hittar du vilket paket som äger en fil? (Debian/Ubuntu)',
        back: 'dpkg -S /sökväg/till/fil\nEx: dpkg -S /usr/bin/ls\nSvar: coreutils: /usr/bin/ls',
        category: 'Kommandon',
        difficulty: 'VG'
    },
    {
        id: 't2-29',
        front: 'Vad är mount och hur används det?',
        back: 'Kopplar ett filsystem till en katalog.\nmount /dev/sdb1 /mnt/usb\numount /mnt/usb för att koppla bort',
        category: 'Kommandon',
        difficulty: 'VG'
    },
    {
        id: 't2-30',
        front: 'Vad visar lsblk?',
        back: 'Lista över block-enheter (diskar, partitioner).\nVisar namn, storlek, typ, mountpoint.',
        category: 'Kommandon',
        difficulty: 'VG'
    }
]

// =============================================================================
// TASK 3: BASH GRUNDER (30 flashcards)
// =============================================================================

const TASK_3_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't3-1', front: 'Vad är shebang och hur skrivs den?', back: '#!/bin/bash\nFörsta raden i ett skript som anger vilken tolk som ska köra det.', category: 'Skriptstruktur', difficulty: 'G' },
    { id: 't3-2', front: 'Kommando för att göra ett skript körbart?', back: 'chmod +x skript.sh\nLägger till execute-rättighet.', category: 'Köra skript', difficulty: 'G' },
    { id: 't3-3', front: 'Tre sätt att köra ett bash-skript?', back: '1. ./skript.sh (kräver +x)\n2. bash skript.sh\n3. source skript.sh (eller . skript.sh)', category: 'Köra skript', difficulty: 'G' },
    { id: 't3-4', front: 'Kommando för att skriva ut text i bash?', back: 'echo "text"\neller printf "text\\n"', category: 'I/O', difficulty: 'G' },
    { id: 't3-5', front: 'Kommando för att läsa input från användaren?', back: 'read variabel\neller read -p "Prompt: " variabel', category: 'I/O', difficulty: 'G' },
    { id: 't3-6', front: 'Vad betyder exit code 0?', back: 'Framgång! Kommandot/skriptet lyckades.\n(Alla andra värden = fel)', category: 'Exit codes', difficulty: 'G' },
    { id: 't3-7', front: 'Hur kontrollerar du senaste kommandots exit code?', back: 'echo $?\nVisar exit code från senaste kommando.', category: 'Exit codes', difficulty: 'G' },
    { id: 't3-8', front: 'Vad betyder exit code 127?', back: 'Kommandot hittades inte.\n(Command not found)', category: 'Exit codes', difficulty: 'G' },
    { id: 't3-9', front: 'Hur skriver du en kommentar i bash?', back: '# Detta är en kommentar\nAllt efter # ignoreras.', category: 'Skriptstruktur', difficulty: 'G' },
    { id: 't3-10', front: 'Skillnad mellan #!/bin/bash och #!/usr/bin/env bash?', back: '#!/bin/bash: Hårdkodad sökväg\n#!/usr/bin/env bash: Portabel, hittar bash via PATH', category: 'Shebang', difficulty: 'G' },
    // Medium (12)
    { id: 't3-11', front: 'Skillnad mellan ./skript.sh och source skript.sh?', back: './skript.sh: Kör i subshell (ändringar påverkar inte nuvarande shell)\nsource: Kör i nuvarande shell (ändringar bevaras)', category: 'Köra skript', difficulty: 'G' },
    { id: 't3-12', front: 'Vad gör exit 1 i ett skript?', back: 'Avslutar skriptet med exit code 1 (indikerar fel).\nexit 0 = framgång, exit 1+ = fel', category: 'Exit codes', difficulty: 'G' },
    { id: 't3-13', front: 'Vad betyder exit code 126?', back: 'Kommandot finns men är inte körbart.\n(Permission denied eller inte executable)', category: 'Exit codes', difficulty: 'G' },
    { id: 't3-14', front: 'Hur kör du ett kommando i bakgrunden?', back: 'kommando &\nLägg & i slutet.', category: 'Processhantering', difficulty: 'G' },
    { id: 't3-15', front: 'Vad gör kommandot set -e?', back: 'Avslutar skriptet direkt om något kommando misslyckas.\nBra för felhantering.', category: 'Skriptstruktur', difficulty: 'G' },
    { id: 't3-16', front: 'Vad gör kommandot set -x?', back: 'Debug-läge: Skriver ut varje kommando innan det körs.\nBra för felsökning.', category: 'Skriptstruktur', difficulty: 'G' },
    { id: 't3-17', front: 'Hur kedjar du kommandon så nästa bara körs om förra lyckades?', back: 'kommando1 && kommando2\n&& = AND (kör nästa endast vid exit 0)', category: 'Kommandokedjning', difficulty: 'G' },
    { id: 't3-18', front: 'Hur kedjar du kommandon så nästa bara körs om förra misslyckades?', back: 'kommando1 || kommando2\n|| = OR (kör nästa endast vid exit != 0)', category: 'Kommandokedjning', difficulty: 'G' },
    { id: 't3-19', front: 'Vad gör ; mellan kommandon?', back: 'Kör kommandon sekventiellt oavsett exit code.\nkommando1 ; kommando2', category: 'Kommandokedjning', difficulty: 'G' },
    { id: 't3-20', front: 'Hur fångar du output från ett kommando i en variabel?', back: 'variabel=$(kommando)\neller variabel=`kommando` (äldre syntax)', category: 'Kommandosubstitution', difficulty: 'G' },
    { id: 't3-21', front: 'Vad är skillnaden mellan echo och printf?', back: 'echo: Enklare, lägger till newline automatiskt\nprintf: Mer kontroll, formatsträngar, ingen auto-newline', category: 'I/O', difficulty: 'G' },
    { id: 't3-22', front: 'Hur läser du lösenord utan att visa det på skärmen?', back: 'read -s variabel\n-s = silent (visa inte input)', category: 'I/O', difficulty: 'G' },
    // Hard (8)
    { id: 't3-23', front: 'Vad gör trap i bash?', back: 'Fångar signaler och kör kod vid avbrott.\ntrap "cleanup" EXIT\ntrap "echo Interrupted" SIGINT', category: 'Signalhantering', difficulty: 'VG' },
    { id: 't3-24', front: 'Vad är skillnaden mellan SIGTERM och SIGKILL?', back: 'SIGTERM (15): Kan fångas, tillåter cleanup\nSIGKILL (9): Kan EJ fångas, omedelbar avslut', category: 'Signalhantering', difficulty: 'VG' },
    { id: 't3-25', front: 'Vad gör set -u?', back: 'Ger fel om odefinierad variabel används.\nBra för att hitta stavfel i variabelnamn.', category: 'Skriptstruktur', difficulty: 'VG' },
    { id: 't3-26', front: 'Vad gör set -o pipefail?', back: 'Returnerar exit code från första misslyckade kommando i en pipe.\nUtan: Endast sista kommandots exit code.', category: 'Skriptstruktur', difficulty: 'VG' },
    { id: 't3-27', front: 'Vanlig bash strict mode-inställning?', back: 'set -euo pipefail\n-e: Avsluta vid fel\n-u: Fel vid odefinierad variabel\n-o pipefail: Pipe-felhantering', category: 'Skriptstruktur', difficulty: 'VG' },
    { id: 't3-28', front: 'Hur får du skriptets egen sökväg?', back: 'SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"\nPortabel metod att hitta skriptets katalog.', category: 'Skriptstruktur', difficulty: 'VG' },
    { id: 't3-29', front: 'Vad är $$ och $!?', back: '$$: PID för nuvarande shell/skript\n$!: PID för senaste bakgrundsprocess', category: 'Specialvariabler', difficulty: 'VG' },
    { id: 't3-30', front: 'Hur skickar du ett skripts output till både fil och terminal?', back: 'kommando | tee filnamn\ntee: Skriver till fil OCH stdout', category: 'I/O', difficulty: 'VG' }
]

// =============================================================================
// TASK 4: VARIABLER & DATATYPER (30 flashcards)
// =============================================================================

const TASK_4_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't4-1', front: 'Hur deklarerar du en variabel i bash?', back: 'namn="värde"\nINGA mellanslag runt =!', category: 'Variabler', difficulty: 'G' },
    { id: 't4-2', front: 'Hur läser du värdet av en variabel?', back: '$variabel\neller ${variabel}', category: 'Variabler', difficulty: 'G' },
    { id: 't4-3', front: 'Vilken miljövariabel innehåller hemkatalogen?', back: '$HOME\nEx: /home/användarnamn', category: 'Miljövariabler', difficulty: 'G' },
    { id: 't4-4', front: 'Vilken miljövariabel innehåller nuvarande användare?', back: '$USER\nEx: root, anna, etc', category: 'Miljövariabler', difficulty: 'G' },
    { id: 't4-5', front: 'Vilken miljövariabel innehåller sökvägar för kommandon?', back: '$PATH\nKolonseparerad lista: /usr/bin:/usr/local/bin', category: 'Miljövariabler', difficulty: 'G' },
    { id: 't4-6', front: 'Hur visar du alla miljövariabler?', back: 'env\neller printenv', category: 'Miljövariabler', difficulty: 'G' },
    { id: 't4-7', front: 'Vad gör export variabel?', back: 'Gör variabeln tillgänglig för barnprocesser.\nUtan export: Endast lokal i nuvarande shell.', category: 'Miljövariabler', difficulty: 'G' },
    { id: 't4-8', front: 'Hur får du längden av en sträng i bash?', back: '${#variabel}\nEx: str="hej"; echo ${#str}  # 3', category: 'Stränghantering', difficulty: 'G' },
    { id: 't4-9', front: 'Vad innehåller $PWD?', back: 'Nuvarande arbetskatalog (Present Working Directory).\nSamma som output från pwd-kommandot.', category: 'Miljövariabler', difficulty: 'G' },
    { id: 't4-10', front: 'Vad innehåller $SHELL?', back: 'Sökvägen till användarens standardshell.\nEx: /bin/bash, /bin/zsh', category: 'Miljövariabler', difficulty: 'G' },
    // Medium (12)
    { id: 't4-11', front: 'Hur tar du ut en substring i bash?', back: '${variabel:start:längd}\nEx: ${str:0:5} = första 5 tecken', category: 'Stränghantering', difficulty: 'G' },
    { id: 't4-12', front: 'Hur ersätter du text i en variabel?', back: '${variabel/mönster/ersättning} (första)\n${variabel//mönster/ersättning} (alla)', category: 'Stränghantering', difficulty: 'G' },
    { id: 't4-13', front: 'Hur tar du bort filändelse från en variabel?', back: '${variabel%.*}\nEx: fil="test.txt"; echo ${fil%.*}  # test', category: 'Stränghantering', difficulty: 'G' },
    { id: 't4-14', front: 'Skillnad mellan ${var%pattern} och ${var%%pattern}?', back: '%: Ta bort kortaste matchning från slutet\n%%: Ta bort längsta matchning från slutet', category: 'Stränghantering', difficulty: 'G' },
    { id: 't4-15', front: 'Hur deklarerar du en array i bash?', back: 'array=("a" "b" "c")\neller declare -a array', category: 'Arrayer', difficulty: 'G' },
    { id: 't4-16', front: 'Hur kommer du åt första elementet i en array?', back: '${array[0]}\nArrayer är 0-indexerade i bash.', category: 'Arrayer', difficulty: 'G' },
    { id: 't4-17', front: 'Hur får du alla element i en array?', back: '${array[@]}\neller ${array[*]}', category: 'Arrayer', difficulty: 'G' },
    { id: 't4-18', front: 'Hur får du antalet element i en array?', back: '${#array[@]}\n# ger längd, @ för alla element.', category: 'Arrayer', difficulty: 'G' },
    { id: 't4-19', front: 'Hur lägger du till element i en array?', back: 'array+=("nytt_element")\neller array[${#array[@]}]="nytt"', category: 'Arrayer', difficulty: 'G' },
    { id: 't4-20', front: 'Vad är skillnaden mellan $@ och $*?', back: '$@: Varje argument som separat sträng\n$*: Alla argument som EN sträng', category: 'Specialvariabler', difficulty: 'G' },
    { id: 't4-21', front: 'Vad innehåller $# i ett skript?', back: 'Antal argument som skickades till skriptet.\nEx: ./skript.sh a b c → $# = 3', category: 'Specialvariabler', difficulty: 'G' },
    { id: 't4-22', front: 'Vad innehåller $0, $1, $2...?', back: '$0: Skriptets namn\n$1: Första argumentet\n$2: Andra argumentet, osv.', category: 'Specialvariabler', difficulty: 'G' },
    // Hard (8)
    { id: 't4-23', front: 'Hur gör du en variabel readonly?', back: 'readonly variabel="värde"\neller declare -r variabel="värde"', category: 'Variabler', difficulty: 'VG' },
    { id: 't4-24', front: 'Hur deklarerar du en integer-variabel?', back: 'declare -i nummer=42\nTillåter aritmetik utan $(( ))', category: 'Variabler', difficulty: 'VG' },
    { id: 't4-25', front: 'Hur skapar du ett associativt array (hash)?', back: 'declare -A hash\nhash[nyckel]="värde"', category: 'Arrayer', difficulty: 'VG' },
    { id: 't4-26', front: 'Hur får du alla nycklar i ett associativt array?', back: '${!hash[@]}\n! ger nycklar istället för värden.', category: 'Arrayer', difficulty: 'VG' },
    { id: 't4-27', front: 'Vad gör ${variabel:-default}?', back: 'Returnerar default om variabel är tom eller odefinierad.\nSätter INTE variabeln.', category: 'Parameterexpansion', difficulty: 'VG' },
    { id: 't4-28', front: 'Vad gör ${variabel:=default}?', back: 'Returnerar default OCH sätter variabeln om den är tom/odefinierad.', category: 'Parameterexpansion', difficulty: 'VG' },
    { id: 't4-29', front: 'Vad gör ${variabel:?felmeddelande}?', back: 'Ger fel och avslutar om variabeln är tom/odefinierad.\nBra för validering av obligatoriska variabler.', category: 'Parameterexpansion', difficulty: 'VG' },
    { id: 't4-30', front: 'Hur gör du strängkonkatenering i bash?', back: 'str1="Hello"\nstr2="$str1 World"\neller str1+=" World"', category: 'Stränghantering', difficulty: 'VG' }
]

// =============================================================================
// TASK 5: REGULJÄRA UTTRYCK - REGEX (30 flashcards)
// =============================================================================

const TASK_5_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't5-1', front: 'Vad matchar . (punkt) i regex?', back: 'ETT valfritt tecken (utom newline).\nEx: h.t matchar "hat", "hit", "hot"', category: 'Metatecken', difficulty: 'G' },
    { id: 't5-2', front: 'Vad betyder ^ i regex?', back: 'Början av raden.\n^Hello matchar rader som BÖRJAR med "Hello"', category: 'Ankare', difficulty: 'G' },
    { id: 't5-3', front: 'Vad betyder $ i regex?', back: 'Slutet av raden.\nworld$ matchar rader som SLUTAR med "world"', category: 'Ankare', difficulty: 'G' },
    { id: 't5-4', front: 'Vad matchar * i regex?', back: '0 eller FLER av föregående tecken.\na* matchar "", "a", "aa", "aaa"...', category: 'Kvantifierare', difficulty: 'G' },
    { id: 't5-5', front: 'Vad matchar + i regex?', back: '1 eller FLER av föregående tecken.\na+ matchar "a", "aa", "aaa"... (EJ tom sträng)', category: 'Kvantifierare', difficulty: 'G' },
    { id: 't5-6', front: 'Vad matchar ? i regex?', back: '0 eller 1 av föregående tecken (valfritt).\ncolou?r matchar "color" och "colour"', category: 'Kvantifierare', difficulty: 'G' },
    { id: 't5-7', front: 'Vad gör [] i regex?', back: 'Teckenklass - matchar ETT av tecknen inom.\n[abc] matchar "a", "b" eller "c"', category: 'Teckenklasser', difficulty: 'G' },
    { id: 't5-8', front: 'Hur matchar du siffror 0-9 med teckenklass?', back: '[0-9]\nMatchar en enda siffra.', category: 'Teckenklasser', difficulty: 'G' },
    { id: 't5-9', front: 'Hur matchar du bokstäver a-z med teckenklass?', back: '[a-z] för gemener\n[A-Z] för versaler\n[a-zA-Z] för alla bokstäver', category: 'Teckenklasser', difficulty: 'G' },
    { id: 't5-10', front: 'Vad gör grep -i?', back: 'Case insensitive sökning.\ngrep -i "error" matchar "Error", "ERROR", "error"', category: 'grep', difficulty: 'G' },
    // Medium (12)
    { id: 't5-11', front: 'Vad gör [^abc] i regex?', back: 'Negerad teckenklass - matchar alla tecken UTOM a, b, c.\n[^0-9] matchar allt utom siffror', category: 'Teckenklasser', difficulty: 'G' },
    { id: 't5-12', front: 'Vad gör | i regex?', back: 'OR/Alternativ.\ncat|dog matchar "cat" eller "dog"', category: 'Operatorer', difficulty: 'G' },
    { id: 't5-13', front: 'Vad gör () i regex?', back: 'Gruppering.\n(ab)+ matchar "ab", "abab", "ababab"...', category: 'Gruppering', difficulty: 'G' },
    { id: 't5-14', front: 'Vad matchar {n} i regex?', back: 'Exakt n förekomster.\na{3} matchar exakt "aaa"', category: 'Kvantifierare', difficulty: 'G' },
    { id: 't5-15', front: 'Vad matchar {n,m} i regex?', back: 'Mellan n och m förekomster.\na{2,4} matchar "aa", "aaa", "aaaa"', category: 'Kvantifierare', difficulty: 'G' },
    { id: 't5-16', front: 'Hur matchar du tomma rader med grep?', back: 'grep "^$" fil.txt\n^ = radstart, $ = radslut, inget emellan', category: 'grep', difficulty: 'G' },
    { id: 't5-17', front: 'Vad gör grep -v?', back: 'Invertera matchning - visa rader som INTE matchar.\ngrep -v "^#" visar icke-kommentarer', category: 'grep', difficulty: 'G' },
    { id: 't5-18', front: 'Vad gör grep -n?', back: 'Visar radnummer före varje matchning.\ngrep -n "error" fil.txt', category: 'grep', difficulty: 'G' },
    { id: 't5-19', front: 'Vad gör grep -E?', back: 'Extended regex - tillåter +, ?, |, () utan escape.\ngrep -E "error|warning" fil.txt', category: 'grep', difficulty: 'G' },
    { id: 't5-20', front: 'Hur matchar du rader som börjar med # (kommentarer)?', back: 'grep "^#" fil.txt\n^ förankrar till radstart', category: 'grep', difficulty: 'G' },
    { id: 't5-21', front: 'Hur söker du rekursivt i kataloger med grep?', back: 'grep -r "pattern" katalog/\n-r eller -R för rekursiv sökning', category: 'grep', difficulty: 'G' },
    { id: 't5-22', front: 'Vad gör grep -l?', back: 'Visa endast filnamn (inte matchande rader).\ngrep -l "TODO" *.py', category: 'grep', difficulty: 'G' },
    // Hard (8)
    { id: 't5-23', front: 'Hur matchar du en IP-adress med regex?', back: '[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\nEller: \\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}', category: 'Mönster', difficulty: 'VG' },
    { id: 't5-24', front: 'Vad är skillnaden mellan BRE och ERE?', back: 'BRE (Basic): ?, +, |, () kräver escape\nERE (Extended): Fungerar direkt (grep -E)', category: 'Regex-typer', difficulty: 'VG' },
    { id: 't5-25', front: 'Vad gör \\b i regex?', back: 'Ordgräns (word boundary).\n\\bword\\b matchar "word" men inte "password"', category: 'Ankare', difficulty: 'VG' },
    { id: 't5-26', front: 'Vad är skillnad mellan .* och .*? (greedy vs lazy)?', back: '.* är greedy - matchar så mycket som möjligt\n.*? är lazy - matchar så lite som möjligt', category: 'Kvantifierare', difficulty: 'VG' },
    { id: 't5-27', front: 'Vad gör grep -o?', back: 'Visa endast matchande del (inte hela raden).\ngrep -oE "[0-9]+" visar bara siffror', category: 'grep', difficulty: 'VG' },
    { id: 't5-28', front: 'Hur gör du en backreference i regex?', back: '\\1, \\2, etc refererar till fångade grupper.\n(\\w+) \\1 matchar upprepade ord som "the the"', category: 'Gruppering', difficulty: 'VG' },
    { id: 't5-29', front: 'Vad matchar \\d, \\w, \\s i regex?', back: '\\d = siffra [0-9]\n\\w = "ord-tecken" [a-zA-Z0-9_]\n\\s = whitespace (space, tab, newline)', category: 'Teckenklasser', difficulty: 'VG' },
    { id: 't5-30', front: 'Hur matchar du e-postadresser med regex?', back: '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}\nFörenklad version - email-validering är komplext!', category: 'Mönster', difficulty: 'VG' }
]

// =============================================================================
// TASK 6: SED - STREAM EDITOR (30 flashcards)
// =============================================================================

const TASK_6_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't6-1', front: 'Vad är sed?', back: 'Stream Editor - verktyg för textmanipulation.\nProcessar text rad för rad.', category: 'Grundläggande', difficulty: 'G' },
    { id: 't6-2', front: 'Grundläggande sed-syntax för ersättning?', back: "sed 's/gammal/ny/' fil.txt\ns = substitute (ersätt)", category: 'Syntax', difficulty: 'G' },
    { id: 't6-3', front: 'Vad gör g-flaggan i sed?', back: "Ersätt ALLA förekomster på raden (global).\nsed 's/a/b/g' ersätter alla 'a' med 'b'", category: 'Flaggor', difficulty: 'G' },
    { id: 't6-4', front: 'Vad gör sed -i?', back: 'In-place editing - ändrar filen direkt.\nsed -i "s/old/new/g" fil.txt', category: 'Flaggor', difficulty: 'G' },
    { id: 't6-5', front: 'Hur gör du backup med sed -i?', back: 'sed -i.bak "s/old/new/g" fil.txt\nSkapar fil.txt.bak före ändring', category: 'Flaggor', difficulty: 'G' },
    { id: 't6-6', front: 'Hur raderar du rader med sed?', back: "sed '/pattern/d' fil.txt\nd = delete", category: 'Kommandon', difficulty: 'G' },
    { id: 't6-7', front: 'Hur raderar du rad 5 med sed?', back: "sed '5d' fil.txt\nAnge radnummer före d", category: 'Kommandon', difficulty: 'G' },
    { id: 't6-8', front: 'Hur visar du endast rad 10 med sed?', back: "sed -n '10p' fil.txt\n-n suppress output, p = print", category: 'Kommandon', difficulty: 'G' },
    { id: 't6-9', front: 'Hur raderar du kommentarer (rader som börjar med #)?', back: "sed '/^#/d' fil.txt\n^# = börjar med #", category: 'Mönster', difficulty: 'G' },
    { id: 't6-10', front: 'Hur raderar du tomma rader med sed?', back: "sed '/^$/d' fil.txt\n^$ = tom rad", category: 'Mönster', difficulty: 'G' },
    // Medium (12)
    { id: 't6-11', front: 'Vad gör sed -n?', back: 'Suppress automatic printing.\nAnvänd med p för att visa specifika rader.', category: 'Flaggor', difficulty: 'G' },
    { id: 't6-12', front: 'Hur använder du annan delimiter än /?', back: "sed 's|/usr/local|/opt|g'\neller sed 's#old#new#g'\nAnvänd |, #, eller annat tecken", category: 'Syntax', difficulty: 'G' },
    { id: 't6-13', front: 'Hur raderar du rad 1-10 med sed?', back: "sed '1,10d' fil.txt\nKommaseparerad range", category: 'Adressering', difficulty: 'G' },
    { id: 't6-14', front: 'Hur visar du rad 5-15 med sed?', back: "sed -n '5,15p' fil.txt\n-n + p för att visa range", category: 'Adressering', difficulty: 'G' },
    { id: 't6-15', front: 'Hur kör du flera sed-kommandon?', back: "sed -e 's/a/b/' -e 's/c/d/' fil.txt\neller sed 's/a/b/; s/c/d/' fil.txt", category: 'Syntax', difficulty: 'G' },
    { id: 't6-16', front: 'Vad gör i-flaggan i sed?', back: "Case insensitive matchning.\nsed 's/error/warning/gi' matchar ERROR, Error, etc", category: 'Flaggor', difficulty: 'G' },
    { id: 't6-17', front: 'Hur ersätter du endast på rad 5?', back: "sed '5s/old/new/' fil.txt\nAnge radnummer före s", category: 'Adressering', difficulty: 'G' },
    { id: 't6-18', front: 'Hur ersätter du på rader som matchar ett mönster?', back: "sed '/error/s/old/new/g' fil.txt\nErsätt endast på rader med 'error'", category: 'Adressering', difficulty: 'G' },
    { id: 't6-19', front: 'Hur infogar du text före rad 1?', back: "sed '1i\\Ny första rad' fil.txt\ni = insert före", category: 'Kommandon', difficulty: 'G' },
    { id: 't6-20', front: 'Hur lägger du till text efter sista raden?', back: "sed '$a\\Ny sista rad' fil.txt\n$ = sista raden, a = append", category: 'Kommandon', difficulty: 'G' },
    { id: 't6-21', front: 'Vad gör sed -r eller sed -E?', back: 'Extended regex - +, ?, |, () utan escape.\nsed -E "s/(foo)+/bar/"', category: 'Flaggor', difficulty: 'G' },
    { id: 't6-22', front: 'Hur ersätter du endast andra förekomsten på varje rad?', back: "sed 's/old/new/2' fil.txt\nSiffra anger vilken förekomst", category: 'Flaggor', difficulty: 'G' },
    // Hard (8)
    { id: 't6-23', front: 'Hur gör du backreference i sed?', back: "sed 's/\\(.*\\):\\(.*\\)/\\2:\\1/' fil.txt\n\\1, \\2 refererar till fångade grupper", category: 'Avancerat', difficulty: 'VG' },
    { id: 't6-24', front: 'Hur raderar du rader mellan två mönster?', back: "sed '/START/,/END/d' fil.txt\nRaderar från START till END (inkl)", category: 'Adressering', difficulty: 'VG' },
    { id: 't6-25', front: 'Hur ersätter du text mellan två mönster?', back: "sed '/START/,/END/s/old/new/g' fil.txt\nErsätt endast inom range", category: 'Adressering', difficulty: 'VG' },
    { id: 't6-26', front: 'Vad gör & i sed ersättning?', back: 'Hela matchningen.\nsed "s/[0-9]*/(&)/" sätter parentes runt siffror', category: 'Avancerat', difficulty: 'VG' },
    { id: 't6-27', front: 'Hur skriver du över samma rad (carriage return)?', back: "sed -n 'p; s/./-/g; p' fil.txt\nVisa rad, sen ersätt med streck", category: 'Avancerat', difficulty: 'VG' },
    { id: 't6-28', front: 'Hur raderar du från rad 10 till slutet?', back: "sed '10,$d' fil.txt\n$ = sista raden", category: 'Adressering', difficulty: 'VG' },
    { id: 't6-29', front: 'Vad gör N-kommandot i sed?', back: 'Läser nästa rad och lägger till i pattern space.\nAnvänds för multi-line operationer.', category: 'Avancerat', difficulty: 'VG' },
    { id: 't6-30', front: 'Hur gör du en sed-operation på varannan rad?', back: "sed 'n; s/old/new/' fil.txt\nn = skip to next line", category: 'Avancerat', difficulty: 'VG' }
]

// =============================================================================
// TASK 7: AWK - TEXTBEARBETNING (30 flashcards)
// =============================================================================

const TASK_7_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't7-1', front: 'Vad är awk?', back: 'Kraftfullt verktyg för kolumnbaserad textbearbetning.\nProcessar text fält för fält (kolumnvis).', category: 'Grundläggande', difficulty: 'G' },
    { id: 't7-2', front: 'Grundläggande awk-syntax?', back: "awk 'pattern { action }' fil.txt\nPattern matchar rader, action utförs.", category: 'Syntax', difficulty: 'G' },
    { id: 't7-3', front: 'Vad är $0 i awk?', back: "Hela raden.\nawk '{print $0}' skriver ut varje rad.", category: 'Fält', difficulty: 'G' },
    { id: 't7-4', front: 'Vad är $1, $2, $3 i awk?', back: 'Fält 1, 2, 3 (kolumner).\nStandard separator är whitespace.', category: 'Fält', difficulty: 'G' },
    { id: 't7-5', front: 'Vad är $NF i awk?', back: 'Sista fältet på raden.\nNF = Number of Fields', category: 'Fält', difficulty: 'G' },
    { id: 't7-6', front: 'Hur ändrar du fältseparatorn i awk?', back: 'awk -F: "..."\neller awk -F"," för CSV', category: 'Syntax', difficulty: 'G' },
    { id: 't7-7', front: 'Hur skriver du ut kolumn 1 och 3 med awk?', back: "awk '{print $1, $3}' fil.txt\nKomma ger mellanslag i output. Använd enkla citattecken!", category: 'Syntax', difficulty: 'G' },
    { id: 't7-8', front: 'Vad gör NR i awk?', back: "Number of Records - radnummer.\nawk '{print NR, $0}' numrerar rader.", category: 'Variabler', difficulty: 'G' },
    { id: 't7-9', front: 'Vad gör NF i awk?', back: "Number of Fields - antal fält på raden.\nawk '{print NF}' visar antal kolumner.", category: 'Variabler', difficulty: 'G' },
    { id: 't7-10', front: 'Hur listar du användarnamn från /etc/passwd?', back: "awk -F: '{print $1}' /etc/passwd\n: är separator, $1 är användarnamn", category: 'Praktiskt', difficulty: 'G' },
    // Medium (12)
    { id: 't7-11', front: 'Hur filtrerar du rader med awk?', back: 'awk "/pattern/ {print}" fil.txt\neller awk "$3 > 100" fil.txt', category: 'Filtrering', difficulty: 'G' },
    { id: 't7-12', front: 'Vad gör BEGIN-blocket i awk?', back: 'Körs EN gång FÖRE första raden.\nawk "BEGIN {print header} {print}"', category: 'Block', difficulty: 'G' },
    { id: 't7-13', front: 'Vad gör END-blocket i awk?', back: 'Körs EN gång EFTER sista raden.\nawk "{sum+=$1} END {print sum}"', category: 'Block', difficulty: 'G' },
    { id: 't7-14', front: 'Hur summerar du en kolumn med awk?', back: 'awk "{sum += $1} END {print sum}" fil.txt\nAckumulera i variabel, skriv ut i END.', category: 'Beräkning', difficulty: 'G' },
    { id: 't7-15', front: 'Hur räknar du antal rader med awk?', back: 'awk "END {print NR}" fil.txt\nNR i END = totala antalet rader.', category: 'Beräkning', difficulty: 'G' },
    { id: 't7-16', front: 'Hur beräknar du medelvärde med awk?', back: 'awk "{sum+=$1} END {print sum/NR}" fil.txt\nSumma delat med antal rader.', category: 'Beräkning', difficulty: 'G' },
    { id: 't7-17', front: 'Hur formaterar du output med printf i awk?', back: 'awk "{printf \\"%-10s %d\\n\\", $1, $2}"\n%s=sträng, %d=heltal, %-10=vänsterjusterad', category: 'Formatering', difficulty: 'G' },
    { id: 't7-18', front: 'Hur skriver du ut rader med villkor i awk?', back: 'awk "$3 > 100 {print $1}" fil.txt\nSkriver ut $1 om $3 > 100', category: 'Filtrering', difficulty: 'G' },
    { id: 't7-19', front: 'Vad är OFS i awk?', back: 'Output Field Separator.\nawk "BEGIN {OFS=\\",\\"} {print $1,$2}"', category: 'Variabler', difficulty: 'G' },
    { id: 't7-20', front: 'Hur hoppar du över första raden (header)?', back: 'awk "NR > 1 {print}" fil.txt\nNR > 1 = alla rader utom första.', category: 'Filtrering', difficulty: 'G' },
    { id: 't7-21', front: 'Hur skriver du ut specifika radnummer?', back: 'awk "NR==5" fil.txt (rad 5)\nawk "NR>=5 && NR<=10" (rad 5-10)', category: 'Filtrering', difficulty: 'G' },
    { id: 't7-22', front: 'Hur använder du variabler i awk?', back: 'awk -v threshold=100 "$1 > threshold"\neller awk "BEGIN {x=5} {print $1+x}"', category: 'Variabler', difficulty: 'G' },
    // Hard (8)
    { id: 't7-23', front: 'Hur hittar du unika värden med awk?', back: 'awk "!seen[$1]++" fil.txt\nAssociativ array som tracker sedda värden.', category: 'Avancerat', difficulty: 'VG' },
    { id: 't7-24', front: 'Hur grupperar och räknar du med awk?', back: 'awk "{count[$1]++} END {for (k in count) print k, count[k]}"\nRäkna förekomster per nyckel.', category: 'Avancerat', difficulty: 'VG' },
    { id: 't7-25', front: 'Hur hittar du max/min med awk?', back: 'awk "BEGIN{max=0} $1>max{max=$1} END{print max}"\nUppdatera max om värde är större.', category: 'Beräkning', difficulty: 'VG' },
    { id: 't7-26', front: 'Vad är FS och RS i awk?', back: 'FS = Field Separator (kolumnavgränsare)\nRS = Record Separator (radavgränsare, default \\n)', category: 'Variabler', difficulty: 'VG' },
    { id: 't7-27', front: 'Hur kör du if/else i awk?', back: 'awk "{if ($1>10) print \\"big\\"; else print \\"small\\"}"\nStandard programmeringssyntax.', category: 'Kontrollflöde', difficulty: 'VG' },
    { id: 't7-28', front: 'Hur loopar du i awk?', back: 'for (i=1; i<=NF; i++) print $i\neller while, do-while', category: 'Kontrollflöde', difficulty: 'VG' },
    { id: 't7-29', front: 'Hur definierar du funktioner i awk?', back: 'awk "function double(x) {return x*2} {print double($1)}"\nEgna funktioner med return.', category: 'Avancerat', difficulty: 'VG' },
    { id: 't7-30', front: 'Hur processar du flera filer med awk?', back: 'awk "FNR==1 {print FILENAME}" fil1 fil2\nFNR=radnummer i aktuell fil, FILENAME=filnamn', category: 'Avancerat', difficulty: 'VG' }
]

// =============================================================================
// TASK 8: VILLKOR (IF/ELSE) (30 flashcards)
// =============================================================================

const TASK_8_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't8-1', front: 'Grundläggande if-syntax i bash?', back: 'if [ villkor ]; then\n  kommando\nfi', category: 'Syntax', difficulty: 'G' },
    { id: 't8-2', front: 'Hur avslutar du ett if-block?', back: 'fi\n(if baklänges)', category: 'Syntax', difficulty: 'G' },
    { id: 't8-3', front: 'Hur skriver du if-else i bash?', back: 'if [ villkor ]; then\n  kommando1\nelse\n  kommando2\nfi', category: 'Syntax', difficulty: 'G' },
    { id: 't8-4', front: 'Hur skriver du elif i bash?', back: 'if [ ]; then\n...\nelif [ ]; then\n...\nelse\n...\nfi', category: 'Syntax', difficulty: 'G' },
    { id: 't8-5', front: 'Hur testar du om en fil existerar?', back: '[ -e fil ] eller [ -f fil ]\n-e = exists, -f = regular file', category: 'Filtest', difficulty: 'G' },
    { id: 't8-6', front: 'Hur testar du om en katalog existerar?', back: '[ -d katalog ]\n-d = directory', category: 'Filtest', difficulty: 'G' },
    { id: 't8-7', front: 'Hur jämför du två strängar för likhet?', back: '[ "$a" = "$b" ]\neller [ "$a" == "$b" ]', category: 'Strängar', difficulty: 'G' },
    { id: 't8-8', front: 'Hur testar du om en sträng är tom?', back: '[ -z "$str" ]\n-z = zero length', category: 'Strängar', difficulty: 'G' },
    { id: 't8-9', front: 'Hur testar du om en sträng INTE är tom?', back: '[ -n "$str" ]\n-n = non-zero length', category: 'Strängar', difficulty: 'G' },
    { id: 't8-10', front: 'Varför behövs mellanslag i [ ]?', back: '[ är ett kommando (test)!\n[ $x = 5 ] ← mellanslag krävs', category: 'Syntax', difficulty: 'G' },
    // Medium (12)
    { id: 't8-11', front: 'Hur testar du om tal är lika?', back: '[ $a -eq $b ]\n-eq = equal', category: 'Numeriskt', difficulty: 'G' },
    { id: 't8-12', front: 'Hur testar du om $a är större än $b?', back: '[ $a -gt $b ]\n-gt = greater than', category: 'Numeriskt', difficulty: 'G' },
    { id: 't8-13', front: 'Hur testar du om $a är mindre än $b?', back: '[ $a -lt $b ]\n-lt = less than', category: 'Numeriskt', difficulty: 'G' },
    { id: 't8-14', front: 'Vad gör -ge och -le?', back: '-ge = greater or equal (>=)\n-le = less or equal (<=)', category: 'Numeriskt', difficulty: 'G' },
    { id: 't8-15', front: 'Vad gör -ne?', back: '-ne = not equal (!=)\n[ $a -ne $b ]', category: 'Numeriskt', difficulty: 'G' },
    { id: 't8-16', front: 'Hur testar du om fil är läsbar?', back: '[ -r fil ]\n-r = readable', category: 'Filtest', difficulty: 'G' },
    { id: 't8-17', front: 'Hur testar du om fil är skrivbar?', back: '[ -w fil ]\n-w = writable', category: 'Filtest', difficulty: 'G' },
    { id: 't8-18', front: 'Hur testar du om fil är körbar?', back: '[ -x fil ]\n-x = executable', category: 'Filtest', difficulty: 'G' },
    { id: 't8-19', front: 'Hur kombinerar du villkor med AND?', back: '[ villkor1 ] && [ villkor2 ]\neller [ villkor1 -a villkor2 ]', category: 'Logik', difficulty: 'G' },
    { id: 't8-20', front: 'Hur kombinerar du villkor med OR?', back: '[ villkor1 ] || [ villkor2 ]\neller [ villkor1 -o villkor2 ]', category: 'Logik', difficulty: 'G' },
    { id: 't8-21', front: 'Hur negerar du ett villkor?', back: '[ ! villkor ]\n! = NOT', category: 'Logik', difficulty: 'G' },
    { id: 't8-22', front: 'Vad testar [ -s fil ]?', back: 'Filen existerar OCH har storlek > 0.\n-s = size greater than zero', category: 'Filtest', difficulty: 'G' },
    // Hard (8)
    { id: 't8-23', front: 'Skillnad mellan [ ] och [[ ]]?', back: '[[ ]] är bash-specifikt och kraftfullare:\n- Stödjer && och || inuti\n- Säkrare med variabler\n- Stödjer =~ för regex', category: 'Avancerat', difficulty: 'VG' },
    { id: 't8-24', front: 'Hur använder du regex i villkor?', back: '[[ $str =~ ^[0-9]+$ ]]\nKontrollera om str är endast siffror.', category: 'Avancerat', difficulty: 'VG' },
    { id: 't8-25', front: 'Vad gör (( )) i bash?', back: 'Aritmetisk kontext.\nif (( x > 5 )); then ...\nTillåter vanlig matematik-syntax.', category: 'Avancerat', difficulty: 'VG' },
    { id: 't8-26', front: 'Hur testar du om variabel är satt?', back: '[ -v variabel ] (bash 4.2+)\neller [ -n "${variabel+x}" ]', category: 'Avancerat', difficulty: 'VG' },
    { id: 't8-27', front: 'Vad är case-satsen i bash?', back: 'case $var in\n  pattern1) cmd1 ;;\n  pattern2) cmd2 ;;\n  *) default ;;\nesac', category: 'Kontrollflöde', difficulty: 'VG' },
    { id: 't8-28', front: 'Hur testar du fil1 är nyare än fil2?', back: '[ fil1 -nt fil2 ]\n-nt = newer than', category: 'Filtest', difficulty: 'VG' },
    { id: 't8-29', front: 'Hur testar du fil1 är äldre än fil2?', back: '[ fil1 -ot fil2 ]\n-ot = older than', category: 'Filtest', difficulty: 'VG' },
    { id: 't8-30', front: 'Hur gör du ternary operator i bash?', back: '[[ villkor ]] && cmd1 || cmd2\neller: result=$(( villkor ? a : b ))', category: 'Avancerat', difficulty: 'VG' }
]

// =============================================================================
// TASK 9: INTERAKTIVA SKRIPT (30 flashcards)
// =============================================================================

const TASK_9_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't9-1', front: 'Hur läser du input från användaren i bash?', back: 'read variabel\neller read -p "Prompt: " variabel', category: 'read', difficulty: 'G' },
    { id: 't9-2', front: 'Hur visar du en prompt med read?', back: 'read -p "Ange namn: " namn\n-p = prompt', category: 'read', difficulty: 'G' },
    { id: 't9-3', front: 'Hur läser du lösenord utan att visa det?', back: 'read -s -p "Lösenord: " pass\n-s = silent/secret', category: 'read', difficulty: 'G' },
    { id: 't9-4', front: 'Hur sätter du timeout på read?', back: 'read -t 10 variabel\n-t = timeout i sekunder', category: 'read', difficulty: 'G' },
    { id: 't9-5', front: 'Hur läser du input till en array?', back: 'read -a array\nSeparerar på whitespace.', category: 'read', difficulty: 'G' },
    { id: 't9-6', front: 'Vad gör select i bash?', back: 'Skapar en numrerad meny.\nselect val in "A" "B" "C"; do ... done', category: 'select', difficulty: 'G' },
    { id: 't9-7', front: 'Hur avslutar du en select-loop?', back: 'break\nAvslutar loopen och fortsätter.', category: 'select', difficulty: 'G' },
    { id: 't9-8', front: 'Grundläggande case-syntax i bash?', back: 'case $var in\n  pattern) kommando ;;\nesac', category: 'case', difficulty: 'G' },
    { id: 't9-9', front: 'Hur avslutar du ett case-block?', back: 'esac\n(case baklänges)', category: 'case', difficulty: 'G' },
    { id: 't9-10', front: 'Hur hanterar du "default" i case?', back: '*) kommando ;;\n* matchar allt annat.', category: 'case', difficulty: 'G' },
    // Medium (12)
    { id: 't9-11', front: 'Hur begränsar du input till N tecken?', back: 'read -n 1 char\n-n = antal tecken', category: 'read', difficulty: 'G' },
    { id: 't9-12', front: 'Hur läser du en hel rad inklusive backslash?', back: 'read -r line\n-r = raw (ingen escape-tolkning)', category: 'read', difficulty: 'G' },
    { id: 't9-13', front: 'Hur läser du från en fil rad för rad?', back: 'while IFS= read -r line; do\n  echo "$line"\ndone < fil.txt', category: 'read', difficulty: 'G' },
    { id: 't9-14', front: 'Vad är IFS i bash?', back: 'Internal Field Separator.\nDefault: space, tab, newline.', category: 'Variabler', difficulty: 'G' },
    { id: 't9-15', front: 'Hur ändrar du PS3 för select?', back: 'PS3="Välj: "\nÄndrar prompten i select-menyn.', category: 'select', difficulty: 'G' },
    { id: 't9-16', front: 'Hur matchar du flera patterns i case?', back: 'case $var in\n  a|b|c) echo "a, b eller c" ;;\nesac', category: 'case', difficulty: 'G' },
    { id: 't9-17', front: 'Hur matchar du prefix i case?', back: 'case $var in\n  start*) echo "börjar med start" ;;\nesac', category: 'case', difficulty: 'G' },
    { id: 't9-18', front: 'Hur validerar du numerisk input?', back: 'if [[ $input =~ ^[0-9]+$ ]]; then\n  echo "Giltigt nummer"\nfi', category: 'Validering', difficulty: 'G' },
    { id: 't9-19', front: 'Hur loopar du tills giltig input?', back: 'while true; do\n  read -p "Input: " val\n  [[ -n "$val" ]] && break\ndone', category: 'Validering', difficulty: 'G' },
    { id: 't9-20', front: 'Vad innehåller REPLY efter read utan variabel?', back: 'Användarens input.\nread; echo $REPLY', category: 'read', difficulty: 'G' },
    { id: 't9-21', front: 'Hur läser du från pipe in i read?', back: 'echo "text" | read var\n(OBS: körs i subshell!)', category: 'read', difficulty: 'G' },
    { id: 't9-22', front: 'Hur undviker du subshell-problemet med pipe?', back: 'read var <<< "text"\neller: var=$(echo "text")', category: 'read', difficulty: 'G' },
    // Hard (8)
    { id: 't9-23', front: 'Hur gör du ;& i case (fall through)?', back: 'case $var in\n  a) echo "a";& # fortsätt till nästa\n  b) echo "b" ;;\nesac', category: 'case', difficulty: 'VG' },
    { id: 't9-24', front: 'Hur gör du ;;& i case (test nästa pattern)?', back: 'case $var in\n  *a*) echo "innehåller a";;& # testa nästa\n  *b*) echo "innehåller b";;\nesac', category: 'case', difficulty: 'VG' },
    { id: 't9-25', front: 'Hur läser du tangent utan Enter?', back: 'read -n 1 -s key\n-n 1 = ett tecken, -s = tyst', category: 'read', difficulty: 'VG' },
    { id: 't9-26', front: 'Hur hanterar du piltangenter i read?', back: 'read -sn3 key\nPiltangenter är escape-sekvenser (3 tecken).', category: 'read', difficulty: 'VG' },
    { id: 't9-27', front: 'Hur gör du en bekräftelse-prompt?', back: 'read -p "Fortsätt? [y/N] " -n 1 svar\n[[ $svar =~ ^[Yy]$ ]] && echo "Ja"', category: 'Validering', difficulty: 'VG' },
    { id: 't9-28', front: 'Hur läser du flera variabler på en rad?', back: 'read var1 var2 var3\nSepareras på IFS.', category: 'read', difficulty: 'VG' },
    { id: 't9-29', front: 'Hur sätter du default-värde om input är tom?', back: 'read -p "Namn [default]: " namn\nnamn=${namn:-default}', category: 'Validering', difficulty: 'VG' },
    { id: 't9-30', front: 'Hur gör du interaktiv meny med while+case?', back: 'while true; do\n  read -p "> " cmd\n  case $cmd in\n    q) break;;\n    *) echo "$cmd";;\n  esac\ndone', category: 'Meny', difficulty: 'VG' }
]

// =============================================================================
// TASK 10: LOOPAR (FOR/WHILE) (30 flashcards)
// =============================================================================

const TASK_10_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't10-1', front: 'Grundläggande for-loop syntax i bash?', back: 'for var in lista; do\n  kommandon\ndone', category: 'for', difficulty: 'G' },
    { id: 't10-2', front: 'Hur loopar du genom en lista av ord?', back: 'for ord in hej på dig; do\n  echo $ord\ndone', category: 'for', difficulty: 'G' },
    { id: 't10-3', front: 'Hur loopar du genom siffror 1-5?', back: 'for i in {1..5}; do\n  echo $i\ndone', category: 'for', difficulty: 'G' },
    { id: 't10-4', front: 'Hur loopar du genom filer med .txt?', back: 'for fil in *.txt; do\n  echo $fil\ndone', category: 'for', difficulty: 'G' },
    { id: 't10-5', front: 'Grundläggande while-loop syntax?', back: 'while [ villkor ]; do\n  kommandon\ndone', category: 'while', difficulty: 'G' },
    { id: 't10-6', front: 'Hur gör du en oändlig loop?', back: 'while true; do\n  ...\ndone\neller: while :; do', category: 'while', difficulty: 'G' },
    { id: 't10-7', front: 'Hur avbryter du en loop?', back: 'break\nAvslutar hela loopen.', category: 'Kontroll', difficulty: 'G' },
    { id: 't10-8', front: 'Hur hoppar du till nästa iteration?', back: 'continue\nHoppar över resten, börjar nästa varv.', category: 'Kontroll', difficulty: 'G' },
    { id: 't10-9', front: 'Vad är skillnaden på while och until?', back: 'while: körs SÅ LÄNGE villkor är sant\nuntil: körs TILLS villkor blir sant', category: 'Loop-typer', difficulty: 'G' },
    { id: 't10-10', front: 'Hur loopar du med steg (t.ex. 0,2,4,6)?', back: 'for i in {0..6..2}; do\n  echo $i\ndone', category: 'for', difficulty: 'G' },
    // Medium (12)
    { id: 't10-11', front: 'C-style for-loop i bash?', back: 'for ((i=0; i<5; i++)); do\n  echo $i\ndone', category: 'for', difficulty: 'G' },
    { id: 't10-12', front: 'Hur räknar du upp en variabel i while?', back: 'while [ $i -lt 5 ]; do\n  echo $i\n  ((i++))\ndone', category: 'while', difficulty: 'G' },
    { id: 't10-13', front: 'Hur läser du fil rad för rad i while?', back: 'while IFS= read -r line; do\n  echo "$line"\ndone < fil.txt', category: 'while', difficulty: 'G' },
    { id: 't10-14', front: 'Hur loopar du genom kommando-output?', back: 'for fil in $(ls); do\n  echo $fil\ndone\n(eller: while read)', category: 'for', difficulty: 'G' },
    { id: 't10-15', front: 'Hur avbryter du flera nivåer av nästlade loopar?', back: 'break 2\nAvbryter 2 nivåer utåt.', category: 'Kontroll', difficulty: 'G' },
    { id: 't10-16', front: 'Hur fortsätter du i yttre loop från inre?', back: 'continue 2\nHoppar till nästa iteration av yttre loop.', category: 'Kontroll', difficulty: 'G' },
    { id: 't10-17', front: 'Hur loopar du genom array-element?', back: 'for elem in "${array[@]}"; do\n  echo $elem\ndone', category: 'for', difficulty: 'G' },
    { id: 't10-18', front: 'Hur loopar du med index genom array?', back: 'for i in "${!array[@]}"; do\n  echo "$i: ${array[$i]}"\ndone', category: 'for', difficulty: 'G' },
    { id: 't10-19', front: 'Vad gör seq kommandot?', back: 'Genererar sekvens av tal.\nseq 1 5 → 1 2 3 4 5\nseq 0 2 10 → 0 2 4 6 8 10', category: 'Verktyg', difficulty: 'G' },
    { id: 't10-20', front: 'Hur kör du kommando tills det lyckas?', back: 'until kommando; do\n  sleep 1\ndone\nVäntar tills exit code 0.', category: 'until', difficulty: 'G' },
    { id: 't10-21', front: 'Hur loopar du baklänges (5,4,3,2,1)?', back: 'for i in {5..1}; do\n  echo $i\ndone', category: 'for', difficulty: 'G' },
    { id: 't10-22', front: 'Hur processar du pipe-data i while?', back: 'cat fil.txt | while read line; do\n  echo "$line"\ndone', category: 'while', difficulty: 'G' },
    // Hard (8)
    { id: 't10-23', front: 'Problem med pipe till while (subshell)?', back: 'Variabeländringar i while försvinner!\nLösning: while ... done < <(kommando)', category: 'Avancerat', difficulty: 'VG' },
    { id: 't10-24', front: 'Vad är process substitution?', back: '< <(kommando)\nTillåter läsning från kommando som fil.', category: 'Avancerat', difficulty: 'VG' },
    { id: 't10-25', front: 'Hur loopar du genom associativt array?', back: 'for key in "${!hash[@]}"; do\n  echo "$key: ${hash[$key]}"\ndone', category: 'for', difficulty: 'VG' },
    { id: 't10-26', front: 'Hur gör du parallell loop i bash?', back: 'for fil in *.txt; do\n  process "$fil" &\ndone\nwait', category: 'Avancerat', difficulty: 'VG' },
    { id: 't10-27', front: 'Hur begränsar du parallella processer?', back: 'parallel -j 4 process ::: *.txt\neller xargs -P 4', category: 'Avancerat', difficulty: 'VG' },
    { id: 't10-28', front: 'Hur loopar du rekursivt genom kataloger?', back: 'shopt -s globstar\nfor fil in **/*.txt; do\n  echo $fil\ndone', category: 'for', difficulty: 'VG' },
    { id: 't10-29', front: 'Hur använder du find med while?', back: 'find . -name "*.txt" -print0 | while IFS= read -r -d "" fil; do\n  echo "$fil"\ndone', category: 'while', difficulty: 'VG' },
    { id: 't10-30', front: 'Hur gör du infinite retry med exponential backoff?', back: 'delay=1\nwhile ! kommando; do\n  sleep $delay\n  ((delay*=2))\ndone', category: 'Avancerat', difficulty: 'VG' }
]

// =============================================================================
// TASK 11: SKRIPTPARAMETRAR (30 flashcards)
// =============================================================================

const TASK_11_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't11-1', front: 'Vad innehåller $0?', back: 'Skriptets namn eller sökväg.\n./script.sh → $0 = "./script.sh"', category: 'Positionella', difficulty: 'G' },
    { id: 't11-2', front: 'Vad innehåller $1, $2, $3...?', back: 'Positionella parametrar.\n./script.sh a b c\n$1=a, $2=b, $3=c', category: 'Positionella', difficulty: 'G' },
    { id: 't11-3', front: 'Vad innehåller $#?', back: 'Antalet argument som skickats till skriptet.\n./script.sh a b c → $# = 3', category: 'Specialvariabler', difficulty: 'G' },
    { id: 't11-4', front: 'Vad innehåller $@?', back: 'ALLA argument som separata ord.\n"$@" bevarar citattecken runt argument.', category: 'Specialvariabler', difficulty: 'G' },
    { id: 't11-5', front: 'Vad innehåller $*?', back: 'ALLA argument som EN sträng.\nMed "$*" sammanfogas med IFS.', category: 'Specialvariabler', difficulty: 'G' },
    { id: 't11-6', front: 'Vad gör kommandot shift?', back: 'Flyttar parametrarna ett steg:\n$2→$1, $3→$2 osv.\n$1 försvinner.', category: 'shift', difficulty: 'G' },
    { id: 't11-7', front: 'Vad innehåller $?', back: 'Exit-koden från senaste kommando.\n0 = lyckades, annat = fel', category: 'Specialvariabler', difficulty: 'G' },
    { id: 't11-8', front: 'Vad innehåller $$?', back: 'Skriptets process-ID (PID).\nAnvändbart för temp-filer.', category: 'Specialvariabler', difficulty: 'G' },
    { id: 't11-9', front: 'Hur kontrollerar du om argument saknas?', back: 'if [ $# -eq 0 ]; then\n  echo "Inga argument!"\n  exit 1\nfi', category: 'Validering', difficulty: 'G' },
    { id: 't11-10', front: 'Vad innehåller $!?', back: 'PID för senaste bakgrundsprocess.\nkommando &\necho $!', category: 'Specialvariabler', difficulty: 'G' },
    // Medium (12)
    { id: 't11-11', front: 'Skillnad mellan "$@" och "$*"?', back: '"$@": varje arg separat → "a" "b c" "d"\n"$*": en sträng → "a b c d"', category: 'Specialvariabler', difficulty: 'G' },
    { id: 't11-12', front: 'Hur shiftar du flera steg?', back: 'shift N\nshift 2 tar bort $1 och $2.', category: 'shift', difficulty: 'G' },
    { id: 't11-13', front: 'Hur loopar du genom alla argument?', back: 'for arg in "$@"; do\n  echo "$arg"\ndone', category: 'Iteration', difficulty: 'G' },
    { id: 't11-14', front: 'Hur använder du shift i en loop?', back: 'while [ $# -gt 0 ]; do\n  echo "$1"\n  shift\ndone', category: 'shift', difficulty: 'G' },
    { id: 't11-15', front: 'Hur sätter du default för parameter?', back: '${1:-default}\nAnvänder "default" om $1 saknas/tom.', category: 'Default', difficulty: 'G' },
    { id: 't11-16', front: 'Hur kräver du en parameter?', back: '${1:?Fel: argument krävs}\nAvslutar skriptet om $1 saknas.', category: 'Validering', difficulty: 'G' },
    { id: 't11-17', front: 'Vad är getopts för något?', back: 'Inbyggt kommando för att parsa flaggor.\ngetopts "ab:" opt\n-a, -b arg', category: 'getopts', difficulty: 'G' },
    { id: 't11-18', front: 'Grundläggande getopts-loop?', back: 'while getopts "hf:" opt; do\n  case $opt in\n    h) usage;;\n    f) file=$OPTARG;;\n  esac\ndone', category: 'getopts', difficulty: 'G' },
    { id: 't11-19', front: 'Vad betyder : efter bokstav i getopts?', back: 'Flaggan kräver argument.\n"f:" = -f kräver värde\n"f" = bara flagga', category: 'getopts', difficulty: 'G' },
    { id: 't11-20', front: 'Vad innehåller OPTARG?', back: 'Argumentet till senaste flaggan.\n-f fil.txt → OPTARG="fil.txt"', category: 'getopts', difficulty: 'G' },
    { id: 't11-21', front: 'Vad innehåller OPTIND?', back: 'Index för nästa argument att processa.\nAnvänd shift $((OPTIND-1)) efter getopts.', category: 'getopts', difficulty: 'G' },
    { id: 't11-22', front: 'Hur hanterar du okänd flagga i getopts?', back: '\\?) echo "Okänd: $OPTARG";;\n: (kolon) hanterar saknat argument.', category: 'getopts', difficulty: 'G' },
    // Hard (8)
    { id: 't11-23', front: 'Hur parsar du långa flaggor (--help)?', back: 'case $1 in\n  --help) usage;;\n  --file=*) file="${1#*=}";;\nesac\neller: getopt (extern)', category: 'Långa flaggor', difficulty: 'VG' },
    { id: 't11-24', front: 'Skillnad getopts vs getopt?', back: 'getopts: inbyggd, korta flaggor\ngetopt: extern, stödjer långa flaggor', category: 'Parsning', difficulty: 'VG' },
    { id: 't11-25', front: 'Hur skickar du alla återstående args till kommando?', back: 'shift $((OPTIND-1))\nkommando "$@"', category: 'Avancerat', difficulty: 'VG' },
    { id: 't11-26', front: 'Vad gör set -- "nya" "args"?', back: 'Ersätter $1, $2... med nya värden.\nset -- "a" "b" → $1=a, $2=b', category: 'set', difficulty: 'VG' },
    { id: 't11-27', front: 'Hur validerar du att argument är fil?', back: '[ -f "$1" ] || { echo "Inte fil"; exit 1; }', category: 'Validering', difficulty: 'VG' },
    { id: 't11-28', front: 'Hur gör du en usage-funktion?', back: 'usage() {\n  echo "Usage: $0 [-h] [-f fil]"\n  exit 1\n}', category: 'Best Practice', difficulty: 'VG' },
    { id: 't11-29', front: 'Hur sparar du args innan shift?', back: 'args=("$@")\nshift\n# args har originalen', category: 'Avancerat', difficulty: 'VG' },
    { id: 't11-30', front: 'Hur hanterar du -- (end of options)?', back: 'Efter -- är allt argument, inte flaggor.\n./script.sh -- -fil.txt\n$1 = "-fil.txt"', category: 'Konventioner', difficulty: 'VG' }
]

// =============================================================================
// TASK 12: FUNKTIONER (30 flashcards)
// =============================================================================

const TASK_12_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't12-1', front: 'Grundläggande funktionssyntax i bash?', back: 'function_name() {\n  kommandon\n}\neller: function name { }', category: 'Syntax', difficulty: 'G' },
    { id: 't12-2', front: 'Hur anropar du en funktion?', back: 'Bara funktionsnamnet:\nminFunktion\n(inga parenteser vid anrop)', category: 'Anrop', difficulty: 'G' },
    { id: 't12-3', front: 'Hur skickar du argument till funktion?', back: 'minFunktion arg1 arg2\nInuti: $1=arg1, $2=arg2', category: 'Argument', difficulty: 'G' },
    { id: 't12-4', front: 'Hur returnerar funktion värde?', back: 'return N\nSätter exit-kod (0-255).\nSenare: echo $?', category: 'Return', difficulty: 'G' },
    { id: 't12-5', front: 'Hur returnerar funktion text?', back: 'Funktionen echo:ar, anroparen fångar:\nresult=$(minFunktion)', category: 'Output', difficulty: 'G' },
    { id: 't12-6', front: 'Var måste funktion definieras?', back: 'INNAN första anropet.\nBash läser uppifrån-ner.', category: 'Ordning', difficulty: 'G' },
    { id: 't12-7', front: 'Vad händer med $1 inuti funktion?', back: '$1 är funktionens första argument.\nSkriptets $1 är dolt temporärt.', category: 'Argument', difficulty: 'G' },
    { id: 't12-8', front: 'Hur kollar du funktionens exit-status?', back: 'minFunktion\nif [ $? -eq 0 ]; then\n  echo "OK"\nfi', category: 'Return', difficulty: 'G' },
    { id: 't12-9', front: 'Kan funktioner vara rekursiva?', back: 'Ja! Funktion kan anropa sig själv.\n(Varning: ingen tail-call optimization)', category: 'Rekursion', difficulty: 'G' },
    { id: 't12-10', front: 'Vad är default return-värde?', back: 'Exit-kod från sista kommandot i funktionen.', category: 'Return', difficulty: 'G' },
    // Medium (12)
    { id: 't12-11', front: 'Vad gör local i funktion?', back: 'Skapar lokal variabel:\nlocal var="värde"\nSynlig bara i funktionen.', category: 'Scope', difficulty: 'G' },
    { id: 't12-12', front: 'Vad händer utan local?', back: 'Variabler är GLOBALA!\nFunktionen ändrar/skapar globala variabler.', category: 'Scope', difficulty: 'G' },
    { id: 't12-13', front: 'Hur deklarerar du flera lokala variabler?', back: 'local var1 var2 var3\nlocal a=1 b=2 c=3', category: 'Scope', difficulty: 'G' },
    { id: 't12-14', front: 'Hur använder du funktion i if?', back: 'if minFunktion; then\n  echo "Return 0"\nfi', category: 'Villkor', difficulty: 'G' },
    { id: 't12-15', front: 'Hur exporterar du funktion till subshell?', back: 'export -f funktionsnamn\nNu tillgänglig i subprocesser.', category: 'Export', difficulty: 'G' },
    { id: 't12-16', front: 'Hur listar du alla definierade funktioner?', back: 'declare -F\neller: typeset -F', category: 'Debug', difficulty: 'G' },
    { id: 't12-17', front: 'Hur visar du funktionsdefinition?', back: 'declare -f funktionsnamn\nVisar hela koden.', category: 'Debug', difficulty: 'G' },
    { id: 't12-18', front: 'Hur tar du bort en funktion?', back: 'unset -f funktionsnamn', category: 'Hantering', difficulty: 'G' },
    { id: 't12-19', front: 'Hur skapar du funktion med array-argument?', back: 'func() {\n  local arr=("$@")\n  echo "${arr[0]}"\n}', category: 'Arrays', difficulty: 'G' },
    { id: 't12-20', front: 'Hur returnerar du array från funktion?', back: 'Svårt! Vanligaste:\necho "${arr[@]}"\nresult=($(func))', category: 'Arrays', difficulty: 'G' },
    { id: 't12-21', front: 'Vad är namerefs (bash 4.3+)?', back: 'local -n ref=$1\nref pekar på variabel med namn $1.', category: 'Avancerat', difficulty: 'G' },
    { id: 't12-22', front: 'Hur dokumenterar du funktion?', back: '# Kort beskrivning\n# Args: $1 = filnamn\n# Returns: 0 om OK\nfunc() { }', category: 'Best Practice', difficulty: 'G' },
    // Hard (8)
    { id: 't12-23', front: 'Hur skapar du privata hjälpfunktioner?', back: 'Konvention: prefix med _\n_private_helper() { }', category: 'Konventioner', difficulty: 'VG' },
    { id: 't12-24', front: 'Skillnad function name vs name()?', back: 'name() är POSIX-kompatibel.\nfunction name är bash-specifik.\nname() föredras.', category: 'Syntax', difficulty: 'VG' },
    { id: 't12-25', front: 'Hur gör du error handling i funktion?', back: 'func() {\n  kommando || { echo "Fel" >&2; return 1; }\n}', category: 'Felhantering', difficulty: 'VG' },
    { id: 't12-26', front: 'Hur skapar du funktion som tar callback?', back: 'foreach() {\n  for item in "${@:2}"; do\n    $1 "$item"\n  done\n}', category: 'Avancerat', difficulty: 'VG' },
    { id: 't12-27', front: 'Vad är ${@:2} syntax?', back: 'Array slice: alla args från position 2.\n${@:2:3} = 3 args från pos 2.', category: 'Slicing', difficulty: 'VG' },
    { id: 't12-28', front: 'Hur skapar du funktion med named params?', back: 'func() {\n  local "${@}"\n  echo "$name $age"\n}\nfunc name=Kalle age=25', category: 'Avancerat', difficulty: 'VG' },
    { id: 't12-29', front: 'Hur gör du lazy evaluation?', back: 'cached="" \nget_data() {\n  [ -z "$cached" ] && cached=$(cmd)\n  echo "$cached"\n}', category: 'Mönster', difficulty: 'VG' },
    { id: 't12-30', front: 'Hur sourcar du funktionsbibliotek?', back: 'source lib.sh\neller: . lib.sh\nFunktioner blir tillgängliga.', category: 'Bibliotek', difficulty: 'VG' }
]

// =============================================================================
// TASK 13: SIGNALER (30 flashcards)
// =============================================================================

const TASK_13_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't13-1', front: 'Vad är en signal i Linux?', back: 'Asynkron notifiering till process.\nAnvänds för kommunikation och kontroll.', category: 'Grunder', difficulty: 'G' },
    { id: 't13-2', front: 'Vad gör Ctrl+C?', back: 'Skickar SIGINT (signal 2).\nAvbryter normalt körande process.', category: 'Vanliga', difficulty: 'G' },
    { id: 't13-3', front: 'Vad gör Ctrl+Z?', back: 'Skickar SIGTSTP (signal 20).\nPausar processen, lägg i bakgrund.', category: 'Vanliga', difficulty: 'G' },
    { id: 't13-4', front: 'Vad är SIGTERM?', back: 'Signal 15 - Terminate.\nStandardsignal för kill-kommando.\nProcessen kan fånga den.', category: 'Signaler', difficulty: 'G' },
    { id: 't13-5', front: 'Vad är SIGKILL?', back: 'Signal 9 - Kill.\nKAN EJ fångas eller ignoreras!\nOmedelbar avslutning.', category: 'Signaler', difficulty: 'G' },
    { id: 't13-6', front: 'Hur dödar du process med PID 1234?', back: 'kill 1234\nSkickar SIGTERM (default).', category: 'kill', difficulty: 'G' },
    { id: 't13-7', front: 'Hur tvingar du processdöd?', back: 'kill -9 PID\neller: kill -SIGKILL PID', category: 'kill', difficulty: 'G' },
    { id: 't13-8', front: 'Vad gör trap i bash?', back: 'Fångar signaler och kör kommando.\ntrap "kommando" SIGNAL', category: 'trap', difficulty: 'G' },
    { id: 't13-9', front: 'Hur listar du alla signaler?', back: 'kill -l\nVisar alla signalnamn och nummer.', category: 'Lista', difficulty: 'G' },
    { id: 't13-10', front: 'Vad är SIGHUP?', back: 'Signal 1 - Hangup.\nSkickas när terminal stängs.\nKan användas för reload.', category: 'Signaler', difficulty: 'G' },
    // Medium (12)
    { id: 't13-11', front: 'Grundläggande trap-syntax?', back: 'trap "echo Avbruten" SIGINT\ntrap cleanup EXIT', category: 'trap', difficulty: 'G' },
    { id: 't13-12', front: 'Hur städar du vid skriptavslut?', back: 'trap cleanup EXIT\n\ncleanup() {\n  rm -f /tmp/tempfil\n}', category: 'trap', difficulty: 'G' },
    { id: 't13-13', front: 'Hur ignorerar du en signal?', back: 'trap "" SIGINT\nTom sträng = ignorera signalen.', category: 'trap', difficulty: 'G' },
    { id: 't13-14', front: 'Hur återställer du trap till default?', back: 'trap - SIGINT\neller trap SIGINT\nBindestrecket återställer.', category: 'trap', difficulty: 'G' },
    { id: 't13-15', front: 'Vad är EXIT i trap?', back: 'Pseudo-signal som triggas vid\nskriptavslut (oavsett anledning).', category: 'trap', difficulty: 'G' },
    { id: 't13-16', front: 'Vad är ERR i trap?', back: 'Triggas vid fel (non-zero exit).\ntrap "echo Fel" ERR', category: 'trap', difficulty: 'G' },
    { id: 't13-17', front: 'Hur dödar du alla processer med namn?', back: 'pkill processnamn\neller: killall processnamn', category: 'kill', difficulty: 'G' },
    { id: 't13-18', front: 'Hur skickar du signal till processgrupp?', back: 'kill -SIGNAL -PGID\nNegativt PID = processgrupp.', category: 'kill', difficulty: 'G' },
    { id: 't13-19', front: 'Vad är SIGSTOP?', back: 'Signal 19 - Stop.\nPausar process, kan EJ fångas.\nOlika från SIGTSTP.', category: 'Signaler', difficulty: 'G' },
    { id: 't13-20', front: 'Hur fortsätter du stoppad process?', back: 'kill -CONT PID\neller: fg (för bakgrundsjobb)', category: 'Signaler', difficulty: 'G' },
    { id: 't13-21', front: 'Vad är SIGCHLD?', back: 'Skickas till parent när child\navslutas eller stoppas.', category: 'Signaler', difficulty: 'G' },
    { id: 't13-22', front: 'Hur hanterar du flera signaler i trap?', back: 'trap handler SIGINT SIGTERM\nSamma handler för båda.', category: 'trap', difficulty: 'G' },
    // Hard (8)
    { id: 't13-23', front: 'Skillnad SIGTERM vs SIGKILL?', back: 'SIGTERM: kan fångas, process kan städa\nSIGKILL: omedelbar död, kan ej fångas', category: 'Jämförelse', difficulty: 'VG' },
    { id: 't13-24', front: 'Vad är DEBUG trap?', back: 'Körs FÖRE varje kommando.\ntrap "echo CMD: $BASH_COMMAND" DEBUG', category: 'trap', difficulty: 'VG' },
    { id: 't13-25', front: 'Vad är RETURN trap?', back: 'Körs när funktion eller sourced\nskript returnerar.', category: 'trap', difficulty: 'VG' },
    { id: 't13-26', front: 'Hur gör du trap-safe temp-filer?', back: 'tmpfile=$(mktemp)\ntrap "rm -f $tmpfile" EXIT', category: 'Best Practice', difficulty: 'VG' },
    { id: 't13-27', front: 'Vad gör set -e med trap ERR?', back: 'set -e: avbryt vid fel\ntrap ERR: kör handler vid fel\nKombinerat: städa och avbryt.', category: 'Kombinerat', difficulty: 'VG' },
    { id: 't13-28', front: 'Hur propagerar du signal i trap?', back: 'trap "cleanup; exit 130" SIGINT\n130 = 128 + signalnummer (2)', category: 'Best Practice', difficulty: 'VG' },
    { id: 't13-29', front: 'Vilka signaler kan INTE fångas?', back: 'SIGKILL (9) och SIGSTOP (19)\nHardkodade i kernel.', category: 'Begränsningar', difficulty: 'VG' },
    { id: 't13-30', front: 'Hur testar du trap i subshell?', back: 'Traps ärvs EJ till subshells!\n(cmd) får inte parent trap.', category: 'Avancerat', difficulty: 'VG' }
]

// =============================================================================
// TASK 14: ANVÄNDARHANTERING (30 flashcards)
// =============================================================================

const TASK_14_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't14-1', front: 'Vilken fil innehåller användarinfo?', back: '/etc/passwd\nUsername:x:UID:GID:GECOS:Home:Shell', category: 'Filer', difficulty: 'G' },
    { id: 't14-2', front: 'Vilken fil innehåller lösenords-hashar?', back: '/etc/shadow\nEndast läsbar av root.', category: 'Filer', difficulty: 'G' },
    { id: 't14-3', front: 'Vilken fil innehåller gruppinfo?', back: '/etc/group\nGruppnamn:x:GID:medlemmar', category: 'Filer', difficulty: 'G' },
    { id: 't14-4', front: 'Hur skapar du en användare?', back: 'sudo useradd username\neller: sudo adduser username', category: 'useradd', difficulty: 'G' },
    { id: 't14-5', front: 'Hur tar du bort en användare?', back: 'sudo userdel username\n-r tar även bort hemkatalog.', category: 'userdel', difficulty: 'G' },
    { id: 't14-6', front: 'Hur ändrar du lösenord?', back: 'passwd\npasswd username (som root)', category: 'passwd', difficulty: 'G' },
    { id: 't14-7', front: 'Hur skapar du en grupp?', back: 'sudo groupadd gruppnamn', category: 'groupadd', difficulty: 'G' },
    { id: 't14-8', front: 'Hur lägger du användare i grupp?', back: 'sudo usermod -aG grupp user\n-a = append, -G = supplementary group', category: 'usermod', difficulty: 'G' },
    { id: 't14-9', front: 'Vad är root-användaren?', back: 'Superuser med UID 0.\nFull kontroll över systemet.', category: 'Grunder', difficulty: 'G' },
    { id: 't14-10', front: 'Hur visar du aktuell användare?', back: 'whoami\neller: id -un', category: 'Kommandon', difficulty: 'G' },
    // Medium (12)
    { id: 't14-11', front: 'Hur skapar du användare med hemkatalog?', back: 'useradd -m username\n-m skapar /home/username', category: 'useradd', difficulty: 'G' },
    { id: 't14-12', front: 'Hur sätter du default shell?', back: 'useradd -s /bin/bash username\neller: chsh -s /bin/bash', category: 'Shell', difficulty: 'G' },
    { id: 't14-13', front: 'Hur låser du en användare?', back: 'sudo passwd -l username\neller: sudo usermod -L username', category: 'Säkerhet', difficulty: 'G' },
    { id: 't14-14', front: 'Hur låser du upp användare?', back: 'sudo passwd -u username\neller: sudo usermod -U username', category: 'Säkerhet', difficulty: 'G' },
    { id: 't14-15', front: 'Hur visar du grupptillhörigheter?', back: 'groups username\neller: id username', category: 'Kommandon', difficulty: 'G' },
    { id: 't14-16', front: 'Skillnad primär vs sekundär grupp?', back: 'Primär: GID i /etc/passwd\nSekundär: Listas i /etc/group', category: 'Grupper', difficulty: 'G' },
    { id: 't14-17', front: 'Hur ändrar du primär grupp?', back: 'usermod -g gruppnamn user', category: 'usermod', difficulty: 'G' },
    { id: 't14-18', front: 'Vad är UID och GID?', back: 'UID: User ID (numeriskt)\nGID: Group ID (numeriskt)\nroot har 0/0', category: 'Grunder', difficulty: 'G' },
    { id: 't14-19', front: 'Hur sätter du lösenordsutgång?', back: 'sudo chage -M 90 user\n-M = max days', category: 'chage', difficulty: 'G' },
    { id: 't14-20', front: 'Hur visar du lösenordspolicy?', back: 'sudo chage -l username\nVisar alla lösenordsinställningar.', category: 'chage', difficulty: 'G' },
    { id: 't14-21', front: 'Vad är GECOS-fältet?', back: 'Kommentarfält i /etc/passwd.\nOfta fullständigt namn, kontorsinfo.', category: 'passwd', difficulty: 'G' },
    { id: 't14-22', front: 'Hur ändrar du GECOS?', back: 'sudo chfn username\neller: usermod -c "Full Name" user', category: 'Kommandon', difficulty: 'G' },
    // Hard (8)
    { id: 't14-23', front: 'Hur skapar du systemanvändare?', back: 'useradd -r -s /sbin/nologin user\n-r = system user (lågt UID)', category: 'System', difficulty: 'VG' },
    { id: 't14-24', front: 'Vad är /etc/login.defs?', back: 'Systemomfattande inställningar för\nuseradd, passwd etc.\nUID/GID-ranges, lösenordspolicyer.', category: 'Konfiguration', difficulty: 'VG' },
    { id: 't14-25', front: 'Vad är /etc/skel?', back: 'Skeleton directory.\nFiler kopieras till nya hemkataloger.\n.bashrc, .profile etc.', category: 'Konfiguration', difficulty: 'VG' },
    { id: 't14-26', front: 'Hur skapar du användare med specifikt UID?', back: 'useradd -u 1500 username', category: 'useradd', difficulty: 'VG' },
    { id: 't14-27', front: 'Vad gör pwck och grpck?', back: 'Verifierar integritet:\npwck - /etc/passwd & shadow\ngrpck - /etc/group', category: 'Verktyg', difficulty: 'VG' },
    { id: 't14-28', front: 'Hur tvingar du lösenordsbyte vid login?', back: 'sudo chage -d 0 username\neller: passwd -e username', category: 'chage', difficulty: 'VG' },
    { id: 't14-29', front: 'Hur tar du bort användare från grupp?', back: 'gpasswd -d user grupp\neller: usermod utan gruppen i -G', category: 'Kommandon', difficulty: 'VG' },
    { id: 't14-30', front: 'Vad är nologin shell?', back: '/sbin/nologin eller /bin/false\nFörhindrar interaktiv login.\nFör systemanvändare.', category: 'Säkerhet', difficulty: 'VG' }
]

// =============================================================================
// TASK 15: RÄTTIGHETER & ACL (30 flashcards)
// =============================================================================

const TASK_15_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't15-1', front: 'Vad betyder r, w, x för filer?', back: 'r = read (läsa innehåll)\nw = write (ändra innehåll)\nx = execute (köra som program)', category: 'Grunder', difficulty: 'G' },
    { id: 't15-2', front: 'Vad betyder r, w, x för kataloger?', back: 'r = lista innehåll (ls)\nw = skapa/ta bort filer\nx = cd in i katalogen', category: 'Grunder', difficulty: 'G' },
    { id: 't15-3', front: 'Vad visar ls -l output: -rwxr-xr--?', back: 'Ägare: rwx (7)\nGrupp: r-x (5)\nAndra: r-- (4)\nOktalt: 754', category: 'ls', difficulty: 'G' },
    { id: 't15-4', front: 'Hur ändrar du rättigheter med chmod?', back: 'chmod 755 fil\neller chmod u+x fil\n(oktalt eller symboliskt)', category: 'chmod', difficulty: 'G' },
    { id: 't15-5', front: 'Vad är oktalt värde för rwx?', back: 'r=4, w=2, x=1\nrwx = 4+2+1 = 7', category: 'Oktalt', difficulty: 'G' },
    { id: 't15-6', front: 'Hur ändrar du ägare på fil?', back: 'chown user fil\nchown user:group fil', category: 'chown', difficulty: 'G' },
    { id: 't15-7', front: 'Hur ändrar du grupp på fil?', back: 'chgrp group fil\neller: chown :group fil', category: 'chgrp', difficulty: 'G' },
    { id: 't15-8', front: 'Vad är u, g, o i chmod?', back: 'u = user (ägare)\ng = group\no = others\na = all', category: 'chmod', difficulty: 'G' },
    { id: 't15-9', front: 'Hur gör du fil exekverbar?', back: 'chmod +x fil\neller: chmod u+x fil', category: 'chmod', difficulty: 'G' },
    { id: 't15-10', front: 'Vad är 644 i rättigheter?', back: 'rw-r--r--\nÄgare: läs/skriv\nGrupp/Andra: bara läs', category: 'Oktalt', difficulty: 'G' },
    // Medium (12)
    { id: 't15-11', front: 'Vad är 755 i rättigheter?', back: 'rwxr-xr-x\nÄgare: full\nGrupp/Andra: läs/exekvera', category: 'Oktalt', difficulty: 'G' },
    { id: 't15-12', front: 'Hur sätter du rättigheter rekursivt?', back: 'chmod -R 755 katalog\nchown -R user:group katalog', category: 'Rekursivt', difficulty: 'G' },
    { id: 't15-13', front: 'Vad är SUID-bit?', back: 'Set User ID\nKör fil som filens ägare.\nchmod u+s fil (4xxx)', category: 'Special', difficulty: 'G' },
    { id: 't15-14', front: 'Vad är SGID-bit?', back: 'Set Group ID\nFil: kör som filens grupp\nKatalog: ärv grupp', category: 'Special', difficulty: 'G' },
    { id: 't15-15', front: 'Vad är Sticky bit?', back: 'På katalog: endast ägare kan ta bort sina filer.\nAnvänds på /tmp.\nchmod +t (1xxx)', category: 'Special', difficulty: 'G' },
    { id: 't15-16', front: 'Hur ser SUID ut i ls?', back: '-rwsr-xr-x\ns istället för x på user.\nS om ingen x.', category: 'Special', difficulty: 'G' },
    { id: 't15-17', front: 'Vad är umask?', back: 'Default rättighetsmask.\nNya filer: 666-umask\nNya kataloger: 777-umask', category: 'umask', difficulty: 'G' },
    { id: 't15-18', front: 'Vad ger umask 022?', back: 'Filer: 644 (666-022)\nKataloger: 755 (777-022)', category: 'umask', difficulty: 'G' },
    { id: 't15-19', front: 'Hur visar du ACL för fil?', back: 'getfacl fil', category: 'ACL', difficulty: 'G' },
    { id: 't15-20', front: 'Hur sätter du ACL för användare?', back: 'setfacl -m u:user:rwx fil\n-m = modify', category: 'ACL', difficulty: 'G' },
    { id: 't15-21', front: 'Vad är ACL mask?', back: 'Maximal effektiv rättighet.\nBegränsar alla named entries.', category: 'ACL', difficulty: 'G' },
    { id: 't15-22', front: 'Hur tar du bort ACL?', back: 'setfacl -b fil (ta bort alla)\nsetfacl -x u:user fil', category: 'ACL', difficulty: 'G' },
    // Hard (8)
    { id: 't15-23', front: 'Hur sätter du default ACL på katalog?', back: 'setfacl -d -m u:user:rwx katalog\n-d = default för nya filer', category: 'ACL', difficulty: 'VG' },
    { id: 't15-24', front: 'Vad indikerar + i ls -l?', back: 'Filen har ACL.\n-rw-r--r--+ file', category: 'ACL', difficulty: 'VG' },
    { id: 't15-25', front: 'Hur kopierar du ACL mellan filer?', back: 'getfacl fil1 | setfacl --set-file=- fil2', category: 'ACL', difficulty: 'VG' },
    { id: 't15-26', front: 'Vad är capability i Linux?', back: 'Finfördelad root-behörighet.\nEx: CAP_NET_BIND_SERVICE\ngetcap/setcap', category: 'Capabilities', difficulty: 'VG' },
    { id: 't15-27', front: 'Hur hittar du SUID-filer?', back: 'find / -perm -4000\neller: find / -perm /u=s', category: 'Sökning', difficulty: 'VG' },
    { id: 't15-28', front: 'Hur beräknas effektiv ACL?', back: 'permission AND mask\nMask begränsar named entries.', category: 'ACL', difficulty: 'VG' },
    { id: 't15-29', front: 'Vad gör chmod u=rwx,g=rx,o= fil?', back: 'Exakt sättning:\nu: rwx, g: rx, o: ingenting\n= 750', category: 'chmod', difficulty: 'VG' },
    { id: 't15-30', front: 'Skillnad mellan --set och -m i setfacl?', back: '--set: ersätt hela ACL\n-m: modifiera specifik entry', category: 'ACL', difficulty: 'VG' }
]

// =============================================================================
// TASK 16: SSH (30 flashcards)
// =============================================================================

const TASK_16_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't16-1', front: 'Vad är SSH?', back: 'Secure Shell\nKrypterad fjärranslutning.\nPort 22 default.', category: 'Grunder', difficulty: 'G' },
    { id: 't16-2', front: 'Hur ansluter du till server?', back: 'ssh user@host\nssh user@192.168.1.10', category: 'Grundläggande', difficulty: 'G' },
    { id: 't16-3', front: 'Var lagras SSH-nycklar?', back: '~/.ssh/\nid_rsa (privat)\nid_rsa.pub (publik)', category: 'Nycklar', difficulty: 'G' },
    { id: 't16-4', front: 'Hur genererar du SSH-nyckelpar?', back: 'ssh-keygen\neller: ssh-keygen -t ed25519', category: 'Nycklar', difficulty: 'G' },
    { id: 't16-5', front: 'Var läggs auktoriserade nycklar?', back: '~/.ssh/authorized_keys\nPå servern.', category: 'Nycklar', difficulty: 'G' },
    { id: 't16-6', front: 'Hur kopierar du nyckel till server?', back: 'ssh-copy-id user@host\nLägger publik nyckel i authorized_keys.', category: 'Nycklar', difficulty: 'G' },
    { id: 't16-7', front: 'Vilken fil konfigurerar SSH-server?', back: '/etc/ssh/sshd_config', category: 'Konfiguration', difficulty: 'G' },
    { id: 't16-8', front: 'Vilken fil konfigurerar SSH-klient?', back: '~/.ssh/config\neller /etc/ssh/ssh_config', category: 'Konfiguration', difficulty: 'G' },
    { id: 't16-9', front: 'Hur kopierar du fil med SSH?', back: 'scp fil user@host:/sökväg\nscp user@host:fil lokal', category: 'scp', difficulty: 'G' },
    { id: 't16-10', front: 'Hur startar du om SSH-tjänsten?', back: 'sudo systemctl restart sshd\neller: service ssh restart', category: 'Tjänst', difficulty: 'G' },
    // Medium (12)
    { id: 't16-11', front: 'Hur ansluter du på annan port?', back: 'ssh -p 2222 user@host', category: 'Portar', difficulty: 'G' },
    { id: 't16-12', front: 'Hur skapar du SSH tunnel?', back: 'ssh -L local:host:remote user@server\nLocal port forwarding.', category: 'Tunnlar', difficulty: 'G' },
    { id: 't16-13', front: 'Hur inaktiverar du lösenordsinloggning?', back: 'I sshd_config:\nPasswordAuthentication no', category: 'Säkerhet', difficulty: 'G' },
    { id: 't16-14', front: 'Hur inaktiverar du root-login?', back: 'PermitRootLogin no\ni /etc/ssh/sshd_config', category: 'Säkerhet', difficulty: 'G' },
    { id: 't16-15', front: 'Vad är SSH agent?', back: 'Cachar nyckellösenord.\nssh-agent\nssh-add', category: 'Agent', difficulty: 'G' },
    { id: 't16-16', front: 'Hur lägger du till nyckel i agent?', back: 'ssh-add ~/.ssh/id_rsa\neller bara: ssh-add', category: 'Agent', difficulty: 'G' },
    { id: 't16-17', front: 'Vilka rättigheter krävs på .ssh/?', back: '~/.ssh: 700\n~/.ssh/id_rsa: 600\nauthorized_keys: 600', category: 'Säkerhet', difficulty: 'G' },
    { id: 't16-18', front: 'Vad gör -i flaggan?', back: 'Anger identity file (nyckel).\nssh -i ~/.ssh/custom_key user@host', category: 'Flaggor', difficulty: 'G' },
    { id: 't16-19', front: 'Hur kör du kommando på remote?', back: 'ssh user@host "kommando"\nssh user@host ls -la', category: 'Kommandon', difficulty: 'G' },
    { id: 't16-20', front: 'Vad är rsync över SSH?', back: 'rsync -avz -e ssh src user@host:dest\nEffektiv filsynk.', category: 'rsync', difficulty: 'G' },
    { id: 't16-21', front: 'Hur konfigurerar du host-alias?', back: 'I ~/.ssh/config:\nHost alias\n  HostName real.host\n  User myuser', category: 'Config', difficulty: 'G' },
    { id: 't16-22', front: 'Vad är known_hosts?', back: '~/.ssh/known_hosts\nSparar serverns fingerprint.\nSkyddar mot MITM.', category: 'Säkerhet', difficulty: 'G' },
    // Hard (8)
    { id: 't16-23', front: 'Hur sätter du upp reverse tunnel?', back: 'ssh -R remote:host:local user@server\nRemote port forwarding.', category: 'Tunnlar', difficulty: 'VG' },
    { id: 't16-24', front: 'Vad är dynamic port forwarding?', back: 'ssh -D 1080 user@host\nSOCKS proxy.', category: 'Tunnlar', difficulty: 'VG' },
    { id: 't16-25', front: 'Hur gör du SSH jump host?', back: 'ssh -J jumphost user@destination\neller ProxyJump i config', category: 'Avancerat', difficulty: 'VG' },
    { id: 't16-26', front: 'Vad är ed25519 vs RSA?', back: 'ed25519: modernare, kortare, snabbare\nRSA: äldre, bredare stöd\nRekommendation: ed25519', category: 'Nycklar', difficulty: 'VG' },
    { id: 't16-27', front: 'Hur begränsar du vilka användare kan SSH?', back: 'AllowUsers user1 user2\neller AllowGroups sshusers\ni sshd_config', category: 'Säkerhet', difficulty: 'VG' },
    { id: 't16-28', front: 'Hur sätter du upp SSH certificate auth?', back: 'ssh-keygen -s CA_key -I id user_key.pub\nSkalar bättre än authorized_keys.', category: 'Avancerat', difficulty: 'VG' },
    { id: 't16-29', front: 'Vad gör StrictHostKeyChecking?', back: 'yes: avvisa okända hosts\nno: acceptera automatiskt\nask: fråga (default)', category: 'Säkerhet', difficulty: 'VG' },
    { id: 't16-30', front: 'Hur debuggar du SSH-anslutning?', back: 'ssh -v user@host\n-vv/-vvv för mer detalj.\nServer: journalctl -u sshd', category: 'Debug', difficulty: 'VG' }
]

// =============================================================================
// TASK 17: UFW FIREWALL (30 flashcards)
// =============================================================================

const TASK_17_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't17-1', front: 'Vad är UFW?', back: 'Uncomplicated Firewall\nEnkelt frontend för iptables.\nStandard i Ubuntu.', category: 'Grunder', difficulty: 'G' },
    { id: 't17-2', front: 'Hur aktiverar du UFW?', back: 'sudo ufw enable', category: 'Grundläggande', difficulty: 'G' },
    { id: 't17-3', front: 'Hur inaktiverar du UFW?', back: 'sudo ufw disable', category: 'Grundläggande', difficulty: 'G' },
    { id: 't17-4', front: 'Hur visar du UFW-status?', back: 'sudo ufw status\nsudo ufw status verbose', category: 'Status', difficulty: 'G' },
    { id: 't17-5', front: 'Hur tillåter du port 22 (SSH)?', back: 'sudo ufw allow 22\neller: sudo ufw allow ssh', category: 'Regler', difficulty: 'G' },
    { id: 't17-6', front: 'Hur blockerar du en port?', back: 'sudo ufw deny 80', category: 'Regler', difficulty: 'G' },
    { id: 't17-7', front: 'Hur tar du bort en regel?', back: 'sudo ufw delete allow 22\neller: sudo ufw delete 3 (radnummer)', category: 'Regler', difficulty: 'G' },
    { id: 't17-8', front: 'Vad är default policy?', back: 'Vad som händer med trafik som inte matchar regler.\nDefault: deny incoming, allow outgoing', category: 'Policy', difficulty: 'G' },
    { id: 't17-9', front: 'Hur sätter du default deny incoming?', back: 'sudo ufw default deny incoming', category: 'Policy', difficulty: 'G' },
    { id: 't17-10', front: 'Hur tillåter du HTTP och HTTPS?', back: 'sudo ufw allow http\nsudo ufw allow https\neller: 80, 443', category: 'Regler', difficulty: 'G' },
    // Medium (12)
    { id: 't17-11', front: 'Hur tillåter du specifik IP?', back: 'sudo ufw allow from 192.168.1.100', category: 'IP-regler', difficulty: 'G' },
    { id: 't17-12', front: 'Hur tillåter du subnät?', back: 'sudo ufw allow from 192.168.1.0/24', category: 'IP-regler', difficulty: 'G' },
    { id: 't17-13', front: 'Hur tillåter du IP till specifik port?', back: 'sudo ufw allow from 192.168.1.100 to any port 22', category: 'IP-regler', difficulty: 'G' },
    { id: 't17-14', front: 'Hur anger du protokoll (TCP/UDP)?', back: 'sudo ufw allow 53/udp\nsudo ufw allow 80/tcp', category: 'Protokoll', difficulty: 'G' },
    { id: 't17-15', front: 'Hur tillåter du portintervall?', back: 'sudo ufw allow 6000:6007/tcp', category: 'Regler', difficulty: 'G' },
    { id: 't17-16', front: 'Hur visar du numrerade regler?', back: 'sudo ufw status numbered\nBra för att radera specifika regler.', category: 'Status', difficulty: 'G' },
    { id: 't17-17', front: 'Hur infogar du regel på specifik position?', back: 'sudo ufw insert 1 deny from 1.2.3.4', category: 'Regler', difficulty: 'G' },
    { id: 't17-18', front: 'Vad är UFW application profiles?', back: 'Fördefinierade regler för appar.\nsudo ufw app list\nsudo ufw allow "OpenSSH"', category: 'Profiler', difficulty: 'G' },
    { id: 't17-19', front: 'Hur visar du info om app-profil?', back: 'sudo ufw app info "Nginx Full"', category: 'Profiler', difficulty: 'G' },
    { id: 't17-20', front: 'Hur aktiverar du loggning?', back: 'sudo ufw logging on\nsudo ufw logging medium', category: 'Loggning', difficulty: 'G' },
    { id: 't17-21', front: 'Var sparas UFW-loggar?', back: '/var/log/ufw.log', category: 'Loggning', difficulty: 'G' },
    { id: 't17-22', front: 'Hur återställer du UFW till default?', back: 'sudo ufw reset\nTar bort alla regler.', category: 'Reset', difficulty: 'G' },
    // Hard (8)
    { id: 't17-23', front: 'Hur tillåter du interface-specifik trafik?', back: 'sudo ufw allow in on eth0 to any port 80', category: 'Interface', difficulty: 'VG' },
    { id: 't17-24', front: 'Hur begränsar du anslutningar (rate limit)?', back: 'sudo ufw limit ssh\nBlockerar efter 6 anslutningar på 30 sek.', category: 'Säkerhet', difficulty: 'VG' },
    { id: 't17-25', front: 'Var finns UFW rules-filer?', back: '/etc/ufw/user.rules\n/etc/ufw/before.rules\n/etc/ufw/after.rules', category: 'Konfiguration', difficulty: 'VG' },
    { id: 't17-26', front: 'Hur lägger du till raw iptables-regel?', back: 'Redigera /etc/ufw/before.rules\neller after.rules', category: 'Avancerat', difficulty: 'VG' },
    { id: 't17-27', front: 'Hur aktiverar du IPv6 i UFW?', back: 'I /etc/default/ufw:\nIPV6=yes', category: 'IPv6', difficulty: 'VG' },
    { id: 't17-28', front: 'Hur blockerar du utgående trafik till IP?', back: 'sudo ufw deny out to 1.2.3.4', category: 'Utgående', difficulty: 'VG' },
    { id: 't17-29', front: 'Hur tillåter du routed/forward trafik?', back: 'I /etc/default/ufw:\nDEFAULT_FORWARD_POLICY="ACCEPT"', category: 'Routing', difficulty: 'VG' },
    { id: 't17-30', front: 'Hur debuggar du UFW-problem?', back: 'sudo ufw status verbose\ntail -f /var/log/ufw.log\niptables -L -n -v', category: 'Debug', difficulty: 'VG' }
]

// =============================================================================
// TASK 18: FIREWALLD (30 flashcards)
// =============================================================================

const TASK_18_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't18-1', front: 'Vad är firewalld?', back: 'Dynamisk firewall-daemon.\nStandard i RHEL/CentOS/Fedora.\nZon-baserad.', category: 'Grunder', difficulty: 'G' },
    { id: 't18-2', front: 'Hur startar du firewalld?', back: 'sudo systemctl start firewalld\nsudo systemctl enable firewalld', category: 'Tjänst', difficulty: 'G' },
    { id: 't18-3', front: 'Hur visar du firewalld-status?', back: 'sudo firewall-cmd --state\nsudo systemctl status firewalld', category: 'Status', difficulty: 'G' },
    { id: 't18-4', front: 'Vad är en zon i firewalld?', back: 'Fördefinierad säkerhetsnivå.\nEx: public, home, trusted, drop.\nInterface kopplas till zon.', category: 'Zoner', difficulty: 'G' },
    { id: 't18-5', front: 'Hur listar du alla zoner?', back: 'sudo firewall-cmd --get-zones', category: 'Zoner', difficulty: 'G' },
    { id: 't18-6', front: 'Hur visar du aktiv zon?', back: 'sudo firewall-cmd --get-active-zones', category: 'Zoner', difficulty: 'G' },
    { id: 't18-7', front: 'Hur listar du regler i default-zon?', back: 'sudo firewall-cmd --list-all', category: 'Regler', difficulty: 'G' },
    { id: 't18-8', front: 'Hur tillåter du en tjänst?', back: 'sudo firewall-cmd --add-service=ssh', category: 'Tjänster', difficulty: 'G' },
    { id: 't18-9', front: 'Hur tillåter du en port?', back: 'sudo firewall-cmd --add-port=80/tcp', category: 'Portar', difficulty: 'G' },
    { id: 't18-10', front: 'Vad gör --permanent flaggan?', back: 'Sparar regel permanent.\nUtan: gäller bara till reload/reboot.', category: 'Permanent', difficulty: 'G' },
    // Medium (12)
    { id: 't18-11', front: 'Hur gör du ändring permanent?', back: 'sudo firewall-cmd --permanent --add-service=http\nsudo firewall-cmd --reload', category: 'Permanent', difficulty: 'G' },
    { id: 't18-12', front: 'Hur laddar du om firewalld?', back: 'sudo firewall-cmd --reload', category: 'Reload', difficulty: 'G' },
    { id: 't18-13', front: 'Hur tar du bort tjänst?', back: 'sudo firewall-cmd --remove-service=http', category: 'Tjänster', difficulty: 'G' },
    { id: 't18-14', front: 'Hur listar du tillgängliga tjänster?', back: 'sudo firewall-cmd --get-services', category: 'Tjänster', difficulty: 'G' },
    { id: 't18-15', front: 'Hur visar du info om en tjänst?', back: 'sudo firewall-cmd --info-service=ssh', category: 'Tjänster', difficulty: 'G' },
    { id: 't18-16', front: 'Hur anger du specifik zon?', back: 'sudo firewall-cmd --zone=public --add-service=http', category: 'Zoner', difficulty: 'G' },
    { id: 't18-17', front: 'Hur ändrar du default-zon?', back: 'sudo firewall-cmd --set-default-zone=home', category: 'Zoner', difficulty: 'G' },
    { id: 't18-18', front: 'Hur flyttar du interface till zon?', back: 'sudo firewall-cmd --zone=trusted --change-interface=eth1', category: 'Interface', difficulty: 'G' },
    { id: 't18-19', front: 'Vad är rich rules?', back: 'Avancerade regler med fler villkor.\nKällor, destinationer, loggning etc.', category: 'Rich Rules', difficulty: 'G' },
    { id: 't18-20', front: 'Hur blockerar du specifik IP?', back: 'sudo firewall-cmd --add-rich-rule=\'rule family="ipv4" source address="1.2.3.4" reject\'', category: 'Rich Rules', difficulty: 'G' },
    { id: 't18-21', front: 'Vad är panic mode?', back: 'Blockerar ALL nätverkstrafik!\nfirewall-cmd --panic-on\nAnvänd för nödsituationer.', category: 'Säkerhet', difficulty: 'G' },
    { id: 't18-22', front: 'Hur listar du permanenta vs aktiva regler?', back: '--list-all: aktiva\n--list-all --permanent: sparade', category: 'Regler', difficulty: 'G' },
    // Hard (8)
    { id: 't18-23', front: 'Hur skapar du egen tjänst?', back: 'Skapa XML i /etc/firewalld/services/\nKopiera från /usr/lib/firewalld/services/', category: 'Tjänster', difficulty: 'VG' },
    { id: 't18-24', front: 'Hur skapar du egen zon?', back: 'sudo firewall-cmd --permanent --new-zone=custom\nsudo firewall-cmd --reload', category: 'Zoner', difficulty: 'VG' },
    { id: 't18-25', front: 'Hur aktiverar du port forwarding?', back: 'sudo firewall-cmd --add-forward-port=port=80:proto=tcp:toport=8080', category: 'Forwarding', difficulty: 'VG' },
    { id: 't18-26', front: 'Hur aktiverar du masquerading (NAT)?', back: 'sudo firewall-cmd --add-masquerade\nKrävs för port forwarding till annan host.', category: 'NAT', difficulty: 'VG' },
    { id: 't18-27', front: 'Var lagras firewalld-konfiguration?', back: '/etc/firewalld/\n/usr/lib/firewalld/ (default)', category: 'Konfiguration', difficulty: 'VG' },
    { id: 't18-28', front: 'Hur loggar du droppade paket?', back: 'sudo firewall-cmd --set-log-denied=all\nLoggar till systemd journal.', category: 'Loggning', difficulty: 'VG' },
    { id: 't18-29', front: 'Skillnad runtime vs permanent?', back: 'Runtime: aktiv nu, försvinner vid reload\nPermanent: sparad, kräver reload', category: 'Koncept', difficulty: 'VG' },
    { id: 't18-30', front: 'Hur synkar du runtime till permanent?', back: 'sudo firewall-cmd --runtime-to-permanent\nSparar alla aktiva ändringar.', category: 'Synk', difficulty: 'VG' }
]

// =============================================================================
// TASK 19: LAGRING & LVM (30 flashcards)
// =============================================================================

const TASK_19_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't19-1', front: 'Hur listar du blockenheter?', back: 'lsblk\nVisar diskar och partitioner.', category: 'Grunder', difficulty: 'G' },
    { id: 't19-2', front: 'Hur visar du diskutrymme?', back: 'df -h\n-h = human readable (GB, MB)', category: 'Grunder', difficulty: 'G' },
    { id: 't19-3', front: 'Hur visar du filstorlekar?', back: 'du -sh /path\n-s = summary, -h = human', category: 'Grunder', difficulty: 'G' },
    { id: 't19-4', front: 'Var monteras diskar vanligtvis?', back: '/mnt eller /media\n/mnt: manuella mounts\n/media: automatiska', category: 'Mount', difficulty: 'G' },
    { id: 't19-5', front: 'Hur monterar du en partition?', back: 'sudo mount /dev/sdb1 /mnt/disk', category: 'Mount', difficulty: 'G' },
    { id: 't19-6', front: 'Hur avmonterar du?', back: 'sudo umount /mnt/disk\neller: sudo umount /dev/sdb1', category: 'Mount', difficulty: 'G' },
    { id: 't19-7', front: 'Vad är /etc/fstab?', back: 'Fil som definierar automatiska mounts vid boot.', category: 'fstab', difficulty: 'G' },
    { id: 't19-8', front: 'Hur partitionerar du disk?', back: 'fdisk /dev/sdb (MBR)\ngdisk /dev/sdb (GPT)\nparted', category: 'Partitioner', difficulty: 'G' },
    { id: 't19-9', front: 'Hur formaterar du partition med ext4?', back: 'sudo mkfs.ext4 /dev/sdb1', category: 'Filsystem', difficulty: 'G' },
    { id: 't19-10', front: 'Vad är LVM?', back: 'Logical Volume Manager\nFlexibel diskhantering.\nKan ändra storlek dynamiskt.', category: 'LVM', difficulty: 'G' },
    // Medium (12)
    { id: 't19-11', front: 'Vilka är LVM:s tre lager?', back: 'PV: Physical Volume (disk)\nVG: Volume Group (pool)\nLV: Logical Volume (partition)', category: 'LVM', difficulty: 'G' },
    { id: 't19-12', front: 'Hur skapar du Physical Volume?', back: 'sudo pvcreate /dev/sdb', category: 'LVM', difficulty: 'G' },
    { id: 't19-13', front: 'Hur skapar du Volume Group?', back: 'sudo vgcreate myvg /dev/sdb /dev/sdc', category: 'LVM', difficulty: 'G' },
    { id: 't19-14', front: 'Hur skapar du Logical Volume?', back: 'sudo lvcreate -L 10G -n mylv myvg', category: 'LVM', difficulty: 'G' },
    { id: 't19-15', front: 'Hur listar du PV/VG/LV?', back: 'pvs, vgs, lvs\neller: pvdisplay, vgdisplay, lvdisplay', category: 'LVM', difficulty: 'G' },
    { id: 't19-16', front: 'Hur utökar du LV?', back: 'sudo lvextend -L +5G /dev/myvg/mylv\nDärefter: resize2fs /dev/myvg/mylv', category: 'LVM', difficulty: 'G' },
    { id: 't19-17', front: 'fstab-format?', back: 'device mountpoint fstype options dump pass\n/dev/sdb1 /mnt ext4 defaults 0 2', category: 'fstab', difficulty: 'G' },
    { id: 't19-18', front: 'Vad är UUID?', back: 'Universally Unique Identifier\nUnikt för varje filsystem.\nblkid visar UUID.', category: 'UUID', difficulty: 'G' },
    { id: 't19-19', front: 'Hur använder du UUID i fstab?', back: 'UUID=abc123... /mnt ext4 defaults 0 2\nSäkrare än /dev/sdX', category: 'fstab', difficulty: 'G' },
    { id: 't19-20', front: 'Vad är swap?', back: 'Virtuellt minne på disk.\nAnvänds när RAM är fullt.\nmkswap, swapon', category: 'Swap', difficulty: 'G' },
    { id: 't19-21', front: 'Hur skapar du swap-fil?', back: 'dd if=/dev/zero of=/swapfile bs=1G count=2\nmkswap /swapfile\nswapon /swapfile', category: 'Swap', difficulty: 'G' },
    { id: 't19-22', front: 'Vad gör blkid?', back: 'Visar UUID, filsystemtyp och labels.\nblkid /dev/sdb1', category: 'Verktyg', difficulty: 'G' },
    // Hard (8)
    { id: 't19-23', front: 'Skillnad MBR vs GPT?', back: 'MBR: max 4 primära, 2TB limit\nGPT: 128 partitioner, stöd för stora diskar', category: 'Partitioner', difficulty: 'VG' },
    { id: 't19-24', front: 'Hur krymper du LV?', back: 'OBS: Kan förlora data!\numount, resize2fs, lvreduce\nKrymper EJ om monterad.', category: 'LVM', difficulty: 'VG' },
    { id: 't19-25', front: 'Hur lägger du till disk till VG?', back: 'pvcreate /dev/sdd\nvgextend myvg /dev/sdd', category: 'LVM', difficulty: 'VG' },
    { id: 't19-26', front: 'Hur tar du snapshot med LVM?', back: 'lvcreate -L 1G -s -n snap /dev/myvg/mylv\n-s = snapshot', category: 'LVM', difficulty: 'VG' },
    { id: 't19-27', front: 'Vad är noatime mount-option?', back: 'Uppdaterar inte access time.\nFörbättrar prestanda på SSD.', category: 'Mount', difficulty: 'VG' },
    { id: 't19-28', front: 'Hur testar du fstab utan reboot?', back: 'mount -a\nMonterar allt i fstab som inte redan är monterat.', category: 'fstab', difficulty: 'VG' },
    { id: 't19-29', front: 'Hur reparerar du filsystem?', back: 'fsck /dev/sdb1\nMÅSTE vara avmonterat!\nfsck.ext4 för ext4', category: 'Reparation', difficulty: 'VG' },
    { id: 't19-30', front: 'Vad är LUKS?', back: 'Linux Unified Key Setup\nDisk-kryptering.\ncryptsetup luksFormat', category: 'Kryptering', difficulty: 'VG' }
]

// =============================================================================
// TASK 20: BACKUP (30 flashcards)
// =============================================================================

const TASK_20_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't20-1', front: 'Grundläggande tar-arkiv?', back: 'tar -cvf arkiv.tar filer/\n-c = create\n-v = verbose\n-f = file', category: 'tar', difficulty: 'G' },
    { id: 't20-2', front: 'Hur packar du upp tar?', back: 'tar -xvf arkiv.tar\n-x = extract', category: 'tar', difficulty: 'G' },
    { id: 't20-3', front: 'Hur komprimerar du med gzip?', back: 'tar -czvf arkiv.tar.gz filer/\n-z = gzip', category: 'tar', difficulty: 'G' },
    { id: 't20-4', front: 'Hur komprimerar du med bzip2?', back: 'tar -cjvf arkiv.tar.bz2 filer/\n-j = bzip2', category: 'tar', difficulty: 'G' },
    { id: 't20-5', front: 'Vad gör rsync?', back: 'Synkroniserar filer/kataloger.\nKopierar bara ändringar.\nEffektiv backup.', category: 'rsync', difficulty: 'G' },
    { id: 't20-6', front: 'Grundläggande rsync-syntax?', back: 'rsync -av källa/ mål/\n-a = archive (bevarar allt)\n-v = verbose', category: 'rsync', difficulty: 'G' },
    { id: 't20-7', front: 'Hur kopierar du med cp rekursivt?', back: 'cp -r källa/ mål/', category: 'cp', difficulty: 'G' },
    { id: 't20-8', front: 'Vad är inkrementell backup?', back: 'Kopierar bara filer som\nändrats sedan förra backupen.', category: 'Koncept', difficulty: 'G' },
    { id: 't20-9', front: 'Vad är full backup?', back: 'Kopierar ALLA filer.\nKrävs som bas för inkrementell.', category: 'Koncept', difficulty: 'G' },
    { id: 't20-10', front: 'Hur listar du innehåll i tar?', back: 'tar -tvf arkiv.tar\n-t = list', category: 'tar', difficulty: 'G' },
    // Medium (12)
    { id: 't20-11', front: 'rsync med progress?', back: 'rsync -av --progress källa/ mål/', category: 'rsync', difficulty: 'G' },
    { id: 't20-12', front: 'rsync över SSH?', back: 'rsync -avz -e ssh källa/ user@host:/mål/', category: 'rsync', difficulty: 'G' },
    { id: 't20-13', front: 'Vad gör rsync --delete?', back: 'Tar bort filer i mål som\ninte finns i källa.\nSynkroniserar exakt.', category: 'rsync', difficulty: 'G' },
    { id: 't20-14', front: 'Vad gör rsync -n/--dry-run?', back: 'Visar vad som skulle hända\nutan att göra något.\nBra för test.', category: 'rsync', difficulty: 'G' },
    { id: 't20-15', front: 'Hur exkluderar du filer i rsync?', back: 'rsync -av --exclude="*.log" källa/ mål/', category: 'rsync', difficulty: 'G' },
    { id: 't20-16', front: 'Vad gör dd?', back: 'Disk duplicator.\nKopierar rå data bit-för-bit.\ndd if=/dev/sda of=/dev/sdb', category: 'dd', difficulty: 'G' },
    { id: 't20-17', front: 'Hur skapar du disk image med dd?', back: 'dd if=/dev/sda of=disk.img bs=4M', category: 'dd', difficulty: 'G' },
    { id: 't20-18', front: 'Vad är 3-2-1 backup-regeln?', back: '3 kopior av data\n2 olika medier\n1 offsite (annan plats)', category: 'Best Practice', difficulty: 'G' },
    { id: 't20-19', front: 'Hur schemalägger du backup?', back: 'Använd cron.\ncrontab -e\n0 2 * * * /scripts/backup.sh', category: 'Schemaläggning', difficulty: 'G' },
    { id: 't20-20', front: 'Hur packar du upp specifik fil från tar?', back: 'tar -xvf arkiv.tar fil.txt', category: 'tar', difficulty: 'G' },
    { id: 't20-21', front: 'Hur komprimerar du med xz (bäst kompression)?', back: 'tar -cJvf arkiv.tar.xz filer/\n-J = xz (långsam men liten)', category: 'tar', difficulty: 'G' },
    { id: 't20-22', front: 'Hur bevarar du rättigheter i tar?', back: 'tar -cvpf arkiv.tar filer/\n-p = preserve permissions', category: 'tar', difficulty: 'G' },
    // Hard (8)
    { id: 't20-23', front: 'Hur gör du inkrementell backup med tar?', back: 'tar --listed-incremental=snapshot.snar -cvzf backup.tar.gz dir/', category: 'tar', difficulty: 'VG' },
    { id: 't20-24', front: 'Vad är rsnapshot?', back: 'Verktyg för rotationsbackuper.\nAnvänder hard links för utrymme.\nKonfigureras i /etc/rsnapshot.conf', category: 'Verktyg', difficulty: 'VG' },
    { id: 't20-25', front: 'Hur verifierar du backup?', back: 'Testa restore!\ntar -tvf för lista\nmd5sum för checksums', category: 'Verifiering', difficulty: 'VG' },
    { id: 't20-26', front: 'Vad är borgbackup?', back: 'Deduplicerande backup.\nKrypterad och komprimerad.\nEffektiv för stora dataset.', category: 'Verktyg', difficulty: 'VG' },
    { id: 't20-27', front: 'Hur klonar du partition med dd?', back: 'dd if=/dev/sda1 of=/dev/sdb1 bs=4M status=progress', category: 'dd', difficulty: 'VG' },
    { id: 't20-28', front: 'Vad gör rsync --link-dest?', back: 'Skapar hard links till oförändrade filer.\nEffektiv för inkrementella backuper.', category: 'rsync', difficulty: 'VG' },
    { id: 't20-29', front: 'Hur gör du remote backup med borgbackup?', back: 'borg create user@host:/repo::arkiv källa/', category: 'Verktyg', difficulty: 'VG' },
    { id: 't20-30', front: 'Hur automatiserar du backup med systemd timer?', back: 'Skapa .service och .timer\nsystemctl enable backup.timer', category: 'Schemaläggning', difficulty: 'VG' }
]

// =============================================================================
// TASK 21: SYSTEMD (30 flashcards)
// =============================================================================

const TASK_21_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't21-1', front: 'Vad är systemd?', back: 'Init-system och servicehanterare.\nPID 1, startar alla tjänster.', category: 'Grunder', difficulty: 'G' },
    { id: 't21-2', front: 'Hur startar du en tjänst?', back: 'sudo systemctl start <tjänst>\nEx: systemctl start nginx', category: 'Tjänster', difficulty: 'G' },
    { id: 't21-3', front: 'Hur stoppar du en tjänst?', back: 'sudo systemctl stop <tjänst>', category: 'Tjänster', difficulty: 'G' },
    { id: 't21-4', front: 'Hur startar du om en tjänst?', back: 'sudo systemctl restart <tjänst>', category: 'Tjänster', difficulty: 'G' },
    { id: 't21-5', front: 'Hur visar du tjänststatus?', back: 'systemctl status <tjänst>\nVisar state, PID, loggar.', category: 'Status', difficulty: 'G' },
    { id: 't21-6', front: 'Hur aktiverar du tjänst vid boot?', back: 'sudo systemctl enable <tjänst>', category: 'Boot', difficulty: 'G' },
    { id: 't21-7', front: 'Hur avaktiverar du tjänst vid boot?', back: 'sudo systemctl disable <tjänst>', category: 'Boot', difficulty: 'G' },
    { id: 't21-8', front: 'Hur listar du alla tjänster?', back: 'systemctl list-units --type=service', category: 'Listing', difficulty: 'G' },
    { id: 't21-9', front: 'Vad är en unit i systemd?', back: 'Resursobjekt: service, timer,\nmount, socket, target etc.', category: 'Koncept', difficulty: 'G' },
    { id: 't21-10', front: 'Var finns systemd unit-filer?', back: '/etc/systemd/system/ (custom)\n/lib/systemd/system/ (default)', category: 'Filer', difficulty: 'G' },
    // Medium (12)
    { id: 't21-11', front: 'Hur laddar du om konfiguration?', back: 'sudo systemctl daemon-reload\nKrävs efter ändring av unit-fil.', category: 'Reload', difficulty: 'G' },
    { id: 't21-12', front: 'Hur laddar du om tjänst utan avbrott?', back: 'sudo systemctl reload <tjänst>\nFungerar om tjänsten stödjer det.', category: 'Reload', difficulty: 'G' },
    { id: 't21-13', front: 'Vad gör enable --now?', back: 'sudo systemctl enable --now <tjänst>\nAktiverar OCH startar direkt.', category: 'Boot', difficulty: 'G' },
    { id: 't21-14', front: 'Hur visar du dependencies?', back: 'systemctl list-dependencies <tjänst>', category: 'Dependencies', difficulty: 'G' },
    { id: 't21-15', front: 'Hur visar du reverse dependencies?', back: 'systemctl list-dependencies --reverse <tjänst>', category: 'Dependencies', difficulty: 'G' },
    { id: 't21-16', front: 'Hur visar du loggar för tjänst?', back: 'journalctl -u <tjänst>\n-f för live-följning', category: 'Logging', difficulty: 'G' },
    { id: 't21-17', front: 'Hur visar du bootloggar?', back: 'journalctl -b\n-b -1 för förra booten', category: 'Logging', difficulty: 'G' },
    { id: 't21-18', front: 'Grundläggande service unit-fil?', back: '[Unit]\nDescription=Min tjänst\n\n[Service]\nExecStart=/usr/bin/app\n\n[Install]\nWantedBy=multi-user.target', category: 'Unit-fil', difficulty: 'G' },
    { id: 't21-19', front: 'Vad är targets i systemd?', back: 'Grupper av units.\nmulti-user.target ≈ runlevel 3\ngraphical.target ≈ runlevel 5', category: 'Targets', difficulty: 'G' },
    { id: 't21-20', front: 'Hur ser du aktuellt target?', back: 'systemctl get-default', category: 'Targets', difficulty: 'G' },
    { id: 't21-21', front: 'Hur visar du misslyckade tjänster?', back: 'systemctl --failed', category: 'Status', difficulty: 'G' },
    { id: 't21-22', front: 'Vad är journald?', back: 'Systemd loggningsdaemon.\nLagrar binära loggar.\nAnvänd journalctl.', category: 'Logging', difficulty: 'G' },
    // Hard (8)
    { id: 't21-23', front: 'Hur skapar du timer unit?', back: '[Unit]\nDescription=Timer\n\n[Timer]\nOnCalendar=daily\nPersistent=true\n\n[Install]\nWantedBy=timers.target', category: 'Timer', difficulty: 'VG' },
    { id: 't21-24', front: 'Hur maskerar du en tjänst?', back: 'sudo systemctl mask <tjänst>\nFörhindrar start helt.\nunmask för att återställa.', category: 'Säkerhet', difficulty: 'VG' },
    { id: 't21-25', front: 'Vad gör Restart=always?', back: 'I [Service]: Startar om tjänsten\nautomatiskt om den crashar.', category: 'Unit-fil', difficulty: 'VG' },
    { id: 't21-26', front: 'Hur begränsar du resurser för tjänst?', back: '[Service]\nMemoryLimit=512M\nCPUQuota=50%', category: 'Resurser', difficulty: 'VG' },
    { id: 't21-27', front: 'Vad är WantedBy vs RequiredBy?', back: 'WantedBy: svagt beroende (enable)\nRequiredBy: starkt beroende', category: 'Dependencies', difficulty: 'VG' },
    { id: 't21-28', front: 'Hur debuggar du startproblem?', back: 'systemctl status <tjänst>\njournalctl -xe\njournalctl -u <tjänst>', category: 'Debug', difficulty: 'VG' },
    { id: 't21-29', front: 'Hur sätter du environment i unit?', back: '[Service]\nEnvironment="VAR=value"\nEnvironmentFile=/etc/default/app', category: 'Config', difficulty: 'VG' },
    { id: 't21-30', front: 'Vad är socket activation?', back: 'Systemd lyssnar på socket.\nStartar tjänst vid anslutning.\nEffektivt för on-demand.', category: 'Avancerat', difficulty: 'VG' }
]

// =============================================================================
// TASK 22: DOCKER GRUNDER (30 flashcards)
// =============================================================================

const TASK_22_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't22-1', front: 'Vad är Docker?', back: 'Containerplattform.\nKör isolerade applikationer.\nDelar värdkärna.', category: 'Grunder', difficulty: 'G' },
    { id: 't22-2', front: 'Skillnad container vs VM?', back: 'Container: delar OS-kärna, lätt\nVM: eget OS, tyngre', category: 'Koncept', difficulty: 'G' },
    { id: 't22-3', front: 'Hur startar du en container?', back: 'docker run <image>\nEx: docker run nginx', category: 'run', difficulty: 'G' },
    { id: 't22-4', front: 'Hur listar du körande containers?', back: 'docker ps\ndocker container ls', category: 'Listing', difficulty: 'G' },
    { id: 't22-5', front: 'Hur listar du alla containers?', back: 'docker ps -a\nInkluderar stoppade.', category: 'Listing', difficulty: 'G' },
    { id: 't22-6', front: 'Hur stoppar du en container?', back: 'docker stop <container>\nGer tid att stänga av gracefully.', category: 'Lifecycle', difficulty: 'G' },
    { id: 't22-7', front: 'Hur tar du bort en container?', back: 'docker rm <container>\nMåste vara stoppad först.', category: 'Lifecycle', difficulty: 'G' },
    { id: 't22-8', front: 'Hur kör du container i bakgrunden?', back: 'docker run -d <image>\n-d = detached mode', category: 'run', difficulty: 'G' },
    { id: 't22-9', front: 'Hur namnger du en container?', back: 'docker run --name myapp <image>', category: 'run', difficulty: 'G' },
    { id: 't22-10', front: 'Hur listar du images?', back: 'docker images\ndocker image ls', category: 'Images', difficulty: 'G' },
    // Medium (12)
    { id: 't22-11', front: 'Hur mappar du port?', back: 'docker run -p 8080:80 nginx\nHost:Container', category: 'Networking', difficulty: 'G' },
    { id: 't22-12', front: 'Hur kör du interaktiv container?', back: 'docker run -it ubuntu bash\n-i = interactive, -t = tty', category: 'run', difficulty: 'G' },
    { id: 't22-13', front: 'Hur monterar du volym?', back: 'docker run -v /host:/container image\neller: -v myvolume:/container', category: 'Volumes', difficulty: 'G' },
    { id: 't22-14', front: 'Hur sätter du miljövariabel?', back: 'docker run -e VAR=value image\neller: --env VAR=value', category: 'Config', difficulty: 'G' },
    { id: 't22-15', front: 'Hur visar du container-loggar?', back: 'docker logs <container>\n-f för follow', category: 'Logs', difficulty: 'G' },
    { id: 't22-16', front: 'Hur kör du kommando i körande container?', back: 'docker exec -it container bash', category: 'exec', difficulty: 'G' },
    { id: 't22-17', front: 'Hur inspekterar du container?', back: 'docker inspect <container>\nVisar all metadata som JSON.', category: 'Info', difficulty: 'G' },
    { id: 't22-18', front: 'Hur tar du bort stoppade containers?', back: 'docker container prune\neller: docker rm $(docker ps -aq)', category: 'Cleanup', difficulty: 'G' },
    { id: 't22-19', front: 'Hur drar du ner image?', back: 'docker pull <image>\nEx: docker pull nginx:latest', category: 'Images', difficulty: 'G' },
    { id: 't22-20', front: 'Hur tar du bort image?', back: 'docker rmi <image>\ndocker image rm <image>', category: 'Images', difficulty: 'G' },
    { id: 't22-21', front: 'Vad är --rm flaggan?', back: 'Tar bort container när den avslutas.\ndocker run --rm image', category: 'run', difficulty: 'G' },
    { id: 't22-22', front: 'Hur startar du stoppad container?', back: 'docker start <container>', category: 'Lifecycle', difficulty: 'G' },
    // Hard (8)
    { id: 't22-23', front: 'Skillnad ENTRYPOINT vs CMD?', back: 'ENTRYPOINT: huvudkommando (fixerat)\nCMD: default-argument (kan överskridas)', category: 'Dockerfile', difficulty: 'VG' },
    { id: 't22-24', front: 'Hur begränsar du minne?', back: 'docker run -m 512m image\neller: --memory=512m', category: 'Resurser', difficulty: 'VG' },
    { id: 't22-25', front: 'Hur begränsar du CPU?', back: 'docker run --cpus=1.5 image\neller: --cpu-shares', category: 'Resurser', difficulty: 'VG' },
    { id: 't22-26', front: 'Vad är Docker network?', back: 'Isolerade nätverk för containers.\nbridge (default), host, none', category: 'Networking', difficulty: 'VG' },
    { id: 't22-27', front: 'Hur skapar du nätverk?', back: 'docker network create mynet\ndocker run --network=mynet image', category: 'Networking', difficulty: 'VG' },
    { id: 't22-28', front: 'Vad är named volume vs bind mount?', back: 'Named: Docker-hanterad (-v name:/path)\nBind: host-sökväg (-v /host:/cont)', category: 'Volumes', difficulty: 'VG' },
    { id: 't22-29', front: 'Hur visar du resursanvändning?', back: 'docker stats\nVisar CPU, mem, network, I/O', category: 'Monitoring', difficulty: 'VG' },
    { id: 't22-30', front: 'Hur exporterar du container till tar?', back: 'docker export container > file.tar\nExporterar filsystem.', category: 'Export', difficulty: 'VG' }
]

// =============================================================================
// TASK 23: DOCKER IMAGES (30 flashcards)
// =============================================================================

const TASK_23_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't23-1', front: 'Vad är en Docker image?', back: 'Mall för containers.\nImmutable lager av filsystem.\nByggs från Dockerfile.', category: 'Grunder', difficulty: 'G' },
    { id: 't23-2', front: 'Vad är en Dockerfile?', back: 'Instruktionsfil för att bygga image.\nDefinierar bas, kommandon, portar etc.', category: 'Dockerfile', difficulty: 'G' },
    { id: 't23-3', front: 'Hur bygger du image?', back: 'docker build -t name:tag .\n-t = tag, . = build context', category: 'Build', difficulty: 'G' },
    { id: 't23-4', front: 'Vad gör FROM i Dockerfile?', back: 'Anger basimage.\nFROM ubuntu:22.04\nFROM python:3.11', category: 'Dockerfile', difficulty: 'G' },
    { id: 't23-5', front: 'Vad gör RUN i Dockerfile?', back: 'Kör kommando vid build.\nRUN apt-get update && apt-get install -y nginx', category: 'Dockerfile', difficulty: 'G' },
    { id: 't23-6', front: 'Vad gör COPY i Dockerfile?', back: 'Kopierar filer till image.\nCOPY ./app /app', category: 'Dockerfile', difficulty: 'G' },
    { id: 't23-7', front: 'Vad gör CMD i Dockerfile?', back: 'Default-kommando vid run.\nCMD ["python", "app.py"]', category: 'Dockerfile', difficulty: 'G' },
    { id: 't23-8', front: 'Vad gör EXPOSE i Dockerfile?', back: 'Dokumenterar vilken port appen lyssnar på.\nEXPOSE 80', category: 'Dockerfile', difficulty: 'G' },
    { id: 't23-9', front: 'Vad gör WORKDIR i Dockerfile?', back: 'Sätter arbetskatalog.\nWORKDIR /app\nAlla kommandon körs därifrån.', category: 'Dockerfile', difficulty: 'G' },
    { id: 't23-10', front: 'Hur taggar du image?', back: 'docker tag source:tag target:tag\neller vid build: -t name:tag', category: 'Tags', difficulty: 'G' },
    // Medium (12)
    { id: 't23-11', front: 'Vad gör ADD vs COPY?', back: 'COPY: enkel kopiering\nADD: extra features (url, untar)', category: 'Dockerfile', difficulty: 'G' },
    { id: 't23-12', front: 'Vad gör ENV i Dockerfile?', back: 'Sätter miljövariabel.\nENV NODE_ENV=production', category: 'Dockerfile', difficulty: 'G' },
    { id: 't23-13', front: 'Vad gör ENTRYPOINT?', back: 'Fixerat startkommando.\nENTRYPOINT ["python"]\nCMD ["app.py"]', category: 'Dockerfile', difficulty: 'G' },
    { id: 't23-14', front: 'Hur pushar du till registry?', back: 'docker login\ndocker push user/image:tag', category: 'Registry', difficulty: 'G' },
    { id: 't23-15', front: 'Vad är Docker Hub?', back: 'Publik image-registry.\nStandard-källa för docker pull.', category: 'Registry', difficulty: 'G' },
    { id: 't23-16', front: 'Vad är image layers?', back: 'Varje instruktion skapar lager.\nLager cachas och återanvänds.\nEffektivt för rebuild.', category: 'Koncept', difficulty: 'G' },
    { id: 't23-17', front: 'Hur visar du image-historik?', back: 'docker history <image>\nVisar alla lager och storlekar.', category: 'Info', difficulty: 'G' },
    { id: 't23-18', front: 'Hur rensar du oanvända images?', back: 'docker image prune\n-a för ALLA oanvända', category: 'Cleanup', difficulty: 'G' },
    { id: 't23-19', front: 'Vad är .dockerignore?', back: 'Exkluderar filer från build context.\nSom .gitignore för Docker.', category: 'Build', difficulty: 'G' },
    { id: 't23-20', front: 'Hur bygger du utan cache?', back: 'docker build --no-cache -t name .', category: 'Build', difficulty: 'G' },
    { id: 't23-21', front: 'Vad gör ARG i Dockerfile?', back: 'Build-time variabel.\nARG VERSION=1.0\ndocker build --build-arg VERSION=2.0', category: 'Dockerfile', difficulty: 'G' },
    { id: 't23-22', front: 'Hur sparar du image till fil?', back: 'docker save image > file.tar\nLadda: docker load < file.tar', category: 'Export', difficulty: 'G' },
    // Hard (8)
    { id: 't23-23', front: 'Vad är multi-stage build?', back: 'Flera FROM i samma Dockerfile.\nBygg i ett steg, kopiera till liten image.\nMinskar slutlig storlek.', category: 'Optimering', difficulty: 'VG' },
    { id: 't23-24', front: 'Multi-stage build exempel?', back: 'FROM golang AS builder\nRUN go build...\n\nFROM alpine\nCOPY --from=builder /app /app', category: 'Optimering', difficulty: 'VG' },
    { id: 't23-25', front: 'Hur minimerar du image-storlek?', back: 'Använd alpine base\nMulti-stage builds\nKombinera RUN-kommandon\nRensa cache i samma lager', category: 'Optimering', difficulty: 'VG' },
    { id: 't23-26', front: 'Hur kör du som non-root?', back: 'RUN useradd -m appuser\nUSER appuser\nSäkrare container.', category: 'Säkerhet', difficulty: 'VG' },
    { id: 't23-27', front: 'Vad gör HEALTHCHECK?', back: 'HEALTHCHECK CMD curl -f http://localhost/\nDocker kollar om container är frisk.', category: 'Dockerfile', difficulty: 'VG' },
    { id: 't23-28', front: 'Hur skannar du image för sårbarheter?', back: 'docker scout cves <image>\neller: trivy image <image>', category: 'Säkerhet', difficulty: 'VG' },
    { id: 't23-29', front: 'Hur bygger du för annan arkitektur?', back: 'docker buildx build --platform linux/arm64\nKräver buildx.', category: 'Avancerat', difficulty: 'VG' },
    { id: 't23-30', front: 'Vad är scratch image?', back: 'Tom basimage.\nFROM scratch\nFör statiskt länkade binärer.', category: 'Optimering', difficulty: 'VG' }
]

// =============================================================================
// TASK 24: DOCKER COMPOSE (30 flashcards)
// =============================================================================

const TASK_24_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't24-1', front: 'Vad är Docker Compose?', back: 'Verktyg för multi-container apps.\nDefinierar tjänster i YAML.\ndocker compose up', category: 'Grunder', difficulty: 'G' },
    { id: 't24-2', front: 'Hur startar du compose?', back: 'docker compose up\n-d för detached (bakgrund)', category: 'Kommandon', difficulty: 'G' },
    { id: 't24-3', front: 'Hur stoppar du compose?', back: 'docker compose down\nStoppar och tar bort containers.', category: 'Kommandon', difficulty: 'G' },
    { id: 't24-4', front: 'Vad heter compose-filen?', back: 'docker-compose.yml\neller compose.yaml', category: 'Konfiguration', difficulty: 'G' },
    { id: 't24-5', front: 'Grundläggande compose-struktur?', back: 'services:\n  web:\n    image: nginx\n    ports:\n      - "80:80"', category: 'YAML', difficulty: 'G' },
    { id: 't24-6', front: 'Hur listar du compose-tjänster?', back: 'docker compose ps', category: 'Kommandon', difficulty: 'G' },
    { id: 't24-7', front: 'Hur visar du loggar?', back: 'docker compose logs\n-f för follow', category: 'Logs', difficulty: 'G' },
    { id: 't24-8', front: 'Hur startar du om tjänst?', back: 'docker compose restart <service>', category: 'Kommandon', difficulty: 'G' },
    { id: 't24-9', front: 'Hur bygger du images med compose?', back: 'docker compose build\neller: docker compose up --build', category: 'Build', difficulty: 'G' },
    { id: 't24-10', front: 'Hur kör du kommando i tjänst?', back: 'docker compose exec <service> bash', category: 'Kommandon', difficulty: 'G' },
    // Medium (12)
    { id: 't24-11', front: 'Hur anger du build-context?', back: 'services:\n  app:\n    build: ./app\n    # eller:\n    build:\n      context: ./app\n      dockerfile: Dockerfile', category: 'Build', difficulty: 'G' },
    { id: 't24-12', front: 'Hur definierar du volymer?', back: 'services:\n  db:\n    volumes:\n      - data:/var/lib/mysql\nvolumes:\n  data:', category: 'Volumes', difficulty: 'G' },
    { id: 't24-13', front: 'Hur definierar du miljövariabler?', back: 'services:\n  app:\n    environment:\n      - NODE_ENV=prod\n    # eller:\n    env_file:\n      - .env', category: 'Config', difficulty: 'G' },
    { id: 't24-14', front: 'Hur skapar du beroenden?', back: 'services:\n  app:\n    depends_on:\n      - db\n      - redis', category: 'Dependencies', difficulty: 'G' },
    { id: 't24-15', front: 'Hur definierar du nätverk?', back: 'services:\n  app:\n    networks:\n      - frontend\n      - backend\nnetworks:\n  frontend:\n  backend:', category: 'Networking', difficulty: 'G' },
    { id: 't24-16', front: 'Hur skalar du tjänst?', back: 'docker compose up -d --scale web=3', category: 'Scaling', difficulty: 'G' },
    { id: 't24-17', front: 'Hur anger du restart policy?', back: 'services:\n  app:\n    restart: always\n    # no, on-failure, unless-stopped', category: 'Config', difficulty: 'G' },
    { id: 't24-18', front: 'Vad gör docker compose pull?', back: 'Drar ner senaste versioner av alla images.', category: 'Kommandon', difficulty: 'G' },
    { id: 't24-19', front: 'Hur kör du engångskommando?', back: 'docker compose run app npm test\nSkapar ny container för kommandot.', category: 'Kommandon', difficulty: 'G' },
    { id: 't24-20', front: 'Hur stoppar du utan att ta bort?', back: 'docker compose stop\nBehåller containers och volymer.', category: 'Kommandon', difficulty: 'G' },
    { id: 't24-21', front: 'Hur tar du bort volymer?', back: 'docker compose down -v\n-v tar bort volymer också.', category: 'Cleanup', difficulty: 'G' },
    { id: 't24-22', front: 'Hur använder du .env-fil?', back: '.env i samma katalog.\nVARIABEL=värde\nAnvänds automatiskt.', category: 'Config', difficulty: 'G' },
    // Hard (8)
    { id: 't24-23', front: 'Hur använder du profiles?', back: 'services:\n  debug:\n    profiles: [dev]\ndocker compose --profile dev up', category: 'Profiles', difficulty: 'VG' },
    { id: 't24-24', front: 'Hur gör du healthcheck i compose?', back: 'services:\n  app:\n    healthcheck:\n      test: curl -f http://localhost\n      interval: 30s', category: 'Health', difficulty: 'VG' },
    { id: 't24-25', front: 'Vad är depends_on condition?', back: 'depends_on:\n  db:\n    condition: service_healthy\nVäntar på healthcheck.', category: 'Dependencies', difficulty: 'VG' },
    { id: 't24-26', front: 'Hur begränsar du resurser?', back: 'services:\n  app:\n    deploy:\n      resources:\n        limits:\n          memory: 512M\n          cpus: "0.5"', category: 'Resurser', difficulty: 'VG' },
    { id: 't24-27', front: 'Hur använder du flera compose-filer?', back: 'docker compose -f base.yml -f prod.yml up\nFiler mergas i ordning.', category: 'Config', difficulty: 'VG' },
    { id: 't24-28', front: 'Vad är extends i compose?', back: 'services:\n  app:\n    extends:\n      file: common.yml\n      service: base\nÄrver från annan fil.', category: 'Avancerat', difficulty: 'VG' },
    { id: 't24-29', front: 'Hur loggar du till extern tjänst?', back: 'services:\n  app:\n    logging:\n      driver: json-file\n      options:\n        max-size: "10m"', category: 'Logging', difficulty: 'VG' },
    { id: 't24-30', front: 'Skillnad docker compose vs docker-compose?', back: 'docker compose: ny (v2, plugin)\ndocker-compose: gammal (v1, standalone)', category: 'Version', difficulty: 'VG' }
]

// =============================================================================
// TASK 25: GIT (30 flashcards)
// =============================================================================

const TASK_25_FLASHCARDS: TaskFlashcard[] = [
    // Easy (10)
    { id: 't25-1', front: 'Vad är Git?', back: 'Distribuerat versionshanteringssystem.\nSpårar ändringar i kod.\nSkapar historik och branches.', category: 'Grunder', difficulty: 'G' },
    { id: 't25-2', front: 'Hur initierar du repo?', back: 'git init\nSkapar .git-katalog.', category: 'Init', difficulty: 'G' },
    { id: 't25-3', front: 'Hur klonar du repo?', back: 'git clone <url>\ngit clone git@github.com:user/repo.git', category: 'Clone', difficulty: 'G' },
    { id: 't25-4', front: 'Hur visar du status?', back: 'git status\nVisar ändrade/staged filer.', category: 'Status', difficulty: 'G' },
    { id: 't25-5', front: 'Hur lägger du till filer för commit?', back: 'git add <fil>\ngit add . (alla)\ngit add -A (allt)', category: 'Staging', difficulty: 'G' },
    { id: 't25-6', front: 'Hur committar du?', back: 'git commit -m "meddelande"', category: 'Commit', difficulty: 'G' },
    { id: 't25-7', front: 'Hur pushar du till remote?', back: 'git push\ngit push origin main', category: 'Push', difficulty: 'G' },
    { id: 't25-8', front: 'Hur pullar du från remote?', back: 'git pull\nHämtar och mergar ändringar.', category: 'Pull', difficulty: 'G' },
    { id: 't25-9', front: 'Hur visar du loggen?', back: 'git log\ngit log --oneline (kort)', category: 'Log', difficulty: 'G' },
    { id: 't25-10', front: 'Hur skapar du branch?', back: 'git branch <namn>\ngit checkout -b <namn> (skapa+byt)', category: 'Branches', difficulty: 'G' },
    // Medium (12)
    { id: 't25-11', front: 'Hur byter du branch?', back: 'git checkout <branch>\ngit switch <branch> (nyare)', category: 'Branches', difficulty: 'G' },
    { id: 't25-12', front: 'Hur mergar du branch?', back: 'git checkout main\ngit merge feature-branch', category: 'Merge', difficulty: 'G' },
    { id: 't25-13', front: 'Hur visar du diff?', back: 'git diff (unstaged)\ngit diff --staged (staged)', category: 'Diff', difficulty: 'G' },
    { id: 't25-14', front: 'Hur ångrar du unstaged ändringar?', back: 'git checkout -- <fil>\ngit restore <fil> (nyare)', category: 'Ångra', difficulty: 'G' },
    { id: 't25-15', front: 'Hur unstagar du fil?', back: 'git reset HEAD <fil>\ngit restore --staged <fil>', category: 'Ångra', difficulty: 'G' },
    { id: 't25-16', front: 'Hur tar du bort branch?', back: 'git branch -d <branch>\n-D för force delete', category: 'Branches', difficulty: 'G' },
    { id: 't25-17', front: 'Hur visar du remote URL?', back: 'git remote -v', category: 'Remote', difficulty: 'G' },
    { id: 't25-18', front: 'Hur lägger du till remote?', back: 'git remote add origin <url>', category: 'Remote', difficulty: 'G' },
    { id: 't25-19', front: 'Hur hämtar du utan merge?', back: 'git fetch\nHämtar men mergar inte.', category: 'Fetch', difficulty: 'G' },
    { id: 't25-20', front: 'Vad gör git stash?', back: 'Sparar undan ändringar temporärt.\ngit stash\ngit stash pop', category: 'Stash', difficulty: 'G' },
    { id: 't25-21', front: 'Hur visar du branches?', back: 'git branch (lokala)\ngit branch -r (remote)\ngit branch -a (alla)', category: 'Branches', difficulty: 'G' },
    { id: 't25-22', front: 'Vad är .gitignore?', back: 'Fil som listar vad Git ska ignorera.\n*.log\nnode_modules/', category: 'Config', difficulty: 'G' },
    // Hard (8)
    { id: 't25-23', front: 'Hur rebasar du?', back: 'git checkout feature\ngit rebase main\nLinjär historik.', category: 'Rebase', difficulty: 'VG' },
    { id: 't25-24', front: 'Skillnad merge vs rebase?', back: 'Merge: bevarar historik, merge commit\nRebase: linjär, skriver om commits', category: 'Koncept', difficulty: 'VG' },
    { id: 't25-25', front: 'Hur cherry-pickar du commit?', back: 'git cherry-pick <commit-hash>\nTar en specifik commit.', category: 'Cherry-pick', difficulty: 'VG' },
    { id: 't25-26', front: 'Hur ångrar du senaste commit?', back: 'git reset --soft HEAD~1 (behåller ändringar)\ngit reset --hard HEAD~1 (tar bort)', category: 'Ångra', difficulty: 'VG' },
    { id: 't25-27', front: 'Hur ändrar du senaste commit?', back: 'git commit --amend\nÄndrar meddelande/lägger till filer.', category: 'Commit', difficulty: 'VG' },
    { id: 't25-28', front: 'Hur löser du merge-konflikt?', back: '1. Öppna filen\n2. Välj kod (HEAD eller incoming)\n3. git add <fil>\n4. git commit', category: 'Konflikter', difficulty: 'VG' },
    { id: 't25-29', front: 'Hur interaktiv rebasar du?', back: 'git rebase -i HEAD~3\nSquash, edit, reorder commits.', category: 'Rebase', difficulty: 'VG' },
    { id: 't25-30', front: 'Hur skapar du tag?', back: 'git tag v1.0.0\ngit tag -a v1.0.0 -m "Release"\ngit push --tags', category: 'Tags', difficulty: 'VG' }
]

// =============================================================================
// EXPORT
// =============================================================================

export const DOE25_TASK_FLASHCARDS: TaskFlashcardSet[] = [
    {
        taskId: 'doe25-0-1-subnetting',
        taskTitle: '0.1 Subnetting & Nätverk',
        flashcards: TASK_1_FLASHCARDS
    },
    {
        taskId: 'doe25-0-2-filsystem',
        taskTitle: '0.2 Linux Filsystem',
        flashcards: TASK_2_FLASHCARDS
    },
    {
        taskId: 'doe25-1-1-bash-grunder',
        taskTitle: '1.1 Bash Grunder',
        flashcards: TASK_3_FLASHCARDS
    },
    {
        taskId: 'doe25-1-2-variabler',
        taskTitle: '1.2 Variabler & Datatyper',
        flashcards: TASK_4_FLASHCARDS
    },
    {
        taskId: 'doe25-1-3-regex',
        taskTitle: '1.3 Reguljära Uttryck (Regex)',
        flashcards: TASK_5_FLASHCARDS
    },
    {
        taskId: 'doe25-1-4-sed',
        taskTitle: '1.4 sed - Stream Editor',
        flashcards: TASK_6_FLASHCARDS
    },
    {
        taskId: 'doe25-1-5-awk',
        taskTitle: '1.5 awk - Textbearbetning',
        flashcards: TASK_7_FLASHCARDS
    },
    {
        taskId: 'doe25-1-6-villkor',
        taskTitle: '1.6 Villkor (if/else)',
        flashcards: TASK_8_FLASHCARDS
    },
    {
        taskId: 'doe25-1-7-interaktiva',
        taskTitle: '1.7 Interaktiva Skript',
        flashcards: TASK_9_FLASHCARDS
    },
    {
        taskId: 'doe25-1-8-loopar',
        taskTitle: '1.8 Loopar (for/while)',
        flashcards: TASK_10_FLASHCARDS
    },
    {
        taskId: 'doe25-1-9-parametrar',
        taskTitle: '1.9 Skriptparametrar',
        flashcards: TASK_11_FLASHCARDS
    },
    {
        taskId: 'doe25-1-10-funktioner',
        taskTitle: '1.10 Funktioner',
        flashcards: TASK_12_FLASHCARDS
    },
    {
        taskId: 'doe25-1-11-signals',
        taskTitle: '1.11 Signaler & Trap',
        flashcards: TASK_13_FLASHCARDS
    },
    {
        taskId: 'doe25-2-1-users',
        taskTitle: '2.1 Användarhantering',
        flashcards: TASK_14_FLASHCARDS
    },
    {
        taskId: 'doe25-2-2-permissions',
        taskTitle: '2.2 Rättigheter & ACL',
        flashcards: TASK_15_FLASHCARDS
    },
    {
        taskId: 'doe25-2-3-ssh',
        taskTitle: '2.3 SSH',
        flashcards: TASK_16_FLASHCARDS
    },
    {
        taskId: 'doe25-2-4-ufw',
        taskTitle: '2.4 UFW Firewall',
        flashcards: TASK_17_FLASHCARDS
    },
    {
        taskId: 'doe25-2-5-firewalld',
        taskTitle: '2.5 Firewalld',
        flashcards: TASK_18_FLASHCARDS
    },
    {
        taskId: 'doe25-2-6-lagring',
        taskTitle: '2.6 Lagring & LVM',
        flashcards: TASK_19_FLASHCARDS
    },
    {
        taskId: 'doe25-2-7-backup',
        taskTitle: '2.7 Backup',
        flashcards: TASK_20_FLASHCARDS
    },
    {
        taskId: 'doe25-2-8-systemd',
        taskTitle: '2.8 Systemd',
        flashcards: TASK_21_FLASHCARDS
    },
    {
        taskId: 'doe25-3-1-docker-grunder',
        taskTitle: '3.1 Docker Grunder',
        flashcards: TASK_22_FLASHCARDS
    },
    {
        taskId: 'doe25-3-2-docker-images',
        taskTitle: '3.2 Docker Images',
        flashcards: TASK_23_FLASHCARDS
    },
    {
        taskId: 'doe25-3-3-docker-compose',
        taskTitle: '3.3 Docker Compose',
        flashcards: TASK_24_FLASHCARDS
    },
    {
        taskId: 'doe25-3-4-git',
        taskTitle: '3.4 Git',
        flashcards: TASK_25_FLASHCARDS
    }
]

// Helper function
export function getFlashcardsForTask(taskId: string): TaskFlashcard[] {
    const set = DOE25_TASK_FLASHCARDS.find(s => s.taskId === taskId)
    return set?.flashcards || []
}

export function getAllDOE25Flashcards(): TaskFlashcard[] {
    return DOE25_TASK_FLASHCARDS.flatMap(s => s.flashcards)
}
