"use client"

/**
 * ============================================================================
 * TASK DETAIL PAGE — Individual Task/Lesson View
 * ============================================================================
 *
 * Features:
 * - Lesson content (markdown) OR interactive content blocks
 * - Quiz, terminal, and checkpoint support
 * - Progress tracking
 * - Mark as complete button
 * - Navigation to next task
 * - Related "fördjupning" tasks (v4 optional deep-dive content)
 *
 * @phase C.2 - Task Content Display
 * @phase ILE - Interactive Learning Engine
 * @phase 4.0 - Task Tier System with Related Tasks
 * @design PHASE 2 — Design System Application Layer
 */

import { useState, useEffect, useCallback } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import ReactMarkdown from "react-markdown"
import rehypeHighlight from "rehype-highlight"
import remarkGfm from "remark-gfm"
import {
    PageLayout,
    Section,
    Block,
    Headline,
    Subtext,
    CodeBlock,
    TaskFooter,
    InfoBanner,
    cn
} from "@saas/ui"
import { GlassCard } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import { getTask, getTasksForModule, TaskPublic } from "@/lib/tasks"
import { getModule, ModulePublic } from "@/lib/modules"
import { useAuth } from "@/components/auth"
import { getToken } from "@/lib/auth"
import { ContentBlockRenderer } from "@/components/learning"
import { RelatedTasks, RelatedTask } from "@/components/tasks/RelatedTasks"
import {
    ArrowLeft,
    ArrowRight,
    CheckCircle2,
    Clock,
    BookOpen,
    RefreshCw,
    AlertCircle,
    Zap,
    Play,
} from "lucide-react"

// Import highlight.js theme for syntax highlighting
import "highlight.js/styles/github-dark.css"

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
   MARKDOWN RENDERER - With Syntax Highlighting
   ============================================================================ */

function MarkdownContent({ content }: { content: string }) {
    return (
        <div className="prose prose-neutral dark:prose-invert max-w-none prose-headings:text-neutral-900 dark:prose-headings:text-white prose-p:text-neutral-700 dark:prose-p:text-neutral-300 prose-li:text-neutral-700 dark:prose-li:text-neutral-300 prose-strong:text-neutral-900 dark:prose-strong:text-white prose-code:text-indigo-600 dark:prose-code:text-indigo-400 prose-code:bg-neutral-100 dark:prose-code:bg-neutral-800 prose-code:px-1.5 prose-code:py-0.5 prose-code:rounded prose-code:before:content-none prose-code:after:content-none prose-pre:bg-neutral-900 prose-pre:border prose-pre:border-neutral-800 prose-h1:text-3xl prose-h1:mt-8 prose-h1:mb-4 prose-h2:text-2xl prose-h2:mt-8 prose-h2:mb-4 prose-h3:text-xl prose-h3:mt-6 prose-h3:mb-3">
            <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                rehypePlugins={[rehypeHighlight]}
                components={{
                    // Custom ordered list - convert inner numbers to bullets
                    ol: ({ children, ...props }) => (
                        <ol className="list-decimal ml-6 my-4 space-y-2" {...props}>
                            {children}
                        </ol>
                    ),
                    // Custom list item - handle nested numbering
                    li: ({ children, ...props }) => {
                        // Check if content starts with a number (like "1. " inside ordered list)
                        const content = String(children)
                        const nestedNumberMatch = content.match(/^(\d+)\.\s*(.*)/)
                        if (nestedNumberMatch) {
                            return (
                                <li className="text-neutral-700 dark:text-neutral-300" {...props}>
                                    <span className="font-medium">{nestedNumberMatch[1]}.</span> {nestedNumberMatch[2]}
                                </li>
                            )
                        }
                        return (
                            <li className="text-neutral-700 dark:text-neutral-300" {...props}>
                                {children}
                            </li>
                        )
                    },
                    // Tables
                    table: ({ children }) => (
                        <table className="w-full border-collapse my-6 text-sm">
                            {children}
                        </table>
                    ),
                    th: ({ children }) => (
                        <th className="border border-neutral-300 dark:border-neutral-700 px-4 py-2 bg-neutral-100 dark:bg-neutral-800 font-semibold text-left">
                            {children}
                        </th>
                    ),
                    td: ({ children }) => (
                        <td className="border border-neutral-300 dark:border-neutral-700 px-4 py-2">
                            {children}
                        </td>
                    ),
                    // Code blocks using design system CodeBlock
                    pre: ({ children }) => {
                        // Extract code and language from children
                        const childElement = children as React.ReactElement<{ children?: string; className?: string }>
                        const code = childElement?.props?.children || ''
                        const className = childElement?.props?.className || ''
                        const languageMatch = className.match(/language-(\w+)/)
                        const language = languageMatch ? languageMatch[1] : 'bash'

                        return (
                            <CodeBlock language={language} className="my-6">
                                {String(code).trim()}
                            </CodeBlock>
                        )
                    },
                    code: ({ className, children, ...props }) => {
                        const isInline = !className
                        if (isInline) {
                            return (
                                <code className="bg-neutral-200 dark:bg-neutral-800 px-2 py-1 rounded text-sm font-mono text-indigo-700 dark:text-indigo-400" {...props}>
                                    {children}
                                </code>
                            )
                        }
                        return (
                            <code className={cn("text-sm", className)} {...props}>
                                {children}
                            </code>
                        )
                    },
                }}
            >
                {content}
            </ReactMarkdown>
        </div>
    )
}

