"use client"

/**
 * ============================================================================
 * MODULE DETAIL PAGE — Individual Module View
 * ============================================================================
 *
 * Features:
 * - Module header with progress
 * - Tasks list with completion status (using TaskCard!)
 * - Bookmark and reminder badges
 * - Continue learning button
 * - Prerequisites display
 *
 * @phase A.3 - App Shell & Routing (Updated to use real API)
 * @design PHASE 2 — Design System Application Layer
 */

import { useState, useEffect } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import { PageLayout, Section, Block, Headline, Subtext, cn } from "@saas/ui"
import { GlassCard } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import { ProgressBar } from "@/components/ui/progress-bar"
import { TaskCard, TaskCardStatus, TaskType } from "@/components/modules/TaskCard"
import { useBookmarks } from "@/hooks/useBookmarks"
import { getModule, ModulePublic } from "@/lib/modules"
import { getTasksForModule, TaskPublic } from "@/lib/tasks"
import {
    ArrowLeft,
    Play,
    CheckCircle2,
    Circle,
    Lock,
    Clock,
    BookOpen,
    ChevronRight,
    RefreshCw,
    AlertCircle,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface TaskUI {
    id: string
    title: string
    description: string
    order: number
    isCompleted: boolean
    isLocked: boolean
    estimatedMinutes: number
    xpReward: number
    type: TaskType
    difficulty: number
}

interface ModuleDetailUI {
    id: string
    slug: string
    title: string
    description: string
    icon: string
    progress: number
    completedTasks: number
    totalTasks: number
    estimatedHours: number
    isLocked: boolean
    prerequisiteModule?: {
        slug: string
        title: string
    }
    tasks: TaskUI[]
}

// Map difficulty to icon
const DIFFICULTY_ICONS: Record<string, string> = {
    beginner: "🌱",
    intermediate: "🌿",
    advanced: "🌳",
    expert: "🏔️",
}

/* ============================================================================
   SKELETON
   ============================================================================ */

function ModuleDetailSkeleton() {
    return (
        <div className="space-y-6 animate-pulse">
            <div className="h-48 rounded-2xl bg-neutral-200 dark:bg-neutral-800" />
            <div className="space-y-3">
                {Array.from({ length: 5 }).map((_, i) => (
                    <div
                        key={i}
                        className="h-20 rounded-xl bg-neutral-200 dark:bg-neutral-800"
                    />
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
        <GlassCard
            variant="default"
            padding="xl"
            radius="xl"
            className="max-w-md mx-auto text-center"
        >
            <div
                className={cn(
                    "w-16 h-16 rounded-full mx-auto mb-4",
                    "bg-red-100 dark:bg-red-900/30",
                    "flex items-center justify-center"
                )}
            >
                <AlertCircle className="w-8 h-8 text-red-500" />
            </div>
            <h2 className="text-xl font-semibold text-neutral-900 dark:text-white mb-2">
                Module Not Found
            </h2>
            <p className="text-neutral-600 dark:text-neutral-400 mb-6">{error}</p>
            <div className="flex gap-3 justify-center">
                <Link href="/modules">
                    <Button variant="outline" className="rounded-xl">
                        <ArrowLeft className="w-4 h-4 mr-2" />
                        Back to Modules
                    </Button>
                </Link>
                <Button onClick={onRetry} className="rounded-xl">
                    <RefreshCw className="w-4 h-4 mr-2" />
                    Try Again
                </Button>
            </div>
        </GlassCard>
    )
}

/* ============================================================================
   LOCKED STATE
   ============================================================================ */

function LockedState({ module }: { module: ModuleDetailUI }) {
    return (
        <GlassCard
            variant="default"
            padding="xl"
            radius="xl"
            className="max-w-md mx-auto text-center"
        >
            <div
                className={cn(
                    "w-16 h-16 rounded-full mx-auto mb-4",
                    "bg-neutral-100 dark:bg-neutral-800",
                    "flex items-center justify-center"
                )}
            >
                <Lock className="w-8 h-8 text-neutral-400" />
            </div>
            <h2 className="text-xl font-semibold text-neutral-900 dark:text-white mb-2">
                Module Locked
            </h2>
            <p className="text-neutral-600 dark:text-neutral-400 mb-6">
                Complete the prerequisite module to unlock this content.
            </p>
            {module.prerequisiteModule && (
                <Link href={`/modules/${module.prerequisiteModule.slug}`}>
                    <Button className="rounded-xl">
                        Go to {module.prerequisiteModule.title}
                        <ChevronRight className="w-4 h-4 ml-2" />
                    </Button>
                </Link>
            )}
        </GlassCard>
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
            // Fetch module details from API
            const moduleResult = await getModule(moduleId)
            if (!moduleResult.ok) {
                setError(moduleResult.message)
                setLoading(false)
                return
            }

            const moduleData = moduleResult.data

            // Fetch tasks for this module
            const tasksResult = await getTasksForModule(moduleId)
            
            // Map difficulty string to number
            const difficultyMap: Record<string, number> = {
                "easy": 1,
                "medium": 3,
                "hard": 5
            }
            
            // Map task_tier to TaskType
            const tierToType: Record<string, TaskType> = {
                "standard": "foundation",
                "advanced": "practice",
                "deep_dive": "deepening"
            }
            
            const tasks: TaskUI[] = tasksResult.ok
                ? tasksResult.data.map((t, index) => ({
                    id: t.id,
                    title: t.title,
                    description: t.description || "",
                    order: t.order_index || index + 1,
                    isCompleted: false, // TODO: Get from progress API
                    isLocked: false, // TODO: Implement prerequisites logic
                    estimatedMinutes: t.estimated_minutes || 15,
                    xpReward: t.xp_reward || 25,
                    type: tierToType[t.task_tier] || "foundation",
                    difficulty: difficultyMap[t.difficulty] || 3,
                }))
                : []

            // Convert API data to UI format
            const moduleUI: ModuleDetailUI = {
                id: moduleData.id,
                slug: moduleData.slug,
                title: moduleData.name,
                description: moduleData.description || "",
                icon: DIFFICULTY_ICONS[moduleData.difficulty] || "📚",
                progress: 0, // TODO: Calculate from completed tasks
                completedTasks: 0, // TODO: Get from progress API
                totalTasks: tasks.length,
                estimatedHours: moduleData.estimated_hours || Math.ceil(tasks.length * 0.25),
                isLocked: false,
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

    const handleStartTask = (taskId: string) => {
        router.push(`/modules/${moduleId}/tasks/${taskId}`)
    }

    const handleContinue = () => {
        const nextTask = module?.tasks.find((t) => !t.isCompleted && !t.isLocked)
        if (nextTask) {
            handleStartTask(nextTask.id)
        }
    }

    // Find next incomplete task
    const nextTask = module?.tasks.find((t) => !t.isCompleted && !t.isLocked)

    return (
        <PageLayout maxWidth="standard" background="subtle">
            {/* Back button */}
            <Link
                href="/modules"
                className={cn(
                    "inline-flex items-center gap-2 text-sm mb-6",
                    "text-neutral-500 hover:text-neutral-900",
                    "dark:text-neutral-400 dark:hover:text-white",
                    "transition-colors"
                )}
            >
                <ArrowLeft className="w-4 h-4" />
                Back to Modules
            </Link>

            {loading ? (
                <ModuleDetailSkeleton />
            ) : error ? (
                <ErrorState error={error} onRetry={fetchModule} />
            ) : module?.isLocked ? (
                <LockedState module={module} />
            ) : module ? (
                <div className="space-y-8">
                    {/* Module Header */}
                    <Section>
                        <Block className="bg-white/80 dark:bg-neutral-900/80 backdrop-blur-xl rounded-2xl border border-neutral-200/50 dark:border-neutral-700/50 shadow-lg p-6 md:p-8">
                            <div className="flex flex-col md:flex-row md:items-start gap-6">
                                {/* Icon */}
                                <div
                                    className={cn(
                                        "w-20 h-20 rounded-2xl flex items-center justify-center shrink-0",
                                        "bg-gradient-to-br from-primary-100 to-primary-50",
                                        "dark:from-primary-900/30 dark:to-primary-800/20"
                                    )}
                                >
                                    <span className="text-4xl">{module.icon}</span>
                                </div>

                                {/* Content */}
                                <div className="flex-1">
                                    <Headline level={1} className="mb-2">
                                        {module.title}
                                    </Headline>
                                    <Subtext className="mb-4">
                                        {module.description}
                                    </Subtext>

                                    <div className="flex flex-wrap items-center gap-4 mb-4">
                                        <span className="flex items-center gap-1.5 text-sm text-neutral-500">
                                            <BookOpen className="w-4 h-4" />
                                            {module.totalTasks} tasks
                                        </span>
                                        <span className="flex items-center gap-1.5 text-sm text-neutral-500">
                                            <Clock className="w-4 h-4" />
                                            {module.estimatedHours}h estimated
                                        </span>
                                        <span className="flex items-center gap-1.5 text-sm text-emerald-500 font-medium">
                                            <CheckCircle2 className="w-4 h-4" />
                                            {module.completedTasks}/{module.totalTasks} completed
                                        </span>
                                    </div>

                                    {/* Progress */}
                                    <div className="mb-4">
                                        <div className="flex items-center justify-between text-sm mb-2">
                                            <span className="text-neutral-600 dark:text-neutral-400">
                                                Progress
                                            </span>
                                            <span className="font-semibold text-indigo-500">
                                                {module.progress}%
                                            </span>
                                        </div>
                                        <ProgressBar value={module.progress} className="h-2" />
                                    </div>

                                    {/* Continue button */}
                                    {nextTask && (
                                        <Button onClick={handleContinue} className="rounded-xl">
                                            <Play className="w-4 h-4 mr-2" />
                                            Continue: {nextTask.title}
                                        </Button>
                                    )}
                                </div>
                            </div>
                        </Block>
                    </Section>

                    {/* Tasks List */}
                    <Section>
                        <Headline level={2} className="mb-4">
                            Tasks
                        </Headline>
                        <div className="space-y-4">
                            {module.tasks.map((task) => {
                                const taskStatus: TaskCardStatus = task.isCompleted
                                    ? "complete"
                                    : task.isLocked
                                        ? "not_started"
                                        : "not_started"

                                return (
                                    <TaskCard
                                        key={task.id}
                                        id={task.id}
                                        orderIndex={task.order}
                                        title={task.title}
                                        description={task.description}
                                        type={task.type}
                                        difficulty={task.difficulty}
                                        xpReward={task.xpReward}
                                        estimatedMinutes={task.estimatedMinutes}
                                        status={taskStatus}
                                        onClick={handleStartTask}
                                        isBookmarked={isBookmarked(task.id)}
                                        onToggleBookmark={toggleBookmark}
                                    />
                                )
                            })}
                        </div>
                    </Section>
                </div>
            ) : null}
        </PageLayout>
    )
}
