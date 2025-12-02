# Design Backup - Version 1.0 (Pre-Enterprise Redesign)

**Date:** 2024-12-02
**Status:** Working Production Design
**Purpose:** Full backup before Level 5 Enterprise redesign

---

## Files Backed Up

1. `dashboard_page.tsx` - Main dashboard page
2. `DashboardHero.tsx` - Hero greeting section
3. `StatsRow.tsx` - Stats cards row
4. `QuickActions.tsx` - Quick action buttons
5. `ModulesOverview.tsx` - Learning path grid
6. `XPProgress.tsx` - XP ring component
7. `RecentActivity.tsx` - Activity timeline
8. `Sidebar.tsx` - Desktop navigation
9. `TopBar.tsx` - Header with search & user
10. `AppLayoutClient.tsx` - Main layout wrapper
11. `AIWizardFAB.tsx` - AI chat floating button

---

## Design Characteristics

### Color Palette

- Primary: Indigo (#6366f1) to Purple (#8b5cf6)
- Success: Emerald (#22c55e)
- Warning: Amber/Orange (#f97316)
- Background: White / Neutral-900 (dark)
- Cards: White / Neutral-800 (dark)

### Typography

- Font: Default system stack
- Headings: font-bold, text-2xl
- Body: text-sm, text-neutral-500

### Spacing

- Cards: p-6, rounded-xl
- Gaps: gap-4, gap-6
- Sections: space-y-8

### Effects

- Cards: shadow-sm, hover:shadow-md
- Hover: -translate-y-0.5
- Animation: animate-fade-in-up
- Backdrop: backdrop-blur-xl on sidebars

---
