"""
Docker Studyflow Data
Flashcards och Multiple Choice för Docker & Containers
"""

DOCKER_MODULE = {
    "slug": "docker",
    "title": "Docker & Containers",
    "description": "Container-teknologi och Docker",
    "icon": "Box",
    "topics": [
        {
            "id": "docker-basics",
            "title": "Docker Basics",
            "flashcards": [
                {"front": "Vad är en container?", "back": "Isolerad miljö för att köra applikationer med alla dependencies"},
                {"front": "Skillnad container vs VM?", "back": "Container delar OS-kernel, VM har eget OS"},
                {"front": "Vad är en Docker image?", "back": "Mall/blueprint för att skapa containers"},
                {"front": "Vad är Docker Hub?", "back": "Public registry för Docker images"},
                {"front": "Vad gör 'docker run'?", "back": "Skapar och startar en container från image"},
            ],
            "multiple_choice": [
                {
                    "question": "Vad delar containers med host-systemet?",
                    "options": ["Ingenting", "OS-kernel", "RAM", "Diskutrymme"],
                    "correct": 1,
                    "explanation": "Containers delar Linux-kernel med host, vilket gör dem lättare än VMs."
                },
                {
                    "question": "Vad är en Docker image?",
                    "options": ["Körande process", "Mall för containers", "Virtuell maskin", "Konfigurationsfil"],
                    "correct": 1,
                    "explanation": "En image är en read-only mall som används för att skapa containers."
                },
            ]
        },
        {
            "id": "docker-commands",
            "title": "Essential Commands",
            "flashcards": [
                {"front": "docker ps", "back": "Listar körande containers"},
                {"front": "docker ps -a", "back": "Listar alla containers inkl. stoppade"},
                {"front": "docker images", "back": "Listar alla lokala images"},
                {"front": "docker pull nginx", "back": "Laddar ner nginx-image från registry"},
                {"front": "docker stop <id>", "back": "Stoppar en körande container"},
                {"front": "docker rm <id>", "back": "Tar bort en stoppad container"},
            ],
            "multiple_choice": [
                {
                    "question": "Vilket kommando listar körande containers?",
                    "options": ["docker list", "docker ps", "docker containers", "docker show"],
                    "correct": 1,
                    "explanation": "docker ps (process status) visar körande containers."
                },
                {
                    "question": "Hur tar man bort en image?",
                    "options": ["docker rm", "docker rmi", "docker delete", "docker remove"],
                    "correct": 1,
                    "explanation": "docker rmi (remove image) tar bort images."
                },
            ]
        },
        {
            "id": "docker-dockerfile",
            "title": "Dockerfile",
            "flashcards": [
                {"front": "Vad är FROM?", "back": "Anger basimage att bygga på"},
                {"front": "Vad är COPY?", "back": "Kopierar filer från host till image"},
                {"front": "Vad är RUN?", "back": "Kör kommando under build (skapar layer)"},
                {"front": "Vad är CMD?", "back": "Default-kommando när container startar"},
                {"front": "Vad är EXPOSE?", "back": "Dokumenterar vilka portar containern lyssnar på"},
                {"front": "Vad är WORKDIR?", "back": "Sätter working directory i containern"},
            ],
            "multiple_choice": [
                {
                    "question": "Vilken instruktion måste vara först i Dockerfile?",
                    "options": ["CMD", "RUN", "FROM", "COPY"],
                    "correct": 2,
                    "explanation": "FROM måste vara först och anger basimage."
                },
                {
                    "question": "Skillnad mellan CMD och RUN?",
                    "options": ["Ingen skillnad", "RUN vid build, CMD vid start", "CMD vid build, RUN vid start", "RUN för Linux, CMD för Windows"],
                    "correct": 1,
                    "explanation": "RUN körs vid image-build, CMD körs när container startar."
                },
            ]
        },
        {
            "id": "docker-networking",
            "title": "Networking",
            "flashcards": [
                {"front": "Vad gör -p 8080:80?", "back": "Mappar host port 8080 till container port 80"},
                {"front": "Vad är bridge network?", "back": "Default nätverk - containers kan prata via IP"},
                {"front": "Vad är host network?", "back": "Container delar host's network namespace"},
                {"front": "Hur skapar man nätverk?", "back": "docker network create mynet"},
                {"front": "Hur ansluter container till nätverk?", "back": "--network mynet vid docker run"},
            ],
            "multiple_choice": [
                {
                    "question": "Vad gör flaggan -p 3000:80?",
                    "options": ["Sätter prioritet", "Mappar portar host:container", "Sätter protokoll", "Sätter process-ID"],
                    "correct": 1,
                    "explanation": "-p mappar host-port till container-port (host:container)."
                },
                {
                    "question": "Vilket är default Docker-nätverk?",
                    "options": ["host", "bridge", "none", "overlay"],
                    "correct": 1,
                    "explanation": "bridge är default nätverk för standalone containers."
                },
            ]
        },
        {
            "id": "docker-volumes",
            "title": "Volumes & Storage",
            "flashcards": [
                {"front": "Vad är en volume?", "back": "Persistent lagring utanför container-filesystem"},
                {"front": "Vad gör -v /host:/container?", "back": "Bind mount - mappar host-katalog till container"},
                {"front": "Hur skapar man named volume?", "back": "docker volume create mydata"},
                {"front": "Var lagras volumes?", "back": "/var/lib/docker/volumes/"},
                {"front": "Varför använda volumes?", "back": "Data överlever container restart/delete"},
            ],
            "multiple_choice": [
                {
                    "question": "Vad händer med data i container utan volume?",
                    "options": ["Sparas automatiskt", "Försvinner vid delete", "Kopieras till host", "Komprimeras"],
                    "correct": 1,
                    "explanation": "Data i container-layer försvinner när containern tas bort."
                },
                {
                    "question": "Skillnad bind mount vs named volume?",
                    "options": ["Ingen skillnad", "Bind mount = specifik path, volume = Docker-managed", "Volume är snabbare", "Bind mount är säkrare"],
                    "correct": 1,
                    "explanation": "Bind mount pekar på host-path, volumes hanteras av Docker."
                },
            ]
        },
        {
            "id": "docker-compose",
            "title": "Docker Compose",
            "flashcards": [
                {"front": "Vad är Docker Compose?", "back": "Verktyg för multi-container applikationer"},
                {"front": "Vad heter config-filen?", "back": "docker-compose.yml eller compose.yml"},
                {"front": "docker compose up", "back": "Startar alla services definierade i compose-fil"},
                {"front": "docker compose down", "back": "Stoppar och tar bort containers, networks"},
                {"front": "docker compose up -d", "back": "Startar i detached mode (bakgrund)"},
            ],
            "multiple_choice": [
                {
                    "question": "Vad gör 'docker compose up -d'?",
                    "options": ["Debug mode", "Detached mode (bakgrund)", "Delete efter körning", "Development mode"],
                    "correct": 1,
                    "explanation": "-d (detached) kör containers i bakgrunden."
                },
                {
                    "question": "Vilken filtyp använder Docker Compose?",
                    "options": ["JSON", "YAML", "TOML", "XML"],
                    "correct": 1,
                    "explanation": "Docker Compose använder YAML-format."
                },
            ]
        },
        {
            "id": "docker-best-practices",
            "title": "Best Practices",
            "flashcards": [
                {"front": "Varför använda .dockerignore?", "back": "Exkluderar filer från build context (snabbare build)"},
                {"front": "Varför multi-stage builds?", "back": "Mindre images - build i en stage, kör i annan"},
                {"front": "Varför inte köra som root?", "back": "Säkerhetsrisk - använd USER instruktion"},
                {"front": "Varför specifika image-taggar?", "back": "nginx:1.24 istället för nginx:latest för reproducerbarhet"},
                {"front": "Hur minskar man layers?", "back": "Kombinera RUN-kommandon med &&"},
            ],
            "multiple_choice": [
                {
                    "question": "Varför undvika 'latest' tag i production?",
                    "options": ["Långsammare", "Opålitlig - kan ändras", "Större storlek", "Kräver internet"],
                    "correct": 1,
                    "explanation": "latest kan peka på olika versioner över tid, använd specifik tag."
                },
                {
                    "question": "Vad är fördelen med multi-stage builds?",
                    "options": ["Snabbare runtime", "Mindre final image", "Bättre logging", "Fler features"],
                    "correct": 1,
                    "explanation": "Multi-stage ger mindre images genom att separera build/runtime."
                },
            ]
        },
    ]
}
