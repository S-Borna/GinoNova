"""
Docker Mastery - Study Data
===========================

90 Flashcards (30 easy, 30 medium, 30 hard)
60 Quiz Questions (20 easy, 20 medium, 20 hard)
"""

DOCKER_STUDY_DATA = {
    "module_slug": "docker-mastery",
    "module_title": "Docker Mastery",
    "module_description": "Container-teknologi och Docker för DevOps",
    "icon": "Box",

    # =========================================================================
    # FLASHCARDS - 90 st totalt (30 per svårighetsgrad)
    # =========================================================================
    "flashcards": {
        "easy": [
            {"front": "Vad är Docker?", "back": "En plattform för att bygga, köra och distribuera applikationer i containers - isolerade, portabla miljöer."},
            {"front": "Vad är skillnaden mellan container och VM?", "back": "Containers delar värdkärnan och är lättare. VM:s har egen kärna och tar mer resurser."},
            {"front": "Vad gör 'docker run hello-world'?", "back": "Laddar ner hello-world imagen (om den saknas) och kör den i en container."},
            {"front": "Vad är en Docker image?", "back": "En skrivskyddad mall som innehåller allt för att köra en applikation - kod, runtime, bibliotek."},
            {"front": "Vad är en Docker container?", "back": "En körande instans av en image. Du kan ha flera containers från samma image."},
            {"front": "Hur listar du körande containers?", "back": "docker ps - visar körande containers. docker ps -a visar alla inklusive stoppade."},
            {"front": "Hur stoppar du en container?", "back": "docker stop container_id - skickar SIGTERM för graceful shutdown."},
            {"front": "Hur tar du bort en container?", "back": "docker rm container_id - tar bort stoppad container. docker rm -f tvingar."},
            {"front": "Hur listar du alla images?", "back": "docker images eller docker image ls - visar alla nedladdade images."},
            {"front": "Hur tar du bort en image?", "back": "docker rmi image_id - tar bort imagen. Måste ta bort containers först."},
            {"front": "Vad gör flaggan -d i docker run?", "back": "Detached mode - kör containern i bakgrunden så terminalen frigjörs."},
            {"front": "Hur kommer du in i en körande container?", "back": "docker exec -it container_id bash - startar interaktiv shell i containern."},
            {"front": "Vad är Docker Hub?", "back": "Dockers officiella registry för att dela och hitta images. Som GitHub för containers."},
            {"front": "Hur laddar du ner en image?", "back": "docker pull imagename - laddar ner från Docker Hub. docker pull nginx:latest"},
            {"front": "Vad är en Dockerfile?", "back": "En textfil med instruktioner för att bygga en image. Definierar steg-för-steg hur imagen skapas."},
            {"front": "Hur bygger du en image från Dockerfile?", "back": "docker build -t imagename . - bygger image med tag från nuvarande katalog."},
            {"front": "Vad gör FROM i Dockerfile?", "back": "Anger basimage att bygga på. FROM ubuntu:22.04 använder Ubuntu som bas."},
            {"front": "Vad gör COPY i Dockerfile?", "back": "Kopierar filer från host till image. COPY app.py /app/ kopierar app.py."},
            {"front": "Vad gör RUN i Dockerfile?", "back": "Kör kommandon under byggprocessen. RUN apt-get update installerar paket."},
            {"front": "Vad gör CMD i Dockerfile?", "back": "Definierar standardkommando när containern startar. Kan överskrivas vid docker run."},
            {"front": "Hur mappar du portar?", "back": "docker run -p host:container - t.ex. -p 8080:80 mappar host 8080 till container 80."},
            {"front": "Hur sätter du miljövariabler?", "back": "docker run -e VAR=värde - t.ex. -e MYSQL_ROOT_PASSWORD=secret"},
            {"front": "Vad är docker-compose?", "back": "Verktyg för att definiera och köra multi-container applikationer med YAML-fil."},
            {"front": "Hur startar du docker-compose?", "back": "docker-compose up - startar alla tjänster. docker-compose up -d för bakgrund."},
            {"front": "Hur stoppar du docker-compose?", "back": "docker-compose down - stoppar och tar bort containers. --volumes tar bort volymer."},
            {"front": "Vad är en Docker volume?", "back": "Persistent lagring som överlever container-omstarter. Data sparas på host-systemet."},
            {"front": "Hur skapar du en namngiven volume?", "back": "docker volume create volymnamn eller -v volymnamn:/path i docker run."},
            {"front": "Vad gör --name flaggan?", "back": "Ger containern ett eget namn istället för slumpmässigt. docker run --name webserver nginx"},
            {"front": "Hur ser du container-loggar?", "back": "docker logs container_id - visar stdout/stderr. -f följer i realtid."},
            {"front": "Vad är Docker network?", "back": "Virtuellt nätverk där containers kan kommunicera. Default bridge, host, eller custom."},
        ],
        "medium": [
            {"front": "Vad är skillnaden mellan CMD och ENTRYPOINT?", "back": "ENTRYPOINT är kommandot som alltid körs. CMD är standardargument som kan överskrivas."},
            {"front": "Hur fungerar Docker layer caching?", "back": "Varje instruktion i Dockerfile skapar ett layer. Oförändrade layers cachas för snabbare builds."},
            {"front": "Vad är multi-stage builds?", "back": "Dockerfile med flera FROM-satser. Bygger i ett stage, kopierar artefakter till slut-stage för mindre images."},
            {"front": "Hur optimerar du Dockerfile för caching?", "back": "Sätt instruktioner som ändras sällan (apt-get) först, kod som ändras ofta (COPY . .) sist."},
            {"front": "Vad är Docker healthcheck?", "back": "HEALTHCHECK i Dockerfile testar om containern fungerar. Docker kan restart om hälsokontroll misslyckas."},
            {"front": "Hur begränsar du containers minne?", "back": "docker run -m 512m eller --memory=512m begränsar till 512 MB RAM."},
            {"front": "Hur begränsar du container CPU?", "back": "docker run --cpus=0.5 ger 50% av en CPU. --cpu-shares sätter relativ vikt."},
            {"front": "Vad är .dockerignore?", "back": "Som .gitignore - anger filer som inte ska kopieras in i imagen. Minskar build context."},
            {"front": "Vad gör EXPOSE i Dockerfile?", "back": "Dokumenterar vilka portar containern lyssnar på. Öppnar INTE portar automatiskt."},
            {"front": "Hur fungerar Docker volumes vs bind mounts?", "back": "Volumes hanteras av Docker i /var/lib/docker. Bind mounts mappar specifik host-path."},
            {"front": "Vad är docker network create?", "back": "Skapar ett custom nätverk. Containers i samma nätverk kan nå varandra via namn."},
            {"front": "Hur inspekterar du en container?", "back": "docker inspect container_id - visar all metadata, IP, mounts, config som JSON."},
            {"front": "Vad gör docker system prune?", "back": "Rensar oanvända containers, nätverk, images, och build cache. -a tar även oanvända images."},
            {"front": "Hur exporterar du en container?", "back": "docker export container > file.tar - exporterar filsystem. docker save för images."},
            {"front": "Vad är docker commit?", "back": "Skapar ny image från körande container. Bra för debugging, inte för produktion."},
            {"front": "Hur sätter du restart policy?", "back": "--restart=always/unless-stopped/on-failure. always startar om även efter host reboot."},
            {"front": "Vad är docker-compose networks?", "back": "docker-compose skapar default nätverk. Tjänster kan nå varandra via servicename."},
            {"front": "Hur skalar du tjänster i docker-compose?", "back": "docker-compose up --scale web=3 - startar 3 instanser av web-tjänsten."},
            {"front": "Vad är depends_on i docker-compose?", "back": "Definierar startordning. depends_on: db startar db innan denna tjänst."},
            {"front": "Hur uppdaterar du en körande stack?", "back": "docker-compose up -d --build - bygger om och startar om ändrade tjänster."},
            {"front": "Vad är ARG i Dockerfile?", "back": "Build-time variabler. ARG VERSION=1.0 kan överskrivas med --build-arg."},
            {"front": "Skillnaden mellan ARG och ENV?", "back": "ARG finns bara under build. ENV finns i körande container och kan ses med inspect."},
            {"front": "Hur kopierar du filer från container till host?", "back": "docker cp container:/path/fil ./lokal - kopierar ut filer från container."},
            {"front": "Vad gör docker stats?", "back": "Visar realtids CPU, minne, nätverk, disk I/O för körande containers."},
            {"front": "Hur begränsar du disk I/O?", "back": "--device-read-bps=/dev/sda:1mb --device-write-bps begränsar läs/skriv-hastighet."},
            {"front": "Vad är docker context?", "back": "Hanterar flera Docker endpoints. docker context create remote --docker host=ssh://server"},
            {"front": "Hur kör du container som specifik användare?", "back": "docker run --user 1000:1000 eller USER i Dockerfile. Undvik root."},
            {"front": "Vad gör --read-only?", "back": "Monterar container-filsystemet som skrivskyddat. Ökar säkerhet."},
            {"front": "Hur sätter du custom DNS?", "back": "docker run --dns 8.8.8.8 - använder Google DNS istället för host DNS."},
            {"front": "Vad är container orchestration?", "back": "Automatiserad hantering av container lifecycle - deployment, scaling, networking. Kubernetes, Swarm."},
        ],
        "hard": [
            {"front": "Hur fungerar Docker namespaces?", "back": "Isolerar processer, nätverk, mounts, användare. Varje container får egna namespaces från Linux kernel."},
            {"front": "Vad är cgroups roll i Docker?", "back": "Control groups begränsar och mäter resurser - CPU, minne, I/O. Isolering + resource limits."},
            {"front": "Hur säkrar du Docker daemon socket?", "back": "TLS-certifikat på /var/run/docker.sock. Undvik --privileged. Använd rootless Docker."},
            {"front": "Vad är Docker Content Trust (DCT)?", "back": "Signerar images kryptografiskt. DOCKER_CONTENT_TRUST=1 verifierar signaturer vid pull."},
            {"front": "Hur bygger du för multi-arkitektur?", "back": "docker buildx build --platform linux/amd64,linux/arm64 med manifest lists."},
            {"front": "Vad är Docker BuildKit?", "back": "Ny build-backend med parallella builds, bättre caching, mount secrets. DOCKER_BUILDKIT=1"},
            {"front": "Hur använder du build secrets?", "back": "RUN --mount=type=secret,id=mysecret med docker build --secret id=mysecret,src=file"},
            {"front": "Vad är Docker overlay network?", "back": "Multi-host nätverk i Swarm/K8s. VXLAN encapsulation för container-kommunikation över hosts."},
            {"front": "Hur fungerar Docker bridge networking?", "back": "Virtual bridge (docker0) med NAT. Containers får privata IPs, port mapping exponerar tjänster."},
            {"front": "Vad är Docker macvlan?", "back": "Ger containers egna MAC-adresser och IPs på fysiska nätverket. Som egna nätverkskort."},
            {"front": "Hur optimerar du image-storlek?", "back": "Multi-stage builds, minimal base (alpine/distroless), kombinera RUN, rensa cache i samma layer."},
            {"front": "Vad är distroless images?", "back": "Google-images utan shell eller pakethanterare. Endast applikation och runtime. Säkrare."},
            {"front": "Hur skannar du images för sårbarheter?", "back": "docker scan, Trivy, Clair, Snyk. Integreras i CI/CD för automatisk scanning."},
            {"front": "Vad är Docker Swarm mode?", "back": "Inbyggd orchestration. docker swarm init skapar kluster. Services, replicas, rolling updates."},
            {"front": "Hur fungerar Docker secrets i Swarm?", "back": "docker secret create skapar krypterad hemlighet. Monteras i /run/secrets/ i containers."},
            {"front": "Vad är Docker configs?", "back": "Som secrets men för icke-känslig config. Monteras som filer i containers."},
            {"front": "Hur fungerar rolling updates i Swarm?", "back": "--update-parallelism och --update-delay styr. Uppdaterar gradvis utan downtime."},
            {"front": "Vad är Docker init process?", "back": "--init kör tini/dumb-init som PID 1. Hanterar signals och zombie processes korrekt."},
            {"front": "Hur hanterar du PID 1 problemet?", "back": "Container PID 1 måste hantera signals. Använd --init, exec form i CMD, eller signal handlers."},
            {"front": "Vad är OCI (Open Container Initiative)?", "back": "Standard för container runtime och image format. Docker, containerd, CRI-O följer OCI."},
            {"front": "Hur fungerar containerd?", "back": "Container runtime som Docker använder under huven. Hanterar lifecycle, men utan build/CLI."},
            {"front": "Vad är Docker rootless mode?", "back": "Kör Docker daemon och containers utan root. Använder user namespaces. Säkrare."},
            {"front": "Hur begränsar du syscalls med seccomp?", "back": "docker run --security-opt seccomp=profile.json begränsar vilka kernel calls containers kan göra."},
            {"front": "Vad gör --cap-drop och --cap-add?", "back": "Tar bort/lägger till Linux capabilities. --cap-drop=ALL --cap-add=NET_BIND_SERVICE för minimal access."},
            {"front": "Hur fungerar Docker layer storage?", "back": "Union filesystem (overlay2) stackar layers. Copy-on-write för ändringar i container layer."},
            {"front": "Vad är Docker Registry garbage collection?", "back": "Rensar unreferenced blobs. registry garbage-collect config.yml på registry-servern."},
            {"front": "Hur sätter du upp privat registry med auth?", "back": "docker run registry med htpasswd-fil och TLS. Eller Harbor för enterprise features."},
            {"front": "Vad är image manifest?", "back": "JSON som beskriver image layers och config. Manifest list för multi-arch images."},
            {"front": "Hur debuggar du container networking?", "back": "docker run --net container:target nicolaka/netshoot - delar nätverk med target för debug."},
            {"front": "Vad är Docker Desktop alternatives?", "back": "Podman (daemonless), Rancher Desktop, Colima. Kör containers utan Docker daemon."},
        ],
    },

    # =========================================================================
    # QUIZ - 60 st totalt (20 per svårighetsgrad)
    # =========================================================================
    "quiz": {
        "easy": [
            {
                "question": "Vad är en Docker container?",
                "options": [
                    "En virtuell maskin",
                    "En körande instans av en image",
                    "En typ av databas",
                    "Ett operativsystem"
                ],
                "correct": 1,
                "explanation": "En container är en körande instans av en Docker image, isolerad från host-systemet."
            },
            {
                "question": "Hur listar du alla körande containers?",
                "options": ["docker list", "docker ps", "docker containers", "docker show"],
                "correct": 1,
                "explanation": "docker ps visar körande containers. docker ps -a visar alla inklusive stoppade."
            },
            {
                "question": "Vad gör 'docker pull nginx'?",
                "options": [
                    "Startar nginx container",
                    "Laddar ner nginx image",
                    "Tar bort nginx",
                    "Uppdaterar nginx"
                ],
                "correct": 1,
                "explanation": "docker pull laddar ner en image från Docker Hub till din lokala maskin."
            },
            {
                "question": "Hur stoppar du en container?",
                "options": ["docker kill", "docker stop", "docker end", "docker close"],
                "correct": 1,
                "explanation": "docker stop skickar SIGTERM för graceful shutdown. docker kill tvingar avslut."
            },
            {
                "question": "Vad är Docker Hub?",
                "options": [
                    "Dockers hemsida",
                    "En IDE för Docker",
                    "Registry för att dela images",
                    "Docker CLI"
                ],
                "correct": 2,
                "explanation": "Docker Hub är det officiella registret för att hitta, dela och lagra Docker images."
            },
            {
                "question": "Hur kör du en container i bakgrunden?",
                "options": [
                    "docker run --background",
                    "docker run -d",
                    "docker run &",
                    "docker run -b"
                ],
                "correct": 1,
                "explanation": "-d (detached) kör containern i bakgrunden så terminalen frigjörs."
            },
            {
                "question": "Vad gör FROM i en Dockerfile?",
                "options": [
                    "Anger destination för imagen",
                    "Anger vilken basimage som används",
                    "Kopierar filer från host",
                    "Definierar startkommando"
                ],
                "correct": 1,
                "explanation": "FROM anger basimage. Varje Dockerfile måste börja med FROM."
            },
            {
                "question": "Hur bygger du en image med taggen 'myapp:v1'?",
                "options": [
                    "docker create -t myapp:v1 .",
                    "docker build -t myapp:v1 .",
                    "docker image myapp:v1 .",
                    "docker make -t myapp:v1 ."
                ],
                "correct": 1,
                "explanation": "docker build -t namn:tag bygger image från Dockerfile i nuvarande katalog."
            },
            {
                "question": "Hur exponerar du port 80 i containern till port 8080 på host?",
                "options": [
                    "-p 80:8080",
                    "-p 8080:80",
                    "--port 80:8080",
                    "--expose 8080:80"
                ],
                "correct": 1,
                "explanation": "-p host:container. 8080:80 mappar host-port 8080 till container-port 80."
            },
            {
                "question": "Hur ser du loggar för en container?",
                "options": ["docker log", "docker logs", "docker output", "docker show logs"],
                "correct": 1,
                "explanation": "docker logs container_id visar stdout och stderr från containern."
            },
            {
                "question": "Vad gör 'docker exec -it container bash'?",
                "options": [
                    "Startar en ny container",
                    "Öppnar shell i körande container",
                    "Kör bash-script",
                    "Bygger container med bash"
                ],
                "correct": 1,
                "explanation": "exec kör kommando i körande container. -it ger interaktiv terminal."
            },
            {
                "question": "Hur tar du bort alla stoppade containers?",
                "options": [
                    "docker rm -all",
                    "docker container prune",
                    "docker clean containers",
                    "docker remove stopped"
                ],
                "correct": 1,
                "explanation": "docker container prune tar bort alla stoppade containers."
            },
            {
                "question": "Vad gör COPY i Dockerfile?",
                "options": [
                    "Kopierar container till host",
                    "Kopierar filer från host till image",
                    "Kopierar image till registry",
                    "Kopierar mellan containers"
                ],
                "correct": 1,
                "explanation": "COPY kopierar filer och kataloger från build context till imagen."
            },
            {
                "question": "Hur sätter du miljövariabel i docker run?",
                "options": [
                    "--var NAME=värde",
                    "-e NAME=värde",
                    "--set NAME=värde",
                    "-v NAME=värde"
                ],
                "correct": 1,
                "explanation": "-e eller --env sätter miljövariabler i containern."
            },
            {
                "question": "Vad är en Docker volume?",
                "options": [
                    "Containers diskutrymme",
                    "Persistent lagring utanför container",
                    "Containerms RAM",
                    "Loggfiler"
                ],
                "correct": 1,
                "explanation": "Volumes är persistent lagring som överlever container-omstarter."
            },
            {
                "question": "Hur namnger du en container?",
                "options": [
                    "--title namn",
                    "--name namn",
                    "-n namn",
                    "--label namn"
                ],
                "correct": 1,
                "explanation": "--name ger containern ett specifikt namn istället för slumpmässigt."
            },
            {
                "question": "Vad gör docker-compose up?",
                "options": [
                    "Uppdaterar Docker",
                    "Startar tjänster definierade i docker-compose.yml",
                    "Laddar upp images",
                    "Visar systemstatus"
                ],
                "correct": 1,
                "explanation": "docker-compose up startar alla tjänster definierade i docker-compose.yml."
            },
            {
                "question": "Hur stoppar du docker-compose tjänster?",
                "options": [
                    "docker-compose stop",
                    "docker-compose down",
                    "Båda fungerar",
                    "docker-compose end"
                ],
                "correct": 2,
                "explanation": "stop pausar containers, down stoppar och tar bort dem. Båda fungerar."
            },
            {
                "question": "Vad anger CMD i Dockerfile?",
                "options": [
                    "Byggtids-kommando",
                    "Standardkommando när container startar",
                    "Kommentar",
                    "Nätverkskonfiguration"
                ],
                "correct": 1,
                "explanation": "CMD definierar kommandot som körs när containern startar."
            },
            {
                "question": "Hur listar du alla images?",
                "options": ["docker images", "docker image ls", "Båda fungerar", "docker list images"],
                "correct": 2,
                "explanation": "Både docker images och docker image ls visar lokala images."
            },
        ],
        "medium": [
            {
                "question": "Vad är skillnaden mellan CMD och ENTRYPOINT?",
                "options": [
                    "Det finns ingen skillnad",
                    "CMD kan överskrivas, ENTRYPOINT är fast",
                    "ENTRYPOINT körs vid build, CMD vid run",
                    "CMD är för Linux, ENTRYPOINT för Windows"
                ],
                "correct": 1,
                "explanation": "ENTRYPOINT är huvudkommandot. CMD ger standardargument som kan överskrivas."
            },
            {
                "question": "Hur fungerar Docker layer caching?",
                "options": [
                    "Alla layers cachas alltid",
                    "Ändrade layers och alla efter invalideras",
                    "Bara RUN-kommandon cachas",
                    "Caching är inaktiverat som standard"
                ],
                "correct": 1,
                "explanation": "När ett layer ändras invalideras det och alla efterföljande layers."
            },
            {
                "question": "Vad är multi-stage builds?",
                "options": [
                    "Bygga för flera OS",
                    "Flera FROM i Dockerfile för mindre slutimage",
                    "Bygga i flera steg automatiskt",
                    "Parallella builds"
                ],
                "correct": 1,
                "explanation": "Multi-stage använder flera FROM. Bygg i ett stage, kopiera artefakter till minimal slutimage."
            },
            {
                "question": "Hur begränsar du containers minne till 512 MB?",
                "options": [
                    "--memory 512",
                    "-m 512m",
                    "--ram 512MB",
                    "--limit-memory 512"
                ],
                "correct": 1,
                "explanation": "-m eller --memory med enhet (m för MB, g för GB) begränsar RAM."
            },
            {
                "question": "Vad gör .dockerignore?",
                "options": [
                    "Ignorerar fel vid build",
                    "Exkluderar filer från build context",
                    "Ignorerar layer cache",
                    "Inaktiverar logging"
                ],
                "correct": 1,
                "explanation": ".dockerignore exkluderar filer från att skickas till Docker daemon vid build."
            },
            {
                "question": "Skillnaden mellan COPY och ADD i Dockerfile?",
                "options": [
                    "Ingen skillnad",
                    "ADD kan extrahera tar och ladda från URL",
                    "COPY är snabbare",
                    "ADD funkar bara med kataloger"
                ],
                "correct": 1,
                "explanation": "ADD har extra funktioner (tar-extraktion, URL). COPY rekommenderas för enkelhet."
            },
            {
                "question": "Hur skapar du custom Docker-nätverk?",
                "options": [
                    "docker network add mynet",
                    "docker network create mynet",
                    "docker create network mynet",
                    "docker net new mynet"
                ],
                "correct": 1,
                "explanation": "docker network create skapar nytt nätverk. Containers i samma nätverk kan nå varandra."
            },
            {
                "question": "Vad gör docker system prune?",
                "options": [
                    "Rensar container logs",
                    "Tar bort oanvända resurser",
                    "Uppdaterar Docker",
                    "Optimerar prestanda"
                ],
                "correct": 1,
                "explanation": "prune tar bort stoppade containers, oanvända nätverk, dangling images och build cache."
            },
            {
                "question": "Hur sätter du restart policy för alltid omstart?",
                "options": [
                    "--restart=always",
                    "--auto-restart",
                    "--keep-alive",
                    "--persistent"
                ],
                "correct": 0,
                "explanation": "--restart=always startar om containern automatiskt, även efter host reboot."
            },
            {
                "question": "Vad är depends_on i docker-compose?",
                "options": [
                    "Installerar dependencies",
                    "Definierar startordning mellan tjänster",
                    "Kräver specifik Docker-version",
                    "Länkar volymer"
                ],
                "correct": 1,
                "explanation": "depends_on säkerställer att beroende tjänster startas först (men väntar inte på ready)."
            },
            {
                "question": "Hur skalar du tjänst till 3 replikor i docker-compose?",
                "options": [
                    "docker-compose scale web=3",
                    "docker-compose up --scale web=3",
                    "docker-compose replicas web 3",
                    "docker-compose -r 3 web"
                ],
                "correct": 1,
                "explanation": "--scale tjänst=antal startar flera instanser av en tjänst."
            },
            {
                "question": "Skillnaden mellan ARG och ENV i Dockerfile?",
                "options": [
                    "Ingen skillnad",
                    "ARG är build-time, ENV är runtime",
                    "ENV är bara för Linux",
                    "ARG kräver Docker Compose"
                ],
                "correct": 1,
                "explanation": "ARG finns bara under build. ENV finns i körande container och kan ses med inspect."
            },
            {
                "question": "Hur kopierar du fil från container till host?",
                "options": [
                    "docker cp container:/path ./lokal",
                    "docker copy container:/path ./lokal",
                    "docker export container:/path ./lokal",
                    "docker get container:/path ./lokal"
                ],
                "correct": 0,
                "explanation": "docker cp kopierar filer mellan container och host i båda riktningar."
            },
            {
                "question": "Vad visar docker stats?",
                "options": [
                    "Image-statistik",
                    "Realtids CPU, minne, I/O för containers",
                    "Build-historik",
                    "Nätverksstatistik för host"
                ],
                "correct": 1,
                "explanation": "docker stats visar live resursanvändning för körande containers."
            },
            {
                "question": "Hur kör du container som icke-root användare?",
                "options": [
                    "--user nobody",
                    "--user 1000:1000",
                    "USER i Dockerfile",
                    "Alla ovan fungerar"
                ],
                "correct": 3,
                "explanation": "Alla fungerar. --user vid run, eller USER i Dockerfile för permanent."
            },
            {
                "question": "Vad gör EXPOSE i Dockerfile?",
                "options": [
                    "Öppnar port automatiskt",
                    "Dokumenterar vilken port appen använder",
                    "Blockerar port",
                    "Mappar till host-port"
                ],
                "correct": 1,
                "explanation": "EXPOSE dokumenterar portar men öppnar dem inte. -p i run krävs för mapping."
            },
            {
                "question": "Hur monterar du host-katalog i container?",
                "options": [
                    "-v /host/path:/container/path",
                    "--mount /host:/container",
                    "--bind /host/path:/container/path",
                    "-d /host:/container"
                ],
                "correct": 0,
                "explanation": "-v eller --volume host:container monterar host-katalog i containern (bind mount)."
            },
            {
                "question": "Vad är Docker healthcheck?",
                "options": [
                    "Skannar image för virus",
                    "Testar om container-applikationen fungerar",
                    "Kontrollerar Docker daemon",
                    "Validerar Dockerfile"
                ],
                "correct": 1,
                "explanation": "HEALTHCHECK testar container-hälsa. Docker kan agera på unhealthy status."
            },
            {
                "question": "Hur bygger du om utan cache?",
                "options": [
                    "docker build --fresh",
                    "docker build --no-cache",
                    "docker build --rebuild",
                    "docker build --clean"
                ],
                "correct": 1,
                "explanation": "--no-cache bygger alla layers på nytt utan att använda cache."
            },
            {
                "question": "Vad gör docker inspect?",
                "options": [
                    "Skannar för säkerhetsproblem",
                    "Visar detaljerad JSON-metadata",
                    "Inspekterar Dockerfile",
                    "Debuggar körande process"
                ],
                "correct": 1,
                "explanation": "docker inspect visar all metadata om container/image/network som JSON."
            },
        ],
        "hard": [
            {
                "question": "Hur isolerar Docker containers?",
                "options": [
                    "Virtualisering med hypervisor",
                    "Linux namespaces och cgroups",
                    "Kryptering av processer",
                    "Separata kernels"
                ],
                "correct": 1,
                "explanation": "Namespaces isolerar resurser (PID, net, mnt). Cgroups begränsar CPU/minne."
            },
            {
                "question": "Vad är Docker Content Trust (DCT)?",
                "options": [
                    "Kryptering av images",
                    "Signering och verifiering av images",
                    "Access control för registries",
                    "SSL för Docker daemon"
                ],
                "correct": 1,
                "explanation": "DCT signerar images kryptografiskt. DOCKER_CONTENT_TRUST=1 aktiverar verifiering."
            },
            {
                "question": "Hur bygger du multi-arkitektur images?",
                "options": [
                    "docker build --arch amd64,arm64",
                    "docker buildx build --platform linux/amd64,linux/arm64",
                    "docker build --multi-platform",
                    "docker manifest create"
                ],
                "correct": 1,
                "explanation": "BuildX med --platform bygger för flera arkitekturer. Skapar manifest list."
            },
            {
                "question": "Vad är distroless images?",
                "options": [
                    "Images utan Docker",
                    "Images utan OS, shell eller pakethanterare",
                    "Komprimerade images",
                    "Images för alla distros"
                ],
                "correct": 1,
                "explanation": "Distroless innehåller bara app och runtime. Ingen shell = säkrare, mindre."
            },
            {
                "question": "Hur fungerar Docker overlay network?",
                "options": [
                    "Delar host-nätverk",
                    "VXLAN för multi-host kommunikation",
                    "VPN mellan containers",
                    "Proxy för extern trafik"
                ],
                "correct": 1,
                "explanation": "Overlay använder VXLAN encapsulation för container-kommunikation över flera hosts."
            },
            {
                "question": "Vad gör --cap-drop=ALL?",
                "options": [
                    "Tar bort alla containers",
                    "Tar bort alla Linux capabilities",
                    "Stänger av logging",
                    "Tar bort alla volymer"
                ],
                "correct": 1,
                "explanation": "--cap-drop=ALL tar bort alla privileges. Lägg till endast vad som behövs med --cap-add."
            },
            {
                "question": "Hur hanterar du secrets i Docker Swarm?",
                "options": [
                    "Miljövariabler",
                    "docker secret create och monteras i /run/secrets/",
                    "Krypterade volymer",
                    ".env-filer"
                ],
                "correct": 1,
                "explanation": "Swarm secrets är krypterade, lagras i Raft log, monteras som filer i containers."
            },
            {
                "question": "Vad är PID 1 problemet i containers?",
                "options": [
                    "Container kan inte starta",
                    "PID 1 måste hantera signals och zombies",
                    "Endast root kan vara PID 1",
                    "PID 1 tar för mycket CPU"
                ],
                "correct": 1,
                "explanation": "Container PID 1 måste hantera signals korrekt och reapa zombie-processer. Använd --init."
            },
            {
                "question": "Hur begränsar du syscalls med seccomp?",
                "options": [
                    "--seccomp /path/profile",
                    "--security-opt seccomp=profile.json",
                    "--syscall-filter profile",
                    "--kernel-restrict profile"
                ],
                "correct": 1,
                "explanation": "--security-opt seccomp=profile.json applicerar seccomp-filter som begränsar kernel calls."
            },
            {
                "question": "Vad är Docker macvlan?",
                "options": [
                    "Virtuellt LAN för containers",
                    "Containers får egna MAC-adresser på fysiska nätverket",
                    "MAC-baserad access control",
                    "VPN mellan hosts"
                ],
                "correct": 1,
                "explanation": "Macvlan ger containers egna MAC-adresser så de syns som separata enheter på nätverket."
            },
            {
                "question": "Hur fungerar Docker BuildKit cache mounts?",
                "options": [
                    "Cachar alla layers automatiskt",
                    "RUN --mount=type=cache persistar cache mellan builds",
                    "Monterar host cache",
                    "Cachar base images"
                ],
                "correct": 1,
                "explanation": "BuildKit cache mounts persistar t.ex. npm cache eller apt cache mellan builds."
            },
            {
                "question": "Vad är OCI?",
                "options": [
                    "Docker företagets namn",
                    "Open Container Initiative - standard för containers",
                    "Online Container Infrastructure",
                    "Orchestration Control Interface"
                ],
                "correct": 1,
                "explanation": "OCI definierar standard för container runtime och image format som alla följer."
            },
            {
                "question": "Hur fungerar Docker rootless mode?",
                "options": [
                    "Kör containers utan root",
                    "Kör Docker daemon och containers som vanlig användare",
                    "Root-lösenord krävs inte",
                    "Tar bort root från containers"
                ],
                "correct": 1,
                "explanation": "Rootless kör hela Docker daemon som icke-root med user namespaces. Säkrare."
            },
            {
                "question": "Vad gör docker run --init?",
                "options": [
                    "Initierar nätverk",
                    "Kör init-process (tini) som PID 1",
                    "Skapar initial volume",
                    "Initierar logging"
                ],
                "correct": 1,
                "explanation": "--init kör tini som PID 1 för korrekt signal-hantering och zombie reaping."
            },
            {
                "question": "Hur skapar du build-time secrets utan att de hamnar i image?",
                "options": [
                    "ARG SECRET=value",
                    "RUN --mount=type=secret,id=mysecret",
                    "ENV SECRET=value",
                    "COPY secrets.txt"
                ],
                "correct": 1,
                "explanation": "BuildKit secret mounts exponerar secrets under build utan att spara i layer."
            },
            {
                "question": "Vad är containerd?",
                "options": [
                    "Alternativ till Docker",
                    "Container runtime som Docker använder",
                    "Container debugger",
                    "Container DNS"
                ],
                "correct": 1,
                "explanation": "containerd är runtime som Docker (och K8s) använder. Hanterar container lifecycle."
            },
            {
                "question": "Hur optimerar du layer caching för Node.js app?",
                "options": [
                    "COPY . . först",
                    "COPY package*.json och npm install före COPY . .",
                    "RUN npm install först",
                    "Ordningen spelar ingen roll"
                ],
                "correct": 1,
                "explanation": "Kopiera package.json och installera dependencies först. Kod ändras oftare än dependencies."
            },
            {
                "question": "Vad är union filesystem i Docker?",
                "options": [
                    "Filsystem för flera containers",
                    "Stackar read-only layers med write layer överst",
                    "Delat nätverk-filsystem",
                    "Komprimerat filsystem"
                ],
                "correct": 1,
                "explanation": "Union FS (overlay2) stackar image layers. Container får write layer överst (copy-on-write)."
            },
            {
                "question": "Hur debuggar du container som kraschar direkt?",
                "options": [
                    "docker logs",
                    "docker run --entrypoint /bin/sh image",
                    "docker inspect",
                    "docker debug"
                ],
                "correct": 1,
                "explanation": "Överskriv entrypoint till shell för att komma in och undersöka innan app startar."
            },
            {
                "question": "Vad är manifest list för Docker images?",
                "options": [
                    "Lista över image-taggar",
                    "Index över images för olika arkitekturer",
                    "Changelog för image",
                    "Lista över layers"
                ],
                "correct": 1,
                "explanation": "Manifest list (fat manifest) pekar på arkitektur-specifika images. Docker väljer rätt automatiskt."
            },
        ],
    },

    "nodes": [
        {"id": 1, "title": "Introduktion till Containers", "slug": "intro-containers"},
        {"id": 2, "title": "Docker Installation & Setup", "slug": "docker-installation"},
        {"id": 3, "title": "Docker Images Grunderna", "slug": "docker-images-basics"},
        {"id": 4, "title": "Container Livscykel", "slug": "container-lifecycle"},
        {"id": 5, "title": "Dockerfile Grunderna", "slug": "dockerfile-basics"},
        {"id": 6, "title": "Docker Build & Layers", "slug": "docker-build-layers"},
        {"id": 7, "title": "Port Mapping & Nätverk", "slug": "port-mapping-networking"},
        {"id": 8, "title": "Docker Volumes", "slug": "docker-volumes"},
        {"id": 9, "title": "Miljövariabler & Konfiguration", "slug": "env-vars-config"},
        {"id": 10, "title": "Docker Compose Grunderna", "slug": "docker-compose-basics"},
        {"id": 11, "title": "Multi-Container Applications", "slug": "multi-container-apps"},
        {"id": 12, "title": "Docker Networks Djupdykning", "slug": "docker-networks-deep"},
        {"id": 13, "title": "Image Optimering", "slug": "image-optimization"},
        {"id": 14, "title": "Multi-Stage Builds", "slug": "multi-stage-builds"},
        {"id": 15, "title": "Docker Security Basics", "slug": "docker-security-basics"},
        {"id": 16, "title": "Debugging & Logging", "slug": "debugging-logging"},
        {"id": 17, "title": "Docker Registry & Distribution", "slug": "registry-distribution"},
        {"id": 18, "title": "Resource Management", "slug": "resource-management"},
        {"id": 19, "title": "Docker i CI/CD", "slug": "docker-cicd"},
        {"id": 20, "title": "Production Best Practices", "slug": "production-best-practices"},
    ],
}
