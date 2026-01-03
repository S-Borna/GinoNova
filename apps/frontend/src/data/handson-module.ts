// Hands-On Lab Module - 7 Praktiska Tasks
// Interfaces

export interface QuizOption {
    text: string;
    correct?: boolean;
    feedback?: string;
}

export interface CompareItem {
    name: string;
    pros: string[];
    cons: string[];
    use_case?: string;
}

export interface ContentBlock {
    type: string;
    title?: string;
    headline?: string;
    explanation?: string;
    code?: string;
    language?: string;
    options?: QuizOption[];
    question?: string;
    hint?: string;
    pro_tip?: string;
    warning?: string;
    warning_level?: string;
    learning_objectives?: string[];
    scenario_title?: string;
    scenario_context?: string;
    scenario_symptoms?: string[];
    scenario_solution?: string;
    challenge_task?: string;
    challenge_commands?: string[];
    expected_output?: string;
    diagram?: string;
    diagram_caption?: string;
    message?: string;
    items?: string[];
    compare_items?: CompareItem[];
    summary_title?: string;
    key_points?: string[];
    next_step?: string;
}

export interface HandsOnTask {
    id: string;
    title: string;
    description: string;
    order_index: number;
    estimated_minutes: number;
    content_blocks: ContentBlock[];
}

export interface HandsOnModule {
    id: string;
    name: string;
    slug: string;
    description: string;
    difficulty: "beginner" | "intermediate" | "advanced" | "expert";
    estimated_hours: number;
    tasks: HandsOnTask[];
}

// ============================================
// SLUG TO ID MAPPING
// ============================================
export const SLUG_TO_ID: Record<string, string> = {
    "handson-onboarding": "handson-1-onboarding",
    "handson-pakethantering-ssh": "handson-2-pakethantering",
    "handson-ssh-brandvagg": "handson-3-ssh-brandvagg",
    "handson-anvandarhantering": "handson-4-anvandarhantering",
    "handson-subnetting": "handson-5-subnetting",
    "handson-docker-containers": "handson-6-docker",
    "handson-block-storage-kryptering": "handson-7-storage",
};

// ============================================
// HANDS-ON LAB MODULE - 7 TASKS
// ============================================

