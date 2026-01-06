/**
 * TENTAISH EXPANSION - 200 NYA QUIZ-FRÅGOR
 * Moment 3: Docker & Disk/LUKS-kryptering
 * 
 * Skapad: 2026-01-06
 */

import { TentaishQuestion } from './tentaish-quiz'

// =============================================================================
// MOMENT 3A: DOCKER - NYA FRÅGOR (25 st)
// =============================================================================

export const DOCKER_EXTRA: TentaishQuestion[] = [
    {
        id: 'tent-docker-ex-1',
        question: 'Vad är en Docker image?',
        options: [
            'En körande process',
            'En skrivskyddad mall för att skapa containers',
            'En konfigurationsfil',
            'En loggfil'
        ],
        correctIndex: 1,
        explanation: 'En image är en read-only template med applikation + beroenden. Containers skapas från images.',
        difficulty: 'G',
        category: 'Docker Grundläggande'
    },
    {
        id: 'tent-docker-ex-2',
        question: 'Vad är en Docker container?',
        options: [
            'En virtuell maskin',
            'En körande instans av en image',
            'En konfigurationsfil',
            'En nätverksbrygga'
        ],
        correctIndex: 1,
        explanation: 'Container = körande image med eget filsystem, nätverk och processer. Isolerad från host.',
        difficulty: 'G',
        category: 'Docker Grundläggande'
    },
    {
        id: 'tent-docker-ex-3',
        question: 'Vad gör "docker run -d nginx"?',
        options: [
            'Tar bort nginx',
            'Startar nginx-container i bakgrunden (detached)',
            'Debuggar nginx',
            'Laddar ner nginx'
        ],
        correctIndex: 1,
        explanation: '-d (detached) kör containern i bakgrunden. Utan -d fastnar terminalen.',
        difficulty: 'G',
        category: 'Docker Run'
    },
    {
        id: 'tent-docker-ex-4',
        question: 'Vad gör "docker run -p 8080:80 nginx"?',
        options: [
            'Pausar på port 80',
            'Mappar host-port 8080 till container-port 80',
            'Sätter prioritet 80',
            'Kör med 80% CPU'
        ],
        correctIndex: 1,
        explanation: '-p host:container publicerar portar. Trafik till localhost:8080 går till containerns port 80.',
        difficulty: 'G',
        category: 'Docker Nätverk'
    },
    {
        id: 'tent-docker-ex-5',
        question: 'Vad gör "docker ps -a"?',
        options: [
            'Listar endast körande containers',
            'Listar ALLA containers inklusive stoppade',
            'Visar alla processer',
            'Analyserar containers'
        ],
        correctIndex: 1,
        explanation: '-a visar alla containers. Utan -a ser du bara körande. -q ger bara IDs.',
        difficulty: 'G',
        category: 'Docker Grundläggande'
    },
    {
        id: 'tent-docker-ex-6',
        question: 'Hur tar du bort en container?',
        options: [
            'docker delete container_id',
            'docker rm container_id',
            'docker remove container_id',
            'docker destroy container_id'
        ],
        correctIndex: 1,
        explanation: 'docker rm tar bort containers. Lägg till -f för att tvinga bort körande container.',
        difficulty: 'G',
        category: 'Docker Grundläggande'
    },
    {
        id: 'tent-docker-ex-7',
        question: 'Hur tar du bort en image?',
        options: [
            'docker rmi image_id',
            'docker rm image_id',
            'docker delete image',
            'docker image remove'
        ],
        correctIndex: 0,
        explanation: 'rmi = remove image. rm är för containers. Kan inte ta bort image som används.',
        difficulty: 'G',
        category: 'Docker Images'
    },
    {
        id: 'tent-docker-ex-8',
        question: 'Vad är en Dockerfile?',
        options: [
            'Docker-loggfil',
            'Textfil med instruktioner för att bygga en image',
            'Docker-konfiguration',
            'Container-backup'
        ],
        correctIndex: 1,
        explanation: 'Dockerfile innehåller steg-för-steg-instruktioner: FROM, RUN, COPY, CMD etc.',
        difficulty: 'G',
        category: 'Dockerfile'
    },
    {
        id: 'tent-docker-ex-9',
        question: 'Vad gör FROM i en Dockerfile?',
        options: [
            'Kopierar filer',
            'Anger basimage att bygga på',
            'Kör kommandon',
            'Sätter arbetskatalog'
        ],
        correctIndex: 1,
        explanation: 'FROM måste vara första instruktionen. Exempel: FROM ubuntu:22.04, FROM node:18.',
        difficulty: 'G',
        category: 'Dockerfile'
    },
    {
        id: 'tent-docker-ex-10',
        question: 'Vad är skillnaden mellan CMD och ENTRYPOINT?',
        options: [
            'Ingen skillnad',
            'CMD kan överskridas vid docker run, ENTRYPOINT är svårare att ändra',
            'ENTRYPOINT är deprecated',
            'CMD kör vid build'
        ],
        correctIndex: 1,
        explanation: 'ENTRYPOINT definierar huvudkommandot. CMD ger default-argument som kan bytas ut.',
        difficulty: 'VG',
        category: 'Dockerfile'
    },
    {
        id: 'tent-docker-ex-11',
        question: 'Vad gör "docker build -t myapp:1.0 ."?',
        options: [
            'Testar image',
            'Bygger image från Dockerfile i aktuell katalog med tag myapp:1.0',
            'Tar bort image',
            'Kopierar image'
        ],
        correctIndex: 1,
        explanation: '-t taggar imagen. Punkt (.) anger build context (var filer kopieras från).',
        difficulty: 'G',
        category: 'Docker Build'
    },
    {
        id: 'tent-docker-ex-12',
        question: 'Vad är Docker volumes?',
        options: [
            'Ljudinställningar',
            'Persistent lagring som överlever container-restart',
            'CPU-tilldelning',
            'Minneshantering'
        ],
        correctIndex: 1,
        explanation: 'Volumes bevarar data mellan container-körninar. Monteras in i containern.',
        difficulty: 'G',
        category: 'Docker Volumes'
    },
    {
        id: 'tent-docker-ex-13',
        question: 'Vad gör "docker run -v /host/path:/container/path"?',
        options: [
            'Verbose output',
            'Bind mount: kopplar host-katalog till container',
            'Verifierar path',
            'Virtuellt nätverk'
        ],
        correctIndex: 1,
        explanation: 'Bind mount mappar host-path direkt. Ändringar syns på båda sidor i realtid.',
        difficulty: 'G',
        category: 'Docker Volumes'
    },
    {
        id: 'tent-docker-ex-14',
        question: 'Hur går du in i en körande container?',
        options: [
            'docker enter container_id',
            'docker exec -it container_id bash',
            'docker ssh container_id',
            'docker connect container_id'
        ],
        correctIndex: 1,
        explanation: 'exec -it kör kommando interaktivt. -i = interactive, -t = tty/terminal.',
        difficulty: 'G',
        category: 'Docker Exec'
    },
    {
        id: 'tent-docker-ex-15',
        question: 'Vad visar "docker logs container_id"?',
        options: [
            'System logs',
            'Container stdout/stderr output',
            'Docker daemon logs',
            'Build logs'
        ],
        correctIndex: 1,
        explanation: 'Visar allt som containerns process skriver till stdout/stderr. -f följer live.',
        difficulty: 'G',
        category: 'Docker Grundläggande'
    },
    {
        id: 'tent-docker-ex-16',
        question: 'Vad är Docker Compose?',
        options: [
            'En textredigerare',
            'Verktyg för att definiera och köra multi-container applikationer',
            'En image registry',
            'En backup-lösning'
        ],
        correctIndex: 1,
        explanation: 'Compose använder YAML-fil för att definiera services, networks, volumes. docker compose up.',
        difficulty: 'G',
        category: 'Docker Compose'
    },
    {
        id: 'tent-docker-ex-17',
        question: 'Vad heter Docker Compose-konfigurationsfilen som standard?',
        options: [
            'docker-compose.yaml eller compose.yaml',
            'compose.json',
            'docker.yml',
            'containers.yaml'
        ],
        correctIndex: 0,
        explanation: 'docker-compose.yaml, docker-compose.yml eller compose.yaml (nyare). -f för annan fil.',
        difficulty: 'G',
        category: 'Docker Compose'
    },
    {
        id: 'tent-docker-ex-18',
        question: 'Vad gör "docker compose up -d"?',
        options: [
            'Uppdaterar compose',
            'Startar alla services definierade i compose-filen i bakgrunden',
            'Tar bort services',
            'Visar status'
        ],
        correctIndex: 1,
        explanation: 'up startar services, -d i bakgrunden. docker compose down stoppar och tar bort.',
        difficulty: 'G',
        category: 'Docker Compose'
    },
    {
        id: 'tent-docker-ex-19',
        question: 'Vad är Docker Hub?',
        options: [
            'Docker dokumentation',
            'Officiellt image registry för Docker images',
            'Docker support',
            'Container orchestration'
        ],
        correctIndex: 1,
        explanation: 'Docker Hub är default registry. Innehåller officiella images och community-uploads.',
        difficulty: 'G',
        category: 'Docker Registry'
    },
    {
        id: 'tent-docker-ex-20',
        question: 'Vad gör "docker pull ubuntu:22.04"?',
        options: [
            'Tar bort Ubuntu',
            'Laddar ner Ubuntu-image med tag 22.04 från registry',
            'Uppdaterar Ubuntu',
            'Startar Ubuntu'
        ],
        correctIndex: 1,
        explanation: 'pull hämtar image från registry (default Docker Hub). :22.04 är specifik tag/version.',
        difficulty: 'G',
        category: 'Docker Images'
    },
    {
        id: 'tent-docker-ex-21',
        question: 'Vad gör "docker system prune -a"?',
        options: [
            'Analyserar system',
            'Tar bort ALLT oanvänt: containers, images, volumes, networks',
            'Uppdaterar Docker',
            'Visar systemstatus'
        ],
        correctIndex: 1,
        explanation: 'prune städar upp. -a tar även bort images som inte har container. Frigör diskutrymme.',
        difficulty: 'G',
        category: 'Docker Underhåll'
    },
    {
        id: 'tent-docker-ex-22',
        question: 'Vad är multi-stage build i Docker?',
        options: [
            'Parallell build',
            'Flera FROM-instruktioner för att skapa mindre slutimage',
            'Multi-thread build',
            'Distribuerad build'
        ],
        correctIndex: 1,
        explanation: 'Multi-stage: bygg i en stor image, kopiera artifacts till liten runtime-image. Mindre slutresultat.',
        difficulty: 'VG',
        category: 'Dockerfile'
    },
    {
        id: 'tent-docker-ex-23',
        question: 'Vad gör COPY vs ADD i Dockerfile?',
        options: [
            'Samma sak',
            'ADD kan extrahera tar och ladda ner URLs, COPY är enklare',
            'COPY är snabbare',
            'ADD är deprecated'
        ],
        correctIndex: 1,
        explanation: 'Använd COPY för vanlig filkopiering. ADD har extra features men är mindre förutsägbar.',
        difficulty: 'VG',
        category: 'Dockerfile'
    },
    {
        id: 'tent-docker-ex-24',
        question: 'Vad är .dockerignore?',
        options: [
            'Ignorerar Docker-fel',
            'Exkluderar filer/kataloger från build context',
            'Docker-konfiguration',
            'Log-filter'
        ],
        correctIndex: 1,
        explanation: 'Som .gitignore. Förhindrar att node_modules, .git etc skickas till build daemon.',
        difficulty: 'G',
        category: 'Dockerfile'
    },
    {
        id: 'tent-docker-ex-25',
        question: 'Vad gör "docker inspect container_id"?',
        options: [
            'Startar container',
            'Visar detaljerad JSON-info om container (nätverk, mounts, config)',
            'Debuggar container',
            'Loggar container'
        ],
        correctIndex: 1,
        explanation: 'inspect ger all metadata i JSON. IP-adress, mounts, miljövariabler, config etc.',
        difficulty: 'G',
        category: 'Docker Grundläggande'
    }
]

