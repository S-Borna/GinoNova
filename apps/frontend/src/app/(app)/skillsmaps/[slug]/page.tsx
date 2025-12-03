"use client"

/**
 * ============================================================================
 * SKILLSMAP DETAIL PAGE — View Single SkillsMap with Nodes
 * ============================================================================
 *
 * Shows:
 * - SkillsMap header with progress
 * - List of nodes (like tasks)
 * - Node content viewer
 * - Premium design matching modules page
 *
 * @phase SKILLSMAPS-INTEGRATION
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

/* ============================================================================
   TYPES
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
   MOCK DATA — Will be replaced with API
   ============================================================================ */

function getMockSkillsMap(slug: string): SkillsMapDetailUI | null {
    const mockData: Record<string, SkillsMapDetailUI> = {
        linux: {
            id: "2",
            slug: "linux",
            title: "Linux Mastery",
            description: "Behärska Linux från kommandoraden till systemadministration och säkerhet. Denna SkillsMap tar dig från nybörjare till avancerad Linux-användare.",
            icon: "🐧",
            color: "#FCC624",
            totalNodes: 20,
            completedNodes: 5,
            totalXP: 2000,
            estimatedHours: 30,
            difficulty: "beginner",
            nodes: [
                {
                    id: "n1",
                    orderIndex: 1,
                    title: "Introduktion till Linux",
                    description: "Förstå Linux historia, distributioner och varför det är viktigt för DevOps",
                    type: "concept",
                    difficulty: "easy",
                    xpReward: 50,
                    estimatedMinutes: 15,
                    status: "complete",
                },
                {
                    id: "n2",
                    orderIndex: 2,
                    title: "Navigera filsystemet",
                    description: "Lär dig cd, ls, pwd och filsystemets struktur",
                    type: "practice",
                    difficulty: "easy",
                    xpReward: 75,
                    estimatedMinutes: 20,
                    status: "complete",
                },
                {
                    id: "n3",
                    orderIndex: 3,
                    title: "Filhantering",
                    description: "Skapa, kopiera, flytta och ta bort filer med cp, mv, rm, touch",
                    type: "practice",
                    difficulty: "easy",
                    xpReward: 100,
                    estimatedMinutes: 25,
                    status: "complete",
                },
                {
                    id: "n4",
                    orderIndex: 4,
                    title: "Permissions & Ownership",
                    description: "Förstå chmod, chown och Linux rättighetssystem",
                    type: "concept",
                    difficulty: "medium",
                    xpReward: 100,
                    estimatedMinutes: 30,
                    status: "complete",
                },
                {
                    id: "n5",
                    orderIndex: 5,
                    title: "Text Processing",
                    description: "Behärska cat, grep, sed, awk för textmanipulation",
                    type: "practice",
                    difficulty: "medium",
                    xpReward: 125,
                    estimatedMinutes: 35,
                    status: "complete",
                },
                {
                    id: "n6",
                    orderIndex: 6,
                    title: "Process Management",
                    description: "Hantera processer med ps, top, kill, htop och systemd",
                    type: "concept",
                    difficulty: "medium",
                    xpReward: 100,
                    estimatedMinutes: 30,
                    status: "in_progress",
                },
                {
                    id: "n7",
                    orderIndex: 7,
                    title: "Package Management",
                    description: "Installera och hantera paket med apt, yum, dnf",
                    type: "practice",
                    difficulty: "medium",
                    xpReward: 100,
                    estimatedMinutes: 25,
                    status: "not_started",
                },
                {
                    id: "n8",
                    orderIndex: 8,
                    title: "User & Group Management",
                    description: "Skapa och hantera användare och grupper",
                    type: "concept",
                    difficulty: "medium",
                    xpReward: 100,
                    estimatedMinutes: 30,
                    status: "not_started",
                },
                {
                    id: "n9",
                    orderIndex: 9,
                    title: "Networking Basics",
                    description: "IP-adresser, DNS, nätverkskommandon som ip, ss, netstat",
                    type: "concept",
                    difficulty: "medium",
                    xpReward: 125,
                    estimatedMinutes: 35,
                    status: "not_started",
                },
                {
                    id: "n10",
                    orderIndex: 10,
                    title: "SSH & Remote Access",
                    description: "Säker fjärråtkomst med SSH, nycklar och config",
                    type: "practice",
                    difficulty: "medium",
                    xpReward: 125,
                    estimatedMinutes: 30,
                    status: "not_started",
                },
            ],
        },
        docker: {
            id: "3",
            slug: "docker",
            title: "Docker",
            description: "Containerisering från grunderna till produktion med Docker och Docker Compose",
            icon: "🐳",
            color: "#2496ED",
            totalNodes: 20,
            completedNodes: 20,
            totalXP: 2000,
            estimatedHours: 20,
            difficulty: "intermediate",
            nodes: [
                {
                    id: "d1",
                    orderIndex: 1,
                    title: "Vad är Docker?",
                    description: "Förstå containers vs VMs och varför Docker förändrade DevOps",
                    type: "concept",
                    difficulty: "easy",
                    xpReward: 50,
                    estimatedMinutes: 15,
                    status: "complete",
                },
                {
                    id: "d2",
                    orderIndex: 2,
                    title: "Installera Docker",
                    description: "Installera Docker Desktop eller Docker Engine på ditt system",
                    type: "practice",
                    difficulty: "easy",
                    xpReward: 75,
                    estimatedMinutes: 20,
                    status: "complete",
                },
                {
                    id: "d3",
                    orderIndex: 3,
                    title: "Docker Images",
                    description: "Förstå images, layers och Docker Hub",
                    type: "concept",
                    difficulty: "easy",
                    xpReward: 75,
                    estimatedMinutes: 20,
                    status: "complete",
                },
                {
                    id: "d4",
                    orderIndex: 4,
                    title: "Dockerfile Basics",
                    description: "Skriva din första Dockerfile med FROM, RUN, COPY, CMD",
                    type: "practice",
                    difficulty: "medium",
                    xpReward: 100,
                    estimatedMinutes: 30,
                    status: "complete",
                },
                {
                    id: "d5",
                    orderIndex: 5,
                    title: "Container Lifecycle",
                    description: "Kör, stoppa, starta om och ta bort containers",
                    type: "practice",
                    difficulty: "easy",
                    xpReward: 75,
                    estimatedMinutes: 20,
                    status: "complete",
                },
            ],
        },
    }

    return mockData[slug] || null
}

