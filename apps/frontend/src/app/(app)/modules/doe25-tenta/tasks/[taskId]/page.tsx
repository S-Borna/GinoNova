"use client"

/**
 * ============================================================================
 * DOE25 TASK PAGE — Premium Interactive Learning Experience
 * ============================================================================
 *
 * Complete redesign with:
 * - Collapsible sidebar for task navigation
 * - Interactive content blocks (not markdown)
 * - Beautiful animations and transitions
 * - Progress tracking
 * - Mobile-responsive design
 *
 * @phase DOE25-REDESIGN
 */

import { useState, useEffect, useCallback } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { TaskFooter } from "@saas/ui"
import { CosmicAurora } from "@/components/ui/cosmic-aurora"
import { useAuth } from "@/components/auth"
import { getToken } from "@/lib/auth"
import {
    ArrowLeft,
    CheckCircle2,
    Clock,
    BookOpen,
    RefreshCw,
    AlertCircle,
    Zap,
    Play,
    Sparkles,
    ChevronLeft,
    ChevronRight,
    Target,
    Trophy,
    Menu,
} from "lucide-react"

// DOE25 Components & Data
import { DOE25_MODULE, DOE25Task, getTaskById } from "@/data/doe25-module"
import { DOE25TaskSidebar } from "@/components/doe25/DOE25TaskSidebar"
import { DOE25ContentRenderer } from "@/components/doe25/DOE25ContentRenderer"

/* ============================================================================
   MODULE COLORS
   ============================================================================ */

const moduleColors: Record<string, { color: string; icon: string }> = {
    "doe25-tenta": { color: "#f59e0b", icon: "📝" },
}

/* ============================================================================
   DIFFICULTY CONFIG
   ============================================================================ */

const difficultyConfig: Record<string, { level: number; label: string; color: string }> = {
    easy: { level: 1, label: "Lätt", color: "bg-green-400" },
    medium: { level: 2, label: "Medium", color: "bg-yellow-400" },
    hard: { level: 3, label: "Svår", color: "bg-orange-400" },
    expert: { level: 4, label: "Expert", color: "bg-red-400" },
}

function DifficultyDots({ difficulty }: { difficulty: string }) {
    const config = difficultyConfig[difficulty] || difficultyConfig.medium
    return (
        <div className="flex items-center gap-1.5">
            <div className="flex items-center gap-0.5">
                {Array.from({ length: 4 }).map((_, i) => (
                    <div
                        key={i}
                        className={cn(
                            "w-1.5 h-1.5 rounded-full transition-all",
                            i < config.level ? config.color : "bg-zinc-700"
                        )}
                    />
                ))}
            </div>
            <span className="text-xs text-zinc-500">{config.label}</span>
        </div>
    )
}

/* ============================================================================
   SKELETON
   ============================================================================ */

function TaskDetailSkeleton() {
    return (
        <div className="space-y-6 animate-pulse">
            <div className="h-48 rounded-3xl bg-zinc-800/50" />
            <div className="h-96 rounded-2xl bg-zinc-800/50" />
        </div>
    )
}

/* ============================================================================
   ERROR STATE
   ============================================================================ */

function ErrorState({ error, onRetry }: { error: string; onRetry: () => void }) {
    return (
        <div className={cn(
            "max-w-md mx-auto text-center p-8 rounded-2xl",
            "bg-zinc-900/80 border border-zinc-800"
        )}>
            <div className={cn(
                "w-16 h-16 mx-auto mb-4 rounded-full",
                "bg-red-500/20 flex items-center justify-center"
            )}>
                <AlertCircle className="w-8 h-8 text-red-400" />
            </div>
            <h2 className="text-xl font-semibold text-white mb-2">
                Task hittades inte
            </h2>
            <p className="text-zinc-400 mb-6">{error}</p>
            <div className="flex gap-3 justify-center">
                <Link href="/modules/doe25-tenta">
                    <button className="px-4 py-2 rounded-xl bg-zinc-800 text-white hover:bg-zinc-700 transition-colors">
                        <ArrowLeft className="w-4 h-4 mr-2 inline" />
                        Tillbaka
                    </button>
                </Link>
                <button onClick={onRetry} className="px-4 py-2 rounded-xl bg-purple-600 text-white hover:bg-purple-500 transition-colors">
                    <RefreshCw className="w-4 h-4 mr-2 inline" />
                    Försök igen
                </button>
            </div>
        </div>
    )
}

/* ============================================================================
   QUICK NAV - Previous/Next Tasks
   ============================================================================ */

