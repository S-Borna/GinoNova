"use client"

/**
 * ============================================================================
 * HANDS-ON LAB TASK PAGE — Fetches Data from Backend API
 * ============================================================================
 *
 * Data source: Backend API (/api/content/task/{taskId})
 * Content comes from: apps/backend/src/db/seeds/content/hands_on.py
 *
 * Supports both:
 * - Markdown content (from backend hands_on.py)
 * - Interactive content_blocks (if present)
 *
 * @phase HANDS-ON-LAB
 */

import { useState, useEffect, useCallback } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { TaskFooter } from "@saas/ui"
import { CosmicAurora } from "@/components/ui/cosmic-aurora"
import { useAuth } from "@/components/auth"
import {
    ArrowLeft,
    CheckCircle2,
    Clock,
    RefreshCw,
    AlertCircle,
    Zap,
    ChevronLeft,
    ChevronRight,
    Trophy,
    Menu,
    Loader2,
} from "lucide-react"

// Backend API hooks
import { useHandsOnModule, useHandsOnTask, HandsOnTask } from "@/hooks/useHandsOn"
import { DOE25ContentRenderer } from "@/components/doe25/DOE25ContentRenderer"
import { MarkdownRenderer } from "@/components/content/MarkdownRenderer"

/* ============================================================================
   MODULE COLORS
   ============================================================================ */

