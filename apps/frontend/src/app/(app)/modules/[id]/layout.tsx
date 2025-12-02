"use client"

/**
 * ============================================================================
 * MODULE LAYOUT — Sidebar Navigation for Tasks + Bookmark System
 * ============================================================================
 *
 * Features:
 * - Left sidebar with task list
 * - Progress indicators per task
 * - Current task highlighting
 * - Collapsible on mobile
 * - Module header with progress
 * - ⭐ Bookmark sidebar for saved tasks (PROMPT 4)
 * - ⭐ Star button on each task to bookmark
 *
 * @phase FAS 2.1 - Task layout with sidebar navigation
 * @location apps/frontend/src/app/(app)/modules/[id]/layout.tsx
 */

import * as React from "react"
import { useState, useEffect } from "react"
import { useParams, usePathname } from "next/navigation"
import Link from "next/link"
import {
  CheckCircle2,
  Circle,
  ChevronLeft,
  ChevronRight,
  BookOpen,
  FlaskConical,
  FolderKanban,
  Clock,
  Menu,
  X,
  Star,
  Bookmark
} from "lucide-react"
import { useBookmarks } from "@/hooks/useBookmarks"
import { BookmarkSidebar } from "@/components/modules/BookmarkSidebar"

/* ============================================================================
   TYPES
   ============================================================================ */

interface Task {
  id: string
  title: string
  type: 'lesson' | 'exercise' | 'quiz'
  order_index: number
  xp_reward: number
  is_completed?: boolean
}

interface Lab {
  id: string
  title: string
  estimated_hours: number
  is_completed?: boolean
}

interface Module {
  id: string
  name: string
  slug: string
  description?: string
  tasks: Task[]
  labs: Lab[]
  project?: {
    id: string
    title: string
    is_completed?: boolean
  }
}

interface ModuleLayoutProps {
  children: React.ReactNode
}

/* ============================================================================
   SIDEBAR COMPONENT
   ============================================================================ */

