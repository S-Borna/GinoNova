"use client"

/**
 * ============================================================================
 * SKILLSMAPS LIST PAGE — REAL API DATA, NO MOCK DATA
 * ============================================================================
 *
 * Main SkillsMaps page with:
 * - Platform check (shows PlatformSelector if OS not chosen)
 * - Premium SkillsMapSelector grid
 * - Category filtering and search
 * - Progress tracking from real backend API
 *
 * @phase SKILLSMAPS-API-INTEGRATION
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
   LOADING SKELETON
   ============================================================================ */

function PageSkeleton() {
    return (
        <div className="space-y-8 animate-pulse">
            <div className="h-48 rounded-3xl bg-zinc-800/50" />
            <div className="flex gap-3">
                {Array.from({ length: 5 }).map((_, i) => (
                    <div key={i} className="h-10 w-28 rounded-xl bg-zinc-800/50" />
                ))}
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {Array.from({ length: 6 }).map((_, i) => (
                    <div key={i} className="h-72 rounded-2xl bg-zinc-800/50" />
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
                Kunde inte ladda SkillsMaps
            </h2>
            <p className="text-zinc-400 mb-6">{error}</p>
            <Button onClick={onRetry} className="rounded-xl">
                <RefreshCw className="w-4 h-4 mr-2" />
                Försök igen
            </Button>
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
            <PageLayout maxWidth="wide" background="gray">
                <PageSkeleton />
            </PageLayout>
        )
    }

    if (loading) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <PageSkeleton />
            </PageLayout>
        )
    }

    if (error) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <ErrorState error={error} onRetry={fetchSkillsMaps} />
            </PageLayout>
        )
    }

    return (
        <PageLayout maxWidth="wide" background="gray">
            <AnimatePresence>
                <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 0.3 }}
                >
                    <Section spacing="none">
                        <SkillsMapSelector skillsmaps={skillsmaps} />
                    </Section>
                </motion.div>
            </AnimatePresence>
        </PageLayout>
    )
}
