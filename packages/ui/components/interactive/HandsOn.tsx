"use client"

/**
 * ============================================================================
 * HANDS-ON COMPONENT — Design System v1.0
 * ============================================================================
 *
 * Used for "Hands-On Lab: Do X" sections in lessons.
 * Features blue accent border, light surface background, and tool icon.
 *
 * @example
 * <HandsOn title="Install Docker">
 *   <CodeBlock language="bash">docker --version</CodeBlock>
 * </HandsOn>
 *
 * @design PHASE 3 — Hands-On, Labs, Exercises & Interactive Components
 */

import * as React from 'react'
import { cn } from '../utils'

export interface HandsOnProps {
    /** Title of the hands-on section */
    title: string
    /** Optional description */
    description?: string
    /** Child content (CodeBlock, steps, etc.) */
    children?: React.ReactNode
    /** Additional CSS classes */
    className?: string
}

export function HandsOn({
    title,
    description,
    children,
    className,
}: HandsOnProps) {
    return (
        <div
            className={cn(
                // Base card
                "relative rounded-2xl",
                "bg-indigo-50/50 dark:bg-indigo-950/20",
                "border border-indigo-200/50 dark:border-indigo-800/50",
                // Left accent border
                "border-l-4 border-l-indigo-500 dark:border-l-indigo-400",
                // Padding
                "p-6",
                className
            )}
        >
            {/* Header */}
            <div className="flex items-start gap-3 mb-4">
                {/* Icon */}
                <span className="text-2xl flex-shrink-0">🛠️</span>

                {/* Title & Description */}
                <div className="flex-1 min-w-0">
                    <h3 className="text-lg font-semibold text-neutral-900 dark:text-white">
                        {title}
                    </h3>
                    {description && (
                        <p className="mt-1 text-sm text-neutral-600 dark:text-neutral-400">
                            {description}
                        </p>
                    )}
                </div>
            </div>

            {/* Content */}
            {children && (
                <div className="mt-4">
                    {children}
                </div>
            )}
        </div>
    )
}

export default HandsOn
