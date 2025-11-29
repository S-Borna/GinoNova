"use client"

/**
 * ============================================================================
 * EXERCISE BLOCK COMPONENT — Design System v1.0
 * ============================================================================
 *
 * Small tasks inside a lesson with numbered badge.
 * Perfect for practice exercises and quick challenges.
 *
 * @example
 * <ExerciseBlock
 *   index={1}
 *   prompt="Create a new Dockerfile in your project root"
 *   code="touch Dockerfile"
 *   language="bash"
 * />
 *
 * @design PHASE 3 — Hands-On, Labs, Exercises & Interactive Components
 */

import * as React from 'react'
import { cn } from '../utils'
import { CodeBlock } from '../CodeBlock'

export interface ExerciseBlockProps {
    /** Exercise number (1, 2, 3...) */
    index: number
    /** Instruction prompt */
    prompt: string
    /** Optional code snippet */
    code?: string
    /** Code language for syntax highlighting */
    language?: string
    /** Additional CSS classes */
    className?: string
}

export function ExerciseBlock({
    index,
    prompt,
    code,
    language = 'bash',
    className,
}: ExerciseBlockProps) {
    return (
        <div
            className={cn(
                // Base card
                "relative rounded-xl",
                "bg-white dark:bg-neutral-900",
                "border border-neutral-200 dark:border-neutral-800",
                "shadow-sm",
                // Padding
                "p-5",
                className
            )}
        >
            <div className="flex items-start gap-4">
                {/* Number Badge */}
                <div
                    className={cn(
                        "flex-shrink-0",
                        "w-8 h-8 rounded-full",
                        "bg-indigo-100 dark:bg-indigo-900/40",
                        "flex items-center justify-center",
                        "text-sm font-bold text-indigo-600 dark:text-indigo-400"
                    )}
                >
                    {index}
                </div>

                {/* Content */}
                <div className="flex-1 min-w-0">
                    {/* Prompt */}
                    <p className="text-neutral-900 dark:text-white font-medium">
                        {prompt}
                    </p>

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
        </div>
    )
}

export default ExerciseBlock
