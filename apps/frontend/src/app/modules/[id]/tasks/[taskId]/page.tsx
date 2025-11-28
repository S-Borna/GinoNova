"use client"

/**
 * ============================================================================
 * TASK DETAIL PAGE - Individual Task Content Display
 * ============================================================================
 *
 * Features:
 * - Breadcrumb navigation with track color
 * - Task title and metadata
 * - Markdown content rendering
 * - Progress sidebar
 * - Task navigation (prev/next)
 * - Mark as complete functionality
 *
 * @phase C.2 - Task Content Display
 */

import * as React from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { getTask, getTasksForModule, TaskPublic, getDifficultyColor } from "@/lib/tasks"
import { getModule, ModulePublic } from "@/lib/modules"
import { MarkdownRenderer } from "@/components/content/MarkdownRenderer"
import { TaskNav } from "@/components/content/TaskNav"
import { GlassCard } from "@/components/ui/glass-card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import {
    ChevronRight,
    Clock,
    Zap,
    BookOpen,
    CheckCircle2,
    Circle,
    ArrowLeft,
    Loader2,
} from "lucide-react"

/* ============================================================================
   TRACK COLORS (from design system)
   ============================================================================ */

const TRACK_COLORS: Record<string, string> = {
    foundation: "#6366f1",
    cloud: "#8b5cf6",
    containers: "#06b6d4",
    platform: "#f97316",
}

function getTrackColor(trackSlug?: string): string {
    if (!trackSlug) return TRACK_COLORS.foundation
    return TRACK_COLORS[trackSlug.toLowerCase()] || TRACK_COLORS.foundation
}

/* ============================================================================
   BREADCRUMB COMPONENT
   ============================================================================ */

interface BreadcrumbProps {
    module: ModulePublic
    task: TaskPublic
    trackColor: string
}

function Breadcrumb({ module, task, trackColor }: BreadcrumbProps) {
    return (
        <nav className="flex items-center gap-1 text-sm mb-6 flex-wrap">
            <Link
                href="/modules"
                className="text-neutral-500 hover:text-neutral-700 dark:hover:text-neutral-300 transition-colors"
            >
                Modules
            </Link>
            <ChevronRight className="h-4 w-4 text-neutral-400" />
            <Link
                href={`/modules/${module.id}`}
                className="hover:underline transition-colors"
                style={{ color: trackColor }}
            >
                {module.name}
            </Link>
            <ChevronRight className="h-4 w-4 text-neutral-400" />
            <span className="text-neutral-700 dark:text-neutral-200 font-medium truncate max-w-[200px]">
                {task.title}
            </span>
        </nav>
    )
}

/* ============================================================================
   METADATA BAR
   ============================================================================ */

interface MetadataBarProps {
    task: TaskPublic
    trackColor: string
}

function MetadataBar({ task, trackColor }: MetadataBarProps) {
    return (
        <div className="flex flex-wrap items-center gap-4 mb-6 pb-6 border-b border-neutral-200 dark:border-neutral-700">
            {/* Difficulty badge */}
            <Badge
                className={cn("capitalize", getDifficultyColor(task.difficulty))}
            >
                {task.difficulty}
            </Badge>

            {/* Type badge (placeholder - would come from task data) */}
            <div className="flex items-center gap-1.5 text-sm text-neutral-600 dark:text-neutral-400">
                <BookOpen className="h-4 w-4" style={{ color: trackColor }} />
                <span>Lesson</span>
            </div>

            {/* Estimated time (placeholder) */}
            <div className="flex items-center gap-1.5 text-sm text-neutral-600 dark:text-neutral-400">
                <Clock className="h-4 w-4" />
                <span>~15 min</span>
            </div>

            {/* XP reward (placeholder) */}
            <div className="flex items-center gap-1.5 text-sm font-medium">
                <Zap className="h-4 w-4 text-amber-500" />
                <span className="text-amber-600 dark:text-amber-400">+50 XP</span>
            </div>
        </div>
    )
}

/* ============================================================================
   PROGRESS SIDEBAR
   ============================================================================ */

interface ProgressSidebarProps {
    tasks: TaskPublic[]
    currentTaskId: string
    moduleId: string
    trackColor: string
}

