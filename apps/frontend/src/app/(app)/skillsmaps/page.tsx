"use client"

/**
 * ============================================================================
 * SKILLSMAPS LIST PAGE — MILESTONE 2.0 🎬
 * ============================================================================
 *
 * Netflix + Disney + Google Design Revolution
 *
 * Main SkillsMaps page with:
 * - COSMIC background with aurora effects
 * - Premium SkillsMapSelector grid
 * - Category filtering and search
 * - Progress tracking from real backend API
 *
 * @phase MILESTONE-2.0-DESIGN-REVOLUTION
 */

import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import { motion, AnimatePresence } from "framer-motion"
import { PageLayout, Section } from "@saas/ui"
import { usePlatform } from "@/hooks/useOperatingSystem"
import { SkillsMapSelector, SkillsMapCardProps } from "@/components/skillsmaps"
import { RefreshCw, AlertCircle } from "lucide-react"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"
import { getSkillsMaps, getLocalProgress } from "@/lib/skillsmaps"

/* ============================================================================
   LOADING SKELETON — Premium Version ✨
   ============================================================================ */

function PageSkeleton() {
    return (
        <div className="space-y-8">
            {/* Shimmer header skeleton */}
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
    )
}

/* ============================================================================
   ERROR STATE — Premium Styled ❌
   ============================================================================ */

function ErrorState({ error, onRetry }: { error: string; onRetry: () => void }) {
    return (
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
            // REAL API CALL - NO MOCK DATA
            const result = await getSkillsMaps()

            if (!result.ok) {
                setError(result.message)
                return
            }

            // Enhance with local progress data
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

    // Redirect to /learn if OS not selected
    useEffect(() => {
        if (!platformLoading && !hasSelected) {
            console.log("[SkillsMaps] No OS selected, redirecting to /learn")
            router.push("/learn")
        }
    }, [platformLoading, hasSelected, router])

    // Platform loading or redirecting
    if (platformLoading || !hasSelected) {
        return (
            <PageLayout maxWidth="wide" background="cosmic">
                <PageSkeleton />
            </PageLayout>
        )
    }

    if (loading) {
        return (
            <PageLayout maxWidth="wide" background="cosmic">
                <PageSkeleton />
            </PageLayout>
        )
    }

    if (error) {
        return (
            <PageLayout maxWidth="wide" background="cosmic">
                <ErrorState error={error} onRetry={fetchSkillsMaps} />
            </PageLayout>
        )
    }

    return (
        <PageLayout maxWidth="wide" background="cosmic">
            <AnimatePresence>
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
                >
                    <Section spacing="none">
                        <SkillsMapSelector skillsmaps={skillsmaps} />
                    </Section>
                </motion.div>
            </AnimatePresence>
        </PageLayout>
    )
}
