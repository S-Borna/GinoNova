"use client"

/**
 * ============================================================================
 * WARNING BANNER COMPONENT — Design System v1.0
 * ============================================================================
 *
 * Yellow warning banner for caution text and important notices.
 *
 * @example
 * <WarningBanner title="Caution">
 *   This action cannot be undone. Make sure to backup your data first.
 * </WarningBanner>
 *
 * @design PHASE 3 — Hands-On, Labs, Exercises & Interactive Components
 */

import * as React from 'react'
import { cn } from '../utils'

export interface WarningBannerProps {
    /** Banner title (optional) */
    title?: string
    /** Banner content */
    children: React.ReactNode
    /** Additional CSS classes */
    className?: string
}

export function WarningBanner({
    title,
    children,
    className,
}: WarningBannerProps) {
    return (
        <div
            className={cn(
                // Base
                "relative rounded-xl",
                "bg-amber-50 dark:bg-amber-950/30",
                "border border-amber-200 dark:border-amber-800",
                // Left accent
                "border-l-4 border-l-amber-500",
                // Padding
                "p-4",
                className
            )}
            role="alert"
        >
            <div className="flex gap-3">
                {/* Icon */}
                <div className="flex-shrink-0">
                    <svg
                        className="w-5 h-5 text-amber-500"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        strokeWidth={2}
                    >
                        <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
                        />
                    </svg>
                </div>

                {/* Content */}
                <div className="flex-1 min-w-0">
                    {title && (
                        <h4 className="text-sm font-semibold text-amber-800 dark:text-amber-300 mb-1">
                            {title}
                        </h4>
                    )}
                    <div className="text-sm text-amber-700 dark:text-amber-400">
                        {children}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default WarningBanner
