# Networking from a Server Perspective

Fokus: Hur servrar pratar med varandra och internet

## IPv4 Fundamentals

### Subnätmasker, nätverks-ID vs host-ID

En IPv4-adress består av 32 bitar, vanligtvis skrivet som 4 oktetter:

```
192.168.1.100
```

Adressen delas upp i två delar:

- **Nätverks-ID**: Identifierar nätverket
- **Host-ID**: Identifierar datorn i nätverket

Subnätmasken bestämmer var gränsen går:

```bash
# Exempel: 192.168.1.100/24
# Subnätmask: 255.255.255.0
# Nätverks-ID: 192.168.1.0
# Host-ID: 100
# Broadcast: 192.168.1.255
```

### Subnetting /24 vs /27 vs /29

CIDR-notation (/24, /27, /29) anger antalet bitar som används för nätverks-ID:

- **/24**: 24 bitar för nätverk, 8 bitar för hosts
- **/27**: 27 bitar för nätverk, 5 bitar för hosts
- **/29**: 29 bitar för nätverk, 3 bitar för hosts

**Beräkna tillgängliga hosts**: 2^(32-n) - 2

- /24: 2^(32-24) - 2 = 2^8 - 2 = 256 - 2 = **254 hosts**
- /27: 2^(32-27) - 2 = 2^5 - 2 = 32 - 2 = **30 hosts**
- /29: 2^(32-29) - 2 = 2^3 - 2 = 8 - 2 = **6 hosts**

(Minus 2 eftersom nätverks-ID och broadcast-adress inte kan användas)

```bash
# Exempel: 192.168.1.0/24
# Nätverks-ID: 192.168.1.0
# Användbara hosts: 192.168.1.1 - 192.168.1.254
# Broadcast: 192.168.1.255

# Exempel: 192.168.1.0/27
# Nätverks-ID: 192.168.1.0
# Användbara hosts: 192.168.1.1 - 192.168.1.30
# Broadcast: 192.168.1.31

# Exempel: 10.0.0.48/29
# Nätverks-ID: 10.0.0.48
# Användbara hosts: 10.0.0.49 - 10.0.0.54
# Broadcast: 10.0.0.55
```

### APIPA (169.254.x.x)

APIPA (Automatic Private IP Addressing) är när en enhet inte kan nå en DHCP-server och tilldelar sig själv en adress i intervallet 169.254.0.0/16.

```bash
# Om servern har IP 169.254.x.x betyder det:
# - DHCP-server kunde inte nås
# - Enheten tilldelade sig själv en lokal adress
# - Ingen internetanslutning (endast lokalt nätverk)

# Lösning: Kontrollera nätverkskabel, DHCP-server, eller sätt statisk IP
```

### Broadcast-adresser

Broadcast-adressen är den sista adressen i nätverket och används för att skicka meddelanden till alla i nätverket.

```bash
# För /24 nätverk
# Broadcast = nätverks-ID med alla host-bitar satta till 1
# 192.168.1.255

# Ping broadcast (testa om någon svarar)
ping -b 192.168.1.255
```

## The Network Stack: OSI-modellen i detalj

OSI-modellen har 7 lager, varje lager har sitt specifika ansvar:

### Layer 1: Physical (Fysiskt)

- Kablar, signaler, elektriska impulser
- Exempel: Ethernet-kabel, fiber

### Layer 2: Data Link (Datalänk)

- MAC-adresser, frame-delivery
- Protokoll: Ethernet
- Exempel: Switchar arbetar här

```bash
# Visa MAC-adresser
ip link show
# link/ether 00:11:22:33:44:55
```

### Layer 3: Network (Nätverk)

- IP-adresser, routing
- Protokoll: IP (IPv4, IPv6), ICMP, ARP
- Exempel: Routers arbetar här

```bash
# Layer 3: IP-adresser
ip addr show
ip route show
```

### Layer 4: Transport (Transport)

- Portar, anslutningar, felkontroll
- Protokoll: TCP, UDP
- Exempel: Load balancers kan arbeta här

