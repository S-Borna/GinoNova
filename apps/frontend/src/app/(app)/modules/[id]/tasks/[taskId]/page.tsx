"use client"

/**
 * ============================================================================
 * TASK DETAIL PAGE — Individual Task/Lesson View
 * ============================================================================
 *
 * Features:
 * - Lesson content (markdown)
 * - Mark as complete button
 * - Navigation to next task
 *
 * @phase C.2 - Task Content Display
 */

import { useState, useEffect } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { GlassCard } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import { getTask, getTasksForModule, TaskPublic } from "@/lib/tasks"
import { getModule, ModulePublic } from "@/lib/modules"
import {
    ArrowLeft,
    ArrowRight,
    CheckCircle2,
    Clock,
    BookOpen,
    RefreshCw,
    AlertCircle,
    Zap,
} from "lucide-react"

/* ============================================================================
   SKELETON
   ============================================================================ */

function TaskDetailSkeleton() {
    return (
        <div className="space-y-6 animate-pulse">
            <div className="h-8 w-48 rounded bg-neutral-200 dark:bg-neutral-800" />
            <div className="h-64 rounded-2xl bg-neutral-200 dark:bg-neutral-800" />
            <div className="space-y-3">
                <div className="h-4 w-full rounded bg-neutral-200 dark:bg-neutral-800" />
                <div className="h-4 w-3/4 rounded bg-neutral-200 dark:bg-neutral-800" />
                <div className="h-4 w-5/6 rounded bg-neutral-200 dark:bg-neutral-800" />
            </div>
        </div>
    )
}

/* ============================================================================
   ERROR STATE
   ============================================================================ */

