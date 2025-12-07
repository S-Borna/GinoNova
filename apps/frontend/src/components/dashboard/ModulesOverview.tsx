"use client"

/**
 * ModulesOverview Component
 * Phase D.2: Apple-Inspired Module Cards Grid
 *
 * Features:
 * - Module cards with icons
 * - Progress bars
 * - Status badges
 * - Click to navigate
 */

import * as React from "react"
import Link from "next/link"
import { Badge } from "@/components/ui/badge"
import { cn } from "@/lib/utils"

/* ============================================================================
   TYPES
   ============================================================================ */

interface Module {
    id: string
    name: string
    description?: string | null
    slug?: string
    tasksCompleted?: number
    totalTasks?: number
    status?: "not_started" | "in_progress" | "complete" | "locked"
    icon?: string
}

interface ModulesOverviewProps {
    modules?: Module[]
    className?: string
}

/* ============================================================================
   HELPER FUNCTIONS
   ============================================================================ */

const moduleIcons: Record<number, string> = {
    1: "🎯",  // Onboarding
    2: "📖",  // Foundations
    3: "🐧",  // Linux
    4: "💻",  // Shell
    5: "🔀",  // Git
    6: "🌐",  // Networking
    7: "☁️",  // Cloud
    8: "🏗️",  // IaC
    9: "🐳",  // Containers
    10: "☸️", // Kubernetes
}

function getModuleIcon(index: number, icon?: string): string {
    if (icon) return icon
    return moduleIcons[index + 1] || "📚"
}

function getStatusBadge(status?: string): { label: string; variant: "default" | "secondary" | "destructive" | "outline"; className?: string } {
    switch (status) {
        case "complete":
            return {
                label: "Complete",
                variant: "default",
                className: "bg-emerald-500 hover:bg-emerald-600 text-white"
            }
        case "in_progress":
            return {
                label: "In Progress",
                variant: "default",
                className: "bg-primary-500 hover:bg-primary-600 text-white"
            }
        case "locked":
            return {
                label: "Locked",
                variant: "secondary",
                className: "bg-neutral-300 text-neutral-600"
            }
        default:
            return {
                label: "Not Started",
                variant: "outline",
                className: "border-neutral-300 text-neutral-500"
            }
    }
}

function getStatusFromProgress(completed: number, total: number): "not_started" | "in_progress" | "complete" {
    if (total === 0) return "not_started"
    if (completed >= total) return "complete"
    if (completed > 0) return "in_progress"
    return "not_started"
}

/* ============================================================================
   MODULE CARD
   ============================================================================ */

interface ModuleCardProps {
    module: Module
    index: number
    delay?: number
}

