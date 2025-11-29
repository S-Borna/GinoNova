"use client"

/**
 * ============================================================================
 * TASK SECTION — Content section with Tesla-style spacing
 * ============================================================================
 *
 * Section wrapper for task content with:
 * - 32px padding
 * - 24px gap between blocks
 * - Subtle card styling
 *
 * @version 2.0
 * @date 2025-11-29
 */

import { cn } from "@/lib/utils"

interface TaskSectionProps {
    children: React.ReactNode
    title?: string
    icon?: React.ReactNode
    className?: string
    variant?: "default" | "transparent" | "highlighted"
}

export function TaskSection({
    children,
    title,
    icon,
    className,
    variant = "default"
}: TaskSectionProps) {
    return (
        <section
            className={cn(
                // Section spacing - 32px padding
                "p-8",
                // Variant styles
                variant === "default" && [
                    "bg-white dark:bg-neutral-900",
                    "rounded-2xl",
                    "border border-black/5 dark:border-white/5",
                    "shadow-[0_2px_8px_rgba(0,0,0,0.05)]",
                ],
                variant === "highlighted" && [
                    "bg-gradient-to-br from-indigo-50/50 to-purple-50/50",
                    "dark:from-indigo-950/20 dark:to-purple-950/20",
                    "rounded-2xl",
                    "border border-indigo-100/50 dark:border-indigo-800/30",
                ],
                variant === "transparent" && "bg-transparent",
                className
            )}
        >
            {/* Section header */}
            {title && (
                <div className="flex items-center gap-3 mb-6 pb-5 border-b border-black/5 dark:border-white/5">
                    {icon && (
                        <div className="text-indigo-500 dark:text-indigo-400">
                            {icon}
                        </div>
                    )}
                    <h2 className="text-lg font-medium text-neutral-900 dark:text-white">
                        {title}
                    </h2>
                </div>
            )}

            {/* Section content - 24px gap between blocks */}
            <div className="space-y-6">
                {children}
            </div>
        </section>
    )
}

export default TaskSection
