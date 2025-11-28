# INTERACTIVE LEARNING ENGINE — Architecture Design

> Senior-level approach to building a real learning platform
> Not quick fixes — proper architecture

---

## Vision

Transform DevOpsHub from a "content display" platform to an **interactive learning environment** where students:

1. **Read** concepts with rich explanations
2. **Practice** in an embedded terminal
3. **Get validated** with automated checking
4. **Answer questions** to confirm understanding
5. **Progress** only when they truly understand

---

## Core Components

### 1. Task Structure (Enhanced)

Current task structure is too simple. We need:

```typescript
interface Task {
  id: string;
  moduleId: string;
  title: string;
  order: number;
  difficulty: 'beginner' | 'intermediate' | 'advanced';
  estimatedMinutes: number;
  xpReward: number;
  
  // NEW: Rich content blocks
  content: ContentBlock[];
  
  // NEW: Completion requirements
  requirements: CompletionRequirement[];
}

// Content is now an array of blocks, not just markdown
type ContentBlock = 
  | TextBlock 
  | CodeBlock 
  | TerminalBlock 
  | QuizBlock 
  | CheckpointBlock;

interface TextBlock {
  type: 'text';
  content: string; // Markdown
}

interface CodeBlock {
  type: 'code';
  language: string;
  code: string;
  filename?: string;
  highlightLines?: number[];
  explanation?: string; // Shown on hover or below
}

interface TerminalBlock {
  type: 'terminal';
  instructions: string;
  expectedCommands: ExpectedCommand[];
  hints?: string[];
  validationScript?: string;
}

interface ExpectedCommand {
  command: string;           // What user should type
  regex?: string;            // Alternative: regex pattern to match
  output?: string;           // Expected output (for display)
  explanation: string;       // Why this command
  allowVariations?: boolean; // Accept slight differences
}

interface QuizBlock {
  type: 'quiz';
  question: string;
  options: QuizOption[];
  explanation: string;       // Shown after answering
  xpBonus?: number;          // Extra XP for correct answer
}

interface QuizOption {
  text: string;
  isCorrect: boolean;
  feedback?: string;         // Shown if selected
}

interface CheckpointBlock {
  type: 'checkpoint';
  title: string;
  description: string;
  validationType: 'manual' | 'command' | 'file';
  validation?: {
    command?: string;        // Command to run for validation
    expectedOutput?: string; // What output indicates success
    fileToCheck?: string;    // File that should exist
  };
}
```

---

### 2. Terminal Integration

**Option A: Browser-based terminal emulator (Recommended for MVP)**

Use xterm.js to create a terminal UI that:
- Looks like a real terminal
- Accepts input
- Validates against expected commands
- Shows simulated output
- Provides hints if stuck

```typescript
// Frontend component
interface TerminalEmulator {
  expectedCommands: ExpectedCommand[];
  onCommandEntered: (cmd: string) => ValidationResult;
  onAllCommandsComplete: () => void;
}

interface ValidationResult {
  isCorrect: boolean;
  feedback: string;
  hint?: string;
  showExpected?: boolean;
}
```

**Option B: Real sandboxed environment (Future)**

For advanced labs, spin up actual containers:
- Use Docker-in-Docker or Firecracker
- Each student gets isolated environment
- Real command execution
- Automatic cleanup after session

**For MVP: Go with Option A** — simulated terminal that validates input.

---

### 3. Progress & Validation System

```typescript
interface TaskProgress {
  userId: string;
  taskId: string;
  status: 'not_started' | 'in_progress' | 'completed';
  
  // Track each block's completion
  blockProgress: {
    blockIndex: number;
    completed: boolean;
    attempts?: number;
    completedAt?: Date;
  }[];
  
  // Quiz answers
  quizAnswers: {
    blockIndex: number;
    selectedOption: number;
    isCorrect: boolean;
    answeredAt: Date;
  }[];
  
  // Terminal commands executed
  terminalHistory: {
    blockIndex: number;
    command: string;
    wasCorrect: boolean;
    timestamp: Date;
  }[];
  
  startedAt: Date;
  completedAt?: Date;
  totalTimeSpent: number; // seconds
  xpEarned: number;
}
```

