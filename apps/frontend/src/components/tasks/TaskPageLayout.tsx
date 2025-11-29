"use client"

/**
 * ============================================================================
 * TASK PAGE LAYOUT — Material 3 + Tesla + Apple Hybrid
 * ============================================================================
 *
 * Main layout wrapper for task detail pages with:
 * - Tesla-style generous spacing
 * - Apple's white-space and grid structure
 * - Material 3 elevation system
 *
 * @version 2.0
 * @date 2025-11-29
 */

import { cn } from "@/lib/utils"

interface TaskPageLayoutProps {
    children: React.ReactNode
    className?: string
}

export function TaskPageLayout({ children, className }: TaskPageLayoutProps) {
    return (
        <div
            className={cn(
                // Max width and centering
                "max-w-[840px] mx-auto",
                // Responsive padding
                "px-5 sm:px-6 lg:px-8",
                // Generous vertical spacing
                "py-10 sm:py-12",
                // Base font settings
                "font-sans leading-relaxed",
                className
            )}
        >
            {children}
        </div>
    )
}

export default TaskPageLayout
