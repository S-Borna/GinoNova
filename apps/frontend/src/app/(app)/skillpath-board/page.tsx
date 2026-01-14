/**
 * ============================================================================
 * SKILLPATH BOARD PAGE — Interactive Learning Path Visualization
 * ============================================================================
 *
 * Transformed into an interactive, game-like visualization of DevOps learning paths.
 * Features career path selection, skill tree visualization, and progress tracking.
 *
 * @phase SKILLPATH-VISUALIZATION-2.0
 */

"use client"

import { useState, useMemo } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { useRouter } from "next/navigation"
import {
    ArrowLeft,
    Trophy,
    TrendingUp,
    Target,
    Sparkles,
    Filter,
    LayoutGrid,
    Network,
    Loader2
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { useModules } from "@/hooks/useModules"
import { useAuth } from "@/components/auth/AuthProvider"
import { PathCard, SkillPathVisualization } from "@/components/skillpath"
import {
    LEARNING_PATHS,
    LearningPath,
    calculatePathProgress,
    getNextModule
} from "@/lib/learning-paths"

export const metadata = {
    title: "SkillPath Board | DevOpsHub",
    description: "Interactive DevOps learning path visualization"
}

/**
 * View modes
 */
type ViewMode = "paths" | "visualization"

/**
 * Cosmic Aurora Background
 */
function CosmicAurora() {
    return (
        <div className="fixed inset-0 pointer-events-none overflow-hidden">
            <div className="absolute inset-0 bg-[#05050a]" />

            <div
                className="absolute inset-0 opacity-[0.03]"
                style={{
                    backgroundImage: `
                        linear-gradient(rgba(139, 92, 246, 0.3) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(139, 92, 246, 0.3) 1px, transparent 1px)
                    `,
                    backgroundSize: '60px 60px'
                }}
            />

            <motion.div
                className="absolute -top-40 -right-40 w-[700px] h-[700px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(139, 92, 246, 0.12) 0%, rgba(139, 92, 246, 0.04) 40%, transparent 70%)',
                }}
                animate={{
                    scale: [1, 1.1, 1],
                    opacity: [0.5, 0.7, 0.5],
                }}
                transition={{ duration: 8, repeat: Infinity, ease: "easeInOut" }}
            />

            <motion.div
                className="absolute -bottom-60 -left-60 w-[600px] h-[600px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(34, 211, 238, 0.1) 0%, rgba(34, 211, 238, 0.03) 40%, transparent 70%)',
                }}
                animate={{
                    scale: [1, 1.15, 1],
                    opacity: [0.4, 0.6, 0.4],
                }}
                transition={{ duration: 10, repeat: Infinity, ease: "easeInOut", delay: 2 }}
            />

            <motion.div
                className="absolute top-1/3 left-1/4 w-[500px] h-[500px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(236, 72, 153, 0.06) 0%, transparent 60%)',
                }}
                animate={{
                    scale: [1, 1.2, 1],
                    opacity: [0.3, 0.5, 0.3],
                }}
                transition={{ duration: 12, repeat: Infinity, ease: "easeInOut", delay: 4 }}
            />
        </div>
    )
}

/**
 * Loading State
 */
function LoadingState() {
    return (
        <div className="min-h-screen bg-[#05050a] p-6 lg:p-8 flex items-center justify-center">
            <CosmicAurora />
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="text-center relative z-10"
            >
                <motion.div
                    animate={{
                        rotate: 360,
                        scale: [1, 1.1, 1]
                    }}
                    transition={{
                        rotate: { duration: 1, repeat: Infinity, ease: "linear" },
                        scale: { duration: 1.5, repeat: Infinity, ease: "easeInOut" }
                    }}
                >
                    <Loader2 className="w-12 h-12 text-purple-500 mx-auto mb-4" />
                </motion.div>
                <p className="text-neutral-400">Laddar learning paths...</p>
            </motion.div>
        </div>
    )
}

/**
 * Main SkillPath Board Page Component
 */
