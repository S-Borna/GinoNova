import * as React from "react"
import { cn } from "@/lib/utils"

interface ProgressBarProps {
    value: number
    className?: string
    showLabel?: boolean
    size?: "sm" | "md" | "lg"
    variant?: "default" | "gradient" | "striped"
    animated?: boolean
    color?: "auto" | "success" | "warning" | "info" | "primary"
}

export function ProgressBar({
    value,
    className,
    showLabel = true,
    size = "md",
    variant = "gradient",
    animated = true,
    color = "auto",
}: ProgressBarProps) {
    // Clamp value between 0 and 100
    const clampedValue = Math.max(0, Math.min(100, value))

    // Size classes
    const sizeClasses = {
        sm: "h-1.5",
        md: "h-2.5",
        lg: "h-4",
    }

    // Get color based on value or explicit color
    const getColorClass = () => {
        const effectiveColor = color === "auto"
            ? clampedValue >= 80
                ? "success"
                : clampedValue >= 50
                    ? "warning"
                    : clampedValue > 0
                        ? "info"
                        : "primary"
            : color

        if (variant === "gradient") {
            switch (effectiveColor) {
                case "success":
                    return "progress-bar-gradient-success"
                case "warning":
                    return "progress-bar-gradient-warning"
                case "info":
                    return "progress-bar-gradient-info"
                case "primary":
                default:
                    return "progress-bar-gradient-primary"
            }
        }

        // Solid colors
        switch (effectiveColor) {
            case "success":
                return "bg-emerald-500 dark:bg-emerald-400"
            case "warning":
                return "bg-amber-500 dark:bg-amber-400"
            case "info":
                return "bg-blue-500 dark:bg-blue-400"
            case "primary":
            default:
                return "bg-indigo-500 dark:bg-indigo-400"
        }
    }

    // Label size classes
    const labelSizeClasses = {
        sm: "text-xs",
        md: "text-sm",
        lg: "text-base",
    }

    return (
        <div className={cn("w-full", className)}>
            <div className="flex items-center gap-2">
                <div
                    className={cn(
                        "flex-1 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden",
                        sizeClasses[size]
                    )}
                >
                    <div
                        className={cn(
                            "h-full rounded-full transition-all duration-500 ease-out",
                            getColorClass(),
                            animated && "progress-bar-animated",
                            variant === "striped" && "bg-striped"
                        )}
                        style={{ width: `${clampedValue}%` }}
                    >
                        {variant === "gradient" && (
                            <div className="w-full h-full shimmer opacity-30" />
                        )}
                    </div>
                </div>
                {showLabel && (
                    <span
                        className={cn(
                            "font-medium text-gray-700 dark:text-gray-300 min-w-[3rem] text-right tabular-nums",
                            labelSizeClasses[size]
                        )}
                    >
                        {clampedValue}%
                    </span>
                )}
            </div>
        </div>
    )
}
