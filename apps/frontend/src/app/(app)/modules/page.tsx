"use client"

/**
 * ============================================================================
 * MODULES LIST PAGE — Apple-Inspired Design (D.4)
 * ============================================================================
 *
 * Beautiful module browsing experience with:
 * - Header with overall progress
 * - Responsive grid layout
 * - Staggered card animations
 * - Loading skeletons
 *
 * @phase A.3 - App Shell & Routing
 * @design D.4 - Modules UI
 */

import { useState, useEffect } from "react"
import Link from "next/link"
import { getModules, ModulePublic } from "@/lib/modules"
import { useAuth } from "@/components/auth"
import { cn } from "@/lib/utils"
import { GlassCard } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import { ProgressBar } from "@/components/ui/progress-bar"
import { ModuleCard, ModuleStatus } from "@/components/modules"
import { BookOpen, Trophy, RefreshCw, AlertCircle, Rocket } from "lucide-react"

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
        <div
            className={cn(
                "rounded-2xl p-6 animate-pulse",
                "bg-white dark:bg-neutral-800/50",
                "border border-neutral-200/50 dark:border-neutral-700/50"
            )}
        >
            {/* Top row */}
            <div className="flex items-center justify-between mb-4">
                <div className="w-10 h-10 rounded-xl bg-neutral-200 dark:bg-neutral-700" />
                <div className="w-20 h-6 rounded-full bg-neutral-200 dark:bg-neutral-700" />
            </div>
            {/* Icon */}
            <div className="w-12 h-12 mb-3 rounded-lg bg-neutral-200 dark:bg-neutral-700" />
            {/* Title */}
            <div className="h-6 w-3/4 mb-2 rounded bg-neutral-200 dark:bg-neutral-700" />
            {/* Description */}
            <div className="space-y-2 mb-4">
                <div className="h-4 w-full rounded bg-neutral-200 dark:bg-neutral-700" />
                <div className="h-4 w-2/3 rounded bg-neutral-200 dark:bg-neutral-700" />
            </div>
            {/* Progress */}
            <div className="h-2 w-full mb-2 rounded bg-neutral-200 dark:bg-neutral-700" />
            <div className="flex justify-between mb-4">
                <div className="h-4 w-20 rounded bg-neutral-200 dark:bg-neutral-700" />
                <div className="h-4 w-10 rounded bg-neutral-200 dark:bg-neutral-700" />
            </div>
            {/* Button */}
            <div className="h-10 w-full rounded-xl bg-neutral-200 dark:bg-neutral-700" />
        </div>
    )
}

function PageSkeleton() {
    return (
        <div className="space-y-8 animate-fade-in">
            {/* Header skeleton */}
            <div className="rounded-2xl p-6 bg-white dark:bg-neutral-800/50">
                <div className="h-8 w-48 mb-2 rounded bg-neutral-200 dark:bg-neutral-700" />
                <div className="h-4 w-64 mb-4 rounded bg-neutral-200 dark:bg-neutral-700" />
                <div className="h-3 w-full rounded bg-neutral-200 dark:bg-neutral-700" />
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
        <GlassCard
            variant="default"
            padding="xl"
            radius="xl"
            className="max-w-md mx-auto text-center animate-fade-in"
        >
            <div
                className={cn(
                    "w-16 h-16 rounded-full mx-auto mb-4",
                    "bg-red-100 dark:bg-red-900/30",
                    "flex items-center justify-center"
                )}
            >
                <AlertCircle className="w-8 h-8 text-red-500" />
            </div>
            <h2 className="text-xl font-semibold text-neutral-900 dark:text-white mb-2">
                Unable to Load Modules
            </h2>
            <p className="text-neutral-600 dark:text-neutral-400 mb-6">{error}</p>
            <Button onClick={onRetry} className="rounded-xl">
                <RefreshCw className="w-4 h-4 mr-2" />
                Try Again
            </Button>
        </GlassCard>
    )
}

/* ============================================================================
   EMPTY STATE
   ============================================================================ */

