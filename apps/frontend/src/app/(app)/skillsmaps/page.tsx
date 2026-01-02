"use client"

/**
 * ============================================================================
 * SKILLSMAPS LIST PAGE — DOE25 PREMIUM DESIGN
 * ============================================================================
 *
 * Premium SkillsMaps page with DOE25 Tenta-style design:
 * - COSMIC background with aurora effects
 * - Hero header with stats grid
 * - Premium progress tracking
 *
 * @phase DOE25-REDESIGN
 */

import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import Link from "next/link"
import { motion, AnimatePresence } from "framer-motion"
import { usePlatform } from "@/hooks/useOperatingSystem"
import { SkillsMapSelector, SkillsMapCardProps } from "@/components/skillsmaps"
import { CosmicAurora } from "@/components/ui/cosmic-aurora"
import {
    RefreshCw,
    AlertCircle,
    ArrowLeft,
    BookOpen,
    Target,
    Trophy,
    Clock,
    Zap,
    Play,
    ChevronRight,
    Map,
    Sparkles
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"
import { getSkillsMaps, getLocalProgress } from "@/lib/skillsmaps"

/* ============================================================================
   STATS CARD — Same as DOE25 Tenta
   ============================================================================ */

function StatCard({
    icon,
    label,
    value,
    color
}: {
    icon: React.ReactNode
    label: string
    value: string | number
    color: string
}) {
    return (
        <motion.div
            whileHover={{ scale: 1.02 }}
            className={cn(
                "flex items-center gap-4 p-4 rounded-xl",
                "bg-white/5 border border-white/10",
                "hover:border-white/20 transition-colors"
            )}
        >
            <div className={cn(
                "w-12 h-12 rounded-xl flex items-center justify-center",
                `bg-gradient-to-br ${color}`
            )}>
                {icon}
            </div>
            <div>
                <p className="text-2xl font-bold text-white">{value}</p>
                <p className="text-sm text-zinc-400">{label}</p>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   LOADING SKELETON — Premium Version ✨
   ============================================================================ */

function PageSkeleton() {
    return (
        <div className="min-h-screen bg-[#05050a] relative">
            <CosmicAurora />
            <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                <div className="space-y-8">
                    <div className="relative h-56 rounded-3xl bg-gradient-to-br from-purple-900/20 to-zinc-900 overflow-hidden">
                        <motion.div
                            className="absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent"
                            animate={{ x: ["-100%", "100%"] }}
                            transition={{ duration: 1.5, repeat: Infinity, ease: "linear" }}
                        />
                    </div>
                    <div className="flex gap-3">
                        {Array.from({ length: 5 }).map((_, i) => (
                            <div key={i} className="h-10 w-28 rounded-xl bg-purple-900/20" />
                        ))}
                    </div>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {Array.from({ length: 6 }).map((_, i) => (
                            <motion.div
                                key={i}
                                className="h-72 rounded-2xl bg-gradient-to-br from-purple-900/10 to-zinc-900"
                                animate={{ opacity: [0.5, 0.8, 0.5] }}
                                transition={{ duration: 2, repeat: Infinity, delay: i * 0.1 }}
                            />
                        ))}
                    </div>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   ERROR STATE — Premium Styled ❌
   ============================================================================ */

function ErrorState({ error, onRetry }: { error: string; onRetry: () => void }) {
    return (
        <div className="min-h-screen bg-[#05050a] relative">
            <CosmicAurora />
            <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                <motion.div
                    initial={{ opacity: 0, scale: 0.95 }}
                    animate={{ opacity: 1, scale: 1 }}
                    className={cn(
                        "max-w-md mx-auto text-center p-8 rounded-3xl",
                        "bg-gradient-to-br from-red-950/30 to-zinc-900",
                        "border border-red-500/30"
                    )}
                    style={{
                        boxShadow: "0 0 60px rgba(239,68,68,0.15)",
                    }}
                >
                    <motion.div
                        className={cn(
                            "w-20 h-20 mx-auto mb-6 rounded-2xl",
                            "bg-red-500/20 flex items-center justify-center"
                        )}
                        animate={{
                            boxShadow: [
                                "0 0 20px rgba(239,68,68,0.3)",
                                "0 0 40px rgba(239,68,68,0.5)",
                                "0 0 20px rgba(239,68,68,0.3)",
                            ]
                        }}
                        transition={{ duration: 2, repeat: Infinity }}
                    >
                        <AlertCircle className="w-10 h-10 text-red-400" />
                    </motion.div>
                    <h2 className="text-2xl font-bold text-white mb-3">
                        Kunde inte ladda SkillsMaps
                    </h2>
                    <p className="text-zinc-400 mb-8">{error}</p>
                    <Button
                        onClick={onRetry}
                        className="rounded-xl bg-gradient-to-r from-red-600 to-orange-600 hover:from-red-500 hover:to-orange-500"
                    >
                        <RefreshCw className="w-4 h-4 mr-2" />
                        Försök igen
                    </Button>
                </motion.div>
            </div>
        </div>
    )
}

/* ============================================================================
   SKILLSMAPS PAGE
   ============================================================================ */

export default function SkillsMapsPage() {
    const router = useRouter()
    const { hasSelected, isLoading: platformLoading } = usePlatform()
    const [skillsmaps, setSkillsmaps] = useState<SkillsMapCardProps[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    const fetchSkillsMaps = async () => {
        setLoading(true)
        setError(null)

        try {
            const result = await getSkillsMaps()

            if (!result.ok) {
                setError(result.message)
                return
            }

            const enhancedMaps = result.data.map(sm => {
                const progress = getLocalProgress(sm.slug)
                const completedNodes = progress.completedNodes.length
                let status: "not_started" | "in_progress" | "complete" = "not_started"

                if (completedNodes > 0 && completedNodes < sm.totalNodes) {
                    status = "in_progress"
                } else if (completedNodes >= sm.totalNodes && sm.totalNodes > 0) {
                    status = "complete"
                }

                return {
                    ...sm,
                    completedNodes,
                    status,
                }
            })

            setSkillsmaps(enhancedMaps)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Ett fel uppstod")
        } finally {
            setLoading(false)
        }
    }

    useEffect(() => {
        fetchSkillsMaps()
    }, [])

    useEffect(() => {
        if (!platformLoading && !hasSelected) {
            console.log("[SkillsMaps] No OS selected, redirecting to /learn")
            router.push("/learn")
        }
    }, [platformLoading, hasSelected, router])

    if (platformLoading || !hasSelected) {
        return <PageSkeleton />
    }

    if (loading) {
        return <PageSkeleton />
    }

    if (error) {
        return <ErrorState error={error} onRetry={fetchSkillsMaps} />
    }

    // Calculate stats
    const totalMaps = skillsmaps.length
    const completedMaps = skillsmaps.filter(sm => sm.status === "complete").length
    const inProgressMaps = skillsmaps.filter(sm => sm.status === "in_progress").length
    const totalNodes = skillsmaps.reduce((acc, sm) => acc + sm.totalNodes, 0)
    const completedNodes = skillsmaps.reduce((acc, sm) => acc + (sm.completedNodes || 0), 0)
    const progressPercent = totalNodes > 0 ? Math.round((completedNodes / totalNodes) * 100) : 0

    // Find first in-progress or not-started map
    const continueMap = skillsmaps.find(sm => sm.status === "in_progress") ||
        skillsmaps.find(sm => sm.status === "not_started")

    return (
        <div className="min-h-screen bg-[#05050a] relative">
            <CosmicAurora />

            <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {/* Back */}
                <Link
                    href="/learn"
                    className={cn(
                        "inline-flex items-center gap-2 text-sm mb-8 px-4 py-2 rounded-xl",
                        "text-zinc-400 hover:text-white",
                        "bg-white/5 hover:bg-white/10 border border-white/10",
                        "transition-all duration-300"
                    )}
                >
                    <ArrowLeft className="w-4 h-4" />
                    Tillbaka till Learning
                </Link>

                {/* Hero Header — DOE25 Style */}
                <motion.div
                    initial={{ opacity: 0, y: -20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className={cn(
                        "relative overflow-hidden rounded-3xl mb-8",
                        "bg-gradient-to-br from-purple-500/10 via-pink-500/10 to-cyan-500/10",
                        "border border-purple-500/20",
                        "p-8 md:p-12"
                    )}
                >
                    {/* Background Glow */}
                    <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/20 rounded-full blur-[100px]" />
                    <div className="absolute bottom-0 left-0 w-64 h-64 bg-cyan-500/10 rounded-full blur-[80px]" />

                    <div className="relative">
                        <div className="flex flex-col md:flex-row md:items-start gap-6 mb-8">
                            {/* Icon */}
                            <motion.div
                                whileHover={{ scale: 1.05, rotate: 5 }}
                                className={cn(
                                    "w-24 h-24 rounded-3xl flex items-center justify-center shrink-0",
                                    "bg-gradient-to-br from-purple-500/30 to-pink-500/30",
                                    "border border-purple-500/40 shadow-lg shadow-purple-500/20"
                                )}
                            >
                                <span className="text-6xl">🗺️</span>
                            </motion.div>

                            <div className="flex-1">
                                <div className="flex items-center gap-3 mb-3">
                                    <span className="px-3 py-1 rounded-full bg-purple-500/20 border border-purple-500/30 text-purple-400 text-xs font-bold uppercase tracking-wider">
                                        Learning Paths
                                    </span>
                                    <span className="px-3 py-1 rounded-full bg-cyan-500/20 border border-cyan-500/30 text-cyan-400 text-xs font-bold">
                                        {totalMaps} SkillsMaps
                                    </span>
                                </div>

                                <h1 className="text-3xl md:text-5xl font-black text-white mb-4">
                                    SkillsMaps
                                </h1>

                                <p className="text-lg text-zinc-300 max-w-2xl mb-6">
                                    Interaktiva kunskapsstigar för att bemästra DevOps, Cloud, AI och mer.
                                    Följ dina framsteg och lås upp nya kunskaper.
                                </p>

                                {/* CTA */}
                                {continueMap && (
                                    <Link href={`/skillsmaps/${continueMap.slug}`}>
                                        <motion.button
                                            whileHover={{ scale: 1.02 }}
                                            whileTap={{ scale: 0.98 }}
                                            className={cn(
                                                "flex items-center gap-3 px-6 py-3 rounded-xl",
                                                "bg-gradient-to-r from-purple-600 to-cyan-600",
                                                "text-white font-semibold",
                                                "shadow-lg shadow-purple-500/30",
                                                "hover:shadow-xl hover:shadow-purple-500/40",
                                                "transition-all duration-300"
                                            )}
                                        >
                                            <Play className="w-5 h-5 fill-white" />
                                            {inProgressMaps > 0 ? "Fortsätt lära dig" : "Börja utforska"}
                                            <ChevronRight className="w-5 h-5" />
                                        </motion.button>
                                    </Link>
                                )}
                            </div>
                        </div>

                        {/* Stats Grid */}
                        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                            <StatCard
                                icon={<Map className="w-6 h-6 text-white" />}
                                label="SkillsMaps"
                                value={totalMaps}
                                color="from-purple-500 to-pink-500"
                            />
                            <StatCard
                                icon={<Target className="w-6 h-6 text-white" />}
                                label="Noder klara"
                                value={`${completedNodes}/${totalNodes}`}
                                color="from-emerald-500 to-green-500"
                            />
                            <StatCard
                                icon={<Trophy className="w-6 h-6 text-white" />}
                                label="Maps klara"
                                value={completedMaps}
                                color="from-amber-500 to-orange-500"
                            />
                            <StatCard
                                icon={<Sparkles className="w-6 h-6 text-white" />}
                                label="Progress"
                                value={`${progressPercent}%`}
                                color="from-cyan-500 to-blue-500"
                            />
                        </div>
                    </div>
                </motion.div>

                {/* Progress Bar */}
                <div className="mb-8 p-4 rounded-2xl bg-zinc-900/50 border border-zinc-800">
                    <div className="flex justify-between text-sm mb-2">
                        <span className="text-zinc-400">Total progress över alla SkillsMaps</span>
                        <span className="text-purple-400 font-medium">{progressPercent}% klar</span>
                    </div>
                    <div className="h-3 bg-zinc-800 rounded-full overflow-hidden">
                        <motion.div
                            initial={{ width: 0 }}
                            animate={{ width: `${progressPercent}%` }}
                            transition={{ duration: 1, ease: "easeOut" }}
                            className="h-full bg-gradient-to-r from-purple-500 via-pink-500 to-cyan-500 rounded-full"
                        />
                    </div>
                </div>

                {/* SkillsMap Selector with all maps */}
                <AnimatePresence>
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
                    >
                        <SkillsMapSelector skillsmaps={skillsmaps} />
                    </motion.div>
                </AnimatePresence>

                {/* Completion Message */}
                {completedMaps === totalMaps && totalMaps > 0 && (
                    <motion.div
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        className={cn(
                            "mt-8 p-8 rounded-3xl text-center",
                            "bg-gradient-to-r from-purple-500/20 via-pink-500/20 to-cyan-500/20",
                            "border border-purple-500/30"
                        )}
                    >
                        <motion.div
                            animate={{ rotate: [0, 10, -10, 0] }}
                            transition={{ duration: 0.5, repeat: Infinity, repeatDelay: 2 }}
                            className="text-6xl mb-4"
                        >
                            🎉
                        </motion.div>
                        <h2 className="text-2xl font-bold text-white mb-2">
                            Grattis! Du har klarat alla SkillsMaps!
                        </h2>
                        <p className="text-zinc-300">
                            Du är en sann DevOps-mästare! 🏆
                        </p>
                    </motion.div>
                )}
            </div>
        </div>
    )
}