/* ============================================================================
   SKELETON
   ============================================================================ */

function DetailSkeleton() {
    return (
        <div className="space-y-6 animate-pulse">
            <div className="h-48 rounded-3xl bg-zinc-800/50" />
            <div className="space-y-4">
                {Array.from({ length: 5 }).map((_, i) => (
                    <div key={i} className="h-28 rounded-2xl bg-zinc-800/50" />
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
                SkillsMap hittades inte
            </h2>
            <p className="text-zinc-400 mb-6">{error}</p>
            <div className="flex gap-3 justify-center">
                <Link href="/skillsmaps">
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
                "bg-gradient-to-br from-zinc-900 via-zinc-900/95 to-zinc-950",
                "border border-white/10",
                "p-8"
            )}
        >
            {/* Colored glow based on skillsmap color */}
            <div
                className="absolute top-0 right-0 w-[400px] h-[400px] rounded-full blur-[120px] opacity-20"
                style={{ backgroundColor: skillsmap.color }}
            />

            {/* Sparkle for complete */}
            {isComplete && (
                <motion.div
                    className="absolute top-6 right-6 text-emerald-400"
                    animate={{ rotate: 360 }}
                    transition={{ duration: 4, repeat: Infinity, ease: "linear" }}
                >
                    <Sparkles className="w-6 h-6" />
                </motion.div>
            )}

            <div className="relative flex flex-col md:flex-row md:items-start gap-6">
                {/* Icon */}
                <motion.div
                    className={cn(
                        "w-20 h-20 rounded-2xl flex items-center justify-center shrink-0",
                        "bg-gradient-to-br from-white/10 to-white/5",
                        "border border-white/10"
                    )}
                    style={{
                        boxShadow: `0 0 40px ${skillsmap.color}30`,
                    }}
                    whileHover={{ scale: 1.05 }}
                >
                    <span className="text-5xl">{skillsmap.icon}</span>
                </motion.div>

                {/* Content */}
                <div className="flex-1">
                    <h1 className={cn(
                        "text-3xl md:text-4xl font-black mb-2",
                        "bg-gradient-to-r from-white to-white/80 bg-clip-text text-transparent"
                    )}>
                        {skillsmap.title}
                    </h1>
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
                        <span className="flex items-center gap-1.5 text-amber-400 font-medium">
                            <Zap className="w-4 h-4" />
                            {skillsmap.totalXP} XP totalt
                        </span>
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
                            <span className="text-zinc-500">Progress</span>
                            <span className={cn(
                                "font-bold",
                                isComplete ? "text-emerald-400" : "text-purple-400"
                            )}>
                                {progress}%
                            </span>
                        </div>
                        <div className="h-2.5 bg-zinc-800 rounded-full overflow-hidden">
                            <motion.div
                                className="h-full rounded-full"
                                style={{
                                    background: isComplete
                                        ? "linear-gradient(90deg, #10b981, #14b8a6)"
                                        : `linear-gradient(90deg, ${skillsmap.color}, ${skillsmap.color}cc)`,
                                    boxShadow: `0 0 15px ${isComplete ? "#10b981" : skillsmap.color}50`,
                                }}
                                initial={{ width: 0 }}
                                animate={{ width: `${progress}%` }}
                                transition={{ duration: 1, ease: "easeOut" }}
                            />
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
            // TODO: Replace with actual API call
            await new Promise(resolve => setTimeout(resolve, 300))
            const data = getMockSkillsMap(slug)

            if (!data) {
                setError("Denna SkillsMap finns inte")
                return
            }

            setSkillsmap(data)
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
        <PageLayout maxWidth="standard" background="gray">
            {/* Back button */}
            <Link
                href="/skillsmaps"
                className={cn(
                    "inline-flex items-center gap-2 text-sm mb-6",
                    "text-zinc-500 hover:text-white",
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
                                    "rounded-xl px-6",
                                    "bg-gradient-to-r from-purple-600 to-indigo-600",
                                    "hover:from-purple-500 hover:to-indigo-500",
                                    "shadow-[0_0_20px_rgba(139,92,246,0.3)]"
                                )}
                            >
                                <Play className="w-4 h-4 mr-2" />
                                Fortsätt: {nextNode.title}
                                <ChevronRight className="w-4 h-4 ml-2" />
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
                                    transition={{ delay: 0.1 + index * 0.05 }}
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
        </PageLayout>
    )
}
