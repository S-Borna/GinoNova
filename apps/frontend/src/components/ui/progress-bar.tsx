/**
 * ProgressBar Component
 * Phase D.1: Apple-Inspired Progress Visualization
 *
 * Features:
 * - Multiple size variants
 * - Gradient, solid, and striped styles
 * - Auto-color based on progress value
 * - Animated fill with shimmer effect
 * - Accessible with ARIA attributes
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { cva, type VariantProps } from "class-variance-authority"

/* ============================================================================
   PROGRESS BAR VARIANTS
   ============================================================================ */

const progressBarContainerVariants = cva(
    // Base: Track styles
    [
        "flex-1",
        "rounded-full",
        "overflow-hidden",
        "bg-neutral-200",
        "dark:bg-neutral-700",
    ],
    {
        variants: {
            size: {
                xs: "h-1",
                sm: "h-1.5",
                md: "h-2.5",
                lg: "h-4",
                xl: "h-5",
            },
        },
        defaultVariants: {
            size: "md",
        },
    }
)

const progressBarFillVariants = cva(
    // Base: Fill styles
    [
        "h-full",
        "rounded-full",
        "transition-all",
        "duration-500",
        "ease-out",
    ],
    {
        variants: {
            variant: {
                default: "",
                gradient: "",
                striped: "bg-striped",
                glow: "",
            },
            color: {
                primary: "",
                success: "",
                warning: "",
                info: "",
                xp: "",
                auto: "",
            },
        },
        compoundVariants: [
            // Default (solid) colors
            { variant: "default", color: "primary", className: "bg-primary-500" },
            { variant: "default", color: "success", className: "bg-accent-success" },
            { variant: "default", color: "warning", className: "bg-accent-warning" },
            { variant: "default", color: "info", className: "bg-accent-info" },
            { variant: "default", color: "xp", className: "bg-accent-xp" },
            // Gradient colors
            { variant: "gradient", color: "primary", className: "bg-gradient-to-r from-primary-500 to-primary-600" },
            { variant: "gradient", color: "success", className: "bg-gradient-to-r from-emerald-500 to-green-500" },
            { variant: "gradient", color: "warning", className: "bg-gradient-to-r from-amber-400 to-orange-500" },
            { variant: "gradient", color: "info", className: "bg-gradient-to-r from-blue-400 to-cyan-500" },
            { variant: "gradient", color: "xp", className: "bg-gradient-to-r from-orange-400 to-amber-500" },
            // Glow colors (gradient + shadow)
            { variant: "glow", color: "primary", className: "bg-gradient-to-r from-primary-500 to-primary-600 shadow-glow-primary" },
            { variant: "glow", color: "success", className: "bg-gradient-to-r from-emerald-500 to-green-500 shadow-glow-success" },
            { variant: "glow", color: "warning", className: "bg-gradient-to-r from-amber-400 to-orange-500 shadow-glow-warning" },
            { variant: "glow", color: "info", className: "bg-gradient-to-r from-blue-400 to-cyan-500 shadow-glow-info" },
            { variant: "glow", color: "xp", className: "bg-gradient-to-r from-orange-400 to-amber-500 shadow-glow-warning" },
        ],
        defaultVariants: {
            variant: "gradient",
            color: "auto",
        },
    }
)

/* ============================================================================
   PROGRESS BAR COMPONENT
   ============================================================================ */

export interface ProgressBarProps
    extends Omit<React.HTMLAttributes<HTMLDivElement>, "color">,
    VariantProps<typeof progressBarContainerVariants>,
    Omit<VariantProps<typeof progressBarFillVariants>, "color"> {
    /**
     * Progress value (0-100)
     */
    value: number
    /**
     * Show percentage label
     */
    showLabel?: boolean
    /**
     * Animate the fill on mount
     */
    animated?: boolean
    /**
     * Color theme - "auto" picks based on value
     */
    color?: "auto" | "primary" | "success" | "warning" | "info" | "xp"
    /**
     * Custom label formatter
     */
    formatLabel?: (value: number) => string
    /**
     * Accessible label for screen readers
     */
    ariaLabel?: string
}

export function ProgressBar({
    value,
    className,
    size = "md",
    variant = "gradient",
    color = "auto",
    showLabel = true,
    animated = true,
    formatLabel,
    ariaLabel,
    ...props
}: ProgressBarProps) {
    // Clamp value between 0 and 100
    const clampedValue = Math.max(0, Math.min(100, value))

    // Determine effective color based on value
    const effectiveColor = React.useMemo(() => {
        if (color !== "auto") return color
        if (clampedValue >= 80) return "success"
        if (clampedValue >= 50) return "warning"
        if (clampedValue > 0) return "info"
        return "primary"
    }, [color, clampedValue])

    // Label size mapping
    const labelSizeClasses = {
        xs: "text-2xs",
        sm: "text-xs",
        md: "text-sm",
        lg: "text-base",
        xl: "text-lg",
    }

    // Format the label
    const label = formatLabel ? formatLabel(clampedValue) : `${clampedValue}%`

    return (
        <div className={cn("w-full", className)} {...props}>
            <div className="flex items-center gap-2">
                {/* Progress track */}
                <div
                    className={cn(progressBarContainerVariants({ size }))}
                    role="progressbar"
                    aria-valuenow={clampedValue}
                    aria-valuemin={0}
                    aria-valuemax={100}
                    aria-label={ariaLabel || `Progress: ${clampedValue}%`}
                >
                    {/* Progress fill */}
                    <div
                        className={cn(
                            progressBarFillVariants({ variant, color: effectiveColor }),
                            animated && "animate-progress-fill"
                        )}
                        style={{ width: `${clampedValue}%` }}
                    >
                        {/* Shimmer overlay for gradient variant */}
                        {(variant === "gradient" || variant === "glow") && (
                            <div
                                className="w-full h-full animate-shimmer opacity-30"
                                aria-hidden="true"
                            />
                        )}
                    </div>
                </div>

                {/* Label */}
                {showLabel && (
                    <span
                        className={cn(
                            "font-medium",
                            "text-neutral-700",
                            "dark:text-neutral-300",
                            "min-w-[3rem]",
                            "text-right",
                            "tabular-nums",
                            labelSizeClasses[size || "md"]
                        )}
                    >
                        {label}
                    </span>
                )}
            </div>
        </div>
    )
}

/* ============================================================================
   XP PROGRESS BAR — Specialized variant for experience points
   ============================================================================ */

interface XPProgressBarProps extends Omit<ProgressBarProps, "color" | "variant" | "formatLabel" | "value"> {
    currentXP: number
    maxXP: number
    level?: number
}

export function XPProgressBar({
    currentXP,
    maxXP,
    level,
    size = "md",
    showLabel = true,
    ...props
}: XPProgressBarProps) {
    const percentage = maxXP > 0 ? (currentXP / maxXP) * 100 : 0

    return (
        <div className="space-y-1">
            {level !== undefined && (
                <div className="flex justify-between text-sm">
                    <span className="font-semibold text-accent-xp">Level {level}</span>
                    <span className="text-neutral-500 dark:text-neutral-400">
                        {currentXP.toLocaleString()} / {maxXP.toLocaleString()} XP
                    </span>
                </div>
            )}
            <ProgressBar
                value={percentage}
                size={size}
                variant="glow"
                color="xp"
                showLabel={showLabel}
                formatLabel={(v) => `${Math.round(v)}%`}
                {...props}
            />
        </div>
    )
}
