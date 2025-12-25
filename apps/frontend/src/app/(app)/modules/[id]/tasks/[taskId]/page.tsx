"use client"

/**
 * ============================================================================
 * TASK DETAIL PAGE — Premium SkillsMaps-Style Design
 * ============================================================================
 *
 * Features:
 * - Glassmorphism header with colored glow
 * - Framer Motion animations
 * - Interactive content blocks (quiz, terminal, checkpoint)
 * - Progress tracking with read progress bar
 * - Mark as complete button
 * - Navigation to next task
 * - Premium design matching SkillsMaps
 *
 * @phase DESIGN-UNIFICATION
 */

import { useState, useEffect, useCallback } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import { motion } from "framer-motion"
import {
    PageLayout,
    Section,
    Block,
    Headline,
    Subtext,
    TaskFooter,
    cn
} from "@saas/ui"
import { GlassCard } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import { CosmicAurora } from "@/components/ui/cosmic-aurora"
import { getTask, getTasksForModule, TaskPublic } from "@/lib/tasks"
import { getModule, ModulePublic } from "@/lib/modules"
import { useAuth } from "@/components/auth"
import { getToken } from "@/lib/auth"
import { ContentBlockRenderer, LessonContent } from "@/components/learning"
import { RelatedTasks, RelatedTask } from "@/components/tasks/RelatedTasks"
import { usePlatform, filterContentByPlatform } from "@/hooks/useOperatingSystem"
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
    ChevronRight,
    Code2,
    Layers,
    Rocket,
    Trophy,
    HelpCircle,
} from "lucide-react"

/* ============================================================================
   MODULE COLORS
   ============================================================================ */

