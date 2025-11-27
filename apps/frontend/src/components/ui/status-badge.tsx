import * as React from "react"
import { cn } from "@/lib/utils"
import { ProgressStatus, mapStatusToColor, mapStatusToLabel } from "@/lib/progress"

interface StatusBadgeProps {
    status: ProgressStatus
    className?: string
}

export function StatusBadge({ status, className }: StatusBadgeProps) {
    return (
        <span
            className={cn(
                "inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium",
                mapStatusToColor(status),
                className
            )}
        >
            {mapStatusToLabel(status)}
        </span>
    )
}
