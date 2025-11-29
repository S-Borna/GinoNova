"use client"

/**
 * ============================================================================
 * TASK TABLE — Google/Tesla Style Table
 * ============================================================================
 *
 * Clean table component with:
 * - 1px border: rgba(0,0,0,0.08)
 * - Row height: 46px
 * - Padding: 12px horizontal
 * - Alternating subtle background: rgba(0,0,0,0.02)
 *
 * @version 2.0
 * @date 2025-11-29
 */

import { cn } from "@/lib/utils"

interface TableColumn {
    key: string
    header: string
    align?: "left" | "center" | "right"
    width?: string
}

interface TaskTableProps {
    columns: TableColumn[]
    data: Record<string, React.ReactNode>[]
    className?: string
}

export function TaskTable({ columns, data, className }: TaskTableProps) {
    return (
        <div className={cn("overflow-x-auto my-6", className)}>
            <table className="w-full border-collapse">
                {/* Header */}
                <thead>
                    <tr>
                        {columns.map((col) => (
                            <th
                                key={col.key}
                                className={cn(
                                    // Padding
                                    "px-3 py-3",
                                    // Border
                                    "border border-black/[0.08] dark:border-white/[0.08]",
                                    // Background
                                    "bg-neutral-50 dark:bg-neutral-800/50",
                                    // Text
                                    "text-sm font-medium text-neutral-700 dark:text-neutral-300",
                                    // Alignment
                                    col.align === "center" && "text-center",
                                    col.align === "right" && "text-right",
                                    !col.align && "text-left"
                                )}
                                style={{ width: col.width }}
                            >
                                {col.header}
                            </th>
                        ))}
                    </tr>
                </thead>

                {/* Body */}
                <tbody>
                    {data.map((row, rowIndex) => (
                        <tr
                            key={rowIndex}
                            className={cn(
                                // Row height
                                "h-[46px]",
                                // Alternating background
                                rowIndex % 2 === 1 && "bg-black/[0.02] dark:bg-white/[0.02]",
                                // Hover
                                "hover:bg-black/[0.04] dark:hover:bg-white/[0.04]",
                                "transition-colors duration-150"
                            )}
                        >
                            {columns.map((col) => (
                                <td
                                    key={col.key}
                                    className={cn(
                                        // Padding
                                        "px-3",
                                        // Border
                                        "border border-black/[0.08] dark:border-white/[0.08]",
                                        // Text
                                        "text-sm text-neutral-700 dark:text-neutral-300",
                                        // Alignment
                                        col.align === "center" && "text-center",
                                        col.align === "right" && "text-right"
                                    )}
                                >
                                    {row[col.key]}
                                </td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default TaskTable