function TaskSidebar({
  module,
  currentPath,
  isOpen,
  onClose,
  isBookmarked,
  toggleBookmark
}: {
  module: Module | null
  currentPath: string
  isOpen: boolean
  onClose: () => void
  isBookmarked: (taskId: string) => boolean
  toggleBookmark: (taskId: string) => Promise<boolean>
}) {
  if (!module) return null

  // Defensive: ensure tasks and labs are arrays
  const tasks = module.tasks || []
  const labs = module.labs || []

  const completedTasks = tasks.filter(t => t.is_completed).length
  const totalTasks = tasks.length
  const progressPercent = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0

  return (
    <>
      {/* Mobile Overlay */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/50 z-40 lg:hidden"
          onClick={onClose}
        />
      )}

      {/* Sidebar */}
      <aside className={`
        fixed lg:sticky top-0 left-0 h-screen w-72
        bg-gray-900 border-r border-gray-800
        flex flex-col overflow-hidden
        transform transition-transform duration-300 ease-in-out
        z-50 lg:z-auto
        ${isOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'}
      `}>
        {/* Header */}
        <div className="p-4 border-b border-gray-800">
          <div className="flex items-center justify-between mb-3">
            <Link
              href="/modules"
              className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors"
            >
              <ChevronLeft className="w-4 h-4" />
              <span className="text-sm">All Modules</span>
            </Link>
            <button
              onClick={onClose}
              className="lg:hidden p-1 rounded hover:bg-gray-800"
            >
              <X className="w-5 h-5 text-gray-400" />
            </button>
          </div>

          <h2 className="font-semibold text-white truncate">{module.name}</h2>

          {/* Progress Bar */}
          <div className="mt-3">
            <div className="flex items-center justify-between text-xs text-gray-500 mb-1">
              <span>{completedTasks}/{totalTasks} tasks</span>
              <span>{progressPercent}%</span>
            </div>
            <div className="h-1.5 bg-gray-800 rounded-full overflow-hidden">
              <div
                className="h-full bg-gradient-to-r from-indigo-500 to-purple-500 transition-all duration-500"
                style={{ width: `${progressPercent}%` }}
              />
            </div>
          </div>
        </div>

        {/* Task List */}
        <nav className="flex-1 overflow-y-auto py-2">
          {/* Tasks Section */}
          <div className="px-3 mb-4">
            <div className="flex items-center gap-2 px-2 py-2 text-xs font-medium text-gray-500 uppercase tracking-wider">
              <BookOpen className="w-3.5 h-3.5" />
              <span>Lessons & Tasks</span>
            </div>

            <ul className="space-y-0.5">
              {tasks.length === 0 ? (
                <li className="px-3 py-2 text-sm text-gray-500">
                  No tasks loaded yet...
                </li>
              ) : (
                tasks.map((task, index) => {
                  const taskPath = `/modules/${module.slug}/tasks/${task.id}`
                  const isActive = currentPath === taskPath
                  const bookmarked = isBookmarked(task.id)

                  return (
                    <li key={task.id} className="group relative">
                      <Link
                        href={taskPath}
                        onClick={onClose}
                        className={`
                          flex items-center gap-3 px-3 py-2.5 rounded-lg
                          transition-all duration-150
                          ${isActive
                            ? 'bg-indigo-500/10 border-l-2 border-indigo-500 text-white'
                            : 'hover:bg-gray-800/50 text-gray-400 hover:text-white border-l-2 border-transparent'
                          }
                        `}
                      >
                        {/* Status Icon */}
                        <div className="flex-shrink-0">
                          {task.is_completed ? (
                            <CheckCircle2 className="w-4 h-4 text-green-400" />
                          ) : (
                            <Circle className={`w-4 h-4 ${isActive ? 'text-indigo-400' : 'text-gray-600'}`} />
                          )}
                        </div>

                        {/* Task Info */}
                        <div className="flex-1 min-w-0">
                          <div className={`text-sm truncate ${isActive ? 'font-medium' : ''}`}>
                            {index + 1}. {task.title}
                          </div>
                        </div>

                        {/* XP Badge */}
                        <span className="flex-shrink-0 text-xs text-gray-600">
                          +{task.xp_reward}
                        </span>
                      </Link>

                      {/* ⭐ Bookmark Star Button */}
                      <button
                        onClick={(e) => {
                          e.preventDefault()
                          e.stopPropagation()
                          toggleBookmark(task.id)
                        }}
                        className={`
                          absolute right-2 top-1/2 -translate-y-1/2
                          p-1 rounded transition-all duration-200
                          ${bookmarked
                            ? 'opacity-100'
                            : 'opacity-0 group-hover:opacity-100'
                          }
                          hover:bg-gray-700
                        `}
                        title={bookmarked ? 'Remove bookmark' : 'Add bookmark'}
                      >
                        <Star
                          className={`w-3.5 h-3.5 transition-colors ${bookmarked
                              ? 'fill-amber-400 text-amber-400'
                              : 'text-gray-500 hover:text-amber-400'
                            }`}
                        />
                      </button>
                    </li>
                  )
                })
              )}
            </ul>
          </div>

          {/* Labs Section */}
          {labs.length > 0 && (
            <div className="px-3 mb-4">
              <div className="flex items-center gap-2 px-2 py-2 text-xs font-medium text-gray-500 uppercase tracking-wider">
                <FlaskConical className="w-3.5 h-3.5" />
                <span>Hands-on Labs</span>
              </div>

              <ul className="space-y-0.5">
                {labs.map((lab) => {
                  const labPath = `/modules/${module.slug}/labs/${lab.id}`
                  const isActive = currentPath === labPath

                  return (
                    <li key={lab.id}>
                      <Link
                        href={labPath}
                        onClick={onClose}
                        className={`
                          flex items-center gap-3 px-3 py-2.5 rounded-lg
                          transition-all duration-150
                          ${isActive
                            ? 'bg-orange-500/10 border-l-2 border-orange-500 text-white'
                            : 'hover:bg-gray-800/50 text-gray-400 hover:text-white border-l-2 border-transparent'
                          }
                        `}
                      >
                        {lab.is_completed ? (
                          <CheckCircle2 className="w-4 h-4 text-green-400" />
                        ) : (
                          <FlaskConical className={`w-4 h-4 ${isActive ? 'text-orange-400' : 'text-gray-600'}`} />
                        )}
                        <div className="flex-1 min-w-0">
                          <div className={`text-sm truncate ${isActive ? 'font-medium' : ''}`}>
                            {lab.title}
                          </div>
                        </div>
                        <div className="flex items-center gap-1 text-xs text-gray-600">
                          <Clock className="w-3 h-3" />
                          {lab.estimated_hours}h
                        </div>
                      </Link>
                    </li>
                  )
                })}
              </ul>
            </div>
          )}

          {/* Project Section */}
          {module.project && (
            <div className="px-3">
              <div className="flex items-center gap-2 px-2 py-2 text-xs font-medium text-gray-500 uppercase tracking-wider">
                <FolderKanban className="w-3.5 h-3.5" />
                <span>Capstone Project</span>
              </div>

              <Link
                href={`/modules/${module.slug}/project`}
                onClick={onClose}
                className={`
                  flex items-center gap-3 px-3 py-2.5 rounded-lg
                  transition-all duration-150
                  ${currentPath.includes('/project')
                    ? 'bg-purple-500/10 border-l-2 border-purple-500 text-white'
                    : 'hover:bg-gray-800/50 text-gray-400 hover:text-white border-l-2 border-transparent'
                  }
                `}
              >
                {module.project.is_completed ? (
                  <CheckCircle2 className="w-4 h-4 text-green-400" />
                ) : (
                  <FolderKanban className="w-4 h-4 text-purple-400" />
                )}
                <span className="text-sm truncate">{module.project.title}</span>
              </Link>
            </div>
          )}
        </nav>

        {/* Footer */}
        <div className="p-4 border-t border-gray-800">
          <div className="flex items-center justify-between text-sm">
            <span className="text-gray-500">Module Progress</span>
            <span className="text-white font-medium">{progressPercent}%</span>
          </div>
        </div>
      </aside>
    </>
  )
}