/* ============================================================================
   TASK DETAIL PAGE
   ============================================================================ */

export default function TaskDetailPage() {
    const params = useParams()
    const router = useRouter()
    const { user } = useAuth()
    const moduleId = params?.id as string
    const taskId = params?.taskId as string

    const [task, setTask] = useState<TaskPublic | null>(null)
    const [module, setModule] = useState<ModulePublic | null>(null)
    const [allTasks, setAllTasks] = useState<TaskPublic[]>([])
    const [relatedTasks, setRelatedTasks] = useState<RelatedTask[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [completing, setCompleting] = useState(false)
    const [isCompleted, setIsCompleted] = useState(false)
    const [taskProgress, setTaskProgress] = useState<any>(null)

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
    const token = getToken()

    // Check if task has interactive content blocks
    const hasContentBlocks = task && Array.isArray((task as any).content_blocks) && (task as any).content_blocks.length > 0

    const fetchData = useCallback(async () => {
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

            // Fetch related tasks (fördjupning)
            try {
                const relatedRes = await fetch(`${API_URL}/api/tasks/${taskId}/related`)
                if (relatedRes.ok) {
                    const relatedData = await relatedRes.json()
                    setRelatedTasks(relatedData)
                }
            } catch (e) {
                console.log("Related tasks fetch skipped:", e)
            }

            // Fetch progress if token available
            if (token) {
                try {
                    const progressRes = await fetch(`${API_URL}/api/task-progress/${taskId}/progress`, {
                        headers: { Authorization: `Bearer ${token}` }
                    })
                    if (progressRes.ok) {
                        const progressData = await progressRes.json()
                        setTaskProgress(progressData)
                        if (progressData.status === "completed") {
                            setIsCompleted(true)
                        }
                    }
                } catch (e) {
                    console.log("Progress fetch skipped:", e)
                }
            }
        } catch (err) {
            setError(err instanceof Error ? err.message : "Failed to load task")
        } finally {
            setLoading(false)
        }
    }, [taskId, moduleId, token, API_URL])

    useEffect(() => {
        fetchData()
    }, [fetchData])

    // ILE handlers
    const handleBlockComplete = useCallback(async (blockIndex: number, blockType: string) => {
        if (!token) return
        try {
            await fetch(`${API_URL}/api/task-progress/${taskId}/progress/block?block_index=${blockIndex}&completed=true`, {
                method: "POST",
                headers: { Authorization: `Bearer ${token}` }
            })
            fetchData()
        } catch (e) {
            console.error("Block complete error:", e)
        }
    }, [token, taskId, API_URL, fetchData])

    const handleQuizAnswer = useCallback(async (blockIndex: number, optionIndex: number) => {
        if (!token) return { is_correct: false, explanation: "" }

        const contentBlocks = (task as any)?.content_blocks || []
        const quizBlock = contentBlocks[blockIndex]
        const isCorrect = quizBlock?.options?.[optionIndex]?.isCorrect || quizBlock?.options?.[optionIndex]?.is_correct || false

        try {
            const res = await fetch(`${API_URL}/api/task-progress/${taskId}/progress/quiz?block_index=${blockIndex}&selected_option=${optionIndex}&is_correct=${isCorrect}`, {
                method: "POST",
                headers: { Authorization: `Bearer ${token}` }
            })
            fetchData()
            return {
                is_correct: isCorrect,
                feedback: quizBlock?.options?.[optionIndex]?.feedback || "",
                explanation: quizBlock?.explanation || "",
                xp_bonus: isCorrect ? (quizBlock?.xp_bonus || 5) : 0
            }
        } catch (e) {
            console.error("Quiz answer error:", e)
            return { is_correct: false, explanation: "" }
        }
    }, [token, taskId, task, API_URL, fetchData])

    const handleTerminalCommand = useCallback(async (blockIndex: number, commandIndex: number, command: string, wasCorrect: boolean) => {
        if (!token) return { is_correct: false }
        try {
            await fetch(`${API_URL}/api/task-progress/${taskId}/progress/terminal?block_index=${blockIndex}&command_index=${commandIndex}&command=${encodeURIComponent(command)}&was_correct=${wasCorrect}`, {
                method: "POST",
                headers: { Authorization: `Bearer ${token}` }
            })
            return { is_correct: wasCorrect }
        } catch (e) {
            console.error("Terminal command error:", e)
            return { is_correct: false }
        }
    }, [token, taskId, API_URL])

    const handleMarkComplete = async () => {
        setCompleting(true)

        if (token) {
            try {
                await fetch(`${API_URL}/api/task-progress/${taskId}/progress/complete`, {
                    method: "POST",
                    headers: { Authorization: `Bearer ${token}` }
                })
            } catch (e) {
                console.error("Complete error:", e)
            }
        }

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
        <PageLayout maxWidth="standard" background="subtle">
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
                <div className="space-y-8">
                    {/* Task Header */}
                    <Section>
                        <Block className="bg-white/80 dark:bg-neutral-900/80 backdrop-blur-xl rounded-2xl border border-neutral-200/50 dark:border-neutral-700/50 shadow-lg p-6 md:p-8">
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
                                    <Headline level={1} className="mb-2">
                                        {task.title}
                                    </Headline>
                                    {task.description && (
                                        <Subtext className="mb-4">
                                            {task.description}
                                        </Subtext>
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
                        </Block>
                    </Section>

                    {/* Lesson Content */}
                    <Section>
                        <Block className="bg-white/80 dark:bg-neutral-900/80 backdrop-blur-xl rounded-2xl border border-neutral-200/50 dark:border-neutral-700/50 shadow-lg p-6 md:p-8">
                            <div className="flex items-center gap-2 mb-6 pb-4 border-b border-neutral-200 dark:border-neutral-700">
                                {hasContentBlocks ? (
                                    <Play className="w-5 h-5 text-indigo-500" />
                                ) : (
                                    <BookOpen className="w-5 h-5 text-indigo-500" />
                                )}
                                <Headline level={2}>
                                    {hasContentBlocks ? "Interactive Lesson" : "Lesson Content"}
                                </Headline>
                                {hasContentBlocks && taskProgress && (
                                    <span className="ml-auto text-sm text-neutral-500">
                                        {taskProgress.progress_percent || 0}% complete
                                    </span>
                                )}
                            </div>

                            {hasContentBlocks ? (
                                <ContentBlockRenderer
                                    blocks={(task as any).content_blocks}
                                    taskId={taskId}
                                    progress={taskProgress}
                                    onBlockComplete={handleBlockComplete}
                                    onQuizAnswer={handleQuizAnswer}
                                    onTerminalCommand={handleTerminalCommand}
                                />
                            ) : (
                                <MarkdownContent content={task.content || placeholderContent} />
                            )}

                            {/* Related Tasks / Fördjupning */}
                            {relatedTasks.length > 0 && (
                                <RelatedTasks
                                    tasks={relatedTasks}
                                    moduleId={moduleId}
                                    className="mt-8"
                                />
                            )}
                        </Block>
                    </Section>

                    {/* Actions - Using TaskFooter from @saas/ui */}
                    <TaskFooter
                        prevTaskUrl={prevTask ? `/modules/${moduleId}/tasks/${prevTask.id}` : undefined}
                        nextTaskUrl={nextTask ? `/modules/${moduleId}/tasks/${nextTask.id}` : undefined}
                        onComplete={handleMarkComplete}
                        xp={task.xp_reward}
                        difficulty={task.difficulty as 'easy' | 'medium' | 'hard'}
                        isCompleted={isCompleted}
                        isLoading={completing}
                    />
                </div>
            ) : null}
        </PageLayout>
    )
}
