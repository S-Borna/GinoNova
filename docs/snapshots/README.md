# Documentation Snapshots

This folder contains visual snapshots of the application at different stages of development.

## How to Take Snapshots

### Option 1: Manual Screenshots (Recommended)

1. Open the app at <http://localhost:3000>
2. Use **Cmd + Shift + 4** to capture specific areas
3. Save screenshots to `docs/snapshots/YYYY-MM-DD/`

### Option 2: Full Page Screenshots in Chrome

1. Open DevTools (Cmd + Option + I)
2. Open Command Palette (Cmd + Shift + P)
3. Type "Capture full size screenshot"
4. Save to this folder

### Option 3: Automated Script

```bash
# Install playwright first (one-time)
npx playwright install chromium

# Run snapshot script
node scripts/take-snapshots.mjs
```

## Naming Convention

```
XX-page-name[-variant].png

Examples:
01-landing.png
02-landing-dark.png
03-dashboard.png
04-module-detail.png
05-task-with-code.png
```

## Key Pages to Document

| # | Page | Path | Notes |
|---|------|------|-------|
| 01 | Landing | `/` | Hero, features |
| 02 | Dashboard | `/dashboard` | Stats, progress |
| 03 | Modules List | `/modules` | All modules |
| 04 | Module Detail | `/modules/[id]` | Tasks list |
| 05 | Task/Lesson | `/modules/[id]/tasks/[taskId]` | Markdown content, code blocks |
| 06 | Profile | `/profile` | User info, stats |
| 07 | Settings | `/settings` | Theme toggle |
| 08 | Sidebar | - | Light & dark mode |

## Snapshot History

### 2025-11-28 - Round 1 Feedback Fixes

- ✅ Syntax highlighting in code blocks
- ✅ Hero cleanup (removed dots, badge)
- ✅ Breadcrumbs show names instead of UUIDs
- ✅ Real task content from seed data
