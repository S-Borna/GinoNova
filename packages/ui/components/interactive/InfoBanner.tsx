"use client"

/**
 * ============================================================================
 * INFO BANNER COMPONENT — Design System v1.0
 * ============================================================================
 *
 * Blue information banner for tips and helpful information.
 *
 * @example
 * <InfoBanner>
 *   Pro tip: Use tab completion to speed up your terminal workflow.
 * </InfoBanner>
 *
 * @design PHASE 3 — Hands-On, Labs, Exercises & Interactive Components
 */

import * as React from 'react'
import { cn } from '../utils'

export interface InfoBannerProps {
    /** Banner title (optional) */
    title?: string
    /** Banner content */
    children: React.ReactNode
    /** Additional CSS classes */
    className?: string
}

export function InfoBanner({
    title,
    children,
    className,
}: InfoBannerProps) {
    return (
        <div
            className={cn(
                // Base
                "relative rounded-xl",
                "bg-blue-50 dark:bg-blue-950/30",
                "border border-blue-200 dark:border-blue-800",
                // Left accent
                "border-l-4 border-l-blue-500",
                // Padding
                "p-4",
                className
            )}
            role="note"
        >
            <div className="flex gap-3">
                {/* Icon */}
                <div className="flex-shrink-0">
                    <svg
                        className="w-5 h-5 text-blue-500"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        strokeWidth={2}
                    >
                        <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                        />
                    </svg>
                </div>

                {/* Content */}
                <div className="flex-1 min-w-0">
                    {title && (
                        <h4 className="text-sm font-semibold text-blue-800 dark:text-blue-300 mb-1">
                            {title}
                        </h4>
                    )}
                    <div className="text-sm text-blue-700 dark:text-blue-400">
                        {children}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default InfoBanner
