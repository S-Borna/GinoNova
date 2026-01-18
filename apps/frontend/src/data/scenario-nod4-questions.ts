/**
 * NOD 4: Nätverk & Server - SCENARIO Questions
 * 20 verklighetstrogna scenariofrågor
 */

import type { Omtenta2Question } from './omtenta-2.0-quiz'

export const SCENARIO_NOD4_QUESTIONS: Omtenta2Question[] = [
    {
        id: 'nod4-s1',
        question: 'Din kollega frågar: "Vi har subnät 10.0.50.0/27, hur många IoT-enheter kan vi ha där max?". Vad svarar du?',
        options: ['32 enheter', '30 enheter', '16 enheter', '62 enheter'],
        correctIndices: [1],
        explanation: '/27 = 32-27 = 5 hostbitar. 2^5 = 32 adresser - 2 (network + broadcast) = 30 hosts.',
        difficulty: 'VG',
        category: 'Subnetting',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s2',
        question: 'Erik ringer: "Jag kör en webserver på localhost:3000 på min laptop. Kan du testa den?". Vad svarar du?',
        options: ['Skicka mig din IP så ansluter jag', 'Det går inte - localhost är bara lokalt', 'Öppna port 3000 i din brandvägg', 'Kör dig mot 127.0.0.1:3000'],
        correctIndices: [1],
        explanation: 'localhost (127.0.0.1) är per definition bara tillgänglig på samma maskin. Erik måste binda till 0.0.0.0.',
        difficulty: 'G',
        category: 'Localhost',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s3',
        question: 'Du får larmet "Disk almost full på prod!". Du SSH:ar in och behöver se ledigt utrymme snabbt. Kommando?',
        options: ['du -h /', 'df -h', 'space --check', 'ls -la /'],
        correctIndices: [1],
        explanation: 'df -h (disk free, human readable) visar ledigt utrymme per filsystem. du visar användning per katalog.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s4',
        question: 'Du behöver kolla vilka portar som lyssnar på servern. Vilket kommando?',
        options: ['netstat -tulpn', 'ss -tulpn', 'ports --list', 'Både A och B fungerar'],
        correctIndices: [3],
        explanation: 'ss (socket statistics) ersätter netstat men båda fungerar. -tulpn = tcp/udp/listening/process/numeric.',
        difficulty: 'G',
        category: 'Portar',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s5',
        question: 'Webappen kan inte nå databasen på db.internal.com. Du vill testa DNS-upplösning. Kommando?',
        options: ['ping db.internal.com', 'nslookup db.internal.com', 'dig db.internal.com', 'Alla testar DNS'],
        correctIndices: [3],
        explanation: 'Alla slår upp DNS. nslookup/dig ger mer DNS-detaljer. ping testar också nätverksanslutning efter DNS.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s6',
        question: 'Du ser att port 443 redan används men nginx startar inte. Hur tar du reda på vilken process som använder porten?',
        options: ['ps aux | grep 443', 'lsof -i :443', 'netstat 443', 'port --check 443'],
        correctIndices: [1],
        explanation: 'lsof -i :PORT visar vilken process som använder en port. Visa info om PID, user, command.',
        difficulty: 'G',
        category: 'Portar',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s7',
        question: 'Din server har IP 192.168.1.50/24. Vilken är broadcast-adressen för nätverket?',
        options: ['192.168.1.0', '192.168.1.1', '192.168.1.255', '192.168.1.254'],
        correctIndices: [2],
        explanation: '/24 = första 24 bitar är nät. 192.168.1.x där x=255 (alla host-bitar 1) är broadcast.',
        difficulty: 'VG',
        category: 'Subnetting',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s8',
        question: 'Du vill testa om port 22 är öppen på server 10.0.0.5. Vilket kommando?',
        options: ['ping 10.0.0.5:22', 'nc -zv 10.0.0.5 22', 'telnet 10.0.0.5 22', 'Både B och C fungerar'],
        correctIndices: [3],
        explanation: 'nc (netcat) och telnet kan testa TCP-portar. ping testar bara ICMP, inte specifika portar.',
        difficulty: 'G',
        category: 'Nätverkstest',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s9',
        question: 'Vilken standardport använder SSH?',
        options: ['21', '22', '23', '25'],
        correctIndices: [1],
        explanation: 'SSH = port 22. FTP=21, Telnet=23, SMTP=25. Viktigt att kunna standardportar!',
        difficulty: 'G',
        category: 'Portar',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s10',
        question: 'Du behöver öppna port 80 i Ubuntu-brandväggen. Vilket kommando?',
        options: ['ufw allow 80/tcp', 'iptables -A INPUT -p tcp --dport 80', 'firewall-cmd --add-port=80/tcp', 'Alla kan funka beroende på distro'],
        correctIndices: [0],
        explanation: 'ufw (Uncomplicated Firewall) är Ubuntu/Debians standard-brandvägg. "ufw allow 80/tcp" öppnar port 80 för TCP-trafik. firewall-cmd används på RHEL/Fedora, iptables är low-level.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s11',
        question: 'Du kör `ip addr` och ser "inet 192.168.1.50/24 brd 192.168.1.255". Vad är "brd"?',
        options: ['Board - nätverkskortsnamn', 'Broadcast-adress', 'Bridge-adress', 'Band - hastighet'],
        correctIndices: [1],
        explanation: 'brd = broadcast address. Paket till denna adress skickas till alla hosts på samma subnät.',
        difficulty: 'G',
        category: 'IP-konfiguration',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s12',
        question: 'Du behöver permanent DNS-server 8.8.8.8. På Ubuntu/Debian, var konfigurerar du detta?',
        options: ['/etc/dns.conf', '/etc/resolv.conf (eller netplan)', '/etc/network/dns', '/var/dns/servers'],
        correctIndices: [1],
        explanation: '/etc/resolv.conf innehåller DNS-servrar. Moderna system använder netplan/systemd-resolved som genererar den.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s13',
        question: 'UDP och TCP - vilken är connectionless och används för t.ex. DNS-queries och streaming?',
        options: ['TCP', 'UDP', 'Båda', 'Ingen av dem'],
        correctIndices: [1],
        explanation: 'UDP är connectionless (fire-and-forget). TCP har handshake och garanterar leverans. DNS, video, VoIP använder ofta UDP.',
        difficulty: 'G',
        category: 'Protokoll',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s14',
        question: 'Du tracear vägen till google.com och vill se vilka routers paketen passerar. Kommando?',
        options: ['ping -t google.com', 'traceroute google.com', 'route google.com', 'path google.com'],
        correctIndices: [1],
        explanation: 'traceroute visar varje hopp (router) på vägen till destinationen med latens för varje.',
        difficulty: 'G',
        category: 'Nätverkstest',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s15',
        question: 'Du vill se routing-tabellen på din Linux-server. Kommando?',
        options: ['ip route', 'route -n', 'netstat -rn', 'Alla fungerar'],
        correctIndices: [3],
        explanation: 'ip route är modernast. route -n och netstat -rn är äldre men fungerar. Visar hur paket routas.',
        difficulty: 'VG',
        category: 'Routing',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s16',
        question: 'Vilken fil används för lokal host-till-IP mappning innan DNS kontaktas?',
        options: ['/etc/dns', '/etc/hosts', '/etc/hostname', '/etc/resolv.conf'],
        correctIndices: [1],
        explanation: '/etc/hosts kollas först (per default). Där kan du mappa hostname till IP lokalt utan DNS.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s17',
        question: 'Privata IP-intervall - vilken av dessa är INTE ett privat nätverk?',
        options: ['10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16', '8.8.8.0/24'],
        correctIndices: [3],
        explanation: 'Privata: 10.x.x.x, 172.16-31.x.x, 192.168.x.x. 8.8.8.x är publikt (Google DNS).',
        difficulty: 'VG',
        category: 'IP-adresser',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s18',
        question: 'Du vill ladda ner en fil från webben via kommandoraden. Vilket kommando?',
        options: ['download file.tar.gz', 'wget https://example.com/file.tar.gz', 'curl -O https://example.com/file.tar.gz', 'Både B och C fungerar'],
        correctIndices: [3],
        explanation: 'wget och curl är båda populära. wget sparar default, curl -O behövs för att spara med originalnamn.',
        difficulty: 'G',
        category: 'Verktyg',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s19',
        question: 'OSI-modellens lager 4 (Transport) - vilka protokoll finns där?',
        options: ['HTTP, FTP', 'TCP, UDP', 'IP, ICMP', 'Ethernet, Wi-Fi'],
        correctIndices: [1],
        explanation: 'Layer 4 = Transport: TCP och UDP. Layer 7 = Application (HTTP). Layer 3 = Network (IP). Layer 2 = Data Link (Ethernet).',
        difficulty: 'VG',
        category: 'OSI',
        topic: 'nod4-natverk',
        type: 'scenario'
    },
    {
        id: 'nod4-s20',
        question: 'En IPv4-adress består av hur många bitar, fördelade på hur många bytes/oktetter?',
        options: ['16 bitar, 2 bytes', '32 bitar, 4 bytes', '64 bitar, 8 bytes', '48 bitar, 6 bytes'],
        correctIndices: [1],
        explanation: 'IPv4 = 32 bitar = 4 bytes. Varje byte visas som 0-255 (t.ex. 192.168.1.1). IPv6 = 128 bitar.',
        difficulty: 'G',
        category: 'IP-adresser',
        topic: 'nod4-natverk',
        type: 'scenario'
    }
]