```bash
# Layer 4: Portar och anslutningar
ss -tlnp  # TCP listening
ss -ulnp  # UDP listening
```

### Layer 5: Session (Session)

- Session-hantering
- Exempel: NetBIOS

### Layer 6: Presentation (Presentation)

- Datakodning, kryptering
- Exempel: SSL/TLS (även om det ofta räknas som Layer 7)

### Layer 7: Application (Applikation)

- Applikationsprotokoll
- Protokoll: HTTP, HTTPS, FTP, SSH, DNS
- Exempel: Webbservrar, e-postservrar

```bash
# Layer 7: Applikationsdata
curl http://example.com
# HTTP-headers, URL, cookies - allt detta är Layer 7
```

### Layer 7 Switching/Load Balancing

Layer 7 Load Balancing balanserar trafik baserat på applikationsdata (t.ex. en specifik URL eller HTTP-header) istället för bara IP-adresser och portar.

```nginx
# Exempel: Nginx kan balansera baserat på URL
location /api/ {
    proxy_pass http://api_backend;
}
location /static/ {
    proxy_pass http://static_backend;
}
```

**Fördel**: Mer intelligent routing baserat på innehållet i paketen, inte bara destination.

## TCP vs UDP

### TCP (Transmission Control Protocol)

- Connection-oriented (etablerar anslutning först)
- Reliable (garanterar leverans)
- Ordered (data kommer i rätt ordning)
- Slower (mer overhead)
- **Används för**: HTTP, HTTPS, SSH, FTP, e-post

### UDP (User Datagram Protocol)

- Connectionless (ingen anslutning)
- Unreliable (ingen garanti för leverans)
- Unordered (data kan komma i fel ordning)
- Faster (mindre overhead)
- **Används för**: DNS, streaming, spel, VoIP

### TCP 3-way Handshake

Innan TCP kan skicka data måste en anslutning etableras via "3-way handshake":

1. **SYN**: Klienten skickar SYN (synchronize) till servern
2. **SYN-ACK**: Servern svarar med SYN-ACK (acknowledgment)
3. **ACK**: Klienten bekräftar med ACK

```bash
# Observera handshake med tcpdump
sudo tcpdump -i eth0 'tcp[tcpflags] & tcp-syn != 0'
# Du ser: SYN → SYN-ACK → ACK
```

### TCP Flaggor

TCP använder flaggor för att kontrollera anslutningar:

- **SYN**: Synchronize - starta anslutning
- **ACK**: Acknowledgment - bekräfta mottagen data
- **FIN**: Finish - avsluta anslutning snyggt
- **RST**: Reset - avbryt anslutning tvärt (vid fel)
- **PSH**: Push - skicka data omedelbart
- **URG**: Urgent - prioritetsdata

```bash
# RST skickas vid fel eller avbruten anslutning
# FIN används för snygg avstängning (båda parter skickar FIN)
```

### ICMP (Internet Control Message Protocol)

ICMP används för felmeddelanden och nätverksdiagnostik.

```bash
# Ping använder ICMP
ping -c 4 8.8.8.8
# Skickar ICMP Echo Request, får ICMP Echo Reply

# ICMP-typer:
# 0 = Echo Reply
# 3 = Destination Unreachable
# 8 = Echo Request
# 11 = Time Exceeded (används av traceroute)
```

**Användning**: Ping, traceroute, felmeddelanden från routers.

```bash
# TCP anslutningar
ss -tn
# ESTAB = established connection
# LISTEN = listening for connections

# UDP sockets
ss -un
# UDP är connectionless, så ingen "established" state
```

## DNS & Resolution: Order of operations

När en dator försöker lösa ett hostnamn till en IP-adress, följs denna ordning:

1. **/etc/hosts**: Lokal fil med statiska mappningar
2. **/etc/resolv.conf**: DNS-servrar att fråga

```bash
# 1. Kolla /etc/hosts först
cat /etc/hosts
# 127.0.0.1 localhost
# 192.168.1.10 myserver.local

# 2. Om inte hittat, fråga DNS-servrar
cat /etc/resolv.conf
# nameserver 8.8.8.8
# nameserver 1.1.1.1
```