---

### 4. Task Completion Flow

```
┌─────────────────────────────────────────────────────────┐
│                    TASK VIEW                             │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [TextBlock] Introduction to File Permissions            │
│  ─────────────────────────────────────────────          │
│  In Linux, every file has permissions that control...    │
│                                                          │
│  [CodeBlock] Permission notation                         │
│  ┌─────────────────────────────────────────────────┐    │
│  │ $ ls -la myfile.txt                             │    │
│  │ -rw-r--r-- 1 user group 1024 Nov 28 myfile.txt  │    │
│  │                                                  │    │
│  │ # -rw-r--r-- breaks down as:                    │    │
│  │ # - = regular file                              │    │
│  │ # rw- = owner can read+write                    │    │
│  │ # r-- = group can read                          │    │
│  │ # r-- = others can read                         │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  [TerminalBlock] Try it yourself                         │
│  ┌─────────────────────────────────────────────────┐    │
│  │ $ █                                              │    │
│  │                                                  │    │
│  │ Type: ls -la                                     │    │
│  └─────────────────────────────────────────────────┘    │
│  💡 Hint: List files with detailed permissions           │
│                                                          │
│  [QuizBlock] Quick check                                 │
│  ─────────────────────────────────────────────          │
│  What does 'rwx' mean for a user?                        │
│  ○ Read, write, execute                                  │
│  ○ Run, wait, exit                                       │
│  ○ Root, wheel, xorg                                     │
│                                                          │
│  [CheckpointBlock] ✓ Checkpoint                          │
│  ─────────────────────────────────────────────          │
│  You've learned the basics of file permissions!          │
│  XP Earned: +25                                          │
│                                                          │
│              [Continue to Next Section →]                │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

### 5. Example Task with New Structure

```json
{
  "id": "task-linux-permissions-01",
  "moduleId": "module-01-linux",
  "title": "Understanding File Permissions",
  "order": 3,
  "difficulty": "beginner",
  "estimatedMinutes": 25,
  "xpReward": 35,
  
  "content": [
    {
      "type": "text",
      "content": "# Understanding File Permissions\n\nIn Linux, every file and directory has **permissions** that control who can read, write, or execute it. This is fundamental to Linux security.\n\n## The Three Permission Types\n\n- **r** (read) — View file contents\n- **w** (write) — Modify file contents  \n- **x** (execute) — Run as a program"
    },
    {
      "type": "code",
      "language": "bash",
      "code": "$ ls -la myfile.txt\n-rw-r--r-- 1 user group 1024 Nov 28 myfile.txt",
      "explanation": "The -rw-r--r-- string shows permissions: owner (rw-), group (r--), others (r--)"
    },
    {
      "type": "terminal",
      "instructions": "Let's see permissions in action. Type the command to list files with details:",
      "expectedCommands": [
        {
          "command": "ls -la",
          "regex": "^ls\\s+(-la|-al|-l\\s+-a|-a\\s+-l).*$",
          "explanation": "ls -la shows all files (-a) with detailed info (-l)",
          "allowVariations": true
        }
      ],
      "hints": [
        "Use ls with flags for 'long' and 'all'",
        "The flags are -l and -a",
        "Try: ls -la"
      ]
    },
    {
      "type": "quiz",
      "question": "What permission does 'x' represent?",
      "options": [
        { "text": "Read", "isCorrect": false, "feedback": "That's 'r'. Try again!" },
        { "text": "Write", "isCorrect": false, "feedback": "That's 'w'. Try again!" },
        { "text": "Execute", "isCorrect": true, "feedback": "Correct! 'x' means execute — run as a program." },
        { "text": "Exit", "isCorrect": false, "feedback": "Not quite. 'x' is a permission type." }
      ],
      "explanation": "The 'x' permission allows a file to be run as a program or script.",
      "xpBonus": 5
    },
    {
      "type": "text", 
      "content": "## Changing Permissions with chmod\n\nThe `chmod` command changes permissions. You can use:\n\n- **Symbolic notation**: `chmod u+x file` (add execute for user)\n- **Numeric notation**: `chmod 755 file` (rwxr-xr-x)"
    },
    {
      "type": "code",
      "language": "bash",
      "code": "# Add execute permission for owner\nchmod u+x script.sh\n\n# Set to rwxr-xr-x (owner full, others read+execute)\nchmod 755 script.sh\n\n# Make file private (owner only)\nchmod 600 secret.txt",
      "explanation": "chmod modifies permissions. 'u' = user/owner, 'g' = group, 'o' = others, 'a' = all"
    },
    {
      "type": "terminal",
      "instructions": "Create a file and make it executable:",
      "expectedCommands": [
        {
          "command": "touch test.sh",
          "explanation": "Create an empty file called test.sh"
        },
        {
          "command": "chmod +x test.sh",
          "regex": "^chmod\\s+(\\+x|u\\+x|a\\+x|755|775|777)\\s+test\\.sh$",
          "explanation": "Add execute permission to the file",
          "allowVariations": true
        },
        {
          "command": "ls -la test.sh",
          "explanation": "Verify the permissions changed"
        }
      ],
      "hints": [
        "First create the file with 'touch'",
        "Then use 'chmod' to add execute permission",
        "Finally verify with 'ls -la'"
      ]
    },
    {
      "type": "quiz",
      "question": "What does chmod 600 do to a file?",
      "options": [
        { "text": "Makes it readable by everyone", "isCorrect": false },
        { "text": "Makes it executable", "isCorrect": false },
        { "text": "Makes it read+write for owner only", "isCorrect": true },
        { "text": "Deletes the file", "isCorrect": false }
      ],
      "explanation": "600 = rw------- (6=rw for owner, 0=nothing for group, 0=nothing for others)",
      "xpBonus": 5
    },
    {
      "type": "checkpoint",
      "title": "Permissions Mastered!",
      "description": "You now understand Linux file permissions and can modify them with chmod.",
      "validationType": "manual"
    }
  ],
  
  "requirements": [
    { "type": "all_terminals_complete" },
    { "type": "all_quizzes_answered" },
    { "type": "checkpoint_reached" }
  ]
}
```

---

## Implementation Plan

### Phase 1: Data Structure (Backend)

```
1. Update Task model to support content blocks
2. Create migration for new structure
3. Update seed scripts with rich content
4. Create API endpoints for progress tracking per block
```

### Phase 2: Terminal Component (Frontend)

```
1. Install xterm.js: npm install xterm xterm-addon-fit
2. Create TerminalEmulator component
3. Implement command validation logic
4. Add hint system
5. Style to match dark theme
```

### Phase 3: Content Blocks Renderer (Frontend)

```
1. Create ContentBlockRenderer component
2. Implement TextBlock (markdown)
3. Implement CodeBlock (syntax highlighting + comments)
4. Implement TerminalBlock (interactive)
5. Implement QuizBlock (multiple choice)
6. Implement CheckpointBlock (progress marker)
```

### Phase 4: Progress Tracking

```
1. Track block-level completion
2. Save terminal command history
3. Save quiz answers
4. Calculate XP including bonuses
5. Show progress bar per task
```

### Phase 5: Content Creation

```
1. Create content for Module 01 (all tasks with blocks)
2. Create content for Module 02
3. Continue for all 15 modules
```

---

## Prompt for Opus: Phase 1

```
INTERACTIVE LEARNING ENGINE — Phase 1: Backend Data Structure

