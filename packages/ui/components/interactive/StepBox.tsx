"use client"

/**
 * ============================================================================
 * STEP BOX COMPONENT — Design System v1.0
 * ============================================================================
 *
 * Displays a single step in a sequence.
 * Used within StepSequence or standalone.
 *
 * @example
 * <StepBox
 *   step={1}
 *   title="Install Docker"
 *   description="Download and install Docker Desktop"
 *   code="brew install --cask docker"
 * />
 *
 * @design PHASE 3 — Hands-On, Labs, Exercises & Interactive Components
 */

import * as React from 'react'
import { cn } from '../utils'
import { CodeBlock } from '../CodeBlock'

export interface StepBoxProps {
    /** Step number */
    step: number
    /** Step title */
    title: string
    /** Optional description */
    description?: string
    /** Optional code snippet */
    code?: string
    /** Code language */
    language?: string
    /** Whether this step is active */
    isActive?: boolean
    /** Whether this step is completed */
    isCompleted?: boolean
    /** Additional CSS classes */
    className?: string
}

export function StepBox({
    step,
    title,
    description,
    code,
    language = 'bash',
    isActive = false,
    isCompleted = false,
    className,
}: StepBoxProps) {
    return (
        <div
            className={cn(
                // Base
                "relative",
                // Left connector line for sequences
                "pl-8",
                className
            )}
        >
            {/* Step Number Badge */}
            <div
                className={cn(
                    "absolute left-0 top-0",
                    "w-6 h-6 rounded-full",
                    "flex items-center justify-center",
                    "text-xs font-bold",
                    "transition-colors duration-200",
                    // States
                    isCompleted
                        ? "bg-emerald-500 text-white"
                        : isActive
                            ? "bg-indigo-500 text-white"
                            : "bg-neutral-200 dark:bg-neutral-700 text-neutral-600 dark:text-neutral-300"
                )}
            >
                {isCompleted ? (
                    <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={3}>
                        <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                    </svg>
                ) : (
                    step
                )}
            </div>

            {/* Content */}
            <div className="pb-6">
                {/* Title */}
                <h4 className={cn(
                    "font-semibold",
                    isCompleted
                        ? "text-emerald-600 dark:text-emerald-400"
                        : isActive
                            ? "text-indigo-600 dark:text-indigo-400"
                            : "text-neutral-900 dark:text-white"
                )}>
                    {title}
                </h4>

                {/* Description */}
                {description && (
                    <p className="mt-1 text-sm text-neutral-600 dark:text-neutral-400">
                        {description}
                    </p>
                )}

                {/* Code */}
                {code && (
                    <div className="mt-3">
                        <CodeBlock language={language} className="text-sm">
                            {code}
                        </CodeBlock>
                    </div>
                )}
            </div>
        </div>
    )
}

export default StepBox
