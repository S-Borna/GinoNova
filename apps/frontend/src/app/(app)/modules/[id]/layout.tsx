"use client"

/**
 * ============================================================================
 * MODULE LAYOUT — Clean layout with Bookmark Sidebar
 * ============================================================================
 *
 * Features:
 * - Full-width content area for module tasks/cards
 * - ⭐ Bookmark sidebar on the right (PROMPT 4)
 * - Mobile bookmark button when bookmarks exist
 *
 * @phase FAS 2.1 - Module layout
 */

import * as React from "react"
import { useState } from "react"
import { X, Star } from "lucide-react"
import { useBookmarks } from "@/hooks/useBookmarks"
import { BookmarkSidebar } from "@/components/modules/BookmarkSidebar"

interface ModuleLayoutProps {
  children: React.ReactNode
}

export default function ModuleLayout({ children }: ModuleLayoutProps) {
  const [bookmarkSidebarOpen, setBookmarkSidebarOpen] = useState(false)
  const { count: bookmarkCount } = useBookmarks()

  return (
    <div className="flex min-h-screen bg-gray-950">
      {/* Main Content - Full width, margin for right bookmark sidebar */}
      <main className="flex-1 min-w-0 lg:mr-72">
        {children}
      </main>

      {/* Bookmark Sidebar (Right Side) - Desktop */}
      <aside className="hidden lg:flex lg:flex-col fixed top-0 right-0 h-screen w-72 bg-gray-900/95 backdrop-blur-sm border-l border-gray-800">
        <BookmarkSidebar className="flex-1" />
      </aside>

      {/* Mobile Bookmark Button */}
      {bookmarkCount > 0 && (
        <button
          onClick={() => setBookmarkSidebarOpen(!bookmarkSidebarOpen)}
          className="fixed bottom-4 right-4 z-50 lg:hidden p-3 bg-amber-500 rounded-full shadow-lg"
        >
          <Star className="w-6 h-6 text-white fill-white" />
          <span className="absolute -top-1 -right-1 w-5 h-5 text-[10px] font-bold bg-white text-amber-600 rounded-full flex items-center justify-center">
            {bookmarkCount > 9 ? '9+' : bookmarkCount}
          </span>
        </button>
      )}

      {/* Mobile Bookmark Overlay */}
      {bookmarkSidebarOpen && (
        <div
          className="fixed inset-0 bg-black/50 z-40 lg:hidden"
          onClick={() => setBookmarkSidebarOpen(false)}
        />
      )}

      {/* Mobile Bookmark Sidebar */}
      <aside className={`fixed top-0 right-0 h-screen w-72 bg-gray-900 border-l border-gray-800 transform transition-transform duration-300 ease-in-out z-50 lg:hidden ${bookmarkSidebarOpen ? 'translate-x-0' : 'translate-x-full'} flex flex-col`}>
        <div className="flex items-center justify-between p-4 border-b border-gray-800">
          <div className="flex items-center gap-2">
            <Star className="w-4 h-4 text-amber-400 fill-amber-400" />
            <span className="text-sm font-semibold text-white">Bookmarks</span>
          </div>
          <button onClick={() => setBookmarkSidebarOpen(false)} className="p-1 rounded hover:bg-gray-800">
            <X className="w-5 h-5 text-gray-400" />
          </button>
        </div>
        <BookmarkSidebar className="flex-1" />
      </aside>
    </div>
  )
}
