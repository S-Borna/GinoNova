/**
 * TENTAISH EXPANSION - 200 NYA QUIZ-FRÅGOR
 * Moment 4: Subnetting & Nätverk
 *
 * Skapad: 2026-01-06
 */

import { TentaishQuestion } from './tentaish-quiz'

// =============================================================================
// MOMENT 4: SUBNETTING & NÄTVERK - NYA FRÅGOR (30 st)
// =============================================================================

export const SUBNETTING_EXTRA: TentaishQuestion[] = [
    {
        id: 'tent-subnet-ex-1',
        question: 'Hur många bitar har en IPv4-adress?',
        options: ['16', '32', '64', '128'],
        correctIndex: 1,
        explanation: 'IPv4 = 32 bitar, skrivs som 4 oktetter (8 bitar var). IPv6 = 128 bitar.',
        difficulty: 'G',
        category: 'IP Grundläggande'
    },
    {
        id: 'tent-subnet-ex-2',
        question: 'Vad är en subnätmask?',
        options: [
            'En säkerhetsfunktion',
            'Definierar vilken del av IP-adressen som är nätverk vs host',
            'En routing-tabell',
            'En DNS-inställning'
        ],
        correctIndex: 1,
        explanation: 'Subnätmasken separerar nätverksdelen (1:or) från hostdelen (0:or) i IP-adressen.',
        difficulty: 'G',
        category: 'Subnetting Grundläggande'
    },
    {
        id: 'tent-subnet-ex-3',
        question: 'Vad betyder /24 i CIDR-notation?',
        options: [
            '24 hosts',
            '24 bitar för nätverksdelen (255.255.255.0)',
            '24 nätverk',
            '24 bytes'
        ],
        correctIndex: 1,
        explanation: '/24 = 24 nätverksbitar = 255.255.255.0. Ger 256 adresser, 254 användbara hosts.',
        difficulty: 'G',
        category: 'CIDR'
    },
    {
        id: 'tent-subnet-ex-4',
        question: 'Hur många användbara hostadresser finns i ett /24-nätverk?',
        options: ['256', '255', '254', '252'],
        correctIndex: 2,
        explanation: '256 totalt minus 1 för nätverksadress minus 1 för broadcast = 254 användbara.',
        difficulty: 'G',
        category: 'Subnetting Beräkningar'
    },
    {
        id: 'tent-subnet-ex-5',
        question: 'Vad är nätverksadressen för 192.168.1.50/24?',
        options: ['192.168.1.0', '192.168.1.50', '192.168.1.1', '192.168.1.255'],
        correctIndex: 0,
        explanation: '/24 betyder att de första 24 bitarna är nätverket. Hostdelen nollställs = .0.',
        difficulty: 'G',
        category: 'Subnetting Beräkningar'
    },
    {
        id: 'tent-subnet-ex-6',
        question: 'Vad är broadcast-adressen för 192.168.1.0/24?',
        options: ['192.168.1.0', '192.168.1.1', '192.168.1.254', '192.168.1.255'],
        correctIndex: 3,
        explanation: 'Broadcast har alla hostbitar satta till 1. I /24 blir det .255.',
        difficulty: 'G',
        category: 'Subnetting Beräkningar'
    },
    {
        id: 'tent-subnet-ex-7',
        question: 'Vilken subnätmask motsvarar /16?',
        options: ['255.0.0.0', '255.255.0.0', '255.255.255.0', '255.255.255.128'],
        correctIndex: 1,
        explanation: '/16 = 16 bitar nätverk = 255.255.0.0. Kallas också Class B-mask.',
        difficulty: 'G',
        category: 'CIDR'
    },
    {
        id: 'tent-subnet-ex-8',
        question: 'Hur många /24-subnät kan du skapa från ett /22-nätverk?',
        options: ['2', '4', '8', '16'],
        correctIndex: 1,
        explanation: '/22 till /24 = 2 extra bitar = 2² = 4 subnät. Varje /24 har 254 hosts.',
        difficulty: 'VG',
        category: 'Subnetting Beräkningar'
    },
    {
        id: 'tent-subnet-ex-9',
        question: 'Vilket privat IP-område används oftast för hemmanätverk?',
        options: [
            '10.0.0.0/8',
            '192.168.0.0/16',
            '172.16.0.0/12',
            '169.254.0.0/16'
        ],
        correctIndex: 1,
        explanation: '192.168.x.x är vanligast hemma. 10.x.x.x för stora företag. 172.16-31.x.x också privat.',
        difficulty: 'G',
        category: 'Privata IP'
    },
    {
        id: 'tent-subnet-ex-10',
        question: 'Vad är 127.0.0.1?',
        options: [
            'Default gateway',
            'Localhost/loopback-adress',
            'Broadcast-adress',
            'DNS-server'
        ],
        correctIndex: 1,
        explanation: '127.0.0.1 är loopback - trafik till dig själv. localhost i /etc/hosts.',
        difficulty: 'G',
        category: 'Speciella Adresser'
    },
    {
        id: 'tent-subnet-ex-11',
        question: 'Hur många användbara hosts finns i ett /30-nätverk?',
        options: ['4', '3', '2', '1'],
        correctIndex: 2,
        explanation: '/30 = 4 adresser. Minus nätverksadress och broadcast = 2. Används för point-to-point.',
        difficulty: 'VG',
        category: 'Subnetting Beräkningar'
    },
    {
        id: 'tent-subnet-ex-12',
        question: 'Vilken klass tillhör IP-adressen 172.16.5.1?',
        options: ['Klass A', 'Klass B', 'Klass C', 'Klass D'],
        correctIndex: 1,
        explanation: 'Klass B: 128-191.x.x.x. 172.16.0.0/12 är dessutom privat IP-range.',
        difficulty: 'G',
        category: 'IP-klasser'
    },
    {
        id: 'tent-subnet-ex-13',
        question: 'Vad är NAT?',
        options: [
            'Network Allocation Table',
            'Network Address Translation - översätter privata IP till publika',
            'Network Authentication Token',
            'Network Audit Tool'
        ],
        correctIndex: 1,
        explanation: 'NAT gör att flera privata IP-adresser delar en publik IP. Din router gör detta.',
        difficulty: 'G',
        category: 'NAT'
    },
    {
        id: 'tent-subnet-ex-14',
        question: 'Vad är default gateway?',
        options: [
            'DNS-server',
            'Routern som hanterar trafik till andra nätverk',
            'DHCP-server',
            'Broadcast-adress'
        ],
        correctIndex: 1,
        explanation: 'Gateway är routern. All trafik som inte är lokal skickas till default gateway.',
        difficulty: 'G',
        category: 'Routing'
    },
    {
        id: 'tent-subnet-ex-15',
        question: 'Hur visar du IP-konfiguration i Linux?',
        options: [
            'ifconfig (deprecated) eller ip addr',
            'ipconfig',
            'netstat -ip',
            'show ip'
        ],
        correctIndex: 0,
        explanation: 'ip addr är modern. ifconfig är äldre men finns ofta. ipconfig är Windows.',
        difficulty: 'G',
        category: 'Linux Nätverk'
    },
    {
        id: 'tent-subnet-ex-16',
        question: 'Vad gör kommandot "ip route"?',
        options: [
            'Visar IP-adresser',
            'Visar routing-tabellen',
            'Testar nätverk',
            'Konfigurerar IP'
        ],
        correctIndex: 1,
        explanation: 'ip route visar hur trafik ska skickas. default via X.X.X.X är din gateway.',
        difficulty: 'G',
        category: 'Linux Nätverk'
    },
    {
        id: 'tent-subnet-ex-17',
        question: 'Vad är DHCP?',
        options: [
            'Dynamic Host Configuration Protocol - tilldelar IP automatiskt',
            'Disk Host Control Protocol',
            'Data Handling Control Process',
            'Domain Host Control Protocol'
        ],
        correctIndex: 0,
        explanation: 'DHCP-server tilldelar IP, gateway, DNS automatiskt. Alternativ: statisk IP-config.',
        difficulty: 'G',
        category: 'DHCP'
    },
    {
        id: 'tent-subnet-ex-18',
        question: 'Vilken port använder DNS?',
        options: ['22', '25', '53', '80'],
        correctIndex: 2,
        explanation: 'DNS använder port 53 (UDP för queries, TCP för zonöverföringar). SSH=22, HTTP=80.',
        difficulty: 'G',
        category: 'Portar'
    },
    {
        id: 'tent-subnet-ex-19',
        question: 'Vad gör "ping"?',
        options: [
            'Testar DNS',
            'Skickar ICMP echo request för att testa nätverksanslutning',
            'Visar routing',
            'Scannar portar'
        ],
        correctIndex: 1,
        explanation: 'ping testar om host svarar. Visar latency (ms). ICMP kan vara blockerat av brandvägg.',
        difficulty: 'G',
        category: 'Diagnostik'
    },
    {
        id: 'tent-subnet-ex-20',
        question: 'Vad gör "traceroute" (tracert på Windows)?',
        options: [
            'Spårar filer',
            'Visar vägen (hopp) som paket tar till destinationen',
            'Testar hastighet',
            'Spårar användare'
        ],
        correctIndex: 1,
        explanation: 'Traceroute visar varje router på vägen med latency. Bra för att hitta flaskhalsar.',
        difficulty: 'G',
        category: 'Diagnostik'
    },
    {
        id: 'tent-subnet-ex-21',
        question: 'Om du har 192.168.10.0/25, vad är sista användbara host-adressen?',
        options: ['192.168.10.127', '192.168.10.126', '192.168.10.128', '192.168.10.125'],
        correctIndex: 1,
        explanation: '/25 = 128 adresser (0-127). .127 är broadcast, så .126 är sista host.',
        difficulty: 'VG',
        category: 'Subnetting Beräkningar'
    },
    {
        id: 'tent-subnet-ex-22',
        question: 'Vad är skillnaden mellan TCP och UDP?',
        options: [
            'TCP är snabbare',
            'TCP är anslutningsorienterat med felhantering, UDP är snabbare utan garantier',
            'UDP är säkrare',
            'Ingen skillnad'
        ],
        correctIndex: 1,
        explanation: 'TCP: pålitlig, ordnad leverans. UDP: snabbare, ingen garanti. DNS/streaming=UDP, HTTP/SSH=TCP.',
        difficulty: 'G',
        category: 'Protokoll'
    },
    {
        id: 'tent-subnet-ex-23',
        question: 'Vad visar "ss -tuln"?',
        options: [
            'System status',
            'Lyssnade TCP/UDP-portar på systemet',
            'Användarsessioner',
            'Nätverksstatistik'
        ],
        correctIndex: 1,
        explanation: 'ss = socket statistics. -t TCP, -u UDP, -l listening, -n numeriskt. Ersätter netstat.',
        difficulty: 'G',
        category: 'Linux Nätverk'
    },
    {
        id: 'tent-subnet-ex-24',
        question: 'Vad är VLAN?',
        options: [
            'Virtual Local Area Network - logisk nätverkssegmentering',
            'Very Large Area Network',
            'Virtual Link Access Node',
            'Verified LAN'
        ],
        correctIndex: 0,
        explanation: 'VLAN segmenterar ett fysiskt nätverk i logiska subnät. Kräver switch-stöd.',
        difficulty: 'VG',
        category: 'VLAN'
    },
    {
        id: 'tent-subnet-ex-25',
        question: 'Vilken fil konfigurerar DNS-servrar i Linux?',
        options: [
            '/etc/dns.conf',
            '/etc/resolv.conf',
            '/etc/dns/resolv',
            '/etc/network/dns'
        ],
        correctIndex: 1,
        explanation: '/etc/resolv.conf innehåller nameserver-rader. Kan överskrivas av NetworkManager.',
        difficulty: 'G',
        category: 'DNS'
    },
    {
        id: 'tent-subnet-ex-26',
        question: 'Vad är ARP?',
        options: [
            'Address Resolution Protocol - mappar IP till MAC-adress',
            'Automatic Routing Protocol',
            'Advanced Relay Protocol',
            'Authentication Request Protocol'
        ],
        correctIndex: 0,
        explanation: 'ARP hittar MAC-adress för en IP på lokala nätverket. arp -a visar ARP-cache.',
        difficulty: 'VG',
        category: 'Protokoll'
    },
    {
        id: 'tent-subnet-ex-27',
        question: 'Hur beräknar du antal hosts i ett subnät?',
        options: [
            '2^nätverksbitar',
            '2^hostbitar - 2',
            '2^hostbitar',
            '2^(32-prefix)'
        ],
        correctIndex: 1,
        explanation: '2^hostbitar ger totalt. Minus 2 för nätverksadress och broadcast = användbara hosts.',
        difficulty: 'G',
        category: 'Subnetting Beräkningar'
    },
    {
        id: 'tent-subnet-ex-28',
        question: 'Vad är ett /31-nätverk används för?',
        options: [
            'Stora nätverk',
            'Point-to-point-länkar (2 adresser, ingen broadcast)',
            'Broadcast-domäner',
            'Används inte'
        ],
        correctIndex: 1,
        explanation: '/31 ger exakt 2 adresser utan "slöseri". RFC 3021 för point-to-point-länkar.',
        difficulty: 'VG',
        category: 'Subnetting Avancerat'
    },
    {
        id: 'tent-subnet-ex-29',
        question: 'Om du delar 10.0.0.0/8 i /16-subnät, hur många subnät får du?',
        options: ['256', '512', '128', '65536'],
        correctIndex: 0,
        explanation: '/8 till /16 = 8 extra bitar = 2⁸ = 256 subnät. Varje /16 har 65534 hosts.',
        difficulty: 'VG',
        category: 'Subnetting Beräkningar'
    },
    {
        id: 'tent-subnet-ex-30',
        question: 'Vad är APIPA-adressen (169.254.x.x)?',
        options: [
            'Privat IP-range',
            'Automatisk adress när DHCP misslyckas (link-local)',
            'Broadcast-range',
            'Multicast-range'
        ],
        correctIndex: 1,
        explanation: '169.254.0.0/16 tilldelas automatiskt om ingen DHCP-server hittas. Fungerar endast lokalt.',
        difficulty: 'VG',
        category: 'Speciella Adresser'
    }
]
