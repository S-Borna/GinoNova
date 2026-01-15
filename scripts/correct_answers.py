#!/usr/bin/env python3
"""
Correct answer mappings for all Nod3-10 quiz questions
Created by manually validating each question against DevOps/Linux knowledge
"""

# Format: 'nod-topic-qN': correct_index (0=A, 1=B, 2=C, 3=D)

CORRECT_ANSWERS = {
    # ===== NOD1: FILSYSTEM & GRUNDER (50 questions) =====
    'nod1-filsystem-q1': 3,   # Boot binärer → D: /bin
    'nod1-filsystem-q2': 1,   # SSH config → B: /etc/ssh/sshd_config
    'nod1-filsystem-q3': 0,   # /tmp syfte → A: Temporära filer raderas vid omstart
    'nod1-filsystem-q4': 0,   # Hårdvara → A: Representeras som filer i /dev
    'nod1-filsystem-q5': 3,   # Diskutrymme → D: df -h
    'nod1-filsystem-q6': 1,   # Radera katalog → B: rm -r
    'nod1-filsystem-q7': 2,   # Hard vs Symbolic → C: Symbolic fungerar över partitioner
    'nod1-filsystem-q8': 3,   # Skapa symlink → D: ln -s data.txt link.txt
    'nod1-filsystem-q9': 2,   # cd hemkatalog fungerar ej → C: cd /root
    'nod1-filsystem-q10': 3,  # pwd → D: Print Working Directory
    'nod1-filsystem-q11': 2,  # Auto-mount → C: /etc/fstab
    'nod1-filsystem-q12': 2,  # Mount Point → C: En katalog där filsystem görs tillgängligt
    'nod1-filsystem-q13': 0,  # Visa fil sida för sida → A: less
    'nod1-filsystem-q14': 1,  # . i början → B: Dold fil
    'nod1-filsystem-q15': 3,  # Sökvägs-separator → D: Forward slash /
    'nod1-filsystem-q16': 3,  # touch på befintlig fil → D: Uppdaterar tidsstämpel
    'nod1-filsystem-q17': 1,  # Processer → B: /proc
    'nod1-filsystem-q18': 3,  # Kopiera och byta namn → D: Både A och C fungerar
    'nod1-filsystem-q19': 2,  # /dev/null → C: Kastar all data
    'nod1-filsystem-q20': 1,  # Detaljerad lista → B: ls -l
    'nod1-filsystem-q21': 1,  # Absolut sökväg → B: Börjar från /
    'nod1-filsystem-q22': 1,  # Krypterad volym → B: Partition -> LUKS -> Filsystem
    'nod1-filsystem-q23': 1,  # Variable data → B: /var
    'nod1-filsystem-q24': 1,  # mv mellan partitioner → B: Kopierar och tar bort
    'nod1-filsystem-q25': 2,  # ext4 → C: Filsystem för Linux
    'nod1-filsystem-q26': 1,  # Sista raderna → B: tail
    'nod1-filsystem-q27': 1,  # Återställa rm → B: Går normalt inte
    'nod1-filsystem-q28': 3,  # Hemkataloger → D: /home
    'nod1-filsystem-q29': 1,  # .. → B: Föräldrakatalogen
    'nod1-filsystem-q30': 2,  # mkdir hela strukturen → C: mkdir -p
    'nod1-filsystem-q31': 0,  # /opt → A: Optional mjukvara
    'nod1-filsystem-q32': 1,  # hosts fil → B: /etc/hosts
    'nod1-filsystem-q33': 1,  # r-x på katalog → B: Läsa och gå in
    'nod1-filsystem-q34': 2,  # Visa RAM → C: free -h
    'nod1-filsystem-q35': 3,  # cd utan arg → D: Hemkatalogen
    'nod1-filsystem-q36': 1,  # Biblioteksfiler → B: /lib eller /usr/lib
    'nod1-filsystem-q37': 0,  # Monterade partitioner → A: cat /proc/mounts eller mount
    'nod1-filsystem-q38': 1,  # cat vs tac → B: tac baklänges
    'nod1-filsystem-q39': 1,  # Hitta binär → B: which python
    'nod1-filsystem-q40': 0,  # Device Node → A: Hårdvara som fil
    'nod1-filsystem-q41': 0,  # / full → A: Systemet kan krascha
    'nod1-filsystem-q42': 0,  # Användare och grupper → A: /etc
    'nod1-filsystem-q43': 1,  # ls -lh → B: Long format, Human readable
    'nod1-filsystem-q44': 2,  # Skapa tom fil → C: touch test
    'nod1-filsystem-q45': 1,  # /srv → B: Data för tjänster
    'nod1-filsystem-q46': 2,  # Kernel och boot → C: /boot
    'nod1-filsystem-q47': 1,  # Radera fil med mellanslag → B: rm -r "Mina Filer"
    'nod1-filsystem-q48': 1,  # cp -i → B: Interaktivt (frågar innan överskrivning)
    'nod1-filsystem-q49': 2,  # history → C: Kommandon du skrivit
    'nod1-filsystem-q50': 0,  # rx → A: Read, Execute

    # ===== NOD2: RÄTTIGHETER & SÄKERHET (50 questions) =====
    'nod2-rattigheter-q1': 3,   # rwxr-xr-- → D: 754
    'nod2-rattigheter-q2': 2,   # /etc/shadow → C: Krypterade lösenord
    'nod2-rattigheter-q3': 0,   # Grupp skrivrättighet → A: chmod g+w
    'nod2-rattigheter-q4': 2,   # Köra som root → C: sudo
    'nod2-rattigheter-q5': 1,   # Köra skript → B: Execute (x)
    'nod2-rattigheter-q6': 2,   # chown root:root → C: Ändrar ägare och grupp
    'nod2-rattigheter-q7': 1,   # rw------- → B: Bara ägaren
    'nod2-rattigheter-q8': 1,   # Sticky Bit → B: Bara ägaren får radera sin fil
    'nod2-rattigheter-q9': 0,   # Vem är jag → A: whoami
    'nod2-rattigheter-q10': 1,  # SSH-nycklar säkrare → B: Immuna mot Brute Force
    'nod2-rattigheter-q11': 2,  # .ssh rättigheter → C: ~/.ssh måste ha 700
    'nod2-rattigheter-q12': 1,  # usermod -aG sudo → B: Lägger till i gruppen
    'nod2-rattigheter-q13': 2,  # SSH port → C: /etc/ssh/sshd_config
    'nod2-rattigheter-q14': 2,  # UFW → C: Uncomplicated Firewall
    'nod2-rattigheter-q15': 1,  # Återställa root-lösenord → B: Single User Mode + passwd
    'nod2-rattigheter-q16': 1,  # id_rsa.pub → B: Publik nyckel
    'nod2-rattigheter-q17': 1,  # Låsa upp konto → B: usermod -U
    'nod2-rattigheter-q18': 1,  # drwxr-xr-x → B: Katalog
    'nod2-rattigheter-q19': 1,  # sudo användare → B: Bara i sudoers
    'nod2-rattigheter-q20': 1,  # Ta bort grupp → B: delgroup eller groupdel
    'nod2-rattigheter-q21': 1,  # SUID → B: Kör med filägarens behörighet
    'nod2-rattigheter-q22': 2,  # Stäng av UFW → C: ufw disable
    'nod2-rattigheter-q23': 0,  # Senast inloggade → A: last
    'nod2-rattigheter-q24': 0,  # /etc/group → A: Lista på grupper
    'nod2-rattigheter-q25': 0,  # UFW neka incoming → A: ufw default deny incoming
    'nod2-rattigheter-q26': 2,  # chmod 000 → C: Ingen utom root
    'nod2-rattigheter-q27': 1,  # Least Privilege → B: Bara nödvändiga rättigheter
    'nod2-rattigheter-q28': 2,  # Banna IP → C: Fail2Ban
    'nod2-rattigheter-q29': 1,  # Kopiera publik nyckel → B: ssh-copy-id
    'nod2-rattigheter-q30': 1,  # rw-r--r-- → B: 644
    'nod2-rattigheter-q31': 0,  # visudo → A: Öppnar /etc/sudoers med syntaxkontroll
    'nod2-rattigheter-q32': 1,  # + tecken → B: ACL utökade rättigheter
    'nod2-rattigheter-q33': 1,  # umask 644 → B: 022
    'nod2-rattigheter-q34': 2,  # UID 0 → C: root
    'nod2-rattigheter-q35': 0,  # Ändra lösenord för bob → A: passwd bob
    'nod2-rattigheter-q36': 1,  # sudoers alias → B: Gruppera kommandon/användare
    'nod2-rattigheter-q37': 1,  # chmod 777 dåligt → B: Säkerhetsrisk
    'nod2-rattigheter-q38': 0,  # su - → A: Login shell med roots miljö
    'nod2-rattigheter-q39': 0,  # Visa grupper → A: groups username
    'nod2-rattigheter-q40': 1,  # dictionary attack → B: Gissa lösenord med ordbok
    'nod2-rattigheter-q41': 1,  # kill default → B: SIGTERM (15)
    'nod2-rattigheter-q42': 0,  # /bin vs /sbin → A: /sbin för root
    'nod2-rattigheter-q43': 0,  # Ta bort w för others → A: chmod o-w
    'nod2-rattigheter-q44': 1,  # Ägare är siffra → B: Användaren finns inte längre
    'nod2-rattigheter-q45': 0,  # UFW textfil → A: /etc/ufw/before.rules
    'nod2-rattigheter-q46': 2,  # passwd -l → C: Låser kontot
    'nod2-rattigheter-q47': 0,  # Lösenordskryptering → A: SHA-512
    'nod2-rattigheter-q48': 0,  # Port Knocking → A: Dölj portar tills sekvens
    'nod2-rattigheter-q49': 1,  # Port 80 vanlig user → B: Nej, < 1024 kräver root
    'nod2-rattigheter-q50': 0,  # SELinux → A: Security Enhanced Linux

    # ===== NOD3: PROCESSHANTERING (48 questions) =====
    'nod3-processhantering-q1': 1,   # uptime shows → B: Hur länge datorn varit på + load average
    'nod3-processhantering-q2': 2,   # 2 cores, good load → C: Under 2.0
    'nod3-processhantering-q3': 3,   # kill default signal → D: SIGTERM (15)
    'nod3-processhantering-q4': 0,   # Zombie status Z → A: Dead, waiting for parent cleanup
    'nod3-processhantering-q5': 2,   # SIGINT keyboard → C: Ctrl+C
    'nod3-processhantering-q6': 1,   # Best real-time tool → B: htop
    'nod3-processhantering-q7': 1,   # nice command → B: Startar program med ändrad prioritet
    'nod3-processhantering-q8': 3,   # PID stands for → D: Process ID
    'nod3-processhantering-q9': 2,   # Start script in background → C: ./longjob.sh &
    'nod3-processhantering-q10': 1,  # Resume paused job → B: bg
    'nod3-processhantering-q11': 2,  # Signal that can't be caught → C: SIGKILL
    'nod3-processhantering-q12': 2,  # RAM+Swap full → C: OOM Killer
    'nod3-processhantering-q13': 3,  # Memory in readable format → D: free -h
    'nod3-processhantering-q14': 0,  # PPID → A: Parent Process ID
    'nod3-processhantering-q15': 1,  # Filter for nginx → B: ps aux | grep nginx
    'nod3-processhantering-q16': 1,  # Load Average meaning → B: Processer i kö för CPU/IO
    'nod3-processhantering-q17': 1,  # Number of signals → B: Över 60 st
    'nod3-processhantering-q18': 0,  # Kill all firefox → A: killall firefox
    'nod3-processhantering-q19': 2,  # nohup & → C: Fortsätter efter logout
    'nod3-processhantering-q20': 0,  # top NI column → A: Nice value
    'nod3-processhantering-q21': 0,  # Daemon → A: Bakgrundsprocess
    'nod3-processhantering-q22': 1,  # PID 1 → B: Init/Systemd
    'nod3-processhantering-q23': 0,  # If SIGTERM doesn't work → A: kill -9
    'nod3-processhantering-q24': 2,  # Status D → C: Uninterruptible sleep (Disk I/O)
    'nod3-processhantering-q25': 3,  # Process tree → D: pstree
    'nod3-processhantering-q26': 3,  # htop visual → D: Staplar/Bars
    'nod3-processhantering-q27': 1,  # load 0.50 → B: Halva CPU används (single core)
    'nod3-processhantering-q28': 3,  # User kill others → D: Nej, bara sina egna
    'nod3-processhantering-q29': 2,  # Swap thrashing → C: Slut på RAM, flyttar data ständigt
    'nod3-processhantering-q30': 1,  # Show open files → B: lsof
    'nod3-processhantering-q31': 0,  # Foreground process → A: Låser terminalen
    'nod3-processhantering-q32': 2,  # Kill hung process → C: Ctrl+C
    'nod3-processhantering-q33': 2,  # vmstat 1 → C: Uppdaterar varje sekund
    'nod3-processhantering-q34': 1,  # fg without arg → B: Senaste bakgrundsjobbet
    'nod3-processhantering-q35': 3,  # SIGHUP for servers → D: Reload config
    'nod3-processhantering-q36': 3,  # CPU Affinity → D: Låst till specifik CPU-kärna
    'nod3-processhantering-q37': 0,  # All processes all users → A: ps aux
    'nod3-processhantering-q38': 0,  # renice +10 → A: Sänker prioriteten
    'nod3-processhantering-q39': 3,  # PID for ssh fastest → D: Alla fungerar, pgrep/pidof är bäst
    'nod3-processhantering-q40': 0,  # Zombie parent dies → A: Adopteras av init
    'nod3-processhantering-q41': 0,  # cron → A: Tidsschemaläggare
    'nod3-processhantering-q42': 2,  # Total memory file → C: /proc/meminfo
    'nod3-processhantering-q43': 1,  # User vs Kernel space → B: Begränsad vs full åtkomst
    'nod3-processhantering-q44': 3,  # Send signal 9 to PID 500 → D: kill -9 500
    'nod3-processhantering-q45': 2,  # Static system info at login → C: landscape-sysinfo
    'nod3-processhantering-q46': 3,  # TTY shows ? → D: Inte kopplad till terminal (daemon)
    'nod3-processhantering-q47': 0,  # Why avoid kill -9 → A: Kan lämna korrupta filer
    'nod3-processhantering-q48': 0,  # iotop shows → A: Disk I/O per process
    'nod3-processhantering-q49': 2,  # Remove jobs → C: kill dem eller vänta
    'nod3-processhantering-q50': 0,  # Process → A: Ett program som körs i minnet

    # ===== NOD4: NÄTVERK & SERVER (50 questions) =====
    'nod4-natverk-q1': 0,   # Show IP addresses → A: ip addr
    'nod4-natverk-q2': 2,   # /24 subnet mask → C: 255.255.255.0
    'nod4-natverk-q3': 3,   # Broadcast 192.168.1.0/24 → D: 192.168.1.255
    'nod4-natverk-q4': 3,   # 169.254 address → D: DHCP failed (APIPA)
    'nod4-natverk-q5': 3,   # Router layer → D: Lager 3
    'nod4-natverk-q6': 3,   # Video streaming protocol → D: UDP
    'nod4-natverk-q7': 3,   # 3-way handshake initiator → D: Klienten
    'nod4-natverk-q8': 2,   # https 's' → C: Secure (TLS/SSL)
    'nod4-natverk-q9': 2,   # List listening ports → C: ss -tulpn
    'nod4-natverk-q10': 3,  # Map minserver to IP → D: /etc/hosts
    'nod4-natverk-q11': 1,  # Destination Unreachable → B: ICMP meddelande
    'nod4-natverk-q12': 2,  # IPv4 addresses → C: 4.3 miljarder
    'nod4-natverk-q13': 1,  # Show TCP handshake → B: tcpdump
    'nod4-natverk-q14': 3,  # SYN flag purpose → D: Synkronisera sekvensnummer
    'nod4-natverk-q15': 1,  # SSH default port → B: 22
    'nod4-natverk-q16': 0,  # Private IP → A: 172.16.0.5
    'nod4-natverk-q17': 3,  # resolv.conf → D: DNS-servrar
    'nod4-natverk-q18': 0,  # ip link show → A: MAC-adresser och status
    'nod4-natverk-q19': 0,  # File transfer protocol → A: FTP
    'nod4-natverk-q20': 3,  # Wrong gateway → D: Kan nå lokala men inte internet
    'nod4-natverk-q21': 3,  # 127.0.0.1 vs 0.0.0.0 → D: 127.0.0.1 bara lokalt, 0.0.0.0 från alla interface
    'nod4-natverk-q22': 0,  # Reset TCP flag → A: RST
    'nod4-natverk-q23': 1,  # Query specific DNS → B: dig @8.8.8.8 host
    'nod4-natverk-q24': 1,  # CIDR → B: Classless Inter-Domain Routing
    'nod4-natverk-q25': 3,  # /30 usable IPs → D: 2
    'nod4-natverk-q26': 3,  # ping protocol → D: ICMP
    'nod4-natverk-q27': 3,  # curl → D: Laddar ner och visar HTML
    'nod4-natverk-q28': 1,  # Socket statistics → B: ss
    'nod4-natverk-q29': 3,  # eth0/ens33 → D: Interface-namn
    'nod4-natverk-q30': 0,  # Temporary failure → A: DNS fungerar inte
    'nod4-natverk-q31': 1,  # No route match → B: Default Gateway
    'nod4-natverk-q32': 3,  # MAC address → D: 48 bitar
    'nod4-natverk-q33': 1,  # Load Balancer HTTP headers → B: Lager 7
    'nod4-natverk-q34': 3,  # Secure email port → D: 25/587
    'nod4-natverk-q35': 1,  # TTL → B: Hopp router får passera
    'nod4-natverk-q36': 1,  # traceroute → B: Visar routrar på vägen
    'nod4-natverk-q37': 3,  # A record → D: A record
    'nod4-natverk-q38': 1,  # AAAA record → B: AAAA (IPv6)
    'nod4-natverk-q39': 1,  # Latency → B: Fördröjning
    'nod4-natverk-q40': 3,  # Show IPv6 → D: ip -6 addr
    'nod4-natverk-q41': 0,  # MTU → A: Maximum Transmission Unit
    'nod4-natverk-q42': 2,  # Packet > MTU → C: Fragmenteras eller kastas
    'nod4-natverk-q43': 3,  # Show routing table → D: ip route show
    'nod4-natverk-q44': 0,  # 127.0.0.1 → A: Localhost
    'nod4-natverk-q45': 2,  # Time Exceeded protocol → C: ICMP
    'nod4-natverk-q46': 0,  # /8 netmask → A: 255.0.0.0
    'nod4-natverk-q47': 3,  # MySQL port → D: 3306
    'nod4-natverk-q48': 3,  # NAT purpose → D: Dela publik IP
    'nod4-natverk-q49': 3,  # Check cable → D: ip link
    'nod4-natverk-q50': 1,  # 10.0.0.0/8 → B: Privat nätverk

    # ===== NOD5: SSH & KOMMUNIKATION (50 questions) =====
    'nod5-ssh-q1': 1,   # Generate SSH key → B: ssh-keygen
    'nod5-ssh-q2': 3,   # Private key file → D: id_rsa
    'nod5-ssh-q3': 0,   # First connection → A: yes
    'nod5-ssh-q4': 1,   # ssh-copy-id purpose → B: Kopiera publik nyckel
    'nod5-ssh-q5': 0,   # authorized_keys → A: ~/.ssh/authorized_keys
    'nod5-ssh-q6': 0,   # Non-standard port → A: -p
    'nod5-ssh-q7': 0,   # -D 8080 → A: Dynamic port forward (SOCKS)
    'nod5-ssh-q8': 2,   # .ssh 777 → C: SSH vägrar pga bad ownership
    'nod5-ssh-q9': 3,   # Remember passphrase → D: ssh-agent
    'nod5-ssh-q10': 2,  # sshd_config → C: /etc/ssh/sshd_config
    'nod5-ssh-q11': 3,  # Passphrase → D: Lösenord för privat nyckel
    'nod5-ssh-q12': 0,  # Agent Forwarding → A: Låta server använda lokal nyckel
    'nod5-ssh-q13': 0,  # Modern algorithm → A: Ed25519
    'nod5-ssh-q14': 2,  # Permission denied publickey → C: Nyckel finns inte i authorized_keys
    'nod5-ssh-q15': 1,  # Disable password auth → B: PasswordAuthentication no
    'nod5-ssh-q16': 1,  # -L 8080:localhost:80 → B: Tunnlar lokal 8080 till fjärr localhost:80
    'nod5-ssh-q17': 3,  # Server fingerprints → D: known_hosts
    'nod5-ssh-q18': 0,  # After sshd_config change → A: Restart sshd
    'nod5-ssh-q19': 2,  # 2FA → C: Kräva nyckel och lösenord/2FA
    'nod5-ssh-q20': 0,  # Show public key → A: cat ~/.ssh/id_rsa.pub
    'nod5-ssh-q21': 3,  # ssh vs scp → D: ssh för remote, scp för filer
    'nod5-ssh-q22': 1,  # Private key permissions → B: 600
    'nod5-ssh-q23': 3,  # Lost private key → D: Ta bort publik från servrar, generera nytt par
    'nod5-ssh-q24': 3,  # Root login risk → D: Angripare vet användarnamnet
    'nod5-ssh-q25': 0,  # Remove host from known_hosts → A: ssh-keygen -R hostname
    'nod5-ssh-q26': 3,  # SSH transport → D: TCP
    'nod5-ssh-q27': 0,  # Connection refused → A: SSH inte installerat/startat
    'nod5-ssh-q28': 2,  # SSH shortcuts → C: ~/.ssh/config
    'nod5-ssh-q29': 1,  # IdentityFile → B: Sökväg till privat nyckel
    'nod5-ssh-q30': 2,  # Automate without password → C: Ja, nyckel utan passphrase
    'nod5-ssh-q31': 3,  # -v flag → D: Verbose mode
    'nod5-ssh-q32': 2,  # OpenSSH → C: SSH implementation
    'nod5-ssh-q33': 0,  # Fingerprint → A: Hash som identifierar nyckeln
    'nod5-ssh-q34': 1,  # SSH version → B: SSH-2
    'nod5-ssh-q35': 3,  # ssh-add -D → D: Ta bort alla nycklar från agent
    'nod5-ssh-q36': 0,  # Unprotected private key → A: chmod 600
    'nod5-ssh-q37': 2,  # Jump host → C: Mellanhandsserver för isolerade nätverk
    'nod5-ssh-q38': 0,  # Remote Port Forwarding → A: Servern kan komma åt din laptop
    'nod5-ssh-q39': 1,  # Public key format → B: Börjar med ssh-rsa/ssh-ed25519
    'nod5-ssh-q40': 0,  # Password attempts → A: 3
    'nod5-ssh-q41': 2,  # ssh-keyscan automation → C: Automatiskt lägga till servernycklar
    'nod5-ssh-q42': 3,  # Change port forgot firewall → D: Stänger ute sig själv
    'nod5-ssh-q43': 3,  # PermitEmptyPasswords → D: no
    'nod5-ssh-q44': 0,  # KeepAlive → A: Skickar paket mot timeout
    'nod5-ssh-q45': 3,  # Edit authorized_keys → D: Använd nano/vim
    'nod5-ssh-q46': 1,  # Same key multiple servers → B: Ja
    'nod5-ssh-q47': 3,  # Passphrase-less key → D: Vem som helst kan använda filen
    'nod5-ssh-q48': 0,  # RSA 1024 → A: Knäckt/för svag
    'nod5-ssh-q49': 3,  # -C comment → D: Lägger till kommentar
    'nod5-ssh-q50': 1,  # Most info flag → B: -v (-vv, -vvv)

    # ===== NOD6: BASH SKRIPT (50 questions) =====
    'nod6-bash-q1': 3,   # First line → D: #!/bin/bash
    'nod6-bash-q2': 0,   # set -u → A: Fel vid odefinierad variabel
    'nod6-bash-q3': 0,   # Test file exists → A: [[ -f "data.txt" ]]
    'nod6-bash-q4': 0,   # $# → A: Antal argument
    'nod6-bash-q5': 0,   # Assign string → A: MSG="Hej"
    'nod6-bash-q6': 1,   # Pipeline → B: |
    'nod6-bash-q7': 0,   # pipefail → A: Hela pipeline fail om något misslyckas
    'nod6-bash-q8': 0,   # $1 → A: Första argumentet
    'nod6-bash-q9': 0,   # Iterate arguments → A: for arg in "$@"
    'nod6-bash-q10': 3,  # Exit with error → D: exit 1
    'nod6-bash-q11': 2,  # read -p → C: Skriver prompt, sparar svar
    'nod6-bash-q12': 1,  # Single vs double quotes → B: Enkel tolkar inte variabler
    'nod6-bash-q13': 0,  # Not equal integer → A: -ne
    'nod6-bash-q14': 0,  # trap EXIT → A: Tar bort temp vid avslut
    'nod6-bash-q15': 2,  # Safe temp file → C: mktemp
    'nod6-bash-q16': 0,  # shift → A: Tar bort $1, flyttar $2→$1
    'nod6-bash-q17': 2,  # String length → C: ${#NAME}
    'nod6-bash-q18': 0,  # && operator → A: Kör 2 bara om 1 lyckades
    'nod6-bash-q19': 1,  # || operator → B: Kör 2 bara om 1 misslyckades
    'nod6-bash-q20': 0,  # Exit status → A: $?
    'nod6-bash-q21': 0,  # Default value → A: word
    'nod6-bash-q22': 0,  # read with prompt → A: read -p
    'nod6-bash-q23': 0,  # exec → A: Ersätter shell med kommando
    'nod6-bash-q24': 1,  # Debug mode → B: set -x
    'nod6-bash-q25': 2,  # Comment → C: #
    'nod6-bash-q26': 0,  # Function → A: Återanvändbart kodblock
    'nod6-bash-q27': 1,  # Avoid ls in scripts → B: Hanterar inte mellanslag korrekt
    'nod6-bash-q28': 2,  # Check syntax → C: bash -n script.sh
    'nod6-bash-q29': 1,  # env bash → B: env letar i PATH
    'nod6-bash-q30': 2,  # export → C: export PATH
    'nod6-bash-q31': 0,  # SIGINT → A: Signal Interrupt (Ctrl+C)
    'nod6-bash-q32': 2,  # -z test → C: Tom sträng
    'nod6-bash-q33': 1,  # Math → B: (( 1 + 1 )) eller $(( ))
    'nod6-bash-q34': 0,  # dirname → A: Returnerar /var/log
    'nod6-bash-q35': 1,  # basename → B: Returnerar syslog
    'nod6-bash-q36': 1,  # local → B: Skriver inte över global
    'nod6-bash-q37': 1,  # Wait background → B: wait
    'nod6-bash-q38': 0,  # sleep 5 → A: Pausar 5 sekunder
    'nod6-bash-q39': 0,  # $! → A: PID senaste bakgrundsjobb
    'nod6-bash-q40': 1,  # Check root → B: if [[ $EUID -eq 0 ]]
    'nod6-bash-q41': 1,  # tee → B: Skriver till stdout och fil
    'nod6-bash-q42': 1,  # Login shell file → B: .bash_profile/.profile
    'nod6-bash-q43': 1,  # source → B: Kör i nuvarande shell
    'nod6-bash-q44': 1,  # Infinite loop → B: while true
    'nod6-bash-q45': 1,  # 2> /dev/null → B: Tysta felmeddelanden
    'nod6-bash-q46': 0,  # Cut parts → A: cut
    'nod6-bash-q47': 0,  # Replace in variable → A: ${TEXT/foo/bar}
    'nod6-bash-q48': 0,  # nounset → A: Samma som set -u
    'nod6-bash-q49': 1,  # grep -q → B: Bara matchning, inte text
    'nod6-bash-q50': 1,  # Command Substitution → B: $(date)

    # ===== NOD7: BASH VERKTYG (50 questions) =====
    'nod7-verktyg-q1': 1,   # Append → B: >>
    'nod7-verktyg-q2': 2,   # ls > overwrites → C: Filen skrivs över
    'nod7-verktyg-q3': 0,   # stderr number → A: 2
    'nod7-verktyg-q4': 0,   # grep -v → A: Rader som INTE innehåller
    'nod7-verktyg-q5': 2,   # Column 3 tool → C: awk/cut
    'nod7-verktyg-q6': 3,   # Sort numerically → D: sort -n
    'nod7-verktyg-q7': 3,   # uniq requires → D: Sorterad fil
    'nod7-verktyg-q8': 0,   # wc -l → A: Räknar rader
    'nod7-verktyg-q9': 2,   # Replace foo bar → C: sed 's/foo/bar/'
    'nod7-verktyg-q10': 0,  # ^Error → A: Börjar med Error
    'nod7-verktyg-q11': 2,  # Follow log → C: tail -f
    'nod7-verktyg-q12': 2,  # tr a-z A-Z → C: Gemener till versaler
    'nod7-verktyg-q13': 2,  # Whole line in awk → C: $0
    'nod7-verktyg-q14': 3,  # head -n 5 → D: Visar 5 första
    'nod7-verktyg-q15': 0,  # grep -r → A: Rekursivt
    'nod7-verktyg-q16': 0,  # xargs purpose → A: Kör rm för varje fil
    'nod7-verktyg-q17': 3,  # grep line numbers → D: -n
    'nod7-verktyg-q18': 1,  # 2>&1 → B: stderr till stdout
    'nod7-verktyg-q19': 2,  # Screen and file → C: tee
    'nod7-verktyg-q20': 2,  # Count duplicates → C: uniq -c
    'nod7-verktyg-q21': 2,  # sed -i → C: In-place editing
    'nod7-verktyg-q22': 1,  # . regex → B: Vilket tecken som helst
    'nod7-verktyg-q23': 3,  # Last 100 lines → D: tail -n 100
    'nod7-verktyg-q24': 0,  # awk -F: → A: Kolon som avgränsare
    'nod7-verktyg-q25': 2,  # grep quiet → C: -q
    'nod7-verktyg-q26': 2,  # awk END NR → C: Totala rader
    'nod7-verktyg-q27': 3,  # Reverse sort → D: sort -r
    'nod7-verktyg-q28': 1,  # tr -d digits → B: Tar bort siffror
    'nod7-verktyg-q29': 2,  # [^...] negation → C: ^
    'nod7-verktyg-q30': 2,  # cut -c 1-5 → C: Tecken 1-5
    'nod7-verktyg-q31': 1,  # fgrep → B: Fixed strings (no regex)
    'nod7-verktyg-q32': 3,  # sed '5d' → D: Raderar rad 5
    'nod7-verktyg-q33': 0,  # xargs spaces → A: -0 med find -print0
    'nod7-verktyg-q34': 2,  # ls | wc -l → C: Räknar filer
    'nod7-verktyg-q35': 2,  # sort -k2 → C: Sorterar kolumn 2
    'nod7-verktyg-q36': 3,  # [0-9]{3} → D: Tre siffror
    'nod7-verktyg-q37': 0,  # Print col 1,3 → A: awk '{print $1, $3}'
    'nod7-verktyg-q38': 2,  # grep -A 2 → C: Visar 2 rader EFTER
    'nod7-verktyg-q39': 2,  # comm → C: Jämför sorterade filer
    'nod7-verktyg-q40': 1,  # uniq without sort → B: Bara intilliggande dubbletter
    'nod7-verktyg-q41': 3,  # paste → D: Slår ihop horisontellt
    'nod7-verktyg-q42': 2,  # Remove trailing space → C: sed 's/ *$//'
    'nod7-verktyg-q43': 1,  # Black hole → B: /dev/null
    'nod7-verktyg-q44': 0,  # $ regex → A: Slut på rad
    'nod7-verktyg-q45': 3,  # CSV to tab → D: tr ',' '\t'
    'nod7-verktyg-q46': 2,  # grep -c → C: Räknar matchande rader
    'nod7-verktyg-q47': 2,  # sed in pipeline → C: Ingen flagga behövs
    'nod7-verktyg-q48': 2,  # awk NR==5 → C: Skriver ut rad 5
    'nod7-verktyg-q49': 2,  # Invert sort → C: sort -r
    'nod7-verktyg-q50': 2,  # Here Document → C: Flerradig text till stdin

    # ===== NOD8: DOCKER ISOLERING (50 questions) =====
    'nod8-docker-q1': 1,   # Container vs VM → B: Lättvikt, delad kernel
    'nod8-docker-q2': 0,   # Crashed status → A: Exited
    'nod8-docker-q3': 0,   # Download image → A: docker pull
    'nod8-docker-q4': 2,   # <none>:<none> → C: Dangling image
    'nod8-docker-q5': 0,   # RUN when → A: Build time
    'nod8-docker-q6': 2,   # docker search → C: Söker Docker Hub
    'nod8-docker-q7': 0,   # Remove image used → A: -f or remove container
    'nod8-docker-q8': 1,   # .dockerignore → B: Exkluderar från build context
    'nod8-docker-q9': 1,   # Multi-stage build → B: Hålla imagen liten
    'nod8-docker-q10': 0,  # Name container → A: --name
    'nod8-docker-q11': 1,  # ENV → B: Sätter miljövariabel
    'nod8-docker-q12': 1,  # Image filesystem → B: Union File System
    'nod8-docker-q13': 0,  # Container IP → A: docker inspect
    'nod8-docker-q14': 0,  # attach vs exec → A: attach=PID1, exec=ny process
    'nod8-docker-q15': 2,  # Two CMD → C: Sista gäller
    'nod8-docker-q16': 1,  # EXPOSE port → B: Bara dokumentation
    'nod8-docker-q17': 3,  # Other Dockerfile → D: -f och --file funkar
    'nod8-docker-q18': 1,  # FROM scratch → B: Tom image
    'nod8-docker-q19': 1,  # docker kill → B: SIGKILL
    'nod8-docker-q20': 1,  # Docker Hub → B: Registry
    'nod8-docker-q21': 1,  # Comment in Dockerfile → B: #
    'nod8-docker-q22': 1,  # CMD when → B: Container start
    'nod8-docker-q23': 2,  # Run container → C: docker run
    'nod8-docker-q24': 1,  # Registry → B: Image storage
    'nod8-docker-q25': 0,  # Update image → A: docker pull
    'nod8-docker-q26': 1,  # HEALTHCHECK → B: Kontrollera om container mår bra
    'nod8-docker-q27': 0,  # Images storage → A: /var/lib/docker
    'nod8-docker-q28': 1,  # CLI -e vs ENV → B: -e skriver över
    'nod8-docker-q29': 0,  # Copy FROM container → A: docker cp container:/path .
    'nod8-docker-q30': 1,  # Copy TO container → B: docker cp fil container:/path
    'nod8-docker-q31': 1,  # ONBUILD → B: Trigger vid FROM inheritance
    'nod8-docker-q32': 1,  # Windows container OS → B: Windows Server Core/Nano
    'nod8-docker-q33': 1,  # Login Docker Hub → B: docker login
    'nod8-docker-q34': 0,  # --restart always → A: Startar alltid om
    'nod8-docker-q35': 1,  # inspect --format → B: Go-templates
    'nod8-docker-q36': 1,  # Image history → B: docker history
    'nod8-docker-q37': 1,  # Volume removed? → B: Finns kvar på host
    'nod8-docker-q38': 1,  # SHELL → B: Ändra standardskal
    'nod8-docker-q39': 0,  # Limit CPU → A: --cpus="0.5"
    'nod8-docker-q40': 1,  # LABEL → B: Metadata
    'nod8-docker-q41': 0,  # Docker Daemon → A: Bakgrundstjänst
    'nod8-docker-q42': 1,  # -t in build → B: Taggar imagen
    'nod8-docker-q43': 1,  # EXPOSE → B: Dokumenterar port
    'nod8-docker-q44': 1,  # Disk usage → B: docker system df
    'nod8-docker-q45': 0,  # One-time container → A: --rm
    'nod8-docker-q46': 1,  # No isolation network → B: Host
    'nod8-docker-q47': 0,  # Layer Caching → A: Återanvänder steg
    'nod8-docker-q48': 1,  # Alpine → B: Minimal Linux distro
    'nod8-docker-q49': 1,  # ENTRYPOINT when → B: Container start
    'nod8-docker-q50': 2,  # PID 1 → C: CMD/ENTRYPOINT process

    # ===== NOD9: DOCKER NÄTVERK & LAGRING (50 questions) =====
    'nod9-natverk-q1': 0,   # Networks connected → A: docker inspect
    'nod9-natverk-q2': 1,   # No isolation → B: Host
    'nod9-natverk-q3': 0,   # Map ports → A: -p
    'nod9-natverk-q4': 0,   # -p 3000:80 → A: Host 3000 → container 80
    'nod9-natverk-q5': 3,   # Reach host services → D: host.docker.internal
    'nod9-natverk-q6': 0,   # volume prune → A: Tar bort oanvända
    'nod9-natverk-q7': 2,   # Networks per container → C: Obegränsat
    'nod9-natverk-q8': 0,   # 127.0.0.11 → A: Docker DNS
    'nod9-natverk-q9': 0,   # User-defined bridge removal → A: Manuellt
    'nod9-natverk-q10': 1,  # Prod database storage → B: Volume
    'nod9-natverk-q11': 0,  # -v /data → A: Anonym volym
    'nod9-natverk-q12': 0,  # Published Port → A: Mappad från host
    'nod9-natverk-q13': 1,  # Multi-host network → B: Overlay
    'nod9-natverk-q14': 0,  # network disconnect → A: Kopplar bort
    'nod9-natverk-q15': 0,  # Read-only mount → A: :ro
    'nod9-natverk-q16': 1,  # Show interfaces → B: ip addr
    'nod9-natverk-q17': 1,  # Static IP → B: --ip (user-defined net)
    'nod9-natverk-q18': 0,  # Mount to existing dir → A: Ärver filer
    'nod9-natverk-q19': 0,  # Subnetting → A: Definiera IP-adressrymder
    'nod9-natverk-q20': 0,  # Volumes location → A: /var/lib/docker/volumes/
    'nod9-natverk-q21': 0,  # User-defined vs default bridge → A: User har DNS
    'nod9-natverk-q22': 0,  # File over dir → A: Mappen ersätts
    'nod9-natverk-q23': 0,  # Create network with DNS → A: docker network create
    'nod9-natverk-q24': 1,  # Change container IP → B: Återskapa
    'nod9-natverk-q25': 0,  # See mounts → A: docker inspect
    'nod9-natverk-q26': 1,  # local driver → B: Lokal disk
    'nod9-natverk-q27': 1,  # Bind Mount advantage → B: Redigera kod live
    'nod9-natverk-q28': 0,  # Bind Mount remote → A: Filer måste finnas
    'nod9-natverk-q29': 0,  # Remove ALL → A: system prune -a --volumes
    'nod9-natverk-q30': 0,  # Share volume → A: Ja
    'nod9-natverk-q31': 0,  # Same host port → A: Andra misslyckas
    'nod9-natverk-q32': 0,  # Dangling volume → A: Inte refererad
    'nod9-natverk-q33': 2,  # tmpfs → C: RAM-lagring
    'nod9-natverk-q34': 1,  # Find IP → B: docker inspect
    'nod9-natverk-q35': 1,  # Macvlan → B: Egna MAC-adresser
    'nod9-natverk-q36': 0,  # ping db fails → A: Default Bridge saknar DNS
    'nod9-natverk-q37': 2,  # Best performance → C: Host
    'nod9-natverk-q38': 0,  # network ls → A: Listar nätverk
    'nod9-natverk-q39': 1,  # Transfer volume data → B: Container med båda monterade
    'nod9-natverk-q40': 0,  # Mount files → A: Ja
    'nod9-natverk-q41': 0,  # Use host network → A: Max prestanda, ej isolering
    'nod9-natverk-q42': 0,  # Remove container with volume → A: Volymen kvar
    'nod9-natverk-q43': 0,  # Bind denied → A: File Sharing settings
    'nod9-natverk-q44': 1,  # DNS file → B: /etc/resolv.conf
    'nod9-natverk-q45': 0,  # docker port → A: Visar portar
    'nod9-natverk-q46': 0,  # none network → A: Bara loopback
    'nod9-natverk-q47': 1,  # Connect network → B: network connect
    'nod9-natverk-q48': 0,  # Compose default → A: Skapar default nätverk
    'nod9-natverk-q49': 0,  # Use IP addresses → A: Ja men inte rekommenderat
    'nod9-natverk-q50': 0,  # Internet only → A: Standard (ej publicerade portar)

    # ===== NOD10: DOCKER COMPOSE & IaC (50 questions) =====
    'nod10-compose-q1': 1,   # depends_on → B: Startordning, väntar ej på app
    'nod10-compose-q2': 2,   # Rebuild → C: up --build
    'nod10-compose-q3': 1,   # Override priority → B: override vinner
    'nod10-compose-q4': 1,   # Volume driver → B: driver: local
    'nod10-compose-q5': 1,   # No YAML file → B: Felmeddelande
    'nod10-compose-q6': 0,   # List networks → A: docker network ls
    'nod10-compose-q7': 1,   # Scale → B: --scale service=10
    'nod10-compose-q8': 1,   # logs web → B: Visar bara web
    'nod10-compose-q9': 1,   # .env → B: Laddas automatiskt
    'nod10-compose-q10': 1,  # context: . → B: Nuvarande katalog
    'nod10-compose-q11': 2,  # Stop and remove → C: down
    'nod10-compose-q12': 2,  # Reach db → C: Via namnet db
    'nod10-compose-q13': 1,  # restart on-failure → B: Exit != 0
    'nod10-compose-q14': 2,  # Detached → C: -d
    'nod10-compose-q15': 1,  # config → B: Validering
    'nod10-compose-q16': 2,  # Named Volume removal → C: Manuellt/down -v
    'nod10-compose-q17': 1,  # Run in running → B: exec
    'nod10-compose-q18': 2,  # ports vs expose → C: ports till host, expose internt
    'nod10-compose-q19': 2,  # Immutable Infrastructure → C: Byt ut, ändra ej
    'nod10-compose-q20': 2,  # Environment vars → C: environment:
    'nod10-compose-q21': 0,  # compose stop → A: Stoppar, behåller data
    'nod10-compose-q22': 2,  # deploy key version → C: Version 3
    'nod10-compose-q23': 1,  # Same host port → B: Krock
    'nod10-compose-q24': 0,  # Force recreate → A: --force-recreate
    'nod10-compose-q25': 2,  # Default network → C: Bridge
    'nod10-compose-q26': 1,  # Ignore files → B: .dockerignore
    'nod10-compose-q27': 0,  # init: true → A: Init-process för signaler
    'nod10-compose-q28': 0,  # Mount current dir → A: - .:/code
    'nod10-compose-q29': 0,  # container_name → A: Fast namn, förhindrar skalning
    'nod10-compose-q30': 0,  # Remove orphans → A: --remove-orphans
    'nod10-compose-q31': 1,  # command: → B: Override CMD
    'nod10-compose-q32': 1,  # Multiple networks → B: Ja, tjänst kan vara med i flera
    'nod10-compose-q33': 3,  # healthcheck advantage → D: Alla
    'nod10-compose-q34': 1,  # Default user → B: Root
    'nod10-compose-q35': 1,  # compose pull → B: Ladda ner senaste images
    'nod10-compose-q36': 0,  # stdin_open tty → A: Interaktivt (-it)
    'nod10-compose-q37': 1,  # Bad YAML → B: Parse error
    'nod10-compose-q38': 0,  # volumes_from → A: Montera från annan container
    'nod10-compose-q39': 1,  # Show ports → B: ps
    'nod10-compose-q40': 1,  # Remote host → B: DOCKER_HOST
    'nod10-compose-q41': 1,  # Bind mount → B: Host mapp
    'nod10-compose-q42': 0,  # sysctls → A: Kernel-parametrar
    'nod10-compose-q43': 0,  # Host network → A: network_mode: host
    'nod10-compose-q44': 0,  # Custom dockerfile → A: context + dockerfile
    'nod10-compose-q45': 3,  # Inactivate service → D: Alla sätt möjliga
    'nod10-compose-q46': 0,  # logging → A: Loggkonfig
    'nod10-compose-q47': 2,  # All interfaces → C: 0.0.0.0
    'nod10-compose-q48': 0,  # cap_add → A: Capabilities
    'nod10-compose-q49': 1,  # entrypoint when → B: Container start
    'nod10-compose-q50': 1,  # IaC benefit → B: Reproducerbarhet
}

def get_correct_answer(question_id: str) -> int:
    """Get correct answer index for a question ID"""
    return CORRECT_ANSWERS.get(question_id, 0)  # Default to 0 if not found
