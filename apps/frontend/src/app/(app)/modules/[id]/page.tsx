"use client"

/**
 * ============================================================================
 * MODULE DETAIL PAGE — Premium SkillsMaps-Style Design
 * ============================================================================
 *
 * Features:
 * - Glassmorphism header with colored glow
 * - Framer Motion animations
 * - Premium NodeCard-style task cards
 * - Progress bar with glow effect
 * - XP indicators in amber
 * - Matches SkillsMaps design exactly
 *
 * @phase DESIGN-UNIFICATION
 */

import { useState, useEffect } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import { motion } from "framer-motion"
import { PageLayout, Section, Headline } from "@saas/ui"
import { Button } from "@/components/ui/button"
import { useBookmarks } from "@/hooks/useBookmarks"
import { getModule } from "@/lib/modules"
import { getTasksForModule } from "@/lib/tasks"
import { cn } from "@/lib/utils"
import {
    ArrowLeft,
    Play,
    CheckCircle2,
    Clock,
    BookOpen,
    Zap,
    ChevronRight,
    RefreshCw,
    AlertCircle,
    Sparkles,
    Loader2,
    Star,
    Code2,
    Layers,
    Rocket,
    Trophy,
    HelpCircle,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface TaskUI {
    id: string
    title: string
    description: string
    orderIndex: number
    isCompleted: boolean
    estimatedMinutes: number
    xpReward: number
    type: "concept" | "practice" | "deep_dive" | "project" | "challenge" | "quiz"
    difficulty: "easy" | "medium" | "hard" | "expert"
    status: "not_started" | "in_progress" | "complete"
}

interface ModuleDetailUI {
    id: string
    slug: string
    title: string
    description: string
    icon: string
    color: string
    totalTasks: number
    completedTasks: number
    totalXP: number
    estimatedHours: number
    difficulty: "beginner" | "intermediate" | "advanced" | "expert"
    tasks: TaskUI[]
}

/* ============================================================================
   TYPE CONFIG
   ============================================================================ */

const typeConfig: Record<string, {
    label: string
    icon: React.ElementType
    emoji: string
    colorClass: string
    bgClass: string
}> = {
    concept: {
        label: "Koncept",
        icon: BookOpen,
        emoji: "📚",
        colorClass: "text-blue-400",
        bgClass: "bg-blue-500/20",
    },
    practice: {
        label: "Praktik",
        icon: Code2,
        emoji: "💻",
        colorClass: "text-emerald-400",
        bgClass: "bg-emerald-500/20",
    },
    deep_dive: {
        label: "Fördjupning",
        icon: Layers,
        emoji: "🔍",
        colorClass: "text-violet-400",
        bgClass: "bg-violet-500/20",
    },
    project: {
        label: "Projekt",
        icon: Rocket,
        emoji: "🚀",
        colorClass: "text-orange-400",
        bgClass: "bg-orange-500/20",
    },
    challenge: {
        label: "Utmaning",
        icon: Trophy,
        emoji: "🏆",
        colorClass: "text-rose-400",
        bgClass: "bg-rose-500/20",
    },
    quiz: {
        label: "Quiz",
        icon: HelpCircle,
        emoji: "❓",
        colorClass: "text-cyan-400",
        bgClass: "bg-cyan-500/20",
    },
}

/* ============================================================================
   MODULE COLORS
   ============================================================================ */

const moduleColors: Record<string, { color: string; icon: string }> = {
    "environment-tooling-setup": { color: "#6366f1", icon: "🛠️" },
    "linux-mastery": { color: "#FCC624", icon: "🐧" },
    "shell-scripting-automation": { color: "#4EAA25", icon: "💻" },
    "git-collaborative-workflows": { color: "#F05032", icon: "🔀" },
    "python-for-devops": { color: "#3776AB", icon: "🐍" },
    "aws-core-services": { color: "#FF9900", icon: "☁️" },
    "infrastructure-as-code-terraform": { color: "#7B42BC", icon: "🏗️" },
    "serverless-architecture": { color: "#FF6B35", icon: "⚡" },
    "networking-security": { color: "#00D4AA", icon: "🔐" },
    "docker-mastery": { color: "#2496ED", icon: "🐳" },
    "docker-fundamentals": { color: "#2496ED", icon: "🐳" },
    "docker-advanced-production": { color: "#066DA5", icon: "🐋" },
    "kubernetes-core": { color: "#326CE5", icon: "☸️" },
    "kubernetes-advanced-gitops": { color: "#1D4ED8", icon: "🚀" },
    "observability-monitoring": { color: "#E6522C", icon: "📊" },
    "sre-devsecops-capstone": { color: "#10B981", icon: "🎯" },
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

function DetailSkeleton() {
    return (
        <div className="space-y-6 animate-pulse">
            <div className="h-48 rounded-3xl bg-zinc-800/50" />
            <div className="space-y-4">
                {Array.from({ length: 5 }).map((_, i) => (
                    <div key={i} className="h-28 rounded-2xl bg-zinc-800/50" />
                ))}
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
                Modulen hittades inte
            </h2>
            <p className="text-zinc-400 mb-6">{error}</p>
            <div className="flex gap-3 justify-center">
                <Link href="/modules">
                    <Button variant="outline" className="rounded-xl">
                        <ArrowLeft className="w-4 h-4 mr-2" />
                        Tillbaka
                    </Button>
                </Link>
                <Button onClick={onRetry} className="rounded-xl">
                    <RefreshCw className="w-4 h-4 mr-2" />
                    Försök igen
                </Button>
            </div>
        </div>
    )
}

/* ============================================================================
   MODULE HEADER
   ============================================================================ */

function ModuleHeader({ module }: { module: ModuleDetailUI }) {
    const progress = module.totalTasks > 0
        ? Math.round((module.completedTasks / module.totalTasks) * 100)
        : 0
    const isComplete = progress === 100

    return (
        <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "relative overflow-hidden rounded-3xl",
                "bg-gradient-to-br from-zinc-900 via-zinc-900/95 to-zinc-950",
                "border border-white/10",
                "p-8"
            )}
        >
            {/* Colored glow based on module color */}
            <div
                className="absolute top-0 right-0 w-[400px] h-[400px] rounded-full blur-[120px] opacity-20"
                style={{ backgroundColor: module.color }}
            />

            {/* Sparkle for complete */}
            {isComplete && (
                <motion.div
                    className="absolute top-6 right-6 text-emerald-400"
                    animate={{ rotate: 360 }}
                    transition={{ duration: 4, repeat: Infinity, ease: "linear" }}
                >
                    <Sparkles className="w-6 h-6" />
                </motion.div>
            )}

            <div className="relative flex flex-col md:flex-row md:items-start gap-6">
                {/* Icon */}
                <motion.div
                    className={cn(
                        "w-20 h-20 rounded-2xl flex items-center justify-center shrink-0",
                        "bg-gradient-to-br from-white/10 to-white/5",
                        "border border-white/10"
                    )}
                    style={{ boxShadow: `0 0 40px ${module.color}30` }}
                    whileHover={{ scale: 1.05 }}
                >
                    <span className="text-5xl">{module.icon}</span>
                </motion.div>

                {/* Content */}
                <div className="flex-1">
                    <h1 className={cn(
                        "text-3xl md:text-4xl font-black mb-2",
                        "bg-gradient-to-r from-white to-white/80 bg-clip-text text-transparent"
                    )}>
                        {module.title}
                    </h1>
                    <p className="text-zinc-400 mb-4 max-w-2xl">
                        {module.description}
                    </p>

                    {/* Meta row */}
                    <div className="flex flex-wrap items-center gap-4 mb-4 text-sm">
                        <span className="flex items-center gap-1.5 text-zinc-400">
                            <BookOpen className="w-4 h-4" />
                            {module.totalTasks} tasks
                        </span>
                        <span className="flex items-center gap-1.5 text-zinc-400">
                            <Clock className="w-4 h-4" />
                            ~{module.estimatedHours}h
                        </span>
                        <span className="flex items-center gap-1.5 text-amber-400 font-medium">
                            <Zap className="w-4 h-4" />
                            {module.totalXP} XP totalt
                        </span>
                        <span className={cn(
                            "flex items-center gap-1.5 font-medium",
                            isComplete ? "text-emerald-400" : "text-purple-400"
                        )}>
                            <CheckCircle2 className="w-4 h-4" />
                            {module.completedTasks}/{module.totalTasks} klara
                        </span>
                    </div>

                    {/* Progress */}
                    <div className="max-w-md">
                        <div className="flex items-center justify-between text-sm mb-2">
                            <span className="text-zinc-500">Progress</span>
                            <span className={cn(
                                "font-bold",
                                isComplete ? "text-emerald-400" : "text-purple-400"
                            )}>
                                {progress}%
                            </span>
                        </div>
                        <div className="h-2.5 bg-zinc-800 rounded-full overflow-hidden">
                            <motion.div
                                className="h-full rounded-full"
                                style={{
                                    background: isComplete
                                        ? "linear-gradient(90deg, #10b981, #14b8a6)"
                                        : `linear-gradient(90deg, ${module.color}, ${module.color}cc)`,
                                    boxShadow: `0 0 15px ${isComplete ? "#10b981" : module.color}50`,
                                }}
                                initial={{ width: 0 }}
                                animate={{ width: `${progress}%` }}
                                transition={{ duration: 1, ease: "easeOut" }}
                            />
                        </div>
                    </div>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   TASK CARD — Premium Style matching NodeCard
   ============================================================================ */

function TaskCard({
    task,
    onClick,
    isBookmarked,
    onToggleBookmark,
}: {
    task: TaskUI
    onClick: (id: string) => void
    isBookmarked: boolean
    onToggleBookmark: (id: string) => void
}) {
    const [isHovered, setIsHovered] = useState(false)
    const [bookmarkLoading, setBookmarkLoading] = useState(false)

    const config = typeConfig[task.type] || typeConfig.concept
    const isComplete = task.status === "complete"
    const isInProgress = task.status === "in_progress"

    const handleBookmark = async (e: React.MouseEvent) => {
        e.stopPropagation()
        setBookmarkLoading(true)
        try {
            onToggleBookmark(task.id)
        } finally {
            setBookmarkLoading(false)
        }
    }

    return (
        <motion.div
            className={cn(
                "group relative h-full",
                "rounded-2xl",
                "bg-zinc-900/80 backdrop-blur-sm",
                "border border-zinc-800/80",
                "transition-all duration-300",
                isHovered && "border-zinc-700/80 shadow-[0_8px_30px_rgba(0,0,0,0.4)]",
                isComplete && "opacity-75",
                "cursor-pointer"
            )}
            onClick={() => onClick(task.id)}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            whileHover={{ y: -4, scale: 1.02 }}
            transition={{ duration: 0.2 }}
        >
            <div className="p-5 flex flex-col h-full">
                {/* Top Row: Icon + Type Badge + Bookmark */}
                <div className="flex items-start justify-between mb-4">
                    {/* Icon container */}
                    <motion.div
                        className={cn(
                            "w-12 h-12 rounded-xl flex items-center justify-center",
                            config.bgClass,
                            "border border-white/5"
                        )}
                        animate={isHovered ? { scale: 1.05 } : { scale: 1 }}
                        transition={{ duration: 0.2 }}
                    >
                        <span className="text-2xl">{config.emoji}</span>
                    </motion.div>

                    {/* Right side: Status + Bookmark */}
                    <div className="flex items-center gap-2">
                        <motion.button
                            onClick={handleBookmark}
                            className={cn(
                                "p-1.5 rounded-lg transition-all duration-200",
                                isBookmarked
                                    ? "text-amber-400 bg-amber-500/20"
                                    : "text-zinc-500 hover:text-amber-400 hover:bg-amber-500/10"
                            )}
                            whileHover={{ scale: 1.1 }}
                            whileTap={{ scale: 0.9 }}
                            disabled={bookmarkLoading}
                        >
                            {bookmarkLoading ? (
                                <Loader2 className="w-4 h-4 animate-spin" />
                            ) : (
                                <Star className={cn("w-4 h-4", isBookmarked && "fill-current")} />
                            )}
                        </motion.button>

                        {isComplete && (
                            <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-emerald-500/20">
                                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                                <span className="text-xs font-medium text-emerald-300">Klar</span>
                            </div>
                        )}
                        {isInProgress && (
                            <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-purple-500/20">
                                <Loader2 className="w-3.5 h-3.5 text-purple-400 animate-spin" />
                                <span className="text-xs font-medium text-purple-300">Pågår</span>
                            </div>
                        )}
                        {!isComplete && !isInProgress && (
                            <span className={cn(
                                "px-2.5 py-1 rounded-full text-xs font-medium",
                                config.bgClass,
                                config.colorClass
                            )}>
                                {config.label}
                            </span>
                        )}
                    </div>
                </div>

                {/* Task number */}
                <span className="text-xs font-medium text-zinc-600 uppercase tracking-wide">
                    Task {task.orderIndex}
                </span>

                {/* Title */}
                <h3 className={cn(
                    "mt-1 text-lg font-semibold leading-tight",
                    "text-white",
                    isComplete && "text-zinc-400"
                )}>
                    {task.title}
                </h3>

                {/* Description - flex-grow to push meta to bottom */}
                <div className="flex-grow">
                    {task.description && (
                        <p className="mt-2 text-sm text-zinc-500 line-clamp-3">
                            {task.description}
                        </p>
                    )}
                </div>

                {/* Meta row - always at bottom */}
                <div className="flex flex-wrap items-center gap-3 mt-4 pt-4 border-t border-zinc-800">
                    {/* Time */}
                    <div className="flex items-center gap-1.5 text-zinc-500">
                        <Clock className="w-3.5 h-3.5" />
                        <span className="text-xs font-medium">{task.estimatedMinutes} min</span>
                    </div>

                    {/* XP */}
                    <div className="flex items-center gap-1.5 text-amber-400">
                        <Zap className="w-3.5 h-3.5" />
                        <span className="text-xs font-bold">{task.xpReward} XP</span>
                    </div>

                    {/* Difficulty */}
                    <DifficultyDots difficulty={task.difficulty} />

                    {/* Action button */}
                    {!isComplete && (
                        <motion.button
                            onClick={(e) => {
                                e.stopPropagation()
                                onClick(task.id)
                            }}
                            className={cn(
                                "ml-auto flex items-center gap-1.5 px-4 py-2 rounded-xl",
                                "text-sm font-medium transition-all duration-200",
                                "bg-white text-zinc-900",
                                "hover:bg-zinc-100"
                            )}
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                        >
                            {isInProgress ? (
                                <>
                                    <span>Fortsätt</span>
                                    <ChevronRight className="w-4 h-4" />
                                </>
                            ) : (
                                <>
                                    <Play className="w-3.5 h-3.5" />
                                    <span>Börja</span>
                                </>
                            )}
                        </motion.button>
                    )}

                    {isComplete && (
                        <motion.button
                            onClick={(e) => {
                                e.stopPropagation()
                                onClick(task.id)
                            }}
                            className={cn(
                                "ml-auto flex items-center gap-1.5 px-4 py-2 rounded-xl",
                                "text-sm font-medium transition-all duration-200",
                                "bg-zinc-800 text-zinc-400",
                                "hover:bg-zinc-700 hover:text-zinc-300"
                            )}
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                        >
                            <span>Granska</span>
                            <ChevronRight className="w-4 h-4" />
                        </motion.button>
                    )}
                </div>
            </div>

            {/* Progress indicator for in-progress */}
            {isInProgress && (
                <div className="absolute bottom-0 left-0 right-0 h-1 bg-zinc-800 rounded-b-2xl overflow-hidden">
                    <motion.div
                        className="h-full bg-purple-500"
                        initial={{ width: "0%" }}
                        animate={{ width: "33%" }}
                        transition={{ duration: 0.5 }}
                    />
                </div>
            )}
        </motion.div>
    )
}

/* ============================================================================
   MODULE DETAIL PAGE
   ============================================================================ */

export default function ModuleDetailPage() {
    const params = useParams()
    const router = useRouter()
    const moduleId = params?.id as string
    const { isBookmarked, toggleBookmark } = useBookmarks()

    const [module, setModule] = useState<ModuleDetailUI | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    const fetchModule = async () => {
        setLoading(true)
        setError(null)

        try {
            const moduleResult = await getModule(moduleId)
            if (!moduleResult.ok) {
                setError(moduleResult.message)
                setLoading(false)
                return
            }

            const moduleData = moduleResult.data
            const tasksResult = await getTasksForModule(moduleId)

            const moduleConfig = moduleColors[moduleData.slug] || {
                color: "#6366f1",
                icon: "📚"
            }

            const tierToType: Record<string, TaskUI["type"]> = {
                "standard": "concept",
                "advanced": "practice",
                "deep_dive": "deep_dive",
            }

            const difficultyMap: Record<string, TaskUI["difficulty"]> = {
                "easy": "easy",
                "medium": "medium",
                "hard": "hard",
            }

            const tasks: TaskUI[] = tasksResult.ok
                ? tasksResult.data.map((t, index) => ({
                    id: t.id,
                    title: t.title,
                    description: t.description || "",
                    orderIndex: t.order_index || index + 1,
                    isCompleted: false,
                    estimatedMinutes: t.estimated_minutes || 15,
                    xpReward: t.xp_reward || 25,
                    type: tierToType[t.task_tier] || "concept",
                    difficulty: difficultyMap[t.difficulty] || "medium",
                    status: "not_started" as const,
                }))
                : []

            const totalXP = tasks.reduce((sum, t) => sum + t.xpReward, 0)

            const moduleUI: ModuleDetailUI = {
                id: moduleData.id,
                slug: moduleData.slug,
                title: moduleData.name,
                description: moduleData.description || "",
                icon: moduleConfig.icon,
                color: moduleConfig.color,
                totalTasks: tasks.length,
                completedTasks: 0,
                totalXP,
                estimatedHours: moduleData.estimated_hours || Math.ceil(tasks.length * 0.25),
                difficulty: moduleData.difficulty as ModuleDetailUI["difficulty"] || "intermediate",
                tasks,
            }

            setModule(moduleUI)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Failed to load module")
        } finally {
            setLoading(false)
        }
    }

    useEffect(() => {
        fetchModule()
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [moduleId])

    const handleTaskClick = (taskId: string) => {
        router.push(`/modules/${moduleId}/tasks/${taskId}`)
    }

    const nextTask = module?.tasks.find(t => t.status !== "complete")

    const handleContinue = () => {
        if (nextTask) {
            handleTaskClick(nextTask.id)
        }
    }

    return (
        <PageLayout maxWidth="standard" background="gray">
            {/* Back button */}
            <Link
                href="/modules"
                className={cn(
                    "inline-flex items-center gap-2 text-sm mb-6",
                    "text-zinc-500 hover:text-white",
                    "transition-colors"
                )}
            >
                <ArrowLeft className="w-4 h-4" />
                Tillbaka till Camp DevOps
            </Link>

            {loading ? (
                <DetailSkeleton />
            ) : error ? (
                <ErrorState error={error} onRetry={fetchModule} />
            ) : module ? (
                <motion.div
                    className="space-y-8"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                >
                    {/* Header */}
                    <ModuleHeader module={module} />

                    {/* Continue button */}
                    {nextTask && (
                        <motion.div
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.2 }}
                        >
                            <Button
                                onClick={handleContinue}
                                size="lg"
                                className={cn(
                                    "rounded-xl px-6",
                                    "bg-gradient-to-r from-purple-600 to-indigo-600",
                                    "hover:from-purple-500 hover:to-indigo-500",
                                    "shadow-[0_0_20px_rgba(139,92,246,0.3)]"
                                )}
                            >
                                <Play className="w-4 h-4 mr-2" />
                                Fortsätt: {nextTask.title}
                                <ChevronRight className="w-4 h-4 ml-2" />
                            </Button>
                        </motion.div>
                    )}

                    {/* Tasks grid */}
                    <Section>
                        <Headline level={2} className="mb-6 text-white">
                            Tasks
                        </Headline>
                        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
                            {module.tasks.map((task, index) => (
                                <motion.div
                                    key={task.id}
                                    initial={{ opacity: 0, y: 20 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: 0.1 + index * 0.03 }}
                                >
                                    <TaskCard
                                        task={task}
                                        onClick={handleTaskClick}
                                        isBookmarked={isBookmarked(task.id)}
                                        onToggleBookmark={toggleBookmark}
                                    />
                                </motion.div>
                            ))}
                        </div>
                    </Section>
                </motion.div>
            ) : null}
        </PageLayout>
    )
}