export const HANDSON_MODULE: HandsOnModule = {
    id: "hands-on-lab",
    name: "Hands-On Lab",
    slug: "hands-on-lab",
    description: "Praktiska labbar som tar dig från grunderna till avancerade Linux- och DevOps-koncept",
    difficulty: "intermediate",
    estimated_hours: 6,
    tasks: [
        // ============================================
        // TASK 1: ONBOARDING - FILSYSTEM & TEXTEDITORER
        // ============================================
        {
            id: "handson-1-onboarding",
            title: "Onboarding - Filsystem & Texteditorer",
            description: "Navigera i Linux filsystem, skapa och hantera filer, samt använda Nano och Vim",
            order_index: 0,
            estimated_minutes: 45,
            content_blocks: [
                {
                    type: "intro",
                    headline: "📁 Onboarding - Filsystem & Texteditorer",
                    learning_objectives: [
                        "Navigera i Linux filsystem med cd, pwd, ls",
                        "Skapa och hantera filer och kataloger",
                        "Använda Nano texteditor",
                        "Grundläggande Vim-kommandon"
                    ]
                },
                {
                    type: "concept",
                    title: "Navigering i filsystemet",
                    explanation: `Grundläggande kommandon för att navigera:

cd ~          # Gå till din hemmapp
pwd           # Visa aktuell sökväg
ls -la        # Lista alla filer (inkl dolda)
mkdir -p dir/subdir  # Skapa katalogstruktur`
                },
                {
                    type: "code",
                    title: "Filhantering",
                    language: "bash",
                    code: `# Skapa fil
touch README.md
echo "# Projekt" > README.md

# Kopiera och flytta
cp fil.txt kopia.txt
mv fil.txt ny_mapp/

# Ta bort
rm fil.txt
rm -r katalog/`
                },
                {
                    type: "concept",
                    title: "Nano Editor",
                    explanation: `Nano är en nybörjarvänlig editor:

nano fil.txt    # Öppna/skapa fil

Genvägar:
Ctrl+O  →  Spara
Ctrl+X  →  Avsluta
Ctrl+K  →  Klipp rad
Ctrl+U  →  Klistra in
Ctrl+W  →  Sök`
                },
                {
                    type: "concept",
                    title: "Vim Basics",
                    explanation: `Vim har två lägen: Normal (navigera) och Insert (skriva)

vim fil.txt     # Öppna fil
i               # Insert mode (börja skriva)
Esc             # Tillbaka till Normal
:w              # Spara
:q              # Avsluta
:wq             # Spara och avsluta
:q!             # Avsluta UTAN spara`
                },
                {
                    type: "summary",
                    summary_title: "Sammanfattning",
                    key_points: [
                        "cd, pwd, ls för navigering",
                        "mkdir -p för katalogstruktur",
                        "touch, cp, mv, rm för filhantering",
                        "Nano: Ctrl+O spara, Ctrl+X avsluta",
                        "Vim: i för insert, Esc + :wq för spara/avsluta"
                    ]
                }
            ]
        },
        // ============================================
        // TASK 2: PAKETHANTERING & SSH-NYCKLAR
        // ============================================
        {
            id: "handson-2-pakethantering",
            title: "Pakethantering & SSH-nycklar",
            description: "Hantera paket med APT och sätta upp SSH-nycklar för säker inloggning",
            order_index: 1,
            estimated_minutes: 40,
            content_blocks: [
                {
                    type: "intro",
                    headline: "📦 Pakethantering & SSH-nycklar",
                    learning_objectives: [
                        "Hantera paket med APT",
                        "Generera SSH-nyckelpar",
                        "Konfigurera SSH för automatisk inloggning",
                        "Skapa SSH config-fil"
                    ]
                },
                {
                    type: "code",
                    title: "APT Grundkommandon",
                    language: "bash",
                    code: `# Uppdatera paketlistor
sudo apt update

# Uppgradera paket
sudo apt upgrade -y

# Sök och installera
apt search nginx
sudo apt install nginx -y

# Ta bort
sudo apt remove nginx
sudo apt purge nginx
sudo apt autoremove`
                },
                {
                    type: "concept",
                    title: "SSH-nycklar - Varför?",
                    explanation: `Lösenord vs SSH-nyckel:
┌──────────────┬─────────────────────┐
│ Lösenord     │ SSH-nyckel          │
├──────────────┼─────────────────────┤
│ Kan gissas   │ Omöjligt att gissa  │
│ Skrivs varje │ Automatisk login    │
│ Sårbart      │ Mycket säkert       │
└──────────────┴─────────────────────┘`
                },
                {
                    type: "code",
                    title: "Generera SSH-nyckel",
                    language: "bash",
                    code: `# Skapa nyckelpar
ssh-keygen -t ed25519 -C "din@email.com"

# Resultat:
# ~/.ssh/id_ed25519      (PRIVAT - aldrig dela!)
# ~/.ssh/id_ed25519.pub  (Publik - kan delas)

# Kopiera till server
ssh-copy-id user@server-ip`
                },
                {
                    type: "code",
                    title: "SSH Config",
                    language: "bash",
                    code: `# ~/.ssh/config
Host prod
    HostName 192.168.1.100
    User deploy
    IdentityFile ~/.ssh/id_ed25519

# Användning:
ssh prod  # Istället för: ssh deploy@192.168.1.100`
                },
                {
                    type: "summary",
                    summary_title: "Sammanfattning",
                    key_points: [
                        "apt update innan install",
                        "ssh-keygen -t ed25519 för nycklar",
                        "Privat nyckel: ALDRIG dela",
                        "~/.ssh/config för genvägar",
                        "chmod 600 på privata nycklar"
                    ]
                }
            ]
        },
        // ============================================
        // TASK 3: SSH & BRANDVÄGG
        // ============================================
        {
            id: "handson-3-ssh-brandvagg",
            title: "SSH & Brandvägg",
            description: "Konfigurera SSH-servern säkert och sätta upp UFW brandvägg",
            order_index: 2,
            estimated_minutes: 50,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🔥 SSH & Brandvägg",
                    learning_objectives: [
                        "Konfigurera sshd_config säkert",
                        "Byta SSH-port och inaktivera root-login",
                        "Sätta upp UFW brandvägg",
                        "Felsöka SSH och brandvägg"
                    ]
                },
                {
                    type: "code",
                    title: "SSH Server Config",
                    language: "bash",
                    code: `# Backup först!
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup

# Redigera config
sudo nano /etc/ssh/sshd_config

# Viktiga inställningar:
Port 2222                    # Byt från 22
PermitRootLogin no           # Förbjud root
PasswordAuthentication no    # Endast nycklar
PubkeyAuthentication yes
AllowUsers deploy admin      # Whitelist

# Validera och starta om
sudo sshd -t
sudo systemctl restart sshd`
                },
                {
                    type: "warning",
                    warning: "TESTA ALLTID SSH i en NY terminal innan du stänger den gamla!",
                    warning_level: "critical"
                },
                {
                    type: "code",
                    title: "UFW Brandvägg",
                    language: "bash",
                    code: `# Default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Tillåt SSH FÖRST!
sudo ufw allow ssh
sudo ufw allow 2222/tcp  # Om du bytt port

# Tillåt webserver
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Aktivera
sudo ufw enable

# Visa status
sudo ufw status verbose`
                },
                {
                    type: "code",
                    title: "Felsökning",
                    language: "bash",
                    code: `# SSH loggar
sudo journalctl -u sshd -f

# Testa SSH verbose
ssh -v user@server

# UFW loggar
sudo tail -f /var/log/ufw.log

# Se vad som lyssnar
sudo ss -tlnp | grep ssh`
                },
                {
                    type: "summary",
                    summary_title: "Sammanfattning",
                    key_points: [
                        "Ändra SSH-port från 22",
                        "PermitRootLogin no",
                        "Tillåt SSH INNAN ufw enable",
                        "Testa i ny terminal!",
                        "journalctl -u sshd för loggar"
                    ]
                }
            ]
        },
        // ============================================
        // TASK 4: ANVÄNDARHANTERING
        // ============================================
        {
            id: "handson-4-anvandarhantering",
            title: "Användarhantering",
            description: "Skapa användare, grupper och hantera behörigheter",
            order_index: 3,
            estimated_minutes: 40,
            content_blocks: [
                {
                    type: "intro",
                    headline: "👥 Användarhantering",
                    learning_objectives: [
                        "Skapa och modifiera användare",
                        "Hantera grupper och medlemskap",
                        "Konfigurera sudo-rättigheter",
                        "Förstå viktiga systemfiler"
                    ]
                },
                {
                    type: "code",
                    title: "Skapa användare",
                    language: "bash",
                    code: `# Skapa med hemmapp
sudo useradd -m -s /bin/bash -c "Deploy User" deploy

# Sätt lösenord
sudo passwd deploy

# Modifiera användare
sudo usermod -aG docker deploy  # Lägg till i grupp
sudo usermod -s /bin/zsh deploy # Ändra shell

# Ta bort
sudo userdel -r deploy  # -r tar bort hemmapp`
                },
                {
                    type: "code",
                    title: "Grupper",
                    language: "bash",
                    code: `# Skapa grupp
sudo groupadd webteam

# Lägg till medlem
sudo usermod -aG webteam deploy

# Se medlemmar
getent group webteam

# Ta bort från grupp
sudo gpasswd -d deploy webteam`
                },
                {
                    type: "code",
                    title: "Sudo-rättigheter",
                    language: "bash",
                    code: `# Lägg till i sudo-gruppen
sudo usermod -aG sudo deploy

# Eller via sudoers (säkrare)
sudo nano /etc/sudoers.d/deploy

# Innehåll:
deploy ALL=(ALL) NOPASSWD: ALL

# Sätt rättigheter
sudo chmod 440 /etc/sudoers.d/deploy`
                },
                {
                    type: "concept",
                    title: "Viktiga filer",
                    explanation: `/etc/passwd  - Användarlista
/etc/shadow  - Krypterade lösenord
/etc/group   - Grupplista
/etc/sudoers - Sudo-konfiguration`
                },
                {
                    type: "summary",
                    summary_title: "Sammanfattning",
                    key_points: [
                        "useradd -m -s /bin/bash",
                        "usermod -aG för grupper",
                        "visudo eller /etc/sudoers.d/",
                        "chmod 440 på sudoers-filer",
                        "groups <user> visar medlemskap"
                    ]
                }
            ]
        },
        // ============================================
        // TASK 5: SUBNETTING
        // ============================================
        {
            id: "handson-5-subnetting",
            title: "Subnetting",
            description: "Beräkna subnät, nätverksadresser och broadcast",
            order_index: 4,
            estimated_minutes: 45,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🌐 Subnetting",
                    learning_objectives: [
                        "Förstå IP-prefix och host-bitar",
                        "Beräkna blockstorlek",
                        "Hitta nätverksadress och broadcast",
                        "Använda ipcalc för verifiering"
                    ]
                },
                {
                    type: "concept",
                    title: "Lådmetoden",
                    explanation: `Memorera dessa värden:
┌─────┬────┬────┬────┬───┬───┬───┬───┐
│ 128 │ 64 │ 32 │ 16 │ 8 │ 4 │ 2 │ 1 │
└─────┴────┴────┴────┴───┴───┴───┴───┘

Host-bitar = 32 - prefix
Blockstorlek = 2^(host-bitar)
Antal hosts = Blockstorlek - 2`
                },
                {
                    type: "concept",
                    title: "Exempel: 192.168.1.147/26",
                    explanation: `Steg 1: Host-bitar = 32 - 26 = 6
Steg 2: Blockstorlek = 2^6 = 64
Steg 3: Subnät = 0, 64, 128, 192...
        147 faller i 128-intervallet

Resultat:
• Nätverksadress: 192.168.1.128
• Broadcast: 192.168.1.191
• Host-range: 192.168.1.129-190
• Antal hosts: 62`
                },
                {
                    type: "concept",
                    title: "Vanliga prefix",
                    explanation: `┌────────┬─────────────────────┬───────┐
│ Prefix │ Subnätmask          │ Hosts │
├────────┼─────────────────────┼───────┤
│ /24    │ 255.255.255.0       │ 254   │
│ /25    │ 255.255.255.128     │ 126   │
│ /26    │ 255.255.255.192     │ 62    │
│ /27    │ 255.255.255.224     │ 30    │
│ /28    │ 255.255.255.240     │ 14    │
│ /29    │ 255.255.255.248     │ 6     │
│ /30    │ 255.255.255.252     │ 2     │
└────────┴─────────────────────┴───────┘`
                },
                {
                    type: "code",
                    title: "Verifiera med ipcalc",
                    language: "bash",
                    code: `sudo apt install ipcalc -y
ipcalc 192.168.1.147/26

# Output:
# Network:   192.168.1.128/26
# Broadcast: 192.168.1.191
# HostMin:   192.168.1.129
# HostMax:   192.168.1.190
# Hosts/Net: 62`
                },
                {
                    type: "summary",
                    summary_title: "Sammanfattning",
                    key_points: [
                        "Host-bitar = 32 - prefix",
                        "Blockstorlek = 2^host-bitar",
                        "Nätverksadress = start av block",
                        "Broadcast = slutet av block",
                        "Hosts = Blockstorlek - 2"
                    ]
                }
            ]
        },
        // ============================================
        // TASK 6: DOCKER & CONTAINERS
        // ============================================
        {
            id: "handson-6-docker",
            title: "Docker & Containers",
            description: "Installera Docker, köra containers, bygga images och använda Compose",
            order_index: 5,
            estimated_minutes: 60,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🐳 Docker & Containers",
                    learning_objectives: [
                        "Installera Docker på Ubuntu",
                        "Köra och hantera containers",
                        "Bygga images med Dockerfile",
                        "Använda Docker Compose"
                    ]
                },
                {
                    type: "code",
                    title: "Installation",
                    language: "bash",
                    code: `# Installera Docker
curl -fsSL https://get.docker.com | sh

# Kör utan sudo
sudo usermod -aG docker $USER
newgrp docker

# Verifiera
docker --version
docker run hello-world`
                },
                {
                    type: "code",
                    title: "Köra containers",
                    language: "bash",
                    code: `# Interaktivt
docker run -it ubuntu bash

# Bakgrund med port
docker run -d -p 8080:80 --name web nginx

# Hantera
docker ps           # Lista körande
docker ps -a        # Alla
docker stop web
docker start web
docker rm web`
                },
                {
                    type: "code",
                    title: "Dockerfile",
                    language: "dockerfile",
                    code: `FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]`
                },
                {
                    type: "code",
                    title: "docker-compose.yml",
                    language: "yaml",
                    code: `version: '3.8'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret`
                },
                {
                    type: "code",
                    title: "Compose kommandon",
                    language: "bash",
                    code: `docker compose up -d    # Starta
docker compose ps       # Status
docker compose logs -f  # Loggar
docker compose down     # Stoppa
docker compose down -v  # + ta bort volumes`
                },
                {
                    type: "summary",
                    summary_title: "Sammanfattning",
                    key_points: [
                        "docker run -d -p host:container",
                        "Dockerfile: FROM, WORKDIR, COPY, RUN, CMD",
                        "docker compose up -d för stack",
                        "docker exec -it <container> bash",
                        "docker system prune -a städar"
                    ]
                }
            ]
        },
        // ============================================
        // TASK 7: BLOCK STORAGE & KRYPTERING
        // ============================================
        {
            id: "handson-7-storage",
            title: "Block Storage & Kryptering",
            description: "Hantera diskar, LVM och sätta upp LUKS-kryptering",
            order_index: 6,
            estimated_minutes: 60,
            content_blocks: [
                {
                    type: "intro",
                    headline: "💾 Block Storage & Kryptering",
                    learning_objectives: [
                        "Partitionera diskar",
                        "Skapa filsystem (ext4, xfs)",
                        "Använda LVM för flexibel lagring",
                        "Konfigurera LUKS-kryptering"
                    ]
                },
                {
                    type: "code",
                    title: "Diskar och partitioner",
                    language: "bash",
                    code: `# Se diskar
lsblk
sudo fdisk -l
df -h

# Partitionera
sudo fdisk /dev/sdb
# n (new), p (primary), 1, Enter, Enter, w (write)

# Skapa filsystem
sudo mkfs.ext4 /dev/sdb1

# Mounta
sudo mkdir /mnt/data
sudo mount /dev/sdb1 /mnt/data`
                },
                {
                    type: "concept",
                    title: "LVM Struktur",
                    explanation: `┌─────────────────────────────┐
│    Logical Volume (LV)      │ ← Filsystem
│    /dev/vg_data/lv_files    │
├─────────────────────────────┤
│    Volume Group (VG)        │ ← Pool
│         vg_data             │
├─────────────────────────────┤
│    Physical Volumes (PV)    │ ← Diskar
│    /dev/sdb1  /dev/sdc1     │
└─────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Skapa LVM",
                    language: "bash",
                    code: `# 1. Physical Volume
sudo pvcreate /dev/sdb1

# 2. Volume Group
sudo vgcreate vg_data /dev/sdb1

# 3. Logical Volume
sudo lvcreate -L 5G -n lv_files vg_data

# 4. Filsystem
sudo mkfs.ext4 /dev/vg_data/lv_files

# 5. Mounta
sudo mount /dev/vg_data/lv_files /mnt/files

# Utöka
sudo lvextend -L +2G /dev/vg_data/lv_files
sudo resize2fs /dev/vg_data/lv_files`
                },
                {
                    type: "code",
                    title: "LUKS Kryptering",
                    language: "bash",
                    code: `# Formatera med LUKS
sudo cryptsetup luksFormat /dev/sdb1

# Öppna
sudo cryptsetup luksOpen /dev/sdb1 krypterad

# Skapa filsystem
sudo mkfs.ext4 /dev/mapper/krypterad

# Mounta
sudo mount /dev/mapper/krypterad /mnt/secure

# Stänga
sudo umount /mnt/secure
sudo cryptsetup luksClose krypterad`
                },
                {
                    type: "summary",
                    summary_title: "Sammanfattning",
                    key_points: [
                        "lsblk för diskinfo",
                        "LVM: PV → VG → LV",
                        "lvextend + resize2fs för utökning",
                        "LUKS: luksFormat → luksOpen",
                        "Kombinera LUKS + LVM för säkerhet"
                    ]
                }
            ]
        }
    ]
};

// ============================================
// HELPER FUNCTIONS
// ============================================

export function getHandsOnTaskById(id: string): HandsOnTask | undefined {
    // Check direct ID match
    const directMatch = HANDSON_MODULE.tasks.find(task => task.id === id);
    if (directMatch) return directMatch;

    // Check slug mapping
    const mappedId = SLUG_TO_ID[id];
    if (mappedId) {
        return HANDSON_MODULE.tasks.find(task => task.id === mappedId);
    }

    return undefined;
}

export function getAllHandsOnTasks(): HandsOnTask[] {
    return HANDSON_MODULE.tasks;
}

export function getHandsOnTotalEstimatedMinutes(): number {
    return HANDSON_MODULE.tasks.reduce((total, task) => total + task.estimated_minutes, 0);
}
