"use client"

/**
 * ============================================================================
 * SKILLSMAP NODE DETAIL PAGE — PREMIUM VIBRANT DESIGN
 * ============================================================================
 *
 * Features:
 * - Stunning gradient headers
 * - Color-coded difficulty and type badges
 * - Premium glass morphism effects
 * - Animated progress indicators
 * - Real lesson content from backend API
 *
 * @design VIBRANT-PREMIUM-2024
 */

import { useState, useEffect, useCallback } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
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
import { useAuth } from "@/components/auth"
import { LessonContent } from "@/components/learning"
import { usePlatform, filterContentByPlatform } from "@/hooks/useOperatingSystem"
import {
    getSkillsMap,
    getNode,
    markNodeComplete,
    isNodeComplete,
} from "@/lib/skillsmaps"
import {
    ArrowLeft,
    CheckCircle2,
    Clock,
    BookOpen,
    RefreshCw,
    AlertCircle,
    Zap,
    Target,
    Code2,
    HelpCircle,
    Trophy,
    Rocket,
    Sparkles,
    Star,
    Flame,
    Brain,
} from "lucide-react"

/* ============================================================================
   VIBRANT COLOR SYSTEM
   ============================================================================ */

const DIFFICULTY_COLORS = {
    easy: {
        gradient: "from-emerald-500 via-green-500 to-teal-500",
        bg: "bg-gradient-to-r from-emerald-500/10 to-teal-500/10",
        border: "border-emerald-500/30",
        text: "text-emerald-400",
        glow: "shadow-emerald-500/20",
    },
    medium: {
        gradient: "from-amber-500 via-orange-500 to-yellow-500",
        bg: "bg-gradient-to-r from-amber-500/10 to-orange-500/10",
        border: "border-amber-500/30",
        text: "text-amber-400",
        glow: "shadow-amber-500/20",
    },
    hard: {
        gradient: "from-rose-500 via-red-500 to-pink-500",
        bg: "bg-gradient-to-r from-rose-500/10 to-red-500/10",
        border: "border-rose-500/30",
        text: "text-rose-400",
        glow: "shadow-rose-500/20",
    },
}

const TYPE_COLORS = {
    concept: {
        gradient: "from-violet-500 via-purple-500 to-indigo-500",
        bg: "bg-gradient-to-r from-violet-500/10 to-purple-500/10",
        border: "border-violet-500/30",
        text: "text-violet-400",
        Icon: BookOpen,
        label: "Koncept",
    },
    practice: {
        gradient: "from-cyan-500 via-blue-500 to-indigo-500",
        bg: "bg-gradient-to-r from-cyan-500/10 to-blue-500/10",
        border: "border-cyan-500/30",
        text: "text-cyan-400",
        Icon: Code2,
        label: "Praktik",
    },
    quiz: {
        gradient: "from-fuchsia-500 via-pink-500 to-rose-500",
        bg: "bg-gradient-to-r from-fuchsia-500/10 to-pink-500/10",
        border: "border-fuchsia-500/30",
        text: "text-fuchsia-400",
        Icon: HelpCircle,
        label: "Quiz",
    },
    challenge: {
        gradient: "from-orange-500 via-red-500 to-rose-500",
        bg: "bg-gradient-to-r from-orange-500/10 to-red-500/10",
        border: "border-orange-500/30",
        text: "text-orange-400",
        Icon: Flame,
        label: "Utmaning",
    },
    project: {
        gradient: "from-emerald-500 via-teal-500 to-cyan-500",
        bg: "bg-gradient-to-r from-emerald-500/10 to-teal-500/10",
        border: "border-emerald-500/30",
        text: "text-emerald-400",
        Icon: Rocket,
        label: "Projekt",
    },
}

/* ============================================================================
   TYPES — Using types from skillsmaps lib
   ============================================================================ */

type NodeType = "concept" | "practice" | "quiz" | "challenge" | "project"
type NodeStatus = "not_started" | "in_progress" | "complete"
type NodeDifficulty = "easy" | "medium" | "hard"

