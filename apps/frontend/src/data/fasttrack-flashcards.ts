/**
 * FastTrack Flashcards Data
 * Organized by tool slug
 */

interface Flashcard {
    front: string
    back: string
}

export const FASTTRACK_FLASHCARDS: Record<string, Flashcard[]> = {
    // YAML
    yaml: [
        { front: "Vad står YAML för?", back: "YAML Ain't Markup Language (rekursivt akronym)" },
        { front: "Hur markerar man en lista i YAML?", back: "Med bindestreck (-) följt av mellanslag" },
        { front: "Vilken filändelse används för YAML?", back: ".yaml eller .yml" },
        { front: "Hur skriver man en kommentar i YAML?", back: "Med # (hashtag)" },
        { front: "Vad är en YAML anchor?", back: "Ett sätt att återanvända data med & för definition och * för referens" },
        { front: "Hur representerar man null i YAML?", back: "null, ~, eller tomt värde" },
        { front: "Vad är skillnaden på | och > i YAML?", back: "| bevarar radbrytningar, > foldar till en rad" },
        { front: "Hur skriver man en boolean i YAML?", back: "true/false, yes/no, on/off" },
        { front: "Vad är ett YAML document?", back: "En sektion separerad med --- (start) och ... (slut)" },
        { front: "Hur många mellanslag används för indentation i YAML?", back: "Vanligtvis 2, men kan vara vilket antal som helst (konsekvent)" },
    ],
    // JSON
    json: [
        { front: "Vad står JSON för?", back: "JavaScript Object Notation" },
        { front: "Vilka datatyper stöds i JSON?", back: "String, Number, Boolean, null, Array, Object" },
        { front: "Kan JSON ha kommentarer?", back: "Nej, JSON stöder inte kommentarer" },
        { front: "Hur representeras ett objekt i JSON?", back: "Med måsvingar { }" },
        { front: "Hur representeras en array i JSON?", back: "Med hakparenteser [ ]" },
        { front: "Måste JSON-nycklar vara i citattecken?", back: "Ja, alltid dubbla citattecken" },
        { front: "Vad returnerar JSON.parse()?", back: "Ett JavaScript-objekt från en JSON-sträng" },
        { front: "Vad returnerar JSON.stringify()?", back: "En JSON-sträng från ett JavaScript-objekt" },
        { front: "Vilken MIME-type har JSON?", back: "application/json" },
        { front: "Kan JSON ha trailing commas?", back: "Nej, det är inte tillåtet i strikt JSON" },
    ],
    // Docker
    docker: [
        { front: "Vad är en Docker container?", back: "En isolerad, körbar instans av en Docker image" },
        { front: "Vad är skillnaden mellan image och container?", back: "Image är en mall (read-only), container är en körande instans" },
        { front: "Vad gör docker build?", back: "Bygger en image från en Dockerfile" },
        { front: "Vad är Dockerfile FROM?", back: "Anger bas-imagen att bygga vidare på" },
        { front: "Vad gör docker-compose up?", back: "Startar alla services definierade i docker-compose.yml" },
        { front: "Vad är ett Docker volume?", back: "Persistent lagring som överlever container-omstart" },
        { front: "Vad gör EXPOSE i Dockerfile?", back: "Dokumenterar vilka portar containern lyssnar på" },
        { front: "Vad är skillnaden på CMD och ENTRYPOINT?", back: "CMD kan överskrivas vid docker run, ENTRYPOINT är fast" },
        { front: "Vad gör docker ps?", back: "Listar körande containers" },
        { front: "Vad är multi-stage build?", back: "Dockerfile med flera FROM för att minska image-storlek" },
        { front: "Vad gör docker exec?", back: "Kör ett kommando i en körande container" },
        { front: "Vad är Docker Hub?", back: "Officiellt registry för Docker images" },
    ],
    // Kubernetes
    kubernetes: [
        { front: "Vad är en Pod i Kubernetes?", back: "Minsta deploybara enheten, en eller flera containers" },
        { front: "Vad gör kubectl apply?", back: "Applicerar en konfiguration till klustret" },
        { front: "Vad är en Deployment?", back: "Controller som hanterar Pod-replikor och uppdateringar" },
        { front: "Vad är en Service i K8s?", back: "Abstraktion som exponerar Pods via stabil IP/DNS" },
        { front: "Vad är ett Namespace?", back: "Logisk separation av resurser i klustret" },
        { front: "Vad är en ConfigMap?", back: "Objekt för att lagra icke-känslig konfigurationsdata" },
        { front: "Vad är ett Secret?", back: "Objekt för att lagra känslig data (base64-kodat)" },
        { front: "Vad är en ReplicaSet?", back: "Säkerställer att ett visst antal Pod-kopior körs" },
        { front: "Vad är Ingress?", back: "Hanterar extern HTTP/HTTPS-access till Services" },
        { front: "Vad gör kubelet?", back: "Agent som kör på varje nod och hanterar containers" },
        { front: "Vad är etcd?", back: "Key-value store för kluster-state" },
        { front: "Vad är en DaemonSet?", back: "Kör en Pod på varje nod i klustret" },
    ],
    // Bash
    bash: [
        { front: "Hur skapar man en variabel i Bash?", back: "variabel=värde (inga mellanslag!)" },
        { front: "Hur refererar man till en variabel?", back: "Med $variabel eller ${variabel}" },
        { front: "Vad gör $? i Bash?", back: "Returnerar exit-status för senaste kommando" },
        { front: "Vad gör $0 $1 $2?", back: "$0=skriptnamn, $1=första arg, $2=andra arg, etc" },
        { front: "Hur gör man en if-sats i Bash?", back: "if [ villkor ]; then ... fi" },
        { front: "Vad är skillnaden på [ ] och [[ ]]?", back: "[[ ]] är säkrare, stöder regex och && ||" },
        { front: "Hur gör man en for-loop?", back: "for i in lista; do ... done" },
        { front: "Vad gör pipe |?", back: "Skickar output från ett kommando till nästa" },
        { front: "Vad gör 2>&1?", back: "Redirectar stderr till stdout" },
        { front: "Vad gör set -e?", back: "Avslutar skript vid första fel" },
        { front: "Hur kör man kommando i bakgrunden?", back: "Med & i slutet av kommandot" },
        { front: "Vad gör chmod +x?", back: "Gör filen körbar" },
    ],
    // Nginx
    nginx: [
        { front: "Vad är Nginx primärt?", back: "Webbserver, reverse proxy och load balancer" },
        { front: "Var ligger Nginx config vanligtvis?", back: "/etc/nginx/nginx.conf" },
        { front: "Vad är ett server block?", back: "Konfigurerar en virtuell host/domän" },
        { front: "Vad gör proxy_pass?", back: "Vidarebefordrar requests till backend-server" },
        { front: "Hur testar man Nginx-config?", back: "nginx -t" },
        { front: "Hur laddar man om Nginx-config?", back: "nginx -s reload eller systemctl reload nginx" },
        { front: "Vad är upstream i Nginx?", back: "Definierar en grupp backend-servrar för load balancing" },
        { front: "Vad är location block?", back: "Matchar URL-paths och definierar hantering" },
        { front: "Hur aktiverar man gzip?", back: "gzip on; i http eller server block" },
        { front: "Vad är worker_processes?", back: "Antal Nginx worker-processer (auto = antal CPU-kärnor)" },
    ],
    // Git
    git: [
        { front: "Vad gör git init?", back: "Skapar ett nytt Git-repository" },
        { front: "Vad är skillnaden på git fetch och git pull?", back: "fetch hämtar utan merge, pull = fetch + merge" },
        { front: "Vad gör git stash?", back: "Sparar undan uncommitted changes temporärt" },
        { front: "Vad är en branch?", back: "En oberoende utvecklingslinje" },
        { front: "Vad gör git rebase?", back: "Flyttar commits till en ny bas-commit" },
        { front: "Vad är HEAD i Git?", back: "Pekare till aktuell commit/branch" },
        { front: "Hur ångrar man senaste commit?", back: "git reset --soft HEAD~1 (behåller ändringar)" },
        { front: "Vad är .gitignore?", back: "Fil som listar filer/mappar Git ska ignorera" },
        { front: "Vad gör git cherry-pick?", back: "Applicerar en specifik commit på aktuell branch" },
        { front: "Vad är skillnaden på merge och rebase?", back: "Merge bevarar historik, rebase skapar linjär historik" },
    ],
    // Terraform
    terraform: [
        { front: "Vad är Terraform?", back: "Infrastructure as Code-verktyg från HashiCorp" },
        { front: "Vad gör terraform init?", back: "Initialiserar working directory, laddar providers" },
        { front: "Vad gör terraform plan?", back: "Visar vilka ändringar som kommer göras" },
        { front: "Vad gör terraform apply?", back: "Applicerar ändringar till infrastrukturen" },
        { front: "Vad är Terraform state?", back: "Fil som spårar nuvarande infrastruktur-state" },
        { front: "Vad är en Terraform provider?", back: "Plugin för att hantera specifik plattform (AWS, Azure, etc)" },
        { front: "Vad är HCL?", back: "HashiCorp Configuration Language - Terraforms syntax" },
        { front: "Vad är en Terraform module?", back: "Återanvändbart paket av Terraform-konfiguration" },
        { front: "Vad gör terraform destroy?", back: "Tar bort all infrastruktur som hanteras" },
        { front: "Vad är terraform.tfvars?", back: "Fil för att sätta variabelvärden" },
    ],
    // Python kwargs
    "python-kwargs": [
        { front: "Vad gör **kwargs?", back: "Fångar godtyckligt antal keyword arguments som dict" },
        { front: "Vad gör *args?", back: "Fångar godtyckligt antal positional arguments som tuple" },
        { front: "Hur använder man **kwargs?", back: "def func(**kwargs): for key, val in kwargs.items()" },
        { front: "Kan man kombinera *args och **kwargs?", back: "Ja: def func(*args, **kwargs)" },
        { front: "Vilken ordning måste parametrar ha?", back: "regular, *args, keyword-only, **kwargs" },
        { front: "Hur skickar man dict som kwargs?", back: "func(**my_dict)" },
        { front: "Vad händer om man skickar okänd kwarg?", back: "Om funktionen inte tar **kwargs får man TypeError" },
    ],
    // Python classes
    "python-classes": [
        { front: "Vad gör __init__?", back: "Konstruktor - körs när objekt skapas" },
        { front: "Vad är self?", back: "Referens till objektinstansen" },
        { front: "Hur skapar man en klass?", back: "class MyClass: ..." },
        { front: "Vad är inheritance?", back: "En klass ärver attribut/metoder från en annan" },
        { front: "Hur ärver man i Python?", back: "class Child(Parent): ..." },
        { front: "Vad är en class method?", back: "Metod som tar cls istället för self, @classmethod" },
        { front: "Vad är en static method?", back: "Metod utan self/cls, @staticmethod" },
        { front: "Vad är en property?", back: "Getter/setter som attribut, @property" },
        { front: "Vad är __str__?", back: "Dunder-metod för string-representation (print)" },
        { front: "Vad är super()?", back: "Anropar metod från parent-klassen" },
    ],
    // Alpine
    alpine: [
        { front: "Vad är Alpine Linux?", back: "Minimal, säkerhetsfokuserad Linux-distribution (~5MB)" },
        { front: "Vilken pakethanterare använder Alpine?", back: "apk (Alpine Package Keeper)" },
        { front: "Hur installerar man paket i Alpine?", back: "apk add paketnamn" },
        { front: "Hur uppdaterar man paketindex?", back: "apk update" },
        { front: "Vilket C-bibliotek använder Alpine?", back: "musl libc (istället för glibc)" },
        { front: "Varför är Alpine populärt för Docker?", back: "Extremt liten storlek, snabba builds" },
        { front: "Vad är BusyBox?", back: "Kombinerar vanliga Unix-verktyg i en binär" },
        { front: "Hur tar man bort apk-cache?", back: "rm -rf /var/cache/apk/*" },
    ],
    // Prometheus
    prometheus: [
        { front: "Vad är Prometheus?", back: "Open-source monitoring och alerting system" },
        { front: "Hur samlar Prometheus in data?", back: "Pull-baserat - scrapes endpoints" },
        { front: "Vad är PromQL?", back: "Prometheus Query Language för att fråga metrics" },
        { front: "Vad är en Prometheus exporter?", back: "Exponerar metrics i Prometheus-format" },
        { front: "Vilken datatyp är vanligast i Prometheus?", back: "Counter och Gauge" },
        { front: "Vad är Alertmanager?", back: "Hanterar alerts från Prometheus" },
        { front: "På vilken port kör Prometheus default?", back: "9090" },
        { front: "Vad är en scrape target?", back: "Endpoint som Prometheus hämtar metrics från" },
    ],
    // Redis
    redis: [
        { front: "Vad är Redis?", back: "In-memory key-value data store" },
        { front: "Vilka datastrukturer stöder Redis?", back: "Strings, Lists, Sets, Sorted Sets, Hashes, Streams" },
        { front: "Vad gör SET och GET?", back: "SET lagrar värde, GET hämtar värde" },
        { front: "Vad är Redis TTL?", back: "Time To Live - automatisk expiry av nycklar" },
        { front: "Vad är Redis Pub/Sub?", back: "Publish/Subscribe messaging pattern" },
        { front: "Vilken port kör Redis default?", back: "6379" },
        { front: "Vad är Redis persistence?", back: "RDB snapshots eller AOF append-only file" },
        { front: "Vad gör INCR?", back: "Ökar ett numeriskt värde med 1 (atomic)" },
    ],
    // SSH
    ssh: [
        { front: "Vad är SSH?", back: "Secure Shell - protokoll för säker remote access" },
        { front: "Vilken port använder SSH default?", back: "22" },
        { front: "Var ligger SSH-config för användare?", back: "~/.ssh/config" },
        { front: "Vad är SSH key pair?", back: "Privat nyckel (hemlig) + publik nyckel (delas)" },
        { front: "Var lägger man publik nyckel på server?", back: "~/.ssh/authorized_keys" },
        { front: "Hur kopierar man publik nyckel till server?", back: "ssh-copy-id user@host" },
        { front: "Vad är SSH tunneling?", back: "Krypterad tunnel för att vidarebefordra portar" },
        { front: "Hur gör man lokal port forwarding?", back: "ssh -L localport:remotehost:remoteport user@server" },
        { front: "Vad är SSH agent?", back: "Lagrar dekrypterade privata nycklar i minnet" },
        { front: "Hur genererar man SSH-nyckel?", back: "ssh-keygen -t ed25519 -C 'kommentar'" },
    ],
    // PostgreSQL
    postgresql: [
        { front: "Vad är PostgreSQL?", back: "Kraftfull open-source relationsdatabas" },
        { front: "Vilken port kör PostgreSQL default?", back: "5432" },
        { front: "Vad är psql?", back: "PostgreSQL kommandoradsklient" },
        { front: "Hur listar man databaser i psql?", back: "\\l eller \\list" },
        { front: "Hur byter man databas i psql?", back: "\\c databasnamn" },
        { front: "Vad är JSONB?", back: "Binärt JSON-format med indexering" },
        { front: "Hur skapar man index?", back: "CREATE INDEX name ON table(column)" },
        { front: "Vad gör VACUUM?", back: "Frigör utrymme och uppdaterar statistik" },
        { front: "Vad är en foreign key?", back: "Referens till primary key i annan tabell" },
        { front: "Hur gör man backup?", back: "pg_dump databasnamn > backup.sql" },
    ],
    // GitHub Actions
    "github-actions": [
        { front: "Var definieras GitHub Actions workflows?", back: ".github/workflows/*.yml" },
        { front: "Vad är en GitHub Actions workflow?", back: "Automatiserad process definierad i YAML" },
        { front: "Vad är ett job i GitHub Actions?", back: "En uppsättning steps som körs på samma runner" },
        { front: "Vad är en step?", back: "Enskild uppgift i ett job (action eller kommando)" },
        { front: "Vad är en runner?", back: "Server som kör workflows (GitHub-hosted eller self-hosted)" },
        { front: "Hur triggar man workflow på push?", back: "on: push: branches: [main]" },
        { front: "Hur använder man secrets?", back: "${{ secrets.SECRET_NAME }}" },
        { front: "Vad är Actions marketplace?", back: "Bibliotek av färdiga actions att återanvända" },
        { front: "Hur cachar man dependencies?", back: "actions/cache action" },
        { front: "Vad är matrix builds?", back: "Köra samma job med olika konfigurationer parallellt" },
    ],
}
