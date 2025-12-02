"use client"

/**
 * ============================================================================
 * MODULES LIST PAGE — Design System v2.0 + Platform Selection
 * ============================================================================
 *
 * Updated with @saas/ui design system components:
 * - PageLayout for consistent layout
 * - Headline for typography
 * - Section/Block for content organization
 * - PlatformSelector for OS/distro selection with wave animation
 *
 * @phase DS.2 - Design System Application Layer
 * @phase FAS-3.1 - OS-Adaptive Content System
 */

import { useState, useEffect } from "react"
import Link from "next/link"
import { motion, AnimatePresence } from "framer-motion"
import { getModules, ModulePublic } from "@/lib/modules"
import { getTasksForModule, TaskPublic } from "@/lib/tasks"
import { getUserProgress, ProgressPublic } from "@/lib/progress"
import { useAuth } from "@/components/auth"
import { usePlatform, LINUX_DISTROS } from "@/hooks/useOperatingSystem"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { ModuleCard, ModuleStatus } from "@/components/modules"
import { PlatformSelector, PlatformBadge } from "@/components/onboarding"
import { BookOpen, Trophy, RefreshCw, AlertCircle, Settings2 } from "lucide-react"

// @saas/ui Design System
import { PageLayout, Section, Block, Headline, Subtext } from "@saas/ui"

/* ============================================================================
   TYPES
   ============================================================================ */

interface EnhancedModule extends ModulePublic {
    orderIndex: number
    icon: string
    progress: number
    tasksCompleted: number
    totalTasks: number
    status: ModuleStatus
    estimatedHours: number
    prerequisiteModule?: string
}

/* ============================================================================
   MODULE ICONS (emoji mapping)
   ============================================================================ */

const moduleIcons: Record<string, string> = {
    onboarding: "🚀",
    foundations: "📚",
    linux: "🐧",
    shell: "💻",
    git: "🔀",
    networking: "🌐",
    cloud: "☁️",
    aws: "☁️",
    iac: "🏗️",
    terraform: "🏗️",
    containers: "📦",
    docker: "🐳",
    kubernetes: "⚙️",
    k8s: "⚙️",
    default: "📖",
}

function getModuleIcon(name: string): string {
    const lower = name.toLowerCase()
    for (const [key, icon] of Object.entries(moduleIcons)) {
        if (lower.includes(key)) {
            return icon
        }
    }
    return moduleIcons.default
}

/* ============================================================================
   SKELETON COMPONENTS
   ============================================================================ */

function ModuleCardSkeleton() {
    return (
        <div className="bg-white dark:bg-neutral-800 rounded-xl shadow-sm border border-gray-100 dark:border-neutral-700 p-6 animate-pulse">
            {/* Top row */}
            <div className="flex items-start justify-between mb-4">
                <div className="flex items-center gap-3">
                    <div className="w-8 h-8 rounded-lg bg-gray-200 dark:bg-neutral-700" />
                    <div>
                        <div className="h-5 w-32 rounded bg-gray-200 dark:bg-neutral-700 mb-1" />
                        <div className="h-4 w-20 rounded bg-gray-200 dark:bg-neutral-700" />
                    </div>
                </div>
                <div className="w-20 h-6 rounded-full bg-gray-200 dark:bg-neutral-700" />
            </div>
            {/* Description */}
            <div className="space-y-2 mb-4">
                <div className="h-4 w-full rounded bg-gray-200 dark:bg-neutral-700" />
                <div className="h-4 w-2/3 rounded bg-gray-200 dark:bg-neutral-700" />
            </div>
            {/* Progress */}
            <div className="h-2 w-full mb-2 rounded bg-gray-200 dark:bg-neutral-700" />
            <div className="flex justify-between mb-4">
                <div className="h-4 w-12 rounded bg-gray-200 dark:bg-neutral-700" />
                <div className="h-4 w-8 rounded bg-gray-200 dark:bg-neutral-700" />
            </div>
            {/* Button */}
            <div className="h-10 w-full rounded-xl bg-gray-200 dark:bg-neutral-700" />
        </div>
    )
}