function ProgressSidebar({ tasks, currentTaskId, moduleId, trackColor }: ProgressSidebarProps) {
    const completedCount = 0 // Would come from user progress
    const totalCount = tasks.length
    const progressPercent = totalCount > 0 ? (completedCount / totalCount) * 100 : 0

    return (
        <GlassCard className="p-4 sticky top-24">
            <h3 className="font-semibold text-neutral-900 dark:text-white mb-4">
                Module Progress
            </h3>

            {/* Progress bar */}
            <div className="mb-4">
                <div className="flex justify-between text-sm mb-1">
                    <span className="text-neutral-600 dark:text-neutral-400">
                        {completedCount} of {totalCount} tasks
                    </span>
                    <span className="font-medium" style={{ color: trackColor }}>
                        {Math.round(progressPercent)}%
                    </span>
                </div>
                <div className="h-2 bg-neutral-200 dark:bg-neutral-700 rounded-full overflow-hidden">
                    <div
                        className="h-full rounded-full transition-all duration-500"
                        style={{
                            width: `${progressPercent}%`,
                            backgroundColor: trackColor,
                        }}
                    />
                </div>
            </div>

            {/* Task list */}
            <div className="space-y-1 max-h-[400px] overflow-y-auto">
                {tasks.map((task, index) => {
                    const isCurrent = task.id === currentTaskId
                    const isCompleted = false // Would come from user progress

                    return (
                        <Link
                            key={task.id}
                            href={`/modules/${moduleId}/tasks/${task.id}`}
                            className={cn(
                                "flex items-center gap-2 px-3 py-2 rounded-lg text-sm",
                                "transition-colors duration-150",
                                isCurrent
                                    ? "bg-primary-50 dark:bg-primary-950/30"
                                    : "hover:bg-neutral-100 dark:hover:bg-neutral-800"
                            )}
                        >
                            {isCompleted ? (
                                <CheckCircle2
                                    className="h-4 w-4 flex-shrink-0 text-green-500"
                                />
                            ) : (
                                <Circle
                                    className={cn(
                                        "h-4 w-4 flex-shrink-0",
                                        isCurrent
                                            ? "text-primary-500"
                                            : "text-neutral-400"
                                    )}
                                    style={isCurrent ? { color: trackColor } : undefined}
                                />
                            )}
                            <span
                                className={cn(
                                    "truncate",
                                    isCurrent
                                        ? "font-medium text-neutral-900 dark:text-white"
                                        : "text-neutral-600 dark:text-neutral-400"
                                )}
                            >
                                {index + 1}. {task.title}
                            </span>
                        </Link>
                    )
                })}
            </div>
        </GlassCard>
    )
}

/* ============================================================================
   LOADING SKELETON
   ============================================================================ */

