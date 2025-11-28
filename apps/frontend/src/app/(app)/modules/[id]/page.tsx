"use client"

/**
 * ============================================================================
 * MODULE DETAIL PAGE — Individual Module View
 * ============================================================================
 *
 * Features:
 * - Module header with progress
 * - Tasks list with completion status
 * - Continue learning button
 * - Prerequisites display
 *
 * @phase A.3 - App Shell & Routing
 */

import { useState, useEffect } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { GlassCard } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import { ProgressBar } from "@/components/ui/progress-bar"
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

interface Task {
    id: string
    title: string
    description: string
    order: number
    isCompleted: boolean
    isLocked: boolean
    estimatedMinutes: number
    xpReward: number
}

interface ModuleDetail {
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
    tasks: Task[]
}

/* ============================================================================
   MOCK DATA (until backend ready)
   ============================================================================ */

const MOCK_MODULE: ModuleDetail = {
    id: "1-3",
    slug: "user-permissions",
    title: "User & Permissions",
    description:
        "Master Linux user management, groups, and file permissions. Learn to secure your system with proper access control.",
    icon: "🔐",
    progress: 40,
    completedTasks: 4,
    totalTasks: 10,
    estimatedHours: 3,
    isLocked: false,
    tasks: [
        {
            id: "t1",
            title: "Understanding Users & Groups",
            description: "Learn about the Linux user model and how groups work",
            order: 1,
            isCompleted: true,
            isLocked: false,
            estimatedMinutes: 15,
            xpReward: 25,
        },
        {
            id: "t2",
            title: "Creating Users with useradd",
            description: "Practice creating new user accounts",
            order: 2,
            isCompleted: true,
            isLocked: false,
            estimatedMinutes: 20,
            xpReward: 30,
        },
        {
            id: "t3",
            title: "Managing Groups",
            description: "Create and manage user groups",
            order: 3,
            isCompleted: true,
            isLocked: false,
            estimatedMinutes: 15,
            xpReward: 25,
        },
        {
            id: "t4",
            title: "File Permissions Basics",
            description: "Understand read, write, and execute permissions",
            order: 4,
            isCompleted: true,
            isLocked: false,
            estimatedMinutes: 25,
            xpReward: 35,
        },
        {
            id: "t5",
            title: "Using chmod",
            description: "Change file permissions with chmod command",
            order: 5,
            isCompleted: false,
            isLocked: false,
            estimatedMinutes: 20,
            xpReward: 30,
        },
        {
            id: "t6",
            title: "Using chown",
            description: "Change file ownership with chown command",
            order: 6,
            isCompleted: false,
            isLocked: false,
            estimatedMinutes: 15,
            xpReward: 25,
        },
        {
            id: "t7",
            title: "Special Permissions",
            description: "Learn about SUID, SGID, and sticky bit",
            order: 7,
            isCompleted: false,
            isLocked: true,
            estimatedMinutes: 30,
            xpReward: 40,
        },
        {
            id: "t8",
            title: "Access Control Lists (ACLs)",
            description: "Advanced file permissions with ACLs",
            order: 8,
            isCompleted: false,
            isLocked: true,
            estimatedMinutes: 25,
            xpReward: 35,
        },
        {
            id: "t9",
            title: "sudo & Elevated Privileges",
            description: "Configure and use sudo for administrative tasks",
            order: 9,
            isCompleted: false,
            isLocked: true,
            estimatedMinutes: 20,
            xpReward: 30,
        },
        {
            id: "t10",
            title: "Module Quiz",
            description: "Test your knowledge of users and permissions",
            order: 10,
            isCompleted: false,
            isLocked: true,
            estimatedMinutes: 15,
            xpReward: 50,
        },
    ],
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

function LockedState({ module }: { module: ModuleDetail }) {
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
   TASK ITEM
   ============================================================================ */

interface TaskItemProps {
    task: Task
    onStart: (taskId: string) => void
}

function TaskItem({ task, onStart }: TaskItemProps) {
    return (
        <div
            className={cn(
                "group relative rounded-xl p-4 transition-all duration-200",
                "border border-neutral-200/50 dark:border-neutral-700/50",
                task.isLocked
                    ? "bg-neutral-50 dark:bg-neutral-800/30 opacity-60"
                    : task.isCompleted
                      ? "bg-success-50/50 dark:bg-success-900/10"
                      : "bg-white dark:bg-neutral-800/50 hover:bg-neutral-50 dark:hover:bg-neutral-800"
            )}
        >
            <div className="flex items-start gap-4">
                {/* Status icon */}
                <div
                    className={cn(
                        "w-10 h-10 rounded-xl flex items-center justify-center shrink-0",
                        task.isLocked
                            ? "bg-neutral-200 dark:bg-neutral-700"
                            : task.isCompleted
                              ? "bg-success-100 dark:bg-success-900/30"
                              : "bg-primary-100 dark:bg-primary-900/30"
                    )}
                >
                    {task.isLocked ? (
                        <Lock className="w-5 h-5 text-neutral-400" />
                    ) : task.isCompleted ? (
                        <CheckCircle2 className="w-5 h-5 text-success-500" />
                    ) : (
                        <Circle className="w-5 h-5 text-primary-500" />
                    )}
                </div>

                {/* Content */}
                <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2 mb-1">
                        <span className="text-xs font-medium text-neutral-400">
                            Task {task.order}
                        </span>
                        {task.isCompleted && (
                            <span className="text-xs text-success-500 font-medium">Completed</span>
                        )}
                    </div>
                    <h3
                        className={cn(
                            "font-semibold mb-1",
                            task.isLocked
                                ? "text-neutral-400 dark:text-neutral-500"
                                : "text-neutral-900 dark:text-white"
                        )}
                    >
                        {task.title}
                    </h3>
                    <p className="text-sm text-neutral-500 dark:text-neutral-400 line-clamp-1">
                        {task.description}
                    </p>

                    {/* Meta */}
                    <div className="flex items-center gap-4 mt-2">
                        <span className="flex items-center gap-1 text-xs text-neutral-400">
                            <Clock className="w-3.5 h-3.5" />
                            {task.estimatedMinutes} min
                        </span>
                        <span className="flex items-center gap-1 text-xs text-primary-500 font-medium">
                            +{task.xpReward} XP
                        </span>
                    </div>
                </div>

                {/* Action */}
                {!task.isLocked && !task.isCompleted && (
                    <Button
                        size="sm"
                        onClick={() => onStart(task.id)}
                        className={cn(
                            "rounded-xl shrink-0",
                            "opacity-0 group-hover:opacity-100 transition-opacity"
                        )}
                    >
                        <Play className="w-4 h-4 mr-1" />
                        Start
                    </Button>
                )}
            </div>
        </div>
    )
}

/* ============================================================================
   MODULE DETAIL PAGE
   ============================================================================ */

export default function ModuleDetailPage() {
    const params = useParams()
    const router = useRouter()
    const slug = params.id as string

    const [module, setModule] = useState<ModuleDetail | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    const fetchModule = async () => {
        setLoading(true)
        setError(null)

        // Simulate API call
        await new Promise((resolve) => setTimeout(resolve, 500))

        // For demo, use mock data if slug matches, otherwise 404
        if (slug === "user-permissions" || slug === "1-3") {
            setModule(MOCK_MODULE)
        } else {
            // Still show mock module for demo purposes
            setModule({
                ...MOCK_MODULE,
                slug,
                title: slug
                    .split("-")
                    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
                    .join(" "),
            })
        }

        setLoading(false)
    }

    useEffect(() => {
        fetchModule()
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [slug])

    const handleStartTask = (taskId: string) => {
        router.push(`/studyflow?module=${slug}&task=${taskId}`)
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
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
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
                <div className="space-y-6">
                    {/* Module Header */}
                    <GlassCard variant="default" padding="lg" radius="xl">
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
                                <h1 className="text-2xl font-bold text-neutral-900 dark:text-white mb-2">
                                    {module.title}
                                </h1>
                                <p className="text-neutral-600 dark:text-neutral-400 mb-4">
                                    {module.description}
                                </p>

                                {/* Stats */}
                                <div className="flex flex-wrap items-center gap-4 mb-4">
                                    <span className="flex items-center gap-1.5 text-sm text-neutral-500">
                                        <BookOpen className="w-4 h-4" />
                                        {module.totalTasks} tasks
                                    </span>
                                    <span className="flex items-center gap-1.5 text-sm text-neutral-500">
                                        <Clock className="w-4 h-4" />
                                        {module.estimatedHours}h estimated
                                    </span>
                                    <span className="flex items-center gap-1.5 text-sm text-success-500 font-medium">
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
                                        <span className="font-semibold text-primary-500">
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
                    </GlassCard>

                    {/* Tasks List */}
                    <div>
                        <h2 className="text-lg font-semibold text-neutral-900 dark:text-white mb-4">
                            Tasks
                        </h2>
                        <div className="space-y-3">
                            {module.tasks.map((task) => (
                                <TaskItem key={task.id} task={task} onStart={handleStartTask} />
                            ))}
                        </div>
                    </div>
                </div>
            ) : null}
        </div>
    )
}
