"use client"

/**
 * ============================================================================
 * SKILLSMAP NODE DETAIL PAGE — REAL API DATA, NO MOCK DATA
 * ============================================================================
 *
 * Features:
 * - Real lesson content from backend API
 * - Interactive content blocks (quiz, terminal, checkpoint)
 * - Progress tracking with read progress bar
 * - Mark as complete button
 * - Navigation to next node
 *
 * @phase SKILLSMAPS-API-INTEGRATION
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
} from "lucide-react"

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
        <div className="space-y-6 animate-pulse">
            <div className="h-8 w-48 rounded bg-zinc-800" />
            <div className="h-64 rounded-2xl bg-zinc-800" />
            <div className="space-y-3">
                <div className="h-4 w-full rounded bg-zinc-800" />
                <div className="h-4 w-3/4 rounded bg-zinc-800" />
                <div className="h-4 w-5/6 rounded bg-zinc-800" />
            </div>
        </div>
    )
}

/* ============================================================================
   ERROR STATE
   ============================================================================ */

function ErrorState({ error, onRetry, slug }: { error: string; onRetry: () => void; slug: string }) {
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
                    "bg-red-900/30",
                    "flex items-center justify-center"
                )}
            >
                <AlertCircle className="w-8 h-8 text-red-500" />
            </div>
            <h2 className="text-xl font-semibold text-white mb-2">
                Node hittades inte
            </h2>
            <p className="text-zinc-400 mb-6">{error}</p>
            <div className="flex gap-3 justify-center">
                <Link href={`/skillsmaps/${slug}`}>
                    <Button variant="outline" className="rounded-xl">
                        <ArrowLeft className="w-4 h-4 mr-2" />
                        Tillbaka till SkillsMap
                    </Button>
                </Link>
                <Button onClick={onRetry} className="rounded-xl">
                    <RefreshCw className="w-4 h-4 mr-2" />
                    Försök igen
                </Button>
            </div>
        </GlassCard>
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
            {/* Back button */}
            <Link
                href={`/skillsmaps/${slug}`}
                className={cn(
                    "inline-flex items-center gap-2 text-sm mb-6",
                    "text-zinc-500 hover:text-white",
                    "transition-colors"
                )}
            >
                <ArrowLeft className="w-4 h-4" />
                Tillbaka till {skillsmap?.title || "SkillsMap"}
            </Link>

            {loading ? (
                <NodeDetailSkeleton />
            ) : error ? (
                <ErrorState error={error} onRetry={fetchData} slug={slug} />
            ) : node && skillsmap ? (
                <div className="space-y-8">
                    {/* Node Header */}
                    <Section>
                        <Block className="bg-zinc-900/80 backdrop-blur-xl rounded-2xl border border-zinc-700/50 shadow-lg p-6 md:p-8">
                            <div className="flex flex-col md:flex-row md:items-start gap-4">
                                {/* Node info */}
                                <div className="flex-1">
                                    <div className="flex items-center gap-2 mb-2">
                                        <span className="text-xs font-medium text-zinc-400">
                                            Nod {node.orderIndex} av {skillsmap.totalNodes}
                                        </span>
                                        {isCompleted && (
                                            <span className="inline-flex items-center gap-1 text-xs text-emerald-500 font-medium">
                                                <CheckCircle2 className="w-3.5 h-3.5" />
                                                Slutförd
                                            </span>
                                        )}
                                    </div>
                                    <Headline level={1} className="mb-2 text-white">
                                        {node.title}
                                    </Headline>
                                    {node.description && (
                                        <Subtext className="mb-4 text-zinc-400">
                                            {node.description}
                                        </Subtext>
                                    )}

                                    {/* Meta */}
                                    <div className="flex flex-wrap items-center gap-4">
                                        <span className="flex items-center gap-1.5 text-sm text-zinc-500">
                                            <Clock className="w-4 h-4" />
                                            {node.estimatedMinutes} min
                                        </span>
                                        <span className="flex items-center gap-1.5 text-sm text-amber-400 font-medium">
                                            <Zap className="w-4 h-4" />
                                            +{node.xpReward} XP
                                        </span>
                                        <span className={cn(
                                            "px-2 py-0.5 rounded text-xs font-medium",
                                            node.difficulty === "easy" && "bg-emerald-900/50 text-emerald-400",
                                            node.difficulty === "medium" && "bg-amber-900/50 text-amber-400",
                                            node.difficulty === "hard" && "bg-red-900/50 text-red-400",
                                        )}>
                                            {node.difficulty === "easy" ? "Enkel" : node.difficulty === "medium" ? "Medel" : "Svår"}
                                        </span>
                                        <span className={cn(
                                            "px-2 py-0.5 rounded text-xs font-medium",
                                            "bg-purple-900/50 text-purple-400"
                                        )}>
                                            {node.type === "concept" ? "Koncept" :
                                                node.type === "practice" ? "Praktik" :
                                                    node.type === "quiz" ? "Quiz" :
                                                        node.type === "challenge" ? "Utmaning" : "Projekt"}
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </Block>
                    </Section>

                    {/* Lesson Content */}
                    <Section>
                        <Block className="bg-zinc-900/80 backdrop-blur-xl rounded-2xl border border-zinc-700/50 shadow-lg p-6 md:p-8">
                            <div className="flex items-center gap-2 mb-6 pb-4 border-b border-zinc-700">
                                <BookOpen className="w-5 h-5 text-purple-400" />
                                <Headline level={2} className="text-white">
                                    Lektionsinnehåll
                                </Headline>
                            </div>

                            <LessonContent
                                content={filteredContent || node.content || ""}
                                title={node.title}
                                estimatedMinutes={node.estimatedMinutes}
                            />
                        </Block>
                    </Section>

                    {/* Actions - Using TaskFooter from @saas/ui */}
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