const moduleColors: Record<string, { color: string; icon: string }> = {
    "hands-on-lab": { color: "#10b981", icon: "🔬" },
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
   LOADING STATE
   ============================================================================ */

function LoadingState() {
    return (
        <div className="min-h-screen bg-[#05050a] relative">
            <CosmicAurora />
            <div className="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                <div className="flex items-center justify-center min-h-[60vh]">
                    <div className="text-center">
                        <Loader2 className="w-12 h-12 text-emerald-400 animate-spin mx-auto mb-4" />
                        <p className="text-zinc-400">Laddar labb...</p>
                    </div>
                </div>
            </div>
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
                <Link href="/modules/hands-on-lab">
                    <button className="px-4 py-2 rounded-xl bg-zinc-800 text-white hover:bg-zinc-700 transition-colors">
                        <ArrowLeft className="w-4 h-4 mr-2 inline" />
                        Tillbaka
                    </button>
                </Link>
                <button onClick={onRetry} className="px-4 py-2 rounded-xl bg-emerald-600 text-white hover:bg-emerald-500 transition-colors">
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
    prevTask: HandsOnTask | null
    nextTask: HandsOnTask | null
    currentIndex: number
    totalTasks: number
}) {
    return (
        <div className="flex items-center justify-between gap-4 mb-6">
            {/* Previous */}
            {prevTask ? (
                <Link
                    href={`/modules/hands-on-lab/tasks/${prevTask.id}`}
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
                    href={`/modules/hands-on-lab/tasks/${nextTask.id}`}
                    className={cn(
                        "flex items-center gap-2 px-4 py-2 rounded-xl",
                        "bg-emerald-500/20 hover:bg-emerald-500/30 border border-emerald-500/30",
                        "text-emerald-300 hover:text-white transition-all",
                        "max-w-[45%]"
                    )}
                >
                    <span className="truncate text-sm">{nextTask.title}</span>
                    <ChevronRight className="w-4 h-4 shrink-0" />
                </Link>
            ) : (
                <Link
                    href="/modules/hands-on-lab"
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
   HANDS-ON TASK SIDEBAR - Uses API data
   ============================================================================ */

function HandsOnTaskSidebar({
    tasks,
    currentTaskId,
    completedTasks,
    isLoading
}: {
    tasks: HandsOnTask[]
    currentTaskId: string
    completedTasks: string[]
    isLoading: boolean
}) {
    const [isOpen, setIsOpen] = useState(true)

    return (
        <>
            {/* Mobile toggle */}
            <button
                onClick={() => setIsOpen(!isOpen)}
                className={cn(
                    "fixed top-20 left-4 z-50 p-2 rounded-xl lg:hidden",
                    "bg-emerald-500/20 border border-emerald-500/30",
                    "text-emerald-300 hover:text-white transition-all"
                )}
            >
                <Menu className="w-5 h-5" />
            </button>

            {/* Sidebar */}
            <AnimatePresence>
                {isOpen && (
                    <motion.aside
                        initial={{ x: -300, opacity: 0 }}
                        animate={{ x: 0, opacity: 1 }}
                        exit={{ x: -300, opacity: 0 }}
                        className={cn(
                            "fixed lg:sticky top-0 left-0 h-screen w-72 z-40",
                            "bg-[#0a0a0f]/95 backdrop-blur-xl",
                            "border-r border-emerald-500/10",
                            "overflow-y-auto",
                            "lg:block"
                        )}
                    >
                        {/* Header */}
                        <div className="p-6 border-b border-emerald-500/10">
                            <Link
                                href="/modules/hands-on-lab"
                                className="flex items-center gap-3 text-white hover:text-emerald-300 transition-colors"
                            >
                                <span className="text-2xl">🔬</span>
                                <div>
                                    <h2 className="font-bold">Hands-On Lab</h2>
                                    <p className="text-xs text-zinc-500">{tasks.length} labbar</p>
                                </div>
                            </Link>
                        </div>

                        {/* Task list */}
                        <nav className="p-4 space-y-2">
                            {isLoading ? (
                                <div className="space-y-2">
                                    {Array.from({ length: 7 }).map((_, i) => (
                                        <div key={i} className="h-12 bg-zinc-800/50 rounded-xl animate-pulse" />
                                    ))}
                                </div>
                            ) : (
                                tasks.map((task, index) => {
                                    const isActive = task.id === currentTaskId
                                    const isCompleted = completedTasks.includes(task.id)

                                    return (
                                        <Link
                                            key={task.id}
                                            href={`/modules/hands-on-lab/tasks/${task.id}`}
                                            className={cn(
                                                "flex items-center gap-3 p-3 rounded-xl transition-all",
                                                isActive
                                                    ? "bg-emerald-500/20 border border-emerald-500/30 text-white"
                                                    : "hover:bg-white/5 text-zinc-400 hover:text-white"
                                            )}
                                        >
                                            {/* Number/Check */}
                                            <div className={cn(
                                                "w-8 h-8 rounded-lg flex items-center justify-center shrink-0 text-sm font-bold",
                                                isCompleted
                                                    ? "bg-emerald-500/30 text-emerald-300"
                                                    : isActive
                                                        ? "bg-emerald-500/20 text-emerald-300"
                                                        : "bg-zinc-800 text-zinc-500"
                                            )}>
                                                {isCompleted ? (
                                                    <CheckCircle2 className="w-4 h-4" />
                                                ) : (
                                                    index + 1
                                                )}
                                            </div>

                                            {/* Title */}
                                            <span className="text-sm truncate">{task.title}</span>
                                        </Link>
                                    )
                                })
                            )}
                        </nav>

                        {/* Progress */}
                        {tasks.length > 0 && (
                            <div className="p-4 border-t border-emerald-500/10">
                                <div className="flex items-center justify-between text-xs text-zinc-500 mb-2">
                                    <span>Progress</span>
                                    <span>{completedTasks.length}/{tasks.length}</span>
                                </div>
                                <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
                                    <div
                                        className="h-full bg-gradient-to-r from-emerald-500 to-cyan-400 transition-all"
                                        style={{ width: `${(completedTasks.length / tasks.length) * 100}%` }}
                                    />
                                </div>
                            </div>
                        )}
                    </motion.aside>
                )}
            </AnimatePresence>

            {/* Backdrop for mobile */}
            {isOpen && (
                <div
                    className="fixed inset-0 bg-black/50 z-30 lg:hidden"
                    onClick={() => setIsOpen(false)}
                />
            )}
        </>
    )
}

/* ============================================================================
   CONTENT RENDERER - Handles both markdown and content_blocks
   ============================================================================ */

function TaskContent({ task }: { task: HandsOnTask }) {
    // If task has content_blocks, use the interactive renderer
    if (task.content_blocks && task.content_blocks.length > 0) {
        return <DOE25ContentRenderer blocks={task.content_blocks} />
    }
    
    // Otherwise, render markdown content
    if (task.content) {
        return (
            <div className={cn(
                "rounded-2xl bg-[#0a0a0f] border border-emerald-500/10 p-6 md:p-8",
                "prose prose-invert prose-emerald max-w-none",
                "prose-headings:text-white prose-headings:font-bold",
                "prose-h1:text-2xl prose-h2:text-xl prose-h3:text-lg",
                "prose-p:text-zinc-300 prose-strong:text-white",
                "prose-code:text-emerald-300 prose-code:bg-zinc-800 prose-code:px-1.5 prose-code:py-0.5 prose-code:rounded",
                "prose-pre:bg-zinc-900 prose-pre:border prose-pre:border-zinc-800",
                "prose-a:text-emerald-400 prose-a:no-underline hover:prose-a:underline",
                "prose-li:text-zinc-300",
                "prose-table:border-collapse",
                "prose-th:bg-zinc-800/50 prose-th:text-white prose-th:border prose-th:border-zinc-700 prose-th:p-2",
                "prose-td:border prose-td:border-zinc-800 prose-td:p-2"
            )}>
                <MarkdownRenderer content={task.content} />
            </div>
        )
    }
    
    // No content available
    return (
        <div className="rounded-2xl bg-zinc-900/50 border border-zinc-800 p-8 text-center">
            <p className="text-zinc-400">Inget innehåll tillgängligt för denna labb.</p>
        </div>
    )
}

/* ============================================================================
   MAIN PAGE COMPONENT
   ============================================================================ */

export default function HandsOnTaskPage() {
    const params = useParams()
    const router = useRouter()
    const { user } = useAuth()
    const taskId = params?.taskId as string

    // Fetch module data (for sidebar and navigation)
    const { data: module, isLoading: moduleLoading } = useHandsOnModule()
    
    // Fetch specific task data
    const { data: task, isLoading: taskLoading, error: taskError, refetch } = useHandsOnTask(taskId)
    
    const [isCompleted, setIsCompleted] = useState(false)
    const [completing, setCompleting] = useState(false)
    const [completedTasks, setCompletedTasks] = useState<string[]>([])

    // Load completed tasks from localStorage
    useEffect(() => {
        try {
            const saved = localStorage.getItem("handson-completed-tasks")
            if (saved) {
                const parsed = JSON.parse(saved)
                setCompletedTasks(parsed)
                setIsCompleted(parsed.includes(taskId))
            }
        } catch (e) {
        }
    }, [taskId])

    // Mark task as complete
    const handleMarkComplete = async () => {
        setCompleting(true)
        await new Promise(resolve => setTimeout(resolve, 500))

        // Save to localStorage
        const newCompleted = [...completedTasks.filter(id => id !== taskId), taskId]
        localStorage.setItem("handson-completed-tasks", JSON.stringify(newCompleted))
        setCompletedTasks(newCompleted)
        setIsCompleted(true)
        setCompleting(false)
    }

    // Navigation using module tasks
    const allTasks = module?.tasks || []
    const currentIndex = allTasks.findIndex(t => t.id === taskId)
    const prevTask = currentIndex > 0 ? allTasks[currentIndex - 1] : null
    const nextTask = currentIndex >= 0 && currentIndex < allTasks.length - 1 ? allTasks[currentIndex + 1] : null

    const handleContinue = () => {
        if (nextTask) {
            router.push(`/modules/hands-on-lab/tasks/${nextTask.id}`)
        } else {
            router.push("/modules/hands-on-lab")
        }
    }

    const moduleConfig = moduleColors["hands-on-lab"]

    // Loading state
    const isLoading = moduleLoading || taskLoading

    if (isLoading && !task) {
        return <LoadingState />
    }

    return (
        <div className="min-h-screen bg-[#05050a] relative">
            {/* Cosmic Aurora Background */}
            <CosmicAurora />

            {/* Layout with Sidebar */}
            <div className="relative z-10 flex">
                {/* Sidebar */}
                <HandsOnTaskSidebar
                    tasks={allTasks}
                    currentTaskId={taskId}
                    completedTasks={completedTasks}
                    isLoading={moduleLoading}
                />

                {/* Main Content */}
                <main className="flex-1 min-h-screen lg:ml-0">
                    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">

                        {/* Back button - mobile */}
                        <Link
                            href="/modules/hands-on-lab"
                            className={cn(
                                "inline-flex items-center gap-2 text-sm mb-6 px-4 py-2 rounded-xl lg:hidden",
                                "text-zinc-400 hover:text-white",
                                "bg-white/5 hover:bg-white/10 border border-white/10",
                                "transition-all duration-300"
                            )}
                        >
                            <ArrowLeft className="w-4 h-4" />
                            Hands-On Lab
                        </Link>

                        {taskLoading ? (
                            <TaskDetailSkeleton />
                        ) : taskError ? (
                            <ErrorState 
                                error={(taskError as Error).message || "Task hittades inte"} 
                                onRetry={() => refetch()} 
                            />
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
                                    currentIndex={currentIndex >= 0 ? currentIndex : 0}
                                    totalTasks={allTasks.length || 1}
                                />

                                {/* Task Header */}
                                <motion.div
                                    initial={{ opacity: 0, y: -20 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    className={cn(
                                        "relative overflow-hidden rounded-3xl",
                                        "bg-[#0a0a0f]",
                                        "border border-emerald-500/20",
                                        "p-6 md:p-8"
                                    )}
                                    style={{
                                        boxShadow: `0 0 80px ${moduleConfig.color}20, 0 0 40px rgba(16,185,129,0.1)`,
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
                                            <span className="text-xs font-bold text-emerald-400/60 uppercase tracking-[0.15em]">
                                                Labb {(currentIndex >= 0 ? currentIndex : 0) + 1} av {allTasks.length || 1}
                                            </span>
                                        </div>

                                        {/* Title */}
                                        <h1 className={cn(
                                            "text-2xl md:text-4xl font-black mb-4 tracking-tight",
                                            "bg-gradient-to-r from-white via-emerald-200 to-cyan-200 bg-clip-text text-transparent"
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
                                                <Clock className="w-4 h-4 text-emerald-400" />
                                                <span className="font-medium">{task.estimated_minutes} min</span>
                                            </span>
                                            <span className="flex items-center gap-2 bg-amber-500/10 px-4 py-2 rounded-xl border border-amber-500/30">
                                                <Zap className="w-4 h-4 text-amber-400" />
                                                <span className="font-black text-amber-400">+{task.xp_reward || 100} XP</span>
                                            </span>
                                            <DifficultyDots difficulty={task.difficulty || "medium"} />
                                        </div>
                                    </div>
                                </motion.div>

                                {/* Content - Markdown or Content Blocks */}
                                <motion.div
                                    initial={{ opacity: 0, y: 20 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: 0.1 }}
                                >
                                    <TaskContent task={task} />
                                </motion.div>

                                {/* Task Footer */}
                                <TaskFooter
                                    prevTaskUrl={prevTask ? `/modules/hands-on-lab/tasks/${prevTask.id}` : undefined}
                                    nextTaskUrl={nextTask ? `/modules/hands-on-lab/tasks/${nextTask.id}` : undefined}
                                    onComplete={handleMarkComplete}
                                    xp={task.xp_reward || 100}
                                    difficulty={task.difficulty}
                                    isCompleted={isCompleted}
                                    isLoading={completing}
                                />

                                {/* Bottom Quick Nav */}
                                <QuickNav
                                    prevTask={prevTask}
                                    nextTask={nextTask}
                                    currentIndex={currentIndex >= 0 ? currentIndex : 0}
                                    totalTasks={allTasks.length || 1}
                                />
                            </motion.div>
                        ) : null}
                    </div>
                </main>
            </div>
        </div>
    )
}
