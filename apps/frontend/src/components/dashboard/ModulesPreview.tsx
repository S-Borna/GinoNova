"use client"

/**
 * ModulesPreview Component
 * Phase 6.2: Module list with progress indicators
 */

import Link from "next/link"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import type { DashboardModule, DashboardProgress } from "@/lib/dashboard"

// ============================================================================
// TYPES
// ============================================================================

interface ModuleWithProgress extends DashboardModule {
    progress?: number
    status?: string
}

interface ModulesPreviewProps {
    modules: DashboardModule[]
    progress?: DashboardProgress[]
    maxDisplay?: number
}

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

function getModuleProgress(
    moduleId: string,
    progressList: DashboardProgress[]
): { progress: number; status: string } {
    const moduleProgress = progressList.find(p => p.module_id === moduleId)
    return {
        progress: moduleProgress?.progress ?? 0,
        status: moduleProgress?.status ?? "not_started"
    }
}

function getProgressColor(progress: number): string {
    if (progress >= 100) return "bg-emerald-500"
    if (progress >= 50) return "bg-blue-500"
    if (progress > 0) return "bg-amber-500"
    return "bg-gray-200"
}

function getStatusBadge(status: string, progress: number): { label: string; className: string } {
    if (progress >= 100 || status === "completed") {
        return { label: "Completed", className: "bg-emerald-100 text-emerald-700 border-emerald-200" }
    }
    if (progress > 0 || status === "in_progress") {
        return { label: "In Progress", className: "bg-blue-100 text-blue-700 border-blue-200" }
    }
    return { label: "Not Started", className: "bg-gray-100 text-gray-600 border-gray-200" }
}

// ============================================================================
// COMPONENT
// ============================================================================

export function ModulesPreview({
    modules,
    progress = [],
    maxDisplay = 5,
}: ModulesPreviewProps) {
    const displayModules = modules.slice(0, maxDisplay)
    const hasMore = modules.length > maxDisplay

    return (
        <Card className="rounded-xl border-0 shadow-md bg-white dark:bg-neutral-900/80">
            <CardHeader className="pb-2 flex flex-row items-center justify-between">
                <CardTitle className="text-base font-semibold text-gray-900 dark:text-white flex items-center gap-2">
                    <span className="text-lg">📚</span>
                    Learning Modules
                </CardTitle>
                <Badge variant="secondary" className="text-xs font-medium">
                    {modules.length} total
                </Badge>
            </CardHeader>
            <CardContent>
                {modules.length === 0 ? (
                    <div className="text-center py-8">
                        <div className="w-12 h-12 mx-auto mb-3 rounded-full bg-gray-100 dark:bg-white/10 flex items-center justify-center">
                            <span className="text-xl">📚</span>
                        </div>
                        <p className="text-sm font-medium text-gray-900 dark:text-white mb-1">No modules available</p>
                        <p className="text-xs text-gray-500 dark:text-zinc-400 mb-4">Modules will appear here once created.</p>
                        <Link prefetch={false} href="/modules/new">
                            <Button variant="outline" size="sm" className="text-xs">
                                Create Module
                            </Button>
                        </Link>
                    </div>
                ) : (
                    <div className="space-y-3">
                        {displayModules.map((module) => {
                            const { progress: moduleProgress, status } = getModuleProgress(module.id, progress)
                            const statusBadge = getStatusBadge(status, moduleProgress)

                            return (
                                <div
                                    key={module.id}
                                    className="group p-3 rounded-xl border border-gray-100 dark:border-white/10 bg-gray-50/50 dark:bg-white/5 hover:bg-white dark:hover:bg-white/10 hover:shadow-sm hover:border-gray-200 dark:hover:border-white/20 transition-all duration-200"
                                >
                                    <div className="flex items-start justify-between gap-3">
                                        {/* Module Info */}
                                        <div className="flex-1 min-w-0">
                                            <div className="flex items-center gap-2 mb-1">
                                                <h4 className="text-sm font-semibold text-gray-900 dark:text-white truncate">
                                                    {module.name}
                                                </h4>
                                                <Badge
                                                    variant="outline"
                                                    className={`text-[10px] px-2 py-0 border ${statusBadge.className}`}
                                                >
                                                    {statusBadge.label}
                                                </Badge>
                                            </div>
                                            {module.description && (
                                                <p className="text-xs text-gray-500 dark:text-zinc-400 line-clamp-1 mb-2">
                                                    {module.description}
                                                </p>
                                            )}

                                            {/* Progress Bar */}
                                            <div className="flex items-center gap-2">
                                                <div className="flex-1 h-1.5 bg-gray-200 dark:bg-white/10 rounded-full overflow-hidden">
                                                    <div
                                                        className={`h-full rounded-full transition-all duration-500 ${getProgressColor(moduleProgress)}`}
                                                        style={{ width: `${moduleProgress}%` }}
                                                    />
                                                </div>
                                                <span className="text-[10px] font-medium text-gray-500 dark:text-zinc-400 w-8 text-right">
                                                    {moduleProgress}%
                                                </span>
                                            </div>
                                        </div>

                                        {/* Continue Button */}
                                        <Link prefetch={false} href={`/modules/${module.id}`}>
                                            <Button
                                                variant="ghost"
                                                size="sm"
                                                className="h-8 px-3 text-xs font-medium text-indigo-600 dark:text-indigo-400 hover:text-indigo-700 dark:hover:text-indigo-300 hover:bg-indigo-50 dark:hover:bg-indigo-500/10 opacity-0 group-hover:opacity-100 transition-opacity"
                                            >
                                                {moduleProgress > 0 ? "Continue" : "Start"}
                                                <span className="ml-1">→</span>
                                            </Button>
                                        </Link>
                                    </div>
                                </div>
                            )
                        })}

                        {/* View All Link */}
                        {hasMore && (
                            <Link
                                href="/modules"
                                className="flex items-center justify-center gap-1 py-2 text-xs font-medium text-indigo-600 hover:text-indigo-700 transition-colors"
                            >
                                View all {modules.length} modules
                                <span>→</span>
                            </Link>
                        )}
                    </div>
                )}
            </CardContent>
        </Card>
    )
}
