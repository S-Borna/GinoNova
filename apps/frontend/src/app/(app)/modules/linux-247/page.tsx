"use client"

/**
 * Linux 24/7 Module Overview Page
 * Premium cosmic design matching DOE25
 */

import * as React from "react"
import Link from "next/link"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { 
  Terminal, 
  Clock, 
  Zap, 
  ChevronRight,
  CheckCircle2,
  BookOpen,
  Trophy
} from "lucide-react"
import { LINUX247_MODULE, getLinux247TasksByCategory } from "@/data/linux247-module"

export default function Linux247ModulePage() {
  const [completedTasks, setCompletedTasks] = React.useState<string[]>([])

  // Load progress from localStorage
  React.useEffect(() => {
    const saved = localStorage.getItem('linux247-progress')
    if (saved) {
      setCompletedTasks(JSON.parse(saved))
    }
  }, [])

  const tasksByCategory = getLinux247TasksByCategory()
  const categories = Object.keys(tasksByCategory)
  const totalCompleted = completedTasks.length
  const progressPercent = (totalCompleted / LINUX247_MODULE.totalTasks) * 100

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

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'easy': return 'text-emerald-400 bg-emerald-500/10 border-emerald-500/20'
      case 'medium': return 'text-amber-400 bg-amber-500/10 border-amber-500/20'
      case 'hard': return 'text-red-400 bg-red-500/10 border-red-500/20'
      default: return 'text-zinc-400 bg-zinc-500/10 border-zinc-500/20'
    }
  }

  return (
    <div className="min-h-screen bg-[#05050a]">
      {/* Background effects */}
      <div className="fixed inset-0 pointer-events-none">
        <div className="absolute top-0 left-1/4 w-96 h-96 bg-emerald-500/10 rounded-full blur-[120px]" />
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-teal-500/10 rounded-full blur-[120px]" />
      </div>

      <div className="relative max-w-6xl mx-auto px-4 py-12">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-12"
        >
          <div className="inline-flex items-center gap-3 mb-6">
            <motion.div
              className={cn(
                "w-16 h-16 rounded-2xl flex items-center justify-center",
                "bg-gradient-to-br from-emerald-500 to-teal-600",
                "shadow-2xl shadow-emerald-500/25"
              )}
              animate={{ 
                boxShadow: [
                  "0 25px 50px -12px rgba(16, 185, 129, 0.25)",
                  "0 25px 50px -12px rgba(16, 185, 129, 0.4)",
                  "0 25px 50px -12px rgba(16, 185, 129, 0.25)"
                ]
              }}
              transition={{ duration: 2, repeat: Infinity }}
            >
              <Terminal className="w-8 h-8 text-white" />
            </motion.div>
          </div>

          <h1 className="text-4xl md:text-5xl font-black text-white mb-4">
            {LINUX247_MODULE.title}
          </h1>
          <p className="text-lg text-zinc-400 max-w-2xl mx-auto">
            {LINUX247_MODULE.description}
          </p>

          {/* Stats */}
          <div className="flex items-center justify-center gap-6 mt-8">
            <div className="flex items-center gap-2 text-zinc-400">
              <BookOpen className="w-5 h-5 text-emerald-400" />
              <span>{LINUX247_MODULE.totalTasks} tasks</span>
            </div>
            <div className="flex items-center gap-2 text-zinc-400">
              <Clock className="w-5 h-5 text-teal-400" />
              <span>{LINUX247_MODULE.estimatedHours}h uppskattat</span>
            </div>
            <div className="flex items-center gap-2 text-zinc-400">
              <Zap className="w-5 h-5 text-amber-400" />
              <span>{LINUX247_MODULE.tasks.reduce((acc, t) => acc + t.xpReward, 0)} XP totalt</span>
            </div>
          </div>
        </motion.div>

        {/* Progress Card */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className={cn(
            "rounded-2xl p-6 mb-12",
            "bg-zinc-900/50 border border-zinc-800/50",
            "backdrop-blur-xl"
          )}
        >
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-3">
              <Trophy className="w-6 h-6 text-amber-400" />
              <h2 className="text-xl font-bold text-white">Din Progress</h2>
            </div>
            <span className="text-2xl font-bold text-emerald-400">
              {totalCompleted}/{LINUX247_MODULE.totalTasks}
            </span>
          </div>

          <div className="h-3 bg-zinc-800 rounded-full overflow-hidden mb-2">
            <motion.div
              className="h-full bg-gradient-to-r from-emerald-500 to-teal-400 rounded-full"
              initial={{ width: 0 }}
              animate={{ width: `${progressPercent}%` }}
              transition={{ duration: 1, ease: "easeOut" }}
            />
          </div>
          <p className="text-sm text-zinc-500">
            {progressPercent === 100 
              ? "🎉 Grattis! Du har slutfört hela modulen!" 
              : `${Math.round(progressPercent)}% klart - fortsätt så!`}
          </p>
        </motion.div>

        {/* Categories & Tasks */}
        <div className="space-y-8">
          {categories.map((category, categoryIndex) => {
            const tasks = tasksByCategory[category]
            const categoryCompleted = tasks.filter(t => completedTasks.includes(t.id)).length

            return (
              <motion.div
                key={category}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.1 + categoryIndex * 0.05 }}
              >
                {/* Category Header */}
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-2xl">{getCategoryIcon(category)}</span>
                  <h2 className="text-xl font-bold text-white">{category}</h2>
                  <span className="text-sm text-zinc-500">
                    {categoryCompleted}/{tasks.length} klara
                  </span>
                  <div className="flex-1 h-px bg-zinc-800" />
                </div>

                {/* Task Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {tasks.map((task, taskIndex) => {
                    const isComplete = completedTasks.includes(task.id)

                    return (
                      <motion.div
                        key={task.id}
                        initial={{ opacity: 0, scale: 0.95 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ delay: 0.1 + taskIndex * 0.03 }}
                      >
                        <Link
                          href={`/modules/linux-247/tasks/${task.slug}`}
                          className={cn(
                            "block rounded-xl p-4",
                            "bg-zinc-900/50 border border-zinc-800/50",
                            "hover:border-emerald-500/30 hover:bg-zinc-900/80",
                            "transition-all duration-200",
                            "group"
                          )}
                        >
                          <div className="flex items-start gap-3">
                            {/* Status Icon */}
                            <div className={cn(
                              "w-10 h-10 rounded-lg flex items-center justify-center shrink-0",
                              "text-xl",
                              isComplete 
                                ? "bg-emerald-500/20" 
                                : "bg-zinc-800"
                            )}>
                              {isComplete ? (
                                <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                              ) : (
                                task.icon
                              )}
                            </div>

                            {/* Content */}
                            <div className="flex-1 min-w-0">
                              <div className="flex items-center gap-2 mb-1">
                                <span className="text-xs text-zinc-500">#{task.order}</span>
                                <span className={cn(
                                  "text-xs px-2 py-0.5 rounded-full border",
                                  getDifficultyColor(task.difficulty)
                                )}>
                                  {task.difficulty}
                                </span>
                              </div>
                              <h3 className={cn(
                                "font-semibold mb-1 truncate",
                                isComplete ? "text-zinc-400" : "text-white group-hover:text-emerald-300"
                              )}>
                                {task.title}
                              </h3>
                              <p className="text-sm text-zinc-500 truncate">
                                {task.description}
                              </p>
                              <div className="flex items-center gap-4 mt-2 text-xs text-zinc-500">
                                <span className="flex items-center gap-1">
                                  <Clock className="w-3 h-3" />
                                  {task.estimatedMinutes} min
                                </span>
                                <span className="flex items-center gap-1">
                                  <Zap className="w-3 h-3 text-amber-400" />
                                  {task.xpReward} XP
                                </span>
                              </div>
                            </div>

                            {/* Arrow */}
                            <ChevronRight className={cn(
                              "w-5 h-5 text-zinc-600 shrink-0",
                              "group-hover:text-emerald-400 group-hover:translate-x-1",
                              "transition-all duration-200"
                            )} />
                          </div>
                        </Link>
                      </motion.div>
                    )
                  })}
                </div>
              </motion.div>
            )
          })}
        </div>
      </div>
    </div>
  )
}
