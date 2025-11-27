"use client"

/**
 * Skeleton Component
 * Phase D.1: Apple-Inspired Loading States
 * 
 * Features:
 * - Multiple preset variants
 * - Smooth shimmer animation
 * - Dark mode support
 * - Accessible (aria-busy)
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { cva, type VariantProps } from "class-variance-authority"

/* ============================================================================
   SKELETON VARIANTS
   ============================================================================ */

const skeletonVariants = cva(
    // Base: Shimmer animation with gradient
    [
        "relative",
        "overflow-hidden",
        "bg-neutral-200",
        "dark:bg-neutral-700",
        // Shimmer effect
        "before:absolute",
        "before:inset-0",
        "before:-translate-x-full",
        "before:animate-[shimmer_2s_infinite]",
        "before:bg-gradient-to-r",
        "before:from-transparent",
        "before:via-white/40",
        "before:to-transparent",
        "dark:before:via-white/10",
    ],
    {
        variants: {
            /**
             * Pre-defined size variants
             */
            variant: {
                text: "h-4 w-full",
                title: "h-6 w-3/4",
                subtitle: "h-5 w-1/2",
                avatar: "h-10 w-10",
                "avatar-sm": "h-8 w-8",
                "avatar-lg": "h-14 w-14",
                card: "h-32 w-full",
                button: "h-10 w-24",
                badge: "h-6 w-16",
                icon: "h-5 w-5",
                custom: "",
            },

            /**
             * Border radius options
             */
            rounded: {
                none: "rounded-none",
                sm: "rounded-sm",
                md: "rounded-md",
                lg: "rounded-lg",
                xl: "rounded-xl",
                full: "rounded-full",
            },

            /**
             * Animation control
             */
            animate: {
                true: "",
                false: "before:hidden",
            },
        },
        compoundVariants: [
            // Avatar variants should be circular
            { variant: "avatar", rounded: undefined, className: "rounded-full" },
            { variant: "avatar-sm", rounded: undefined, className: "rounded-full" },
            { variant: "avatar-lg", rounded: undefined, className: "rounded-full" },
            // Icon should be rounded
            { variant: "icon", rounded: undefined, className: "rounded-md" },
            // Badge should be pill-shaped
            { variant: "badge", rounded: undefined, className: "rounded-full" },
        ],
        defaultVariants: {
            variant: "custom",
            rounded: "md",
            animate: true,
        },
    }
)

/* ============================================================================
   SKELETON COMPONENT
   ============================================================================ */

export interface SkeletonProps
    extends React.HTMLAttributes<HTMLDivElement>,
        VariantProps<typeof skeletonVariants> {
    /**
     * Custom width (number = px, string = CSS value)
     */
    width?: string | number
    /**
     * Custom height (number = px, string = CSS value)
     */
    height?: string | number
}

export function Skeleton({
    className,
    variant,
    rounded,
    animate = true,
    width,
    height,
    style,
    ...props
}: SkeletonProps) {
    const computedStyle: React.CSSProperties = {
        ...style,
        ...(width !== undefined && {
            width: typeof width === "number" ? `${width}px` : width,
        }),
        ...(height !== undefined && {
            height: typeof height === "number" ? `${height}px` : height,
        }),
    }

    return (
        <div
            className={cn(skeletonVariants({ variant, rounded, animate }), className)}
            style={computedStyle}
            aria-busy="true"
            aria-label="Loading..."
            {...props}
        />
    )
}

/* ============================================================================
   PRE-BUILT SKELETON COMPOSITIONS
   ============================================================================ */

/**
 * Generic card skeleton
 */
export function SkeletonCard({ className }: { className?: string }) {
    return (
        <div className={cn("rounded-xl border border-neutral-200 dark:border-neutral-700 bg-white dark:bg-neutral-800 p-5", className)}>
            <div className="flex items-center justify-between mb-4">
                <Skeleton variant="title" width="40%" />
                <Skeleton variant="badge" />
            </div>
            <div className="space-y-3">
                <Skeleton variant="text" />
                <Skeleton variant="text" width="80%" />
                <Skeleton variant="text" width="60%" />
            </div>
        </div>
    )
}