### DNS-verktyg

```bash
# Testa DNS-resolution
nslookup example.com
dig example.com
host example.com

# Testa specifik DNS-server
dig @8.8.8.8 example.com

# Reverse DNS lookup (IP → hostname)
dig -x 8.8.8.8

# Avancerad DNS-uppslagning med hela svarshuvudet
dig example.com +noall +answer
dig example.com ANY  # Alla typer av poster
```

### DNS-posttyper

- **A**: IPv4-adress
- **AAAA**: IPv6-adress
- **CNAME**: Canonical Name (alias som pekar på ett annat namn)
- **MX**: Mail Exchange (e-postserver)
- **TXT**: Textposter (t.ex. för verifiering)

```bash
# CNAME-exempel
dig www.example.com
# www.example.com.    CNAME   example.com.
# example.com.        A       192.0.2.1

# CNAME fungerar som ett alias
# www.example.com pekar på example.com
```

### TTL (Time To Live)

TTL anger hur länge en DNS-post kan cachas innan den måste uppdateras.

```bash
# Visa TTL
dig example.com
# ;; ANSWER SECTION:
# example.com.    3600    IN    A    192.0.2.1
#                  ↑
#                  TTL i sekunder (3600 = 1 timme)

# Hög TTL (t.ex. 86400 = 24 timmar):
# - Ändringar tar längre tid att sprida sig (propagera)
# - Gamla värden sparas i cache längre
# - Mindre belastning på DNS-servrar

# Låg TTL (t.ex. 300 = 5 minuter):
# - Ändringar sprids snabbt
# - Mer DNS-frågor (högre belastning)
```

**Best practice**: Använd låg TTL (300-600) innan ändringar, sedan höj till normalt värde.

## Portar & Sockets

### Skillnaden mellan TCP (connection-oriented) och UDP

**TCP Socket**:

```bash
# Server lyssnar på port 80
ss -tlnp | grep :80
# LISTEN 0 128 0.0.0.0:80 0.0.0.0:* users:(("nginx",pid=1234))

# Klient ansluter
curl http://server:80
# TCP etablerar först anslutning, sedan skickar data
```

**UDP Socket**:

```bash
# Server lyssnar på UDP port 53 (DNS)
ss -ulnp | grep :53
# UNCONN 0 0 0.0.0.0:53 0.0.0.0:* users:(("dnsmasq",pid=5678))

# Klient skickar direkt (ingen anslutning)
dig @server example.com
# UDP skickar direkt, ingen anslutning etableras
```

### Portintervall och vanliga portar

**Well-known ports (0-1023)**: Reserverade för systemtjänster, kräver root för att lyssna:

```bash
80/tcp   # HTTP
443/tcp  # HTTPS
22/tcp   # SSH
53/udp, 53/tcp  # DNS
25/tcp   # SMTP (email)
21/tcp   # FTP
23/tcp   # Telnet
```

**Registered ports (1024-49151)**: För applikationer:

```bash
3306/tcp   # MySQL
5432/tcp   # PostgreSQL
6379/tcp   # Redis
27017/tcp  # MongoDB
```

**Dynamic/Private ports (49152-65535)**: För temporära anslutningar (ephemeral ports).

### Socket-koncept i detalj

En Socket är kombinationen av en IP-adress och ett portnummer.

```bash
# Socket-format: IP:Port
192.168.1.10:80
127.0.0.1:3306
0.0.0.0:22  # Lyssnar på alla interfaces

# Visa sockets
ss -tlnp
# State      Recv-Q Send-Q Local Address:Port  Peer Address:Port
# LISTEN     0      128    0.0.0.0:80          0.0.0.0:*       users:(("nginx",pid=1234))
#            ↑                                    ↑
#         Local socket                        Peer socket (tom när LISTEN)
```

**Socket States**:
- **LISTEN**: Väntar på inkommande anslutningar
- **ESTABLISHED**: Aktiv anslutning
- **TIME-WAIT**: Väntar på att stänga anslutning
- **CLOSE-WAIT**: Väntar på att applikationen stänger