function PageSkeleton() {
    return (
        <div className="space-y-8">
            {/* Header skeleton */}
            <div className="mb-8">
                <div className="h-8 w-48 rounded bg-gray-200 dark:bg-neutral-700 mb-2" />
                <div className="h-5 w-32 rounded bg-gray-200 dark:bg-neutral-700 mb-6" />
                <div className="bg-white dark:bg-neutral-800 rounded-xl shadow-sm border border-gray-100 dark:border-neutral-700 p-6">
                    <div className="h-4 w-full mb-3 rounded bg-gray-200 dark:bg-neutral-700" />
                    <div className="h-3 w-full rounded bg-gray-200 dark:bg-neutral-700" />
                </div>
            </div>
            {/* Grid skeleton */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {Array.from({ length: 6 }).map((_, i) => (
                    <ModuleCardSkeleton key={i} />
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
        <div className="bg-white dark:bg-neutral-800 rounded-xl shadow-sm border border-gray-100 dark:border-neutral-700 p-8 max-w-md mx-auto text-center">
            <div className="w-16 h-16 rounded-full mx-auto mb-4 bg-red-100 dark:bg-red-900/30 flex items-center justify-center">
                <AlertCircle className="w-8 h-8 text-red-500" />
            </div>
            <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                Unable to Load Modules
            </h2>
            <p className="text-gray-600 dark:text-neutral-400 mb-6">{error}</p>
            <Button onClick={onRetry} className="rounded-xl">
                <RefreshCw className="w-4 h-4 mr-2" />
                Try Again
            </Button>
        </div>
    )
}

/* ============================================================================
   EMPTY STATE
   ============================================================================ */

function EmptyState() {
    return (
        <div className="bg-white dark:bg-neutral-800 rounded-xl shadow-sm border border-gray-100 dark:border-neutral-700 p-8 max-w-md mx-auto text-center">
            <div className="w-16 h-16 rounded-full mx-auto mb-4 bg-indigo-100 dark:bg-indigo-900/30 flex items-center justify-center">
                <BookOpen className="w-8 h-8 text-indigo-500" />
            </div>
            <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                No Modules Yet
            </h2>
            <p className="text-gray-600 dark:text-neutral-400 mb-6">
                Modules will appear here once they&apos;re added to your learning path.
            </p>
            <Link href="/modules/new">
                <Button className="rounded-xl">Create First Module</Button>
            </Link>
        </div>
    )
}

/* ============================================================================
   HEADER COMPONENT
   ============================================================================ */

interface HeaderProps {
    totalModules: number
    completedModules: number
    overallProgress: number
    onRefresh: () => void
    isRefreshing: boolean
    onChangePlatform?: () => void
}

function Header({
    totalModules,
    completedModules,
    overallProgress,
    onRefresh,
    isRefreshing,
    onChangePlatform,
}: HeaderProps) {
    return (
        <div className="mb-8">
            <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mb-6">
                <div>
                    <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
                        Learning Path
                    </h1>
                    <p className="text-gray-500 dark:text-neutral-400 mt-2">
                        {totalModules} modules • {completedModules} completed
                    </p>
                </div>

                <div className="flex items-center gap-3">
                    {/* Platform Badge */}
                    <PlatformBadge />

                    {/* Trophy badge */}
                    <div className="flex items-center gap-2 px-4 py-2 bg-amber-100 dark:bg-amber-900/30 rounded-xl">
                        <Trophy className="w-5 h-5 text-amber-600 dark:text-amber-400" />
                        <span className="font-semibold text-amber-700 dark:text-amber-400">
                            {completedModules}/{totalModules}
                        </span>
                    </div>

                    {/* Refresh button */}
                    <Button
                        variant="ghost"
                        size="sm"
                        onClick={onRefresh}
                        disabled={isRefreshing}
                        className="rounded-xl"
                    >
                        <RefreshCw className={cn("w-4 h-4", isRefreshing && "animate-spin")} />
                    </Button>
                </div>
            </div>

            {/* Overall progress card */}
            <div className="bg-white dark:bg-neutral-800 rounded-xl shadow-sm border border-gray-100 dark:border-neutral-700 p-6">
                <div className="flex items-center justify-between text-sm mb-3">
                    <span className="text-gray-600 dark:text-neutral-400">Overall Progress</span>
                    <span className={cn(
                        "font-semibold",
                        overallProgress === 100 ? "text-emerald-600" : "text-indigo-600"
                    )}>
                        {overallProgress}%
                    </span>
                </div>
                <div className="w-full bg-gray-200 dark:bg-neutral-700 rounded-full h-3">
                    <div
                        className={cn(
                            "h-3 rounded-full transition-all duration-500",
                            overallProgress === 100
                                ? "bg-gradient-to-r from-emerald-500 to-teal-500"
                                : "bg-gradient-to-r from-indigo-500 to-purple-600"
                        )}
                        style={{ width: `${overallProgress}%` }}
                    />
                </div>
                <p className="text-sm text-gray-500 dark:text-neutral-400 mt-3">
                    {overallProgress === 100
                        ? "🎉 Congratulations! You've completed all modules!"
                        : `Keep going! ${totalModules - completedModules} modules remaining.`}
                </p>
            </div>
        </div>
    )
}

/* ============================================================================
   MODULES PAGE
   ============================================================================ */

export default function ModulesPage() {
    const { user } = useAuth()
    const { hasSelected, isLoading: platformLoading, os, distro } = usePlatform()
    const [modules, setModules] = useState<EnhancedModule[]>([])
    const [loading, setLoading] = useState(true)
    const [refreshing, setRefreshing] = useState(false)
    const [error, setError] = useState<string | null>(null)
    const [showModules, setShowModules] = useState(false)

    const fetchModules = async (isRefresh = false) => {
        if (isRefresh) {
            setRefreshing(true)
        } else {
            setLoading(true)
        }
        setError(null)

        try {
            const result = await getModules()
            if (result.ok) {
                // Fetch user progress if logged in
                let userProgress: ProgressPublic[] = []
                if (user?.id) {
                    const progressResult = await getUserProgress(user.id)
                    if (progressResult.ok) {
                        userProgress = progressResult.data
                    }
                }

                // Create a map of module_id -> progress
                const progressMap = new Map<string, ProgressPublic>()
                userProgress.forEach(p => {
                    if (p.module_id) {
                        progressMap.set(p.module_id, p)
                    }
                })

                // Create a map of task progress by task_id
                const taskProgressMap = new Map<string, ProgressPublic>()
                userProgress.forEach(p => {
                    if (p.task_id) {
                        taskProgressMap.set(p.task_id, p)
                    }
                })

                // Fetch tasks for each module to get accurate counts
                const modulesWithTasks = await Promise.all(
                    result.data.map(async (mod, index) => {
                        // Get tasks for this module
                        const tasksResult = await getTasksForModule(mod.id)
                        const tasks: TaskPublic[] = tasksResult.ok ? tasksResult.data : []
                        const totalTasks = tasks.length

                        // Count completed tasks from progress data
                        const completedTasks = tasks.filter(t => {
                            const taskProgress = taskProgressMap.get(t.id)
                            return taskProgress?.status === "completed"
                        }).length

                        // Calculate progress percentage
                        const progressPercent = totalTasks > 0
                            ? Math.round((completedTasks / totalTasks) * 100)
                            : 0

                        // Determine status - NO LOCKING, all modules open!
                        let status: ModuleStatus = "not_started"
                        if (progressPercent === 100) {
                            status = "complete"
                        } else if (progressPercent > 0) {
                            status = "in_progress"
                        }
                        // All modules are accessible - no prerequisites blocking

                        return {
                            ...mod,
                            orderIndex: mod.order_index || index + 1,
                            icon: getModuleIcon(mod.name),
                            progress: progressPercent,
                            tasksCompleted: completedTasks,
                            totalTasks,
                            status,
                            estimatedHours: mod.estimated_hours || 4 + index * 2,
                            prerequisiteModule: mod.prerequisites?.[0],
                        } as EnhancedModule
                    })
                )

                setModules(modulesWithTasks)
            } else {
                setError(result.message)
            }
        } catch {
            setError("Failed to load modules. Please try again.")
        } finally {
            setLoading(false)
            setRefreshing(false)
        }
    }

    useEffect(() => {
        fetchModules()
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [user?.id])

    const handleRefresh = () => {
        fetchModules(true)
    }

    // Calculate stats
    const totalModules = modules.length
    const completedModules = modules.filter((m) => m.status === "complete").length
    const overallProgress =
        totalModules > 0 ? Math.round((completedModules / totalModules) * 100) : 0

    // Handle platform selection complete - trigger wave animation
    const handlePlatformComplete = () => {
        setShowModules(true)
    }

    // Show modules immediately if platform already selected
    useEffect(() => {
        if (hasSelected && !platformLoading) {
            setShowModules(true)
        }
    }, [hasSelected, platformLoading])

    // Platform selection loading
    if (platformLoading) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <PageSkeleton />
            </PageLayout>
        )
    }

    // Show platform selector if not yet selected
    // TEMP: Force show for testing - change back to: if (!hasSelected)
    if (true) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <div className="min-h-[70vh] flex items-center justify-center py-12">
                    <PlatformSelector onComplete={handlePlatformComplete} />
                </div>
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
                <ErrorState error={error ?? "Ett fel uppstod"} onRetry={handleRefresh} />
            </PageLayout>
        )
    }

    if (modules.length === 0) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <EmptyState />
            </PageLayout>
        )
    }

    return (
        <PageLayout maxWidth="wide" background="gray">
            <AnimatePresence>
                {showModules && (
                    <motion.div
                        className="space-y-8"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ duration: 0.3 }}
                    >
                        {/* Header */}
                        <Section spacing="none">
                            <motion.div
                                initial={{ opacity: 0, y: -20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.1, duration: 0.4 }}
                            >
                                <Header
                                    totalModules={totalModules}
                                    completedModules={completedModules}
                                    overallProgress={overallProgress}
                                    onRefresh={handleRefresh}
                                    isRefreshing={refreshing}
                                />
                            </motion.div>
                        </Section>

                        {/* Modules grid with wave animation */}
                        <Section spacing="none">
                            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                                {modules.map((module, index) => (
                                    <motion.div
                                        key={module.id}
                                        initial={{ opacity: 0, y: 50, scale: 0.9 }}
                                        animate={{ opacity: 1, y: 0, scale: 1 }}
                                        transition={{
                                            type: "spring",
                                            stiffness: 100,
                                            damping: 15,
                                            delay: 0.2 + index * 0.08, // Wave effect
                                        }}
                                    >
                                        <ModuleCard
                                            id={module.id}
                                            orderIndex={module.orderIndex}
                                            title={module.name}
                                            description={module.description || "No description available"}
                                            icon={module.icon}
                                            progress={module.progress}
                                            tasksCompleted={module.tasksCompleted}
                                            totalTasks={module.totalTasks}
                                            status={module.status}
                                            estimatedHours={module.estimatedHours}
                                            prerequisiteModule={module.prerequisiteModule}
                                        />
                                    </motion.div>
                                ))}
                            </div>
                        </Section>
                    </motion.div>
                )}
            </AnimatePresence>
        </PageLayout>
    )
}
