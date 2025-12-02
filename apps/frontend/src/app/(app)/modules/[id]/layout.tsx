"use client"

/**
 * ============================================================================
 * MODULE LAYOUT — Premium Layout with Right Sidebar
 * ============================================================================
 *
 * Features:
 * - Full-width content area for module tasks/cards
 * - ⭐ Premium Right Sidebar with Bookmarks & Task Reminders
 * - Mobile support with slide-out sidebar
 *
 * @phase Premium Upgrade Phase 2
 */

import * as React from "react"
import { useState } from "react"
import { X, Star, Sparkles } from "lucide-react"
import { useBookmarks } from "@/hooks/useBookmarks"
import { RightSidebar } from "@/components/modules/RightSidebar"

interface ModuleLayoutProps {
  children: React.ReactNode
}

export default function ModuleLayout({ children }: ModuleLayoutProps) {
  const [sidebarOpen, setSidebarOpen] = useState(false)
  const { count: bookmarkCount } = useBookmarks()

  return (
    <div className="flex min-h-screen bg-zinc-950">
      {/* Main Content - Full width, margin for right sidebar */}
      <main className="flex-1 min-w-0 lg:mr-72">
        {children}
      </main>

      {/* Right Sidebar - Desktop */}
      <aside className="hidden lg:flex lg:flex-col fixed top-0 right-0 h-screen w-72 border-l border-zinc-800/60">
        <RightSidebar className="flex-1" />
      </aside>

      {/* Mobile Quick Access Button */}
      <button
        onClick={() => setSidebarOpen(!sidebarOpen)}
        className="fixed bottom-4 right-4 z-50 lg:hidden p-3 bg-gradient-to-r from-purple-600 to-purple-500 rounded-full shadow-lg shadow-purple-500/25 hover:shadow-purple-500/40 transition-all"
      >
        <Sparkles className="w-6 h-6 text-white" />
        {bookmarkCount > 0 && (
          <span className="absolute -top-1 -right-1 w-5 h-5 text-[10px] font-bold bg-amber-500 text-white rounded-full flex items-center justify-center">
            {bookmarkCount > 9 ? '9+' : bookmarkCount}
          </span>
        )}
      </button>

      {/* Mobile Overlay */}
      {sidebarOpen && (
        <div
          className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 lg:hidden"
          onClick={() => setSidebarOpen(false)}
        />
      )}

      {/* Mobile Right Sidebar */}
      <aside className={`fixed top-0 right-0 h-screen w-72 border-l border-zinc-800/60 transform transition-transform duration-300 ease-in-out z-50 lg:hidden ${sidebarOpen ? 'translate-x-0' : 'translate-x-full'} flex flex-col`}>
        <div className="flex items-center justify-between p-4 border-b border-zinc-800/60 bg-zinc-900">
          <div className="flex items-center gap-2">
            <Sparkles className="w-4 h-4 text-purple-400" />
            <span className="text-sm font-semibold text-white">Quick Access</span>
          </div>
          <button onClick={() => setSidebarOpen(false)} className="p-1 rounded hover:bg-zinc-800">
            <X className="w-5 h-5 text-zinc-400" />
          </button>
        </div>
        <RightSidebar className="flex-1" />
      </aside>
    </div>
  )
}