/* ============================================================================
   MAIN LAYOUT
   ============================================================================ */

export default function ModuleLayout({ children }: ModuleLayoutProps) {
  const params = useParams()
  const pathname = usePathname()
  const [module, setModule] = useState<Module | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [sidebarOpen, setSidebarOpen] = useState(false)
  const [bookmarkSidebarOpen, setBookmarkSidebarOpen] = useState(false)

  // ⭐ Bookmark hook for task starring
  const { isBookmarked, toggleBookmark, count: bookmarkCount } = useBookmarks()

  // Fetch module data and tasks
  useEffect(() => {
    async function fetchModuleAndTasks() {
      if (!params?.id) return

      setIsLoading(true)
      try {
        const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

        // Fetch module and tasks in parallel
        const [moduleRes, tasksRes] = await Promise.all([
          fetch(`${apiUrl}/api/modules/${params.id}`),
          fetch(`${apiUrl}/api/tasks/module/${params.id}`)
        ])

        if (moduleRes.ok) {
          const moduleData = await moduleRes.json()

          // Fetch tasks and merge into module
          let tasks: Task[] = []
          if (tasksRes.ok) {
            const tasksData = await tasksRes.json()
            tasks = (tasksData || []).map((t: any) => ({
              id: t.id,
              title: t.title,
              type: 'lesson' as const,
              order_index: t.order_index || 0,
              xp_reward: t.xp_reward || 25,
              is_completed: false // TODO: fetch from progress API
            })).sort((a: Task, b: Task) => a.order_index - b.order_index)
          }

          setModule({
            ...moduleData,
            tasks,
            labs: [], // TODO: fetch labs when API is ready
          })
        }
      } catch (error) {
        console.error('Failed to fetch module:', error)
      } finally {
        setIsLoading(false)
      }
    }

    fetchModuleAndTasks()
  }, [params?.id])

  // Close sidebar on route change (mobile)
  useEffect(() => {
    setSidebarOpen(false)
  }, [pathname])

  return (
    <div className="flex min-h-screen bg-gray-950">
      {/* Mobile Menu Button */}
      <button
        onClick={() => setSidebarOpen(true)}
        className="fixed bottom-4 left-4 z-50 lg:hidden p-3 bg-indigo-500 rounded-full shadow-lg"
      >
        <Menu className="w-6 h-6 text-white" />
      </button>

      {/* ⭐ Mobile Bookmark Button */}
      <button
        onClick={() => setBookmarkSidebarOpen(!bookmarkSidebarOpen)}
        className="fixed bottom-4 right-4 z-50 lg:hidden p-3 bg-amber-500 rounded-full shadow-lg"
      >
        <Star className={`w-6 h-6 text-white ${bookmarkCount > 0 ? 'fill-white' : ''}`} />
        {bookmarkCount > 0 && (
          <span className="absolute -top-1 -right-1 w-5 h-5 text-[10px] font-bold bg-white text-amber-600 rounded-full flex items-center justify-center">
            {bookmarkCount > 9 ? '9+' : bookmarkCount}
          </span>
        )}
      </button>

      {/* Task Sidebar */}
      <TaskSidebar
        module={module}
        currentPath={pathname || ''}
        isOpen={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
        isBookmarked={isBookmarked}
        toggleBookmark={toggleBookmark}
      />

      {/* Main Content */}
      <main className="flex-1 min-w-0">
        {children}
      </main>

      {/* ⭐ Bookmark Sidebar (Right Side) */}
      <aside className={`
        fixed lg:sticky top-0 right-0 h-screen w-72
        bg-gray-900 border-l border-gray-800
        transform transition-transform duration-300 ease-in-out
        z-50 lg:z-auto
        ${bookmarkSidebarOpen ? 'translate-x-0' : 'translate-x-full lg:translate-x-0'}
        hidden lg:flex lg:flex-col
      `}>
        {/* Mobile close button */}
        <button
          onClick={() => setBookmarkSidebarOpen(false)}
          className="lg:hidden absolute top-4 left-4 p-1 rounded hover:bg-gray-800"
        >
          <X className="w-5 h-5 text-gray-400" />
        </button>

        <BookmarkSidebar className="flex-1" />
      </aside>

      {/* Mobile Bookmark Overlay */}
      {bookmarkSidebarOpen && (
        <div
          className="fixed inset-0 bg-black/50 z-40 lg:hidden"
          onClick={() => setBookmarkSidebarOpen(false)}
        />
      )}

      {/* Mobile Bookmark Sidebar */}
      <aside className={`
        fixed top-0 right-0 h-screen w-72
        bg-gray-900 border-l border-gray-800
        transform transition-transform duration-300 ease-in-out
        z-50 lg:hidden
        ${bookmarkSidebarOpen ? 'translate-x-0' : 'translate-x-full'}
        flex flex-col
      `}>
        <div className="flex items-center justify-between p-4 border-b border-gray-800">
          <div className="flex items-center gap-2">
            <Star className="w-4 h-4 text-amber-400 fill-amber-400" />
            <span className="text-sm font-semibold text-white">Bookmarks</span>
          </div>
          <button
            onClick={() => setBookmarkSidebarOpen(false)}
            className="p-1 rounded hover:bg-gray-800"
          >
            <X className="w-5 h-5 text-gray-400" />
          </button>
        </div>
        <BookmarkSidebar className="flex-1" />
      </aside>
    </div>
  )
}
