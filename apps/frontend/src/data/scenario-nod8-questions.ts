/**
 * NOD 8: Docker Isolering & Images - SCENARIO Questions
 * 20 verklighetstrogna scenariofrågor
 */

import type { Omtenta2Question } from './omtenta-2.0-quiz'

export const SCENARIO_NOD8_QUESTIONS: Omtenta2Question[] = [
    {
        id: 'nod8-s1',
        question: 'Din kollega frågar: "Är Docker samma sak som en virtuell maskin?". Vad svarar du?',
        options: ['Ja, det är samma teknik', 'Nej, en container är en isolerad process - inte en hel VM', 'Ja, men Docker är snabbare', 'Nej, Docker använder bara nätverk'],
        correctIndices: [1],
        explanation: 'Containers delar värd-kernel och är isolerade processer. VM har egen kernel och hårdvaruemulering.',
        difficulty: 'G',
        category: 'Koncept',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s2',
        question: 'Du vill starta en nginx-container i bakgrunden. Kommando?',
        options: ['docker start nginx', 'docker run nginx', 'docker run -d nginx', 'docker exec nginx'],
        correctIndices: [2],
        explanation: 'docker run -d (detached) startar i bakgrunden. Utan -d blockerar terminalen.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s3',
        question: 'Du har en körande container och vill köra bash inuti den för debugging. Kommando?',
        options: ['docker ssh container bash', 'docker exec -it container bash', 'docker attach container bash', 'docker connect container bash'],
        correctIndices: [1],
        explanation: 'docker exec -it kör kommando i körande container. -i=interactive, -t=tty (terminal).',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s4',
        question: 'Du vill se loggar från en container som crashade. Kommando?',
        options: ['docker log container', 'docker logs container', 'docker output container', 'docker cat container'],
        correctIndices: [1],
        explanation: 'docker logs visar stdout/stderr från containern. -f för att följa i realtid (som tail -f).',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s5',
        question: 'Du vill bygga en Docker image från din Dockerfile. Kommando?',
        options: ['docker create .', 'docker build .', 'docker make .', 'docker compile .'],
        correctIndices: [1],
        explanation: 'docker build . bygger image från Dockerfile i current directory. -t name:tag för att tagga.',
        difficulty: 'G',
        category: 'Build',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s6',
        question: 'I Dockerfile, vilken instruktion kopierar filer från host till image?',
        options: ['ADD', 'COPY', 'TRANSFER', 'Både ADD och COPY (med skillnader)'],
        correctIndices: [3],
        explanation: 'COPY kopierar lokala filer. ADD kan också extrahera tar och hämta från URL. COPY föredras för enkelhet.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s7',
        question: 'Du vill att containern automatiskt tas bort när den stoppar. Run-flagga?',
        options: ['docker run --delete nginx', 'docker run --rm nginx', 'docker run --cleanup nginx', 'docker run --auto-remove nginx'],
        correctIndices: [1],
        explanation: '--rm tar bort containern automatiskt vid exit. Bra för engångs-körningar och tester.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s8',
        question: 'Vad är skillnaden mellan CMD och ENTRYPOINT i Dockerfile?',
        options: ['Samma sak', 'CMD kan överskrivas från CLI, ENTRYPOINT är mer permanent', 'ENTRYPOINT kör före CMD', 'CMD är deprecated'],
        correctIndices: [1],
        explanation: 'ENTRYPOINT sätter "basen" som är svårare att ändra. CMD ger default-args som enkelt överskrids.',
        difficulty: 'VG',
        category: 'Dockerfile',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s9',
        question: 'Du ser en Dockerfile med "FROM python:3.11-slim". Vad är "slim"?',
        options: ['En version av Python', 'En mindre base-image utan onödiga paket', 'Slim mode som komprimerar', 'En nätverksprofil'],
        correctIndices: [1],
        explanation: 'slim-varianter har minimalt installerat. Mindre image = snabbare pulls. Alpine är ännu mindre.',
        difficulty: 'G',
        category: 'Images',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s10',
        question: 'Du vill lista alla körande containers. Kommando?',
        options: ['docker ps', 'docker list', 'docker containers', 'docker running'],
        correctIndices: [0],
        explanation: 'docker ps visar körande. docker ps -a visar alla (även stoppade). ps = process status.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s11',
        question: 'Du bygger en image och vill minska layer-storlek. Vilken best practice för RUN?',
        options: ['En RUN per kommando', 'Kombinera kommandon med && i samma RUN', 'Använd EXEC istället för RUN', 'Layers påverkar inte storlek'],
        correctIndices: [1],
        explanation: 'Varje RUN skapar layer. Kombinera apt update && apt install && rm cache i samma RUN för mindre image.',
        difficulty: 'VG',
        category: 'Dockerfile',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s12',
        question: 'Du vill pusha din image till Docker Hub. Första steget?',
        options: ['docker push image', 'docker upload image', 'docker login', 'docker connect hub'],
        correctIndices: [2],
        explanation: 'docker login autentiserar mot registry. Sen docker push username/image:tag.',
        difficulty: 'G',
        category: 'Registry',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s13',
        question: 'En container har process ID 1 (PID 1). Vad är speciellt med PID 1?',
        options: ['Inget speciellt', 'PID 1 får signaler direkt och måste hantera dem rätt', 'PID 1 har mer minne', 'PID 1 är alltid root'],
        correctIndices: [1],
        explanation: 'PID 1 är init-process. Får SIGTERM vid docker stop. Om den inte hanterar signaler kan stop ta lång tid.',
        difficulty: 'VG',
        category: 'Koncept',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s14',
        question: 'Du vill se vilka images du har lokalt. Kommando?',
        options: ['docker images', 'docker image ls', 'docker list images', 'Både A och B fungerar'],
        correctIndices: [3],
        explanation: 'docker images och docker image ls är synonymer. Visar lokala images med size och tag.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s15',
        question: 'Du har gamla images som tar diskutrymme. Kommando för att städa bort oanvända?',
        options: ['docker clean', 'docker image prune', 'docker rm images', 'docker delete unused'],
        correctIndices: [1],
        explanation: 'docker image prune tar bort dangling images. docker system prune städar allt (containers, images, networks).',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s16',
        question: 'Du vill sätta en miljövariabel i containern. Run-flagga?',
        options: ['docker run -e VAR=value', 'docker run --env VAR=value', 'docker run -v VAR=value', 'Både A och B fungerar'],
        correctIndices: [3],
        explanation: '-e och --env är samma. Kan användas flera gånger. Eller --env-file för många variabler.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s17',
        question: 'I Dockerfile, var sparas filer som COPY kopierar till om du skriver "COPY . /app"?',
        options: ['I host-systemet under /app', 'I imagen under /app', 'I en temporär mapp', 'COPY fungerar inte så'],
        correctIndices: [1],
        explanation: 'COPY kopierar IN i imagen. Filerna bäddas in och finns sedan i varje container som startas från imagen.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s18',
        question: 'Du vill namnge din container "web" när du startar den. Flagga?',
        options: ['docker run -n web nginx', 'docker run --name web nginx', 'docker run --label web nginx', 'docker run -id web nginx'],
        correctIndices: [1],
        explanation: '--name sätter containernamn. Utan namn får containern ett slumpmässigt namn som "happy_einstein".',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s19',
        question: 'Vad gör instruktionen WORKDIR /app i en Dockerfile?',
        options: ['Sätter host-katalog', 'Sätter working directory inuti imagen', 'Monterar /app som volume', 'Skapar /app på host'],
        correctIndices: [1],
        explanation: 'WORKDIR sätter pwd för följande RUN, CMD, COPY etc. Skapas om den inte finns.',
        difficulty: 'G',
        category: 'Dockerfile',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    },
    {
        id: 'nod8-s20',
        question: 'Du vill stoppa en körande container "web". Kommando?',
        options: ['docker kill web', 'docker stop web', 'docker terminate web', 'Både A och B (men stop är snällare)'],
        correctIndices: [3],
        explanation: 'stop skickar SIGTERM, väntar 10s, sen SIGKILL. kill skickar SIGKILL direkt. stop föredras normalt.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod8-docker-isolering',
        type: 'scenario'
    }
]