const moduleColors: Record<string, { color: string; icon: string }> = {
    // Linux 24/7 - Vår första modul!
    "linux-247": { color: "#FCC624", icon: "🐧" },
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
   TYPE CONFIG
   ============================================================================ */

const typeConfig: Record<string, {
    label: string
    emoji: string
    colorClass: string
    bgClass: string
}> = {
    concept: { label: "Koncept", emoji: "📚", colorClass: "text-blue-400", bgClass: "bg-blue-500/20" },
    practice: { label: "Praktik", emoji: "💻", colorClass: "text-emerald-400", bgClass: "bg-emerald-500/20" },
    deep_dive: { label: "Fördjupning", emoji: "🔍", colorClass: "text-violet-400", bgClass: "bg-violet-500/20" },
    project: { label: "Projekt", emoji: "🚀", colorClass: "text-orange-400", bgClass: "bg-orange-500/20" },
    challenge: { label: "Utmaning", emoji: "🏆", colorClass: "text-rose-400", bgClass: "bg-rose-500/20" },
    quiz: { label: "Quiz", emoji: "❓", colorClass: "text-cyan-400", bgClass: "bg-cyan-500/20" },
    standard: { label: "Standard", emoji: "📝", colorClass: "text-zinc-400", bgClass: "bg-zinc-500/20" },
    advanced: { label: "Avancerad", emoji: "⚡", colorClass: "text-purple-400", bgClass: "bg-purple-500/20" },
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

function ErrorState({ error, onRetry, moduleId }: { error: string; onRetry: () => void; moduleId: string }) {
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
                <Link prefetch={false} href={`/modules/${moduleId}`}>
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
   TASK DETAIL PAGE
   ============================================================================ */

export default function TaskDetailPage() {
    const params = useParams()
    const router = useRouter()
    const { user } = useAuth()
    const { platform: platformConfig, os, distro } = usePlatform()
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

    // Filter content based on user's platform selection
    const filteredContent = task?.content
        ? filterContentByPlatform(task.content, os, distro)
        : null

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

    // Get module color for styling - with proper fallback
    const defaultModuleConfig = { color: "#6366f1", icon: "📚" }
    const moduleConfig = module ? (moduleColors[module.slug] || defaultModuleConfig) : defaultModuleConfig
    const taskType = (task as any)?.task_tier || "standard"
    const taskTypeConfig = typeConfig[taskType] || typeConfig.standard

    return (
        <div className="min-h-screen bg-[#05050a] relative overflow-hidden">
            {/* Cosmic Aurora Background */}
            <CosmicAurora />

            <div className="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            {/* Back button */}
            <Link
                href={`/modules/${moduleId}`}
                className={cn(
                    "inline-flex items-center gap-2 text-sm mb-6 px-4 py-2 rounded-xl",
                    "text-zinc-400 hover:text-white",
                    "bg-white/5 hover:bg-white/10 border border-white/10",
                    "transition-all duration-300"
                )}
            >
                <ArrowLeft className="w-4 h-4" />
                Tillbaka till {module?.name || "Module"}
            </Link>

            {loading ? (
                <TaskDetailSkeleton />
            ) : error ? (
                <ErrorState error={error} onRetry={fetchData} moduleId={moduleId} />
            ) : task ? (
                <motion.div
                    className="space-y-8"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                >
                    {/* Task Header — EPIC Cosmic Premium Style */}
                    <motion.div
                        initial={{ opacity: 0, y: -20 }}
                        animate={{ opacity: 1, y: 0 }}
                        className={cn(
                            "relative overflow-hidden rounded-3xl",
                            "bg-[#0a0a0f]", // Deep cosmic
                            "border border-purple-500/20",
                            "p-8 md:p-10"
                        )}
                        style={{
                            boxShadow: `0 0 80px ${moduleConfig.color}20, 0 0 40px rgba(168,85,247,0.1)`,
                        }}
                    >
                        {/* AURORA GLOW — Multi-layered */}
                        <motion.div
                            className="absolute -top-20 -right-20 w-[500px] h-[500px] rounded-full"
                            style={{
                                background: `radial-gradient(circle, ${moduleConfig.color}50 0%, transparent 70%)`,
                                filter: "blur(80px)",
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
                        <motion.div
                            className="absolute -bottom-20 -left-20 w-[400px] h-[400px] rounded-full"
                            style={{
                                background: "radial-gradient(circle, rgba(168,85,247,0.4) 0%, transparent 70%)",
                                filter: "blur(60px)",
                            }}
                            animate={{
                                scale: [1, 1.15, 1],
                                x: [0, 20, 0],
                            }}
                            transition={{
                                duration: 8,
                                repeat: Infinity,
                                ease: "easeInOut",
                            }}
                        />

                        {/* Grid pattern */}
                        <div
                            className="absolute inset-0 opacity-[0.03]"
                            style={{
                                backgroundImage: "linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px)",
                                backgroundSize: "40px 40px",
                            }}
                        />

                        {/* Completed sparkle */}
                        {isCompleted && (
                            <motion.div
                                className="absolute top-6 right-6"
                                animate={{ rotate: 360, scale: [1, 1.2, 1] }}
                                transition={{ rotate: { duration: 4, repeat: Infinity, ease: "linear" }, scale: { duration: 2, repeat: Infinity } }}
                            >
                                <Sparkles className="w-8 h-8 text-emerald-400" />
                            </motion.div>
                        )}

                        <div className="relative flex flex-col md:flex-row md:items-start gap-6">
                            {/* Task Type Icon — Pulsating */}
                            <motion.div
                                className={cn(
                                    "w-24 h-24 rounded-3xl flex items-center justify-center shrink-0",
                                    "bg-gradient-to-br from-white/10 to-white/5",
                                    "border border-white/20"
                                )}
                                style={{ boxShadow: `0 0 60px ${moduleConfig.color}40` }}
                                whileHover={{ scale: 1.08, rotate: 5 }}
                                animate={{
                                    boxShadow: [
                                        `0 0 40px ${moduleConfig.color}30`,
                                        `0 0 80px ${moduleConfig.color}50`,
                                        `0 0 40px ${moduleConfig.color}30`,
                                    ],
                                }}
                                transition={{
                                    boxShadow: { duration: 3, repeat: Infinity, ease: "easeInOut" },
                                }}
                            >
                                <span className="text-6xl drop-shadow-lg">{taskTypeConfig.emoji}</span>
                            </motion.div>

                            {/* Content */}
                            <div className="flex-1">
                                <div className="flex items-center gap-3 mb-3">
                                    <span className="text-xs font-bold text-purple-400/60 uppercase tracking-[0.15em]">
                                        Task {task.order_index}
                                    </span>
                                    <span className={cn(
                                        "px-3 py-1.5 rounded-xl text-xs font-bold border",
                                        taskTypeConfig.bgClass,
                                        taskTypeConfig.colorClass,
                                        "border-white/10"
                                    )}>
                                        {taskTypeConfig.label}
                                    </span>
                                    {isCompleted && (
                                        <motion.span
                                            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-emerald-500/20 border border-emerald-500/30"
                                            animate={{ boxShadow: ["0 0 10px rgba(16,185,129,0.2)", "0 0 20px rgba(16,185,129,0.4)", "0 0 10px rgba(16,185,129,0.2)"] }}
                                            transition={{ duration: 2, repeat: Infinity }}
                                        >
                                            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                                            <span className="text-xs font-bold text-emerald-300">Klar</span>
                                        </motion.span>
                                    )}
                                </div>

                                <h1
                                    className={cn(
                                        "text-3xl md:text-4xl font-black mb-3 tracking-tight",
                                        "bg-gradient-to-r from-white via-purple-200 to-cyan-200 bg-clip-text text-transparent"
                                    )}
                                    style={{ textShadow: `0 0 40px ${moduleConfig.color}40` }}
                                >
                                    {task.title}
                                </h1>

                                {task.description && (
                                    <p className="text-zinc-300 text-lg mb-5 max-w-2xl leading-relaxed">
                                        {task.description}
                                    </p>
                                )}

                                {/* Meta row — Premium styled */}
                                <div className="flex flex-wrap items-center gap-5 text-sm">
                                    <span className="flex items-center gap-2 text-zinc-300 bg-white/5 px-4 py-2 rounded-xl border border-white/10">
                                        <Clock className="w-4 h-4 text-purple-400" />
                                        <span className="font-medium">{task.estimated_minutes} min</span>
                                    </span>
                                    <motion.span
                                        className="flex items-center gap-2 bg-amber-500/10 px-4 py-2 rounded-xl border border-amber-500/30"
                                        whileHover={{ scale: 1.05 }}
                                    >
                                        <Zap className="w-4 h-4 text-amber-400" />
                                        <span className="font-black text-amber-400">+{task.xp_reward} XP</span>
                                    </motion.span>
                                    <DifficultyDots difficulty={task.difficulty} />
                                </div>
                            </div>
                        </div>
                    </motion.div>

                    {/* Lesson Content — Premium Cosmic Style */}
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.1 }}
                        className={cn(
                            "relative overflow-hidden rounded-3xl",
                            "bg-[#0a0a0f]/90 backdrop-blur-xl",
                            "border border-purple-500/20",
                            "p-8 md:p-10"
                        )}
                        style={{
                            boxShadow: "0 0 60px rgba(168,85,247,0.08), 0 20px 40px rgba(0,0,0,0.4)",
                        }}
                    >
                        {/* Subtle glow */}
                        <div
                            className="absolute top-0 right-0 w-[300px] h-[300px] rounded-full opacity-20 blur-[80px] pointer-events-none"
                            style={{ background: "radial-gradient(circle, rgba(168,85,247,0.4) 0%, transparent 70%)" }}
                        />

                        <div className="relative flex items-center gap-3 mb-8 pb-6 border-b border-purple-500/20">
                            <motion.div
                                className={cn(
                                    "p-3 rounded-xl",
                                    hasContentBlocks ? "bg-purple-500/20" : "bg-blue-500/20",
                                    "border border-white/10"
                                )}
                                whileHover={{ scale: 1.1 }}
                            >
                                {hasContentBlocks ? (
                                    <Play className="w-5 h-5 text-purple-400" />
                                ) : (
                                    <BookOpen className="w-5 h-5 text-blue-400" />
                                )}
                            </motion.div>
                            <Headline level={2} className="text-white font-bold">
                                {hasContentBlocks ? "Interaktiv Lektion" : "Lektionsinnehåll"}
                            </Headline>
                            {hasContentBlocks && taskProgress && (
                                <motion.span
                                    className="ml-auto text-sm font-medium px-4 py-2 rounded-xl bg-purple-500/20 text-purple-300 border border-purple-500/30"
                                    animate={{ boxShadow: ["0 0 5px rgba(168,85,247,0.2)", "0 0 15px rgba(168,85,247,0.3)", "0 0 5px rgba(168,85,247,0.2)"] }}
                                    transition={{ duration: 2, repeat: Infinity }}
                                >
                                    {taskProgress.progress_percent || 0}% klart
                                </motion.span>
                            )}
                        </div>

                        <div className="relative">
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
                                <LessonContent
                                    content={filteredContent || placeholderContent}
                                    title={task.title}
                                    estimatedMinutes={task.estimated_minutes}
                                />
                            )}
                        </div>

                        {/* Related Tasks / Fördjupning */}
                        {relatedTasks.length > 0 && (
                            <RelatedTasks
                                tasks={relatedTasks}
                                moduleId={moduleId}
                                className="mt-10 pt-8 border-t border-purple-500/20"
                            />
                        )}
                    </motion.div>

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
                </motion.div>
            ) : null}
            </div>
        </div>
    )
}
