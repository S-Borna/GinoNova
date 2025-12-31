/**
 * DOE25 Tentaplugg - Task-specifika Quiz
 * 20 quiz per task, pedagogiskt fokuserade med variation i rätt svar (A-D)
 */

export interface TaskQuizQuestion {
  id: string
  question: string
  options: [string, string, string, string] // A, B, C, D
  correctIndex: 0 | 1 | 2 | 3 // 0=A, 1=B, 2=C, 3=D
  explanation: string
  difficulty: 'G' | 'VG'
  category: string
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
