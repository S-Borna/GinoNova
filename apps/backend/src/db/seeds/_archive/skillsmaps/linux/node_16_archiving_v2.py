"""
Linux Mastery Node 16: Archiving & Compression - V2 Interactive Format
"""

LINUX_NODE_16_ARCHIVING_V2 = {
    "node_id": 16,
    "title": "Archiving & Compression",
    "slug": "archiving",
    "description": "tar, gzip, zip och backup",
    "difficulty": "beginner",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Archiving & Compression",
            "content": {
                "headline": "10GB loggfil -> 500MB komprimerad",
                "hook": "Backups, deployments, logrotation - allt involverar arkiv. En 10GB loggfil blir 500MB komprimerad. Att kunna tar är obligatoriskt för varje sysadmin.",
                "learning_objectives": [
                    "Skapa och extrahera tar-arkiv",
                    "Förstå olika komprimeringsformat (gzip, bzip2, xz)",
                    "Arbeta med zip för Windows-kompatibilitet",
                    "Automatisera backups med tar"
                ],
                "prerequisites": ["Basic file operations"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Archiving Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "tar - Tape Archive",
                        "explanation": "tar samlar filer till ETT arkiv. Kombineras med kompression: -z=gzip, -j=bzip2, -J=xz. Minns: -c=create, -x=extract, -v=verbose, -f=file.",
                        "diagram": """
+-----------------------------------------------------+
| TAR KOMMANDON                                       |
+-----------------------------------------------------+
| SKAPA:                                              |
| tar -cvf archive.tar folder/      | Bara arkiv     |
| tar -czvf archive.tar.gz folder/  | Med gzip       |
| tar -cjvf archive.tar.bz2 folder/ | Med bzip2      |
| tar -cJvf archive.tar.xz folder/  | Med xz         |
+-----------------------------------------------------+
| EXTRAHERA:                                          |
| tar -xvf archive.tar              | Extrahera      |
| tar -xzvf archive.tar.gz          | Extrahera gzip |
| tar -xzvf archive.tar.gz -C /dest | Till katalog   |
+-----------------------------------------------------+
| LISTA:                                              |
| tar -tvf archive.tar.gz           | Visa innehåll  |
+-----------------------------------------------------+""",
                        "pro_tip": "Minns CVFZ: Create Verbose File Zip",
                        "common_mistake": "Glömma -f flaggan - tar vet inte var arkivet ska"
                    },
                    {
                        "title": "Komprimeringsformat",
                        "explanation": "gzip=snabb/ok kompression, bzip2=bättre/långsammare, xz=bäst/långsammast. Välj efter behov!",
                        "diagram": """
+-----------------------------------------------------+
| KOMPRIMERING JÄMFÖRELSE                             |
+-----------------------------------------------------+
| Format   | Ext      | Kompression | Hastighet      |
|----------|----------|-------------|----------------|
| gzip     | .gz      | ★★★☆☆      | ★★★★★ Snabb    |
| bzip2    | .bz2     | ★★★★☆      | ★★★☆☆ Medium   |
| xz       | .xz      | ★★★★★      | ★★☆☆☆ Långsam  |
| zip      | .zip     | ★★★☆☆      | ★★★★☆ Windows  |
+-----------------------------------------------------+
| Tumregel: gzip för dagliga backups, xz för arkiv   |
+-----------------------------------------------------+""",
                        "pro_tip": "Använd gzip för snabba dagliga backups, xz för långtidsarkivering",
                        "common_mistake": "Att komprimera redan komprimerade filer (jpg, mp3) - ingen vinst!"
                    },
                    {
                        "title": "Praktiska Backup-mönster",
                        "explanation": "Kombinera tar med datum, exclude-mönster och piping för effektiva backups.",
                        "diagram": """
+-----------------------------------------------------+
| BACKUP PATTERNS                                     |
+-----------------------------------------------------+
| # Daglig backup med datum                           |
| tar -czvf backup_$(date +%Y%m%d).tar.gz /var/www/  |
|                                                     |
| # Exkludera filer                                   |
| tar -czvf app.tar.gz \\                            |
|     --exclude='*.log' \\                           |
|     --exclude='node_modules' \\                    |
|     --exclude='.git' \\                            |
|     ./app/                                          |
|                                                     |
| # Extrahera specifik fil                            |
| tar -xzvf backup.tar.gz path/to/file.txt           |
+-----------------------------------------------------+""",
                        "pro_tip": "--exclude-from=file.txt låter dig lista excludes i en fil",
                        "common_mistake": "Att glömma trailing slash på source-katalog påverkar strukturen"
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Archiving",
            "content": {
                "exercises": [
                    {
                        "task": "Skapa gzip-arkiv",
                        "instruction": "Skapa ett komprimerat arkiv av /var/log/ som heter logs.tar.gz",
                        "expected_command": "tar -czvf logs.tar.gz /var/log/",
                        "hint": "-c=create, -z=gzip, -v=verbose, -f=file"
                    },
                    {
                        "task": "Lista arkivinnehåll",
                        "instruction": "Visa innehållet i backup.tar.gz utan att extrahera",
                        "expected_command": "tar -tvf backup.tar.gz",
                        "hint": "-t=list, inte -x=extract"
                    },
                    {
                        "task": "Extrahera till katalog",
                        "instruction": "Extrahera archive.tar.gz till /tmp/restored/",
                        "expected_command": "tar -xzvf archive.tar.gz -C /tmp/restored/",
                        "hint": "-C anger destination directory"
                    },
                    {
                        "task": "Skapa backup med datum",
                        "instruction": "Skapa en backup av ~/projects med dagens datum i filnamnet",
                        "expected_command": "tar -czvf backup_$(date +%Y%m%d).tar.gz ~/projects",
                        "hint": "$(date +%Y%m%d) ger format 20241215"
                    }
                ],
                "estimated_time": "10 min",
                "xp_reward": 30
            }
        },
        {
            "section_id": "quiz",
            "type": "quiz",
            "title": "Testa dina kunskaper",
            "content": {
                "questions": {
                    "flashcards": [
                        {"front": "Vad gör tar -z flaggan?", "back": "Komprimerar/dekomprimerar med gzip"},
                        {"front": "Skillnad mellan tar -c och tar -x?", "back": "-c=create (skapa), -x=extract (extrahera)"},
                        {"front": "Vilken komprimering ger bäst ratio?", "back": "xz (.tar.xz) men är långsammast"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Hur extraherar du bara en specifik fil från ett arkiv?",
                            "options": [
                                "tar -xzvf archive.tar.gz file.txt",
                                "tar -xzvf archive.tar.gz --only file.txt",
                                "tar -xzvf archive.tar.gz -f file.txt",
                                "tar --extract-file file.txt archive.tar.gz"
                            ],
                            "correct": 0,
                            "explanation": "Ange bara filens sökväg efter arkivnamnet"
                        },
                        {
                            "question": "Vad händer om du glömmer -f flaggan?",
                            "options": [
                                "Tar skapar default.tar",
                                "Tar försöker läsa från tape device",
                                "Kommandot skriver ut innehåll",
                                "Fel: file not specified"
                            ],
                            "correct": 1,
                            "explanation": "tar försöker använda /dev/st0 (tape) som default device"
                        }
                    ]
                },
                "passing_score": 0.8,
                "estimated_time": "5 min",
                "xp_reward": 25
            }
        },
        {
            "section_id": "challenge",
            "type": "challenge",
            "title": "Archiving Challenge",
            "content": {
                "scenario": "Skapa ett automatiserat backup-script som arkiverar /var/www, exkluderar cache-filer, och roterar gamla backups.",
                "requirements": [
                    "Skapa daglig backup med datumstämpel",
                    "Exkludera .cache, tmp och log-kataloger",
                    "Spara till /backup/ katalogen",
                    "Ta bort backups äldre än 7 dagar"
                ],
                "hints": [
                    "Använd $(date +%Y%m%d) för datumstämpel",
                    "--exclude för att hoppa över filer",
                    "find -mtime +7 -delete för rotation"
                ],
                "solution": """#!/bin/bash
# backup_www.sh - Daglig backup av webbapplikation

# Variabler
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backup"
SOURCE="/var/www"
BACKUP_FILE="$BACKUP_DIR/www_$DATE.tar.gz"

# Skapa backup-katalog om den saknas
mkdir -p "$BACKUP_DIR"

# Skapa backup med excludes
tar -czvf "$BACKUP_FILE" \\
    --exclude='*.cache' \\
    --exclude='*/.cache' \\
    --exclude='*/tmp' \\
    --exclude='*/logs' \\
    --exclude='*.log' \\
    "$SOURCE"

# Verifiera att backupen skapades
if [ -f "$BACKUP_FILE" ]; then
    echo "Backup skapad: $BACKUP_FILE"
    ls -lh "$BACKUP_FILE"
else
    echo "FEL: Backup misslyckades!"
    exit 1
fi

# Rotera gamla backups (ta bort äldre än 7 dagar)
find "$BACKUP_DIR" -name "www_*.tar.gz" -mtime +7 -delete
echo "Gamla backups roterade"

# Lista kvarvarande backups
echo "Nuvarande backups:"
ls -lh "$BACKUP_DIR"/www_*.tar.gz""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