// =============================================================================
// MOMENT 3B: DISK & LUKS-KRYPTERING - NYA FRÅGOR (25 st)
// =============================================================================

export const DISK_EXTRA: TentaishQuestion[] = [
    {
        id: 'tent-disk-ex-1',
        question: 'Vad visar kommandot "lsblk"?',
        options: [
            'Nätverksblock',
            'Block devices (diskar och partitioner) i trädstruktur',
            'Blockerade processer',
            'Filsystemblock'
        ],
        correctIndex: 1,
        explanation: 'lsblk listar alla block devices: diskar, partitioner, LVM, LUKS-volymer etc.',
        difficulty: 'G',
        category: 'Disk Grundläggande'
    },
    {
        id: 'tent-disk-ex-2',
        question: 'Vad visar "df -h"?',
        options: [
            'Disk-fel',
            'Diskutrymme på monterade filsystem i läsbart format',
            'Alla diskar',
            'Filstorlekar'
        ],
        correctIndex: 1,
        explanation: 'df = disk free. -h = human readable (GB/MB). Visar användning per mount point.',
        difficulty: 'G',
        category: 'Disk Grundläggande'
    },
    {
        id: 'tent-disk-ex-3',
        question: 'Vad är LUKS?',
        options: [
            'Linux User Key Storage',
            'Linux Unified Key Setup - standard för diskkryptering',
            'Logical Unit Key System',
            'Linux USB Key System'
        ],
        correctIndex: 1,
        explanation: 'LUKS är standard för full-disk encryption i Linux. Hanterar nycklar och metadata.',
        difficulty: 'G',
        category: 'LUKS'
    },
    {
        id: 'tent-disk-ex-4',
        question: 'Hur skapar du en LUKS-krypterad partition?',
        options: [
            'luks create /dev/sdb1',
            'cryptsetup luksFormat /dev/sdb1',
            'crypt /dev/sdb1',
            'luksformat /dev/sdb1'
        ],
        correctIndex: 1,
        explanation: 'cryptsetup luksFormat initierar LUKS på partitionen. VARNING: Raderar allt!',
        difficulty: 'G',
        category: 'LUKS'
    },
    {
        id: 'tent-disk-ex-5',
        question: 'Hur öppnar du en LUKS-krypterad volym?',
        options: [
            'luks open /dev/sdb1',
            'cryptsetup luksOpen /dev/sdb1 namn',
            'mount -o luks /dev/sdb1',
            'crypt unlock /dev/sdb1'
        ],
        correctIndex: 1,
        explanation: 'luksOpen dekrypterar och skapar /dev/mapper/namn. Sedan kan du montera den.',
        difficulty: 'G',
        category: 'LUKS'
    },
    {
        id: 'tent-disk-ex-6',
        question: 'Var hamnar den öppnade LUKS-volymen?',
        options: [
            '/dev/luks/namn',
            '/dev/mapper/namn',
            '/mnt/luks/namn',
            '/luks/namn'
        ],
        correctIndex: 1,
        explanation: '/dev/mapper/ innehåller dekrypterade volymer och LVM logical volumes.',
        difficulty: 'G',
        category: 'LUKS'
    },
    {
        id: 'tent-disk-ex-7',
        question: 'Hur stänger du en LUKS-volym?',
        options: [
            'cryptsetup close namn',
            'luks close namn',
            'umount /dev/mapper/namn',
            'crypt lock namn'
        ],
        correctIndex: 0,
        explanation: 'cryptsetup close (eller luksClose) stänger mappningen. Unmount först!',
        difficulty: 'G',
        category: 'LUKS'
    },
    {
        id: 'tent-disk-ex-8',
        question: 'Vad är fdisk?',
        options: [
            'File disk',
            'Verktyg för att partitionera diskar (MBR)',
            'Format disk',
            'Find disk'
        ],
        correctIndex: 1,
        explanation: 'fdisk är klassiskt partitioneringsverktyg för MBR. Använd gdisk för GPT.',
        difficulty: 'G',
        category: 'Partitionering'
    },
    {
        id: 'tent-disk-ex-9',
        question: 'Vad är skillnaden mellan MBR och GPT?',
        options: [
            'Ingen skillnad',
            'GPT stödjer större diskar och fler partitioner än MBR',
            'MBR är nyare',
            'GPT är endast för SSD'
        ],
        correctIndex: 1,
        explanation: 'MBR: max 2TB, 4 primära partitioner. GPT: mycket större, 128+ partitioner.',
        difficulty: 'G',
        category: 'Partitionering'
    },
    {
        id: 'tent-disk-ex-10',
        question: 'Hur skapar du ett ext4-filsystem på en partition?',
        options: [
            'format ext4 /dev/sdb1',
            'mkfs.ext4 /dev/sdb1',
            'create ext4 /dev/sdb1',
            'ext4 /dev/sdb1'
        ],
        correctIndex: 1,
        explanation: 'mkfs = make filesystem. mkfs.ext4, mkfs.xfs, mkfs.vfat för olika typer.',
        difficulty: 'G',
        category: 'Filsystem'
    },
    {
        id: 'tent-disk-ex-11',
        question: 'Vad är /etc/fstab?',
        options: [
            'Firewall table',
            'Fil som definierar automatisk montering av filsystem vid boot',
            'Function table',
            'Filesystem attributes'
        ],
        correctIndex: 1,
        explanation: 'fstab = file system table. Anger vilka volymer som monteras var och med vilka optioner.',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 'tent-disk-ex-12',
        question: 'Hur testar du fstab utan att reboota?',
        options: [
            'fstab test',
            'mount -a',
            'systemctl restart fstab',
            'reload fstab'
        ],
        correctIndex: 1,
        explanation: 'mount -a monterar allt i fstab som inte redan är monterat. Avslöjar fel.',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 'tent-disk-ex-13',
        question: 'Vad är UUID i diskkontext?',
        options: [
            'User Unique ID',
            'Universellt unik identifierare för partition/filsystem',
            'Unix Utility ID',
            'Unified Unit Disk'
        ],
        correctIndex: 1,
        explanation: 'UUID är unikt per filsystem. Bättre än /dev/sdX som kan ändras mellan boots.',
        difficulty: 'G',
        category: 'Disk Grundläggande'
    },
    {
        id: 'tent-disk-ex-14',
        question: 'Hur hittar du UUID för en partition?',
        options: [
            'blkid',
            'uuid /dev/sdb1',
            'fdisk -u',
            'lsblk --id'
        ],
        correctIndex: 0,
        explanation: 'blkid visar UUID, TYPE (filsystem) och LABEL för block devices.',
        difficulty: 'G',
        category: 'Disk Grundläggande'
    },
    {
        id: 'tent-disk-ex-15',
        question: 'Vad är LVM?',
        options: [
            'Linux Virtual Machine',
            'Logical Volume Manager - flexibel diskhantering',
            'Linux Volume Mount',
            'Large Virtual Memory'
        ],
        correctIndex: 1,
        explanation: 'LVM abstraherar fysiska diskar. Tillåter resize, snapshots, striping över diskar.',
        difficulty: 'G',
        category: 'LVM'
    },
    {
        id: 'tent-disk-ex-16',
        question: 'Vad är ordningen i LVM: PV, VG, LV?',
        options: [
            'LV -> VG -> PV',
            'PV (Physical Volume) -> VG (Volume Group) -> LV (Logical Volume)',
            'VG -> PV -> LV',
            'Ingen ordning finns'
        ],
        correctIndex: 1,
        explanation: 'Fysiska volymer (diskar) -> grupperas i Volume Groups -> delas upp i Logical Volumes.',
        difficulty: 'G',
        category: 'LVM'
    },
    {
        id: 'tent-disk-ex-17',
        question: 'Hur skapar du en physical volume för LVM?',
        options: [
            'lvm create pv /dev/sdb',
            'pvcreate /dev/sdb',
            'vgcreate /dev/sdb',
            'lvmcreate pv /dev/sdb'
        ],
        correctIndex: 1,
        explanation: 'pvcreate initierar disk för LVM. Sedan vgcreate för group, lvreate för volumes.',
        difficulty: 'G',
        category: 'LVM'
    },
    {
        id: 'tent-disk-ex-18',
        question: 'Hur utökar du ett LVM logical volume?',
        options: [
            'lvm extend /dev/vg/lv',
            'lvextend -L +10G /dev/vg/lv',
            'lvresize -L +10G /dev/vg/lv',
            'Både B och C fungerar'
        ],
        correctIndex: 3,
        explanation: 'lvextend eller lvresize ökar LV. Glöm inte att också utöka filsystemet efteråt!',
        difficulty: 'VG',
        category: 'LVM'
    },
    {
        id: 'tent-disk-ex-19',
        question: 'Hur utökar du ext4-filsystemet efter lvextend?',
        options: [
            'ext4resize /dev/vg/lv',
            'resize2fs /dev/vg/lv',
            'fsresize ext4 /dev/vg/lv',
            'extendfs /dev/vg/lv'
        ],
        correctIndex: 1,
        explanation: 'resize2fs för ext2/3/4. xfs_growfs för XFS. Kan göras online på monterat FS.',
        difficulty: 'VG',
        category: 'Filsystem'
    },
    {
        id: 'tent-disk-ex-20',
        question: 'Vad visar "du -sh /var"?',
        options: [
            'Disk usage',
            'Storlek på /var-katalogen i läsbart format',
            'Disk utility',
            'Directory upload'
        ],
        correctIndex: 1,
        explanation: 'du = disk usage. -s = summary, -h = human readable. Visar faktisk användning.',
        difficulty: 'G',
        category: 'Disk Grundläggande'
    },
    {
        id: 'tent-disk-ex-21',
        question: 'Hur lägger du till en extra nyckel till LUKS?',
        options: [
            'luks addkey',
            'cryptsetup luksAddKey /dev/sdb1',
            'crypt key add',
            'lukskey add /dev/sdb1'
        ],
        correctIndex: 1,
        explanation: 'LUKS stödjer upp till 8 key slots. luksAddKey lägger till, luksRemoveKey tar bort.',
        difficulty: 'VG',
        category: 'LUKS'
    },
    {
        id: 'tent-disk-ex-22',
        question: 'Vad gör "cryptsetup luksDump /dev/sdb1"?',
        options: [
            'Dumpar data',
            'Visar LUKS-header information (slots, cipher, etc)',
            'Tar bort kryptering',
            'Exporterar nycklar'
        ],
        correctIndex: 1,
        explanation: 'luksDump visar metadata: UUID, cipher, key slots, hash. Visar INTE nycklar.',
        difficulty: 'G',
        category: 'LUKS'
    },
    {
        id: 'tent-disk-ex-23',
        question: 'Hur kontrollerar du filsystemintegritet?',
        options: [
            'checkfs /dev/sdb1',
            'fsck /dev/sdb1',
            'diskcheck /dev/sdb1',
            'verify /dev/sdb1'
        ],
        correctIndex: 1,
        explanation: 'fsck = file system check. MÅSTE köras på omonterat filsystem! -n för read-only check.',
        difficulty: 'G',
        category: 'Filsystem'
    },
    {
        id: 'tent-disk-ex-24',
        question: 'Vad är swap?',
        options: [
            'Filbyte',
            'Virtuellt minne på disk när RAM är fullt',
            'Disk-byte',
            'Backup-minne'
        ],
        correctIndex: 1,
        explanation: 'Swap-partition eller swap-fil används när fysiskt RAM tar slut. Långsammare än RAM.',
        difficulty: 'G',
        category: 'Swap'
    },
    {
        id: 'tent-disk-ex-25',
        question: 'Hur aktiverar du en swap-partition?',
        options: [
            'mount /dev/sdb2 swap',
            'swapon /dev/sdb2',
            'swap enable /dev/sdb2',
            'mkswap /dev/sdb2'
        ],
        correctIndex: 1,
        explanation: 'Först mkswap för att formatera, sedan swapon för att aktivera. swapoff inaktiverar.',
        difficulty: 'G',
        category: 'Swap'
    }
]
