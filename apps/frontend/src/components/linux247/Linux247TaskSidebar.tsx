"use client"

/**
 * Linux247TaskSidebar - Premium Cosmic Navigation for Linux 24/7 Module
 * Same design as DOE25TaskSidebar
 */

import * as React from "react"
import Link from "next/link"
import { usePathname } from "next/navigation"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { 
  ChevronDown, 
  ChevronRight,
  CheckCircle2,
  Circle,
  Menu,
  X,
  Terminal
} from "lucide-react"
import { LINUX247_MODULE, getLinux247TasksByCategory } from "@/data/linux247-module"

interface Linux247TaskSidebarProps {
  currentTaskId?: string
  completedTasks?: string[]
  collapsed?: boolean
  onToggle?: () => void
}

export function Linux247TaskSidebar({ 
  currentTaskId, 
  completedTasks = [],
  collapsed = false,
  onToggle
}: Linux247TaskSidebarProps) {
  const pathname = usePathname()
  const [expandedCategories, setExpandedCategories] = React.useState<string[]>(['Grundläggande'])
  const [mobileOpen, setMobileOpen] = React.useState(false)

  const tasksByCategory = getLinux247TasksByCategory()
  const categories = Object.keys(tasksByCategory)

  const toggleCategory = (category: string) => {
    setExpandedCategories(prev => 
      prev.includes(category) 
        ? prev.filter(c => c !== category)
        : [...prev, category]
    )
  }

  const isTaskComplete = (taskId: string) => completedTasks.includes(taskId)
  const isCurrentTask = (taskId: string) => currentTaskId === taskId || pathname?.includes(taskId)

  const getCategoryProgress = (category: string) => {
    const tasks = tasksByCategory[category]
    const completed = tasks.filter(t => isTaskComplete(t.id)).length
    return { completed, total: tasks.length }
  }

  const getCategoryIcon = (category: string) => {
    const icons: Record<string, string> = {
      'Grundläggande': '📁',
      'Nätverk': '🌐',
      'Säkerhet': '🔐',
      'System': '⚙️',
      'Automation': '🤖',
      'Produktivitet': '⚡',
      'Reference': '📚',
      'Avancerat': '🎯'
    }
    return icons[category] || '📌'
  }

  const SidebarContent = () => (
    <div className="flex flex-col h-full">
      {/* Header */}
      <div className="p-4 border-b border-white/10">
        <div className="flex items-center gap-3">
          <div className={cn(
            "w-10 h-10 rounded-xl flex items-center justify-center",
            "bg-gradient-to-br from-emerald-500 to-teal-600",
            "shadow-lg shadow-emerald-500/25"
          )}>
            <Terminal className="w-5 h-5 text-white" />
          </div>
          {!collapsed && (
            <div>
              <h2 className="font-bold text-white">Linux 24/7</h2>
              <p className="text-xs text-zinc-400">{LINUX247_MODULE.totalTasks} tasks</p>
            </div>
          )}
        </div>
      </div>

      {/* Progress */}
      {!collapsed && (
        <div className="px-4 py-3 border-b border-white/5">
          <div className="flex items-center justify-between text-xs mb-2">
            <span className="text-zinc-400">Progress</span>
            <span className="text-emerald-400 font-medium">
              {completedTasks.length}/{LINUX247_MODULE.totalTasks}
            </span>
          </div>
          <div className="h-1.5 bg-zinc-800 rounded-full overflow-hidden">
            <motion.div 
              className="h-full bg-gradient-to-r from-emerald-500 to-teal-400 rounded-full"
              initial={{ width: 0 }}
              animate={{ width: `${(completedTasks.length / LINUX247_MODULE.totalTasks) * 100}%` }}
              transition={{ duration: 0.5, ease: "easeOut" }}
            />
          </div>
        </div>
      )}

      {/* Categories */}
      <nav className="flex-1 overflow-y-auto p-2 space-y-1">
        {categories.map((category) => {
          const isExpanded = expandedCategories.includes(category)
          const { completed, total } = getCategoryProgress(category)
          const tasks = tasksByCategory[category]

          return (
            <div key={category}>
              {/* Category Header */}
              <button
                onClick={() => toggleCategory(category)}
                className={cn(
                  "w-full flex items-center gap-2 px-3 py-2 rounded-lg",
                  "text-left transition-all duration-200",
                  "hover:bg-white/5",
                  isExpanded && "bg-white/5"
                )}
              >
                <span className="text-lg">{getCategoryIcon(category)}</span>
                {!collapsed && (
                  <>
                    <span className="flex-1 text-sm font-medium text-zinc-300">
                      {category}
                    </span>
                    <span className="text-xs text-zinc-500">
                      {completed}/{total}
                    </span>
                    <motion.div
                      animate={{ rotate: isExpanded ? 180 : 0 }}
                      transition={{ duration: 0.2 }}
                    >
                      <ChevronDown className="w-4 h-4 text-zinc-500" />
                    </motion.div>
                  </>
                )}
              </button>

              {/* Tasks */}
              <AnimatePresence>
                {isExpanded && !collapsed && (
                  <motion.div
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: "auto", opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    transition={{ duration: 0.2 }}
                    className="overflow-hidden"
                  >
                    <div className="ml-4 pl-3 border-l border-zinc-700/50 space-y-0.5 py-1">
                      {tasks.map((task) => {
                        const isComplete = isTaskComplete(task.id)
                        const isCurrent = isCurrentTask(task.id)

                        return (
                          <Link
                            key={task.id}
                            href={`/modules/linux-247/tasks/${task.slug}`}
                            className={cn(
                              "flex items-center gap-2 px-2 py-1.5 rounded-lg",
                              "text-sm transition-all duration-200",
                              isCurrent && [
                                "bg-gradient-to-r from-emerald-500/20 to-teal-500/10",
                                "text-emerald-300 font-medium",
                                "border border-emerald-500/30"
                              ],
                              !isCurrent && isComplete && "text-zinc-400",
                              !isCurrent && !isComplete && "text-zinc-500 hover:text-zinc-300 hover:bg-white/5"
                            )}
                          >
                            {isComplete ? (
                              <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                            ) : isCurrent ? (
                              <motion.div
                                animate={{ scale: [1, 1.2, 1] }}
                                transition={{ duration: 2, repeat: Infinity }}
                              >
                                <Circle className="w-4 h-4 text-emerald-400 shrink-0" />
                              </motion.div>
                            ) : (
                              <Circle className="w-4 h-4 shrink-0" />
                            )}
                            <span className="truncate">{task.order}. {task.title}</span>
                          </Link>
                        )
                      })}
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          )
        })}
      </nav>
    </div>
  )

  return (
    <>
      {/* Desktop Sidebar */}
      <motion.aside
        initial={{ x: -20, opacity: 0 }}
        animate={{ x: 0, opacity: 1 }}
        className={cn(
          "hidden lg:flex flex-col h-screen sticky top-0",
          "bg-[#0a0a12]/95 backdrop-blur-xl",
          "border-r border-white/5",
          "transition-all duration-300",
          collapsed ? "w-16" : "w-72"
        )}
      >
        <SidebarContent />
        
        {/* Toggle Button */}
        <button
          onClick={onToggle}
          className={cn(
            "absolute -right-3 top-20 z-10",
            "w-6 h-6 rounded-full",
            "bg-zinc-800 border border-zinc-700",
            "flex items-center justify-center",
            "hover:bg-zinc-700 transition-colors"
          )}
        >
          <ChevronRight className={cn(
            "w-4 h-4 text-zinc-400 transition-transform",
            collapsed && "rotate-180"
          )} />
        </button>
      </motion.aside>

      {/* Mobile Toggle */}
      <button
        onClick={() => setMobileOpen(true)}
        className={cn(
          "lg:hidden fixed bottom-4 left-4 z-50",
          "w-12 h-12 rounded-full",
          "bg-gradient-to-r from-emerald-500 to-teal-600",
          "flex items-center justify-center",
          "shadow-lg shadow-emerald-500/25"
        )}
      >
        <Menu className="w-5 h-5 text-white" />
      </button>

      {/* Mobile Drawer */}
      <AnimatePresence>
        {mobileOpen && (
          <>
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setMobileOpen(false)}
              className="lg:hidden fixed inset-0 bg-black/60 backdrop-blur-sm z-50"
            />
            <motion.div
              initial={{ x: "-100%" }}
              animate={{ x: 0 }}
              exit={{ x: "-100%" }}
              transition={{ type: "spring", damping: 25, stiffness: 300 }}
              className={cn(
                "lg:hidden fixed left-0 top-0 bottom-0 w-80 z-50",
                "bg-[#0a0a12] border-r border-white/10"
              )}
            >
              <button
                onClick={() => setMobileOpen(false)}
                className="absolute top-4 right-4 p-2 text-zinc-400 hover:text-white"
              >
                <X className="w-5 h-5" />
              </button>
              <SidebarContent />
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </>
  )
}

export default Linux247TaskSidebar
