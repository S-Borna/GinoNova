// DOE25 Tenta Module - Linux/Unix Server
// Innehåll baserat på kursföreläsningar och hands-on övningar
// Tentadatum: 7 januari 2025

export interface ContentBlock {
  type: 'intro' | 'concept' | 'code' | 'checkpoint';
  title?: string;
  headline?: string;
  explanation?: string;
  learning_objectives?: string[];
  code?: string;
  language?: string;
  pro_tip?: string;
  message?: string;
}

export interface DOE25Task {
  id: string;
  title: string;
  description: string;
  order_index: number;
  estimated_minutes: number;
  content_blocks: ContentBlock[];
}

export interface DOE25Module {
  id: string;
  name: string;
  slug: string;
  description: string;
  difficulty: 'beginner' | 'intermediate' | 'advanced';
  estimated_hours: number;
  exam_date: string;
  tasks: DOE25Task[];
}

export const DOE25_MODULE: DOE25Module = {
  id: "doe25-tenta",
  name: "DOE25 Tenta",
  slug: "doe25-tenta",
  description: "Komplett tentaplugg för Linux/Unix Server - Kursmål 1-8",
  difficulty: "intermediate",
  estimated_hours: 30,
  exam_date: "2025-01-07T09:30:00",
  tasks: [
    // ============================================
    // KM1: FELSÖKNING OCH ÅTGÄRDER
    // ============================================
    {
      id: "doe25-km1-felsokning",
      title: "KM1: Felsökning och åtgärder",
      description: "Redogöra för grundläggande metoder för felsökning och åtgärder i Linux/Unix-system",
      order_index: 1,
      estimated_minutes: 45,
      content_blocks: [
        {
          type: "intro",
          headline: "Felsökning – Systematisk metodik",
          learning_objectives: [
            "Felsökningsprocessen i 7 steg",
            "Loggfiler och journalctl",
            "Processhantering (ps, kill, top)",
            "Systemresurser (df, free, lsblk)",
            "Tjänstehantering (systemctl)"
          ]
        },
        {
          type: "concept",
          title: "Systematisk felsökningsmetodik",
          explanation: `**Steg-för-steg-processen:**

1. **IDENTIFIERA** → Vad är symtomet? Vad fungerar inte?
2. **REPRODUCERA** → Kan du få felet att hända igen?
3. **ISOLERA** → Var uppstår felet? (nätverk? disk? process? behörighet?)
4. **DIAGNOSTISERA** → Vilka loggar/verktyg visar vad som händer?
5. **ÅTGÄRDA** → Fixa grundorsaken, inte symtomet
6. **VERIFIERA** → Bekräfta att problemet är löst
7. **DOKUMENTERA** → Skriv ner vad du gjorde (för framtiden)`,
          pro_tip: "Tänk som en läkare. Du behandlar inte bara feber (symtom), du tar reda på varför patienten har feber (grundorsak)."
        },
        {
          type: "concept",
          title: "Loggfiler – systemets svarta låda",
          explanation: `**Var loggar finns:**

\`\`\`
/var/log/           ← Huvudkatalog för loggar
├── syslog          ← Allmän systemlogg (Debian/Ubuntu)
├── messages        ← Allmän systemlogg (RHEL/Fedora)
├── auth.log        ← Inloggningsförsök, sudo-användning
├── kern.log        ← Kernel-meddelanden
├── dmesg           ← Boot-meddelanden, hårdvara
├── apt/            ← Pakethantering (Debian)
└── dnf.log         ← Pakethantering (Fedora)
\`\`\`

**Varför journalctl?** Systemd samlar alla loggar på ett ställe med metadata (tid, tjänst, prioritet). Enklare att filtrera än att grep:a i textfiler.`
        },
        {
          type: "code",
          title: "Loggkommandon",
          language: "bash",
          code: `# Journalctl - moderna sättet
journalctl                      # Alla loggar
journalctl -u ssh               # Specifik tjänst
journalctl -p err               # Endast fel
journalctl --since "1 hour ago" # Senaste timmen
journalctl -f                   # Följ i realtid (som tail -f)

# Traditionella loggfiler
tail -f /var/log/syslog         # Följ i realtid`
        },
        {
          type: "concept",
          title: "Processhantering",
          explanation: `**Visa processer:**
- \`ps aux\` - Alla processer, detaljerad info
- \`ps -ef\` - Alternativ format
- \`top\` - Realtidsvy (interaktiv)
- \`htop\` - Bättre realtidsvy (om installerad)
- \`pgrep -a nginx\` - Hitta process via namn

**Tolka ps-output:**
\`\`\`
USER   PID  %CPU %MEM    VSZ   RSS TTY  STAT START   TIME COMMAND
root     1   0.0  0.1 169584 13256 ?    Ss   Dec24   0:02 /sbin/init
\`\`\`

- **PID**: Process-ID (unikt nummer)
- **%CPU/%MEM**: Resursanvändning
- **STAT**: S=sleeping, R=running, Z=zombie, D=uninterruptible
- **TTY**: Terminal (? = ingen terminal = daemon/bakgrund)`,
          pro_tip: "SIGTERM före SIGKILL! SIGTERM låter processen städa upp (stänga filer, spara data). SIGKILL dödar direkt utan cleanup – risk för korruption."
        },
        {
          type: "code",
          title: "Process- och resurskommandon",
          language: "bash",
          code: `# Processer
ps aux                         # Lista processer
top / htop                     # Realtid
kill PID                       # SIGTERM (snäll avslutning)
kill -9 PID                    # SIGKILL (tvångsavslutning)
killall processnamn            # Avsluta alla med det namnet

# Resurser
df -h                          # Diskutrymme per partition
du -sh /var/log                # Storlek på specifik katalog
free -h                        # RAM-användning
lsblk                          # Blockenheter (diskar, partitioner)

# Nätverk
ss -tuln                       # Öppna portar
ip a                           # IP-adresser
ip r                           # Routing-tabell

# Tjänster (systemd)
systemctl status nginx          # Status för tjänst
systemctl start nginx           # Starta
systemctl stop nginx            # Stoppa
systemctl restart nginx         # Omstart
systemctl enable nginx          # Starta automatiskt vid boot
systemctl disable nginx         # Starta INTE vid boot
systemctl list-units --failed   # Visa misslyckade tjänster`
        },
        {
          type: "concept",
          title: "Minnestolkning",
          explanation: `**free -h output:**
\`\`\`
              total        used        free      shared  buff/cache   available
Mem:          7.7Gi       2.1Gi       3.2Gi       234Mi       2.4Gi       5.1Gi
\`\`\`

**Viktigt:** \`available\` är vad du faktiskt kan använda, inte \`free\`. Linux använder ledigt RAM till cache (det är bra, inte ett problem).`
        },
        {
          type: "checkpoint",
          message: "Du har slutfört KM1: Felsökning och åtgärder!"
        }
      ]
    },

    // ============================================
    // KM2: LAGRINGSPRINCIPER
    // ============================================
    {
      id: "doe25-km2-lagring",
      title: "KM2: Lagringsprinciper",
      description: "Redogöra för lagringsprinciper för Linux/Unix-filsystem",
      order_index: 2,
      estimated_minutes: 40,
      content_blocks: [
        {
          type: "intro",
          headline: "Lagring – Filsystem, LVM och RAID",
          learning_objectives: [
            "FHS - Filesystem Hierarchy Standard",
            "Filsystemtyper (ext4, XFS)",
            "LVM - Logical Volume Manager",
            "RAID-nivåer (0, 1, 5)",
            "Hårda vs symboliska länkar"
          ]
        },
        {
          type: "concept",
          title: "FHS - Filesystem Hierarchy Standard",
          explanation: `**Viktiga kataloger:**

| Katalog | Innehåll |
|---------|----------|
| \`/etc\` | Konfigurationsfiler (textbaserade, redigerbara) |
| \`/var/log\` | Loggfiler |
| \`/home\` | Användarnas hemkataloger |
| \`/tmp\` | Temporära filer (rensas vid omstart) |
| \`/opt\` | Tredjepartsprogram |
| \`/mnt\` | Tillfälliga monteringspunkter |
| \`/bin\` | Grundläggande kommandon |
| \`/sbin\` | Systemadministrationskommandon |
| \`/usr\` | Användarprogram och data |`
        },
        {
          type: "concept",
          title: "Filsystemtyper",
          explanation: `**ext4 vs XFS:**

| Egenskap | ext4 | XFS |
|----------|------|-----|
| Standard | Debian/Ubuntu | RHEL/Fedora |
| Storlek | Bra för mindre | Stora filer, enterprise |
| Krympning | Ja | Nej |
| Journaling | Ja | Ja |

**Journaling:** Loggar ändringar innan de görs → möjliggör återställning vid krasch.`
        },
        {
          type: "concept",
          title: "LVM - Logical Volume Manager",
          explanation: `**Vad LVM gör:**
Abstraktion mellan fysisk disk och filsystem → dynamisk storleksändring utan omstart.

**Hierarki:**
\`\`\`
Physical Volumes (PV)  →  /dev/sda1, /dev/sdb1
        ↓
Volume Groups (VG)     →  vg_data
        ↓
Logical Volumes (LV)   →  lv_home, lv_var
\`\`\`

**Fördelar:**
- Utöka/krympa volymer utan omstart
- Samla flera diskar till en pool
- Snapshots för backup`
        },
        {
          type: "code",
          title: "LVM-kommandon",
          language: "bash",
          code: `# Visa LVM-info
pvs                           # Physical Volumes
vgs                           # Volume Groups
lvs                           # Logical Volumes

# Utöka en Logical Volume
lvextend -L +10G /dev/vg/lv   # Lägg till 10GB
resize2fs /dev/vg/lv          # Utöka filsystemet (ext4)
xfs_growfs /dev/vg/lv         # Utöka filsystemet (XFS)`
        },
        {
          type: "concept",
          title: "RAID-nivåer",
          explanation: `**RAID 0 - Striping:**
- Data sprids över diskar
- Ingen redundans
- Snabbt, men en disk dör = allt borta

**RAID 1 - Mirroring:**
- Identisk kopia på två diskar
- En disk kan dö
- Halva kapaciteten

**RAID 5 - Striping + Paritet:**
- Data + paritet sprids
- En disk kan dö
- Bra balans prestanda/redundans`,
          pro_tip: "RAID är INTE backup! RAID skyddar mot diskfel, inte mot radering eller korruption."
        },
        {
          type: "concept",
          title: "Länkar - Hårda vs Symboliska",
          explanation: `**Hård länk:**
- Pekar direkt på inode (data)
- Överlever om original tas bort
- Fungerar endast inom samma filsystem
- \`ln fil hardlink\`

**Symbolisk länk (symlink):**
- Pekar på filnamn (sökväg)
- Bryts om original tas bort
- Kan korsa filsystem
- \`ln -s fil symlink\``,
          pro_tip: "Tänk hård länk som alias till samma data. Symlink som en genväg."
        },
        {
          type: "code",
          title: "Disk- och länkkommandon",
          language: "bash",
          code: `# Diskinfo
df -h                          # Diskutrymme per partition
du -sh katalog                 # Katalogstorlek
lsblk                          # Blockenheter
lsblk -f                       # Med filsysteminfo

# Montering
mount /dev/sdb1 /mnt/disk      # Montera
umount /mnt/disk               # Avmontera
cat /etc/fstab                 # Permanenta monteringar

# Länkar
ln fil hardlink                # Hård länk
ln -s fil symlink              # Symbolisk länk
ls -li                         # Visa inode-nummer`
        },
        {
          type: "checkpoint",
          message: "Du har slutfört KM2: Lagringsprinciper!"
        }
      ]
    },

    // ============================================
    // KM3: RÄTTIGHETER & ANVÄNDARE
    // ============================================
    {
      id: "doe25-km3-rattigheter",
      title: "KM3: Rättigheter & användare",
      description: "Redogöra för principer för rättigheter i Linux/Unix-system",
      order_index: 3,
      estimated_minutes: 50,
      content_blocks: [
        {
          type: "intro",
          headline: "Rättigheter – rwx, chmod och speciella bitar",
          learning_objectives: [
            "Filbehörigheter (rwx)",
            "Numerisk och symbolisk chmod",
            "SUID, SGID, Sticky bit",
            "Användar- och grupphantering",
            "sudo och /etc/sudoers"
          ]
        },
        {
          type: "concept",
          title: "Från Hands-on 1 december",
          explanation: `**Det här gjorde ni i kursen:**

Skapa användare:
\`\`\`bash
# Skapa 5 användare
sudo useradd -m Alice
sudo useradd -m Bob
sudo useradd -m Charlie
sudo useradd -m David
sudo useradd -m Evert
\`\`\`

**-m flaggan** = Skapar hemkatalog automatiskt under \`/home/användarnamn\`

Skapa grupp och lägg till medlemmar:
\`\`\`bash
# Skapa gruppen developers
sudo groupadd developers

# Lägg till Alice, Charlie och Evert i gruppen
sudo usermod -aG developers Alice
sudo usermod -aG developers Charlie
sudo usermod -aG developers Evert
\`\`\`

**-aG flaggan:**
- \`-a\` = append (lägg till, ersätt inte befintliga grupper)
- \`-G\` = secondary group`
        },
        {
          type: "concept",
          title: "Filbehörigheter - rwx",
          explanation: `**Tolka behörigheter:**
\`\`\`
-rwxr-xr-- 1 said developers 4096 Dec 1 10:00 script.sh
│├─┤├─┤├─┤
│ │  │  └── Others: r-- (läs)
│ │  └───── Group: r-x (läs, kör)
│ └──────── Owner: rwx (läs, skriv, kör)
└────────── Filtyp: - = fil, d = katalog
\`\`\`

**Numeriska värden:**
- r (read) = 4
- w (write) = 2
- x (execute) = 1

**Vanliga kombinationer:**
- \`755\` = rwxr-xr-x (script som alla kan köra)
- \`644\` = rw-r--r-- (vanlig fil)
- \`700\` = rwx------ (privat)
- \`600\` = rw------- (endast ägaren kan läsa/skriva)`
        },
        {
          type: "concept",
          title: "Delad katalog med SGID",
          explanation: `**Från kursen:**
\`\`\`bash
# Skapa katalog för teamet
sudo mkdir -p /opt/developers

# Sätt ägare och grupp
sudo chown root:developers /opt/developers

# SGID + rwx för grupp, ingen access för others
sudo chmod 2770 /opt/developers
\`\`\`

**Vad betyder 2770?**
- \`2\` = SGID-bit (Set Group ID)
- \`7\` = rwx för ägare (root)
- \`7\` = rwx för gruppen (developers)
- \`0\` = ingen access för others

**SGID-effekten:** Alla filer som skapas i \`/opt/developers\` får automatiskt gruppen \`developers\`, oavsett vem som skapar dem.`
        },
        {
          type: "concept",
          title: "Speciella bitar",
          explanation: `| Bit | Numeriskt | Effekt på fil | Effekt på katalog |
|-----|-----------|---------------|-------------------|
| SUID | 4xxx | Körs som filägaren | - |
| SGID | 2xxx | Körs som filgruppen | Nya filer ärver grupp |
| Sticky | 1xxx | - | Bara ägaren kan radera |

**Exempel:**
\`\`\`bash
chmod 4755 /usr/bin/passwd   # SUID - kör som root
chmod 2770 /opt/shared       # SGID - nya filer får gruppägare
chmod 1777 /tmp              # Sticky - bara ägare kan radera
\`\`\``
        },
        {
          type: "concept",
          title: "Lösenord och utgångsdatum",
          explanation: `**Från kursen:**
\`\`\`bash
# Sätt utgångsdatum för Bob och David (31 dec 2025)
sudo chage -E 2025-12-31 Bob
sudo chage -E 2025-12-31 David

# Tvinga Evert att byta lösenord vid nästa inloggning
sudo passwd --expire Evert
\`\`\`

**chage-kommandon att kunna:**
\`\`\`bash
chage -l användare     # Lista lösenordsinställningar
chage -E YYYY-MM-DD    # Sätt utgångsdatum
chage -M 90            # Lösenord måste bytas var 90:e dag
chage -m 7             # Minst 7 dagar mellan byten
chage -d 0 användare   # Tvinga lösenordsbyte vid nästa inloggning
\`\`\``
        },
        {
          type: "concept",
          title: "Viktiga filer för användare",
          explanation: `| Fil | Innehåll |
|-----|----------|
| \`/etc/passwd\` | Användarinfo (UID, GID, hemkatalog, shell) |
| \`/etc/shadow\` | Krypterade lösenord och lösenordspolicy |
| \`/etc/group\` | Gruppinfo och medlemmar |
| \`/etc/gshadow\` | Grupplösenord (sällan använt) |
| \`/etc/sudoers\` | Sudo-konfiguration (redigera med visudo) |

**Exempel från /etc/passwd:**
\`\`\`
Alice:x:1001:1001::/home/Alice:/bin/bash
\`\`\`
Format: \`användarnamn:x:UID:GID:kommentar:hemkatalog:shell\``
        },
        {
          type: "code",
          title: "Användar- och rättighetskommandon",
          language: "bash",
          code: `# Rättigheter
chmod 755 fil                  # rwxr-xr-x
chmod u+x fil                  # Ägare +execute
chmod g+s katalog              # SGID (ärv grupp)
chmod +t katalog               # Sticky bit

# Ägare
chown user:group fil
chown -R user:group katalog    # Rekursivt

# Användare
useradd -m -s /bin/bash -G grupp user
passwd user
usermod -aG grupp user         # Lägg till i grupp
userdel -r user                # Ta bort med hemkatalog

# Grupper
groupadd gruppnamn
groups användarnamn            # Visa användarens grupper
getent group gruppnamn         # Visa gruppmedlemmar

# Sudo
visudo                         # Redigera /etc/sudoers säkert
# user ALL=(ALL) NOPASSWD: ALL`
        },
        {
          type: "checkpoint",
          message: "Du har slutfört KM3: Rättigheter & användare!"
        }
      ]
    },

    // ============================================
    // KM4: KONFIGURATION & ADMINISTRATION
    // ============================================
    {
      id: "doe25-km4-administration",
      title: "KM4: Konfiguration & administration",
      description: "Redogöra för principer för konfiguration av Linux/Unix-system",
      order_index: 4,
      estimated_minutes: 45,
      content_blocks: [
        {
          type: "intro",
          headline: "Administration – Paket, systemd och SSH",
          learning_objectives: [
            "Pakethantering (apt, dnf)",
            "Systemd och tjänster",
            "Cron för schemalagda jobb",
            "SSH-konfiguration och härdning"
          ]
        },
        {
          type: "concept",
          title: "Pakethantering",
          explanation: `**Debian/Ubuntu (apt):**
\`\`\`bash
apt update              # Uppdatera paketlista (inte paketen)
apt upgrade             # Uppgradera installerade paket
apt install paket       # Installera
apt remove paket        # Ta bort (behåll config)
apt purge paket         # Ta bort inkl. config
apt search sökord       # Sök paket
\`\`\`

**Fedora/RHEL (dnf):**
\`\`\`bash
dnf check-update        # Kolla tillgängliga uppdateringar
dnf upgrade             # Uppgradera
dnf install paket
dnf remove paket
dnf search sökord
\`\`\``,
          pro_tip: "apt update uppdaterar LISTAN över paket. apt upgrade uppdaterar PAKETEN."
        },
        {
          type: "concept",
          title: "Systemd och tjänster",
          explanation: `**Grundläggande tjänsthantering:**
\`\`\`bash
systemctl status tjänst      # Visa status
systemctl start tjänst       # Starta
systemctl stop tjänst        # Stoppa
systemctl restart tjänst     # Omstart
systemctl reload tjänst      # Ladda om config utan omstart
systemctl enable tjänst      # Autostart vid boot
systemctl disable tjänst     # Ingen autostart
systemctl daemon-reload      # Efter servicefil-ändring
\`\`\`

**Targets (motsvarar runlevels):**
- \`multi-user.target\` = Fleranvändarläge utan GUI (runlevel 3)
- \`graphical.target\` = Med GUI (runlevel 5)
- \`rescue.target\` = Räddningsläge (runlevel 1)`
        },
        {
          type: "concept",
          title: "Cron - Schemalagda jobb",
          explanation: `**Cron-format:**
\`\`\`
┌───────────── minut (0-59)
│ ┌───────────── timme (0-23)
│ │ ┌───────────── dag i månaden (1-31)
│ │ │ ┌───────────── månad (1-12)
│ │ │ │ ┌───────────── veckodag (0-7, 0 och 7 = söndag)
│ │ │ │ │
* * * * * kommando
\`\`\`

**Exempel:**
- \`*/5 * * * *\` = var 5:e minut
- \`0 2 * * *\` = kl 02:00 dagligen
- \`0 3 * * 1\` = kl 03:00 måndagar
- \`0 0 1 * *\` = midnatt första dagen varje månad`
        },
        {
          type: "code",
          title: "Cron-kommandon",
          language: "bash",
          code: `# Redigera användarens crontab
crontab -e

# Lista cron-jobb
crontab -l

# System-wide cron
cat /etc/crontab
ls /etc/cron.d/
ls /etc/cron.daily/
ls /etc/cron.hourly/`
        },
        {
          type: "concept",
          title: "SSH-härdning (från föreläsningen 19 nov)",
          explanation: `**Varför SSH-härdning?**
SSH är porten till din server. Default-inställningar är osäkra:
- Port 22 är känt mål för attacker
- Lösenordsinloggning kan bruteforcas
- Root-access direkt är farligt

**Steg 1: Generera SSH-nyckel (på din maskin)**
\`\`\`bash
ssh-keygen -t ed25519 -C "said@devops"
# Privat nyckel: ~/.ssh/id_ed25519
# Publik nyckel: ~/.ssh/id_ed25519.pub
\`\`\`

**ed25519 vs RSA:**
- ed25519 = modernare, kortare nycklar, snabbare
- RSA = äldre, kompatibelt med allt`
        },
        {
          type: "concept",
          title: "SSH-härdning config",
          explanation: `**Kopiera publik nyckel till server:**
\`\`\`bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub said@192.168.1.100
\`\`\`

**Viktigt om behörigheter:**
- \`~/.ssh\` måste vara \`700\`
- \`~/.ssh/authorized_keys\` måste vara \`600\`
- Annars vägrar SSH använda nycklarna!

**Härdning i /etc/ssh/sshd_config.d/01-hardening.conf:**
\`\`\`bash
Port 6622                      # Byt från standardport 22
PasswordAuthentication no      # Tillåt INTE lösenord
PermitRootLogin no             # Tillåt INTE root-inloggning
AllowUsers said                # Tillåt ENDAST specifika användare
\`\`\``,
          pro_tip: "Testa alltid i en NY terminal innan du stänger den gamla - annars kan du låsa ut dig!"
        },
        {
          type: "code",
          title: "SSH och brandvägg",
          language: "bash",
          code: `# Starta om SSH efter ändring
sudo systemctl restart sshd

# Ubuntu (UFW)
sudo ufw allow 6622/tcp
sudo ufw enable
sudo ufw status

# Fedora (FirewallD)
sudo firewall-cmd --permanent --add-port=6622/tcp
sudo firewall-cmd --reload
sudo firewall-cmd --list-all

# SSH-config på klienten (~/.ssh/config)
Host ubuntu-vm
    HostName 192.168.1.100
    User said
    Port 6622
    IdentityFile ~/.ssh/id_ed25519

# Nu: ssh ubuntu-vm`
        },
        {
          type: "checkpoint",
          message: "Du har slutfört KM4: Konfiguration & administration!"
        }
      ]
    },

    // ============================================
    // KM5: NÄTVERK, OSI & SUBNETTING
    // ============================================
    {
      id: "doe25-km5-natverk",
      title: "KM5: Nätverk, OSI & subnetting",
      description: "Redogöra för grundläggande nätverksteknik, bland annat OSI-modellen och subnetting",
      order_index: 5,
      estimated_minutes: 60,
      content_blocks: [
        {
          type: "intro",
          headline: "Nätverk – OSI, TCP/IP och subnetting",
          learning_objectives: [
            "OSI-modellens 7 lager",
            "TCP vs UDP",
            "IP-adressering och privata intervall",
            "Subnetting och CIDR",
            "Viktiga portar"
          ]
        },
        {
          type: "concept",
          title: "OSI-modellen – de 7 lagren",
          explanation: `**Minnesregel (uppifrån):** "Alla Personer Som Talar Norska Dricker Fanta"

| Lager | Namn | Funktion | Protokoll |
|-------|------|----------|-----------|
| 7 | Application | Användargränssnitt | HTTP, SSH, DNS |
| 6 | Presentation | Format, kryptering | SSL/TLS, JPEG |
| 5 | Session | Sessionshantering | NetBIOS |
| 4 | Transport | End-to-end leverans | TCP, UDP |
| 3 | Network | Routing, adressering | IP, ICMP |
| 2 | Data Link | Lokal leverans | Ethernet, MAC |
| 1 | Physical | Elektriska signaler | Kablar, Wi-Fi |

**Analogi – skicka ett paket:**
1. Application: Du skriver ett brev
2. Presentation: Du översätter till gemensamt språk
3. Session: Du etablerar kontakt
4. Transport: Du delar upp brevet i numrerade sidor
5. Network: Du skriver mottagarens adress
6. Data Link: Posten hittar rätt hus på gatan
7. Physical: Lastbilen kör brevet fysiskt`
        },
        {
          type: "concept",
          title: "TCP vs UDP",
          explanation: `| Egenskap | TCP | UDP |
|----------|-----|-----|
| Anslutning | Connection-oriented | Connectionless |
| Tillförlitlighet | Garanterad leverans | Best effort |
| Ordning | Garanterad ordning | Ingen garanti |
| Hastighet | Långsammare | Snabbare |
| Användning | HTTP, SSH, e-post | DNS, video, gaming |

**Analogi:**
- TCP = Rekommenderat brev med kvittens. Du vet att det kom fram.
- UDP = Vykort. Snabbt, men ingen garanti.

**TCP 3-way handshake:**
\`\`\`
Klient  →  SYN        →  Server    "Vill ansluta"
Klient  ←  SYN-ACK    ←  Server    "OK, jag lyssnar"
Klient  →  ACK        →  Server    "Fint, vi kör"
\`\`\``
        },
        {
          type: "concept",
          title: "IP-adressering",
          explanation: `**IPv4-format:** 4 oktetter à 8 bitar = 32 bitar totalt
\`192.168.1.10\`

**Privata adressintervall (RFC 1918):**
- \`10.0.0.0/8\` (10.0.0.0 – 10.255.255.255)
- \`172.16.0.0/12\` (172.16.0.0 – 172.31.255.255)
- \`192.168.0.0/16\` (192.168.0.0 – 192.168.255.255)

**Speciella adresser:**
- \`127.0.0.1\` = localhost (loopback)
- \`0.0.0.0\` = "alla interface" eller "okänd"
- \`255.255.255.255\` = broadcast`
        },
        {
          type: "concept",
          title: "Subnetting – dela upp nätverk",
          explanation: `**Varför subnetting?**
- Effektiv användning av IP-adresser
- Isolera nätverkssegment (säkerhet)
- Minska broadcast-domäner

**CIDR-notation och hosts:**
| Prefix | Mask | Adresser | Hosts |
|--------|------|----------|-------|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |

**Formel:** Hosts = 2^(32-prefix) - 2
(-2 för nätverks- och broadcast-adress)`,
          pro_tip: "Binär subnetting: 256 - sista oktetten i masken = 'magiskt nummer'. För /26: 256-192=64, subnät börjar vid 0, 64, 128, 192..."
        },
        {
          type: "concept",
          title: "Subnetting-exempel",
          explanation: `**Givet: 192.168.1.0/24, dela i 4 subnät**

Steg 1: Vi behöver 2 extra bitar (2² = 4)
Steg 2: /24 + 2 = /26

**Resultat:**
\`\`\`
Subnät 1: 192.168.1.0/26    (0-63,   host: 1-62)
Subnät 2: 192.168.1.64/26   (64-127, host: 65-126)
Subnät 3: 192.168.1.128/26  (128-191, host: 129-190)
Subnät 4: 192.168.1.192/26  (192-255, host: 193-254)
\`\`\``
        },
        {
          type: "concept",
          title: "Viktiga portar",
          explanation: `| Port | Protokoll | Tjänst |
|------|-----------|--------|
| 22 | TCP | SSH |
| 25 | TCP | SMTP (e-post) |
| 53 | TCP/UDP | DNS |
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |`
        },
        {
          type: "code",
          title: "Nätverkskommandon",
          language: "bash",
          code: `# Visa konfiguration
ip a                    # IP-adresser
ip r                    # Routing-tabell
ip link                 # Interface-status

# Testa anslutning
ping 8.8.8.8            # ICMP echo
ping google.com         # Testa DNS-upplösning
traceroute google.com   # Spåra vägen

# DNS
nslookup google.com     # DNS-uppslagning
dig google.com          # Detaljerad DNS

# Portar och anslutningar
ss -tuln                # Lyssnande portar
ss -tun                 # Aktiva anslutningar`
        },
        {
          type: "checkpoint",
          message: "Du har slutfört KM5: Nätverk, OSI & subnetting!"
        }
      ]
    },

    // ============================================
    // KM6: ARKIVERING & BACKUP
    // ============================================
    {
      id: "doe25-km6-backup",
      title: "KM6: Arkivering & backup",
      description: "Beskriva metoder för arkivering och backup på Linux/Unix-servrar",
      order_index: 6,
      estimated_minutes: 30,
      content_blocks: [
        {
          type: "intro",
          headline: "Backup – 3-2-1-regeln och verktyg",
          learning_objectives: [
            "3-2-1-regeln för backup",
            "Backup-typer (full, inkrementell, differentiell)",
            "tar för arkivering",
            "rsync för synkronisering"
          ]
        },
        {
          type: "concept",
          title: "3-2-1-regeln",
          explanation: `**3** kopior av data
**2** olika lagringsmedier
**1** off-site (annan fysisk plats)

**Exempel:**
- Originaldata på servern
- Backup på NAS lokalt
- Kopia i molnet (S3, Backblaze)`,
          pro_tip: "En backup du aldrig testat är ingen backup. Testa återställning regelbundet!"
        },
        {
          type: "concept",
          title: "Backup-typer",
          explanation: `| Typ | Beskrivning | Tid | Plats | Återställning |
|-----|-------------|-----|-------|---------------|
| Full | Allt varje gång | Lång | Stor | Snabb |
| Inkrementell | Ändringar sedan senaste | Kort | Liten | Långsam |
| Differentiell | Ändringar sedan fulla | Medel | Medel | Medel |

**Strategi-exempel:**
- Söndag: Full backup
- Måndag-Lördag: Inkrementell
- Återställning: Full + alla inkrementella`,
          pro_tip: "Inkrementell sparar mest plats men kräver alla backups för återställning."
        },
        {
          type: "code",
          title: "tar – arkivering",
          language: "bash",
          code: `# Skapa arkiv
tar -cvf backup.tar /etc             # Create, Verbose, File
tar -czvf backup.tar.gz /etc         # Med gzip-komprimering
tar -cjvf backup.tar.bz2 /etc        # Med bzip2

# Minnesregel för tar-flaggor:
# c = Create
# x = Extract
# t = lisT
# v = Verbose
# f = File
# z = gZip

# Lista innehåll
tar -tvf backup.tar.gz

# Extrahera
tar -xzvf backup.tar.gz              # Packa upp
tar -xzvf backup.tar.gz -C /restore/ # Till specifik katalog`
        },
        {
          type: "code",
          title: "rsync – synkronisering",
          language: "bash",
          code: `# Lokal synk
rsync -av /source/ /backup/
# -a = archive (behåller rättigheter, timestamps etc)
# -v = verbose

# Fjärr (över SSH)
rsync -avz /local/ user@server:/backup/
# -z = komprimering

# --delete tar bort filer på destination som inte finns i source
rsync -av --delete /source/ /backup/`
        },
        {
          type: "checkpoint",
          message: "Du har slutfört KM6: Arkivering & backup!"
        }
      ]
    },

    // ============================================
    // KM7: CONTAINERTEKNIK (DOCKER)
    // ============================================
    {
      id: "doe25-km7-docker",
      title: "KM7: Containerteknik (Docker)",
      description: "Förklara grunderna i containerteknik i Linux och dess användningsområden",
      order_index: 7,
      estimated_minutes: 45,
      content_blocks: [
        {
          type: "intro",
          headline: "Docker – kör vad som helst, var som helst",
          learning_objectives: [
            "Skillnad container vs VM",
            "Image vs container",
            "Grundläggande docker-kommandon",
            "Dockerfile och volymer"
          ]
        },
        {
          type: "concept",
          title: "Container vs VM",
          explanation: `| Egenskap | VM | Container |
|----------|-----|----------|
| Isolering | Full OS | Delar kernel |
| Storlek | Gigabyte | Megabyte |
| Uppstart | Minuter | Sekunder |
| Overhead | Hög | Låg |

**Underliggande teknologi (Linux kernel):**
- **Namespaces**: Isolering (process, nätverk, filsystem)
- **Cgroups**: Resursbegränsning (CPU, RAM)
- **Union filesystem**: Lager på lager`,
          pro_tip: "Tänk VM som att bygga ett helt hus per gäst. Container är hyreslägenhet med delad grund, el, VVS."
        },
        {
          type: "concept",
          title: "Image vs Container",
          explanation: `**Image:**
- Mall/ritning för en container
- Read-only lager
- Byggs från Dockerfile
- Delas via registries (Docker Hub)

**Container:**
- Körande instans av en image
- Eget skrivbart lager ovanpå imagen
- Isolerad process

**Analogi:** Image = Klass, Container = Objekt/instans`,
          pro_tip: "En image kan ha många körande containers. Ändring i en container påverkar inte andra."
        },
        {
          type: "code",
          title: "Docker-kommandon",
          language: "bash",
          code: `# === IMAGES ===
docker pull nginx              # Ladda ner
docker images                  # Lista lokala
docker rmi nginx               # Ta bort

# === CONTAINERS ===
docker run nginx               # Skapa och starta
docker run -d nginx            # Detached (bakgrund)
docker run -d -p 8080:80 nginx # Port-mapping host:container
docker run -d --name web nginx # Med namn

docker ps                      # Körande containers
docker ps -a                   # Alla (även stoppade)

docker stop web                # Stoppa
docker start web               # Starta
docker rm web                  # Ta bort

# === INSPEKTERA ===
docker logs web                # Visa loggar
docker logs -f web             # Följ loggar
docker exec -it web bash       # Shell i container`
        },
        {
          type: "concept",
          title: "Dockerfile",
          explanation: `\`\`\`dockerfile
FROM ubuntu:22.04           # Bas-image

RUN apt-get update && \\     # Installera
    apt-get install -y nginx

COPY index.html /var/www/   # Kopiera filer

EXPOSE 80                   # Dokumentera port

CMD ["nginx", "-g", "daemon off;"]  # Startkommando
\`\`\`

**Bygg:** \`docker build -t myapp:v1 .\`
**Kör:** \`docker run -d -p 8080:80 myapp:v1\``,
          pro_tip: "FROM = bas, RUN = bygg-steg, COPY = filer in, CMD = startkommando."
        },
        {
          type: "concept",
          title: "Volymer – persistent data",
          explanation: `Containers är ephemeral – data försvinner vid borttagning.

**Lösning: Volymer**
\`\`\`bash
# Named volume
docker run -v mydata:/data nginx

# Bind mount
docker run -v /host/path:/container/path nginx
\`\`\``,
          pro_tip: "Databaser i containers MÅSTE ha volymer, annars försvinner all data."
        },
        {
          type: "checkpoint",
          message: "Du har slutfört KM7: Containerteknik (Docker)!"
        }
      ]
    },

    // ============================================
    // KM8: GIT & VERSIONSHANTERING
    // ============================================
    {
      id: "doe25-km8-git",
      title: "KM8: Git & versionshantering",
      description: "Förklara användningen av versionshanteringsverktyg som Git i moderna utvecklingsprocesser",
      order_index: 8,
      estimated_minutes: 35,
      content_blocks: [
        {
          type: "intro",
          headline: "Git – tidsmaskinen för kod",
          learning_objectives: [
            "Varför versionshantering behövs",
            "git add, commit, push, pull",
            "Branching och merging",
            "Gits roll i DevOps"
          ]
        },
        {
          type: "concept",
          title: "Git-koncept",
          explanation: `**Utan Git:** fil_v1.txt, fil_final.txt, fil_final_FINAL.txt
**Med Git:** Fullständig historik, samarbete, trygghet

**Repository (repo):** Projektmapp med all historik (.git-mappen)

**Workflow:**
\`\`\`
Working directory → Staging → Local repo → Remote repo
Ändra filer → git add → git commit → git push
              staging    lokal historik  server
\`\`\`

**Branch:** Parallell utvecklingslinje
**Commit:** En sparad version med meddelande`,
          pro_tip: "Staging area låter dig välja exakt vad som ska ingå i nästa commit."
        },
        {
          type: "code",
          title: "Git-kommandon",
          language: "bash",
          code: `# Setup
git config --global user.name "Said"
git config --global user.email "said@example.com"

# Skapa/klona
git init                        # Nytt repo
git clone <url>                 # Kopiera

# Dagligt arbete
git status                      # Vad har ändrats?
git add .                       # Stagea allt
git commit -m "Beskrivning"     # Spara
git push                        # Skicka till server
git pull                        # Hämta från server

# Historik
git log --oneline               # Kompakt historik
git diff                        # Visa ändringar

# Branches
git branch                      # Lista
git checkout -b feature         # Skapa och byt
git merge feature               # Mergea in

# Ångra
git revert <commit>             # Säker ångrning (ny commit)
git reset --hard HEAD~1         # Farligt (tar bort)`
        },
        {
          type: "concept",
          title: "Branching-workflow",
          explanation: `**Varför branches?**
- Jobba på features utan att störa main
- Experimentera säkert
- Code review via pull requests

**Vanligt flöde:**
\`\`\`bash
git checkout -b feature/login   # Skapa branch
# ... arbeta ...
git add . && git commit -m "Add login"
git push -u origin feature/login
# → Pull Request → Code Review → Merge
\`\`\``,
          pro_tip: "Aldrig commit direkt till main i team-projekt. Använd branches och pull requests."
        },
        {
          type: "concept",
          title: "Git i DevOps",
          explanation: `**CI/CD-koppling:**
1. Developer pushar kod
2. CI-pipeline triggas automatiskt
3. Tester körs
4. Om OK → deploy

**GitOps:**
- Infrastruktur definieras i Git
- Ändringar via pull requests
- Automatisk deploy från main`,
          pro_tip: "Git är navet i modern DevOps. All förändring – kod, infrastruktur, config – går genom Git."
        },
        {
          type: "concept",
          title: "Fetch vs Pull",
          explanation: `**git fetch:** Hämtar ändringar men integrerar dem INTE
**git pull:** fetch + merge (hämtar och integrerar)

Använd fetch när du vill se vad som ändrats innan du mergar.`
        },
        {
          type: "checkpoint",
          message: "Du har slutfört KM8: Git & versionshantering! 🎉"
        }
      ]
    }
  ]
};

// Export individual tasks for easy access
export const DOE25_TASKS = DOE25_MODULE.tasks;

// Get task by ID
export const getTaskById = (id: string) => DOE25_TASKS.find(t => t.id === id);

// Get task by KM number
export const getTaskByKM = (km: number) => DOE25_TASKS.find(t => t.order_index === km);