We're rebuilding the task system to support interactive learning.

1. UPDATE Task model (apps/backend/src/models/Task.ts):

Replace simple 'content: string' with structured content blocks:

interface ContentBlock {
  type: 'text' | 'code' | 'terminal' | 'quiz' | 'checkpoint';
  // Type-specific fields...
}

interface Task {
  // existing fields...
  content: ContentBlock[]; // Array of blocks instead of string
  requirements: CompletionRequirement[];
}

2. CREATE TaskProgress model:

Track per-block completion:
- blockProgress: which blocks completed
- quizAnswers: quiz responses
- terminalHistory: commands entered
- timeSpent: seconds in task

3. CREATE API endpoints:

POST /api/tasks/:taskId/progress
- Update block completion
- Record quiz answer
- Record terminal command

GET /api/tasks/:taskId/progress
- Get user's progress on task

4. UPDATE task completion logic:
- Task is complete when ALL requirements met
- Requirements: all_terminals_complete, all_quizzes_answered, checkpoint_reached

Do NOT create content yet — just the data structure.

COMMIT: feat(tasks): implement content blocks data structure
```

---

## Prompt for Opus: Phase 2

```
INTERACTIVE LEARNING ENGINE — Phase 2: Terminal Component

Create an interactive terminal emulator for practicing commands.