export default function SkillpathBoardPage() {
    const router = useRouter()
    const { user } = useAuth()
    const { data: modulesData, isLoading } = useModules()

    const [viewMode, setViewMode] = useState<ViewMode>("paths")
    const [selectedPath, setSelectedPath] = useState<LearningPath | null>(null)
    const [filterDifficulty, setFilterDifficulty] = useState<string>("all")
    const [filterDemand, setFilterDemand] = useState<number>(0)

    // Get user's first name
    const firstName = user?.full_name?.split(' ')[0] || user?.email?.split('@')[0] || 'DevOps Pro'

    // Mock completed modules (replace with real data from API)
    const completedModules: string[] = useMemo(() => {
        if (typeof window === "undefined") return []
        const stored = localStorage.getItem("devopshub_completed_modules")
        return stored ? JSON.parse(stored) : []
    }, [])

    // Calculate progress for each path
    const pathsWithProgress = useMemo(() => {
        return LEARNING_PATHS.map(path => ({
            ...path,
            progress: calculatePathProgress(path.id, completedModules),
            completedModules: path.modules.filter(m => completedModules.includes(m)).length,
            totalModules: path.modules.length,
            nextModule: getNextModule(path.id, completedModules)
        }))
    }, [completedModules])

    // Filter paths
    const filteredPaths = useMemo(() => {
        let filtered = pathsWithProgress

        // Difficulty filter
        if (filterDifficulty !== "all") {
            filtered = filtered.filter(path => {
                const avgDifficulty = path.modules.length > 0 ? "intermediate" : "beginner"
                return avgDifficulty === filterDifficulty
            })
        }

        // Job demand filter
        if (filterDemand > 0) {
            filtered = filtered.filter(path => path.jobDemand >= filterDemand)
        }

        return filtered
    }, [pathsWithProgress, filterDifficulty, filterDemand])

    // Recommended path (highest demand path not started)
    const recommendedPath = useMemo(() => {
        return pathsWithProgress
            .filter(p => p.progress === 0)
            .sort((a, b) => b.jobDemand - a.jobDemand)[0]
    }, [pathsWithProgress])

    // Stats
    const stats = useMemo(() => {
        const totalPaths = LEARNING_PATHS.length
        const startedPaths = pathsWithProgress.filter(p => p.progress > 0).length
        const completedPaths = pathsWithProgress.filter(p => p.progress === 100).length
        const totalModules = completedModules.length

        return {
            totalPaths,
            startedPaths,
            completedPaths,
            totalModules
        }
    }, [pathsWithProgress, completedModules])

    // Handle path selection
    const handlePathSelect = (path: LearningPath) => {
        setSelectedPath(path)
        setViewMode("visualization")
    }

    // Handle module click
    const handleModuleClick = (moduleSlug: string) => {
        router.push(`/skillsmaps/${moduleSlug}`)
    }

    // Handle back to paths
    const handleBackToPaths = () => {
        setViewMode("paths")
        setSelectedPath(null)
    }

    if (isLoading) {
        return <LoadingState />
    }

    return (
        <div className="min-h-screen bg-[#05050a] relative">
            <CosmicAurora />

            <div className="relative z-10 p-6 lg:p-8">
                {/* Header */}
                <motion.div
                    initial={{ opacity: 0, y: -20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className={cn(
                        "relative overflow-hidden rounded-2xl mb-8",
                        "bg-gradient-to-r from-[#0a0a0f] via-[#0a0a0f]/95 to-purple-950/20",
                        "border border-purple-500/30 p-8"
                    )}
                    style={{
                        boxShadow: '0 0 60px rgba(139, 92, 246, 0.15)'
                    }}
                >
                    {/* Background effects */}
                    <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/15 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/2" />
                    <div className="absolute bottom-0 left-1/4 w-64 h-64 bg-cyan-500/8 rounded-full blur-[80px]" />

                    <div className="relative">
                        {/* Back button (shown in visualization mode) */}
                        {viewMode === "visualization" && (
                            <Button
                                onClick={handleBackToPaths}
                                variant="ghost"
                                className="mb-4 text-purple-400 hover:text-purple-300"
                            >
                                <ArrowLeft className="w-4 h-4 mr-2" />
                                Tillbaka till banor
                            </Button>
                        )}

                        {/* Title */}
                        <div className="flex items-center justify-between">
                            <div>
                                <div className="flex items-center gap-2 mb-4">
                                    <motion.div
                                        animate={{
                                            scale: [1, 1.2, 1],
                                            opacity: [0.7, 1, 0.7]
                                        }}
                                        transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                                    >
                                        <Sparkles className="w-5 h-5 text-purple-400" />
                                    </motion.div>
                                    <span className="text-sm font-semibold text-purple-400 tracking-wide uppercase">
                                        {viewMode === "paths" ? "Välj Din Karriärväg" : selectedPath?.name}
                                    </span>
                                </div>

                                <h1 className="text-3xl lg:text-4xl font-bold mb-3">
                                    <span className="bg-gradient-to-r from-white via-purple-200 to-cyan-200 bg-clip-text text-transparent">
                                        {viewMode === "paths"
                                            ? `Välkommen, ${firstName}! 🚀`
                                            : "Interaktiv SkillPath"}
                                    </span>
                                </h1>

                                <p className="text-zinc-400 text-lg max-w-2xl">
                                    {viewMode === "paths"
                                        ? "Välj en karriärväg som passar dig och börja din resa mot ditt drömjobb inom DevOps."
                                        : "Utforska moduler, spåra dina framsteg och lås upp nya färdigheter."}
                                </p>
                            </div>

                            {/* View Toggle */}
                            {viewMode === "paths" && (
                                <div className="flex items-center gap-2 bg-neutral-900/50 border border-neutral-700 rounded-lg p-1">
                                    <Button
                                        onClick={() => setViewMode("paths")}
                                        size="sm"
                                        variant={viewMode === "paths" ? "default" : "ghost"}
                                        className="gap-2"
                                    >
                                        <LayoutGrid className="w-4 h-4" />
                                        Banor
                                    </Button>
                                </div>
                            )}
                        </div>

                        {/* Stats (shown in paths mode) */}
                        {viewMode === "paths" && (
                            <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
                                <div className="flex items-center gap-3 p-3 rounded-lg bg-neutral-900/50 border border-purple-500/30">
                                    <Trophy className="w-5 h-5 text-amber-400" />
                                    <div>
                                        <p className="text-xs text-gray-400">Banor klara</p>
                                        <p className="text-lg font-bold text-white">{stats.completedPaths}/{stats.totalPaths}</p>
                                    </div>
                                </div>
                                <div className="flex items-center gap-3 p-3 rounded-lg bg-neutral-900/50 border border-cyan-500/30">
                                    <Target className="w-5 h-5 text-cyan-400" />
                                    <div>
                                        <p className="text-xs text-gray-400">Banor påbörjade</p>
                                        <p className="text-lg font-bold text-white">{stats.startedPaths}</p>
                                    </div>
                                </div>
                                <div className="flex items-center gap-3 p-3 rounded-lg bg-neutral-900/50 border border-green-500/30">
                                    <TrendingUp className="w-5 h-5 text-green-400" />
                                    <div>
                                        <p className="text-xs text-gray-400">Moduler klara</p>
                                        <p className="text-lg font-bold text-white">{stats.totalModules}</p>
                                    </div>
                                </div>
                                <div className="flex items-center gap-3 p-3 rounded-lg bg-neutral-900/50 border border-pink-500/30">
                                    <Sparkles className="w-5 h-5 text-pink-400" />
                                    <div>
                                        <p className="text-xs text-gray-400">Rekommenderad</p>
                                        <p className="text-sm font-bold text-white truncate">
                                            {recommendedPath?.icon} {recommendedPath?.name.split(' ')[0]}
                                        </p>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                </motion.div>

                {/* Content */}
                <AnimatePresence mode="wait">
                    {viewMode === "paths" ? (
                        <motion.div
                            key="paths"
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0, y: -20 }}
                            transition={{ duration: 0.3 }}
                        >
                            {/* Filters */}
                            <div className="flex items-center gap-4 mb-6">
                                <div className="flex items-center gap-2">
                                    <Filter className="w-4 h-4 text-gray-400" />
                                    <span className="text-sm text-gray-400">Filter:</span>
                                </div>
                                <select
                                    value={filterDemand}
                                    onChange={(e) => setFilterDemand(Number(e.target.value))}
                                    className="px-3 py-1.5 text-sm rounded-lg bg-neutral-900 border border-neutral-700 text-white"
                                >
                                    <option value="0">Alla efterfrågan</option>
                                    <option value="80">Hög efterfrågan (80%+)</option>
                                    <option value="90">Mycket hög (90%+)</option>
                                </select>
                            </div>

                            {/* Recommended Path (if not started) */}
                            {recommendedPath && recommendedPath.progress === 0 && (
                                <motion.div
                                    initial={{ opacity: 0, y: 20 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    className="mb-8"
                                >
                                    <div className="flex items-center gap-2 mb-4">
                                        <Sparkles className="w-5 h-5 text-amber-400" />
                                        <h2 className="text-xl font-bold text-white">Rekommenderad för dig</h2>
                                    </div>
                                    <PathCard
                                        path={recommendedPath}
                                        progress={recommendedPath.progress}
                                        completedModules={recommendedPath.completedModules}
                                        totalModules={recommendedPath.totalModules}
                                        onStart={() => handlePathSelect(recommendedPath)}
                                    />
                                </motion.div>
                            )}

                            {/* All Paths Grid */}
                            <div>
                                <h2 className="text-xl font-bold text-white mb-4">Alla karriärvägar</h2>
                                <div className="grid lg:grid-cols-2 gap-6">
                                    {filteredPaths.map((path, index) => (
                                        <motion.div
                                            key={path.id}
                                            initial={{ opacity: 0, y: 20 }}
                                            animate={{ opacity: 1, y: 0 }}
                                            transition={{ delay: index * 0.1 }}
                                        >
                                            <PathCard
                                                path={path}
                                                progress={path.progress}
                                                completedModules={path.completedModules}
                                                totalModules={path.totalModules}
                                                onStart={() => handlePathSelect(path)}
                                            />
                                        </motion.div>
                                    ))}
                                </div>
                            </div>
                        </motion.div>
                    ) : (
                        <motion.div
                            key="visualization"
                            initial={{ opacity: 0, scale: 0.95 }}
                            animate={{ opacity: 1, scale: 1 }}
                            exit={{ opacity: 0, scale: 0.95 }}
                            transition={{ duration: 0.3 }}
                            className="h-[calc(100vh-20rem)]"
                        >
                            {selectedPath && modulesData && (
                                <SkillPathVisualization
                                    path={selectedPath}
                                    modules={modulesData}
                                    completedModules={completedModules}
                                    onModuleClick={handleModuleClick}
                                />
                            )}
                        </motion.div>
                    )}
                </AnimatePresence>
            </div>
        </div>
    )
}
