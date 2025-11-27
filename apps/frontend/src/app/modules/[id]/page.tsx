"use client"

/**
 * ============================================================================
 * MODULE DETAIL PAGE — Apple-Inspired Design (D.4)
 * ============================================================================
 *
 * Beautiful module detail page with:
 * - Hero section with icon, title, progress ring
 * - Info cards row
 * - Tasks list with TaskCard components
 * - Prerequisites section
 * - Sticky progress sidebar on desktop
 *
 * @phase D.4 - Modules UI
 */

import { useState, useEffect } from "react"
import { useParams } from "next/navigation"
import Link from "next/link"
import { getModule, ModulePublic } from "@/lib/modules"
import { useAuth } from "@/components/auth"
import { Protected } from "@/components/auth/Protected"
import { cn } from "@/lib/utils"
import { AppShell } from "@/components/layout"
import { GlassCard } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import {
    ModuleHeader,
    ModuleProgress,
    TaskCard,
    PrerequisitesSection,
    type TaskType,
    type TaskCardStatus,
    type MiniTask,
    type Prerequisite
} from "@/components/modules"
import {
    ArrowLeft,
    AlertCircle,
    RefreshCw,
    BookOpen,
    Clock,
    Zap,
    CheckCircle2
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface Task {
    id: string
    orderIndex: number
    title: string
    description?: string
    type: TaskType
    difficulty: number
    xpReward: number
    status: TaskCardStatus
}

/* ============================================================================
   SKELETON COMPONENTS
   ============================================================================ */

function TaskSkeleton() {
    return (
        <div className={cn(
            "rounded-xl p-4 animate-pulse",
            "bg-white dark:bg-neutral-800/50",
            "border border-neutral-200/50 dark:border-neutral-700/50"
        )}>
            <div className="flex items-center gap-3">
                <div className="w-6 h-6 rounded-full bg-neutral-200 dark:bg-neutral-700" />
                <div className="flex-1">
                    <div className="h-4 w-32 mb-1 rounded bg-neutral-200 dark:bg-neutral-700" />
                    <div className="h-5 w-3/4 rounded bg-neutral-200 dark:bg-neutral-700" />
                </div>
                <div className="h-6 w-16 rounded-full bg-neutral-200 dark:bg-neutral-700" />
            </div>
        </div>
    )
}

function PageSkeleton() {
    return (
        <div className="space-y-6 animate-fade-in">
            {/* Header skeleton */}
            <div className="rounded-2xl p-8 bg-white dark:bg-neutral-800/50">
                <div className="flex items-start justify-between">
                    <div className="flex-1">
                        <div className="w-16 h-16 mb-4 rounded-xl bg-neutral-200 dark:bg-neutral-700" />
                        <div className="h-8 w-64 mb-2 rounded bg-neutral-200 dark:bg-neutral-700" />
                        <div className="h-4 w-96 mb-4 rounded bg-neutral-200 dark:bg-neutral-700" />
                        <div className="flex gap-3">
                            {Array.from({ length: 3 }).map((_, i) => (
                                <div key={i} className="h-8 w-24 rounded-full bg-neutral-200 dark:bg-neutral-700" />
                            ))}
                        </div>
                    </div>
                    <div className="w-24 h-24 rounded-full bg-neutral-200 dark:bg-neutral-700" />
                </div>
            </div>

            <div className="grid lg:grid-cols-3 gap-6">
                {/* Tasks skeleton */}
                <div className="lg:col-span-2 space-y-4">
                    <div className="h-6 w-24 rounded bg-neutral-200 dark:bg-neutral-700" />
                    {Array.from({ length: 5 }).map((_, i) => (
                        <TaskSkeleton key={i} />
                    ))}
                </div>
                {/* Sidebar skeleton */}
                <div className="rounded-2xl p-6 h-96 bg-white dark:bg-neutral-800/50" />
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
            className="max-w-md mx-auto text-center animate-fade-in"
        >
            <div className={cn(
                "w-16 h-16 rounded-full mx-auto mb-4",
                "bg-red-100 dark:bg-red-900/30",
                "flex items-center justify-center"
            )}>
                <AlertCircle className="w-8 h-8 text-red-500" />
            </div>
            <h2 className="text-xl font-semibold text-neutral-900 dark:text-white mb-2">
                Unable to Load Module
            </h2>
            <p className="text-neutral-600 dark:text-neutral-400 mb-6">
                {error}
            </p>
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
   INFO CARDS ROW
   ============================================================================ */

interface InfoCardsProps {
    tasksCount: number
    estimatedHours: number
    totalXP: number
    prerequisitesCount: number
}

function InfoCardsRow({
    tasksCount,
    estimatedHours,
    totalXP,
    prerequisitesCount
}: InfoCardsProps) {
    const cards = [
        {
            icon: BookOpen,
            label: "Tasks",
            value: tasksCount,
            color: "primary"
        },
        {
            icon: Clock,
            label: "Est. Hours",
            value: estimatedHours,
            color: "info"
        },
        {
            icon: Zap,
            label: "XP Available",
            value: totalXP,
            color: "xp"
        },
        {
            icon: CheckCircle2,
            label: "Prerequisites",
            value: prerequisitesCount,
            color: "success"
        }
    ]

    return (
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {cards.map((card) => (
                <GlassCard
                    key={card.label}
                    variant="default"
                    padding="md"
                    radius="xl"
                    className="text-center"
                >
                    <card.icon className={cn(
                        "w-6 h-6 mx-auto mb-2",
                        card.color === "primary" && "text-primary-500",
                        card.color === "info" && "text-info-500",
                        card.color === "xp" && "text-xp-500",
                        card.color === "success" && "text-success-500"
                    )} />
                    <div className="text-2xl font-bold text-neutral-900 dark:text-white">
                        {card.value}
                    </div>
                    <div className="text-xs text-neutral-500">
                        {card.label}
                    </div>
                </GlassCard>
            ))}
        </div>
    )
}

/* ============================================================================
   MODULE CONTENT
   ============================================================================ */

function ModuleContent() {
    const params = useParams()
    const moduleId = params?.id as string | undefined
    useAuth()

    const [module, setModule] = useState<ModulePublic | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    // Mock task data (would come from backend)
    const [tasks] = useState<Task[]>([
        {
            id: "task-1",
            orderIndex: 1,
            title: "Introduction to the Module",
            description: "Learn the core concepts and objectives of this module.",
            type: "foundation",
            difficulty: 1,
            xpReward: 50,
            status: "complete"
        },
        {
            id: "task-2",
            orderIndex: 2,
            title: "Setting Up Your Environment",
            description: "Configure your development environment for the hands-on exercises.",
            type: "foundation",
            difficulty: 2,
            xpReward: 75,
            status: "complete"
        },
        {
            id: "task-3",
            orderIndex: 3,
            title: "Hands-On Exercise 1",
            description: "Apply what you've learned in a practical exercise.",
            type: "practice",
            difficulty: 3,
            xpReward: 100,
            status: "in_progress"
        },
        {
            id: "task-4",
            orderIndex: 4,
            title: "Deep Dive: Advanced Concepts",
            description: "Explore advanced topics and edge cases.",
            type: "deepening",
            difficulty: 4,
            xpReward: 125,
            status: "not_started"
        },
        {
            id: "task-5",
            orderIndex: 5,
            title: "Mini Project",
            description: "Build a small project to demonstrate your understanding.",
            type: "project",
            difficulty: 4,
            xpReward: 200,
            status: "not_started"
        },
        {
            id: "task-6",
            orderIndex: 6,
            title: "Knowledge Check Quiz",
            description: "Test your understanding with a quiz.",
            type: "quiz",
            difficulty: 2,
            xpReward: 50,
            status: "not_started"
        },
        {
            id: "task-7",
            orderIndex: 7,
            title: "Challenge: Real-World Scenario",
            description: "Solve a challenging real-world problem.",
            type: "challenge",
            difficulty: 5,
            xpReward: 250,
            status: "not_started"
        },
        {
            id: "task-8",
            orderIndex: 8,
            title: "Module Summary & Next Steps",
            description: "Review key takeaways and prepare for the next module.",
            type: "foundation",
            difficulty: 1,
            xpReward: 50,
            status: "not_started"
        }
    ])

    // Mock prerequisites
    const [prerequisites] = useState<Prerequisite[]>([
        { id: "prereq-1", title: "Module 01 · Onboarding", isComplete: true, progress: 100 },
        { id: "prereq-2", title: "Module 02 · Foundations", isComplete: true, progress: 100 }
    ])

    const fetchModule = async () => {
        if (!moduleId) {
            setError("Module ID not provided")
            setLoading(false)
            return
        }

        setLoading(true)
        setError(null)

        try {
            const result = await getModule(moduleId)
            if (result.ok) {
                setModule(result.data)
            } else {
                setError(result.message)
            }
        } catch {
            setError("Failed to load module. Please try again.")
        } finally {
            setLoading(false)
        }
    }

    useEffect(() => {
        fetchModule()
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [moduleId])

    const handleTaskToggle = (taskId: string) => {
        console.log("Toggle task:", taskId)
        // Would update task status via API
    }

    const handleTaskClick = (taskId: string) => {
        // Navigate to task detail page
        window.location.href = `/modules/${moduleId}/tasks/${taskId}`
    }

    if (loading) {
        return <PageSkeleton />
    }

    if (error || !module) {
        return <ErrorState error={error || "Module not found"} onRetry={fetchModule} />
    }

    // Calculate progress stats
    const completedTasks = tasks.filter(t => t.status === "complete").length
    const progress = Math.round((completedTasks / tasks.length) * 100)
    const totalXP = tasks.reduce((sum, t) => sum + t.xpReward, 0)
    const earnedXP = tasks
        .filter(t => t.status === "complete")
        .reduce((sum, t) => sum + t.xpReward, 0)

    // Mini tasks for sidebar
    const miniTasks: MiniTask[] = tasks.map(t => ({
        id: t.id,
        title: t.title,
        isComplete: t.status === "complete"
    }))

    // Find next incomplete task
    const nextTask = tasks.find(t => t.status !== "complete")

    // Module icon based on name
    const getIcon = (name: string): string => {
        const lower = name.toLowerCase()
        if (lower.includes("linux")) return "🐧"
        if (lower.includes("git")) return "🔀"
        if (lower.includes("docker") || lower.includes("container")) return "🐳"
        if (lower.includes("kubernetes") || lower.includes("k8s")) return "⚙️"
        if (lower.includes("cloud") || lower.includes("aws")) return "☁️"
        if (lower.includes("terraform") || lower.includes("iac")) return "🏗️"
        if (lower.includes("network")) return "🌐"
        if (lower.includes("shell") || lower.includes("bash")) return "💻"
        return "📚"
    }

    return (
        <div className="space-y-6">
            {/* Back link */}
            <Link
                href="/modules"
                className={cn(
                    "inline-flex items-center gap-2 text-sm font-medium",
                    "text-neutral-600 dark:text-neutral-400",
                    "hover:text-primary-500 transition-colors"
                )}
            >
                <ArrowLeft className="w-4 h-4" />
                Back to Modules
            </Link>

            {/* Module Header */}
            <ModuleHeader
                title={module.name}
                description={module.description || "No description available"}
                icon={getIcon(module.name)}
                difficulty={3}
                estimatedHours={8}
                tasksCount={tasks.length}
                totalXP={totalXP}
                progress={progress}
            />

            {/* Info cards row */}
            <InfoCardsRow
                tasksCount={tasks.length}
                estimatedHours={8}
                totalXP={totalXP}
                prerequisitesCount={prerequisites.length}
            />

            {/* Main content grid */}
            <div className="grid lg:grid-cols-3 gap-6">
                {/* Tasks list - 2 columns */}
                <div className="lg:col-span-2 space-y-4">
                    <h2 className="text-lg font-semibold text-neutral-900 dark:text-white">
                        Tasks ({completedTasks}/{tasks.length})
                    </h2>

                    <div className="space-y-3">
                        {tasks.map((task, index) => (
                            <div
                                key={task.id}
                                className="animate-fade-in-up"
                                style={{ animationDelay: `${index * 50}ms` }}
                            >
                                <TaskCard
                                    id={task.id}
                                    orderIndex={task.orderIndex}
                                    title={task.title}
                                    description={task.description}
                                    type={task.type}
                                    difficulty={task.difficulty}
                                    xpReward={task.xpReward}
                                    status={task.status}
                                    onToggleComplete={handleTaskToggle}
                                    onClick={handleTaskClick}
                                />
                            </div>
                        ))}
                    </div>
                </div>

                {/* Sidebar - 1 column */}
                <div className="space-y-6">
                    {/* Progress sidebar */}
                    <ModuleProgress
                        moduleId={moduleId || ""}
                        progress={progress}
                        xpEarned={earnedXP}
                        totalXP={totalXP}
                        timeSpentMinutes={145}
                        tasksCompleted={completedTasks}
                        totalTasks={tasks.length}
                        tasks={miniTasks}
                        nextTaskId={nextTask?.id}
                    />

                    {/* Prerequisites section */}
                    {prerequisites.length > 0 && (
                        <PrerequisitesSection prerequisites={prerequisites} />
                    )}
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   EXPORT
   ============================================================================ */

export default function ModuleDetailsPage() {
    return (
        <Protected>
            <AppShell>
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                    <ModuleContent />
                </div>
            </AppShell>
        </Protected>
    )
}