function QuickNav({
    prevTask,
    nextTask,
    currentIndex,
    totalTasks
}: {
    prevTask: DOE25Task | null
    nextTask: DOE25Task | null
    currentIndex: number
    totalTasks: number
}) {
    return (
        <div className="flex items-center justify-between gap-4 mb-6">
            {/* Previous */}
            {prevTask ? (
                <Link
                    href={`/modules/doe25-tenta/tasks/${prevTask.id}`}
                    className={cn(
                        "flex items-center gap-2 px-4 py-2 rounded-xl",
                        "bg-white/5 hover:bg-white/10 border border-white/10",
                        "text-zinc-400 hover:text-white transition-all",
                        "max-w-[45%]"
                    )}
                >
                    <ChevronLeft className="w-4 h-4 shrink-0" />
                    <span className="truncate text-sm">{prevTask.title}</span>
                </Link>
            ) : (
                <div />
            )}

            {/* Progress indicator */}
            <div className="text-xs text-zinc-500 shrink-0">
                {currentIndex + 1} / {totalTasks}
            </div>

            {/* Next */}
            {nextTask ? (
                <Link
                    href={`/modules/doe25-tenta/tasks/${nextTask.id}`}
                    className={cn(
                        "flex items-center gap-2 px-4 py-2 rounded-xl",
                        "bg-purple-500/20 hover:bg-purple-500/30 border border-purple-500/30",
                        "text-purple-300 hover:text-white transition-all",
                        "max-w-[45%]"
                    )}
                >
                    <span className="truncate text-sm">{nextTask.title}</span>
                    <ChevronRight className="w-4 h-4 shrink-0" />
                </Link>
            ) : (
                <Link
                    href="/modules/doe25-tenta"
                    className={cn(
                        "flex items-center gap-2 px-4 py-2 rounded-xl",
                        "bg-emerald-500/20 hover:bg-emerald-500/30 border border-emerald-500/30",
                        "text-emerald-300 hover:text-white transition-all"
                    )}
                >
                    <Trophy className="w-4 h-4" />
                    <span className="text-sm">Klar!</span>
                </Link>
            )}
        </div>
    )
}

/* ============================================================================
   MAIN PAGE COMPONENT
   ============================================================================ */

