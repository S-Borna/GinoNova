"use client"

/**
 * ============================================================================
 * TASK PAGE — Design System v1.0
 * ============================================================================
 *
 * Wrapper component for ALL task pages.
 * Auto-applies:
 * - PageLayout (centered, max-width 840px)
 * - Proper section spacing
 * - Headline/subheadline hierarchy
 * - Consistent text-to-code spacing
 *
 * Ensures all task pages visually match landing page quality.
 *
 * @example
 * <TaskPage
 *   title="Install Docker"
 *   type="foundation"
 *   estimatedMinutes={15}
 *   xpReward={50}
 *   difficulty={2}
 * >
 *   <TaskPage.Section>
 *     <TaskPage.Headline>Introduction</TaskPage.Headline>
 *     <TaskPage.Block>
 *       <p>Docker is a containerization platform...</p>
 *       <TaskPage.Subtext beforeCode>Run the following:</TaskPage.Subtext>
 *       <TaskPage.Code language="bash">docker --version</TaskPage.Code>
 *     </TaskPage.Block>
 *   </TaskPage.Section>
 * </TaskPage>
 */

import * as React from 'react'
import { cn } from './utils'
import { PageLayout } from './PageLayout'
import { Section } from './Section'
import { Block } from './Block'
import { Headline } from './Headline'
import { Subtext } from './Subtext'
import { CodeBlock } from './CodeBlock'

/* ============================================================================
   TYPES
   ============================================================================ */

export type TaskType =
    | 'foundation'
    | 'practice'
    | 'deepening'
    | 'project'
    | 'challenge'
    | 'quiz'

export interface TaskPageProps {
    children: React.ReactNode
    /** Task title */
    title: string
    /** Task type */
    type?: TaskType
    /** Estimated completion time */
    estimatedMinutes?: number
    /** XP reward */
    xpReward?: number
    /** Difficulty level (1-5) */
    difficulty?: number
    /** Module name (for breadcrumb) */
    moduleName?: string
    /** Back navigation handler */
    onBack?: () => void
    /** Additional CSS classes */
    className?: string
}

/* ============================================================================
   TYPE CONFIGURATION
   ============================================================================ */

const typeConfig: Record<TaskType, {
    label: string
    emoji: string
    colorClass: string
    bgClass: string
}> = {
    foundation: {
        label: 'Foundation',
        emoji: '📚',
        colorClass: 'text-blue-600 dark:text-blue-400',
        bgClass: 'bg-blue-50 dark:bg-blue-950/40',
    },
    practice: {
        label: 'Practice',
        emoji: '💻',
        colorClass: 'text-emerald-600 dark:text-emerald-400',
        bgClass: 'bg-emerald-50 dark:bg-emerald-950/40',
    },
    deepening: {
        label: 'Deep Dive',
        emoji: '🔍',
        colorClass: 'text-violet-600 dark:text-violet-400',
        bgClass: 'bg-violet-50 dark:bg-violet-950/40',
    },
    project: {
        label: 'Project',
        emoji: '🚀',
        colorClass: 'text-orange-600 dark:text-orange-400',
        bgClass: 'bg-orange-50 dark:bg-orange-950/40',
    },
    challenge: {
        label: 'Challenge',
        emoji: '🏆',
        colorClass: 'text-rose-600 dark:text-rose-400',
        bgClass: 'bg-rose-50 dark:bg-rose-950/40',
    },
    quiz: {
        label: 'Quiz',
        emoji: '❓',
        colorClass: 'text-cyan-600 dark:text-cyan-400',
        bgClass: 'bg-cyan-50 dark:bg-cyan-950/40',
    },
}

/* ============================================================================
   ICONS
   ============================================================================ */

function ArrowLeftIcon({ className }: { className?: string }) {
    return (
        <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M19 12H5M12 19l-7-7 7-7" />
        </svg>
    )
}

