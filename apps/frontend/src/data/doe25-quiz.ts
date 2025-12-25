/**
 * DOE25 Linux Tenta Quiz
 * Datum: 7 januari 2026 kl 09:30
 *
 * Simulerade tentafrågor - G och VG-nivå
 * Baserade på kursmaterial KM1-KM8
 */

export interface QuizQuestion {
    question: string;
    options: string[];
    correctIndex: number;
    explanation: string;
    difficulty: "G" | "VG";
    kursmål: string;
}

export const DOE25_QUIZ: Record<string, QuizQuestion[]> = {
    // ═══════════════════════════════════════════════════════════════════════════
    // KURSMÅL 1: FELSÖKNING
    // ═══════════════════════════════════════════════════════════════════════════
    "KM1 - Felsökning": [
        {
            question: "En webbtjänst svarar inte. Vad är det FÖRSTA du bör kontrollera?",
            options: [
                "Om tjänsten körs: systemctl status nginx",
                "Brandväggsregler: firewall-cmd --list-all",
                "DNS-inställningar",
                "Omstarta servern"
            ],
            correctIndex: 0,
            explanation: "Börja alltid med att verifiera att tjänsten faktiskt körs innan du felsöker andra komponenter.",
            difficulty: "G",
            kursmål: "KM1"
        },
        {
            question: "Var finns systemloggar i Linux?",
            options: [
                "/home/logs/",
                "/var/log/",
                "/etc/logs/",
                "/tmp/logs/"
            ],
            correctIndex: 1,
            explanation: "/var/log/ innehåller systemloggar som syslog, auth.log, kern.log, och messages.",
            difficulty: "G",
            kursmål: "KM1"
        },
        {
            question: "Vilket kommando visar loggar för SSH-tjänsten?",
            options: [
                "cat /var/log/ssh.log",
                "journalctl -u sshd",
                "systemctl logs ssh",
                "tail -f /etc/ssh/log"
            ],
            correctIndex: 1,
            explanation: "journalctl -u tjänstnamn visar loggar för specifika systemd-tjänster.",
            difficulty: "G",
            kursmål: "KM1"
        },
        {
            question: "Vad är skillnaden mellan kill och kill -9?",
            options: [
                "kill -9 är snällare och låter processen städa",
                "kill skickar SIGTERM (cleanup), kill -9 skickar SIGKILL (tvång)",
                "Det finns ingen skillnad",
                "kill -9 skickar signalen 9 gånger"
            ],
            correctIndex: 1,
            explanation: "kill = SIGTERM låter processen städa upp. kill -9 = SIGKILL tvångsavslutar utan cleanup.",
            difficulty: "G",
            kursmål: "KM1"
        },
        {
            question: "SSH fungerar inte. Vilken kombination av kontroller är korrekt?",
            options: [
                "DNS, webbserver, disk",
                "sshd-status, port (ss -tuln), brandvägg, nyckelrättigheter",
                "Bara kolla om servern är igång",
                "Installera om SSH"
            ],
            correctIndex: 1,
            explanation: "Kontrollera: 1) Är sshd igång? 2) Rätt port? 3) Brandvägg? 4) Nyckelrättigheter (700/600)?",
            difficulty: "VG",
            kursmål: "KM1"
        },
        {
            question: "Hur testar du om SSH-konfigurationen är syntaktiskt korrekt?",
            options: [
                "ssh --test",
                "systemctl test sshd",
                "sudo sshd -t",
                "cat /etc/ssh/sshd_config | grep error"
            ],
            correctIndex: 2,
            explanation: "sudo sshd -t testar syntaxen. Ingen output = konfigurationen är OK.",
            difficulty: "G",
            kursmål: "KM1"
        }
    ],

    // ═══════════════════════════════════════════════════════════════════════════
    // KURSMÅL 2: LAGRING
    // ═══════════════════════════════════════════════════════════════════════════
    "KM2 - Lagring": [
        {
            question: "Vad är skillnaden mellan ext4 och XFS?",
            options: [
                "ext4 är nyare och snabbare",
                "ext4: stabilt standard, XFS: bättre för stora filer/enterprise",
                "De är identiska",
                "XFS stöder inte journaling"
            ],
            correctIndex: 1,
            explanation: "ext4 är stabilt allround-filsystem. XFS är optimerat för stora filer och hög I/O i enterprise-miljöer.",
            difficulty: "G",
            kursmål: "KM2"
        },
        {
            question: "Vad är journaling i ett filsystem?",
            options: [
                "En loggbok för användare",
                "Loggar ändringar innan de görs för att möjliggöra återställning vid krasch",
                "Automatisk backup",
                "Komprimering av data"
            ],
            correctIndex: 1,
            explanation: "Journaling loggar planerade ändringar först, så systemet kan återställas konsistent efter en krasch.",
            difficulty: "G",
            kursmål: "KM2"
        },
        {
            question: "Vad gör LVM?",
            options: [
                "Krypterar diskar",
                "Abstraktionslager mellan disk och filsystem för dynamisk storleksändring",
                "Komprimerar data",
                "Skapar backup automatiskt"
            ],
            correctIndex: 1,
            explanation: "LVM (Logical Volume Manager) möjliggör flexibel hantering av diskutrymme utan omstart.",
            difficulty: "G",
            kursmål: "KM2"
        },
        {
            question: "Skillnad mellan hård och symbolisk länk?",
            options: [
                "Ingen skillnad",
                "Hård: samma inode (överlever om original tas bort). Symbolisk: pekare (bryts om original tas bort)",
                "Symbolisk är snabbare",
                "Hård länk fungerar bara på kataloger"
            ],
            correctIndex: 1,
            explanation: "Hård länk delar inode med originalet. Symbolisk länk är bara en pekare till filnamnet.",
            difficulty: "G",
            kursmål: "KM2"
        },
        {
            question: "Vad är RAID 5?",
            options: [
                "Mirroring av 2 diskar",
                "Striping utan redundans",
                "Striping med paritet, 3+ diskar, tolererar 1 diskfel",
                "5 diskar i serie"
            ],
            correctIndex: 2,
            explanation: "RAID 5 använder striping med paritet fördelat över minst 3 diskar. En disk kan gå sönder utan dataförlust.",
            difficulty: "G",
            kursmål: "KM2"
        },
        {
            question: "Vilket kommando visar blockenheter?",
            options: [
                "df -h",
                "lsblk",
                "mount",
                "fdisk"
            ],
            correctIndex: 1,
            explanation: "lsblk listar blockenheter. lsblk -f visar även filsystem.",
            difficulty: "G",
            kursmål: "KM2"
        }
    ],

    // ═══════════════════════════════════════════════════════════════════════════
    // KURSMÅL 3: RÄTTIGHETER
    // ═══════════════════════════════════════════════════════════════════════════
    "KM3 - Rättigheter": [
        {
            question: "Vad betyder rwxr-xr-- numeriskt?",
            options: [
                "644",
                "754",
                "755",
                "740"
            ],
            correctIndex: 1,
            explanation: "rwx=7, r-x=5, r--=4. Totalt 754.",
            difficulty: "G",
            kursmål: "KM3"
        },
        {
            question: "Vad gör chmod u+s (SUID)?",
            options: [
                "Sätter sticky bit",
                "Programmet körs som filens ägare",
                "Ger skrivrättigheter",
                "Tar bort alla rättigheter"
            ],
            correctIndex: 1,
            explanation: "SUID gör att programmet körs med filens ägares rättigheter, inte användarens.",
            difficulty: "G",
            kursmål: "KM3"
        },
        {
            question: "Vad gör sticky bit på en katalog?",
            options: [
                "Gör katalogen osynlig",
                "Bara ägaren kan ta bort sina egna filer",
                "Krypterar innehållet",
                "Gör alla filer skrivskyddade"
            ],
            correctIndex: 1,
            explanation: "Sticky bit (chmod +t) på katalog: användare kan bara radera sina egna filer. Används på /tmp.",
            difficulty: "G",
            kursmål: "KM3"
        },
        {
            question: "Hur tvingar du lösenordsbyte vid nästa inloggning?",
            options: [
                "passwd --force user",
                "chage -d 0 användarnamn",
                "usermod --expire user",
                "force-passwd user"
            ],
            correctIndex: 1,
            explanation: "chage -d 0 sätter sista lösenordsändring till 0, vilket tvingar byte vid nästa inloggning.",
            difficulty: "G",
            kursmål: "KM3"
        },
        {
            question: "Vad gör chmod 2770 /opt/developers?",
            options: [
                "Bara ägaren har access",
                "SGID + rwx för ägare + rwx för grupp + ingen access för others",
                "Sticky bit på katalogen",
                "Full access för alla"
            ],
            correctIndex: 1,
            explanation: "2=SGID (nya filer ärver grupp), 770=rwxrwx---. SGID gör att nya filer automatiskt ägs av kataloggruppen.",
            difficulty: "VG",
            kursmål: "KM3"
        },
        {
            question: "Vilka rättigheter måste ~/.ssh och ~/.ssh/authorized_keys ha?",
            options: [
                "777 och 666",
                "700 och 600",
                "755 och 644",
                "Spelar ingen roll"
            ],
            correctIndex: 1,
            explanation: "~/.ssh måste vara 700, authorized_keys måste vara 600. För lösa eller strikta = SSH vägrar.",
            difficulty: "G",
            kursmål: "KM3"
        },
        {
            question: "Skillnad mellan /etc/passwd och /etc/shadow?",
            options: [
                "Ingen skillnad",
                "passwd: användarinfo (läsbar), shadow: krypterade lösenord (endast root)",
                "shadow är för grupper",
                "passwd används inte längre"
            ],
            correctIndex: 1,
            explanation: "passwd innehåller användarinfo och är läsbar för alla. shadow innehåller hash av lösenord och läses bara av root.",
            difficulty: "G",
            kursmål: "KM3"
        }
    ],

    // ═══════════════════════════════════════════════════════════════════════════
    // KURSMÅL 4: ADMINISTRATION & SÄKERHET
    // ═══════════════════════════════════════════════════════════════════════════
    "KM4 - Administration": [
        {
            question: "Skillnad mellan apt remove och apt purge?",
            options: [
                "Ingen skillnad",
                "remove: tar bort program men behåller config. purge: tar bort allt",
                "purge är snabbare",
                "remove tar bort mer"
            ],
            correctIndex: 1,
            explanation: "apt remove behåller konfigurationsfiler. apt purge tar bort allt inklusive config.",
            difficulty: "G",
            kursmål: "KM4"
        },
        {
            question: "Vad gör systemctl daemon-reload?",
            options: [
                "Startar om alla tjänster",
                "Läser om service-filer efter ändringar",
                "Tar bort alla service-filer",
                "Visar status för daemon"
            ],
            correctIndex: 1,
            explanation: "daemon-reload laddar om systemd-konfiguration efter att du ändrat eller lagt till unit-filer.",
            difficulty: "G",
            kursmål: "KM4"
        },
        {
            question: "Cron-syntax för varje måndag kl 03:00?",
            options: [
                "3 0 * * 1 kommando",
                "0 3 * * 1 kommando",
                "* 3 * * mon kommando",
                "0 3 1 * * kommando"
            ],
            correctIndex: 1,
            explanation: "Format: minut timme dag månad veckodag. 0 3 * * 1 = minut 0, timme 3, varje dag, varje månad, måndag (1).",
            difficulty: "G",
            kursmål: "KM4"
        },
        {
            question: "Vilka fyra inställningar härdade ni SSH med i kursen?",
            options: [
                "Bara ändrade port",
                "Port 6622, PasswordAuthentication no, PermitRootLogin no, AllowUsers said",
                "Installerade extra paket",
                "Ändrade cipher"
            ],
            correctIndex: 1,
            explanation: "SSH-härdning: byt port, stäng av lösenordslogin, förbjud root-login, vitlista användare.",
            difficulty: "VG",
            kursmål: "KM4"
        },
        {
            question: "Hur tillåter du port 6622 med UFW?",
            options: [
                "ufw open 6622",
                "sudo ufw allow 6622/tcp",
                "firewall-cmd --add-port=6622",
                "iptables -A 6622"
            ],
            correctIndex: 1,
            explanation: "UFW (Ubuntu): sudo ufw allow 6622/tcp följt av sudo ufw enable.",
            difficulty: "G",
            kursmål: "KM4"
        },
        {
            question: "Varför fungerade inte port 6622 på Fedora i kursen?",
            options: [
                "Porten var upptagen",
                "SELinux blockerade icke-standardportar för SSH",
                "Fedora stöder inte andra portar",
                "Brandväggen var av"
            ],
            correctIndex: 1,
            explanation: "SELinux blockerar icke-standardportar. Lösning: semanage port -a -t ssh_port_t -p tcp 6622",
            difficulty: "VG",
            kursmål: "KM4"
        }
    ],

    // ═══════════════════════════════════════════════════════════════════════════
    // KURSMÅL 5: NÄTVERK
    // ═══════════════════════════════════════════════════════════════════════════
    "KM5 - Nätverk": [
        {
            question: "Vilka är OSI-modellens 7 lager (nerifrån)?",
            options: [
                "Application, Presentation, Session, Transport, Network, Data Link, Physical",
                "Physical, Data Link, Network, Transport, Session, Presentation, Application",
                "Network, Transport, Application, Session, Physical, Data Link, Presentation",
                "Physical, Network, Transport, Application, Session, Data Link, Presentation"
            ],
            correctIndex: 1,
            explanation: "Minnesregel uppifrån: Alla Personer Som Talar Norska Dricker Fanta",
            difficulty: "G",
            kursmål: "KM5"
        },
        {
            question: "TCP vs UDP - vad stämmer?",
            options: [
                "UDP är mer tillförlitligt",
                "TCP: tillförlitlig, connection-oriented. UDP: snabb, connectionless",
                "De är samma sak",
                "TCP används för streaming"
            ],
            correctIndex: 1,
            explanation: "TCP garanterar leverans och ordning (HTTP, SSH). UDP är snabbare men utan garanti (DNS, video, gaming).",
            difficulty: "G",
            kursmål: "KM5"
        },
        {
            question: "Hur många hosts rymmer ett /24-nät?",
            options: [
                "256",
                "254",
                "255",
                "252"
            ],
            correctIndex: 1,
            explanation: "2^8 - 2 = 256 - 2 = 254 hosts (minus nätverks- och broadcast-adress).",
            difficulty: "G",
            kursmål: "KM5"
        },
        {
            question: "Hur många hosts rymmer ett /27-nät?",
            options: [
                "32",
                "30",
                "28",
                "62"
            ],
            correctIndex: 1,
            explanation: "2^(32-27) - 2 = 2^5 - 2 = 32 - 2 = 30 hosts.",
            difficulty: "G",
            kursmål: "KM5"
        },
        {
            question: "Du har 192.168.10.0/24 och ska dela det i 4 subnät. Vilken mask får du?",
            options: [
                "/25",
                "/26",
                "/27",
                "/28"
            ],
            correctIndex: 1,
            explanation: "4 subnät = 2 extra bitar (2²=4). /24 + 2 = /26. Varje subnät = 64 adresser, 62 hosts.",
            difficulty: "G",
            kursmål: "KM5"
        },
        {
            question: "Vilka är de privata IP-intervallen (RFC 1918)?",
            options: [
                "192.168.0.0 endast",
                "10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16",
                "Alla IP-adresser",
                "127.0.0.0/8"
            ],
            correctIndex: 1,
            explanation: "RFC 1918 definierar tre privata intervall som inte routas på internet.",
            difficulty: "G",
            kursmål: "KM5"
        },
        {
            question: "Port för SSH, HTTP, HTTPS, DNS?",
            options: [
                "21, 80, 443, 53",
                "22, 80, 443, 53",
                "22, 8080, 443, 53",
                "23, 80, 443, 53"
            ],
            correctIndex: 1,
            explanation: "SSH=22, HTTP=80, HTTPS=443, DNS=53. Viktiga portar att memorera!",
            difficulty: "G",
            kursmål: "KM5"
        },
        {
            question: "Om ping 8.8.8.8 fungerar men ping google.com inte fungerar - vad är problemet?",
            options: [
                "Nätverkskortet är trasigt",
                "DNS-problem - nätverket fungerar men namnuppslag misslyckas",
                "Brandväggen blockerar allt",
                "Routern är trasig"
            ],
            correctIndex: 1,
            explanation: "IP-adress fungerar = nätverket OK. Domännamn fungerar inte = DNS-upplösning är problemet.",
            difficulty: "VG",
            kursmål: "KM5"
        },
        {
            question: "Förklara TCP 3-way handshake",
            options: [
                "ACK → SYN → SYN-ACK",
                "SYN → SYN-ACK → ACK",
                "SYN → ACK → SYN",
                "HELLO → OK → START"
            ],
            correctIndex: 1,
            explanation: "1) Klient: SYN (vill ansluta), 2) Server: SYN-ACK (OK, jag lyssnar), 3) Klient: ACK (fint, vi kör).",
            difficulty: "VG",
            kursmål: "KM5"
        },
        {
            question: "På vilket OSI-lager finns IP-adresser?",
            options: [
                "Lager 2 - Data Link",
                "Lager 3 - Network",
                "Lager 4 - Transport",
                "Lager 7 - Application"
            ],
            correctIndex: 1,
            explanation: "Lager 3 (Network) hanterar IP-adresser och routing.",
            difficulty: "G",
            kursmål: "KM5"
        }
    ],

    // ═══════════════════════════════════════════════════════════════════════════
    // KURSMÅL 6: BACKUP
    // ═══════════════════════════════════════════════════════════════════════════
    "KM6 - Backup": [
        {
            question: "Vad är 3-2-1-regeln?",
            options: [
                "3 servrar, 2 datacenter, 1 admin",
                "3 kopior, 2 medier, 1 off-site",
                "3 backups per dag",
                "3 GB minst, 2 partitioner, 1 fil"
            ],
            correctIndex: 1,
            explanation: "3-2-1: 3 kopior av data, på 2 olika medier, 1 lagras off-site (annan fysisk plats).",
            difficulty: "G",
            kursmål: "KM6"
        },
        {
            question: "Skillnad mellan full, inkrementell och differentiell backup?",
            options: [
                "Ingen skillnad",
                "Full: allt. Inkrementell: ändringar sedan senast. Differentiell: ändringar sedan senaste fulla.",
                "Full är mindre än inkrementell",
                "Differentiell är snabbast"
            ],
            correctIndex: 1,
            explanation: "Full = mest plats, snabbast restore. Inkrementell = minst plats, långsammast restore.",
            difficulty: "G",
            kursmål: "KM6"
        },
        {
            question: "Hur skapar du ett komprimerat tar-arkiv av /katalog?",
            options: [
                "tar /katalog backup.tar.gz",
                "tar -czvf backup.tar.gz /katalog",
                "zip -r backup.tar.gz /katalog",
                "gzip /katalog > backup.tar.gz"
            ],
            correctIndex: 1,
            explanation: "-c=Create, -z=gzip, -v=Verbose, -f=File. tar -czvf skapar komprimerat arkiv.",
            difficulty: "G",
            kursmål: "KM6"
        },
        {
            question: "Hur extraherar du backup.tar.gz?",
            options: [
                "tar -czvf backup.tar.gz",
                "tar -xzvf backup.tar.gz",
                "untar backup.tar.gz",
                "extract backup.tar.gz"
            ],
            correctIndex: 1,
            explanation: "-x=Extract istället för -c=Create. Resten är samma: -z=gzip, -v=verbose, -f=file.",
            difficulty: "G",
            kursmål: "KM6"
        },
        {
            question: "Vad är fördelen med rsync jämfört med cp?",
            options: [
                "rsync är alltid snabbare",
                "rsync kopierar bara ändringar (deltasync), kan återupptas",
                "cp fungerar över nätverk",
                "Ingen skillnad"
            ],
            correctIndex: 1,
            explanation: "rsync är smart: kopierar bara det som ändrats, kan komprimera, fungerar över SSH.",
            difficulty: "G",
            kursmål: "KM6"
        },
        {
            question: "Vad betyder rsync -av --delete source/ dest/?",
            options: [
                "Kopierar endast nya filer",
                "Arkiverar med verbose, och tar bort filer i dest som inte finns i source",
                "Tar bort source efter kopiering",
                "Krypterar överföringen"
            ],
            correctIndex: 1,
            explanation: "-a=archive, -v=verbose, --delete=fullständig spegling (tar bort orphaned filer i dest).",
            difficulty: "VG",
            kursmål: "KM6"
        }
    ],

    // ═══════════════════════════════════════════════════════════════════════════
    // KURSMÅL 7: DOCKER
    // ═══════════════════════════════════════════════════════════════════════════
    "KM7 - Docker": [
        {
            question: "Skillnad mellan container och VM?",
            options: [
                "Ingen skillnad",
                "Container: delar kernel, snabb, MB. VM: full OS, långsam, GB",
                "VM är alltid säkrare",
                "Container kräver mer resurser"
            ],
            correctIndex: 1,
            explanation: "Containers delar värdkerneln = lätt och snabb. VMs har egen kernel = tungt men full isolering.",
            difficulty: "G",
            kursmål: "KM7"
        },
        {
            question: "Skillnad mellan Docker image och container?",
            options: [
                "Samma sak",
                "Image: read-only mall. Container: körande instans av image",
                "Container är alltid större",
                "Image körs, container lagras"
            ],
            correctIndex: 1,
            explanation: "Image = mall/ritning (statisk). Container = körande instans med eget skrivbart lager.",
            difficulty: "G",
            kursmål: "KM7"
        },
        {
            question: "Vad gör docker run -d -p 8080:80 nginx?",
            options: [
                "Laddar ner nginx",
                "Kör nginx i bakgrunden (-d) och mappar host:8080 till container:80",
                "Tar bort nginx",
                "Visar nginx-loggar"
            ],
            correctIndex: 1,
            explanation: "-d=detached (bakgrund), -p=port mapping (host:container). Mappar port 8080 till nginx port 80.",
            difficulty: "G",
            kursmål: "KM7"
        },
        {
            question: "Hur sparar du data permanent i Docker?",
            options: [
                "Data sparas automatiskt",
                "Volymer (-v volymnamn:/sökväg) eller bind mounts",
                "Skriv till /tmp",
                "Använd docker save"
            ],
            correctIndex: 1,
            explanation: "Containers är ephemeral - data försvinner. Volymer bevarar data mellan container-körningar.",
            difficulty: "G",
            kursmål: "KM7"
        },
        {
            question: "Vilka Linux-teknologier möjliggör containers?",
            options: [
                "Bara cgroups",
                "Namespaces (isolering) + Cgroups (resursbegränsning)",
                "Kernel modules endast",
                "Virtualisering"
            ],
            correctIndex: 1,
            explanation: "Namespaces isolerar (process, nätverk, filsystem). Cgroups begränsar resurser (CPU, RAM).",
            difficulty: "VG",
            kursmål: "KM7"
        },
        {
            question: "Hur öppnar du ett shell i en körande container?",
            options: [
                "docker bash containernamn",
                "docker exec -it containernamn bash",
                "docker shell containernamn",
                "docker connect containernamn"
            ],
            correctIndex: 1,
            explanation: "docker exec -it: -i=interactive, -t=terminal. Kör bash (eller sh) inuti containern.",
            difficulty: "G",
            kursmål: "KM7"
        },
        {
            question: "Hur listar du alla containers (även stoppade)?",
            options: [
                "docker ps",
                "docker ps -a",
                "docker list --all",
                "docker containers"
            ],
            correctIndex: 1,
            explanation: "docker ps visar körande. docker ps -a visar alla inklusive stoppade containers.",
            difficulty: "G",
            kursmål: "KM7"
        }
    ],

    // ═══════════════════════════════════════════════════════════════════════════
    // KURSMÅL 8: GIT
    // ═══════════════════════════════════════════════════════════════════════════
    "KM8 - Git": [
        {
            question: "Vad är staging area?",
            options: [
                "Där commits sparas",
                "Mellansteg där du väljer vad som inkluderas i nästa commit",
                "Remote repository",
                "Backup av working directory"
            ],
            correctIndex: 1,
            explanation: "Staging area (index) är ett förberedelseområde mellan working directory och repository.",
            difficulty: "G",
            kursmål: "KM8"
        },
        {
            question: "Skillnad mellan git fetch och git pull?",
            options: [
                "Samma sak",
                "fetch: hämtar utan merge. pull: fetch + merge",
                "pull är snabbare",
                "fetch tar bort lokala ändringar"
            ],
            correctIndex: 1,
            explanation: "fetch hämtar data men ändrar inte din kod. pull = fetch + automatisk merge.",
            difficulty: "G",
            kursmål: "KM8"
        },
        {
            question: "Hur skapar du en branch och byter till den i ett kommando?",
            options: [
                "git branch branchnamn && git checkout branchnamn",
                "git checkout -b branchnamn",
                "git create branchnamn",
                "git new-branch branchnamn"
            ],
            correctIndex: 1,
            explanation: "git checkout -b kombinerar branch creation och checkout. Nyare alternativ: git switch -c",
            difficulty: "G",
            kursmål: "KM8"
        },
        {
            question: "Hur ångrar du en pushad commit säkert?",
            options: [
                "git reset --hard",
                "git revert <commit-hash>",
                "git delete commit",
                "git undo push"
            ],
            correctIndex: 1,
            explanation: "git revert skapar en ny commit som ångrar ändringar. Säkert för delad historik.",
            difficulty: "G",
            kursmål: "KM8"
        },
        {
            question: "Vad gör git add .?",
            options: [
                "Committar alla filer",
                "Lägger alla ändrade filer i staging area",
                "Pushar till remote",
                "Skapar ny branch"
            ],
            correctIndex: 1,
            explanation: "git add . stagar alla ändringar i working directory för nästa commit.",
            difficulty: "G",
            kursmål: "KM8"
        },
        {
            question: "Hur mergar du en feature-branch till main?",
            options: [
                "git merge main (från feature-branch)",
                "git checkout main följt av git merge feature-branch",
                "git push feature-branch main",
                "git combine feature main"
            ],
            correctIndex: 1,
            explanation: "Först checkout till target-branch (main), sedan merge source-branch (feature).",
            difficulty: "G",
            kursmål: "KM8"
        },
        {
            question: "Vad är .gitignore?",
            options: [
                "En lista på ignorerade commits",
                "Fil som anger vilka filer Git ska ignorera",
                "Konfiguration för remote",
                "Loggfil för git-errors"
            ],
            correctIndex: 1,
            explanation: ".gitignore innehåller patterns för filer/mappar som Git inte ska spåra (t.ex. node_modules, .env).",
            difficulty: "G",
            kursmål: "KM8"
        }
    ]
};

// Statistik
export const DOE25_QUIZ_STATS = {
    totalQuestions: Object.values(DOE25_QUIZ).flat().length,
    categories: Object.keys(DOE25_QUIZ).length,
    examDate: new Date("2026-01-07T09:30:00+01:00"),
    source: "DOE25 Linux kurs - simulerade tentafrågor baserade på kursmaterial"
};
