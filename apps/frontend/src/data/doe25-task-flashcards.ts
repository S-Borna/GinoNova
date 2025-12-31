/**
 * DOE25 Tentaplugg - Task-specifika Flashcards
 * 30 flashcards per task, pedagogiskt fokuserade för tentaplugg
 */

export interface TaskFlashcard {
  id: string
  front: string
  back: string
  category: string
  difficulty: 'easy' | 'medium' | 'hard'
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
    difficulty: 'easy'
  },
  {
    id: 't1-2',
    front: 'Vad är värdeintervallet för en oktett i en IPv4-adress?',
    back: '0-255 (eftersom 8 bitar = 2⁸ = 256 möjliga värden)',
    category: 'IPv4 Grunder',
    difficulty: 'easy'
  },
  {
    id: 't1-3',
    front: 'Vad betyder /24 i CIDR-notation?',
    back: '24 av 32 bitar är nätverksdelen. Motsvarar subnätmask 255.255.255.0',
    category: 'CIDR',
    difficulty: 'easy'
  },
  {
    id: 't1-4',
    front: 'Vilken IP-range är reserverad för loopback (localhost)?',
    back: '127.0.0.0 - 127.255.255.255 (oftast 127.0.0.1)',
    category: 'Reserverade adresser',
    difficulty: 'easy'
  },
  {
    id: 't1-5',
    front: 'Vad är kommandot för att visa nätverkskonfiguration i Linux?',
    back: 'ip addr show (eller ip a)\nÄldre alternativ: ifconfig',
    category: 'Kommandon',
    difficulty: 'easy'
  },
  {
    id: 't1-6',
    front: 'Vad är en broadcast-adress?',
    back: 'Den sista adressen i ett subnät. Används för att skicka till ALLA enheter i nätverket.',
    category: 'Nätverkskoncept',
    difficulty: 'easy'
  },
  {
    id: 't1-7',
    front: 'Vad är en nätverksadress?',
    back: 'Den första adressen i ett subnät (alla hostbitar = 0). Identifierar själva nätverket.',
    category: 'Nätverkskoncept',
    difficulty: 'easy'
  },
  {
    id: 't1-8',
    front: 'Kommando för att testa nätverksanslutning till en host?',
    back: 'ping <ip-adress eller hostname>\nEx: ping -c 3 google.com',
    category: 'Kommandon',
    difficulty: 'easy'
  },
  {
    id: 't1-9',
    front: 'Vad visar kommandot "ip route show"?',
    back: 'Routingtabellen - visar hur nätverkstrafik dirigeras, inklusive default gateway.',
    category: 'Kommandon',
    difficulty: 'easy'
  },
  {
    id: 't1-10',
    front: 'Vad står CIDR för?',
    back: 'Classless Inter-Domain Routing - ersatte de gamla IP-klasserna för mer flexibel adressering.',
    category: 'CIDR',
    difficulty: 'easy'
  },
  // Medium (12)
  {
    id: 't1-11',
    front: 'Hur många hosts kan finnas i ett /24 nätverk?',
    back: '254 hosts\nFormel: 2^(32-24) - 2 = 2^8 - 2 = 256 - 2 = 254\n(-2 för nätverks- och broadcast-adress)',
    category: 'Subnätberäkning',
    difficulty: 'medium'
  },
  {
    id: 't1-12',
    front: 'Vad är subnätmasken för /16?',
    back: '255.255.0.0\n16 ettor följt av 16 nollor i binärt.',
    category: 'CIDR',
    difficulty: 'medium'
  },
  {
    id: 't1-13',
    front: 'Givet 192.168.1.100/24 - vad är nätverksadressen?',
    back: '192.168.1.0\nDe första 24 bitarna behålls, resten sätts till 0.',
    category: 'Subnätberäkning',
    difficulty: 'medium'
  },
  {
    id: 't1-14',
    front: 'Givet 192.168.1.100/24 - vad är broadcast-adressen?',
    back: '192.168.1.255\nDe första 24 bitarna behålls, resten sätts till 1.',
    category: 'Subnätberäkning',
    difficulty: 'medium'
  },
  {
    id: 't1-15',
    front: 'Vilka IP-adresser är privata (RFC 1918)?',
    back: '• 10.0.0.0/8 (Klass A)\n• 172.16.0.0/12 (Klass B)\n• 192.168.0.0/16 (Klass C)',
    category: 'Reserverade adresser',
    difficulty: 'medium'
  },
  {
    id: 't1-16',
    front: 'Vad är default gateway?',
    back: 'Routern som hanterar trafik till nätverk utanför det lokala subnätet. Typiskt första eller sista användbara IP i subnätet.',
    category: 'Nätverkskoncept',
    difficulty: 'medium'
  },
  {
    id: 't1-17',
    front: 'Hur många hosts i ett /30 nätverk?',
    back: '2 hosts\n2^(32-30) - 2 = 2^2 - 2 = 4 - 2 = 2\nAnvänds för punkt-till-punkt-länkar.',
    category: 'Subnätberäkning',
    difficulty: 'medium'
  },
  {
    id: 't1-18',
    front: 'Kommando för att se subnätinformation med beräkningar?',
    back: 'ipcalc <ip/prefix>\nEx: ipcalc 192.168.1.100/24',
    category: 'Kommandon',
    difficulty: 'medium'
  },
  {
    id: 't1-19',
    front: 'Vad var Klass A nätverk enligt gamla IP-klasserna?',
    back: 'Första oktett: 1-126\nDefault mask: 255.0.0.0 (/8)\nStor mängd hosts per nätverk.',
    category: 'IP-klasser',
    difficulty: 'medium'
  },
  {
    id: 't1-20',
    front: 'Vad var Klass C nätverk enligt gamla IP-klasserna?',
    back: 'Första oktett: 192-223\nDefault mask: 255.255.255.0 (/24)\nSmå nätverk med max 254 hosts.',
    category: 'IP-klasser',
    difficulty: 'medium'
  },
  {
    id: 't1-21',
    front: 'Vad gör kommandot traceroute?',
    back: 'Visar vägen (alla hopp/routrar) som paket tar för att nå en destination.\ntraceroute google.com',
    category: 'Kommandon',
    difficulty: 'medium'
  },
  {
    id: 't1-22',
    front: 'Formel för antal hosts i ett subnät?',
    back: '2^(32 - prefix) - 2\n\nEx /24: 2^(32-24) - 2 = 2^8 - 2 = 254\n-2 för nätverks- och broadcast-adress',
    category: 'Subnätberäkning',
    difficulty: 'medium'
  },
  // Hard (8)
  {
    id: 't1-23',
    front: 'Givet 10.0.0.0/8 - vad är broadcast-adressen?',
    back: '10.255.255.255\nEndast första oktetten är nätverksdel, resten (3 oktetter) blir 255.',
    category: 'Subnätberäkning',
    difficulty: 'hard'
  },
  {
    id: 't1-24',
    front: 'Du behöver 500 hosts. Vilken prefix-längd krävs minst?',
    back: '/23 (510 hosts)\n2^9 - 2 = 510 hosts\n/24 ger bara 254 hosts (för lite)',
    category: 'Subnätberäkning',
    difficulty: 'hard'
  },
  {
    id: 't1-25',
    front: 'Vad är 172.16.0.0/12 i subnätmask-format?',
    back: '255.240.0.0\nBinärt: 11111111.11110000.00000000.00000000\n(12 ettor)',
    category: 'CIDR',
    difficulty: 'hard'
  },
  {
    id: 't1-26',
    front: 'Kan två enheter på 192.168.1.50/24 och 192.168.2.50/24 kommunicera direkt?',
    back: 'NEJ - de är i olika subnät.\n192.168.1.0 vs 192.168.2.0\nKräver router för kommunikation.',
    category: 'Nätverkskoncept',
    difficulty: 'hard'
  },
  {
    id: 't1-27',
    front: 'Dela upp 192.168.1.0/24 i 4 lika stora subnät - vilka prefix får de?',
    back: '/26 (64 adresser per subnät)\n• 192.168.1.0/26\n• 192.168.1.64/26\n• 192.168.1.128/26\n• 192.168.1.192/26',
    category: 'Subnätberäkning',
    difficulty: 'hard'
  },
  {
    id: 't1-28',
    front: 'Vad är skillnaden mellan NAT och PAT?',
    back: 'NAT: Network Address Translation - mappar privata till publika IP:n.\nPAT: Port Address Translation - flera privata IP:n delar EN publik IP via olika portar.',
    category: 'Nätverkskoncept',
    difficulty: 'hard'
  },
  {
    id: 't1-29',
    front: 'Vad är VLSM och varför används det?',
    back: 'Variable Length Subnet Masking - tillåter olika subnätstorlekar i samma nätverk för effektivare IP-användning.',
    category: 'Subnätberäkning',
    difficulty: 'hard'
  },
  {
    id: 't1-30',
    front: 'Givet 10.20.30.40/22 - vad är nätverksadressen?',
    back: '10.20.28.0\n/22 = 255.255.252.0\n30 & 252 = 28 (tredje oktetten)',
    category: 'Subnätberäkning',
    difficulty: 'hard'
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
    difficulty: 'easy'
  },
  {
    id: 't2-2',
    front: 'Var lagras systemkonfigurationsfiler i Linux?',
    back: '/etc\nInnehåller konfigurationsfiler som passwd, shadow, fstab, hosts, ssh/',
    category: 'Viktiga kataloger',
    difficulty: 'easy'
  },
  {
    id: 't2-3',
    front: 'Var finns användarnas hemkataloger?',
    back: '/home\nVarje användare har /home/användarnamn (utom root som har /root)',
    category: 'Viktiga kataloger',
    difficulty: 'easy'
  },
  {
    id: 't2-4',
    front: 'Var lagras systemloggar i Linux?',
    back: '/var/log\nInnehåller syslog, auth.log, kern.log, messages, etc.',
    category: 'Viktiga kataloger',
    difficulty: 'easy'
  },
  {
    id: 't2-5',
    front: 'Vad är FHS?',
    back: 'Filesystem Hierarchy Standard\nStandard som definierar katalogstrukturen i Linux/Unix.',
    category: 'FHS Grunder',
    difficulty: 'easy'
  },
  {
    id: 't2-6',
    front: 'Kommando för att lista alla filer (inklusive dolda) med detaljer?',
    back: 'ls -la\n-l = lång format, -a = alla (inklusive dolda filer som börjar med .)',
    category: 'Kommandon',
    difficulty: 'easy'
  },
  {
    id: 't2-7',
    front: 'Vad innehåller /tmp?',
    back: 'Temporära filer som rensas vid omstart.\nAlla användare kan skriva här.',
    category: 'Viktiga kataloger',
    difficulty: 'easy'
  },
  {
    id: 't2-8',
    front: 'Vad innehåller /bin och /sbin?',
    back: '/bin: Grundläggande användarkommandon (ls, cp, mv)\n/sbin: Systemadministrationskommandon (fdisk, iptables)',
    category: 'Viktiga kataloger',
    difficulty: 'easy'
  },
  {
    id: 't2-9',
    front: 'Kommando för att visa nuvarande arbetskatalog?',
    back: 'pwd\n(Print Working Directory)',
    category: 'Kommandon',
    difficulty: 'easy'
  },
  {
    id: 't2-10',
    front: 'Skillnad mellan absolut och relativ sökväg?',
    back: 'Absolut: Börjar från / (t.ex. /etc/ssh/sshd_config)\nRelativ: Utgår från nuvarande katalog (t.ex. ../lib)',
    category: 'Navigation',
    difficulty: 'easy'
  },
  // Medium (12)
  {
    id: 't2-11',
    front: 'Vilka 7 filtyper finns i Linux? (visa med ls -l)',
    back: '- : Vanlig fil\nd : Katalog\nl : Symbolisk länk\nc : Character device\nb : Block device\ns : Socket\np : Named pipe (FIFO)',
    category: 'Filtyper',
    difficulty: 'medium'
  },
  {
    id: 't2-12',
    front: 'Vad innehåller /proc?',
    back: 'Virtuellt filsystem med processinformation och systemstatus.\nFiler som /proc/cpuinfo, /proc/meminfo, /proc/[pid]/',
    category: 'Viktiga kataloger',
    difficulty: 'medium'
  },
  {
    id: 't2-13',
    front: 'Vad är /dev och vad innehåller den?',
    back: 'Device-filer - representerar hårdvara.\nEx: /dev/sda (disk), /dev/tty (terminal), /dev/null, /dev/zero',
    category: 'Viktiga kataloger',
    difficulty: 'medium'
  },
  {
    id: 't2-14',
    front: 'Vad är skillnaden mellan /bin och /usr/bin?',
    back: '/bin: Essentiella kommandon för boot och single-user mode\n/usr/bin: Icke-essentiella användarprogram',
    category: 'FHS Grunder',
    difficulty: 'medium'
  },
  {
    id: 't2-15',
    front: 'Kommando för att hitta filer efter namn?',
    back: 'find <sökväg> -name "mönster"\nEx: find /etc -name "*.conf"',
    category: 'Kommandon',
    difficulty: 'medium'
  },
  {
    id: 't2-16',
    front: 'Vad gör kommandot df -h?',
    back: 'Visar diskutrymme per filsystem i human-readable format.\n-h = storlekar som KB, MB, GB',
    category: 'Kommandon',
    difficulty: 'medium'
  },
  {
    id: 't2-17',
    front: 'Vad gör kommandot du -sh?',
    back: 'Visar total storlek på en katalog.\n-s = summary (total), -h = human-readable',
    category: 'Kommandon',
    difficulty: 'medium'
  },
  {
    id: 't2-18',
    front: 'Vad innehåller filen /etc/passwd?',
    back: 'Användarinformation:\nusername:x:UID:GID:GECOS:home:shell\n(x = lösenord i shadow)',
    category: 'Konfigurationsfiler',
    difficulty: 'medium'
  },
  {
    id: 't2-19',
    front: 'Vad innehåller filen /etc/fstab?',
    back: 'Filsystem som ska monteras vid boot.\nFormat: device mountpoint fstype options dump pass',
    category: 'Konfigurationsfiler',
    difficulty: 'medium'
  },
  {
    id: 't2-20',
    front: 'Vad är /opt för katalog?',
    back: 'Optional - för tredjepartsprogram som inte följer FHS.\nEx: /opt/google/chrome',
    category: 'Viktiga kataloger',
    difficulty: 'medium'
  },
  {
    id: 't2-21',
    front: 'Skillnad mellan locate och find?',
    back: 'locate: Snabb sökning i databas (uppdateras med updatedb)\nfind: Realtidssökning, långsammare men alltid aktuell',
    category: 'Kommandon',
    difficulty: 'medium'
  },
  {
    id: 't2-22',
    front: 'Vad gör kommandot tree?',
    back: 'Visar katalogstruktur som träd.\ntree -L 2 = max 2 nivåer djupt',
    category: 'Kommandon',
    difficulty: 'medium'
  },
  // Hard (8)
  {
    id: 't2-23',
    front: 'Vad är skillnaden mellan /dev/null och /dev/zero?',
    back: '/dev/null: Slänger all data (svart hål)\n/dev/zero: Producerar oändligt med nollor (för att skapa tomma filer)',
    category: 'Device-filer',
    difficulty: 'hard'
  },
  {
    id: 't2-24',
    front: 'Vad är en inode och vad innehåller den?',
    back: 'Datastruktur med metadata om en fil:\n• Filtyp och rättigheter\n• Ägare/grupp\n• Storlek\n• Tidsmarkörer\n• Pekare till datablockFiler, EJ filnamnet!',
    category: 'Filsystem internals',
    difficulty: 'hard'
  },
  {
    id: 't2-25',
    front: 'Skillnad mellan hård och symbolisk länk?',
    back: 'Hård länk: Samma inode, fungerar om original tas bort\nSymbolisk länk: Pekare till filnamn, bryts om original tas bort',
    category: 'Filtyper',
    difficulty: 'hard'
  },
  {
    id: 't2-26',
    front: 'Vad gör sticky bit på en katalog?',
    back: 'Endast filägaren (och root) kan ta bort filer.\nAnvänds på /tmp för att skydda andras filer.\nSätts med chmod +t',
    category: 'Rättigheter',
    difficulty: 'hard'
  },
  {
    id: 't2-27',
    front: 'Vad innehåller /sys?',
    back: 'Virtuellt filsystem (sysfs) som exponerar kernel-information.\nEnhetsinformation, drivrutiner, bus-information.',
    category: 'Viktiga kataloger',
    difficulty: 'hard'
  },
  {
    id: 't2-28',
    front: 'Hur hittar du vilket paket som äger en fil? (Debian/Ubuntu)',
    back: 'dpkg -S /sökväg/till/fil\nEx: dpkg -S /usr/bin/ls\nSvar: coreutils: /usr/bin/ls',
    category: 'Kommandon',
    difficulty: 'hard'
  },
  {
    id: 't2-29',
    front: 'Vad är mount och hur används det?',
    back: 'Kopplar ett filsystem till en katalog.\nmount /dev/sdb1 /mnt/usb\numount /mnt/usb för att koppla bort',
    category: 'Kommandon',
    difficulty: 'hard'
  },
  {
    id: 't2-30',
    front: 'Vad visar lsblk?',
    back: 'Lista över block-enheter (diskar, partitioner).\nVisar namn, storlek, typ, mountpoint.',
    category: 'Kommandon',
    difficulty: 'hard'
  }
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
