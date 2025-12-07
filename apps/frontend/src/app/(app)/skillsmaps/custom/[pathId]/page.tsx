"use client"

/**
 * ============================================================================
 * CUSTOM PATH VIEW — Display User's Custom Learning Path
 * ============================================================================
 *
 * Shows a custom path with:
 * - Overview of all modules in the path
 * - Progress tracking per module
 * - Navigation to individual modules
 * - Edit/delete functionality
 *
 * @phase CUSTOM-PATHS
 */

import { useState, useEffect, useMemo } from "react"
import { useParams, useRouter } from "next/navigation"
import { motion, AnimatePresence } from "framer-motion"
import Link from "next/link"
import { PageLayout, Section } from "@saas/ui"
import { cn } from "@/lib/utils"
import {
    ArrowLeft,
    Star,
    Clock,
    Zap,
    BookOpen,
    ChevronRight,
    Pencil,
    Trash2,
    Rocket,
    CheckCircle2,
    Circle,
    PlayCircle,
    Sparkles,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import {
    getCustomPaths,
    deleteCustomPath,
    CustomPath,
} from "@/components/skillsmaps/CustomPathBuilder"
import { getLocalProgress } from "@/lib/skillsmaps"

/* ============================================================================
   MODULE CARD FOR CUSTOM PATH
   ============================================================================ */

function CustomPathModuleCard({
    module,
    index,
    progress,
    completedNodes,
    totalNodes,
}: {
    module: {
        id: string
        slug: string
        title: string
        icon: string
        color: string
        totalNodes: number
        totalXP: number
        estimatedHours: number
    }
    index: number
    progress: number
    completedNodes: number
    totalNodes: number
}) {
    const isComplete = progress === 100
    const isStarted = progress > 0

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.05 }}
        >
            <Link prefetch={false} href={`/skillsmaps/${module.slug}`}>
                <motion.div
                    className={cn(
                        "group relative overflow-hidden rounded-2xl",
                        "bg-gradient-to-br from-zinc-900/90 via-zinc-900/95 to-zinc-950/90",
                        "border border-white/[0.08]",
                        "p-5 transition-all duration-300",
                        "hover:border-white/20 hover:shadow-lg"
                    )}
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                >
                    {/* Order badge */}
                    <div className={cn(
                        "absolute top-4 left-4 w-8 h-8 rounded-lg",
                        "flex items-center justify-center",
                        "bg-gradient-to-br from-amber-500/20 to-orange-500/20",
                        "border border-amber-500/30",
                        "text-sm font-bold text-amber-300"
                    )}>
                        {index + 1}
                    </div>

                    {/* Status indicator */}
                    <div className="absolute top-4 right-4">
                        {isComplete ? (
                            <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                        ) : isStarted ? (
                            <PlayCircle className="w-5 h-5 text-purple-400" />
                        ) : (
                            <Circle className="w-5 h-5 text-zinc-600" />
                        )}
                    </div>

                    {/* Content */}
                    <div className="pt-8">
                        <div className="flex items-center gap-3 mb-3">
                            <div
                                className="w-12 h-12 rounded-xl flex items-center justify-center text-2xl"
                                style={{ backgroundColor: `${module.color}20` }}
                            >
                                {module.icon}
                            </div>
                            <div>
                                <h3 className="font-bold text-white">{module.title}</h3>
                                <div className="flex items-center gap-3 text-xs text-zinc-500 mt-1">
                                    <span className="flex items-center gap-1">
                                        <BookOpen className="w-3 h-3" />
                                        {totalNodes} noder
                                    </span>
                                    <span className="flex items-center gap-1 text-amber-400">
                                        <Zap className="w-3 h-3" />
                                        {module.totalXP} XP
                                    </span>
                                </div>
                            </div>
                        </div>

                        {/* Progress bar */}
                        <div className="mb-3">
                            <div className="flex items-center justify-between text-xs mb-1.5">
                                <span className="text-zinc-500">
                                    {completedNodes} / {totalNodes} klara
                                </span>
                                <span className={cn(
                                    "font-bold",
                                    isComplete ? "text-emerald-400" : "text-purple-400"
                                )}>
                                    {progress}%
                                </span>
                            </div>
                            <div className="h-1.5 bg-zinc-800 rounded-full overflow-hidden">
                                <motion.div
                                    className="h-full rounded-full"
                                    style={{
                                        backgroundColor: isComplete ? "#10b981" : module.color,
                                    }}
                                    initial={{ width: 0 }}
                                    animate={{ width: `${progress}%` }}
                                    transition={{ duration: 0.5 }}
                                />
                            </div>
                        </div>

                        {/* Action */}
                        <div className={cn(
                            "flex items-center justify-between",
                            "text-sm font-medium",
                            isComplete
                                ? "text-zinc-400"
                                : isStarted
                                    ? "text-purple-400"
                                    : "text-zinc-500"
                        )}>
                            <span>
                                {isComplete ? "Granska" : isStarted ? "Fortsätt" : "Börja"}
                            </span>
                            <ChevronRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                        </div>
                    </div>
                </motion.div>
            </Link>
        </motion.div>
    )
}

