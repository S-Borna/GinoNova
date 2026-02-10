# CLAUDE.md — Enterprise Quality Standards

## Identity

You are building a **paid, enterprise-grade product**. Every file, function, and commit must reflect that standard. If it wouldn't pass a senior engineer's code review, don't ship it.

---

## Pre-Action Protocol (BEFORE writing any code)

1. **Confirm requirements** — If the user hasn't specified a tech stack, ASK. Never assume.
2. **Confirm structure** — If creating more than 3 files, propose the structure first.
3. **Scope check** — Restate what you're about to do in one sentence. If you can't, the task isn't clear enough.
4. **Run `guardian_pre_action`** if the MCP server is available.

---

## Code Quality Standards (DURING implementation)

### Absolute Prohibitions
- ❌ **No heredoc** (`<< EOF`) — Use template files or multi-line strings
- ❌ **No hardcoded secrets** — Use environment variables via `.env`
- ❌ **No `eval()` or `exec()`** — Use safe alternatives
- ❌ **No wildcard imports** (`from x import *`) — Import explicitly
- ❌ **No `any`/`Any` types** — Use explicit typing always
- ❌ **No `console.log`/`print()` in production** — Use structured logging
- ❌ **No magic numbers** — Extract to named constants
- ❌ **No nested ternaries** — Use if/else or helper functions
- ❌ **No TODO/HACK/FIXME** in committed code — Resolve or create an issue

### Required Practices
- ✅ **Type everything** — Full type annotations on all functions and variables
- ✅ **Error handling** — Every external call wrapped in try/catch with specific error types
- ✅ **Validate inputs** — Use Pydantic (Python) or Zod (TypeScript) for all inputs
- ✅ **DRY** — If you write similar logic twice, extract it
- ✅ **Constants** — UPPER_CASE at module level, never inline
- ✅ **Docstrings** — Every public function and class
- ✅ **Small functions** — Max ~40 lines per function. If longer, split.

---

## Repository Structure Standards

### Required Files (every project)
```
README.md           — What it does, how to run it, how to deploy
.gitignore          — Language-appropriate ignores
.env.example        — All required env vars documented
```

### Recommended Structure
```
project-root/
├── src/              or  app/          — Source code (NEVER in root)
│   ├── config/                         — Configuration
│   ├── services/                       — Business logic
│   ├── utils/                          — Shared utilities
│   └── types/                          — Type definitions
├── tests/                              — Mirror src/ structure
├── docs/                               — Extended documentation
├── scripts/                            — Build/deploy scripts
├── .github/workflows/                  — CI/CD pipelines
├── docker-compose.yml                  — Dev environment
├── CHANGELOG.md                        — Version history
└── LICENSE                             — Legal clarity
```

### Naming Conventions
- **Files**: `snake_case.py` or `kebab-case.ts` — pick ONE per project and stick to it
- **Directories**: always `lowercase` or `kebab-case`
- **No spaces, no uppercase** in file or directory names
- **Max 5 levels** of directory nesting

---

## Post-Action Protocol (AFTER completing work)

1. **Self-review** — Read every file you touched. Does it meet the standards above?
2. **Run `guardian_post_action`** if the MCP server is available.
3. **Check for drift** — Did you add anything the user didn't ask for? Remove it.
4. **Verify it runs** — `npm run build`, `python -m py_compile`, or equivalent. Broken code is never acceptable.
5. **No orphans** — Every file should be imported/used somewhere. Dead code = technical debt.

---

## Enterprise Mindset

- Every output should be **deployable as-is** to production
- Think about **the next developer** who reads this code
- **Fewer files, better organized** beats many scattered files
- **Explicit is always better than implicit**
- If a symptom fix is tempting, find and fix the **root cause** instead
- Never commit code you wouldn't put your name on

---

## Quick Decision Framework

| Situation | Action |
|---|---|
| User didn't specify stack | ASK, don't assume |
| Tempted to use heredoc | Use a template file |
| Writing a "quick fix" | Find the root cause |
| File getting long | Split by responsibility |
| Adding a dependency | Justify it — is it truly needed? |
| Test failing | Fix the code, never the test (unless test is wrong) |
| Unsure about structure | Propose it before building |
