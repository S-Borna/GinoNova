"use client"

/**
 * ============================================================================
 * SKILLSMAP DETAIL PAGE — COSMIC EDITION 🌌
 * ============================================================================
 *
 * MILESTONE 2.0 DESIGN REVOLUTION
 *
 * Shows:
 * - SkillsMap header with progress
 * - List of nodes (tasks) from real backend API
 * - Node content viewer
 * - COSMIC aurora background
 *
 * @phase MILESTONE-2.0-COSMIC-REVOLUTION
 */

import { useState, useEffect } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import { motion, AnimatePresence } from "framer-motion"
import { PageLayout, Section, Block, Headline, Subtext } from "@saas/ui"
import { NodeCard, NodeCardProps, NodeType, NodeStatus } from "@/components/skillsmaps"
import { Button } from "@/components/ui/button"
import { ProgressBar } from "@/components/ui/progress-bar"
import { cn } from "@/lib/utils"
import { getSkillsMap, getLocalProgress, isNodeComplete, SkillsMapDetail } from "@/lib/skillsmaps"
import {
    ArrowLeft,
    Play,
    CheckCircle2,
    Clock,
    BookOpen,
    Zap,
    RefreshCw,
    AlertCircle,
    Sparkles,
    ChevronRight,
} from "lucide-react"
import { CosmicAurora } from "@/components/ui/cosmic-aurora"

/* ============================================================================
   Using shared CosmicAurora from @/components/ui/cosmic-aurora
   ============================================================================ */

/* ============================================================================
   TYPES — Using types from skillsmaps lib
   ============================================================================ */

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
    nodes: NodeCardProps[]
}

/* ============================================================================
   SKELETON
   ============================================================================ */

