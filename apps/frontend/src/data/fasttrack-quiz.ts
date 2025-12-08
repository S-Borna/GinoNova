/**
 * FastTrack Quiz Data
 * Multiple choice questions organized by tool slug
 */

interface QuizQuestion {
    question: string
    options: string[]
    correct: number
    explanation?: string
}

export const FASTTRACK_QUIZ: Record<string, QuizQuestion[]> = {
    // YAML
    yaml: [
        { question: "Vad står YAML för?", options: ["Yet Another Markup Language", "YAML Ain't Markup Language", "Your Advanced Markup Language", "YAML Application Markup Language"], correct: 1, explanation: "YAML Ain't Markup Language är ett rekursivt akronym" },
        { question: "Hur markerar man en lista i YAML?", options: ["Med hakparenteser [ ]", "Med bindestreck -", "Med asterisk *", "Med nummer 1. 2. 3."], correct: 1 },
        { question: "Vilken symbol används för kommentarer i YAML?", options: ["//", "/* */", "#", "--"], correct: 2 },
        { question: "Vad gör | i YAML?", options: ["Skapar en pipe", "Bevarar radbrytningar", "Foldar text till en rad", "Escape-tecken"], correct: 1, explanation: "| (literal block) bevarar radbrytningar, > foldar till en rad" },
        { question: "Hur representerar man null i YAML?", options: ["null eller ~", "undefined", "nil", "empty"], correct: 0 },
        { question: "Vad används & för i YAML?", options: ["Kommentar", "Anchor (för återanvändning)", "Escape-tecken", "String concatenation"], correct: 1, explanation: "& definierar en anchor som kan refereras med *" },
    ],
    // JSON
    json: [
        { question: "Vilka citattecken måste användas för JSON-nycklar?", options: ["Enkla '", "Dubbla \"", "Backticks `", "Inga krävs"], correct: 1, explanation: "JSON kräver alltid dubbla citattecken för nycklar" },
        { question: "Stöder JSON kommentarer?", options: ["Ja, med //", "Ja, med #", "Ja, med /* */", "Nej"], correct: 3, explanation: "Standard JSON stöder inte kommentarer" },
        { question: "Vad returnerar JSON.parse()?", options: ["En sträng", "Ett JavaScript-objekt", "En array", "undefined"], correct: 1 },
        { question: "Vilken MIME-type har JSON?", options: ["text/json", "application/json", "text/javascript", "application/x-json"], correct: 1 },
        { question: "Är trailing commas tillåtna i JSON?", options: ["Ja, alltid", "Ja, bara i arrays", "Ja, bara i objects", "Nej"], correct: 3 },
    ],
    // Docker
    docker: [
        { question: "Vad är skillnaden mellan Docker image och container?", options: ["Ingen skillnad", "Image är körande, container är mall", "Container är körande, image är mall", "Image är för Linux, container för Windows"], correct: 2, explanation: "Image är en read-only mall, container är en körande instans" },
        { question: "Vad gör kommandot 'docker build'?", options: ["Startar en container", "Bygger en image från Dockerfile", "Uppdaterar Docker", "Listar images"], correct: 1 },
        { question: "Vilken instruktion i Dockerfile anger bas-imagen?", options: ["BASE", "IMAGE", "FROM", "IMPORT"], correct: 2 },
        { question: "Vad gör 'docker ps -a'?", options: ["Visar bara körande containers", "Visar alla containers inkl stoppade", "Visar alla images", "Visar processer i container"], correct: 1 },
        { question: "Vad är ett Docker volume?", options: ["CPU-begränsning", "Nätverkskonfiguration", "Persistent lagring", "Log-fil"], correct: 2, explanation: "Volumes är för persistent data som överlever container-omstart" },
        { question: "Vad gör EXPOSE i Dockerfile?", options: ["Öppnar portar automatiskt", "Dokumenterar portar", "Blockerar portar", "Mappnar portar"], correct: 1, explanation: "EXPOSE dokumenterar vilka portar containern lyssnar på" },
        { question: "Vad är multi-stage build?", options: ["Bygga flera containers samtidigt", "Dockerfile med flera FROM", "Distribuera till flera servrar", "Versionshantering av images"], correct: 1 },
    ],
    // Kubernetes
    kubernetes: [
        { question: "Vad är en Pod i Kubernetes?", options: ["En server", "Minsta deploybara enheten", "Ett nätverk", "En databas"], correct: 1, explanation: "Pod är den minsta enheten och kan innehålla en eller flera containers" },
        { question: "Vad hanterar en Deployment?", options: ["Nätverk", "Lagring", "Pod-replikor och uppdateringar", "Användare"], correct: 2 },
        { question: "Vad gör en Service i Kubernetes?", options: ["Kör containers", "Exponerar Pods via stabil IP/DNS", "Lagrar data", "Hanterar config"], correct: 1 },
        { question: "Vad är ett Namespace?", options: ["DNS-server", "Logisk separation av resurser", "Container-runtime", "Filsystem"], correct: 1 },
        { question: "Vad är skillnaden på ConfigMap och Secret?", options: ["Ingen skillnad", "ConfigMap är encrypted", "Secret är för känslig data (base64)", "ConfigMap är större"], correct: 2 },
        { question: "Vad gör kubelet?", options: ["Hanterar API-server", "Agent på varje nod som hanterar containers", "Load balancer", "Storage controller"], correct: 1 },
        { question: "Vad lagras i etcd?", options: ["Container images", "Kluster-state", "Log-filer", "Metrics"], correct: 1 },
    ],
    // Bash
    bash: [
        { question: "Hur skapar man en variabel i Bash?", options: ["var = värde", "var=värde", "$var=värde", "set var=värde"], correct: 1, explanation: "Inga mellanslag runt = tecken!" },
        { question: "Vad returnerar $?", options: ["PID", "Exit-status för senaste kommando", "Antal argument", "Skriptnamn"], correct: 1 },
        { question: "Vad gör 2>&1?", options: ["Redirectar stdout till fil 2", "Redirectar stderr till stdout", "Kör kommando 2 gånger", "Skapar fil med namn 2"], correct: 1 },
        { question: "Vad är skillnaden på [ ] och [[ ]]?", options: ["Ingen skillnad", "[[ ]] är säkrare och har fler features", "[ ] är nyare", "[[ ]] fungerar bara i zsh"], correct: 1, explanation: "[[ ]] stöder regex, && || och är säkrare med variabler" },
        { question: "Vad gör set -e?", options: ["Exporterar variabler", "Avslutar vid första fel", "Aktiverar echo", "Sätter environment"], correct: 1 },
        { question: "Hur kör man kommando i bakgrunden?", options: ["bg kommando", "kommando bg", "kommando &", "& kommando"], correct: 2 },
    ],
    // Nginx
    nginx: [
        { question: "Vad är Nginx primärt?", options: ["Databas", "Webbserver och reverse proxy", "Container runtime", "CI/CD verktyg"], correct: 1 },
        { question: "Hur testar man Nginx-konfiguration?", options: ["nginx --test", "nginx -t", "nginx check", "nginx validate"], correct: 1 },
        { question: "Vad gör proxy_pass?", options: ["Blockerar requests", "Vidarebefordrar requests till backend", "Aktiverar SSL", "Cachar svar"], correct: 1 },
        { question: "Vad definierar upstream?", options: ["SSL-certifikat", "Grupp av backend-servrar", "Loggformat", "Rate limiting"], correct: 1, explanation: "upstream används för load balancing mellan flera servrar" },
        { question: "Hur laddar man om Nginx-config utan downtime?", options: ["nginx restart", "nginx -s reload", "nginx refresh", "nginx --reload"], correct: 1 },
    ],
    // Git
    git: [
        { question: "Vad är skillnaden på git fetch och git pull?", options: ["Ingen skillnad", "fetch = pull + merge", "pull = fetch + merge", "fetch är deprecated"], correct: 2, explanation: "git fetch hämtar utan merge, git pull hämtar OCH mergar" },
        { question: "Vad gör git stash?", options: ["Tar bort ändringar", "Sparar undan uncommitted changes temporärt", "Skapar branch", "Pushar till remote"], correct: 1 },
        { question: "Vad är HEAD i Git?", options: ["Första commit", "Senaste push", "Pekare till aktuell commit/branch", "Remote URL"], correct: 2 },
        { question: "Hur ångrar man senaste commit men behåller ändringarna?", options: ["git undo", "git reset --hard HEAD~1", "git reset --soft HEAD~1", "git revert HEAD"], correct: 2, explanation: "--soft behåller ändringar staged, --hard tar bort dem" },
        { question: "Vad gör git cherry-pick?", options: ["Väljer branch", "Applicerar specifik commit på aktuell branch", "Tar bort commit", "Mergar allt"], correct: 1 },
    ],
    // Terraform
    terraform: [
        { question: "Vad gör terraform init?", options: ["Skapar resurser", "Initialiserar directory och laddar providers", "Tar bort state", "Visar plan"], correct: 1 },
        { question: "Vad är Terraform state?", options: ["Konfigurationsfil", "Fil som spårar nuvarande infrastruktur", "Log-fil", "Plugin"], correct: 1, explanation: "State filen mappar config till verkliga resurser" },
        { question: "Vad är HCL?", options: ["HashiCorp Container Language", "HashiCorp Configuration Language", "High-level Code Language", "Hybrid Cloud Language"], correct: 1 },
        { question: "Vad gör terraform plan?", options: ["Applicerar ändringar", "Visar vilka ändringar som kommer göras", "Initialiserar projekt", "Tar bort resurser"], correct: 1, explanation: "plan är för preview, apply genomför ändringarna" },
        { question: "Vad gör terraform destroy?", options: ["Tar bort state-fil", "Tar bort all hanterad infrastruktur", "Tar bort terraform binary", "Resettar konfiguration"], correct: 1 },
    ],
    // Python kwargs
    "python-kwargs": [
        { question: "Vad fångar **kwargs?", options: ["Positional arguments som tuple", "Keyword arguments som dict", "Alla arguments som lista", "Endast första argument"], correct: 1 },
        { question: "Vilken ordning måste parametrar ha?", options: ["kwargs, args, regular", "regular, kwargs, args", "regular, *args, **kwargs", "Spelar ingen roll"], correct: 2 },
        { question: "Hur skickar man en dict som kwargs?", options: ["func(dict)", "func(*dict)", "func(**dict)", "func(&dict)"], correct: 2 },
        { question: "Vad fångar *args?", options: ["Keyword arguments som dict", "Positional arguments som tuple", "Alla variabler", "Environment variables"], correct: 1 },
    ],
    // Python classes
    "python-classes": [
        { question: "Vad gör __init__?", options: ["Destructor", "Konstruktor - körs vid objektskapande", "Static method", "Property"], correct: 1 },
        { question: "Vad är self i Python-klasser?", options: ["Klassnamn", "Referens till objektinstansen", "Statisk variabel", "Parent class"], correct: 1 },
        { question: "Hur ärver man från en klass?", options: ["class Child extends Parent", "class Child(Parent)", "class Child: Parent", "class Child inherits Parent"], correct: 1 },
        { question: "Vad är en @classmethod?", options: ["Metod som tar cls istället för self", "Metod utan parametrar", "Private method", "Abstract method"], correct: 0, explanation: "classmethod tar cls som första parameter och kan anropas på klassen" },
        { question: "Vad gör super()?", options: ["Skapar superklass", "Anropar metod från parent-klassen", "Gör metod public", "Validerar input"], correct: 1 },
    ],
    // Alpine
    alpine: [
        { question: "Vilken pakethanterare använder Alpine?", options: ["apt", "yum", "apk", "pacman"], correct: 2 },
        { question: "Vilket C-bibliotek använder Alpine?", options: ["glibc", "musl libc", "uclibc", "dietlibc"], correct: 1, explanation: "musl är mindre än glibc vilket bidrar till Alpines storlek" },
        { question: "Varför är Alpine populärt för Docker?", options: ["Har flest paket", "Extremt liten storlek (~5MB)", "Är gratis", "Stöder Windows"], correct: 1 },
        { question: "Hur installerar man paket i Alpine?", options: ["apt install", "yum install", "apk add", "alpine install"], correct: 2 },
    ],
    // Prometheus
    prometheus: [
        { question: "Hur samlar Prometheus in metrics?", options: ["Push-baserat", "Pull-baserat (scrapes)", "Båda", "Via message queue"], correct: 1, explanation: "Prometheus scrapar endpoints, det är pull-baserat" },
        { question: "Vad är PromQL?", options: ["Programmeringsspråk", "Prometheus Query Language", "Prometheus Queue Library", "Protocol definition"], correct: 1 },
        { question: "Vad är en Prometheus exporter?", options: ["Exporterar data till fil", "Exponerar metrics i Prometheus-format", "Tar backup", "Skickar alerts"], correct: 1 },
        { question: "Vilken port kör Prometheus default?", options: ["8080", "9090", "3000", "5000"], correct: 1 },
    ],
    // Redis
    redis: [
        { question: "Vad är Redis primärt?", options: ["Relationsdatabas", "In-memory key-value store", "Filsystem", "Message broker only"], correct: 1 },
        { question: "Vilken port kör Redis default?", options: ["3306", "5432", "6379", "27017"], correct: 2 },
        { question: "Vad är Redis TTL?", options: ["Total Transaction Log", "Time To Live", "Transfer Type Layer", "Test Tool Library"], correct: 1, explanation: "TTL är automatisk expiry av nycklar efter viss tid" },
        { question: "Vilka datastrukturer stöder Redis?", options: ["Bara strings", "Strings, Lists, Sets, Hashes m.fl.", "Bara key-value", "Bara JSON"], correct: 1 },
    ],
    // SSH
    ssh: [
        { question: "Vilken port använder SSH default?", options: ["21", "22", "23", "80"], correct: 1 },
        { question: "Var placeras publika nycklar på servern?", options: ["~/.ssh/id_rsa.pub", "~/.ssh/authorized_keys", "~/.ssh/known_hosts", "/etc/ssh/keys"], correct: 1 },
        { question: "Hur kopierar man publik nyckel till server?", options: ["scp ~/.ssh/id_rsa.pub", "ssh-copy-id user@host", "ssh --copy-key", "rsync key"], correct: 1 },
        { question: "Vad är SSH tunneling?", options: ["VPN-tjänst", "Krypterad tunnel för port forwarding", "Fil-komprimering", "DNS over SSH"], correct: 1 },
        { question: "Vilken algoritm rekommenderas för SSH-nycklar idag?", options: ["RSA 1024", "DSA", "ed25519", "MD5"], correct: 2, explanation: "ed25519 är modern, säker och snabb" },
    ],
    // PostgreSQL
    postgresql: [
        { question: "Vilken port kör PostgreSQL default?", options: ["3306", "5432", "27017", "6379"], correct: 1 },
        { question: "Vad är psql?", options: ["Python SQL library", "PostgreSQL CLI-klient", "Query optimizer", "Backup tool"], correct: 1 },
        { question: "Vad är JSONB i PostgreSQL?", options: ["JSON Backup", "Binärt JSON-format med indexering", "JavaScript runtime", "JSON validator"], correct: 1 },
        { question: "Vad gör VACUUM?", options: ["Tar bort databas", "Frigör utrymme och uppdaterar statistik", "Skapar backup", "Krypterar data"], correct: 1 },
        { question: "Hur listar man databaser i psql?", options: ["SHOW DATABASES", "\\l", "list db", "SELECT databases"], correct: 1 },
    ],
    // GitHub Actions
    "github-actions": [
        { question: "Var definieras GitHub Actions workflows?", options: [".github/actions/", ".github/workflows/", "actions/", ".workflows/"], correct: 1 },
        { question: "Vad är en runner?", options: ["Workflow definition", "Server som kör workflows", "GitHub-användare", "Branch"], correct: 1 },
        { question: "Hur använder man secrets i workflows?", options: ["$SECRET", "{{secrets.NAME}}", "${{ secrets.NAME }}", "env.SECRET"], correct: 2 },
        { question: "Vad är matrix builds?", options: ["Bygga för olika arkitekturer", "Köra samma job med olika konfigurationer parallellt", "Kryptering", "Dependency management"], correct: 1 },
        { question: "Hur triggar man workflow på push till main?", options: ["trigger: push", "on: push: branches: [main]", "event: push:main", "when: push"], correct: 1 },
    ],
}
