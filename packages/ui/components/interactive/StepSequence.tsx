"use client"

/**
 * ============================================================================
 * STEP SEQUENCE COMPONENT — Design System v1.0
 * ============================================================================
 *
 * Renders an entire sequence of StepBox components with connecting lines.
 *
 * @example
 * <StepSequence
 *   steps={[
 *     { title: "Install Docker", description: "..." },
 *     { title: "Create Dockerfile", code: "FROM node:18" },
 *     { title: "Build Image", code: "docker build -t myapp ." },
 *   ]}
 * />
 *
 * @design PHASE 3 — Hands-On, Labs, Exercises & Interactive Components
 */

import * as React from 'react'
import { cn } from '../utils'
import { StepBox, type StepBoxProps } from './StepBox'

export interface StepSequenceStep {
    /** Step title */
    title: string
    /** Optional description */
    description?: string
    /** Optional code snippet */
    code?: string
    /** Code language */
    language?: string
}

export interface StepSequenceProps {
    /** Array of steps */
    steps: StepSequenceStep[]
    /** Current active step (0-indexed) */
    activeStep?: number
    /** Completed steps (0-indexed) */
    completedSteps?: number[]
    /** Additional CSS classes */
    className?: string
}

export function StepSequence({
    steps,
    activeStep,
    completedSteps = [],
    className,
}: StepSequenceProps) {
    return (
        <div className={cn("relative", className)}>
            {/* Vertical connector line */}
            <div
                className={cn(
                    "absolute left-3 top-3 bottom-3",
                    "w-px",
                    "bg-neutral-200 dark:bg-neutral-700"
                )}
            />

            {/* Steps */}
            <div className="space-y-0">
                {steps.map((step, index) => (
                    <StepBox
                        key={index}
                        step={index + 1}
                        title={step.title}
                        description={step.description}
                        code={step.code}
                        language={step.language}
                        isActive={activeStep === index}
                        isCompleted={completedSteps.includes(index)}
                    />
                ))}
            </div>
        </div>
    )
}

export default StepSequence
