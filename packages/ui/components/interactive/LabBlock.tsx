"use client"

/**
 * ============================================================================
 * LAB BLOCK COMPONENT — Design System v1.0
 * ============================================================================
 *
 * Larger guided labs with title, estimated time, and step sequence.
 * Perfect for comprehensive hands-on exercises.
 *
 * @example
 * <LabBlock
 *   title="Build Your First Container"
 *   minutes={20}
 *   steps={[
 *     { title: "Create Dockerfile", code: "FROM node:18" },
 *     { title: "Build Image", code: "docker build -t app ." },
 *   ]}
 * />
 *
 * @design PHASE 3 — Hands-On, Labs, Exercises & Interactive Components
 */

import * as React from 'react'
import { cn } from '../utils'
import { StepSequence, type StepSequenceStep } from './StepSequence'

export interface LabBlockProps {
    /** Lab title */
    title: string
    /** Estimated time in minutes */
    minutes: number
    /** Array of steps */
    steps: StepSequenceStep[]
    /** Additional CSS classes */
    className?: string
}

export function LabBlock({
    title,
    minutes,
    steps,
    className,
}: LabBlockProps) {
    return (
        <div
            className={cn(
                // Base card
                "relative rounded-2xl",
                "bg-white dark:bg-neutral-900",
                "border border-neutral-200 dark:border-neutral-800",
                "shadow-lg",
                // Overflow hidden for header
                "overflow-hidden",
                className
            )}
        >
            {/* Header */}
            <div
                className={cn(
                    "px-6 py-4",
                    "bg-gradient-to-r from-indigo-500 to-purple-500",
                    "text-white"
                )}
            >
                <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                        {/* Lab Icon */}
                        <span className="text-2xl">🧪</span>
                        {/* Title */}
                        <h3 className="text-lg font-bold">{title}</h3>
                    </div>

                    {/* Time Badge */}
                    <div
                        className={cn(
                            "flex items-center gap-1.5",
                            "px-3 py-1 rounded-full",
                            "bg-white/20 backdrop-blur-sm",
                            "text-sm font-medium"
                        )}
                    >
                        <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                            <path strokeLinecap="round" strokeLinejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        {minutes} min
                    </div>
                </div>
            </div>

            {/* Steps */}
            <div className="p-6">
                <StepSequence steps={steps} />
            </div>
        </div>
    )
}

export default LabBlock
