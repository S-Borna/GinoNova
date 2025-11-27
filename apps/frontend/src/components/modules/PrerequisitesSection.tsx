"use client"

/**
 * ============================================================================
 * PREREQUISITES SECTION — Apple-Inspired Design (D.4)
 * ============================================================================
 *
 * Shows required modules with:
 * - Link to each prerequisite
 * - Completion status
 * - Visual progress indicator
 *
 * @phase D.4 - Modules UI
 */

import { cn } from "@/lib/utils"
import { GlassCard } from "@/components/ui/glass-card"
import { CheckCircle2, Circle, Lock, ArrowRight } from "lucide-react"
import Link from "next/link"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface Prerequisite {
    id: string
    title: string
    isComplete: boolean
    progress: number
}

export interface PrerequisitesSectionProps {
    prerequisites: Prerequisite[]
    className?: string
}

/* ============================================================================
   PREREQUISITES SECTION COMPONENT
   ============================================================================ */

export function PrerequisitesSection({
    prerequisites,
    className
}: PrerequisitesSectionProps) {
    if (prerequisites.length === 0) {
        return null
    }

    const allComplete = prerequisites.every(p => p.isComplete)

    return (
        <GlassCard
            variant="default"
            padding="lg"
            radius="xl"
            className={className}
        >
            {/* Header */}
            <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-2">
                    {allComplete ? (
                        <CheckCircle2 className="w-5 h-5 text-success-500" />
                    ) : (
                        <Lock className="w-5 h-5 text-warning-500" />
                    )}
                    <h3 className="text-lg font-semibold text-neutral-900 dark:text-white">
                        Prerequisites
                    </h3>
                </div>
                <span className={cn(
                    "text-sm font-medium px-2.5 py-1 rounded-full",
                    allComplete
                        ? "bg-success-100 dark:bg-success-900/30 text-success-700 dark:text-success-400"
                        : "bg-warning-100 dark:bg-warning-900/30 text-warning-700 dark:text-warning-400"
                )}>
                    {allComplete ? "All Complete" : `${prerequisites.filter(p => p.isComplete).length}/${prerequisites.length}`}
                </span>
            </div>

            {/* Prerequisites list */}
            <div className="space-y-3">
                {prerequisites.map((prereq) => (
                    <Link
                        key={prereq.id}
                        href={`/modules/${prereq.id}`}
                        className={cn(
                            "flex items-center gap-3 p-3 rounded-xl transition-all duration-200",
                            "bg-neutral-50 dark:bg-neutral-800/50",
                            "hover:bg-neutral-100 dark:hover:bg-neutral-800",
                            "group"
                        )}
                    >
                        {/* Status icon */}
                        {prereq.isComplete ? (
                            <CheckCircle2 className="w-5 h-5 text-success-500 flex-shrink-0" />
                        ) : (
                            <Circle className="w-5 h-5 text-neutral-400 flex-shrink-0" />
                        )}

                        {/* Module info */}
                        <div className="flex-1 min-w-0">
                            <p className={cn(
                                "font-medium truncate",
                                prereq.isComplete
                                    ? "text-neutral-500 dark:text-neutral-400"
                                    : "text-neutral-900 dark:text-white"
                            )}>
                                {prereq.title}
                            </p>
                            <p className="text-xs text-neutral-500">
                                {prereq.isComplete ? "Completed" : `${prereq.progress}% complete`}
                            </p>
                        </div>

                        {/* Arrow */}
                        <ArrowRight className={cn(
                            "w-4 h-4 text-neutral-400 transition-transform",
                            "group-hover:translate-x-1"
                        )} />
                    </Link>
                ))}
            </div>

            {/* Info message if not all complete */}
            {!allComplete && (
                <p className="mt-4 text-sm text-neutral-500 dark:text-neutral-400">
                    Complete all prerequisites to unlock this module&apos;s full content.
                </p>
            )}
        </GlassCard>
    )
}

export default PrerequisitesSection
