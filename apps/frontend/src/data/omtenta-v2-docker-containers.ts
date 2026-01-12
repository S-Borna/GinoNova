/**
 * OMTENTA V2 - Docker & Containers (110 frågor)
 * EXAKT spegling av Omtenta/Docker_Containers_Quiz_110.md
 * 
 * OBS: Inkluderar multi-select frågor (choose X)
 */

import { OmtentaV2Question } from './omtenta-v2-ssh-brandvagg'

// Re-export with correct topic type
export type DockerContainersQuestion = Omit<OmtentaV2Question, 'topic'> & {
    topic: 'docker-containers'
}

export const DOCKER_CONTAINERS_V2_QUESTIONS: DockerContainersQuestion[] = [
    {
        id: 'omtenta-v2-docker-1',
        question: 'A Docker container is...',
        options: ['A virtual machine', 'A disk image', 'An isolated process', 'A network interface'],
        correctIndices: [2],
        explanation: 'En Docker-container är en isolerad process, inte en virtuell maskin.',
        difficulty: 'G',
        category: 'Docker Grundläggande',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-2',
        question: 'Docker image is...',
        options: ['A running container', 'A template for containers', 'A virtual disk', 'A network config'],
        correctIndices: [1],
        explanation: 'En Docker-image är en mall som används för att skapa containers.',
        difficulty: 'G',
        category: 'Docker Grundläggande',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-3',
        question: 'The two types of Docker volumes are...',
        options: ['Local and remote', 'Temp and perm', 'Bind and named', 'Read and write'],
        correctIndices: [2],
        explanation: 'Docker har två typer av volymer: bind mounts och named volumes.',
        difficulty: 'G',
        category: 'Docker Volumes',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-4',
        question: 'A container can access the host\'s localhost',
        options: ['True', 'False'],
        correctIndices: [1],
        explanation: 'En container kan inte direkt nå hostens localhost utan speciell konfiguration.',
        difficulty: 'G',
        category: 'Docker Nätverk',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-5',
        question: 'The host can access a container\'s localhost',
        options: ['True', 'False'],
        correctIndices: [0],
        explanation: 'Hosten kan nå containerns localhost via port mapping.',
        difficulty: 'G',
        category: 'Docker Nätverk',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-6',
        question: 'To list running containers, use...',
        options: ['docker list', 'docker containers', 'docker ps', 'docker show'],
        correctIndices: [2],
        explanation: 'docker ps visar körande containers.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-7',
        question: 'To list all containers, use...',
        options: ['docker ps -r', 'docker list -all', 'docker ps -a', 'docker containers -all'],
        correctIndices: [2],
        explanation: 'docker ps -a visar alla containers, inklusive stoppade.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-8',
        question: 'To start a container from image, use...',
        options: ['docker start nginx', 'docker begin nginx', 'docker run nginx', 'docker create nginx'],
        correctIndices: [2],
        explanation: 'docker run skapar och startar en ny container från en image.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-9',
        question: 'To stop a running container, use...',
        options: ['docker halt', 'docker end', 'docker stop', 'docker terminate'],
        correctIndices: [2],
        explanation: 'docker stop stoppar en körande container.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-10',
        question: 'To remove a container, use...',
        options: ['docker delete', 'docker remove', 'docker rm', 'docker destroy'],
        correctIndices: [2],
        explanation: 'docker rm tar bort en container.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-11',
        question: 'To remove an image, use...',
        options: ['docker rm', 'docker delete', 'docker rmi', 'docker remove-image'],
        correctIndices: [2],
        explanation: 'docker rmi tar bort en image.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-12',
        question: 'To list images, use...',
        options: ['docker list', 'docker show', 'docker images', 'docker img'],
        correctIndices: [2],
        explanation: 'docker images listar alla images.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-13',
        question: 'To download an image, use...',
        options: ['docker get', 'docker download', 'docker pull', 'docker fetch'],
        correctIndices: [2],
        explanation: 'docker pull laddar ner en image från registry.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-14',
        question: 'To upload an image, use...',
        options: ['docker upload', 'docker send', 'docker push', 'docker put'],
        correctIndices: [2],
        explanation: 'docker push laddar upp en image till registry.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-15',
        question: 'To build an image, use...',
        options: ['docker create', 'docker make', 'docker build', 'docker compile'],
        correctIndices: [2],
        explanation: 'docker build skapar en image från en Dockerfile.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-16',
        question: 'To view container logs, use...',
        options: ['docker output', 'docker print', 'docker logs', 'docker show'],
        correctIndices: [2],
        explanation: 'docker logs visar loggar från en container.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-17',
        question: 'To execute command in running container, use...',
        options: ['docker run', 'docker command', 'docker exec', 'docker shell'],
        correctIndices: [2],
        explanation: 'docker exec kör kommandon i en redan körande container.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-18',
        question: 'The -d flag means...',
        options: ['Debug', 'Delete', 'Detached', 'Daemon'],
        correctIndices: [2],
        explanation: '-d flaggan kör containern i detached (bakgrunds) läge.',
        difficulty: 'G',
        category: 'Docker Flaggor',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-19',
        question: 'The -p flag is for...',
        options: ['Password', 'Process', 'Port mapping', 'Path'],
        correctIndices: [2],
        explanation: '-p flaggan används för port mapping mellan host och container.',
        difficulty: 'G',
        category: 'Docker Flaggor',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-20',
        question: 'The -v flag is for...',
        options: ['Verbose', 'Version', 'Volume', 'Virtual'],
        correctIndices: [2],
        explanation: '-v flaggan används för att montera volymer.',
        difficulty: 'G',
        category: 'Docker Flaggor',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-21',
        question: 'Select all valid docker commands (choose 5):',
        options: ['docker ps', 'docker list', 'docker run', 'docker start container', 'docker build', 'docker make', 'docker pull', 'docker download', 'docker logs', 'docker output'],
        correctIndices: [0, 2, 4, 6, 8],
        explanation: 'Giltiga docker-kommandon: docker ps, docker run, docker build, docker pull, docker logs.',
        difficulty: 'VG',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-22',
        question: 'The -it flags provide...',
        options: ['Image tag', 'Interactive terminal', 'Internal transfer', 'Instance type'],
        correctIndices: [1],
        explanation: '-it ger en interaktiv terminal i containern.',
        difficulty: 'G',
        category: 'Docker Flaggor',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-23',
        question: 'The --name flag...',
        options: ['Renames image', 'Names the container', 'Sets hostname', 'Labels the build'],
        correctIndices: [1],
        explanation: '--name ger containern ett specifikt namn.',
        difficulty: 'G',
        category: 'Docker Flaggor',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-24',
        question: 'The --rm flag...',
        options: ['Removes image', 'Removes container on stop', 'Restarts machine', 'Resets memory'],
        correctIndices: [1],
        explanation: '--rm tar automatiskt bort containern när den stoppas.',
        difficulty: 'G',
        category: 'Docker Flaggor',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-25',
        question: 'Port mapping 8080:80 means...',
        options: ['Container 8080 → Host 80', 'Host 8080 → Container 80', 'Both ports 8080', 'Both ports 80'],
        correctIndices: [1],
        explanation: '8080:80 betyder host port 8080 mappar till container port 80.',
        difficulty: 'G',
        category: 'Docker Nätverk',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-26',
        question: 'Dockerfile starts with...',
        options: ['RUN', 'CMD', 'FROM', 'COPY'],
        correctIndices: [2],
        explanation: 'En Dockerfile måste börja med FROM instruktionen.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-27',
        question: 'To run command during build, use...',
        options: ['EXEC', 'CMD', 'RUN', 'DO'],
        correctIndices: [2],
        explanation: 'RUN kör kommandon under image-byggprocessen.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-28',
        question: 'To copy files into image, use...',
        options: ['ADD always', 'MOVE', 'COPY', 'PUT'],
        correctIndices: [2],
        explanation: 'COPY kopierar filer från host till image.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-29',
        question: 'To set start command, use...',
        options: ['RUN', 'START', 'CMD', 'EXEC'],
        correctIndices: [2],
        explanation: 'CMD anger standardkommandot som körs när containern startar.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-30',
        question: 'The ENTRYPOINT instruction...',
        options: ['Same as CMD', 'Cannot be easily overridden', 'Is deprecated', 'Runs at build time'],
        correctIndices: [1],
        explanation: 'ENTRYPOINT kan inte enkelt överskrivas vid container start.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-31',
        question: 'The WORKDIR instruction sets...',
        options: ['Build directory', 'Host directory', 'Container working directory', 'Volume directory'],
        correctIndices: [2],
        explanation: 'WORKDIR sätter arbetskatalogen i containern.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-32',
        question: 'The EXPOSE instruction...',
        options: ['Opens port immediately', 'Documents port (doesn\'t open)', 'Exposes to internet', 'Is required for ports'],
        correctIndices: [1],
        explanation: 'EXPOSE dokumenterar vilka portar som används men öppnar dem inte.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-33',
        question: 'The ENV instruction sets...',
        options: ['Build variables', 'Environment variables', 'External variables', 'Entry variables'],
        correctIndices: [1],
        explanation: 'ENV sätter miljövariabler i containern.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-34',
        question: 'Select valid Dockerfile instructions (choose 5):',
        options: ['FROM', 'BASE', 'RUN', 'EXEC', 'COPY', 'MOVE', 'CMD', 'COMMAND', 'WORKDIR', 'DIRECTORY'],
        correctIndices: [0, 2, 4, 6, 8],
        explanation: 'Giltiga Dockerfile-instruktioner: FROM, RUN, COPY, CMD, WORKDIR.',
        difficulty: 'VG',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-35',
        question: 'Bind volume syntax is...',
        options: ['-v name:/path', '-v /host/path:/container/path', '-v volume:/path', '--volume name'],
        correctIndices: [1],
        explanation: 'Bind mount syntax: -v /host/path:/container/path',
        difficulty: 'G',
        category: 'Docker Volumes',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-36',
        question: 'Named volume syntax is...',
        options: ['-v /path:/path', '-v name:/container/path', '--named name:/path', '-volume name'],
        correctIndices: [1],
        explanation: 'Named volume syntax: -v name:/container/path',
        difficulty: 'G',
        category: 'Docker Volumes',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-37',
        question: 'Named volumes are stored in...',
        options: ['/var/docker/', '/var/lib/docker/volumes/', '/docker/volumes/', '/home/docker/'],
        correctIndices: [1],
        explanation: 'Named volumes lagras i /var/lib/docker/volumes/',
        difficulty: 'G',
        category: 'Docker Volumes',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-38',
        question: 'To create a network, use...',
        options: ['docker net create', 'docker new network', 'docker network create', 'docker create network'],
        correctIndices: [2],
        explanation: 'docker network create skapar ett nytt nätverk.',
        difficulty: 'G',
        category: 'Docker Nätverk',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-39',
        question: 'To list networks, use...',
        options: ['docker network show', 'docker networks', 'docker network ls', 'docker net list'],
        correctIndices: [2],
        explanation: 'docker network ls listar alla nätverk.',
        difficulty: 'G',
        category: 'Docker Nätverk',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-40',
        question: 'Default network type is...',
        options: ['host', 'none', 'bridge', 'overlay'],
        correctIndices: [2],
        explanation: 'Bridge är standardnätverkstypen i Docker.',
        difficulty: 'G',
        category: 'Docker Nätverk',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-41',
        question: 'To inspect container details, use...',
        options: ['docker details', 'docker info', 'docker inspect', 'docker show'],
        correctIndices: [2],
        explanation: 'docker inspect visar detaljerad information om en container.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-42',
        question: 'To see resource usage, use...',
        options: ['docker usage', 'docker resources', 'docker stats', 'docker monitor'],
        correctIndices: [2],
        explanation: 'docker stats visar resursutnyttjande i realtid.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-43',
        question: 'docker-compose file is named...',
        options: ['compose.yml', 'docker.yml', 'docker-compose.yml', 'container.yml'],
        correctIndices: [2],
        explanation: 'Standard docker-compose filen heter docker-compose.yml',
        difficulty: 'G',
        category: 'Docker Compose',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-44',
        question: 'To start compose services, use...',
        options: ['docker-compose start', 'docker-compose run', 'docker-compose up', 'docker-compose begin'],
        correctIndices: [2],
        explanation: 'docker-compose up startar alla definierade tjänster.',
        difficulty: 'G',
        category: 'Docker Compose',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-45',
        question: 'To stop compose services, use...',
        options: ['docker-compose stop', 'docker-compose end', 'docker-compose down', 'docker-compose halt'],
        correctIndices: [2],
        explanation: 'docker-compose down stoppar och tar bort tjänster och nätverk.',
        difficulty: 'G',
        category: 'Docker Compose',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-46',
        question: 'docker-compose up -d runs...',
        options: ['In debug mode', 'In detached mode', 'With defaults', 'In daemon mode'],
        correctIndices: [1],
        explanation: '-d flaggan kör docker-compose i detached (bakgrunds) läge.',
        difficulty: 'G',
        category: 'Docker Compose',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-47',
        question: 'To follow compose logs, use...',
        options: ['docker-compose log', 'docker-compose output', 'docker-compose logs -f', 'docker-compose show'],
        correctIndices: [2],
        explanation: 'docker-compose logs -f följer loggarna i realtid.',
        difficulty: 'G',
        category: 'Docker Compose',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-48',
        question: 'In compose, services communicate via...',
        options: ['IP addresses only', 'Service names as hostnames', 'Port numbers only', 'External DNS'],
        correctIndices: [1],
        explanation: 'I docker-compose kan tjänster kommunicera via sina tjänstnamn som hostnames.',
        difficulty: 'G',
        category: 'Docker Compose',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-49',
        question: 'To rebuild compose images, use...',
        options: ['docker-compose rebuild', 'docker-compose build', 'docker-compose make', 'docker-compose create'],
        correctIndices: [1],
        explanation: 'docker-compose build bygger om images.',
        difficulty: 'G',
        category: 'Docker Compose',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-50',
        question: 'Select valid docker-compose commands (choose 4):',
        options: ['up', 'start', 'down', 'stop', 'build', 'make', 'logs', 'output', 'create', 'run'],
        correctIndices: [0, 2, 4, 6],
        explanation: 'Giltiga docker-compose kommandon: up, down, build, logs.',
        difficulty: 'VG',
        category: 'Docker Compose',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-51',
        question: 'To enter running container with bash...',
        options: ['docker bash container', 'docker shell container', 'docker exec -it container bash', 'docker run -it container bash'],
        correctIndices: [2],
        explanation: 'docker exec -it container bash öppnar en bash-session i en körande container.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-52',
        question: 'docker run vs docker exec...',
        options: ['Same thing', 'run creates new, exec enters existing', 'exec creates new, run enters existing', 'Both create new'],
        correctIndices: [1],
        explanation: 'docker run skapar ny container, docker exec kör kommando i befintlig.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-53',
        question: 'To copy file to container, use...',
        options: ['docker copy', 'docker transfer', 'docker cp', 'docker mv'],
        correctIndices: [2],
        explanation: 'docker cp kopierar filer till/från containers.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-54',
        question: 'docker cp syntax is...',
        options: ['docker cp container:file host', 'docker cp file container:path', 'docker cp -c file container', 'docker cp file -to container'],
        correctIndices: [1],
        explanation: 'docker cp file container:path kopierar fil till container.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-55',
        question: 'To tag an image, use...',
        options: ['docker label', 'docker name', 'docker tag', 'docker mark'],
        correctIndices: [2],
        explanation: 'docker tag taggar en image med ett nytt namn/tag.',
        difficulty: 'G',
        category: 'Docker Images',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-56',
        question: 'Image tag format is...',
        options: ['image/tag', 'image@tag', 'image:tag', 'image-tag'],
        correctIndices: [2],
        explanation: 'Image-tag formatet är image:tag',
        difficulty: 'G',
        category: 'Docker Images',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-57',
        question: 'Default tag is...',
        options: ['default', 'current', 'latest', 'main'],
        correctIndices: [2],
        explanation: 'Standardtaggen är "latest" om ingen annan anges.',
        difficulty: 'G',
        category: 'Docker Images',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-58',
        question: 'To build with tag, use...',
        options: ['docker build --name image', 'docker build -n image', 'docker build -t image .', 'docker build --tag=image'],
        correctIndices: [2],
        explanation: 'docker build -t image . bygger och taggar en image.',
        difficulty: 'G',
        category: 'Docker Build',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-59',
        question: 'The dot in docker build . means...',
        options: ['Current image', 'Build context (current directory)', 'Hidden files', 'Default config'],
        correctIndices: [1],
        explanation: 'Punkten anger build context, dvs. aktuell katalog.',
        difficulty: 'G',
        category: 'Docker Build',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-60',
        question: '.dockerignore excludes files from...',
        options: ['Container', 'Build context', 'Image', 'Volume'],
        correctIndices: [1],
        explanation: '.dockerignore exkluderar filer från build context.',
        difficulty: 'G',
        category: 'Docker Build',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-61',
        question: 'Select all valid flags for docker run (choose 5):',
        options: ['-d', '-b', '-p', '-port', '-v', '-vol', '-e', '-env', '--name', '-n'],
        correctIndices: [0, 2, 4, 6, 8],
        explanation: 'Giltiga flaggor för docker run: -d, -p, -v, -e, --name.',
        difficulty: 'VG',
        category: 'Docker Flaggor',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-62',
        question: 'The -e flag sets...',
        options: ['Entry point', 'Environment variable', 'Execute command', 'External port'],
        correctIndices: [1],
        explanation: '-e flaggan sätter miljövariabler i containern.',
        difficulty: 'G',
        category: 'Docker Flaggor',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-63',
        question: 'To limit memory, use...',
        options: ['--memory-limit', '-m or --memory', '--ram', '--mem-max'],
        correctIndices: [1],
        explanation: '-m eller --memory begränsar containerminne.',
        difficulty: 'G',
        category: 'Docker Resurser',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-64',
        question: 'To limit CPU, use...',
        options: ['--cpu-limit', '--processor', '--cpus', '--cpu-max'],
        correctIndices: [2],
        explanation: '--cpus begränsar CPU-användning för containern.',
        difficulty: 'G',
        category: 'Docker Resurser',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-65',
        question: '--restart always means...',
        options: ['Restart on error', 'Always restart container', 'Restart once', 'Never restart'],
        correctIndices: [1],
        explanation: '--restart always startar alltid om containern automatiskt.',
        difficulty: 'G',
        category: 'Docker Flaggor',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-66',
        question: 'Container layers are...',
        options: ['Writable', 'Read-only', 'Shared', 'Encrypted'],
        correctIndices: [1],
        explanation: 'Image-lager är skrivskyddade (read-only).',
        difficulty: 'G',
        category: 'Docker Arkitektur',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-67',
        question: 'Container top layer is...',
        options: ['Read-only', 'Writable', 'Shared', 'Cached'],
        correctIndices: [1],
        explanation: 'Containerns översta lager är skrivbart.',
        difficulty: 'G',
        category: 'Docker Arkitektur',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-68',
        question: 'Multi-stage build is for...',
        options: ['Multiple containers', 'Smaller final images', 'Parallel builds', 'Multiple platforms'],
        correctIndices: [1],
        explanation: 'Multi-stage builds ger mindre slutgiltiga images.',
        difficulty: 'VG',
        category: 'Docker Build',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-69',
        question: 'In multi-stage, COPY --from=...',
        options: ['Copies from host', 'Copies from earlier stage', 'Copies from volume', 'Copies from URL'],
        correctIndices: [1],
        explanation: 'COPY --from= kopierar från en tidigare build-stage.',
        difficulty: 'VG',
        category: 'Docker Build',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-70',
        question: 'Alpine image is known for...',
        options: ['Speed', 'Small size', 'Security', 'Compatibility'],
        correctIndices: [1],
        explanation: 'Alpine-images är kända för sin lilla storlek.',
        difficulty: 'G',
        category: 'Docker Images',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-71',
        question: 'Select container runtimes (choose 3):',
        options: ['containerd', 'dockerd', 'runc', 'dockerc', 'cri-o', 'docker-runtime', 'buildah', 'podman', 'skopeo', 'kaniko'],
        correctIndices: [0, 2, 4],
        explanation: 'Container runtimes: containerd, runc, cri-o.',
        difficulty: 'VG',
        category: 'Docker Arkitektur',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-72',
        question: 'Docker daemon is called...',
        options: ['docker', 'dockerd', 'docker-daemon', 'containerd'],
        correctIndices: [1],
        explanation: 'Docker-daemonen heter dockerd.',
        difficulty: 'G',
        category: 'Docker Arkitektur',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-73',
        question: 'Docker socket is at...',
        options: ['/var/docker/socket', '/var/run/docker.sock', '/etc/docker/socket', '/run/docker/sock'],
        correctIndices: [1],
        explanation: 'Docker socket finns på /var/run/docker.sock',
        difficulty: 'G',
        category: 'Docker Arkitektur',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-74',
        question: 'To prune unused images, use...',
        options: ['docker image clean', 'docker image remove', 'docker image prune', 'docker image delete'],
        correctIndices: [2],
        explanation: 'docker image prune tar bort oanvända images.',
        difficulty: 'G',
        category: 'Docker Städning',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-75',
        question: 'To prune everything unused, use...',
        options: ['docker clean all', 'docker remove unused', 'docker system prune', 'docker prune all'],
        correctIndices: [2],
        explanation: 'docker system prune rensar alla oanvända resurser.',
        difficulty: 'G',
        category: 'Docker Städning',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-76',
        question: 'To see disk usage by Docker, use...',
        options: ['docker disk', 'docker usage', 'docker system df', 'docker space'],
        correctIndices: [2],
        explanation: 'docker system df visar diskanvändning.',
        difficulty: 'G',
        category: 'Docker Städning',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-77',
        question: 'Dockerfile best practice: fewer layers means...',
        options: ['Slower build', 'Larger image', 'Smaller image', 'No difference'],
        correctIndices: [2],
        explanation: 'Färre lager ger mindre images.',
        difficulty: 'G',
        category: 'Dockerfile Best Practice',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-78',
        question: 'Combine RUN commands with...',
        options: [';', '+', '&&', '||'],
        correctIndices: [2],
        explanation: 'Kombinera RUN-kommandon med && för att minska lager.',
        difficulty: 'G',
        category: 'Dockerfile Best Practice',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-79',
        question: 'HEALTHCHECK instruction...',
        options: ['Checks host health', 'Monitors container health', 'Checks network', 'Is deprecated'],
        correctIndices: [1],
        explanation: 'HEALTHCHECK övervakar containerns hälsa.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-80',
        question: 'USER instruction sets...',
        options: ['Host user', 'Container user', 'Build user', 'Registry user'],
        correctIndices: [1],
        explanation: 'USER anger vilken användare containern kör som.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-81',
        question: 'Select valid health check options (choose 3):',
        options: ['--interval', '--delay', '--timeout', '--wait', '--retries', '--attempts', '--count', '--check', '--period', '--frequency'],
        correctIndices: [0, 2, 4],
        explanation: 'Giltiga healthcheck-alternativ: --interval, --timeout, --retries.',
        difficulty: 'VG',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-82',
        question: 'ARG vs ENV difference...',
        options: ['Same thing', 'ARG is build-time only', 'ENV is build-time only', 'Both are runtime'],
        correctIndices: [1],
        explanation: 'ARG är bara tillgänglig under build, ENV finns i runtime.',
        difficulty: 'VG',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-83',
        question: 'To pass build argument, use...',
        options: ['docker build -e', 'docker build --env', 'docker build --build-arg', 'docker build -a'],
        correctIndices: [2],
        explanation: 'docker build --build-arg skickar build-argument.',
        difficulty: 'G',
        category: 'Docker Build',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-84',
        question: 'LABEL instruction adds...',
        options: ['Version info', 'Metadata', 'Tags', 'Comments'],
        correctIndices: [1],
        explanation: 'LABEL lägger till metadata till imagen.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-85',
        question: 'ADD vs COPY difference...',
        options: ['Same thing', 'COPY can extract tar', 'ADD can extract tar and fetch URLs', 'ADD is deprecated'],
        correctIndices: [2],
        explanation: 'ADD kan extrahera tar-filer och hämta från URL, COPY är enklare.',
        difficulty: 'VG',
        category: 'Dockerfile',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-86',
        question: 'Best practice: prefer...',
        options: ['ADD always', 'COPY over ADD', 'Neither', 'Both equally'],
        correctIndices: [1],
        explanation: 'Best practice är att föredra COPY framför ADD.',
        difficulty: 'G',
        category: 'Dockerfile Best Practice',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-87',
        question: 'To see image history, use...',
        options: ['docker image log', 'docker image layers', 'docker history', 'docker image history'],
        correctIndices: [2],
        explanation: 'docker history visar image-historik.',
        difficulty: 'G',
        category: 'Docker Images',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-88',
        question: 'Dangling images are...',
        options: ['Corrupt images', 'Untagged images', 'Old images', 'Large images'],
        correctIndices: [1],
        explanation: 'Dangling images är otaggade images utan referens.',
        difficulty: 'G',
        category: 'Docker Images',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-89',
        question: 'To list dangling images, use...',
        options: ['docker images -d', 'docker images -f dangling=true', 'docker images --dangling', 'docker images untagged'],
        correctIndices: [1],
        explanation: 'docker images -f dangling=true listar dangling images.',
        difficulty: 'G',
        category: 'Docker Images',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-90',
        question: 'To stop all containers, use...',
        options: ['docker stop --all', 'docker stop -a', 'docker stop $(docker ps -q)', 'docker stopall'],
        correctIndices: [2],
        explanation: 'docker stop $(docker ps -q) stoppar alla körande containers.',
        difficulty: 'VG',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-91',
        question: 'Select valid network types (choose 4):',
        options: ['bridge', 'internal', 'host', 'external', 'none', 'isolated', 'overlay', 'underlay', 'private', 'public'],
        correctIndices: [0, 2, 4, 6],
        explanation: 'Giltiga nätverkstyper: bridge, host, none, overlay.',
        difficulty: 'VG',
        category: 'Docker Nätverk',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-92',
        question: 'host network mode means...',
        options: ['Container has no network', 'Container shares host network', 'Container is host', 'Host joins container'],
        correctIndices: [1],
        explanation: 'Host-nätverksläge delar hostens nätverksstack med containern.',
        difficulty: 'G',
        category: 'Docker Nätverk',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-93',
        question: 'none network mode means...',
        options: ['Default network', 'Bridge network', 'No network', 'Overlay network'],
        correctIndices: [2],
        explanation: 'None-läge ger containern inget nätverk.',
        difficulty: 'G',
        category: 'Docker Nätverk',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-94',
        question: 'overlay network is for...',
        options: ['Single host', 'Multi-host (Swarm)', 'Local only', 'Testing'],
        correctIndices: [1],
        explanation: 'Overlay-nätverk används för multi-host/Swarm-miljöer.',
        difficulty: 'VG',
        category: 'Docker Nätverk',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-95',
        question: 'To attach to container output, use...',
        options: ['docker connect', 'docker follow', 'docker attach', 'docker join'],
        correctIndices: [2],
        explanation: 'docker attach kopplar till en containers output.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-96',
        question: 'Ctrl+P Ctrl+Q in attached container...',
        options: ['Stops container', 'Detaches without stopping', 'Restarts container', 'Kills container'],
        correctIndices: [1],
        explanation: 'Ctrl+P Ctrl+Q kopplar loss utan att stoppa containern.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-97',
        question: 'docker diff shows...',
        options: ['Image differences', 'Changed files in container', 'Config differences', 'Version differences'],
        correctIndices: [1],
        explanation: 'docker diff visar ändrade filer i containern.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-98',
        question: 'docker commit creates...',
        options: ['New container', 'New image from container', 'Backup', 'Snapshot'],
        correctIndices: [1],
        explanation: 'docker commit skapar en ny image från en container.',
        difficulty: 'G',
        category: 'Docker Images',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-99',
        question: 'docker save exports...',
        options: ['Container', 'Image to tar', 'Volume', 'Network'],
        correctIndices: [1],
        explanation: 'docker save exporterar en image till tar-fil.',
        difficulty: 'G',
        category: 'Docker Images',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-100',
        question: 'docker load imports...',
        options: ['Container', 'Image from tar', 'Volume', 'Network'],
        correctIndices: [1],
        explanation: 'docker load importerar en image från tar-fil.',
        difficulty: 'G',
        category: 'Docker Images',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-101',
        question: 'docker export exports...',
        options: ['Image', 'Container filesystem to tar', 'Volume', 'Network'],
        correctIndices: [1],
        explanation: 'docker export exporterar containerns filsystem till tar.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-102',
        question: 'docker import imports...',
        options: ['Image tar', 'Filesystem tar as image', 'Container', 'Volume'],
        correctIndices: [1],
        explanation: 'docker import importerar filsystem-tar som image.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-103',
        question: 'To pause container, use...',
        options: ['docker stop', 'docker halt', 'docker pause', 'docker freeze'],
        correctIndices: [2],
        explanation: 'docker pause pausar en container.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-104',
        question: 'To unpause container, use...',
        options: ['docker start', 'docker continue', 'docker unpause', 'docker resume'],
        correctIndices: [2],
        explanation: 'docker unpause återupptar en pausad container.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-105',
        question: 'docker top shows...',
        options: ['Top images', 'Processes in container', 'Top containers', 'Resource usage'],
        correctIndices: [1],
        explanation: 'docker top visar processer som körs i containern.',
        difficulty: 'G',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-106',
        question: 'Select valid docker info commands (choose 4):',
        options: ['docker info', 'docker status', 'docker version', 'docker about', 'docker inspect', 'docker details', 'docker stats', 'docker monitor', 'docker show', 'docker list'],
        correctIndices: [0, 2, 4, 6],
        explanation: 'Giltiga info-kommandon: docker info, docker version, docker inspect, docker stats.',
        difficulty: 'VG',
        category: 'Docker Kommandon',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-107',
        question: 'To login to registry, use...',
        options: ['docker auth', 'docker connect', 'docker login', 'docker signin'],
        correctIndices: [2],
        explanation: 'docker login loggar in på ett registry.',
        difficulty: 'G',
        category: 'Docker Registry',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-108',
        question: 'To logout from registry, use...',
        options: ['docker signout', 'docker disconnect', 'docker logout', 'docker exit'],
        correctIndices: [2],
        explanation: 'docker logout loggar ut från ett registry.',
        difficulty: 'G',
        category: 'Docker Registry',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-109',
        question: 'Docker Hub is...',
        options: ['Local registry', 'Public registry', 'Private only', 'Enterprise only'],
        correctIndices: [1],
        explanation: 'Docker Hub är ett publikt registry för Docker images.',
        difficulty: 'G',
        category: 'Docker Registry',
        topic: 'docker-containers'
    },
    {
        id: 'omtenta-v2-docker-110',
        question: 'To search Docker Hub, use...',
        options: ['docker find', 'docker lookup', 'docker search', 'docker query'],
        correctIndices: [2],
        explanation: 'docker search söker efter images på Docker Hub.',
        difficulty: 'G',
        category: 'Docker Registry',
        topic: 'docker-containers'
    }
]
