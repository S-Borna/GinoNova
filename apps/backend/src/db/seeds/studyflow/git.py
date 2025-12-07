"""
Git Studyflow Data
Flashcards och Multiple Choice för Git
"""

GIT_MODULE = {
    "slug": "git",
    "title": "Git Version Control",
    "description": "Versionskontroll med Git",
    "icon": "GitBranch",
    "topics": [
        {
            "id": "git-basics",
            "title": "Git Basics",
            "flashcards": [
                {"front": "Vad gör 'git init'?", "back": "Skapar ett nytt git-repository"},
                {"front": "Vad gör 'git clone'?", "back": "Kopierar ett remote repository lokalt"},
                {"front": "Vad är staging area?", "back": "Mellansteg där ändringar förbereds innan commit"},
                {"front": "Vad gör 'git add .'?", "back": "Lägger till alla ändringar i staging"},
                {"front": "Vad gör 'git commit -m'?", "back": "Sparar staged ändringar med meddelande"},
            ],
            "multiple_choice": [
                {
                    "question": "Vad skapar 'git init'?",
                    "options": ["Branch", "Commit", "Repository", "Remote"],
                    "correct": 2,
                    "explanation": "git init initierar ett nytt git-repository i mappen."
                },
                {
                    "question": "Var hamnar filer efter 'git add'?",
                    "options": ["Remote", "Staging area", "Branch", "Stash"],
                    "correct": 1,
                    "explanation": "git add flyttar ändringar till staging area."
                },
            ]
        },
        {
            "id": "git-branches",
            "title": "Branches",
            "flashcards": [
                {"front": "Vad gör 'git branch feature'?", "back": "Skapar ny branch 'feature'"},
                {"front": "Vad gör 'git checkout feature'?", "back": "Byter till branch 'feature'"},
                {"front": "Vad gör 'git checkout -b feature'?", "back": "Skapar och byter till ny branch"},
                {"front": "Vad gör 'git merge feature'?", "back": "Mergar feature-branch till current branch"},
                {"front": "Vad gör 'git branch -d feature'?", "back": "Tar bort branch (om merged)"},
            ],
            "multiple_choice": [
                {
                    "question": "Hur skapar och byter man till ny branch?",
                    "options": ["git branch -new", "git checkout -b", "git switch -c", "Både B och C"],
                    "correct": 3,
                    "explanation": "Både 'git checkout -b' och 'git switch -c' fungerar."
                },
                {
                    "question": "Vad händer vid merge conflict?",
                    "options": ["Auto-merge", "Git väljer en version", "Manuell fix krävs", "Merge avbryts permanent"],
                    "correct": 2,
                    "explanation": "Vid conflict måste du manuellt lösa och committa."
                },
            ]
        },
        {
            "id": "git-remote",
            "title": "Remote Repositories",
            "flashcards": [
                {"front": "Vad gör 'git push'?", "back": "Skickar commits till remote repository"},
                {"front": "Vad gör 'git pull'?", "back": "Hämtar och mergar ändringar från remote"},
                {"front": "Vad gör 'git fetch'?", "back": "Hämtar ändringar utan att merga"},
                {"front": "Vad gör 'git remote -v'?", "back": "Visar konfigurerade remote repositories"},
                {"front": "Vad är origin?", "back": "Default-namn för remote repository"},
            ],
            "multiple_choice": [
                {
                    "question": "Skillnad mellan pull och fetch?",
                    "options": ["Ingen skillnad", "Pull = fetch + merge", "Fetch = pull + rebase", "Pull är snabbare"],
                    "correct": 1,
                    "explanation": "git pull = git fetch + git merge."
                },
                {
                    "question": "Vad är 'origin' i git?",
                    "options": ["Första commit", "Main branch", "Default remote namn", "Lokalt repo"],
                    "correct": 2,
                    "explanation": "origin är konventionellt namn för primary remote."
                },
            ]
        },
        {
            "id": "git-history",
            "title": "History & Undo",
            "flashcards": [
                {"front": "Vad gör 'git log'?", "back": "Visar commit-historik"},
                {"front": "Vad gör 'git log --oneline'?", "back": "Kompakt vy med en rad per commit"},
                {"front": "Vad gör 'git reset HEAD~1'?", "back": "Ångrar senaste commit (behåller ändringar)"},
                {"front": "Vad gör 'git revert'?", "back": "Skapar ny commit som ångrar en specifik commit"},
                {"front": "Vad gör 'git stash'?", "back": "Sparar undan uncommitted ändringar temporärt"},
            ],
            "multiple_choice": [
                {
                    "question": "Skillnad mellan reset och revert?",
                    "options": ["Ingen skillnad", "Reset tar bort commit, revert skapar ny", "Revert är snabbare", "Reset är säkrare"],
                    "correct": 1,
                    "explanation": "Reset ändrar historik, revert skapar ny commit som ångrar."
                },
                {
                    "question": "När använder man 'git stash'?",
                    "options": ["För att radera ändringar", "Temporärt spara undan ändringar", "För att pusha", "För att skapa branch"],
                    "correct": 1,
                    "explanation": "Stash sparar ändringar temporärt så du kan byta branch."
                },
            ]
        },
        {
            "id": "git-rebase",
            "title": "Rebase & Advanced",
            "flashcards": [
                {"front": "Vad gör 'git rebase main'?", "back": "Flyttar commits ovanpå main (linjär historik)"},
                {"front": "Vad är interactive rebase?", "back": "git rebase -i - redigera, squash, reorder commits"},
                {"front": "Vad gör 'squash'?", "back": "Slår ihop flera commits till en"},
                {"front": "När INTE använda rebase?", "back": "På publika/delade branches"},
                {"front": "Vad gör 'git cherry-pick'?", "back": "Plockar specifik commit till current branch"},
            ],
            "multiple_choice": [
                {
                    "question": "Varför undvika rebase på publika branches?",
                    "options": ["Långsamt", "Skriver om historik som andra har", "Fungerar inte", "Tar bort filer"],
                    "correct": 1,
                    "explanation": "Rebase skriver om commit-hashar vilket skapar problem för andra."
                },
                {
                    "question": "Vad gör squash?",
                    "options": ["Tar bort commits", "Slår ihop commits", "Kopierar commits", "Flyttar commits"],
                    "correct": 1,
                    "explanation": "Squash kombinerar flera commits till en."
                },
            ]
        },
    ]
}
