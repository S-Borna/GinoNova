/**
 * NOD 9: Docker Nätverk & Lagring - SCENARIO Questions
 * 20 verklighetstrogna scenariofrågor
 */

import type { Omtenta2Question } from './omtenta-2.0-quiz'

export const SCENARIO_NOD9_QUESTIONS: Omtenta2Question[] = [
    {
        id: 'nod9-s1',
        question: 'Du kör nginx i Docker och vill att port 8080 på host ska gå till port 80 i containern. Flagga?',
        options: ['docker run -p 80:8080 nginx', 'docker run -p 8080:80 nginx', 'docker run --port 8080=80 nginx', 'docker run -P 8080:80 nginx'],
        correctIndices: [1],
        explanation: '-p HOST:CONTAINER. -p 8080:80 = host port 8080 → container port 80.',
        difficulty: 'G',
        category: 'Port mapping',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s2',
        question: 'En container försöker ansluta till host-maskinen localhost:5432 (PostgreSQL). Det funkar inte. Varför?',
        options: ['Postgres är inte igång', 'Container har eget nätverk - localhost pekar på containern själv', 'Port 5432 är blockerad', 'Docker stödjer inte PostgreSQL'],
        correctIndices: [1],
        explanation: 'localhost i container = containern själv, inte host. Använd host.docker.internal (Mac/Win) eller host IP.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s3',
        question: 'Du vill att data i din PostgreSQL-container ska överleva restart. Vilka två typer av volumes finns?',
        options: ['Local och remote volumes', 'Bind mounts och named volumes', 'Persistent och ephemeral', 'Internal och external'],
        correctIndices: [1],
        explanation: 'Bind mounts = mappar host-katalog. Named volumes = hanteras av Docker i /var/lib/docker/volumes.',
        difficulty: 'G',
        category: 'Volumes',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s4',
        question: 'Du vill skapa ett custom Docker-nätverk där containers kan nå varandra via namn. Kommando?',
        options: ['docker network create mynet', 'docker create network mynet', 'docker net add mynet', 'docker add-network mynet'],
        correctIndices: [0],
        explanation: 'docker network create skapar user-defined network med inbyggd DNS. Containers på samma nätverk kan pinga med namn.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s5',
        question: 'Du kör två containers på samma custom network. Container "web" vill ansluta till container "db". Vilken hostname?',
        options: ['localhost', 'db', 'container-db', 'docker-db'],
        correctIndices: [1],
        explanation: 'På user-defined networks fungerar containernamn som hostname. web kan ansluta till db:5432 direkt.',
        difficulty: 'G',
        category: 'DNS',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s6',
        question: 'Du vill montera /home/dev/app till /app i containern för utveckling. Syntax?',
        options: ['docker run -v /home/dev/app:/app', 'docker run --mount /home/dev/app=/app', 'docker run -m /home/dev/app:/app', 'docker run --bind /home/dev/app:/app'],
        correctIndices: [0],
        explanation: '-v HOST_PATH:CONTAINER_PATH är bind mount syntax. Ändringar på host syns direkt i containern.',
        difficulty: 'G',
        category: 'Volumes',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s7',
        question: 'Du vill skapa en named volume och montera den i containern. Kommando?',
        options: ['docker volume create data && docker run -v data:/var/lib/data image', 'docker run --volume-create data:/var/lib/data image', 'docker run -nv data:/var/lib/data image', 'Man måste använda docker-compose för named volumes'],
        correctIndices: [0],
        explanation: 'docker volume create skapar volume. Sen -v volname:/path monterar. Docker skapar också vid första -v om den saknas.',
        difficulty: 'VG',
        category: 'Volumes',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s8',
        question: 'Vilket Docker-nätverk är default om du inte anger något?',
        options: ['host', 'none', 'bridge', 'overlay'],
        correctIndices: [2],
        explanation: 'bridge är default. Containers får privat IP och kan nå omvärlden via NAT. OBS: ingen DNS på default bridge!',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s9',
        question: 'Du vill att containern ska använda hostens nätverk direkt (ingen isolering). Nätverks-flagga?',
        options: ['--network=direct', '--network=host', '--network=none', '--network=bridge'],
        correctIndices: [1],
        explanation: '--network=host ger containern samma nätverk som host. Port 80 i container = port 80 på host.',
        difficulty: 'VG',
        category: 'Nätverk',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s10',
        question: 'Du tar bort en container men vill behålla dess data. Var lagras named volumes?',
        options: ['/var/docker/volumes', '/var/lib/docker/volumes', '/home/docker/data', '/etc/docker/volumes'],
        correctIndices: [1],
        explanation: 'Named volumes lagras i /var/lib/docker/volumes på host. Överlever container borttagning.',
        difficulty: 'VG',
        category: 'Volumes',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s11',
        question: 'Du vill lista alla Docker-nätverk på systemet. Kommando?',
        options: ['docker network ls', 'docker networks', 'docker net list', 'docker show networks'],
        correctIndices: [0],
        explanation: 'docker network ls visar alla nätverk. Default: bridge, host, none. Plus eventuella custom.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s12',
        question: 'Du vill inspektera ett nätverk och se vilka containers som är anslutna. Kommando?',
        options: ['docker network show mynet', 'docker network inspect mynet', 'docker net details mynet', 'docker network info mynet'],
        correctIndices: [1],
        explanation: 'docker network inspect visar config, subnet, connected containers med IP-adresser.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s13',
        question: 'Du vill montera volume som read-only så containern inte kan ändra data. Syntax?',
        options: ['docker run -v data:/app:ro', 'docker run -v data:/app:readonly', 'docker run -v data:/app --readonly', 'docker run -v data:/app -r'],
        correctIndices: [0],
        explanation: ':ro suffix gör mount read-only. Bra för config-filer och statisk data.',
        difficulty: 'VG',
        category: 'Volumes',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s14',
        question: 'Vad är skillnaden mellan -p och -P (stor P) i docker run?',
        options: ['Ingen skillnad', '-p anger specifik port, -P publicerar alla EXPOSE-portar till random host-portar', '-P är persistent', '-P är för produktion'],
        correctIndices: [1],
        explanation: '-P publicerar alla portar definierade med EXPOSE i Dockerfile till random lediga host-portar.',
        difficulty: 'VG',
        category: 'Port mapping',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s15',
        question: 'Du vill ansluta en körande container till ett annat nätverk. Kommando?',
        options: ['docker network connect mynet container', 'docker container add-network mynet', 'docker connect container mynet', 'docker network add container mynet'],
        correctIndices: [0],
        explanation: 'docker network connect lägger till container på nätverk. En container kan vara på flera nätverk.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s16',
        question: 'Var i Dockerfile definierar du vilka portar containern lyssnar på?',
        options: ['PORT 80', 'EXPOSE 80', 'LISTEN 80', 'OPEN 80'],
        correctIndices: [1],
        explanation: 'EXPOSE dokumenterar vilka portar appen lyssnar på. Publicerar INTE automatiskt - det gör -p.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s17',
        question: 'Du har old volumes som inte längre används. Kommando för att städa?',
        options: ['docker volume rm --all', 'docker volume prune', 'docker clean volumes', 'docker volume delete --unused'],
        correctIndices: [1],
        explanation: 'docker volume prune tar bort alla volumes som inte används av någon container.',
        difficulty: 'G',
        category: 'Volumes',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s18',
        question: 'Din app i container behöver nå en tjänst på host-maskinen. Vilken special-DNS finns på Mac/Windows?',
        options: ['localhost', 'docker.host', 'host.docker.internal', 'host.local'],
        correctIndices: [2],
        explanation: 'host.docker.internal pekar på host-maskinen. Fungerar på Mac/Windows. Linux kräver --add-host.',
        difficulty: 'VG',
        category: 'DNS',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s19',
        question: 'Du vill se vilka portar en körande container har mappade. Kommando?',
        options: ['docker ports container', 'docker port container', 'docker ps --ports container', 'docker show-ports container'],
        correctIndices: [1],
        explanation: 'docker port container visar port mappings. docker ps visar också portar i output.',
        difficulty: 'G',
        category: 'Port mapping',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    },
    {
        id: 'nod9-s20',
        question: 'Du behöver köra container utan något nätverk alls (max isolering). Nätverks-flagga?',
        options: ['--network=isolated', '--network=none', '--network=disabled', '--no-network'],
        correctIndices: [1],
        explanation: '--network=none ger ingen nätverksaccess. Bara loopback interface. Maximum network isolation.',
        difficulty: 'VG',
        category: 'Nätverk',
        topic: 'nod9-docker-natverk',
        type: 'scenario'
    }
]