/* ============================================================================
   CUSTOM PATH PAGE
   ============================================================================ */

export default function CustomPathPage() {
    const params = useParams()
    const router = useRouter()
    const pathId = params?.pathId as string | undefined

    const [path, setPath] = useState<CustomPath | null>(null)
    const [loading, setLoading] = useState(true)

    // Load custom path
    useEffect(() => {
        if (!pathId) {
            setLoading(false)
            return
        }
        const paths = getCustomPaths()
        const found = paths.find((p) => p.id === pathId)
        setPath(found || null)
        setLoading(false)
    }, [pathId])

    // Calculate progress for each module
    const moduleProgress = useMemo(() => {
        if (!path) return []

        return path.modules.map((mod) => {
            const localProgress = getLocalProgress(mod.slug)
            const completedNodes = localProgress.completedNodes.length
            const totalNodes = mod.totalNodes
            const progress = totalNodes > 0
                ? Math.round((completedNodes / totalNodes) * 100)
                : 0

            return {
                module: mod,
                progress,
                completedNodes,
                totalNodes,
            }
        })
    }, [path])

    // Overall progress
    const overallProgress = useMemo(() => {
        if (moduleProgress.length === 0) return 0
        const total = moduleProgress.reduce((sum, m) => sum + m.progress, 0)
        return Math.round(total / moduleProgress.length)
    }, [moduleProgress])

    const handleDelete = () => {
        if (!path) return
        if (confirm("Är du säker på att du vill ta bort denna lärstig?")) {
            deleteCustomPath(path.id)
            router.push("/skillsmaps")
        }
    }

    // Find first incomplete module
    const nextModule = useMemo(() => {
        return moduleProgress.find((m) => m.progress < 100)?.module
    }, [moduleProgress])

    if (loading) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <div className="animate-pulse space-y-8">
                    <div className="h-48 rounded-3xl bg-zinc-800/50" />
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {Array.from({ length: 6 }).map((_, i) => (
                            <div key={i} className="h-48 rounded-2xl bg-zinc-800/50" />
                        ))}
                    </div>
                </div>
            </PageLayout>
        )
    }

    if (!path) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <div className="text-center py-16">
                    <h1 className="text-2xl font-bold text-white mb-4">
                        Lärstigen hittades inte
                    </h1>
                    <p className="text-zinc-400 mb-6">
                        Denna lärstig existerar inte eller har tagits bort.
                    </p>
                    <Button onClick={() => router.push("/skillsmaps")}>
                        <ArrowLeft className="w-4 h-4 mr-2" />
                        Tillbaka till SkillsMaps
                    </Button>
                </div>
            </PageLayout>
        )
    }

    return (
        <PageLayout maxWidth="wide" background="gray">
            {/* Header */}
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className={cn(
                    "relative overflow-hidden rounded-3xl mb-8",
                    "bg-gradient-to-br from-zinc-900 via-amber-950/10 to-zinc-900",
                    "border border-amber-500/20",
                    "p-8"
                )}
            >
                {/* Glow effect */}
                <div className="absolute top-0 right-0 w-[400px] h-[400px] bg-amber-500/10 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/4" />

                <div className="relative">
                    {/* Back link */}
                    <Link
                        href="/skillsmaps"
                        className="inline-flex items-center gap-2 text-zinc-400 hover:text-white transition-colors mb-6"
                    >
                        <ArrowLeft className="w-4 h-4" />
                        <span>Tillbaka till SkillsMaps</span>
                    </Link>

                    <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-6">
                        <div>
                            {/* Custom badge */}
                            <div className="flex items-center gap-2 mb-4">
                                <div className={cn(
                                    "flex items-center gap-1.5 px-3 py-1.5 rounded-full",
                                    "bg-amber-500/20 border border-amber-500/30"
                                )}>
                                    <Star className="w-3.5 h-3.5 text-amber-400 fill-current" />
                                    <span className="text-xs font-medium text-amber-300">
                                        Egen SkillsMap
                                    </span>
                                </div>
                            </div>

                            <h1 className={cn(
                                "text-3xl md:text-4xl font-black mb-2",
                                "bg-gradient-to-r from-white via-amber-200 to-white bg-clip-text text-transparent"
                            )}>
                                {path.name}
                            </h1>

                            {path.description && (
                                <p className="text-zinc-400 max-w-xl">{path.description}</p>
                            )}

                            {/* Stats */}
                            <div className="flex items-center gap-6 mt-4 text-sm text-zinc-400">
                                <span className="flex items-center gap-1.5">
                                    <BookOpen className="w-4 h-4" />
                                    {path.modules.length} moduler
                                </span>
                                <span className="flex items-center gap-1.5">
                                    <Clock className="w-4 h-4" />
                                    ~{path.estimatedHours}h
                                </span>
                                <span className="flex items-center gap-1.5 text-amber-400">
                                    <Zap className="w-4 h-4" />
                                    {path.totalXP.toLocaleString()} XP
                                </span>
                            </div>
                        </div>

                        {/* Actions */}
                        <div className="flex items-center gap-3">
                            <Button
                                variant="outline"
                                size="sm"
                                onClick={() => router.push(`/skillsmaps?edit=${path.id}`)}
                                className="rounded-xl"
                            >
                                <Pencil className="w-4 h-4 mr-2" />
                                Redigera
                            </Button>
                            <Button
                                variant="outline"
                                size="sm"
                                onClick={handleDelete}
                                className="rounded-xl text-red-400 hover:text-red-300 hover:bg-red-500/10 border-red-500/30"
                            >
                                <Trash2 className="w-4 h-4 mr-2" />
                                Ta bort
                            </Button>
                        </div>
                    </div>

                    {/* Overall Progress */}
                    <div className={cn(
                        "mt-6 p-4 rounded-xl",
                        "bg-zinc-800/50 border border-zinc-700/50"
                    )}>
                        <div className="flex items-center justify-between text-sm mb-2">
                            <span className="text-zinc-400">Total Progress</span>
                            <span className="font-bold text-amber-400">{overallProgress}%</span>
                        </div>
                        <div className="h-3 bg-zinc-700 rounded-full overflow-hidden">
                            <motion.div
                                className="h-full bg-gradient-to-r from-amber-500 to-orange-500"
                                initial={{ width: 0 }}
                                animate={{ width: `${overallProgress}%` }}
                                transition={{ duration: 1, ease: "easeOut" }}
                                style={{ boxShadow: "0 0 20px rgba(245, 158, 11, 0.5)" }}
                            />
                        </div>
                    </div>

                    {/* Continue button */}
                    {nextModule && (
                        <motion.div
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.3 }}
                            className="mt-6"
                        >
                            <Link prefetch={false} href={`/skillsmaps/${nextModule.slug}`}>
                                <Button
                                    className={cn(
                                        "rounded-xl",
                                        "bg-gradient-to-r from-amber-600 to-orange-600",
                                        "hover:from-amber-500 hover:to-orange-500"
                                    )}
                                >
                                    <Rocket className="w-4 h-4 mr-2" />
                                    Fortsätt med {nextModule.title}
                                    <ChevronRight className="w-4 h-4 ml-2" />
                                </Button>
                            </Link>
                        </motion.div>
                    )}
                </div>
            </motion.div>

            {/* Module Grid */}
            <Section spacing="none">
                <h2 className="text-xl font-bold text-white mb-6 flex items-center gap-2">
                    <Sparkles className="w-5 h-5 text-amber-400" />
                    Moduler i din ordning
                </h2>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {moduleProgress.map((item, index) => (
                        <CustomPathModuleCard
                            key={item.module.id}
                            module={item.module}
                            index={index}
                            progress={item.progress}
                            completedNodes={item.completedNodes}
                            totalNodes={item.totalNodes}
                        />
                    ))}
                </div>
            </Section>
        </PageLayout>
    )
}
