/**
 * DOE25 Linux Tenta Flashcards
 * Datum: 7 januari 2026 kl 09:30
 * 
 * KURSSPECIFIKA (75 st) + PRINTABLE (65 st) = 140 flashcards totalt
 * Baserade på föreläsningar, hands-on övningar och kursmaterial
 */

export interface Flashcard {
  front: string;
  back: string;
}

export const DOE25_FLASHCARDS: Record<string, Flashcard[]> = {
  // ═══════════════════════════════════════════════════════════════════════════
  // KURSMÅL 1: FELSÖKNING
  // ═══════════════════════════════════════════════════════════════════════════
  "KM1 - Felsökning": [
    // PRINTABLE
    {
      front: "Var finns systemloggar i Linux?",
      back: "/var/log/ (syslog, auth.log, kern.log, messages)"
    },
    {
      front: "Kommando för att visa loggar för SSH-tjänsten?",
      back: "journalctl -u ssh eller journalctl -u sshd"
    },
    {
      front: "Skillnad mellan kill och kill -9?",
      back: "kill = SIGTERM (snäll, cleanup)\nkill -9 = SIGKILL (tvångsavslut)"
    },
    {
      front: "Hur listar du lyssnande portar?",
      back: "ss -tuln (t=tcp, u=udp, l=listening, n=numeriskt)"
    },
    {
      front: "Visa diskutrymme per partition?",
      back: "df -h (-h = human readable)"
    },
    {
      front: "Hur startar du en tjänst automatiskt vid boot?",
      back: "systemctl enable tjänstnamn"
    },
    {
      front: "Felsökningsprocessen i ordning?",
      back: "1. Identifiera → 2. Reproducera → 3. Isolera → 4. Diagnostisera → 5. Åtgärda → 6. Verifiera → 7. Dokumentera"
    },
    {
      front: "Hur följer du loggar i realtid?",
      back: "journalctl -f eller tail -f /var/log/syslog"
    },
    // KURSSPECIFIK
    {
      front: "Vilka tre grundsteg följer du vid felsökning?",
      back: "1) Definiera problemet (vad, när, ändringar), 2) Samla info (loggar, status), 3) Testa hypoteser systematiskt"
    },
    {
      front: "SSH fungerar inte. Vilka fyra saker kontrollerar du?",
      back: "1) Är sshd igång? (systemctl status sshd), 2) Rätt port? (ss -tuln), 3) Brandvägg? (ufw/firewall-cmd), 4) Nyckelrättigheter? (700 på .ssh, 600 på authorized_keys)"
    },
    {
      front: "Hur testar du om SSH-konfigurationen är syntaktiskt korrekt?",
      back: "sudo sshd -t (ingen output = OK)"
    }
  ],

  // ═══════════════════════════════════════════════════════════════════════════
  // KURSMÅL 2: LAGRING
  // ═══════════════════════════════════════════════════════════════════════════
  "KM2 - Lagring": [
    // PRINTABLE
    {
      front: "Vad innehåller /etc/?",
      back: "Konfigurationsfiler (textbaserade, redigerbara)"
    },
    {
      front: "Vad innehåller /var/log/?",
      back: "Loggfiler"
    },
    {
      front: "Skillnad ext4 och XFS?",
      back: "ext4: standard, stabilt\nXFS: stora filer, enterprise"
    },
    {
      front: "Vad är journaling?",
      back: "Loggar ändringar innan de görs → möjliggör återställning vid krasch"
    },
    {
      front: "Vad gör LVM?",
      back: "Abstraktion mellan disk och filsystem → dynamisk storleksändring utan omstart"
    },
    {
      front: "Skillnad hård vs symbolisk länk?",
      back: "Hård: samma inode, överlever om original tas bort\nSymbolisk: pekare till filnamn, bryts om original tas bort"
    },
    {
      front: "RAID 0 vs RAID 1 vs RAID 5?",
      back: "RAID 0: striping, ingen redundans\nRAID 1: mirroring, 1 disk kan dö\nRAID 5: striping+paritet, 1 disk kan dö"
    },
    {
      front: "Kommando: visa blockenheter?",
      back: "lsblk eller lsblk -f (med filsystem)"
    }
  ],

  // ═══════════════════════════════════════════════════════════════════════════
  // KURSMÅL 3: RÄTTIGHETER & ANVÄNDARHANTERING
  // ═══════════════════════════════════════════════════════════════════════════
  "KM3 - Rättigheter & Användare": [
    // PRINTABLE
    {
      front: "rwxr-xr-- i numerisk form?",
      back: "754 (rwx=7, r-x=5, r--=4)"
    },
    {
      front: "Vad gör chmod 600?",
      back: "rw------- (endast ägaren kan läsa/skriva)"
    },
    {
      front: "Vad gör chmod u+s?",
      back: "Sätter SUID → programmet körs som filens ägare"
    },
    {
      front: "Vad gör sticky bit (+t)?",
      back: "På katalog: bara ägaren kan ta bort sina egna filer (ex: /tmp)"
    },
    {
      front: "Hur gör du nya filer i katalog ärver gruppägare?",
      back: "SGID: chmod g+s katalog eller chmod 2755 katalog"
    },
    {
      front: "Tvinga lösenordsbyte vid nästa inloggning?",
      back: "chage -d 0 användarnamn"
    },
    {
      front: "Var konfigureras sudo?",
      back: "/etc/sudoers (redigera med visudo)"
    },
    {
      front: "Skillnad /etc/passwd och /etc/shadow?",
      back: "passwd: användarinfo (alla kan läsa)\nshadow: krypterade lösenord (endast root)"
    },
    // KURSSPECIFIK - Från Hands-on 1 dec
    {
      front: "Vad gör kommandot useradd -m Alice?",
      back: "Skapar användaren Alice med en hemkatalog under /home/Alice. Flaggan -m skapar hemkatalogen automatiskt."
    },
    {
      front: "Vad gör usermod -aG developers Alice?",
      back: "Lägger till Alice i gruppen developers som sekundär grupp. -a = append (lägg till utan att ta bort befintliga grupper), -G = sekundär grupp."
    },
    {
      front: "Hur verifierar du vilka grupper Alice tillhör?",
      back: "groups Alice eller id Alice"
    },
    {
      front: "Vad är skillnaden mellan primär och sekundär grupp?",
      back: "Primär grupp (GID i /etc/passwd) - filer skapas med denna grupp som standard. Sekundär grupp - extra grupptillhörighet för access till resurser."
    },
    {
      front: "Vad gör chmod 2770 /opt/developers?",
      back: "Sätter SGID-bit (2) + rwx för ägare (7) + rwx för grupp (7) + ingen access för others (0). SGID gör att nya filer i katalogen automatiskt ärver gruppägaren."
    },
    {
      front: "Hur tvingar du en användare att byta lösenord vid nästa inloggning?",
      back: "sudo passwd --expire användarnamn eller sudo chage -d 0 användarnamn"
    },
    {
      front: "Vad innehåller /etc/passwd?",
      back: "Användarinformation: användarnamn:x:UID:GID:kommentar:hemkatalog:shell. \"x\" betyder att lösenordet finns i /etc/shadow."
    },
    {
      front: "Vad innehåller /etc/shadow?",
      back: "Krypterade lösenord och lösenordspolicy (utgångsdatum, min/max dagar mellan byten, etc.)"
    },
    {
      front: "Vilka behörigheter måste ~/.ssh ha för att SSH ska fungera?",
      back: "~/.ssh måste vara 700, ~/.ssh/authorized_keys måste vara 600. För strikta eller lösa behörigheter = SSH vägrar."
    },
    {
      front: "Vad betyder rwxr-xr-- i siffror?",
      back: "754. Ägare: rwx=7, Grupp: r-x=5, Others: r--=4"
    },
    {
      front: "Vad är sticky bit och var används den?",
      back: "Sticky bit (chmod 1xxx) på en katalog gör att endast filägaren kan radera sina filer, även om andra har skrivbehörighet. Används på /tmp."
    }
  ],

  // ═══════════════════════════════════════════════════════════════════════════
  // KURSMÅL 4: ADMINISTRATION, SSH & BRANDVÄGG
  // ═══════════════════════════════════════════════════════════════════════════
  "KM4 - Administration & Säkerhet": [
    // PRINTABLE
    {
      front: "Skillnad apt remove vs apt purge?",
      back: "remove: tar bort program, behåller config\npurge: tar bort allt inkl. config"
    },
    {
      front: "Vad gör systemctl daemon-reload?",
      back: "Läser om service-filer efter ändringar"
    },
    {
      front: "Cron: varje måndag kl 03:00?",
      back: "0 3 * * 1 kommando (min tim dag mån veckodag)"
    },
    {
      front: "Vad är multi-user.target?",
      back: "Systemd-target för fleranvändarläge utan GUI (motsvarar runlevel 3)"
    },
    {
      front: "Lista misslyckade systemd-tjänster?",
      back: "systemctl list-units --failed"
    },
    {
      front: "Sätt hostname permanent?",
      back: "hostnamectl set-hostname nyttnamn"
    },
    // KURSSPECIFIK - Systemd & Tjänster
    {
      front: "Hur startar du en tjänst?",
      back: "sudo systemctl start tjänstnamn"
    },
    {
      front: "Hur gör du att en tjänst startar automatiskt vid boot?",
      back: "sudo systemctl enable tjänstnamn"
    },
    {
      front: "Hur ser du detaljerad status för en tjänst?",
      back: "systemctl status tjänstnamn"
    },
    {
      front: "Hur ser du loggar för en specifik tjänst?",
      back: "journalctl -u tjänstnamn"
    },
    {
      front: "Hur ser du de senaste systemfelen med förklaringar?",
      back: "journalctl -xe"
    },
    // KURSSPECIFIK - SSH Härdning (från föreläsningen 19 nov)
    {
      front: "Vilken port använder SSH som standard?",
      back: "Port 22"
    },
    {
      front: "Varför byter man SSH-port från 22?",
      back: "För att minska automatiserade attacker/scans som riktar sig mot standardporten. Inte säkerhet i sig, men reducerar \"noise\"."
    },
    {
      front: "Var lägger du SSH-härdningskonfiguration enligt kursen?",
      back: "/etc/ssh/sshd_config.d/01-hardening.conf - en egen fil i .d-katalogen för att undvika att ändringar skrivs över vid uppdateringar."
    },
    {
      front: "Vilka fyra inställningar härdade ni SSH med?",
      back: "Port 6622, PasswordAuthentication no, PermitRootLogin no, AllowUsers said"
    },
    {
      front: "Vad händer efter du ändrat SSH-config?",
      back: "Du måste köra sudo systemctl restart sshd för att ladda om konfigurationen."
    },
    {
      front: "Hur kopierar du din SSH-nyckel till en server?",
      back: "ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server eller manuellt genom att lägga den i ~/.ssh/authorized_keys på servern."
    },
    {
      front: "Vad är skillnaden mellan ed25519 och RSA nycklar?",
      back: "ed25519 är modernare, kortare nycklar (256 bit), snabbare. RSA är äldre, längre nycklar (2048-4096 bit), kompatibelt med allt."
    },
    {
      front: "Hur förenklar du SSH-inloggning med config-fil?",
      back: "Skapa ~/.ssh/config med Host-block som anger HostName, User, Port, IdentityFile. Sedan kan du köra ssh värdnamn istället för hela kommandot."
    },
    {
      front: "Varför fungerade inte port 6622 på Fedora i kursen?",
      back: "SELinux blockerade icke-standardportar för SSH. Lösning: semanage port -a -t ssh_port_t -p tcp 6622 eller använd port 22."
    },
    // KURSSPECIFIK - Brandvägg
    {
      front: "Vad heter brandväggsverktyget i Ubuntu?",
      back: "UFW (Uncomplicated Firewall)"
    },
    {
      front: "Vad heter brandväggsverktyget i Fedora/RHEL?",
      back: "FirewallD"
    },
    {
      front: "Hur tillåter du port 6622 med UFW?",
      back: "sudo ufw allow 6622/tcp följt av sudo ufw enable (om inte redan aktiverad)"
    },
    {
      front: "Hur tillåter du port 6622 med FirewallD permanent?",
      back: "sudo firewall-cmd --permanent --add-port=6622/tcp följt av sudo firewall-cmd --reload"
    },
    {
      front: "Hur ser du nuvarande brandväggsregler i UFW?",
      back: "sudo ufw status eller sudo ufw status verbose"
    },
    {
      front: "Hur ser du nuvarande brandväggsregler i FirewallD?",
      back: "sudo firewall-cmd --list-all"
    }
  ],

  // ═══════════════════════════════════════════════════════════════════════════
  // KURSMÅL 5: NÄTVERK & OSI-MODELLEN
  // ═══════════════════════════════════════════════════════════════════════════
  "KM5 - Nätverk": [
    // PRINTABLE
    {
      front: "OSI-lagren 1-7 (nerifrån)?",
      back: "Physical, Data Link, Network, Transport, Session, Presentation, Application"
    },
    {
      front: "Minnesregel OSI (uppifrån)?",
      back: "\"Alla Personer Som Talar Norska Dricker Fanta\""
    },
    {
      front: "TCP vs UDP?",
      back: "TCP: tillförlitlig, connection-oriented, handshake\nUDP: snabb, connectionless, best-effort"
    },
    {
      front: "TCP 3-way handshake?",
      back: "1. SYN → 2. SYN-ACK ← 3. ACK →"
    },
    {
      front: "Hur många hosts i /24?",
      back: "254 (2^8 - 2 = 256 - 2)"
    },
    {
      front: "Hur många hosts i /26?",
      back: "62 (2^6 - 2 = 64 - 2)"
    },
    {
      front: "Privata IP-intervall?",
      back: "10.0.0.0/8\n172.16.0.0/12\n192.168.0.0/16"
    },
    {
      front: "Port: SSH, HTTP, HTTPS, DNS?",
      back: "22, 80, 443, 53"
    },
    {
      front: "Visa routing-tabell?",
      back: "ip r eller ip route"
    },
    {
      front: "Dela 192.168.1.0/24 i 4 subnät: vilken mask?",
      back: "/26 (256/4 = 64 per subnät)"
    },
    // KURSSPECIFIK - Från föreläsningen 24 nov
    {
      front: "Vad är formeln för att beräkna antal hostar i ett subnät?",
      back: "2^(32-prefix) - 2. Minus 2 för nätadress och broadcast."
    },
    {
      front: "Hur många hostar rymmer ett /24-nät?",
      back: "254 hostar. 2^(32-24) - 2 = 2^8 - 2 = 256 - 2 = 254"
    },
    {
      front: "Hur många hostar rymmer ett /27-nät?",
      back: "30 hostar. 2^(32-27) - 2 = 2^5 - 2 = 32 - 2 = 30"
    },
    {
      front: "Vad är nätadressen för 137.92.49.86/17?",
      back: "137.0.0.0. Binärmetoden: /17 ger gräns mitt i andra oktetten. Alla hostbitar sätts till 0."
    },
    {
      front: "Vad är broadcast för 137.92.49.86/17?",
      back: "137.127.255.255. Alla hostbitar sätts till 1."
    },
    {
      front: "Vad är subnätmasken för /24?",
      back: "255.255.255.0"
    },
    {
      front: "Vad är subnätmasken för /27?",
      back: "255.255.255.224. De 27 första bitarna är 1:or = 11111111.11111111.11111111.11100000"
    },
    {
      front: "Vad är NAT och varför behövs det?",
      back: "Network Address Translation. Flera interna enheter delar en publik IP. Behövs pga IPv4-adressbrist."
    },
    {
      front: "Vilka är de privata IP-adresserna (RFC 1918)?",
      back: "10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16"
    },
    {
      front: "Vad är DNS?",
      back: "Domain Name System. Översätter domännamn (google.com) till IP-adresser."
    },
    {
      front: "Vad är en A-post i DNS?",
      back: "En post som pekar ett domännamn till en IPv4-adress."
    },
    {
      front: "Vad är en MX-post i DNS?",
      back: "Mail eXchange - pekar ut vilken server som tar emot e-post för domänen."
    },
    {
      front: "Vad är TTL i nätverkssammanhang?",
      back: "Time To Live. Räknare som minskar för varje router-hop. Förhindrar oändliga routingloopar."
    },
    {
      front: "Hur fungerar traceroute?",
      back: "Skickar paket med ökande TTL (1, 2, 3...). Varje router som droppar paketet svarar, vilket visar nätverksvägen."
    },
    {
      front: "Om ping 8.8.8.8 fungerar men ping google.com inte fungerar, vad är problemet?",
      back: "DNS-problem. Nätverket fungerar men namnuppslag misslyckas."
    },
    {
      front: "Vilket kommando visar öppna portar på ett modernt Linux-system?",
      back: "ss -tuln (-t=TCP, -u=UDP, -l=listening, -n=numeriskt)"
    },
    {
      front: "Hur visar du IP-adresser på moderna Linux-system?",
      back: "ip addr eller ip a (äldre: ifconfig)"
    },
    // KURSSPECIFIK - OSI-modellen
    {
      front: "Vilka är de 7 lagren i OSI-modellen (uppifrån och ner)?",
      back: "7-Application, 6-Presentation, 5-Session, 4-Transport, 3-Network, 2-Data Link, 1-Physical"
    },
    {
      front: "På vilket OSI-lager finns IP-adresser?",
      back: "Lager 3 - Network"
    },
    {
      front: "På vilket OSI-lager finns portnummer?",
      back: "Lager 4 - Transport (TCP/UDP)"
    },
    {
      front: "På vilket OSI-lager finns MAC-adresser?",
      back: "Lager 2 - Data Link"
    },
    {
      front: "Vad är skillnaden mellan TCP och UDP?",
      back: "TCP = tillförlitlig, connection-oriented, kontrollerar att data kommer fram. UDP = snabbare, connectionless, ingen garanti för leverans."
    }
  ],

  // ═══════════════════════════════════════════════════════════════════════════
  // KURSMÅL 6: BACKUP & ARKIVERING
  // ═══════════════════════════════════════════════════════════════════════════
  "KM6 - Backup": [
    // PRINTABLE
    {
      front: "3-2-1-regeln?",
      back: "3 kopior, 2 medier, 1 off-site"
    },
    {
      front: "Full vs inkrementell backup?",
      back: "Full: allt varje gång\nInkrementell: endast ändringar sedan senast"
    },
    {
      front: "Skapa komprimerat tar-arkiv?",
      back: "tar -czvf arkiv.tar.gz /katalog"
    },
    {
      front: "Extrahera tar-arkiv?",
      back: "tar -xzvf arkiv.tar.gz"
    },
    {
      front: "Fördel rsync vs cp?",
      back: "Kopierar bara ändringar (deltasync), kan återupptas"
    },
    {
      front: "rsync över SSH?",
      back: "rsync -avz källa user@server:/mål"
    },
    // KURSSPECIFIK
    {
      front: "Vad gör tar -czvf backup.tar.gz /folder?",
      back: "Skapar (-c) ett gzip-komprimerat (-z) arkiv med verbose output (-v) till filen (-f) backup.tar.gz innehållande /folder."
    },
    {
      front: "Hur extraherar du backup.tar.gz?",
      back: "tar -xzvf backup.tar.gz (-x = extract)"
    },
    {
      front: "Vad är fördelen med rsync jämfört med cp?",
      back: "rsync kopierar bara ändringar (inkrementellt), kan synka över nätverk, kan komprimera under överföring."
    },
    {
      front: "Vad betyder rsync -av --delete source/ dest/?",
      back: "Arkiverar med verbose, och --delete tar bort filer i dest som inte finns i source (fullständig speglig)."
    }
  ],

  // ═══════════════════════════════════════════════════════════════════════════
  // KURSMÅL 7: DOCKER
  // ═══════════════════════════════════════════════════════════════════════════
  "KM7 - Docker": [
    // PRINTABLE
    {
      front: "Container vs VM?",
      back: "Container: delar kernel, MB, sekunder\nVM: full OS, GB, minuter"
    },
    {
      front: "Skillnad image vs container?",
      back: "Image: read-only mall\nContainer: körande instans av image"
    },
    {
      front: "docker run -d -p 8080:80 nginx?",
      back: "Startar nginx i bakgrunden, mappar host:8080 → container:80"
    },
    {
      front: "Hur sparar du data permanent i Docker?",
      back: "Volymer: -v volymnamn:/sökväg eller bind mount"
    },
    {
      front: "Lista körande containers?",
      back: "docker ps"
    },
    {
      front: "Öppna shell i container?",
      back: "docker exec -it containernamn bash"
    },
    {
      front: "Vilka Linux-teknologier möjliggör containers?",
      back: "Namespaces (isolering) + Cgroups (resursbegränsning)"
    },
    // KURSSPECIFIK
    {
      front: "Vad är huvudskillnaden mellan en container och en VM?",
      back: "Container delar värdmaskinens kernel (lättare, snabbare start). VM har eget OS med egen kernel (tyngre, full isolering)."
    },
    {
      front: "Vad gör docker run -d -p 8080:80 nginx?",
      back: "Kör nginx-imagen i bakgrunden (-d = detached) och mappar lokal port 8080 till containerns port 80."
    },
    {
      front: "Hur listar du körande containers?",
      back: "docker ps (lägg till -a för att se stoppade också)"
    },
    {
      front: "Hur ser du loggar från en container?",
      back: "docker logs <container_id>"
    },
    {
      front: "Hur kör du ett kommando inuti en körande container?",
      back: "docker exec -it <container_id> bash (eller annat kommando)"
    }
  ],

  // ═══════════════════════════════════════════════════════════════════════════
  // KURSMÅL 8: GIT
  // ═══════════════════════════════════════════════════════════════════════════
  "KM8 - Git": [
    // PRINTABLE
    {
      front: "Vad är staging area?",
      back: "Mellansteg där du väljer vad som inkluderas i nästa commit"
    },
    {
      front: "Skillnad fetch vs pull?",
      back: "fetch: hämtar utan merge\npull: fetch + merge"
    },
    {
      front: "Skapa branch och byt till den?",
      back: "git checkout -b branchnamn"
    },
    {
      front: "Ångra pushad commit säkert?",
      back: "git revert <commit-hash> (skapar ny commit som ångrar)"
    },
    {
      front: "Visa commit-historik kompakt?",
      back: "git log --oneline"
    },
    {
      front: "Lägg till alla ändringar till staging?",
      back: "git add ."
    },
    {
      front: "Vad är .gitignore?",
      back: "Fil som anger vilka filer Git ska ignorera"
    },
    // KURSSPECIFIK
    {
      front: "Vad gör git add .?",
      back: "Lägger alla ändrade filer i working directory till staging area."
    },
    {
      front: "Vad är skillnaden mellan staging area och repository?",
      back: "Staging area = förberedelsezon för nästa commit. Repository = faktiska versionshistoriken."
    },
    {
      front: "Vad gör git commit -m \"message\"?",
      back: "Skapar en permanent snapshot av staging area med beskrivande meddelande."
    },
    {
      front: "Hur skapar och byter du till en ny branch i ett kommando?",
      back: "git checkout -b branch-name eller nyare: git switch -c branch-name"
    },
    {
      front: "Hur mergar du en feature-branch till main?",
      back: "git checkout main sedan git merge feature-branch"
    }
  ],

  // ═══════════════════════════════════════════════════════════════════════════
  // BONUS: SNABBTEST
  // ═══════════════════════════════════════════════════════════════════════════
  "Bonus - Snabbtest": [
    {
      front: "5 viktiga kataloger i Linux?",
      back: "/etc (config), /var (variabel data), /home (användare), /tmp (temporärt), /opt (program)"
    },
    {
      front: "3 kommandon för att kolla systemhälsa?",
      back: "df -h (disk), free -h (RAM), top (processer)"
    },
    {
      front: "Starta, stoppa, status för tjänst?",
      back: "systemctl start/stop/status tjänst"
    },
    {
      front: "Skapa användare med hemkatalog?",
      back: "useradd -m användarnamn"
    },
    {
      front: "Se vilka grupper en användare tillhör?",
      back: "groups användarnamn"
    }
  ]
};

// Statistik
export const DOE25_FLASHCARD_STATS = {
  totalCards: Object.values(DOE25_FLASHCARDS).flat().length,
  categories: Object.keys(DOE25_FLASHCARDS).length,
  examDate: new Date("2026-01-07T09:30:00+01:00"),
  source: "DOE25 Linux kurs - föreläsningar, hands-on övningar och kursmaterial"
};