```bash
# Visa vilka processer som lyssnar på portar
sudo lsof -i -P -n | grep LISTEN
# eller
sudo netstat -tlnp
```

### Localhost: Varför 127.0.0.1 är en loopback

127.0.0.1 är loopback-adressen - den pekar alltid tillbaka till den lokala datorn.

```bash
# Alla dessa är localhost
127.0.0.1
localhost
::1  # IPv6 loopback

# Testa
ping 127.0.0.1
curl http://127.0.0.1:8080
```

### Hur man når en containers localhost

**Problem**: När du kör en container, är dess localhost isolerad från hostens localhost.

**Lösningar**:

1. **Port mapping**: Mappa container-port till host-port
```bash
docker run -p 8080:80 nginx
# Container port 80 → Host port 8080
# Nu kan du nå via http://localhost:8080
```

2. **Host network mode**: Dela nätverk med host
```bash
docker run --network host nginx
# Container delar hosts nätverk
# localhost i container = localhost på host
```

3. **Docker bridge network**: Använd container-namn för kommunikation
```bash
# Container A kan nå Container B via namn
docker run --name app nginx
docker run --link app:app client
# I client-containern: curl http://app:80
```

## Praktiska nätverkskommandon

### Visa nätverkskonfiguration

```bash
# Alla interfaces
ip addr show
# eller
ifconfig

# ip link - Hantera länkar (interfaces)
ip link show                    # Visa alla interfaces
ip link set eth0 up            # Aktivera interface
ip link set eth0 down          # Inaktivera interface
ip link set eth0 name eth1     # Byt namn (kräver interface down)

# "lo" = Loopback interface (127.0.0.1)
# Det interna virtuella nätverket för kommunikation inom maskinen
```

### Nätverkskonfiguration - /etc/network/interfaces vs /etc/netplan

**Debian/Ubuntu (äldre)**: /etc/network/interfaces

```bash
# /etc/network/interfaces
auto eth0
iface eth0 inet static
    address 192.168.1.10
    netmask 255.255.255.0
    gateway 192.168.1.1
    dns-nameservers 8.8.8.8 1.1.1.1

# Tillämpa ändringar
sudo ifdown eth0 && sudo ifup eth0
# eller
sudo systemctl restart networking
```

