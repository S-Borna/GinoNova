"use client"

/**
 * ============================================================================
 * SUCCESS BANNER COMPONENT — Design System v1.0
 * ============================================================================
 *
 * Green success banner for completion messages and positive feedback.
 *
 * @example
 * <SuccessBanner title="Great job!">
 *   You've successfully completed this exercise.
 * </SuccessBanner>
 *
 * @design PHASE 3 — Hands-On, Labs, Exercises & Interactive Components
 */

import * as React from 'react'
import { cn } from '../utils'

export interface SuccessBannerProps {
    /** Banner title (optional) */
    title?: string
    /** Banner content */
    children: React.ReactNode
    /** Additional CSS classes */
    className?: string
}

export function SuccessBanner({
    title,
    children,
    className,
}: SuccessBannerProps) {
    return (
        <div
            className={cn(
                // Base
                "relative rounded-xl",
                "bg-emerald-50 dark:bg-emerald-950/30",
                "border border-emerald-200 dark:border-emerald-800",
                // Left accent
                "border-l-4 border-l-emerald-500",
                // Padding
                "p-4",
                className
            )}
            role="status"
        >
            <div className="flex gap-3">
                {/* Icon */}
                <div className="flex-shrink-0">
                    <svg
                        className="w-5 h-5 text-emerald-500"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        strokeWidth={2}
                    >
                        <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                        />
                    </svg>
                </div>

                {/* Content */}
                <div className="flex-1 min-w-0">
                    {title && (
                        <h4 className="text-sm font-semibold text-emerald-800 dark:text-emerald-300 mb-1">
                            {title}
                        </h4>
                    )}
                    <div className="text-sm text-emerald-700 dark:text-emerald-400">
                        {children}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default SuccessBanner
