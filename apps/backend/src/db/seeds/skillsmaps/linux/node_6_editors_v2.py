"""
Linux Mastery Node 6: Text Editors - V2 Interactive Format
"""

LINUX_NODE_6_EDITORS_V2 = {
    "node_id": 6,
    "title": "Text Editors - Vim & Nano",
    "slug": "text-editors",
    "description": "Editera filer direkt i terminalen",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Text Editors",
            "content": {
                "headline": "SSH kräver terminal-editorer",
                "hook": "När du är inloggad på en server via SSH finns ingen grafisk editor. Vim och Nano är dina vapen - lär dig åtminstone en av dem.",
                "learning_objectives": [
                    "Grundläggande Nano för snabba editeringar",
                    "Vim modes: Normal, Insert, Command, Visual",
                    "Navigera, söka, ersätta i Vim",
                    "Konfigurera editors med .vimrc/.nanorc"
                ],
                "prerequisites": ["Terminal basics"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Editor Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Vim Modes",
                        "explanation": "NORMAL (navigera, default), INSERT (skriv text, i/a/o), COMMAND (:kommandon), VISUAL (markera, v/V).",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ VIM MODES                                   │
├─────────────────────────────────────────────┤
│ NORMAL  │ Start här. ESC tar dig tillbaka.│
│    ↓ i  │                                  │
│ INSERT  │ Skriv text. ESC för att gå ut.  │
│    ↓ ESC → :                               │
│ COMMAND │ :w :q :wq :s/old/new/g          │
│    ↓ v  │                                  │
│ VISUAL  │ Markera text med hjkl           │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "ESC ESC (dubbel-escape) tar dig alltid till NORMAL mode.",
                        "common_mistake": "Att skriva i NORMAL mode - tecken blir kommandon!"
                    },
                    {
                        "title": "Vim Survival Kit",
                        "explanation": ":q! (avsluta utan spara), :wq (spara och avsluta), i (insert mode), ESC (normal mode), dd (ta bort rad), u (undo).",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ VIKTIGASTE KOMMANDON                        │
├─────────────────────────────────────────────┤
│ :q!  │ Avsluta UTAN att spara (nödutgång)│
│ :wq  │ Spara och avsluta                  │
│ i    │ Insert mode före cursor            │
│ ESC  │ Tillbaka till normal mode          │
│ dd   │ Ta bort hela raden                 │
│ u    │ Ångra (undo)                       │
│ /text│ Sök efter 'text'                   │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "ZZ (shift+z två gånger) är snabbaste sättet att spara och avsluta.",
                        "common_mistake": "Att panika när man är fast i Vim. ESC :q! tar dig ut!"
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Editors",
            "content": {
                "exercises": [
                    {
                        "task": "Öppna och avsluta Vim",
                        "instruction": "Öppna test.txt i vim, gå till insert mode, skriv 'Hello', spara och avsluta",
                        "expected_command": "vim test.txt → i → Hello → ESC → :wq",
                        "hint": "i = insert, ESC = normal, :wq = write & quit"
                    },
                    {
                        "task": "Sök och ersätt i Vim",
                        "instruction": "Ersätt alla 'foo' med 'bar' i filen",
                        "expected_command": ":%s/foo/bar/g",
                        "hint": "% = hela filen, g = global (alla på varje rad)"
                    },
                    {
                        "task": "Snabbedit med Nano",
                        "instruction": "Öppna config.conf, editera, spara och avsluta",
                        "expected_command": "nano config.conf → edit → Ctrl+O → Enter → Ctrl+X",
                        "hint": "^O = save (Write Out), ^X = exit"
                    },
                    {
                        "task": "Gå till specifik rad i Vim",
                        "instruction": "Öppna fil och gå direkt till rad 50",
                        "expected_command": "vim +50 file.txt",
                        "hint": "+N öppnar på rad N"
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
                        {"front": "Hur avslutar du Vim utan att spara?", "back": ":q! (quit force, ignorera ändringar)"},
                        {"front": "Vad gör dd i Vim?", "back": "Tar bort hela raden (delete line)"},
                        {"front": "Vilken tangent tar dig till INSERT mode?", "back": "i (insert före cursor), a (append efter), o (ny rad under)"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilket Vim-kommando ersätter alla förekomster i filen?",
                            "options": [":s/old/new/", ":s/old/new/g", ":%s/old/new/g", ":/old/new/g"],
                            "correct": 2,
                            "explanation": "% = hela filen, s = substitute, g = global"
                        },
                        {
                            "question": "Hur sparar du i Nano?",
                            "options": ["Ctrl+S", "Ctrl+W", "Ctrl+O", ":w"],
                            "correct": 2,
                            "explanation": "Ctrl+O (Write Out) sparar filen i Nano"
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
            "title": "Editor Challenge",
            "content": {
                "scenario": "Editera en nginx config-fil för att fixa en bugg.",
                "requirements": [
                    "Öppna /etc/nginx/nginx.conf med vim",
                    "Sök efter 'worker_connections'",
                    "Ändra värdet från 768 till 1024",
                    "Spara och avsluta"
                ],
                "hints": [
                    "/worker_connections för att söka",
                    "ciw för att ändra ett ord (change inner word)",
                    ":wq för att spara och avsluta"
                ],
                "solution": """# Metod 1: Interaktiv
sudo vim /etc/nginx/nginx.conf
/worker_connections     # Sök
n                       # Nästa träff om behövs
ciw1024                 # Change inner word till 1024
ESC :wq                 # Spara och avsluta

# Metod 2: One-liner med sed
sudo sed -i 's/worker_connections 768/worker_connections 1024/' /etc/nginx/nginx.conf

# Verifiera
grep worker_connections /etc/nginx/nginx.conf""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