interface SkillsMapNode {
    id: string
    orderIndex: number
    title: string
    description: string
    type: NodeType
    difficulty: NodeDifficulty
    xpReward: number
    estimatedMinutes: number
    status: NodeStatus
    content?: string
}

interface SkillsMapDetailUI {
    id: string
    slug: string
    title: string
    description: string
    icon: string
    color: string
    totalNodes: number
    completedNodes: number
    totalXP: number
    estimatedHours: number
    difficulty: "beginner" | "intermediate" | "advanced" | "expert"
    nodes: SkillsMapNode[]
}

/* ============================================================================
   SKELETON
   ============================================================================ */

function NodeDetailSkeleton() {
    return (
        <div className="space-y-6">
            {/* Header skeleton */}
            <div className="relative rounded-3xl overflow-hidden">
                <div className="absolute inset-0 bg-gradient-to-r from-violet-600/20 via-purple-600/20 to-indigo-600/20 animate-pulse" />
                <div className="relative p-8 space-y-4">
                    <div className="h-6 w-32 rounded-lg bg-zinc-800 animate-pulse" />
                    <div className="h-10 w-96 rounded-lg bg-zinc-800 animate-pulse" />
                    <div className="h-5 w-64 rounded-lg bg-zinc-800 animate-pulse" />
                    <div className="flex gap-3 pt-4">
                        <div className="h-8 w-24 rounded-xl bg-zinc-800 animate-pulse" />
                        <div className="h-8 w-24 rounded-xl bg-zinc-800 animate-pulse" />
                        <div className="h-8 w-24 rounded-xl bg-zinc-800 animate-pulse" />
                    </div>
                </div>
            </div>

            {/* Content skeleton */}
            <div className="rounded-3xl bg-zinc-900/80 p-8 space-y-4">
                <div className="h-6 w-48 rounded-lg bg-zinc-800 animate-pulse" />
                <div className="space-y-3 pt-4">
                    <div className="h-4 w-full rounded bg-zinc-800 animate-pulse" />
                    <div className="h-4 w-5/6 rounded bg-zinc-800 animate-pulse" />
                    <div className="h-4 w-4/6 rounded bg-zinc-800 animate-pulse" />
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   ERROR STATE
   ============================================================================ */

function ErrorState({ error, onRetry, slug }: { error: string; onRetry: () => void; slug: string }) {
    return (
        <div className="relative rounded-3xl overflow-hidden max-w-md mx-auto">
            {/* Background glow */}
            <div className="absolute inset-0 bg-gradient-to-r from-rose-500/10 via-red-500/10 to-pink-500/10" />

            <div className="relative p-8 text-center">
                <div className={cn(
                    "w-20 h-20 rounded-2xl mx-auto mb-6",
                    "bg-gradient-to-br from-rose-500 to-red-500",
                    "flex items-center justify-center",
                    "shadow-xl shadow-rose-500/30"
                )}>
                    <AlertCircle className="w-10 h-10 text-white" />
                </div>
                <h2 className={cn(
                    "text-2xl font-bold mb-3",
                    "bg-clip-text text-transparent",
                    "bg-gradient-to-r from-rose-400 to-red-400"
                )}>
                    Node hittades inte
                </h2>
                <p className="text-zinc-400 mb-8">{error}</p>
                <div className="flex gap-4 justify-center">
                    <Link prefetch={false} href={`/skillsmaps/${slug}`}>
                        <Button
                            variant="outline"
                            className={cn(
                                "rounded-xl px-6",
                                "border-zinc-700 hover:border-violet-500/50",
                                "hover:bg-violet-500/10"
                            )}
                        >
                            <ArrowLeft className="w-4 h-4 mr-2" />
                            Tillbaka
                        </Button>
                    </Link>
                    <Button
                        onClick={onRetry}
                        className={cn(
                            "rounded-xl px-6",
                            "bg-gradient-to-r from-violet-500 to-purple-500",
                            "hover:from-violet-600 hover:to-purple-600",
                            "shadow-lg shadow-violet-500/25"
                        )}
                    >
                        <RefreshCw className="w-4 h-4 mr-2" />
                        Försök igen
                    </Button>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   NODE DETAIL PAGE
   ============================================================================ */

export default function SkillsMapNodeDetailPage() {
    const params = useParams()
    const router = useRouter()
    const { user } = useAuth()
    const { platform: platformConfig, os, distro } = usePlatform()
    const slug = params?.slug as string
    const nodeId = params?.nodeId as string

    const [skillsmap, setSkillsmap] = useState<SkillsMapDetailUI | null>(null)
    const [node, setNode] = useState<SkillsMapNode | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [completing, setCompleting] = useState(false)
    const [isCompleted, setIsCompleted] = useState(false)

    const fetchData = useCallback(async () => {
        setLoading(true)
        setError(null)

        try {
            // REAL API CALL - NO MOCK DATA
            const skillsmapResult = await getSkillsMap(slug)
            if (!skillsmapResult.ok) {
                setError(skillsmapResult.message)
                return
            }

            const skillsmapData = skillsmapResult.data

            // Find the node in the skillsmap
            const nodeData = skillsmapData.nodes.find(n => n.id === nodeId)
            if (!nodeData) {
                // Try fetching node directly
                const nodeResult = await getNode(nodeId)
                if (!nodeResult.ok) {
                    setError("Denna nod finns inte")
                    return
                }
                setNode(nodeResult.data)
            } else {
                setNode(nodeData)
            }

            setSkillsmap({
                ...skillsmapData,
                nodes: skillsmapData.nodes as any,
            })

            // Check completion status
            setIsCompleted(isNodeComplete(slug, nodeId))
        } catch (err) {
            setError(err instanceof Error ? err.message : "Ett fel uppstod")
        } finally {
            setLoading(false)
        }
    }, [slug, nodeId])

    useEffect(() => {
        fetchData()
    }, [fetchData])

    const handleMarkComplete = async () => {
        setCompleting(true)
        await new Promise((resolve) => setTimeout(resolve, 300))

        // Mark node complete using skillsmaps lib
        markNodeComplete(slug, nodeId)

        setIsCompleted(true)
        setCompleting(false)
    }

    // Find current node index and next/prev nodes
    const allNodes = skillsmap?.nodes || []
    const currentIndex = allNodes.findIndex(n => n.id === nodeId)
    const nextNode = currentIndex >= 0 && currentIndex < allNodes.length - 1
        ? allNodes[currentIndex + 1]
        : null
    const prevNode = currentIndex > 0
        ? allNodes[currentIndex - 1]
        : null

    const handleContinue = () => {
        if (nextNode) {
            router.push(`/skillsmaps/${slug}/nodes/${nextNode.id}`)
        } else {
            // No more nodes, go back to skillsmap
            router.push(`/skillsmaps/${slug}`)
        }
    }

    // Filter content based on user's platform selection
    const filteredContent = node?.content
        ? filterContentByPlatform(node.content, os, distro)
        : null

    return (
        <PageLayout maxWidth="standard" background="gray">
            {/* Premium back button */}
            <Link
                href={`/skillsmaps/${slug}`}
                className={cn(
                    "inline-flex items-center gap-2 text-sm mb-8 group",
                    "text-zinc-500 hover:text-violet-400",
                    "transition-all duration-300"
                )}
            >
                <div className={cn(
                    "w-8 h-8 rounded-lg flex items-center justify-center",
                    "bg-zinc-800/50 group-hover:bg-violet-500/20",
                    "border border-zinc-700/50 group-hover:border-violet-500/30",
                    "transition-all duration-300"
                )}>
                    <ArrowLeft className="w-4 h-4" />
                </div>
                <span>Tillbaka till {skillsmap?.title || "SkillsMap"}</span>
            </Link>

            {loading ? (
                <NodeDetailSkeleton />
            ) : error ? (
                <ErrorState error={error} onRetry={fetchData} slug={slug} />
            ) : node && skillsmap ? (
                <div className="space-y-8">
                    {/* PREMIUM NODE HEADER */}
                    <Section>
                        <div className="relative rounded-3xl overflow-hidden">
                            {/* Background gradient based on node type */}
                            <div className={cn(
                                "absolute inset-0",
                                `bg-gradient-to-r ${TYPE_COLORS[node.type as keyof typeof TYPE_COLORS]?.gradient || TYPE_COLORS.concept.gradient}`,
                                "opacity-10"
                            )} />

                            {/* Animated glow */}
                            <div className={cn(
                                "absolute -inset-1 rounded-3xl blur-2xl opacity-20",
                                `bg-gradient-to-r ${TYPE_COLORS[node.type as keyof typeof TYPE_COLORS]?.gradient || TYPE_COLORS.concept.gradient}`
                            )} />

                            <div className={cn(
                                "relative p-8 md:p-10",
                                "bg-zinc-900/80 backdrop-blur-xl",
                                "border border-white/10 rounded-3xl"
                            )}>
                                {/* Top row: progress + completion */}
                                <div className="flex items-center justify-between mb-6">
                                    <div className="flex items-center gap-3">
                                        <div className={cn(
                                            "px-4 py-2 rounded-xl",
                                            "bg-zinc-800/80 border border-zinc-700/50",
                                            "text-sm font-medium text-zinc-400"
                                        )}>
                                            Nod {node.orderIndex} av {skillsmap.totalNodes}
                                        </div>

                                        {isCompleted && (
                                            <div className={cn(
                                                "flex items-center gap-2 px-4 py-2 rounded-xl",
                                                "bg-gradient-to-r from-emerald-500/10 to-teal-500/10",
                                                "border border-emerald-500/30",
                                                "text-emerald-400 font-medium"
                                            )}>
                                                <CheckCircle2 className="w-4 h-4" />
                                                <span>Slutförd</span>
                                            </div>
                                        )}
                                    </div>

                                    {/* XP Badge */}
                                    <div className={cn(
                                        "flex items-center gap-2 px-5 py-2.5 rounded-xl",
                                        "bg-gradient-to-r from-amber-500/10 to-orange-500/10",
                                        "border border-amber-500/30"
                                    )}>
                                        <Zap className="w-5 h-5 text-amber-400" />
                                        <span className={cn(
                                            "text-lg font-bold",
                                            "bg-clip-text text-transparent",
                                            "bg-gradient-to-r from-amber-400 to-orange-400"
                                        )}>
                                            +{node.xpReward} XP
                                        </span>
                                    </div>
                                </div>

                                {/* Title with gradient */}
                                <h1 className={cn(
                                    "text-3xl md:text-4xl font-black mb-4",
                                    "bg-clip-text text-transparent",
                                    "bg-gradient-to-r from-white via-zinc-200 to-zinc-400"
                                )}>
                                    {node.title}
                                </h1>

                                {/* Description */}
                                {node.description && (
                                    <p className="text-lg text-zinc-400 mb-8 max-w-2xl">
                                        {node.description}
                                    </p>
                                )}

                                {/* Meta badges */}
                                <div className="flex flex-wrap items-center gap-3">
                                    {/* Time */}
                                    <div className={cn(
                                        "flex items-center gap-2 px-4 py-2 rounded-xl",
                                        "bg-zinc-800/60 border border-zinc-700/50"
                                    )}>
                                        <Clock className="w-4 h-4 text-zinc-500" />
                                        <span className="text-sm font-medium text-zinc-400">
                                            {node.estimatedMinutes} min
                                        </span>
                                    </div>

                                    {/* Difficulty */}
                                    <div className={cn(
                                        "flex items-center gap-2 px-4 py-2 rounded-xl",
                                        DIFFICULTY_COLORS[node.difficulty as keyof typeof DIFFICULTY_COLORS]?.bg || DIFFICULTY_COLORS.easy.bg,
                                        DIFFICULTY_COLORS[node.difficulty as keyof typeof DIFFICULTY_COLORS]?.border || DIFFICULTY_COLORS.easy.border
                                    )}>
                                        <Star className={cn(
                                            "w-4 h-4",
                                            DIFFICULTY_COLORS[node.difficulty as keyof typeof DIFFICULTY_COLORS]?.text || DIFFICULTY_COLORS.easy.text
                                        )} />
                                        <span className={cn(
                                            "text-sm font-bold uppercase tracking-wide",
                                            DIFFICULTY_COLORS[node.difficulty as keyof typeof DIFFICULTY_COLORS]?.text || DIFFICULTY_COLORS.easy.text
                                        )}>
                                            {node.difficulty === "easy" ? "Enkel" : node.difficulty === "medium" ? "Medel" : "Svår"}
                                        </span>
                                    </div>

                                    {/* Type */}
                                    {(() => {
                                        const typeConfig = TYPE_COLORS[node.type as keyof typeof TYPE_COLORS] || TYPE_COLORS.concept
                                        const TypeIcon = typeConfig.Icon
                                        return (
                                            <div className={cn(
                                                "flex items-center gap-2 px-4 py-2 rounded-xl",
                                                typeConfig.bg,
                                                typeConfig.border
                                            )}>
                                                <TypeIcon className={cn("w-4 h-4", typeConfig.text)} />
                                                <span className={cn(
                                                    "text-sm font-bold uppercase tracking-wide",
                                                    typeConfig.text
                                                )}>
                                                    {typeConfig.label}
                                                </span>
                                            </div>
                                        )
                                    })()}
                                </div>
                            </div>
                        </div>
                    </Section>

                    {/* PREMIUM LESSON CONTENT */}
                    <Section>
                        <div className="relative rounded-3xl overflow-hidden">
                            {/* Subtle glow */}
                            <div className="absolute -inset-1 rounded-3xl blur-2xl opacity-10 bg-gradient-to-r from-violet-500 via-purple-500 to-indigo-500" />

                            <div className={cn(
                                "relative",
                                "bg-zinc-900/80 backdrop-blur-xl",
                                "border border-white/10 rounded-3xl",
                                "p-6 md:p-10"
                            )}>
                                {/* Section header */}
                                <div className="flex items-center gap-4 mb-8 pb-6 border-b border-white/10">
                                    <div className={cn(
                                        "w-12 h-12 rounded-xl flex items-center justify-center",
                                        "bg-gradient-to-br from-violet-500 to-purple-500",
                                        "shadow-lg shadow-violet-500/25"
                                    )}>
                                        <BookOpen className="w-6 h-6 text-white" />
                                    </div>
                                    <div>
                                        <h2 className={cn(
                                            "text-xl font-bold",
                                            "bg-clip-text text-transparent",
                                            "bg-gradient-to-r from-violet-400 to-purple-400"
                                        )}>
                                            Lektionsinnehåll
                                        </h2>
                                        <p className="text-sm text-zinc-500">
                                            Läs igenom materialet och slutför lektionen
                                        </p>
                                    </div>
                                </div>

                                <LessonContent
                                    content={filteredContent || node.content || ""}
                                    title={node.title}
                                    estimatedMinutes={node.estimatedMinutes}
                                />
                            </div>
                        </div>
                    </Section>

                    {/* Premium Task Footer */}
                    <TaskFooter
                        prevTaskUrl={prevNode ? `/skillsmaps/${slug}/nodes/${prevNode.id}` : undefined}
                        nextTaskUrl={nextNode ? `/skillsmaps/${slug}/nodes/${nextNode.id}` : undefined}
                        onComplete={handleMarkComplete}
                        xp={node.xpReward}
                        difficulty={node.difficulty as 'easy' | 'medium' | 'hard'}
                        isCompleted={isCompleted}
                        isLoading={completing}
                    />
                </div>
            ) : null}
        </PageLayout>
    )
}