function ClockIcon({ className }: { className?: string }) {
    return (
        <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <circle cx="12" cy="12" r="10" />
            <path d="M12 6v6l4 2" />
        </svg>
    )
}

function ZapIcon({ className }: { className?: string }) {
    return (
        <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
        </svg>
    )
}

/* ============================================================================
   DIFFICULTY DOTS
   ============================================================================ */

function DifficultyDots({ difficulty }: { difficulty: number }) {
    const labels = ['Beginner', 'Easy', 'Medium', 'Hard', 'Expert']
    return (
        <div className="flex items-center gap-1.5">
            <div className="flex items-center gap-0.5">
                {Array.from({ length: 5 }).map((_, i) => (
                    <div
                        key={i}
                        className={cn(
                            'w-1.5 h-1.5 rounded-full',
                            i < difficulty
                                ? 'bg-neutral-600 dark:bg-neutral-300'
                                : 'bg-neutral-200 dark:bg-neutral-700'
                        )}
                    />
                ))}
            </div>
            <span className="text-xs text-[#6B7280] dark:text-neutral-400">
                {labels[Math.min(difficulty - 1, 4)] || 'Beginner'}
            </span>
        </div>
    )
}

/* ============================================================================
   TASK PAGE COMPONENT
   ============================================================================ */

export function TaskPage({
    children,
    title,
    type = 'foundation',
    estimatedMinutes,
    xpReward,
    difficulty,
    moduleName,
    onBack,
    className,
}: TaskPageProps) {
    const config = typeConfig[type]

    return (
        <PageLayout className={className}>
            {/* Header */}
            <header className="mb-8">
                {/* Back navigation */}
                {onBack && (
                    <button
                        onClick={onBack}
                        className={cn(
                            'flex items-center gap-2 mb-6',
                            'text-sm font-medium text-[#6B7280] dark:text-neutral-400',
                            'hover:text-[#111827] dark:hover:text-white',
                            'transition-colors'
                        )}
                    >
                        <ArrowLeftIcon className="w-4 h-4" />
                        <span>{moduleName || 'Back to Module'}</span>
                    </button>
                )}

                {/* Type badge */}
                <div className="flex items-center gap-3 mb-3">
                    <span className="text-2xl" role="img" aria-label={config.label}>
                        {config.emoji}
                    </span>
                    <span className={cn(
                        'px-2.5 py-1 rounded-full text-xs font-medium',
                        config.bgClass,
                        config.colorClass
                    )}>
                        {config.label}
                    </span>
                </div>

                {/* Title */}
                <h1 className="text-[34px] font-semibold leading-[40px] tracking-tight text-[#111827] dark:text-white">
                    {title}
                </h1>

                {/* Meta row */}
                {(estimatedMinutes || xpReward || difficulty) && (
                    <div className="flex items-center gap-4 mt-4">
                        {estimatedMinutes && (
                            <div className="flex items-center gap-1.5 text-[#6B7280] dark:text-neutral-400">
                                <ClockIcon className="w-4 h-4" />
                                <span className="text-sm">{estimatedMinutes} min</span>
                            </div>
                        )}
                        {xpReward && (
                            <div className="flex items-center gap-1.5 text-amber-600 dark:text-amber-400">
                                <ZapIcon className="w-4 h-4" />
                                <span className="text-sm font-semibold">{xpReward} XP</span>
                            </div>
                        )}
                        {difficulty && (
                            <DifficultyDots difficulty={difficulty} />
                        )}
                    </div>
                )}
            </header>

            {/* Content */}
            <div className="space-y-8">
                {children}
            </div>
        </PageLayout>
    )
}

/* ============================================================================
   COMPOUND COMPONENTS
   ============================================================================ */

// Attach sub-components for convenient access
TaskPage.Section = Section
TaskPage.Block = Block
TaskPage.Headline = Headline
TaskPage.Subtext = Subtext
TaskPage.Code = CodeBlock

export default TaskPage
