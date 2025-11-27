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
import { GlassCard } from "@/components/ui/glass-card"
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
        <GlassCard
            variant="default"
            padding="md"
            radius="lg"
            interactive={!isLocked}
            className={cn(
                "h-full animate-fade-in-up group",
                isLocked && "opacity-60 cursor-not-allowed",
                !isLocked && "hover:shadow-glow"
            )}
            style={{ animationDelay: `${delay}ms` }}
        >
            {/* Header */}
            <div className="flex items-start justify-between mb-4">
                {/* Icon */}
                <div className={cn(
                    "w-12 h-12 rounded-xl flex items-center justify-center text-2xl",
                    "bg-gradient-to-br from-neutral-100 to-neutral-50",
                    "dark:from-neutral-800 dark:to-neutral-700",
                    "shadow-sm transition-transform duration-300",
                    !isLocked && "group-hover:scale-110"
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
                <h3 className="font-semibold text-neutral-900 dark:text-white line-clamp-1">
                    {module.name}
                </h3>

                {module.description && (
                    <p className="text-sm text-neutral-500 dark:text-neutral-400 line-clamp-2">
                        {module.description}
                    </p>
                )}
            </div>

            {/* Progress */}
            <div className="mt-4 space-y-2">
                <div className="flex justify-between text-xs">
                    <span className="text-neutral-500 dark:text-neutral-400">
                        {completed} / {total} tasks
                    </span>
                    <span className={cn(
                        "font-medium",
                        status === "complete" ? "text-emerald-600" : "text-primary-600"
                    )}>
                        {progress}%
                    </span>
                </div>
                <div className="h-1.5 bg-neutral-200 dark:bg-neutral-700 rounded-full overflow-hidden">
                    <div
                        className={cn(
                            "h-full rounded-full transition-all duration-700 ease-out",
                            status === "complete"
                                ? "bg-gradient-to-r from-emerald-500 to-teal-500"
                                : "bg-gradient-to-r from-primary-500 to-primary-400"
                        )}
                        style={{ width: `${progress}%` }}
                    />
                </div>
            </div>

            {/* Action hint */}
            {!isLocked && (
                <div className="mt-4 flex items-center justify-between text-sm">
                    <span className="text-primary-600 dark:text-primary-400 font-medium opacity-0 group-hover:opacity-100 transition-opacity">
                        {status === "complete" ? "Review →" : status === "in_progress" ? "Continue →" : "Start →"}
                    </span>
                </div>
            )}
        </GlassCard>
    )

    if (isLocked) {
        return cardContent
    }

    return (
        <Link href={`/modules/${module.slug || module.id}`}>
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
                    <h2 className="text-xl font-bold text-neutral-900 dark:text-white">
                        Learning Path
                    </h2>
                    <p className="text-sm text-neutral-500 dark:text-neutral-400">
                        {displayModules.length} modules in your bootcamp
                    </p>
                </div>
                <Link
                    href="/modules"
                    className="text-sm font-medium text-primary-600 dark:text-primary-400 hover:underline"
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
                        className="inline-flex items-center gap-2 px-6 py-2 rounded-full bg-neutral-100 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 font-medium hover:bg-neutral-200 dark:hover:bg-neutral-700 transition-colors"
                    >
                        View all {displayModules.length} modules
                        <span>→</span>
                    </Link>
                </div>
            )}
        </div>
    )
}
