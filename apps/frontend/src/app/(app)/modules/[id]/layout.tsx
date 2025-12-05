"use client"

/**
 * ============================================================================
 * MODULE LAYOUT — Clean Layout without Sidebar
 * ============================================================================
 *
 * Camp DevOps module detail page - clean, full-width layout
 * matching SkillsMaps design for consistency.
 *
 * @phase Design Unification
 */

interface ModuleLayoutProps {
  children: React.ReactNode
}

export default function ModuleLayout({ children }: ModuleLayoutProps) {
  return (
    <div className="min-h-screen bg-zinc-950">
      <main className="flex-1">
        {children}
      </main>
    </div>
  )
}