function ErrorState({ error, onRetry, moduleId }: { error: string; onRetry: () => void; moduleId: string }) {
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
                Task Not Found
            </h2>
            <p className="text-neutral-600 dark:text-neutral-400 mb-6">{error}</p>
            <div className="flex gap-3 justify-center">
                <Link href={`/modules/${moduleId}`}>
                    <Button variant="outline" className="rounded-xl">
                        <ArrowLeft className="w-4 h-4 mr-2" />
                        Back to Module
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
   MARKDOWN RENDERER (Simple)
   ============================================================================ */

function MarkdownContent({ content }: { content: string }) {
    // Simple markdown rendering - in production, use react-markdown or similar
    const renderMarkdown = (md: string) => {
        // Convert headers
        let html = md
            .replace(/^### (.+)$/gm, '<h3 class="text-xl font-semibold text-neutral-900 dark:text-white mt-8 mb-4">$1</h3>')
            .replace(/^## (.+)$/gm, '<h2 class="text-2xl font-bold text-neutral-900 dark:text-white mt-10 mb-5">$1</h2>')
            .replace(/^# (.+)$/gm, '<h1 class="text-3xl font-bold text-neutral-900 dark:text-white mt-10 mb-6">$1</h1>')

        // Convert code blocks - visible in both light and dark mode
        html = html.replace(/```(\w+)?\n([\s\S]*?)```/g, (_, lang, code) => {
            return `<pre class="bg-neutral-900 dark:bg-neutral-950 text-neutral-100 rounded-xl p-5 my-6 overflow-x-auto text-sm font-mono border border-neutral-800"><code>${code.trim()}</code></pre>`
        })

        // Convert inline code - visible in both modes
        html = html.replace(/`([^`]+)`/g, '<code class="bg-neutral-200 dark:bg-neutral-800 px-2 py-1 rounded text-sm font-mono text-indigo-700 dark:text-indigo-400">$1</code>')

        // Convert bold
        html = html.replace(/\*\*([^*]+)\*\*/g, '<strong class="font-semibold text-neutral-900 dark:text-white">$1</strong>')

        // Convert italic
        html = html.replace(/\*([^*]+)\*/g, '<em>$1</em>')

        // Convert tables (basic support)
        html = html.replace(/^\|(.+)\|$/gm, (match, content) => {
            const cells = content.split('|').map((cell: string) => cell.trim())
            if (cells.every((cell: string) => /^[-:]+$/.test(cell))) {
                return '' // Skip separator row
            }
            const cellsHtml = cells.map((cell: string) => `<td class="border border-neutral-300 dark:border-neutral-700 px-4 py-2">${cell}</td>`).join('')
            return `<tr class="bg-neutral-50 dark:bg-neutral-800/50">${cellsHtml}</tr>`
        })
        
        // Wrap tables
        html = html.replace(/(<tr[^>]*>.*<\/tr>\n?)+/g, (match) => {
            return `<table class="w-full border-collapse my-6 text-sm"><tbody>${match}</tbody></table>`
        })

        // Convert lists - single bullet, no double
        html = html.replace(/^- (.+)$/gm, '<li class="ml-6 text-neutral-700 dark:text-neutral-300 mb-2 list-disc">$1</li>')
        html = html.replace(/^(\d+)\. (.+)$/gm, '<li class="ml-6 text-neutral-700 dark:text-neutral-300 mb-2 list-decimal">$1. $2</li>')

        // Wrap consecutive list items in ul/ol
        html = html.replace(/(<li class="[^"]*list-disc[^"]*">[\s\S]*?<\/li>\n?)+/g, (match) => {
            return `<ul class="my-4 space-y-1">${match}</ul>`
        })

        // Convert paragraphs (lines that aren't already wrapped)
        html = html.replace(/^(?!<[hpuol]|<li|<pre|<code|<table|<tr)(.+)$/gm, '<p class="text-neutral-700 dark:text-neutral-300 mb-4 leading-relaxed text-base">$1</p>')

        return html
    }

    return (
        <div
            className="prose prose-neutral dark:prose-invert max-w-none"
            dangerouslySetInnerHTML={{ __html: renderMarkdown(content) }}
        />
    )
}

/* ============================================================================
   TASK DETAIL PAGE
   ============================================================================ */

export default function TaskDetailPage() {
    const params = useParams()
    const router = useRouter()
    const moduleId = params.id as string
    const taskId = params.taskId as string

    const [task, setTask] = useState<TaskPublic | null>(null)
    const [module, setModule] = useState<ModulePublic | null>(null)
    const [allTasks, setAllTasks] = useState<TaskPublic[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [completing, setCompleting] = useState(false)
    const [isCompleted, setIsCompleted] = useState(false)

    const fetchData = async () => {
        setLoading(true)
        setError(null)

        try {
            // Fetch task, module, and all tasks in parallel
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
            if (tasksResult.ok) {
                // Sort tasks by order_index
                const sorted = [...tasksResult.data].sort((a, b) => a.order_index - b.order_index)
                setAllTasks(sorted)
            }
        } catch (err) {
            setError(err instanceof Error ? err.message : "Failed to load task")
        } finally {
            setLoading(false)
        }
    }

    useEffect(() => {
        fetchData()
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [moduleId, taskId])

    const handleMarkComplete = async () => {
        setCompleting(true)
        // TODO: Call progress API to mark task as complete
        await new Promise((resolve) => setTimeout(resolve, 500))
        setIsCompleted(true)
        setCompleting(false)
    }

    // Find current task index and next task
    const currentIndex = allTasks.findIndex(t => t.id === taskId)
    const nextTask = currentIndex >= 0 && currentIndex < allTasks.length - 1
        ? allTasks[currentIndex + 1]
        : null
    const prevTask = currentIndex > 0
        ? allTasks[currentIndex - 1]
        : null

    const handleContinue = () => {
        if (nextTask) {
            router.push(`/modules/${moduleId}/tasks/${nextTask.id}`)
        } else {
            // No more tasks, go back to module
            router.push(`/modules/${moduleId}`)
        }
    }

    // Placeholder content when task has no content
    const placeholderContent = `# ${task?.title || "Loading..."}

${task?.description || ""}

## Overview

This lesson will teach you the fundamentals of this topic. Follow along with the examples below.

## Key Concepts

- Concept 1: Understanding the basics
- Concept 2: Practical applications
- Concept 3: Best practices

## Try It Yourself

\`\`\`bash
# Example command
echo "Hello, DevOps!"
\`\`\`

## Summary

You've learned the core concepts of this topic. Practice these skills to reinforce your learning.

---

*💡 Tip: Take notes as you learn to help retain information better.*
`

    return (
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            {/* Back button */}
            <Link
                href={`/modules/${moduleId}`}
                className={cn(
                    "inline-flex items-center gap-2 text-sm mb-6",
                    "text-neutral-500 hover:text-neutral-900",
                    "dark:text-neutral-400 dark:hover:text-white",
                    "transition-colors"
                )}
            >
                <ArrowLeft className="w-4 h-4" />
                Back to {module?.name || "Module"}
            </Link>

            {loading ? (
                <TaskDetailSkeleton />
            ) : error ? (
                <ErrorState error={error} onRetry={fetchData} moduleId={moduleId} />
            ) : task ? (
                <div className="space-y-6">
                    {/* Task Header */}
                    <GlassCard variant="default" padding="lg" radius="xl">
                        <div className="flex flex-col md:flex-row md:items-start gap-4">
                            {/* Task info */}
                            <div className="flex-1">
                                <div className="flex items-center gap-2 mb-2">
                                    <span className="text-xs font-medium text-neutral-400">
                                        Task {task.order_index}
                                    </span>
                                    {isCompleted && (
                                        <span className="inline-flex items-center gap-1 text-xs text-emerald-500 font-medium">
                                            <CheckCircle2 className="w-3.5 h-3.5" />
                                            Completed
                                        </span>
                                    )}
                                </div>
                                <h1 className="text-2xl font-bold text-neutral-900 dark:text-white mb-2">
                                    {task.title}
                                </h1>
                                {task.description && (
                                    <p className="text-neutral-600 dark:text-neutral-400 mb-4">
                                        {task.description}
                                    </p>
                                )}

                                {/* Meta */}
                                <div className="flex flex-wrap items-center gap-4">
                                    <span className="flex items-center gap-1.5 text-sm text-neutral-500">
                                        <Clock className="w-4 h-4" />
                                        {task.estimated_minutes} min
                                    </span>
                                    <span className="flex items-center gap-1.5 text-sm text-indigo-500 font-medium">
                                        <Zap className="w-4 h-4" />
                                        +{task.xp_reward} XP
                                    </span>
                                    <span className={cn(
                                        "px-2 py-0.5 rounded text-xs font-medium",
                                        task.difficulty === "easy" && "bg-emerald-100 text-emerald-700",
                                        task.difficulty === "medium" && "bg-amber-100 text-amber-700",
                                        task.difficulty === "hard" && "bg-red-100 text-red-700",
                                    )}>
                                        {task.difficulty}
                                    </span>
                                </div>
                            </div>
                        </div>
                    </GlassCard>

                    {/* Lesson Content */}
                    <GlassCard variant="default" padding="lg" radius="xl">
                        <div className="flex items-center gap-2 mb-6 pb-4 border-b border-neutral-200 dark:border-neutral-700">
                            <BookOpen className="w-5 h-5 text-indigo-500" />
                            <h2 className="text-lg font-semibold text-neutral-900 dark:text-white">
                                Lesson Content
                            </h2>
                        </div>

                        <MarkdownContent content={task.content || placeholderContent} />
                    </GlassCard>

                    {/* Actions */}
                    <div className="flex items-center justify-between">
                        <Link href={`/modules/${moduleId}`}>
                            <Button variant="outline" className="rounded-xl">
                                <ArrowLeft className="w-4 h-4 mr-2" />
                                Back to Module
                            </Button>
                        </Link>

                        {isCompleted ? (
                            <Button
                                onClick={handleContinue}
                                className="rounded-xl bg-emerald-500 hover:bg-emerald-600"
                            >
                                <CheckCircle2 className="w-4 h-4 mr-2" />
                                {nextTask ? "Continue to Next" : "Back to Module"}
                                <ArrowRight className="w-4 h-4 ml-2" />
                            </Button>
                        ) : (
                            <Button
                                onClick={handleMarkComplete}
                                disabled={completing}
                                className="rounded-xl"
                            >
                                {completing ? (
                                    <>
                                        <RefreshCw className="w-4 h-4 mr-2 animate-spin" />
                                        Saving...
                                    </>
                                ) : (
                                    <>
                                        <CheckCircle2 className="w-4 h-4 mr-2" />
                                        Mark as Complete
                                    </>
                                )}
                            </Button>
                        )}
                    </div>
                </div>
            ) : null}
        </div>
    )
}