function DetailSkeleton() {
    return (
        <div className="space-y-6">
            {/* Shimmer header skeleton */}
            <div className="relative h-52 rounded-3xl bg-gradient-to-br from-purple-900/20 to-[#0a0a0f] overflow-hidden border border-purple-500/20">
                <motion.div
                    className="absolute inset-0 bg-gradient-to-r from-transparent via-purple-500/10 to-transparent"
                    animate={{ x: ["-100%", "100%"] }}
                    transition={{ duration: 1.5, repeat: Infinity, ease: "linear" }}
                />
            </div>
            <div className="space-y-4">
                {Array.from({ length: 5 }).map((_, i) => (
                    <motion.div
                        key={i}
                        className="h-28 rounded-2xl bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f] border border-purple-500/10"
                        animate={{ opacity: [0.5, 0.8, 0.5] }}
                        transition={{ duration: 2, repeat: Infinity, delay: i * 0.1 }}
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
        <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className={cn(
                "max-w-md mx-auto text-center p-8 rounded-2xl",
                "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                "border border-red-500/30",
                "shadow-[0_0_40px_rgba(239,68,68,0.15)]"
            )}
        >
            <motion.div
                className={cn(
                    "w-16 h-16 mx-auto mb-4 rounded-full",
                    "bg-red-500/20 flex items-center justify-center"
                )}
                animate={{
                    boxShadow: [
                        '0 0 20px rgba(239,68,68,0.2)',
                        '0 0 40px rgba(239,68,68,0.4)',
                        '0 0 20px rgba(239,68,68,0.2)'
                    ]
                }}
                transition={{ duration: 2, repeat: Infinity }}
            >
                <AlertCircle className="w-8 h-8 text-red-400" />
            </motion.div>
            <h2 className="text-xl font-semibold text-white mb-2">
                SkillsMap hittades inte
            </h2>
            <p className="text-zinc-400 mb-6">{error}</p>
            <div className="flex gap-3 justify-center">
                <Link prefetch={false} href="/skillsmaps">
                    <Button variant="outline" className="rounded-xl border-zinc-700 hover:border-purple-500/50 transition-all">
                        <ArrowLeft className="w-4 h-4 mr-2" />
                        Tillbaka
                    </Button>
                </Link>
                <Button
                    onClick={onRetry}
                    className="rounded-xl bg-gradient-to-r from-purple-600 to-violet-600 shadow-[0_0_20px_rgba(139,92,246,0.3)] hover:shadow-[0_0_30px_rgba(139,92,246,0.5)] transition-all"
                >
                    <RefreshCw className="w-4 h-4 mr-2" />
                    Försök igen
                </Button>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   HEADER COMPONENT
   ============================================================================ */

function SkillsMapHeader({ skillsmap }: { skillsmap: SkillsMapDetailUI }) {
    const progress = skillsmap.totalNodes > 0
        ? Math.round((skillsmap.completedNodes / skillsmap.totalNodes) * 100)
        : 0
    const isComplete = progress === 100

    return (
        <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "relative overflow-hidden rounded-3xl",
                "bg-gradient-to-br from-[#0d0d14] via-[#0a0a0f] to-[#08080c]",
                "border border-purple-500/30",
                "p-8",
                "shadow-[0_0_60px_rgba(139,92,246,0.15)]"
            )}
        >
            {/* Animated gradient background */}
            <div
                className="absolute inset-0 opacity-20"
                style={{
                    background: `radial-gradient(circle at 70% 30%, ${skillsmap.color}40, transparent 50%), radial-gradient(circle at 30% 70%, ${skillsmap.color}20, transparent 40%)`
                }}
            />

            {/* Colored glow based on skillsmap color */}
            <motion.div
                className="absolute top-0 right-0 w-[500px] h-[500px] rounded-full blur-[150px] opacity-20"
                style={{ backgroundColor: skillsmap.color }}
                animate={{ scale: [1, 1.1, 1], opacity: [0.15, 0.25, 0.15] }}
                transition={{ duration: 6, repeat: Infinity }}
            />

            {/* Second glow for depth */}
            <motion.div
                className="absolute bottom-0 left-1/4 w-[300px] h-[300px] rounded-full blur-[100px] opacity-15"
                style={{ backgroundColor: skillsmap.color }}
                animate={{ scale: [1.1, 1, 1.1], opacity: [0.1, 0.2, 0.1] }}
                transition={{ duration: 8, repeat: Infinity }}
            />

            {/* Sparkle for complete */}
            {isComplete && (
                <motion.div
                    className="absolute top-6 right-6 text-emerald-400"
                    animate={{
                        rotate: 360,
                        scale: [1, 1.2, 1],
                    }}
                    transition={{
                        rotate: { duration: 4, repeat: Infinity, ease: "linear" },
                        scale: { duration: 2, repeat: Infinity }
                    }}
                >
                    <Sparkles className="w-6 h-6" />
                </motion.div>
            )}

            <div className="relative flex flex-col md:flex-row md:items-start gap-6">
                {/* Icon with enhanced styling */}
                <motion.div
                    className={cn(
                        "w-24 h-24 rounded-2xl flex items-center justify-center shrink-0",
                        "bg-gradient-to-br from-white/15 to-white/5",
                        "border border-white/20",
                        "backdrop-blur-xl"
                    )}
                    style={{
                        boxShadow: `0 0 60px ${skillsmap.color}40, inset 0 0 30px ${skillsmap.color}10`,
                    }}
                    whileHover={{ scale: 1.08, rotate: 3 }}
                    transition={{ type: "spring", stiffness: 300 }}
                >
                    <span className="text-6xl drop-shadow-lg">{skillsmap.icon}</span>
                </motion.div>

                {/* Content */}
                <div className="flex-1">
                    <motion.h1
                        className={cn(
                            "text-3xl md:text-4xl font-black mb-2",
                            "bg-gradient-to-r from-white to-white/80 bg-clip-text text-transparent"
                        )}
                        animate={{
                            textShadow: [
                                `0 0 20px ${skillsmap.color}00`,
                                `0 0 30px ${skillsmap.color}40`,
                                `0 0 20px ${skillsmap.color}00`
                            ]
                        }}
                        transition={{ duration: 3, repeat: Infinity }}
                    >
                        {skillsmap.title}
                    </motion.h1>
                    <p className="text-zinc-400 mb-4 max-w-2xl">
                        {skillsmap.description}
                    </p>

                    {/* Meta row */}
                    <div className="flex flex-wrap items-center gap-4 mb-4 text-sm">
                        <span className="flex items-center gap-1.5 text-zinc-400">
                            <BookOpen className="w-4 h-4" />
                            {skillsmap.totalNodes} noder
                        </span>
                        <span className="flex items-center gap-1.5 text-zinc-400">
                            <Clock className="w-4 h-4" />
                            ~{skillsmap.estimatedHours}h
                        </span>
                        <motion.span
                            className="flex items-center gap-1.5 font-bold"
                            animate={{
                                textShadow: ['0 0 10px rgba(251,191,36,0)', '0 0 20px rgba(251,191,36,0.5)', '0 0 10px rgba(251,191,36,0)']
                            }}
                            transition={{ duration: 2, repeat: Infinity }}
                        >
                            <div className="p-1 rounded bg-gradient-to-r from-amber-500/20 to-yellow-500/20">
                                <Zap className="w-4 h-4 text-amber-400" />
                            </div>
                            <span className="bg-gradient-to-r from-amber-400 to-yellow-400 bg-clip-text text-transparent">
                                {skillsmap.totalXP} XP totalt
                            </span>
                        </motion.span>
                        <span className={cn(
                            "flex items-center gap-1.5 font-medium",
                            isComplete ? "text-emerald-400" : "text-purple-400"
                        )}>
                            <CheckCircle2 className="w-4 h-4" />
                            {skillsmap.completedNodes}/{skillsmap.totalNodes} klara
                        </span>
                    </div>

                    {/* Progress */}
                    <div className="max-w-md">
                        <div className="flex items-center justify-between text-sm mb-2">
                            <span className="text-zinc-400 font-medium">Progress</span>
                            <motion.span
                                className={cn(
                                    "font-black text-lg",
                                    isComplete ? "text-emerald-400" : "bg-gradient-to-r from-violet-400 to-purple-400 bg-clip-text text-transparent"
                                )}
                                animate={{
                                    textShadow: isComplete
                                        ? ['0 0 10px rgba(52,211,153,0.3)', '0 0 20px rgba(52,211,153,0.6)', '0 0 10px rgba(52,211,153,0.3)']
                                        : ['0 0 10px rgba(139,92,246,0.3)', '0 0 20px rgba(139,92,246,0.5)', '0 0 10px rgba(139,92,246,0.3)']
                                }}
                                transition={{ duration: 2, repeat: Infinity }}
                            >
                                {progress}%
                            </motion.span>
                        </div>
                        <div className="h-3 bg-zinc-800/50 rounded-full overflow-hidden border border-purple-500/20 relative">
                            <motion.div
                                className="h-full rounded-full relative"
                                style={{
                                    background: isComplete
                                        ? "linear-gradient(90deg, #10b981, #14b8a6, #06b6d4)"
                                        : `linear-gradient(90deg, ${skillsmap.color}, ${skillsmap.color}cc, ${skillsmap.color}99)`,
                                    boxShadow: `0 0 20px ${isComplete ? "#10b981" : skillsmap.color}60`,
                                }}
                                initial={{ width: 0 }}
                                animate={{ width: `${progress}%` }}
                                transition={{ duration: 1.2, ease: [0.16, 1, 0.3, 1] }}
                            >
                                {/* Shimmer effect */}
                                <motion.div
                                    className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent"
                                    animate={{ x: ["-100%", "200%"] }}
                                    transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
                                />
                            </motion.div>
                        </div>
                    </div>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   SKILLSMAP DETAIL PAGE
   ============================================================================ */

export default function SkillsMapDetailPage() {
    const params = useParams()
    const router = useRouter()
    const slug = params?.slug as string

    const [skillsmap, setSkillsmap] = useState<SkillsMapDetailUI | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    const fetchSkillsMap = async () => {
        setLoading(true)
        setError(null)

        try {
            // REAL API CALL - NO MOCK DATA
            const result = await getSkillsMap(slug)

            if (!result.ok) {
                setError(result.message)
                return
            }

            // Enhance nodes with completion status from localStorage
            const progress = getLocalProgress(slug)
            const enhancedNodes: NodeCardProps[] = result.data.nodes.map(node => ({
                ...node,
                status: isNodeComplete(slug, node.id) ? "complete" as NodeStatus : "not_started" as NodeStatus,
            }))

            const completedCount = enhancedNodes.filter(n => n.status === "complete").length

            setSkillsmap({
                ...result.data,
                nodes: enhancedNodes,
                completedNodes: completedCount,
            })
        } catch (err) {
            setError(err instanceof Error ? err.message : "Ett fel uppstod")
        } finally {
            setLoading(false)
        }
    }

    useEffect(() => {
        if (slug) {
            fetchSkillsMap()
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [slug])

    const handleNodeClick = (nodeId: string) => {
        router.push(`/skillsmaps/${slug}/nodes/${nodeId}`)
    }

    // Find next incomplete node
    const nextNode = skillsmap?.nodes.find(n => n.status !== "complete")

    const handleContinue = () => {
        if (nextNode) {
            handleNodeClick(nextNode.id)
        }
    }

    return (
        <div className="min-h-screen bg-[#05050a] relative overflow-hidden">
            {/* Cosmic Aurora Background */}
            <CosmicAurora />

            <div className="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {/* Back button */}
                <Link
                    href="/skillsmaps"
                    className={cn(
                        "inline-flex items-center gap-2 text-sm mb-6",
                        "text-zinc-500 hover:text-purple-400",
                        "transition-colors"
                    )}
                >
                    <ArrowLeft className="w-4 h-4" />
                    Tillbaka till SkillsMaps
                </Link>

                {loading ? (
                    <DetailSkeleton />
                ) : error ? (
                    <ErrorState error={error} onRetry={fetchSkillsMap} />
                ) : skillsmap ? (
                    <motion.div
                        className="space-y-8"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                    >
                        {/* Header */}
                        <SkillsMapHeader skillsmap={skillsmap} />

                        {/* Continue button */}
                        {nextNode && (
                            <motion.div
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.2 }}
                            >
                                <Button
                                    onClick={handleContinue}
                                    size="lg"
                                    className={cn(
                                        "rounded-2xl px-8 py-6 text-base font-bold",
                                        "bg-gradient-to-r from-violet-600 via-purple-600 to-indigo-600",
                                        "hover:from-violet-500 hover:via-purple-500 hover:to-indigo-500",
                                        "shadow-[0_0_40px_rgba(139,92,246,0.4)]",
                                        "hover:shadow-[0_0_60px_rgba(139,92,246,0.6)]",
                                        "transition-all duration-300",
                                        "border border-violet-500/30"
                                    )}
                                >
                                    <Play className="w-5 h-5 mr-2" />
                                    Fortsätt: {nextNode.title}
                                    <ChevronRight className="w-5 h-5 ml-2" />
                                </Button>
                            </motion.div>
                        )}

                        {/* Nodes list */}
                        <Section>
                            <Headline level={2} className="mb-4 text-white">
                                Noder
                            </Headline>
                            <div className="space-y-4">
                                {skillsmap.nodes.map((node, index) => (
                                    <motion.div
                                        key={node.id}
                                        initial={{ opacity: 0, x: -20 }}
                                        animate={{ opacity: 1, x: 0 }}
                                        transition={{ delay: 0.1 + index * 0.05, ease: [0.16, 1, 0.3, 1] }}
                                    >
                                        <NodeCard
                                            {...node}
                                            onClick={handleNodeClick}
                                        />
                                    </motion.div>
                                ))}
                            </div>
                        </Section>
                    </motion.div>
                ) : null}
            </div>
        </div>
    )
}