**Ubuntu (nyare)**: /etc/netplan/*.yaml

```yaml
# /etc/netplan/01-netcfg.yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      addresses:
        - 192.168.1.10/24
      gateway4: 192.168.1.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 1.1.1.1

# Tillämpa ändringar
sudo netplan apply
```

**Viktigt**: Dessa filer innehåller den permanenta konfigurationen för nätverkskorten (statisk IP, DHCP, etc.).

### DHCP Lease Time

DHCP Lease Time är den tid en enhet får behålla en tilldelad IP-adress innan den måste be om förnyelse.

```bash
# Visa DHCP-information
dhclient -v eth0

# Lease time anges av DHCP-servern
# Vanliga värden: 3600 (1 timme), 86400 (24 timmar)

# Om lease time går ut:
# 1. Enheten försöker förnya med DHCP-servern
# 2. Om förnyelse misslyckas, försöker enheten få ny IP
# 3. Om det misslyckas, kan enheten använda APIPA (169.254.x.x)
```

### Testa anslutningar

```bash
# TCP connection test
telnet server.com 80
# eller
nc -zv server.com 80

# HTTP test
curl -I http://server.com

# Ping (ICMP)
ping -c 4 server.com

# Traceroute
traceroute server.com
# eller
tracepath server.com
```

### Övervaka nätverkstrafik

```bash
# Realtidsöversikt
iftop
# eller
nethogs

# Packet capture (kräver sudo)
tcpdump -i eth0
tcpdump -i eth0 port 80
```

### tcpdump - Avancerad packet capture

```bash
# Grundläggande användning
sudo tcpdump -i eth0

# Filtrera på port
sudo tcpdump -i eth0 port 80

# Filtrera på IP
sudo tcpdump -i eth0 host 192.168.1.10

# Kombinera filter
sudo tcpdump -i eth0 'host 192.168.1.10 and port 80'

# Visa ASCII-innehåll
sudo tcpdump -i eth0 -A port 80

# Spara till fil
sudo tcpdump -i eth0 -w capture.pcap

# Läsa från fil
tcpdump -r capture.pcap

# Visa TCP-flaggorna
sudo tcpdump -i eth0 'tcp[tcpflags] & tcp-syn != 0'
```

**Användning**: Debugga nätverksproblem, analysera trafik, identifiera problem.

### nmap - Nätverksskanning

```bash
# Skanna efter öppna portar
nmap 192.168.1.1

# Skanna specifik port
nmap -p 80,443 192.168.1.1

# Skanna portintervall
nmap -p 1-1000 192.168.1.1

# Identifiera tjänster
nmap -sV 192.168.1.1

# Snabb skanning (vanliga portar)
nmap -F 192.168.1.1

# OS-detektering
nmap -O 192.168.1.1

# Skanna hela nätverk
nmap 192.168.1.0/24
```

**Användning**: Säkerhetsauditering, identifiera öppna portar, hitta tjänster på nätverket.

### ss -tulpen - Detaljerad socket-information

```bash
# Visa alla lyssnande TCP/UDP-portar med process-ID och användare
sudo ss -tulpen

# -t = TCP
# -u = UDP
# -l = Listening
# -p = Process
# -e = Extended information
# -n = Numeric (ingen DNS-lookup)

# Exempel output:
# LISTEN 0 128 0.0.0.0:80 0.0.0.0:* users:(("nginx",pid=1234,fd=6))
#         ↑    ↑   ↑        ↑
#      Recv Send Local   Peer
```

### wget - Ladda ner filer

```bash
# Ladda ner fil
wget http://example.com/file.zip

# Ladda ner till specifik fil
wget -O myfile.zip http://example.com/file.zip

# Fortsätt avbruten nedladdning
wget -c http://example.com/largefile.zip

# Ladda ner i bakgrunden
wget -b http://example.com/file.zip
```

### hostname -i - Visa IP-adress

```bash
# Visa IP-adressen som är kopplad till serverns hostname
hostname -i
# 192.168.1.10

# Visa hostname
hostname
# myserver

# Sätt hostname permanent
# Redigera /etc/hostname
sudo nano /etc/hostname
```

### Bandwidth vs Latency

**Bandwidth (Bandbredd)**: Den maximala mängden data som kan överföras per sekund över en anslutning.

```bash
# Mät bandbredd
speedtest-cli
# eller
iperf3 -c server.com
```

**Latency (Latens)**: Fördröjningen (tiden) det tar för ett datapaket att färdas från sändare till mottagare.

```bash
# Mät latens
ping -c 10 server.com
# time=25.3 ms  ← Detta är latens
```

**Skillnad**: Hög bandbredd = kan skicka mycket data, låg latens = data kommer snabbt.

### MTU (Maximum Transmission Unit)

MTU är den största tillåtna storleken på ett paket i nätverket.

```bash
# Visa MTU
ip link show eth0
# mtu 1500

# Standard MTU: 1500 bytes (Ethernet)
# Jumbo frames: 9000 bytes (kräver stöd i nätverket)

# Ändra MTU
sudo ip link set eth0 mtu 9000

# Testa MTU
ping -M do -s 1472 8.8.8.8
# -M do = Don't fragment
# -s 1472 = Packet size (1500 - 28 bytes header = 1472)
```

**Viktigt**: Om paket är större än MTU delas de upp (fragmentering), vilket kan påverka prestanda.

## Brandvägg & Säkerhet

### ufw (Uncomplicated Firewall)

ufw är ett användarvänligt gränssnitt för iptables.

```bash
# Aktivera ufw
sudo ufw enable

# Tillåt SSH (viktigt innan du aktiverar!)
sudo ufw allow 22/tcp

# Tillåt HTTP och HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Tillåt från specifik IP
sudo ufw allow from 192.168.1.0/24

# Blockera port
sudo ufw deny 3306/tcp

# Visa status
sudo ufw status

# Visa numrerade regler
sudo ufw status numbered

# Ta bort regel
sudo ufw delete 3
```

### NAT (Network Address Translation)

NAT låter flera enheter i ett privat nätverk dela på en enda publik IP-adress.

```bash
# NAT fungerar så här:
# 1. Privat nätverk (192.168.1.0/24) använder privata IP:ar
# 2. Router har publik IP (t.ex. 203.0.113.1)
# 3. När en enhet skickar paket ut:
#    - Router ändrar source IP från 192.168.1.10 till 203.0.113.1
#    - Router sparar mappningen i NAT-tabellen
# 4. När svar kommer tillbaka:
#    - Router tittar i NAT-tabellen
#    - Router ändrar destination IP tillbaka till 192.168.1.10
```

**Användning**: Hemnätverk, företagsnätverk - alla delar samma publik IP.

### Port Forwarding

Port Forwarding är när en router skickar trafik som kommer till en specifik port vidare till en enhet i det lokala nätverket.

```bash
# Exempel: Port forwarding på router
# Externa port 8080 → Intern 192.168.1.10:80

# När någon ansluter till router:8080,
# router skickar trafiken vidare till 192.168.1.10:80
```

**Användning**: Exponera tjänster i privat nätverk till internet.

### Destination Host Unreachable

Om ping visar "Destination Host Unreachable" betyder det att din server inte vet vilken väg (rutt) den ska ta för att nå den IP-adressen.

```bash
# Problem: Ingen rutt till destination
ping 10.0.0.50
# From 192.168.1.10 icmp_seq=1 Destination Host Unreachable

# Lösning: Kontrollera routing table
ip route show
# Lägg till rutt om nödvändigt
sudo ip route add 10.0.0.0/24 via 192.168.1.1
```

## Viktiga takeaways

- **IPv4**: Nätverks-ID + Host-ID, bestäms av subnätmask
- **Subnetting**: /24 = 254 hosts, /27 = 30 hosts, /29 = 6 hosts (formel: 2^(32-n) - 2)
- **APIPA (169.254.x.x)**: Automatisk IP när DHCP misslyckas
- **OSI-modellen**: 7 lager - Physical, Data Link (Ethernet), Network (IP), Transport (TCP/UDP), Session, Presentation, Application
- **TCP 3-way handshake**: SYN → SYN-ACK → ACK
- **TCP flaggor**: SYN, ACK, FIN, RST, PSH, URG
- **ICMP**: Används för ping, traceroute, felmeddelanden
- **DNS CNAME**: Alias som pekar på ett annat namn
- **TTL**: Hur länge DNS-post kan cachas (hög TTL = långsam propagation)
- **Well-known ports (0-1023)**: Reserverade för systemtjänster
- **Socket**: Kombination av IP-adress och portnummer (t.ex. 192.168.1.10:80)
- **ARP**: Översätter IP-adress till MAC-adress i lokalt nätverk
- **ip link**: Hantera nätverksinterfaces (up, down, rename)
- **DHCP Lease Time**: Tid en enhet får behålla IP-adress
- **tcpdump**: Avancerad packet capture för nätverksanalys
- **nmap**: Skanna nätverk efter öppna portar och tjänster
- **ss -tulpen**: Visa lyssnande portar med process-ID
- **ufw**: Användarvänlig brandvägg för iptables
- **NAT**: Flera enheter delar samma publik IP
- **Port Forwarding**: Router skickar trafik vidare till intern enhet
- **Bandwidth**: Maximal data per sekund, **Latency**: Fördröjning
- **MTU**: Maximal paketstorlek (standard 1500 bytes)
- **TCP**: Connection-oriented, reliable, ordered
- **UDP**: Connectionless, unreliable, faster
- **DNS**: Först /etc/hosts, sedan /etc/resolv.conf
- **Localhost**: 127.0.0.1 är loopback, isolerad i containers
- **Port mapping**: Använd `-p` för att nå container-localhost från host
