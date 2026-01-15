/**
 * NOD 10: Docker Compose & IaC - SCENARIO Questions
 * 20 verklighetstrogna scenariofrågor
 */

import type { Omtenta2Question } from './omtenta-2.0-quiz'

export const SCENARIO_NOD10_QUESTIONS: Omtenta2Question[] = [
    {
        id: 'nod10-s1',
        question: 'Du har en docker-compose.yml och vill starta alla tjänster i bakgrunden. Kommando?',
        options: ['docker-compose start', 'docker-compose up', 'docker-compose up -d', 'docker-compose run'],
        correctIndices: [2],
        explanation: 'docker-compose up -d startar alla services detached. Utan -d ser du alla loggar i terminalen.',
        difficulty: 'G',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s2',
        question: 'Du vill stoppa och ta bort alla containers, nätverk, och volumes från compose. Kommando?',
        options: ['docker-compose stop', 'docker-compose down', 'docker-compose down -v', 'docker-compose rm --all'],
        correctIndices: [2],
        explanation: 'down stoppar och tar bort containers och nätverk. -v tar även bort volumes. stop bara stoppar.',
        difficulty: 'G',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s3',
        question: 'I docker-compose.yml, hur definierar du att "web" behöver "db" innan start?',
        options: ['needs: db', 'depends_on: [db]', 'requires: db', 'after: db'],
        correctIndices: [1],
        explanation: 'depends_on säger startordning. OBS: väntar inte på att db är "ready", bara startad!',
        difficulty: 'G',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s4',
        question: 'Du vill se loggar från alla compose services samtidigt. Kommando?',
        options: ['docker-compose logs', 'docker-compose log -all', 'docker-compose output', 'docker-compose show-logs'],
        correctIndices: [0],
        explanation: 'docker-compose logs visar alla services. -f för att följa. logs web db för specifika.',
        difficulty: 'G',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s5',
        question: 'Vad är fördelen med Infrastructure as Code (IaC) som docker-compose?',
        options: ['Snabbare containers', 'Versionshantering, reproducerbarhet, dokumentation i kod', 'Mindre diskutrymme', 'Bättre säkerhet automatiskt'],
        correctIndices: [1],
        explanation: 'IaC = infra definierad i filer. Kan versionshanteras (git), reproduceras, granskas, och delas.',
        difficulty: 'G',
        category: 'IaC',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s6',
        question: 'Du har ändrat Dockerfile och vill bygga om images med compose. Kommando?',
        options: ['docker-compose up', 'docker-compose build', 'docker-compose up --build', 'Både B och C'],
        correctIndices: [3],
        explanation: 'build bygger bara. up --build bygger och startar. Utan --build använder compose cached images.',
        difficulty: 'G',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s7',
        question: 'Du vill skala upp web-service till 3 instanser med compose. Kommando?',
        options: ['docker-compose scale web=3', 'docker-compose up --scale web=3', 'docker-compose replicas web 3', 'Båda A och B (A är deprecated)'],
        correctIndices: [3],
        explanation: 'scale är deprecated. Använd up --scale web=3. Compose v3 har också deploy.replicas i swarm.',
        difficulty: 'VG',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s8',
        question: 'I compose-fil, hur monterar du named volume "dbdata" till /var/lib/postgresql/data?',
        options: ['volumes: [dbdata:/var/lib/postgresql/data]', 'mount: dbdata:/var/lib/postgresql/data', 'volume_mount: dbdata=/var/lib/postgresql/data', 'data: dbdata:/var/lib/postgresql/data'],
        correctIndices: [0],
        explanation: 'volumes: under service. Named volumes deklareras även under top-level volumes: i filen.',
        difficulty: 'G',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s9',
        question: 'Du vill använda miljövariabler från .env fil i compose. Fungerar det automatiskt?',
        options: ['Nej, måste ange env_file', 'Ja, .env i samma katalog läses automatiskt', 'Måste sourca filen först', 'Endast med docker-compose v2'],
        correctIndices: [1],
        explanation: 'Compose läser .env automatiskt från samma katalog. ${VAR} i yaml ersätts med värden därifrån.',
        difficulty: 'G',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s10',
        question: 'Vad gör "restart: unless-stopped" i compose?',
        options: ['Startar om vid krasch, men inte efter manuell stop', 'Startar alltid om', 'Startar aldrig om', 'Startar om bara vid fel'],
        correctIndices: [0],
        explanation: 'unless-stopped = restart vid krasch/reboot, men inte om du kör docker stop. always restarter alltid.',
        difficulty: 'VG',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s11',
        question: 'Du vill köra ett engångskommando i web-servicen. Compose-kommando?',
        options: ['docker-compose exec web command', 'docker-compose run web command', 'Båda fungerar men har skillnader', 'docker-compose command web'],
        correctIndices: [2],
        explanation: 'exec kör i KÖRANDE container. run startar NY container för kommandot. Använd exec för debugging.',
        difficulty: 'VG',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s12',
        question: 'Hur definierar du custom nätverk i compose så services kan nå varandra via namn?',
        options: ['networks: under services och top-level', 'link: mellan services', 'dns: custom', 'Det funkar automatiskt i compose'],
        correctIndices: [3],
        explanation: 'Compose skapar automatiskt nätverk för projektet. Services kan nå varandra via servicenamn.',
        difficulty: 'G',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s13',
        question: 'Vilket format använder docker-compose.yml?',
        options: ['JSON', 'YAML', 'TOML', 'XML'],
        correctIndices: [1],
        explanation: 'YAML (YAML Aint Markup Language). Indentation-baserat, läsbart. OBS: känsligt för tabs vs spaces!',
        difficulty: 'G',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s14',
        question: 'Du vill validera din compose-fil utan att starta något. Kommando?',
        options: ['docker-compose check', 'docker-compose validate', 'docker-compose config', 'docker-compose --dry-run'],
        correctIndices: [2],
        explanation: 'docker-compose config validerar och visar merged config (inkl. env-variabler). Bra för debugging.',
        difficulty: 'VG',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s15',
        question: 'Du har compose v2 plugin istället för standalone. Hur kör du?',
        options: ['docker-compose up', 'docker compose up', 'Båda fungerar i v2', 'compose up'],
        correctIndices: [1],
        explanation: 'docker compose (utan bindestreck) är v2 plugin-syntax. Gamla docker-compose är standalone binary.',
        difficulty: 'G',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s16',
        question: 'Vad är skillnaden mellan "build: ." och "image: nginx" i compose?',
        options: ['Ingen skillnad', 'build bygger lokal Dockerfile, image drar från registry', 'build är snabbare', 'image stödjer inte volumes'],
        correctIndices: [1],
        explanation: 'build: anger Dockerfile-kontext för lokal build. image: drar färdig image från registry.',
        difficulty: 'G',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s17',
        question: 'Du vill att compose-projekt ska heta "myapp" istället för katalognamnet. Flagga?',
        options: ['docker-compose -n myapp up', 'docker-compose --name myapp up', 'docker-compose -p myapp up', 'docker-compose --project myapp up'],
        correctIndices: [2],
        explanation: '-p eller --project-name sätter projektnamn. Default är katalognamnet. Påverkar container-prefix.',
        difficulty: 'VG',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s18',
        question: 'Vilka är fördelarna med 3-2-1 backup-regeln? (3 kopior, 2 mediatyper, 1 offsite)',
        options: ['Bara för stora företag', 'Skyddar mot korrupt fil, mediafel, och katastrofer', 'Endast för databaser', 'För dyrt i praktiken'],
        correctIndices: [1],
        explanation: '3 kopior = korruptionsskydd. 2 media = skydd mot mediafel. 1 offsite = skydd mot brand/stöld.',
        difficulty: 'G',
        category: 'IaC/Backup',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s19',
        question: 'Du vill starta endast db-servicen utan dependencies. Flagga?',
        options: ['docker-compose up db', 'docker-compose up db --no-deps', 'docker-compose start db --only', 'docker-compose run db --single'],
        correctIndices: [1],
        explanation: '--no-deps startar endast angiven service utan att starta depends_on services.',
        difficulty: 'VG',
        category: 'Compose',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    },
    {
        id: 'nod10-s20',
        question: 'Vad betyder "idempotent" i IaC-sammanhang?',
        options: ['Snabb exekvering', 'Samma resultat oavsett hur många gånger du kör', 'Automatisk rollback', 'Parallell körning'],
        correctIndices: [1],
        explanation: 'Idempotent = samma utfall varje gång. docker-compose up ger samma resultat oavsett current state.',
        difficulty: 'VG',
        category: 'IaC',
        topic: 'nod10-docker-compose',
        type: 'scenario'
    }
]
