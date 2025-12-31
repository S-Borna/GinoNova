"use client"

/**
 * Linux 24/7 Individual Task Page
 * Premium cosmic design with interactive learning
 */

import * as React from "react"
import { useParams, useRouter, notFound } from "next/navigation"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import {
  ArrowLeft,
  ArrowRight,
  Clock,
  Zap,
  CheckCircle2,
  BookOpen,
  RotateCcw,
  Trophy
} from "lucide-react"
import Link from "next/link"
import { 
  LINUX247_MODULE, 
  getLinux247TaskBySlug 
} from "@/data/linux247-module"
import { 
  Linux247TaskSidebar, 
  Linux247ContentRenderer 
} from "@/components/linux247"

export default function Linux247TaskPage() {
  const params = useParams()
  const router = useRouter()
  const taskId = params?.taskId as string

  const [completedTasks, setCompletedTasks] = React.useState<string[]>([])
  const [sidebarCollapsed, setSidebarCollapsed] = React.useState(false)
  const [showCelebration, setShowCelebration] = React.useState(false)

  // Get task data
  const task = getLinux247TaskBySlug(taskId)
  
  if (!task) {
    notFound()
  }

  // Load progress
  React.useEffect(() => {
    const saved = localStorage.getItem('linux247-progress')
    if (saved) {
      setCompletedTasks(JSON.parse(saved))
    }
  }, [])

  // Check if completed
  const isCompleted = completedTasks.includes(task.id)

  // Get adjacent tasks
  const currentIndex = LINUX247_MODULE.tasks.findIndex(t => t.id === task.id)
  const prevTask = currentIndex > 0 ? LINUX247_MODULE.tasks[currentIndex - 1] : null
  const nextTask = currentIndex < LINUX247_MODULE.tasks.length - 1 ? LINUX247_MODULE.tasks[currentIndex + 1] : null

  // Mark complete handler
  const handleMarkComplete = () => {
    const newCompleted = [...completedTasks]
    if (!newCompleted.includes(task.id)) {
      newCompleted.push(task.id)
      setCompletedTasks(newCompleted)
      localStorage.setItem('linux247-progress', JSON.stringify(newCompleted))
      setShowCelebration(true)
      setTimeout(() => setShowCelebration(false), 3000)
    }
  }

  // Reset progress handler
  const handleResetProgress = () => {
    const newCompleted = completedTasks.filter(id => id !== task.id)
    setCompletedTasks(newCompleted)
    localStorage.setItem('linux247-progress', JSON.stringify(newCompleted))
  }

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'easy': return 'text-emerald-400 bg-emerald-500/10 border-emerald-500/30'
      case 'medium': return 'text-amber-400 bg-amber-500/10 border-amber-500/30'
      case 'hard': return 'text-red-400 bg-red-500/10 border-red-500/30'
      default: return 'text-zinc-400 bg-zinc-500/10 border-zinc-500/30'
    }
  }

  return (
    <div className="min-h-screen bg-[#05050a] flex">
      {/* Sidebar */}
      <Linux247TaskSidebar
        currentTaskId={task.id}
        completedTasks={completedTasks}
        collapsed={sidebarCollapsed}
        onToggle={() => setSidebarCollapsed(!sidebarCollapsed)}
      />

      {/* Main Content */}
      <div className={cn(
        "flex-1 transition-all duration-300",
        sidebarCollapsed ? "ml-16" : "ml-72"
      )}>
        {/* Background effects */}
        <div className="fixed inset-0 pointer-events-none">
          <div className="absolute top-1/4 left-1/3 w-96 h-96 bg-emerald-500/5 rounded-full blur-[120px]" />
          <div className="absolute bottom-1/3 right-1/4 w-80 h-80 bg-teal-500/5 rounded-full blur-[100px]" />
        </div>

        <div className="relative max-w-4xl mx-auto px-6 py-10">
          {/* Back Link */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
          >
            <Link
              href="/modules/linux-247"
              className="inline-flex items-center gap-2 text-zinc-400 hover:text-emerald-400 transition-colors mb-8"
            >
              <ArrowLeft className="w-4 h-4" />
              <span>Tillbaka till Linux 24/7</span>
            </Link>
          </motion.div>

          {/* Task Header */}
          <motion.header
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="mb-10"
          >
            <div className="flex items-start gap-4 mb-6">
              <div className={cn(
                "w-14 h-14 rounded-xl flex items-center justify-center text-2xl",
                "bg-gradient-to-br from-emerald-500/20 to-teal-500/20",
                "border border-emerald-500/30"
              )}>
                {task.icon}
              </div>
              
              <div className="flex-1">
                <div className="flex items-center gap-3 mb-2">
                  <span className="text-sm text-zinc-500">
                    Task {task.order} av {LINUX247_MODULE.totalTasks}
                  </span>
                  <span className={cn(
                    "text-xs px-2 py-0.5 rounded-full border",
                    getDifficultyColor(task.difficulty)
                  )}>
                    {task.difficulty}
                  </span>
                  {isCompleted && (
                    <span className="flex items-center gap-1 text-xs text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full">
                      <CheckCircle2 className="w-3 h-3" />
                      Slutförd
                    </span>
                  )}
                </div>
                
                <h1 className="text-3xl md:text-4xl font-black text-white mb-3">
                  {task.title}
                </h1>
                
                <p className="text-lg text-zinc-400">
                  {task.description}
                </p>
              </div>
            </div>

            {/* Meta Info */}
            <div className="flex flex-wrap items-center gap-6 p-4 rounded-xl bg-zinc-900/50 border border-zinc-800/50">
              <div className="flex items-center gap-2">
                <Clock className="w-4 h-4 text-zinc-500" />
                <span className="text-zinc-300">{task.estimatedMinutes} minuter</span>
              </div>
              <div className="flex items-center gap-2">
                <Zap className="w-4 h-4 text-amber-400" />
                <span className="text-zinc-300">{task.xpReward} XP</span>
              </div>
              <div className="flex items-center gap-2">
                <BookOpen className="w-4 h-4 text-emerald-400" />
                <span className="text-zinc-300">{task.category}</span>
              </div>
            </div>
          </motion.header>

          {/* Content */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="space-y-6"
          >
            <Linux247ContentRenderer blocks={task.content_blocks} />
          </motion.div>

          {/* Completion Section */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className={cn(
              "mt-12 p-6 rounded-2xl",
              "bg-gradient-to-br from-zinc-900/80 to-zinc-900/50",
              "border",
              isCompleted ? "border-emerald-500/30" : "border-zinc-800/50"
            )}
          >
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-xl font-bold text-white mb-1">
                  {isCompleted ? "✅ Bra jobbat!" : "Redo att gå vidare?"}
                </h3>
                <p className="text-zinc-400">
                  {isCompleted 
                    ? "Du har slutfört denna task!" 
                    : "Markera som slutförd när du är klar"}
                </p>
              </div>
              
              <div className="flex items-center gap-3">
                {isCompleted ? (
                  <button
                    onClick={handleResetProgress}
                    className={cn(
                      "flex items-center gap-2 px-4 py-2 rounded-lg",
                      "bg-zinc-800 text-zinc-300",
                      "hover:bg-zinc-700 transition-colors"
                    )}
                  >
                    <RotateCcw className="w-4 h-4" />
                    <span>Återställ</span>
                  </button>
                ) : (
                  <button
                    onClick={handleMarkComplete}
                    className={cn(
                      "flex items-center gap-2 px-6 py-3 rounded-xl font-semibold",
                      "bg-gradient-to-r from-emerald-500 to-teal-500",
                      "text-white shadow-lg shadow-emerald-500/25",
                      "hover:shadow-emerald-500/40 hover:scale-105",
                      "transition-all duration-200"
                    )}
                  >
                    <CheckCircle2 className="w-5 h-5" />
                    <span>Markera som klar</span>
                  </button>
                )}
              </div>
            </div>
          </motion.div>

          {/* Navigation */}
          <motion.nav
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.3 }}
            className="flex items-center justify-between mt-8 pt-8 border-t border-zinc-800/50"
          >
            {prevTask ? (
              <Link
                href={`/modules/linux-247/tasks/${prevTask.slug}`}
                className={cn(
                  "flex items-center gap-3 px-4 py-3 rounded-xl",
                  "bg-zinc-900/50 border border-zinc-800/50",
                  "hover:border-emerald-500/30 hover:bg-zinc-900/80",
                  "transition-all duration-200 group"
                )}
              >
                <ArrowLeft className="w-5 h-5 text-zinc-500 group-hover:text-emerald-400 transition-colors" />
                <div className="text-left">
                  <span className="text-xs text-zinc-500">Föregående</span>
                  <p className="text-sm text-white group-hover:text-emerald-300 transition-colors">
                    {prevTask.title}
                  </p>
                </div>
              </Link>
            ) : (
              <div />
            )}

            {nextTask ? (
              <Link
                href={`/modules/linux-247/tasks/${nextTask.slug}`}
                className={cn(
                  "flex items-center gap-3 px-4 py-3 rounded-xl",
                  "bg-zinc-900/50 border border-zinc-800/50",
                  "hover:border-emerald-500/30 hover:bg-zinc-900/80",
                  "transition-all duration-200 group"
                )}
              >
                <div className="text-right">
                  <span className="text-xs text-zinc-500">Nästa</span>
                  <p className="text-sm text-white group-hover:text-emerald-300 transition-colors">
                    {nextTask.title}
                  </p>
                </div>
                <ArrowRight className="w-5 h-5 text-zinc-500 group-hover:text-emerald-400 transition-colors" />
              </Link>
            ) : (
              <Link
                href="/modules/linux-247"
                className={cn(
                  "flex items-center gap-3 px-4 py-3 rounded-xl",
                  "bg-gradient-to-r from-emerald-500/20 to-teal-500/20",
                  "border border-emerald-500/30",
                  "hover:from-emerald-500/30 hover:to-teal-500/30",
                  "transition-all duration-200 group"
                )}
              >
                <div className="text-right">
                  <span className="text-xs text-emerald-400">Slutfört!</span>
                  <p className="text-sm text-white">Tillbaka till översikt</p>
                </div>
                <Trophy className="w-5 h-5 text-amber-400" />
              </Link>
            )}
          </motion.nav>
        </div>
      </div>

      {/* Celebration Animation */}
      <AnimatePresence>
        {showCelebration && (
          <motion.div
            initial={{ opacity: 0, scale: 0.5 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.5 }}
            className="fixed inset-0 flex items-center justify-center pointer-events-none z-50"
          >
            <div className="text-center">
              <motion.div
                initial={{ scale: 0 }}
                animate={{ scale: [0, 1.2, 1] }}
                transition={{ duration: 0.5 }}
                className="text-8xl mb-4"
              >
                🎉
              </motion.div>
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2 }}
                className="bg-gradient-to-r from-emerald-400 to-teal-400 bg-clip-text text-transparent text-2xl font-bold"
              >
                +{task.xpReward} XP
              </motion.div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}
