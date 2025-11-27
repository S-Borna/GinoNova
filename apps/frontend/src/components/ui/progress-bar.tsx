import * as React from "react"
import { cn } from "@/lib/utils"

interface ProgressBarProps {
    value: number
    className?: string
    showLabel?: boolean
}

export function ProgressBar({
    value,
    className,
    showLabel = true,
}: ProgressBarProps) {
    // Clamp value between 0 and 100
    const clampedValue = Math.max(0, Math.min(100, value))

    // Determine color based on value
    const getColorClass = () => {
        if (clampedValue === 100) return "bg-green-500"
        if (clampedValue >= 50) return "bg-yellow-500"
        if (clampedValue > 0) return "bg-blue-500"
        return "bg-gray-300"
    }

    return (
        <div className={cn("w-full", className)}>
            <div className="flex items-center gap-2">
                <div className="flex-1 h-2.5 bg-gray-200 rounded-full overflow-hidden">
                    <div
                        className={cn(
                            "h-full rounded-full transition-all duration-300",
                            getColorClass()
                        )}
                        style={{ width: `${clampedValue}%` }}
                    />
                </div>
                {showLabel && (
                    <span className="text-sm font-medium text-gray-700 min-w-[3rem] text-right">
                        {clampedValue}%
                    </span>
                )}
            </div>
        </div>
    )
}