function TaskDetailSkeleton() {
    return (
        <div className="min-h-screen bg-neutral-50 dark:bg-neutral-950">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {/* Breadcrumb skeleton */}
                <div className="flex items-center gap-2 mb-6">
                    <div className="h-4 w-16 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                    <div className="h-4 w-4 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                    <div className="h-4 w-24 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
                    {/* Main content skeleton */}
                    <div className="lg:col-span-3">
                        <div className="h-10 w-3/4 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse mb-4" />
                        <div className="flex gap-4 mb-6">
                            <div className="h-6 w-16 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                            <div className="h-6 w-20 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                            <div className="h-6 w-16 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                        </div>
                        <div className="space-y-3">
                            <div className="h-4 w-full bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                            <div className="h-4 w-5/6 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                            <div className="h-4 w-4/6 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                        </div>
                    </div>

                    {/* Sidebar skeleton */}
                    <div className="hidden lg:block">
                        <div className="h-64 bg-neutral-200 dark:bg-neutral-800 rounded-xl animate-pulse" />
                    </div>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   MAIN PAGE COMPONENT
   ============================================================================ */

export default function TaskDetailPage() {
    const params = useParams()
    const router = useRouter()
    const moduleId = params?.id as string
    const taskId = params?.taskId as string

    // State
    const [task, setTask] = React.useState<TaskPublic | null>(null)
    const [module, setModule] = React.useState<ModulePublic | null>(null)
    const [allTasks, setAllTasks] = React.useState<TaskPublic[]>([])
    const [loading, setLoading] = React.useState(true)
    const [error, setError] = React.useState<string | null>(null)
    const [isCompleting, setIsCompleting] = React.useState(false)
    const [isCompleted, setIsCompleted] = React.useState(false)

    // Derived state
    const currentIndex = React.useMemo(
        () => allTasks.findIndex((t) => t.id === taskId),
        [allTasks, taskId]
    )
    const previousTask = currentIndex > 0 ? allTasks[currentIndex - 1] : null
    const nextTask = currentIndex < allTasks.length - 1 ? allTasks[currentIndex + 1] : null

    // Track color (placeholder - would come from module/track data)
    const trackColor = getTrackColor("foundation")

    // Fetch data
    React.useEffect(() => {
        async function fetchData() {
            if (!moduleId || !taskId) {
                setError("Invalid URL parameters")
                setLoading(false)
                return
            }

            try {
                const [taskResult, moduleResult, tasksResult] = await Promise.all([
                    getTask(taskId),
                    getModule(moduleId),
                    getTasksForModule(moduleId),
                ])

                if (!taskResult.ok) {
                    setError(taskResult.message)
                    setLoading(false)
                    return
                }

                if (!moduleResult.ok) {
                    setError(moduleResult.message)
                    setLoading(false)
                    return
                }

                setTask(taskResult.data)
                setModule(moduleResult.data)
                setAllTasks(tasksResult.ok ? tasksResult.data : [])
                setLoading(false)
            } catch (err) {
                setError("Failed to load task")
                setLoading(false)
            }
        }

        fetchData()
    }, [moduleId, taskId])

    // Handle task completion
    const handleComplete = async () => {
        setIsCompleting(true)

        // Simulate API call
        await new Promise((resolve) => setTimeout(resolve, 500))

        setIsCompleted(true)
        setIsCompleting(false)

        // Navigate to next task if available
        if (nextTask) {
            setTimeout(() => {
                router.push(`/modules/${moduleId}/tasks/${nextTask.id}`)
            }, 300)
        }
    }

    // Sample markdown content (would come from task.content in real app)
    const sampleContent = task?.description || `
# ${task?.title || "Task"}

This is a sample task content. In a real application, this would be rich markdown content stored in the database.

## Learning Objectives

- Understand the core concepts
- Practice with hands-on exercises
- Apply knowledge to real-world scenarios

## Getting Started

First, make sure you have the prerequisites installed:

\`\`\`bash
# Check your installation
node --version
npm --version
\`\`\`

## Key Concepts

Here's an example of how this works:

\`\`\`javascript
function greet(name) {
  return \`Hello, \${name}!\`;
}

console.log(greet('DevOps Engineer'));
\`\`\`

## Summary

- Point 1: Important concept
- Point 2: Another key takeaway
- Point 3: Final thought

> **Pro Tip:** Always test your code before deploying to production!
    `

    // Loading state
    if (loading) {
        return <TaskDetailSkeleton />
    }

    // Error state
    if (error || !task || !module) {
        return (
            <div className="min-h-screen bg-neutral-50 dark:bg-neutral-950 flex items-center justify-center">
                <div className="text-center">
                    <p className="text-red-500 mb-4">{error || "Task not found"}</p>
                    <Button variant="outline" onClick={() => router.back()}>
                        <ArrowLeft className="h-4 w-4 mr-2" />
                        Go Back
                    </Button>
                </div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-neutral-50 dark:bg-neutral-950">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {/* Breadcrumb */}
                <Breadcrumb module={module} task={task} trackColor={trackColor} />

                <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
                    {/* Main content */}
                    <div className="lg:col-span-3">
                        <GlassCard className="p-6 md:p-8">
                            {/* Task title */}
                            <h1 className="text-2xl md:text-3xl font-bold text-neutral-900 dark:text-white mb-4">
                                {task.title}
                            </h1>

                            {/* Metadata bar */}
                            <MetadataBar task={task} trackColor={trackColor} />

                            {/* Content */}
                            <div className="prose-container">
                                <MarkdownRenderer content={sampleContent} />
                            </div>
                        </GlassCard>

                        {/* Task navigation (bottom) */}
                        <div className="mt-6">
                            <GlassCard className="overflow-hidden">
                                <TaskNav
                                    moduleId={moduleId}
                                    currentIndex={currentIndex}
                                    totalTasks={allTasks.length}
                                    previousTask={previousTask}
                                    nextTask={nextTask}
                                    isCompleted={isCompleted}
                                    isCompleting={isCompleting}
                                    onComplete={handleComplete}
                                    trackColor={trackColor}
                                />
                            </GlassCard>
                        </div>
                    </div>

                    {/* Sidebar */}
                    <div className="hidden lg:block">
                        <ProgressSidebar
                            tasks={allTasks}
                            currentTaskId={taskId}
                            moduleId={moduleId}
                            trackColor={trackColor}
                        />
                    </div>
                </div>
            </div>
        </div>
    )
}