1. INSTALL dependencies:
cd apps/frontend
npm install xterm @xterm/xterm @xterm/addon-fit

2. CREATE TerminalEmulator component:
Location: apps/frontend/src/components/learning/TerminalEmulator.tsx

Features:
- Looks like real terminal (dark background, monospace font)
- Shows prompt: $ 
- Accepts user input
- Validates against expectedCommands
- Shows feedback (correct/incorrect)
- Displays hints after failed attempts
- Shows simulated output for correct commands
- Tracks completion

Props:
- expectedCommands: array of commands to complete
- hints: array of hint strings
- onComplete: callback when all commands done
- onCommandEntered: callback for each command

3. STYLING:
- Match dark theme
- Green text for correct
- Red for incorrect
- Yellow for hints
- Monospace font throughout

4. TEST with simple example:
Create a test page that shows terminal expecting "ls -la"

COMMIT: feat(terminal): create interactive terminal emulator component
```

---

## Prompt for Opus: Phase 3

```
INTERACTIVE LEARNING ENGINE — Phase 3: Content Block Renderer

Create components to render each content block type.

1. CREATE ContentBlockRenderer:
Location: apps/frontend/src/components/learning/ContentBlockRenderer.tsx

Switch on block.type and render appropriate component.

2. CREATE TextBlock component:
- Render markdown with react-markdown
- Support headers, lists, bold, italic, links
- Syntax highlighting for inline code

3. CREATE CodeBlock component:
- Syntax highlighting with react-syntax-highlighter
- Show filename if provided
- Highlight specific lines if specified
- Show explanation below or on hover
- Copy button

4. CREATE QuizBlock component:
- Show question
- Radio buttons for options
- Submit button
- Show feedback after answer
- Show explanation
- Track if answered correctly
- Award bonus XP

5. CREATE CheckpointBlock component:
- Celebratory design
- Show XP earned
- Confetti animation (optional)
- "Continue" button

6. UPDATE task detail page:
- Map over task.content
- Render each block
- Track completion per block
- Show progress indicator

COMMIT: feat(learning): create content block renderer components
```

---

## Clean Data Prompt

```
CLEAN ALL MOCK DATA

Remove all fake/seed progress data:

1. CREATE cleanup endpoint:
POST /api/admin/cleanup-mock-data

This should:
- Delete ALL TaskCompletion records
- Delete ALL StudySession records  
- Reset ALL users to: xp=0, level=1, streak=0
- Keep user accounts and modules/tasks

2. RUN cleanup on your account:
Remove the fake "Recent Sessions" data showing 2h, 4 tasks, 305 XP

3. ENSURE new users start clean:
- No pre-populated progress
- No fake sessions
- XP = 0, Level = 1

4. UPDATE seed script:
- ONLY seed modules, tasks, content
- Do NOT seed any user progress
- Do NOT seed fake sessions

COMMIT: fix(data): remove all mock progress data
```

---

## Summary

This architecture gives you:

✅ **Rich content** — Not just markdown, but interactive blocks
✅ **Terminal practice** — Type commands, get validated
✅ **Quizzes** — Confirm understanding before moving on
✅ **Progress tracking** — Per-block completion
✅ **Real learning** — Students actually DO things, not just read

It's more work upfront, but creates a **real learning platform** instead of a glorified documentation site.

Want me to create the prompts for Opus to start implementing this?