export default function DOE25TaskPage() {
    const params = useParams()
    const router = useRouter()
    const { user } = useAuth()
    const taskId = params?.taskId as string

    const [task, setTask] = useState<DOE25Task | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [isCompleted, setIsCompleted] = useState(false)
    const [completing, setCompleting] = useState(false)
    const [completedTasks, setCompletedTasks] = useState<string[]>([])

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
    const token = getToken()

    // Load task
    const loadTask = useCallback(() => {
        setLoading(true)
        setError(null)

        const doe25Task = getTaskById(taskId)
        if (!doe25Task) {
            setError("Task hittades inte")
            setLoading(false)
            return
        }

        setTask(doe25Task)
        setLoading(false)

        // Load completed tasks from localStorage
        try {
            const saved = localStorage.getItem("doe25-completed-tasks")
            if (saved) {
                const parsed = JSON.parse(saved)
                setCompletedTasks(parsed)
                setIsCompleted(parsed.includes(taskId))
            }
        } catch (e) {
            console.log("Could not load progress from localStorage")
        }
    }, [taskId])

    useEffect(() => {
        loadTask()
    }, [loadTask])

    // Mark task as complete
    const handleMarkComplete = async () => {
        setCompleting(true)
        await new Promise(resolve => setTimeout(resolve, 500))

        // Save to localStorage
        const newCompleted = [...completedTasks.filter(id => id !== taskId), taskId]
        localStorage.setItem("doe25-completed-tasks", JSON.stringify(newCompleted))
        setCompletedTasks(newCompleted)
        setIsCompleted(true)
        setCompleting(false)
    }

    // Navigation
    const allTasks = DOE25_MODULE.tasks
    const currentIndex = allTasks.findIndex(t => t.id === taskId)
    const prevTask = currentIndex > 0 ? allTasks[currentIndex - 1] : null
    const nextTask = currentIndex < allTasks.length - 1 ? allTasks[currentIndex + 1] : null

    const handleContinue = () => {
        if (nextTask) {
            router.push(`/modules/doe25-tenta/tasks/${nextTask.id}`)
        } else {
            router.push("/modules/doe25-tenta")
        }
    }

    const moduleConfig = moduleColors["doe25-tenta"]

    return (
        <div className="min-h-screen bg-[#05050a] relative">
            {/* Cosmic Aurora Background */}
            <CosmicAurora />

            {/* Layout with Sidebar */}
            <div className="relative z-10 flex">
                {/* Sidebar */}
                <DOE25TaskSidebar
                    currentTaskId={taskId}
                    completedTasks={completedTasks}
                />

                {/* Main Content */}
                <main className="flex-1 min-h-screen lg:ml-0">
                    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">

                        {/* Back button - mobile */}
                        <Link
                            href="/modules/doe25-tenta"
                            className={cn(
                                "inline-flex items-center gap-2 text-sm mb-6 px-4 py-2 rounded-xl lg:hidden",
                                "text-zinc-400 hover:text-white",
                                "bg-white/5 hover:bg-white/10 border border-white/10",
                                "transition-all duration-300"
                            )}
                        >
                            <ArrowLeft className="w-4 h-4" />
                            DOE25 Tenta
                        </Link>

                        {loading ? (
                            <TaskDetailSkeleton />
                        ) : error ? (
                            <ErrorState error={error} onRetry={loadTask} />
                        ) : task ? (
                            <motion.div
                                className="space-y-6"
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                            >
                                {/* Quick Navigation */}
                                <QuickNav
                                    prevTask={prevTask}
                                    nextTask={nextTask}
                                    currentIndex={currentIndex}
                                    totalTasks={allTasks.length}
                                />

                                {/* Task Header */}
                                <motion.div
                                    initial={{ opacity: 0, y: -20 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    className={cn(
                                        "relative overflow-hidden rounded-3xl",
                                        "bg-[#0a0a0f]",
                                        "border border-purple-500/20",
                                        "p-6 md:p-8"
                                    )}
                                    style={{
                                        boxShadow: `0 0 80px ${moduleConfig.color}20, 0 0 40px rgba(168,85,247,0.1)`,
                                    }}
                                >
                                    {/* Aurora Glow */}
                                    <motion.div
                                        className="absolute -top-20 -right-20 w-[400px] h-[400px] rounded-full"
                                        style={{
                                            background: `radial-gradient(circle, ${moduleConfig.color}40 0%, transparent 70%)`,
                                            filter: "blur(60px)",
                                        }}
                                        animate={{
                                            scale: [1, 1.2, 1],
                                            opacity: [0.3, 0.5, 0.3],
                                        }}
                                        transition={{
                                            duration: 6,
                                            repeat: Infinity,
                                            ease: "easeInOut",
                                        }}
                                    />

                                    {/* Completed Badge */}
                                    {isCompleted && (
                                        <motion.div
                                            initial={{ scale: 0 }}
                                            animate={{ scale: 1 }}
                                            className="absolute top-6 right-6"
                                        >
                                            <div className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-500/20 border border-emerald-500/30">
                                                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                                                <span className="text-xs font-bold text-emerald-300">Klar</span>
                                            </div>
                                        </motion.div>
                                    )}

                                    <div className="relative">
                                        {/* Task Number */}
                                        <div className="flex items-center gap-3 mb-4">
                                            <span className="text-xs font-bold text-purple-400/60 uppercase tracking-[0.15em]">
                                                Task {task.order_index} av {allTasks.length}
                                            </span>
                                        </div>

                                        {/* Title */}
                                        <h1 className={cn(
                                            "text-2xl md:text-4xl font-black mb-4 tracking-tight",
                                            "bg-gradient-to-r from-white via-purple-200 to-cyan-200 bg-clip-text text-transparent"
                                        )}>
                                            {task.title}
                                        </h1>

                                        {/* Description */}
                                        <p className="text-zinc-300 text-lg mb-6 max-w-2xl">
                                            {task.description}
                                        </p>

                                        {/* Meta */}
                                        <div className="flex flex-wrap items-center gap-4">
                                            <span className="flex items-center gap-2 text-zinc-300 bg-white/5 px-4 py-2 rounded-xl border border-white/10">
                                                <Clock className="w-4 h-4 text-purple-400" />
                                                <span className="font-medium">{task.estimated_minutes} min</span>
                                            </span>
                                            <span className="flex items-center gap-2 bg-amber-500/10 px-4 py-2 rounded-xl border border-amber-500/30">
                                                <Zap className="w-4 h-4 text-amber-400" />
                                                <span className="font-black text-amber-400">+100 XP</span>
                                            </span>
                                            <DifficultyDots difficulty="medium" />
                                        </div>
                                    </div>
                                </motion.div>

                                {/* Content Blocks */}
                                <motion.div
                                    initial={{ opacity: 0, y: 20 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: 0.1 }}
                                >
                                    <DOE25ContentRenderer blocks={task.content_blocks} />
                                </motion.div>

                                {/* Task Footer */}
                                <TaskFooter
                                    prevTaskUrl={prevTask ? `/modules/doe25-tenta/tasks/${prevTask.id}` : undefined}
                                    nextTaskUrl={nextTask ? `/modules/doe25-tenta/tasks/${nextTask.id}` : undefined}
                                    onComplete={handleMarkComplete}
                                    xp={100}
                                    difficulty="medium"
                                    isCompleted={isCompleted}
                                    isLoading={completing}
                                />

                                {/* Bottom Quick Nav */}
                                <QuickNav
                                    prevTask={prevTask}
                                    nextTask={nextTask}
                                    currentIndex={currentIndex}
                                    totalTasks={allTasks.length}
                                />
                            </motion.div>
                        ) : null}
                    </div>
                </main>
            </div>
        </div>
    )
}
