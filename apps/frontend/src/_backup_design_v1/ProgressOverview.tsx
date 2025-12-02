"use client"

/**
 * ProgressOverview Component
 * Phase 6.2: Bootcamp progress visualization
 */

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { ProgressBar } from "@/components/ui/progress-bar"
import type { DashboardStats } from "@/lib/dashboard"

// ============================================================================
// TYPES
// ============================================================================

interface ProgressOverviewProps {
    stats: DashboardStats
    completedModules?: number
    completedTasks?: number
}

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

function getProgressColor(percentage: number): string {
    if (percentage >= 80) return "bg-emerald-500"
    if (percentage >= 50) return "bg-blue-500"
    if (percentage >= 25) return "bg-amber-500"
    return "bg-gray-400"
}

function getProgressLabel(percentage: number): string {
    if (percentage >= 100) return "Complete! 🎉"
    if (percentage >= 80) return "Almost there!"
    if (percentage >= 50) return "Great progress!"
    if (percentage >= 25) return "Keep going!"
    return "Just started"
}

// ============================================================================
// COMPONENT
// ============================================================================

export function ProgressOverview({
    stats,
    completedModules = 0,
    completedTasks = 0,
}: ProgressOverviewProps) {
    const moduleProgress = stats.total_modules > 0
        ? Math.round((completedModules / stats.total_modules) * 100)
        : 0

    const taskProgress = stats.total_tasks > 0
        ? Math.round((completedTasks / stats.total_tasks) * 100)
        : 0

    const overallProgress = Math.round((moduleProgress + taskProgress) / 2)

    return (
        <Card className="rounded-xl border-0 shadow-md bg-white">
            <CardHeader className="pb-2">
                <CardTitle className="text-base font-semibold text-gray-900 flex items-center gap-2">
                    <span className="text-lg">📊</span>
                    Bootcamp Progress
                </CardTitle>
            </CardHeader>
            <CardContent className="space-y-5">
                {/* Overall Progress Circle */}
                <div className="flex items-center justify-center py-4">
                    <div className="relative w-28 h-28">
                        {/* Background circle */}
                        <svg className="w-full h-full -rotate-90" viewBox="0 0 36 36">
                            <path
                                d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                                fill="none"
                                stroke="#e5e7eb"
                                strokeWidth="3"
                            />
                            <path
                                d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                                fill="none"
                                stroke="url(#progressGradient)"
                                strokeWidth="3"
                                strokeDasharray={`${overallProgress}, 100`}
                                strokeLinecap="round"
                            />
                            <defs>
                                <linearGradient id="progressGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                                    <stop offset="0%" stopColor="#6366f1" />
                                    <stop offset="100%" stopColor="#8b5cf6" />
                                </linearGradient>
                            </defs>
                        </svg>
                        {/* Center text */}
                        <div className="absolute inset-0 flex flex-col items-center justify-center">
                            <span className="text-2xl font-bold text-gray-900">{overallProgress}%</span>
                            <span className="text-[10px] text-gray-500 font-medium">Overall</span>
                        </div>
                    </div>
                </div>

                {/* Status Label */}
                <div className="text-center">
                    <span className="inline-block px-3 py-1 rounded-full text-xs font-medium bg-indigo-50 text-indigo-600">
                        {getProgressLabel(overallProgress)}
                    </span>
                </div>

                {/* Detailed Progress Bars */}
                <div className="space-y-4 pt-2">
                    {/* Modules Progress */}
                    <div>
                        <div className="flex items-center justify-between text-sm mb-1.5">
                            <span className="text-gray-600 font-medium">Modules</span>
                            <span className="text-gray-900 font-semibold">
                                {completedModules} / {stats.total_modules}
                            </span>
                        </div>
                        <div className="h-2.5 bg-gray-100 rounded-full overflow-hidden">
                            <div
                                className={`h-full rounded-full transition-all duration-500 ${getProgressColor(moduleProgress)}`}
                                style={{ width: `${moduleProgress}%` }}
                            />
                        </div>
                    </div>

                    {/* Tasks Progress */}
                    <div>
                        <div className="flex items-center justify-between text-sm mb-1.5">
                            <span className="text-gray-600 font-medium">Tasks</span>
                            <span className="text-gray-900 font-semibold">
                                {completedTasks} / {stats.total_tasks}
                            </span>
                        </div>
                        <div className="h-2.5 bg-gray-100 rounded-full overflow-hidden">
                            <div
                                className={`h-full rounded-full transition-all duration-500 ${getProgressColor(taskProgress)}`}
                                style={{ width: `${taskProgress}%` }}
                            />
                        </div>
                    </div>
                </div>

                {/* Stats Summary */}
                <div className="grid grid-cols-2 gap-3 pt-3 border-t border-gray-100">
                    <div className="text-center p-2 rounded-lg bg-gray-50">
                        <p className="text-lg font-bold text-gray-900">{stats.active_modules}</p>
                        <p className="text-[10px] text-gray-500 uppercase tracking-wider">Active Modules</p>
                    </div>
                    <div className="text-center p-2 rounded-lg bg-gray-50">
                        <p className="text-lg font-bold text-gray-900">{stats.active_tasks}</p>
                        <p className="text-[10px] text-gray-500 uppercase tracking-wider">Active Tasks</p>
                    </div>
                </div>
            </CardContent>
        </Card>
    )
}