function ModuleCard({ module, index, delay = 0 }: ModuleCardProps) {
    const completed = module.tasksCompleted ?? 0
    const total = module.totalTasks ?? 5
    const progress = total > 0 ? Math.round((completed / total) * 100) : 0
    const status = module.status ?? getStatusFromProgress(completed, total)
    const statusBadge = getStatusBadge(status)
    const icon = getModuleIcon(index, module.icon)
    const isLocked = status === "locked"

    const cardContent = (
        <div
            className={cn(
                "bg-white dark:bg-neutral-800 rounded-xl shadow-sm border border-gray-100 dark:border-neutral-700 p-5 transition-all duration-200 animate-fade-in-up h-full",
                isLocked && "opacity-60 cursor-not-allowed",
                !isLocked && "hover:shadow-md hover:-translate-y-0.5 cursor-pointer"
            )}
            style={{ animationDelay: `${delay}ms` }}
        >
            {/* Header */}
            <div className="flex items-start justify-between mb-4">
                {/* Icon */}
                <div className={cn(
                    "w-10 h-10 rounded-lg flex items-center justify-center text-xl",
                    "bg-gray-100 dark:bg-neutral-700"
                )}>
                    {isLocked ? "🔒" : icon}
                </div>

                {/* Status badge */}
                <Badge
                    variant={statusBadge.variant}
                    className={cn("text-xs", statusBadge.className)}
                >
                    {statusBadge.label}
                </Badge>
            </div>

            {/* Content */}
            <div className="space-y-2">
                <h3 className="font-semibold text-gray-900 dark:text-white line-clamp-1">
                    {module.name}
                </h3>

                {module.description && (
                    <p className="text-sm text-gray-500 dark:text-neutral-400 line-clamp-2">
                        {module.description}
                    </p>
                )}
            </div>

            {/* Progress */}
            <div className="mt-4 space-y-2">
                <div className="flex justify-between text-xs">
                    <span className="text-gray-500 dark:text-neutral-400">
                        {completed} / {total} tasks
                    </span>
                    <span className={cn(
                        "font-medium",
                        status === "complete" ? "text-emerald-600" : "text-indigo-600"
                    )}>
                        {progress}%
                    </span>
                </div>
                <div className="w-full bg-gray-200 dark:bg-neutral-700 rounded-full h-1.5">
                    <div
                        className={cn(
                            "h-1.5 rounded-full transition-all duration-700 ease-out",
                            status === "complete"
                                ? "bg-gradient-to-r from-emerald-500 to-teal-500"
                                : "bg-gradient-to-r from-indigo-500 to-purple-500"
                        )}
                        style={{ width: `${progress}%` }}
                    />
                </div>
            </div>
        </div>
    )

    if (isLocked) {
        return cardContent
    }

    return (
        <Link prefetch={false} href={`/modules/${module.slug || module.id}`}>
            {cardContent}
        </Link>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function ModulesOverview({ modules = [], className }: ModulesOverviewProps) {
    // Default bootcamp modules if none provided
    const displayModules = modules.length > 0 ? modules : [
        { id: "1", name: "Onboarding", tasksCompleted: 0, totalTasks: 5 },
        { id: "2", name: "Foundations", tasksCompleted: 0, totalTasks: 8 },
        { id: "3", name: "Linux Basics", tasksCompleted: 0, totalTasks: 10 },
        { id: "4", name: "Shell Scripting", tasksCompleted: 0, totalTasks: 8 },
        { id: "5", name: "Git & GitHub", tasksCompleted: 0, totalTasks: 7 },
        { id: "6", name: "Networking", tasksCompleted: 0, totalTasks: 9 },
        { id: "7", name: "Cloud & AWS", tasksCompleted: 0, totalTasks: 12 },
        { id: "8", name: "Infrastructure as Code", tasksCompleted: 0, totalTasks: 10 },
        { id: "9", name: "Containers", tasksCompleted: 0, totalTasks: 8 },
        { id: "10", name: "Kubernetes", tasksCompleted: 0, totalTasks: 15 },
    ]

    return (
        <div className={className}>
            {/* Section header */}
            <div className="flex items-center justify-between mb-6">
                <div>
                    <h2 className="text-xl font-bold text-gray-900 dark:text-white">
                        Learning Path
                    </h2>
                    <p className="text-sm text-gray-500 dark:text-neutral-400">
                        {displayModules.length} modules in your bootcamp
                    </p>
                </div>
                <Link
                    href="/modules"
                    className="text-sm font-medium text-indigo-600 dark:text-indigo-400 hover:underline"
                >
                    View all →
                </Link>
            </div>

            {/* Module grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                {displayModules.slice(0, 8).map((module, index) => (
                    <ModuleCard
                        key={module.id}
                        module={module}
                        index={index}
                        delay={100 + index * 50}
                    />
                ))}
            </div>

            {/* Show more link if there are more modules */}
            {displayModules.length > 8 && (
                <div className="mt-6 text-center">
                    <Link
                        href="/modules"
                        className="inline-flex items-center gap-2 px-6 py-2.5 rounded-full bg-gray-100 dark:bg-neutral-800 text-gray-700 dark:text-neutral-300 font-medium hover:bg-gray-200 dark:hover:bg-neutral-700 transition-colors"
                    >
                        View all {displayModules.length} modules
                        <span>→</span>
                    </Link>
                </div>
            )}
        </div>
    )
}