function EmptyState() {
    return (
        <GlassCard
            variant="default"
            padding="xl"
            radius="xl"
            className="max-w-md mx-auto text-center animate-fade-in"
        >
            <div
                className={cn(
                    "w-16 h-16 rounded-full mx-auto mb-4",
                    "bg-primary-100 dark:bg-primary-900/30",
                    "flex items-center justify-center"
                )}
            >
                <BookOpen className="w-8 h-8 text-primary-500" />
            </div>
            <h2 className="text-xl font-semibold text-neutral-900 dark:text-white mb-2">
                No Modules Yet
            </h2>
            <p className="text-neutral-600 dark:text-neutral-400 mb-6">
                Modules will appear here once they&apos;re added to your learning path.
            </p>
            <Link href="/modules/new">
                <Button className="rounded-xl">Create First Module</Button>
            </Link>
        </GlassCard>
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
}

function Header({
    totalModules,
    completedModules,
    overallProgress,
    onRefresh,
    isRefreshing,
}: HeaderProps) {
    return (
        <GlassCard variant="default" padding="lg" radius="xl" className="animate-fade-in">
            <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                <div>
                    <div className="flex items-center gap-3 mb-2">
                        <div
                            className={cn(
                                "w-10 h-10 rounded-xl flex items-center justify-center",
                                "bg-gradient-to-br from-primary-500 to-primary-600",
                                "shadow-lg shadow-primary-500/25"
                            )}
                        >
                            <Rocket className="w-5 h-5 text-white" />
                        </div>
                        <h1 className="text-2xl font-bold text-neutral-900 dark:text-white">
                            Your Learning Path
                        </h1>
                    </div>
                    <p className="text-neutral-600 dark:text-neutral-400">
                        {overallProgress === 100
                            ? "Congratulations! You've completed all modules! 🎉"
                            : `Keep going! ${completedModules} of ${totalModules} modules complete.`}
                    </p>
                </div>

                <div className="flex items-center gap-3">
                    {/* Trophy badge */}
                    <div
                        className={cn(
                            "flex items-center gap-2 px-4 py-2 rounded-xl",
                            "bg-warning-100 dark:bg-warning-900/30"
                        )}
                    >
                        <Trophy className="w-5 h-5 text-warning-500" />
                        <span className="font-semibold text-warning-700 dark:text-warning-400">
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

            {/* Progress bar */}
            <div className="mt-4">
                <div className="flex items-center justify-between text-sm mb-2">
                    <span className="text-neutral-600 dark:text-neutral-400">Overall Progress</span>
                    <span
                        className={cn(
                            "font-semibold",
                            overallProgress === 100 ? "text-success-500" : "text-primary-500"
                        )}
                    >
                        {overallProgress}%
                    </span>
                </div>
                <ProgressBar value={overallProgress} className="h-3" />
            </div>
        </GlassCard>
    )
}

/* ============================================================================
   MODULES PAGE
   ============================================================================ */

export default function ModulesPage() {
    useAuth()
    const [modules, setModules] = useState<EnhancedModule[]>([])
    const [loading, setLoading] = useState(true)
    const [refreshing, setRefreshing] = useState(false)
    const [error, setError] = useState<string | null>(null)

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
                // Transform modules to enhanced format with mock progress data
                const enhanced: EnhancedModule[] = result.data.map((mod, index) => ({
                    ...mod,
                    orderIndex: index + 1,
                    icon: getModuleIcon(mod.name),
                    // Mock progress data (would come from backend in real app)
                    progress: index === 0 ? 100 : index === 1 ? 65 : index === 2 ? 30 : 0,
                    tasksCompleted: index === 0 ? 8 : index === 1 ? 5 : index === 2 ? 2 : 0,
                    totalTasks: 8,
                    status:
                        index === 0
                            ? "complete"
                            : index === 1
                                ? "in_progress"
                                : index === 2
                                    ? "not_started"
                                    : index > 3
                                        ? "locked"
                                        : "not_started",
                    estimatedHours: 4 + index * 2,
                    prerequisiteModule: index > 3 ? result.data[index - 1]?.name : undefined,
                }))
                setModules(enhanced)
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
    }, [])

    const handleRefresh = () => {
        fetchModules(true)
    }

    // Calculate stats
    const totalModules = modules.length
    const completedModules = modules.filter((m) => m.status === "complete").length
    const overallProgress =
        totalModules > 0 ? Math.round((completedModules / totalModules) * 100) : 0

    if (loading) {
        return (
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                <PageSkeleton />
            </div>
        )
    }

    if (error) {
        return (
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                <ErrorState error={error} onRetry={handleRefresh} />
            </div>
        )
    }

    if (modules.length === 0) {
        return (
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                <EmptyState />
            </div>
        )
    }

    return (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div className="space-y-8">
                {/* Header */}
                <Header
                    totalModules={totalModules}
                    completedModules={completedModules}
                    overallProgress={overallProgress}
                    onRefresh={handleRefresh}
                    isRefreshing={refreshing}
                />

                {/* Modules grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {modules.map((module, index) => (
                        <div
                            key={module.id}
                            className="animate-fade-in-up"
                            style={{ animationDelay: `${index * 100}ms` }}
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
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}