/**
 * Statistics card skeleton
 */
export function SkeletonStatCard({ className }: { className?: string }) {
    return (
        <div className={cn("rounded-xl border border-neutral-200 dark:border-neutral-700 bg-white dark:bg-neutral-800 p-5", className)}>
            <Skeleton variant="text" width="50%" className="mb-3" />
            <Skeleton height={36} width={72} className="mb-2" rounded="lg" />
            <Skeleton height={12} width="40%" />
        </div>
    )
}

/**
 * List item skeleton
 */
export function SkeletonListItem({ className }: { className?: string }) {
    return (
        <div className={cn("flex items-center gap-3 p-3 rounded-lg bg-neutral-50 dark:bg-neutral-800/50", className)}>
            <Skeleton variant="avatar" />
            <div className="flex-1 space-y-2">
                <Skeleton variant="text" width="60%" />
                <Skeleton height={12} width="40%" />
            </div>
            <Skeleton variant="badge" />
        </div>
    )
}

/**
 * Progress card skeleton with multiple items
 */
export function SkeletonProgressCard({ className }: { className?: string }) {
    return (
        <div className={cn("rounded-xl border border-neutral-200 dark:border-neutral-700 bg-white dark:bg-neutral-800 p-5", className)}>
            <div className="flex items-center justify-between mb-4">
                <Skeleton variant="title" width="50%" />
                <Skeleton variant="icon" />
            </div>
            <div className="space-y-4">
                {[1, 2, 3].map((i) => (
                    <div key={i} className="p-3 rounded-lg bg-neutral-50 dark:bg-neutral-800/50">
                        <div className="flex items-center justify-between mb-2">
                            <Skeleton variant="text" width="30%" />
                            <Skeleton variant="badge" />
                        </div>
                        <Skeleton height={8} rounded="full" />
                    </div>
                ))}
            </div>
        </div>
    )
}

/**
 * Header/Hero skeleton
 */
export function SkeletonHeader({ className }: { className?: string }) {
    return (
        <div
            className={cn(
                "rounded-2xl p-6",
                "bg-gradient-to-br from-neutral-100 to-neutral-50",
                "dark:from-neutral-800 dark:to-neutral-900",
                className
            )}
        >
            <div className="flex items-center gap-4 mb-6">
                <Skeleton variant="avatar-lg" />
                <div className="space-y-2">
                    <Skeleton variant="title" width={200} />
                    <Skeleton variant="subtitle" width={150} />
                </div>
            </div>
            <div className="grid grid-cols-3 gap-4">
                {[1, 2, 3].map((i) => (
                    <div key={i} className="text-center">
                        <Skeleton height={32} width={48} className="mx-auto mb-2" rounded="lg" />
                        <Skeleton height={12} width={60} className="mx-auto" />
                    </div>
                ))}
            </div>
        </div>
    )
}

/**
 * Table row skeleton
 */
export function SkeletonTableRow({ columns = 4, className }: { columns?: number; className?: string }) {
    return (
        <div className={cn("flex items-center gap-4 py-3 px-4", className)}>
            {Array.from({ length: columns }).map((_, i) => (
                <Skeleton 
                    key={i} 
                    variant="text" 
                    width={i === 0 ? "30%" : i === columns - 1 ? "15%" : "20%"} 
                />
            ))}
        </div>
    )
}

/**
 * Navigation skeleton
 */
export function SkeletonNav({ items = 5, className }: { items?: number; className?: string }) {
    return (
        <div className={cn("flex items-center gap-2", className)}>
            {Array.from({ length: items }).map((_, i) => (
                <Skeleton key={i} height={36} width={80 + Math.random() * 40} rounded="lg" />
            ))}
        </div>
    )
}
