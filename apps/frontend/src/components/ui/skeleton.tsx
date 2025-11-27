"use client"

/**
 * Skeleton Component
 * Phase 6.3: Reusable loading skeleton states
 */

import * as React from "react"
import { cn } from "@/lib/utils"

interface SkeletonProps extends React.HTMLAttributes<HTMLDivElement> {
    variant?: "text" | "title" | "avatar" | "card" | "button" | "custom"
    width?: string | number
    height?: string | number
    rounded?: "none" | "sm" | "md" | "lg" | "full"
    animate?: boolean
}

export function Skeleton({
    className,
    variant = "custom",
    width,
    height,
    rounded = "md",
    animate = true,
    style,
    ...props
}: SkeletonProps) {
    const variantStyles: Record<string, React.CSSProperties> = {
        text: { height: '1rem', width: '100%' },
        title: { height: '1.5rem', width: '75%' },
        avatar: { height: '2.5rem', width: '2.5rem' },
        card: { height: '8rem', width: '100%' },
        button: { height: '2.5rem', width: '6rem' },
        custom: {},
    }

    const roundedClasses = {
        none: "",
        sm: "rounded-sm",
        md: "rounded-md",
        lg: "rounded-lg",
        full: "rounded-full",
    }

    return (
        <div
            className={cn(
                "skeleton",
                animate && "animate-pulse",
                roundedClasses[rounded],
                className
            )}
            style={{
                ...variantStyles[variant],
                width: width ? (typeof width === "number" ? `${width}px` : width) : variantStyles[variant].width,
                height: height ? (typeof height === "number" ? `${height}px` : height) : variantStyles[variant].height,
                ...style,
            }}
            {...props}
        />
    )
}

// Pre-built skeleton compositions for common UI patterns
export function SkeletonCard({ className }: { className?: string }) {
    return (
        <div className={cn("dashboard-card p-5", className)}>
            <div className="flex items-center justify-between mb-4">
                <Skeleton variant="title" width="40%" />
                <Skeleton width={32} height={24} rounded="full" />
            </div>
            <div className="space-y-3">
                <Skeleton variant="text" />
                <Skeleton variant="text" width="80%" />
                <Skeleton variant="text" width="60%" />
            </div>
        </div>
    )
}

export function SkeletonStatCard({ className }: { className?: string }) {
    return (
        <div className={cn("dashboard-card p-5", className)}>
            <Skeleton variant="text" width="50%" className="mb-3" />
            <Skeleton height={36} width={56} className="mb-2" />
            <Skeleton variant="text" width="40%" height={10} />
        </div>
    )
}

export function SkeletonListItem({ className }: { className?: string }) {
    return (
        <div className={cn("flex items-center gap-3 p-3 rounded-lg", className)} style={{ background: 'var(--secondary)' }}>
            <Skeleton variant="avatar" rounded="lg" />
            <div className="flex-1 space-y-2">
                <Skeleton variant="text" width="60%" />
                <Skeleton variant="text" width="40%" height={12} />
            </div>
            <Skeleton width={60} height={24} rounded="full" />
        </div>
    )
}

export function SkeletonProgressCard({ className }: { className?: string }) {
    return (
        <div className={cn("dashboard-card p-5", className)}>
            <div className="flex items-center justify-between mb-4">
                <Skeleton variant="title" width="50%" />
                <Skeleton width={32} height={24} rounded="full" />
            </div>
            <div className="space-y-4">
                {[1, 2, 3].map((i) => (
                    <div key={i} className="p-3 rounded-lg" style={{ background: 'var(--secondary)' }}>
                        <div className="flex items-center justify-between mb-2">
                            <Skeleton variant="text" width="30%" />
                            <Skeleton width={60} height={20} rounded="full" />
                        </div>
                        <Skeleton height={8} rounded="full" />
                    </div>
                ))}
            </div>
        </div>
    )
}

export function SkeletonHeader({ className }: { className?: string }) {
    return (
        <div
            className={cn("rounded-2xl p-6", className)}
            style={{ background: 'linear-gradient(to right, var(--muted), var(--secondary))' }}
        >
            <div className="flex items-center gap-4 mb-6">
                <Skeleton variant="avatar" width={56} height={56} rounded="full" />
                <div className="space-y-2">
                    <Skeleton height={24} width={200} />
                    <Skeleton height={14} width={150} />
                </div>
            </div>
            <div className="grid grid-cols-3 gap-4">
                {[1, 2, 3].map((i) => (
                    <div key={i} className="text-center">
                        <Skeleton height={32} width={48} className="mx-auto mb-2" />
                        <Skeleton height={12} width={60} className="mx-auto" />
                    </div>
                ))}
            </div>
        </div>
    )
}
