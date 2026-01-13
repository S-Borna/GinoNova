import { OmtentaV2Question } from './omtenta-v2-ssh-brandvagg'

export const SUBNETTING_NATVERK_V2_QUESTIONS: OmtentaV2Question[] = [
    {
        id: 'omtenta-v2-subnet-1',
        question: 'An IPv4 address has...',
        options: ['24 bits', '32 bits', '48 bits', '64 bits'],
        correctIndices: [1],
        explanation: 'An IPv4 address consists of 32 bits, divided into 4 octets of 8 bits each.',
        difficulty: 'G',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-2',
        question: 'An IPv4 address has...',
        options: ['3 bytes', '4 bytes', '6 bytes', '8 bytes'],
        correctIndices: [1],
        explanation: 'An IPv4 address has 4 bytes (32 bits / 8 = 4 bytes).',
        difficulty: 'G',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-3',
        question: 'An IPv6 address has...',
        options: ['32 bits', '64 bits', '128 bits', '256 bits'],
        correctIndices: [2],
        explanation: 'An IPv6 address consists of 128 bits, much larger than IPv4 to support more addresses.',
        difficulty: 'G',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-4',
        question: 'How many hosts in /24?',
        options: ['256', '254', '252', '128'],
        correctIndices: [1],
        explanation: 'A /24 network has 2^8 - 2 = 254 usable hosts (subtract network and broadcast addresses).',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-5',
        question: 'How many hosts in /25?',
        options: ['128', '126', '64', '62'],
        correctIndices: [1],
        explanation: 'A /25 network has 2^7 - 2 = 126 usable hosts.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-6',
        question: 'How many hosts in /26?',
        options: ['64', '62', '32', '30'],
        correctIndices: [1],
        explanation: 'A /26 network has 2^6 - 2 = 62 usable hosts.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-7',
        question: 'How many hosts in /28?',
        options: ['16', '14', '8', '6'],
        correctIndices: [1],
        explanation: 'A /28 network has 2^4 - 2 = 14 usable hosts.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-8',
        question: 'How many hosts in /29?',
        options: ['8', '6', '4', '2'],
        correctIndices: [1],
        explanation: 'A /29 network has 2^3 - 2 = 6 usable hosts.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-9',
        question: 'How many hosts in /30?',
        options: ['4', '2', '1', '0'],
        correctIndices: [1],
        explanation: 'A /30 network has 2^2 - 2 = 2 usable hosts, commonly used for point-to-point links.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-10',
        question: 'Why subtract 2 from host count?',
        options: ['For DNS and DHCP', 'For gateway and DNS', 'For network and broadcast', 'For router and switch'],
        correctIndices: [2],
        explanation: 'We subtract 2 because the network address (first) and broadcast address (last) cannot be assigned to hosts.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-11',
        question: 'The loopback address is...',
        options: ['0.0.0.0', '127.0.0.1', '192.168.1.1', '255.255.255.255'],
        correctIndices: [1],
        explanation: '127.0.0.1 is the loopback address, used to refer to the local machine itself.',
        difficulty: 'G',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-12',
        question: 'Localhost refers to...',
        options: ['The network gateway', 'The local machine', 'The DNS server', 'The DHCP server'],
        correctIndices: [1],
        explanation: 'Localhost is a hostname that refers to the current computer/local machine.',
        difficulty: 'G',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-13',
        question: "Can you access another machine's localhost?",
        options: ['Yes, with SSH', 'Yes, with routing', "No, it's not possible", 'Yes, with DNS'],
        correctIndices: [2],
        explanation: 'Localhost (127.0.0.1) always refers to the local machine and cannot be accessed from another machine.',
        difficulty: 'G',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-14',
        question: 'DNS translates...',
        options: ['IPs to MACs', 'MACs to IPs', 'Hostnames to IPs', 'Ports to IPs'],
        correctIndices: [2],
        explanation: 'DNS (Domain Name System) translates human-readable hostnames to IP addresses.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-15',
        question: 'DNS default port is...',
        options: ['22', '53', '80', '443'],
        correctIndices: [1],
        explanation: 'DNS uses port 53 for both TCP and UDP.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-16',
        question: 'DHCP provides...',
        options: ['DNS resolution', 'Automatic IP assignment', 'Firewall rules', 'Routing tables'],
        correctIndices: [1],
        explanation: 'DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses to devices on a network.',
        difficulty: 'G',
        category: 'DHCP',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-17',
        question: 'DHCP default port is...',
        options: ['53', '67/68', '80', '443'],
        correctIndices: [1],
        explanation: 'DHCP uses port 67 for the server and port 68 for the client.',
        difficulty: 'G',
        category: 'DHCP',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-18',
        question: 'NAT stands for...',
        options: ['Network Access Terminal', 'Network Address Translation', 'Native Address Table', 'Network Admin Tool'],
        correctIndices: [1],
        explanation: 'NAT (Network Address Translation) translates private IP addresses to public IP addresses.',
        difficulty: 'G',
        category: 'NAT',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-19',
        question: 'Private IP range 10.x.x.x is...',
        options: ['/8', '/16', '/24', 'Class A private'],
        correctIndices: [3],
        explanation: '10.0.0.0/8 is a Class A private IP range, providing a large address space.',
        difficulty: 'G',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-20',
        question: 'Private IP range 172.16.x.x - 172.31.x.x is...',
        options: ['Class A', 'Class B private', 'Class C', 'Class D'],
        correctIndices: [1],
        explanation: '172.16.0.0/12 is a Class B private IP range.',
        difficulty: 'G',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-21',
        question: 'Private IP range 192.168.x.x is...',
        options: ['Class A', 'Class B', 'Class C private', 'Class D'],
        correctIndices: [2],
        explanation: '192.168.0.0/16 is a Class C private IP range, commonly used in home networks.',
        difficulty: 'G',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-22',
        question: 'Select all private IP ranges (choose 3):',
        options: [
            '10.0.0.0/8',
            '11.0.0.0/8',
            '172.16.0.0/12',
            '172.0.0.0/8',
            '192.168.0.0/16',
            '192.0.0.0/8',
            '169.254.0.0/16',
            '224.0.0.0/4',
            '8.8.8.0/24',
            '1.1.1.0/24'
        ],
        correctIndices: [0, 2, 4],
        explanation: 'The three private IP ranges defined by RFC 1918 are: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16.',
        difficulty: 'VG',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-23',
        question: 'Gateway is...',
        options: ['A DNS server', 'A router to other networks', 'A firewall', 'A switch'],
        correctIndices: [1],
        explanation: 'A gateway is a router that connects a local network to other networks, including the internet.',
        difficulty: 'G',
        category: 'Routing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-24',
        question: 'Subnet mask for /24 is...',
        options: ['255.255.0.0', '255.255.255.0', '255.255.255.128', '255.255.255.192'],
        correctIndices: [1],
        explanation: '/24 means 24 bits for network, resulting in subnet mask 255.255.255.0.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-25',
        question: 'Subnet mask for /16 is...',
        options: ['255.0.0.0', '255.255.0.0', '255.255.255.0', '255.255.128.0'],
        correctIndices: [1],
        explanation: '/16 means 16 bits for network, resulting in subnet mask 255.255.0.0.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-26',
        question: 'Subnet mask for /8 is...',
        options: ['255.0.0.0', '255.255.0.0', '255.255.255.0', '128.0.0.0'],
        correctIndices: [0],
        explanation: '/8 means 8 bits for network, resulting in subnet mask 255.0.0.0.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-27',
        question: 'Subnet mask 255.255.255.128 is...',
        options: ['/24', '/25', '/26', '/27'],
        correctIndices: [1],
        explanation: '255.255.255.128 has 25 bits set (24 + 1), so it is /25.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-28',
        question: 'Subnet mask 255.255.255.192 is...',
        options: ['/24', '/25', '/26', '/27'],
        correctIndices: [2],
        explanation: '255.255.255.192 has 26 bits set (24 + 2), so it is /26.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-29',
        question: 'Subnet mask 255.255.255.224 is...',
        options: ['/25', '/26', '/27', '/28'],
        correctIndices: [2],
        explanation: '255.255.255.224 has 27 bits set (24 + 3), so it is /27.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-30',
        question: 'Subnet mask 255.255.255.240 is...',
        options: ['/26', '/27', '/28', '/29'],
        correctIndices: [2],
        explanation: '255.255.255.240 has 28 bits set (24 + 4), so it is /28.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-31',
        question: 'CIDR stands for...',
        options: ['Class Inter-Domain Routing', 'Classless Inter-Domain Routing', 'Common Internet Domain Routing', 'Classful Inter-Domain Routing'],
        correctIndices: [1],
        explanation: 'CIDR (Classless Inter-Domain Routing) allows flexible allocation of IP addresses without class boundaries.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-32',
        question: 'The command to show IP address is...',
        options: ['ipconfig', 'ifconfig', 'ip a', 'show ip'],
        correctIndices: [2],
        explanation: 'The modern Linux command to show IP addresses is "ip a" (or "ip addr").',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-33',
        question: 'The command to test connectivity is...',
        options: ['test', 'connect', 'ping', 'reach'],
        correctIndices: [2],
        explanation: 'The ping command tests network connectivity by sending ICMP echo requests.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-34',
        question: 'The command to trace route is...',
        options: ['route', 'path', 'traceroute', 'trace'],
        correctIndices: [2],
        explanation: 'The traceroute command shows the path packets take to reach a destination.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-35',
        question: 'The command to show routing table is...',
        options: ['routes', 'ip route', 'routing', 'show route'],
        correctIndices: [1],
        explanation: 'The "ip route" command displays the routing table on Linux.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-36',
        question: 'The command to show DNS servers is...',
        options: ['dns', 'resolve', 'cat /etc/resolv.conf', 'nslookup'],
        correctIndices: [2],
        explanation: 'The DNS servers are configured in /etc/resolv.conf, viewable with cat.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-37',
        question: 'DNS config file is...',
        options: ['/etc/dns.conf', '/etc/resolv.conf', '/etc/named.conf', '/etc/dns/config'],
        correctIndices: [1],
        explanation: '/etc/resolv.conf contains DNS resolver configuration including nameservers.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-38',
        question: 'Hosts file is...',
        options: ['/etc/hostname', '/etc/hosts', '/etc/hostnames', '/etc/host.conf'],
        correctIndices: [1],
        explanation: '/etc/hosts contains static hostname to IP mappings.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-39',
        question: '/etc/hosts overrides...',
        options: ['Nothing', 'DNS for listed hosts', 'All DNS', 'Routing'],
        correctIndices: [1],
        explanation: '/etc/hosts takes precedence over DNS for hostnames listed in the file.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-40',
        question: 'Network config in Ubuntu is...',
        options: ['/etc/network/', '/etc/netplan/', '/etc/sysconfig/', '/etc/net/'],
        correctIndices: [1],
        explanation: 'Ubuntu uses Netplan for network configuration, stored in /etc/netplan/.',
        difficulty: 'G',
        category: 'Network Configuration',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-41',
        question: 'ICMP is used by...',
        options: ['SSH', 'HTTP', 'ping', 'DNS'],
        correctIndices: [2],
        explanation: 'ICMP (Internet Control Message Protocol) is used by ping for connectivity testing.',
        difficulty: 'G',
        category: 'Protocols',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-42',
        question: 'TCP is...',
        options: ['Connection-oriented', 'Connectionless', 'Faster than UDP', 'Unreliable'],
        correctIndices: [0],
        explanation: 'TCP is connection-oriented, establishing a connection before data transfer.',
        difficulty: 'G',
        category: 'Protocols',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-43',
        question: 'UDP is...',
        options: ['Connection-oriented', 'Connectionless', 'Slower than TCP', 'More reliable'],
        correctIndices: [1],
        explanation: 'UDP is connectionless, sending data without establishing a connection first.',
        difficulty: 'G',
        category: 'Protocols',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-44',
        question: 'TCP port 80 is for...',
        options: ['SSH', 'HTTP', 'HTTPS', 'FTP'],
        correctIndices: [1],
        explanation: 'Port 80 is the default port for HTTP (unencrypted web traffic).',
        difficulty: 'G',
        category: 'Ports',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-45',
        question: 'TCP port 443 is for...',
        options: ['HTTP', 'HTTPS', 'SSH', 'DNS'],
        correctIndices: [1],
        explanation: 'Port 443 is the default port for HTTPS (encrypted web traffic).',
        difficulty: 'G',
        category: 'Ports',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-46',
        question: 'TCP port 22 is for...',
        options: ['Telnet', 'FTP', 'SSH', 'SMTP'],
        correctIndices: [2],
        explanation: 'Port 22 is the default port for SSH (Secure Shell).',
        difficulty: 'G',
        category: 'Ports',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-47',
        question: 'TCP port 21 is for...',
        options: ['SSH', 'FTP', 'Telnet', 'HTTP'],
        correctIndices: [1],
        explanation: 'Port 21 is the default control port for FTP (File Transfer Protocol).',
        difficulty: 'G',
        category: 'Ports',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-48',
        question: 'TCP port 25 is for...',
        options: ['POP3', 'IMAP', 'SMTP', 'HTTP'],
        correctIndices: [2],
        explanation: 'Port 25 is the default port for SMTP (Simple Mail Transfer Protocol).',
        difficulty: 'G',
        category: 'Ports',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-49',
        question: 'TCP port 23 is for...',
        options: ['SSH', 'Telnet', 'FTP', 'SMTP'],
        correctIndices: [1],
        explanation: 'Port 23 is the default port for Telnet (unencrypted remote access).',
        difficulty: 'G',
        category: 'Ports',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-50',
        question: 'Select all well-known ports (choose 5):',
        options: ['22', '2222', '80', '8080', '443', '4443', '21', '2121', '25', '2525'],
        correctIndices: [0, 2, 4, 6, 8],
        explanation: 'Well-known ports are 0-1023. 22 (SSH), 80 (HTTP), 443 (HTTPS), 21 (FTP), and 25 (SMTP) are all well-known ports.',
        difficulty: 'VG',
        category: 'Ports',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-51',
        question: 'MAC address has...',
        options: ['32 bits', '48 bits', '64 bits', '128 bits'],
        correctIndices: [1],
        explanation: 'A MAC address is 48 bits (6 bytes), typically written as 12 hex digits.',
        difficulty: 'G',
        category: 'MAC Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-52',
        question: 'MAC address is...',
        options: ['Layer 2', 'Layer 3', 'Layer 4', 'Layer 7'],
        correctIndices: [0],
        explanation: 'MAC addresses operate at Layer 2 (Data Link layer) of the OSI model.',
        difficulty: 'G',
        category: 'OSI Model',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-53',
        question: 'IP address is...',
        options: ['Layer 2', 'Layer 3', 'Layer 4', 'Layer 7'],
        correctIndices: [1],
        explanation: 'IP addresses operate at Layer 3 (Network layer) of the OSI model.',
        difficulty: 'G',
        category: 'OSI Model',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-54',
        question: 'Port number is...',
        options: ['Layer 2', 'Layer 3', 'Layer 4', 'Layer 7'],
        correctIndices: [2],
        explanation: 'Port numbers operate at Layer 4 (Transport layer) of the OSI model.',
        difficulty: 'G',
        category: 'OSI Model',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-55',
        question: 'ARP translates...',
        options: ['Hostnames to IPs', 'IPs to MACs', 'MACs to IPs', 'Ports to IPs'],
        correctIndices: [1],
        explanation: 'ARP (Address Resolution Protocol) translates IP addresses to MAC addresses.',
        difficulty: 'G',
        category: 'Protocols',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-56',
        question: 'To view ARP cache, use...',
        options: ['arp -l', 'arp -a', 'arp -show', 'arp -cache'],
        correctIndices: [1],
        explanation: 'The "arp -a" command displays the ARP cache (IP to MAC mappings).',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-57',
        question: 'MTU stands for...',
        options: ['Maximum Transfer Unit', 'Maximum Transmission Unit', 'Minimum Transfer Unit', 'Maximum Transport Unit'],
        correctIndices: [1],
        explanation: 'MTU (Maximum Transmission Unit) is the largest packet size that can be transmitted.',
        difficulty: 'G',
        category: 'Network Concepts',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-58',
        question: 'Default MTU is usually...',
        options: ['1000', '1500', '9000', '65535'],
        correctIndices: [1],
        explanation: 'The default MTU for Ethernet is 1500 bytes.',
        difficulty: 'G',
        category: 'Network Concepts',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-59',
        question: 'Jumbo frames have MTU of...',
        options: ['1500', '4000', '9000', '16000'],
        correctIndices: [2],
        explanation: 'Jumbo frames typically have an MTU of 9000 bytes, used in high-performance networks.',
        difficulty: 'G',
        category: 'Network Concepts',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-60',
        question: 'FQDN stands for...',
        options: ['Full Quality Domain Name', 'Fully Qualified Domain Name', 'Fast Query Domain Name', 'Full Qualified DNS Name'],
        correctIndices: [1],
        explanation: 'FQDN (Fully Qualified Domain Name) is the complete domain name for a host.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-61',
        question: 'TTL in ping stands for...',
        options: ['Total Transfer Length', 'Time To Live', 'Transfer Time Limit', 'Total Time Left'],
        correctIndices: [1],
        explanation: 'TTL (Time To Live) indicates how many hops a packet can traverse before being discarded.',
        difficulty: 'G',
        category: 'Network Concepts',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-62',
        question: 'TTL decreases by 1 at each...',
        options: ['Switch', 'Router', 'Server', 'Firewall'],
        correctIndices: [1],
        explanation: 'TTL is decremented by 1 at each router (hop) the packet passes through.',
        difficulty: 'G',
        category: 'Network Concepts',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-63',
        question: 'When TTL reaches 0...',
        options: ['Packet speeds up', 'Packet is dropped', 'Packet loops forever', 'Packet resets'],
        correctIndices: [1],
        explanation: 'When TTL reaches 0, the packet is dropped to prevent infinite loops.',
        difficulty: 'G',
        category: 'Network Concepts',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-64',
        question: 'Broadcast address for 192.168.1.0/24 is...',
        options: ['192.168.1.0', '192.168.1.1', '192.168.1.254', '192.168.1.255'],
        correctIndices: [3],
        explanation: 'The broadcast address for a /24 network is the last address (192.168.1.255).',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-65',
        question: 'Network address for 192.168.1.0/24 is...',
        options: ['192.168.1.0', '192.168.1.1', '192.168.1.254', '192.168.1.255'],
        correctIndices: [0],
        explanation: 'The network address is the first address in the subnet (192.168.1.0).',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-66',
        question: 'First usable IP in 192.168.1.0/24 is...',
        options: ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.254'],
        correctIndices: [1],
        explanation: 'The first usable IP is one after the network address (192.168.1.1).',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-67',
        question: 'Last usable IP in 192.168.1.0/24 is...',
        options: ['192.168.1.253', '192.168.1.254', '192.168.1.255', '192.168.1.256'],
        correctIndices: [1],
        explanation: 'The last usable IP is one before the broadcast address (192.168.1.254).',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-68',
        question: '0.0.0.0 means...',
        options: ['Localhost', 'Broadcast', 'All interfaces / default route', 'Invalid'],
        correctIndices: [2],
        explanation: '0.0.0.0 represents all interfaces (when binding) or the default route (in routing).',
        difficulty: 'G',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-69',
        question: '255.255.255.255 is...',
        options: ['Network address', 'Broadcast address', 'Gateway', 'Localhost'],
        correctIndices: [1],
        explanation: '255.255.255.255 is the limited broadcast address, used to broadcast to all hosts on the local network.',
        difficulty: 'G',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-70',
        question: 'Link-local address range is...',
        options: ['127.0.0.0/8', '169.254.0.0/16', '192.168.0.0/16', '10.0.0.0/8'],
        correctIndices: [1],
        explanation: '169.254.0.0/16 is the link-local address range, used when DHCP is unavailable.',
        difficulty: 'G',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-71',
        question: 'Select valid IP addresses (choose 4):',
        options: [
            '192.168.1.1',
            '192.168.1.256',
            '10.0.0.1',
            '10.0.0.0.1',
            '172.16.0.1',
            '172.16.0.1.1',
            '8.8.8.8',
            '8.8.8.8.8',
            '256.1.1.1',
            '1.1.1.1.1'
        ],
        correctIndices: [0, 2, 4, 6],
        explanation: 'Valid IPv4 addresses have 4 octets with values 0-255. Invalid: 256 in any octet, or more than 4 octets.',
        difficulty: 'VG',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-72',
        question: 'To show listening ports, use...',
        options: ['ports', 'listen', 'ss -tuln', 'netstat only'],
        correctIndices: [2],
        explanation: '"ss -tuln" shows TCP/UDP listening ports with numeric addresses.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-73',
        question: 'To resolve hostname, use...',
        options: ['resolve', 'dns', 'nslookup', 'host only'],
        correctIndices: [2],
        explanation: 'nslookup is a command to query DNS and resolve hostnames to IP addresses.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-74',
        question: 'Another command to resolve hostname is...',
        options: ['resolve', 'dns', 'dig', 'lookup'],
        correctIndices: [2],
        explanation: 'dig (Domain Information Groper) is another DNS lookup utility.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-75',
        question: 'To show hostname, use...',
        options: ['name', 'host', 'hostname', 'myname'],
        correctIndices: [2],
        explanation: 'The hostname command displays the current system hostname.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-76',
        question: 'To set hostname permanently...',
        options: ['hostname newname', 'hostnamectl set-hostname', 'sethostname', 'name set'],
        correctIndices: [1],
        explanation: '"hostnamectl set-hostname" sets the hostname permanently on systemd systems.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-77',
        question: '/etc/hostname contains...',
        options: ['All hostnames', 'System hostname', 'Network hosts', 'DNS servers'],
        correctIndices: [1],
        explanation: '/etc/hostname contains the system\'s own hostname.',
        difficulty: 'G',
        category: 'Network Configuration',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-78',
        question: 'curl is used to...',
        options: ['Create URLs', 'Transfer data from/to servers', 'Check routing', 'Configure network'],
        correctIndices: [1],
        explanation: 'curl is a tool to transfer data from or to a server using various protocols.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-79',
        question: 'wget is used to...',
        options: ['Get network info', 'Download files', 'Configure wget', 'Watch network'],
        correctIndices: [1],
        explanation: 'wget is a command-line utility for downloading files from the web.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-80',
        question: 'To download file with wget...',
        options: ['wget get URL', 'wget URL', 'wget download URL', 'wget -d URL'],
        correctIndices: [1],
        explanation: 'Simply "wget URL" downloads the file from the specified URL.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-81',
        question: 'Select all network diagnostic tools (choose 5):',
        options: ['ping', 'cat', 'traceroute', 'ls', 'dig', 'grep', 'nslookup', 'vim', 'curl', 'chmod'],
        correctIndices: [0, 2, 4, 6, 8],
        explanation: 'Network diagnostic tools: ping (connectivity), traceroute (path), dig (DNS), nslookup (DNS), curl (data transfer).',
        difficulty: 'VG',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-82',
        question: 'VPN stands for...',
        options: ['Virtual Port Network', 'Virtual Private Network', 'Very Private Network', 'Virtual Protected Network'],
        correctIndices: [1],
        explanation: 'VPN (Virtual Private Network) creates a secure, encrypted connection over a public network.',
        difficulty: 'G',
        category: 'VPN',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-83',
        question: 'VPN encrypts traffic...',
        options: ['Only locally', 'Only on server', 'Between client and server', 'Not at all'],
        correctIndices: [2],
        explanation: 'VPN encrypts traffic between the client and the VPN server.',
        difficulty: 'G',
        category: 'VPN',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-84',
        question: 'To flush DNS cache in systemd...',
        options: ['dns flush', 'flush dns', 'systemd-resolve --flush-caches', 'clear dns'],
        correctIndices: [2],
        explanation: '"systemd-resolve --flush-caches" flushes the DNS cache on systemd systems.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-85',
        question: 'NetworkManager command is...',
        options: ['network', 'nm', 'nmcli', 'netman'],
        correctIndices: [2],
        explanation: 'nmcli is the command-line interface for NetworkManager.',
        difficulty: 'G',
        category: 'Network Configuration',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-86',
        question: 'To show nmcli connections...',
        options: ['nmcli list', 'nmcli connection show', 'nmcli show', 'nmcli connections'],
        correctIndices: [1],
        explanation: '"nmcli connection show" displays all NetworkManager connections.',
        difficulty: 'G',
        category: 'Network Configuration',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-87',
        question: 'To restart networking in Ubuntu...',
        options: ['service network restart', 'systemctl restart NetworkManager', 'network restart', 'restart network'],
        correctIndices: [1],
        explanation: '"systemctl restart NetworkManager" restarts the network service on Ubuntu.',
        difficulty: 'G',
        category: 'Network Configuration',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-88',
        question: 'netplan apply does...',
        options: ['Shows config', 'Applies network config', 'Tests config', 'Creates config'],
        correctIndices: [1],
        explanation: '"netplan apply" applies the network configuration defined in netplan YAML files.',
        difficulty: 'G',
        category: 'Network Configuration',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-89',
        question: 'ethtool shows...',
        options: ['Ethernet configuration', 'Network interface details', 'Routing table', 'DNS info'],
        correctIndices: [1],
        explanation: 'ethtool displays and modifies network interface settings and details.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-90',
        question: 'To show interface statistics...',
        options: ['ip stats', 'ip -s link', 'net stats', 'if stats'],
        correctIndices: [1],
        explanation: '"ip -s link" shows interface statistics including packets and errors.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-91',
        question: 'Select all that are Layer 4 protocols (choose 2):',
        options: ['IP', 'TCP', 'HTTP', 'UDP', 'Ethernet', 'ARP', 'ICMP', 'DNS', 'SSH', 'FTP'],
        correctIndices: [1, 3],
        explanation: 'TCP and UDP are Layer 4 (Transport layer) protocols. Others operate at different layers.',
        difficulty: 'VG',
        category: 'OSI Model',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-92',
        question: 'HTTP is Layer...',
        options: ['4', '5', '6', '7'],
        correctIndices: [3],
        explanation: 'HTTP operates at Layer 7 (Application layer) of the OSI model.',
        difficulty: 'G',
        category: 'OSI Model',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-93',
        question: 'SSH is Layer...',
        options: ['4', '5', '6', '7'],
        correctIndices: [3],
        explanation: 'SSH operates at Layer 7 (Application layer) of the OSI model.',
        difficulty: 'G',
        category: 'OSI Model',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-94',
        question: 'To check if port is open remotely...',
        options: ['port check', 'nc -zv host port', 'open port', 'test port'],
        correctIndices: [1],
        explanation: '"nc -zv host port" uses netcat to check if a port is open on a remote host.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-95',
        question: 'Ephemeral ports range is...',
        options: ['0-1023', '1024-49151', '49152-65535', '1-65535'],
        correctIndices: [2],
        explanation: 'Ephemeral (dynamic) ports are in the range 49152-65535, used for temporary connections.',
        difficulty: 'G',
        category: 'Ports',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-96',
        question: 'Well-known ports range is...',
        options: ['0-1023', '1024-49151', '49152-65535', '1-1024'],
        correctIndices: [0],
        explanation: 'Well-known ports are in the range 0-1023, reserved for common services.',
        difficulty: 'G',
        category: 'Ports',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-97',
        question: 'To add static route...',
        options: ['route add', 'ip route add', 'add route', 'static route'],
        correctIndices: [1],
        explanation: '"ip route add" is the modern command to add a static route on Linux.',
        difficulty: 'G',
        category: 'Routing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-98',
        question: 'Default gateway shows as...',
        options: ['gateway', 'router', 'default via', 'route 0'],
        correctIndices: [2],
        explanation: 'In "ip route" output, the default gateway is shown as "default via [IP]".',
        difficulty: 'G',
        category: 'Routing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-99',
        question: 'To delete route...',
        options: ['route remove', 'ip route del', 'del route', 'remove route'],
        correctIndices: [1],
        explanation: '"ip route del" is used to delete a route from the routing table.',
        difficulty: 'G',
        category: 'Routing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-100',
        question: 'Multicast address range is...',
        options: ['192.168.0.0/16', '169.254.0.0/16', '224.0.0.0/4', '240.0.0.0/4'],
        correctIndices: [2],
        explanation: '224.0.0.0/4 (224.0.0.0 - 239.255.255.255) is the multicast address range.',
        difficulty: 'G',
        category: 'IP Addressing',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-101',
        question: 'VLAN stands for...',
        options: ['Virtual Local Address Network', 'Virtual Local Area Network', 'Very Large Area Network', 'Virtual LAN Network'],
        correctIndices: [1],
        explanation: 'VLAN (Virtual Local Area Network) logically segments a physical network.',
        difficulty: 'G',
        category: 'Network Concepts',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-102',
        question: 'To see network namespaces...',
        options: ['ip netns list', 'ip netns', 'netns show', 'show netns'],
        correctIndices: [1],
        explanation: '"ip netns" lists all network namespaces on the system.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-103',
        question: 'Bridge in networking is...',
        options: ['A router', 'Connects network segments', 'A firewall', 'A gateway'],
        correctIndices: [1],
        explanation: 'A network bridge connects multiple network segments at Layer 2.',
        difficulty: 'G',
        category: 'Network Concepts',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-104',
        question: 'To show bridge interfaces...',
        options: ['bridge list', 'brctl show', 'ip bridge', 'show bridge'],
        correctIndices: [1],
        explanation: '"brctl show" displays bridge interfaces and their configuration.',
        difficulty: 'G',
        category: 'Network Commands',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-105',
        question: 'Bonding/teaming is used for...',
        options: ['Security', 'Link aggregation/redundancy', 'Routing', 'DNS'],
        correctIndices: [1],
        explanation: 'Network bonding/teaming combines multiple interfaces for increased bandwidth or redundancy.',
        difficulty: 'G',
        category: 'Network Concepts',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-106',
        question: 'Select valid subnet masks (choose 4):',
        options: [
            '255.255.255.0',
            '255.255.255.1',
            '255.255.255.128',
            '255.255.255.100',
            '255.255.255.192',
            '255.255.255.200',
            '255.255.0.0',
            '255.255.0.1',
            '255.0.255.0',
            '255.255.255.255'
        ],
        correctIndices: [0, 2, 4, 6],
        explanation: 'Valid subnet masks have contiguous 1s followed by contiguous 0s. Invalid values like 1, 100, 200 break this pattern.',
        difficulty: 'VG',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-107',
        question: '/31 is used for...',
        options: ['Large networks', 'Point-to-point links', 'Broadcast', 'Multicast'],
        correctIndices: [1],
        explanation: '/31 provides 2 addresses with no network/broadcast waste, ideal for point-to-point links.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-108',
        question: '/32 means...',
        options: ['Network address', 'Single host', 'Broadcast', 'Subnet'],
        correctIndices: [1],
        explanation: '/32 represents a single host address (all 32 bits are network bits).',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-109',
        question: 'To calculate hosts: 2^n - 2, n is...',
        options: ['Network bits', 'Host bits', 'Subnet bits', 'Total bits'],
        correctIndices: [1],
        explanation: 'In the formula 2^n - 2, n represents the number of host bits in the subnet.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    },
    {
        id: 'omtenta-v2-subnet-110',
        question: 'Host bits in /24 is...',
        options: ['24', '8', '16', '32'],
        correctIndices: [1],
        explanation: 'In /24, 24 bits are for network, leaving 32 - 24 = 8 bits for hosts.',
        difficulty: 'G',
        category: 'Subnetting',
        topic: 'subnetting-natverk'
    }
]
