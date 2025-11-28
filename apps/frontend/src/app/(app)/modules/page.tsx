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
import { Button } from "@/components/ui/button"
import { ModuleCard, ModuleStatus } from "@/components/modules"
import { BookOpen, Trophy, RefreshCw, AlertCircle } from "lucide-react"

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
}

function Header({
    totalModules,
    completedModules,
    overallProgress,
    onRefresh,
    isRefreshing,
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
