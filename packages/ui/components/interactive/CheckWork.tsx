"use client"

/**
 * ============================================================================
 * CHECK WORK COMPONENT — Design System v1.0
 * ============================================================================
 *
 * "Verify you did it right" block with verification command,
 * success criteria, and failure hints.
 *
 * @example
 * <CheckWork
 *   verifyCommand="docker --version"
 *   successCriteria={[
 *     "Output shows Docker version 20.10 or higher",
 *     "No error messages displayed",
 *   ]}
 *   failureHints={[
 *     "Make sure Docker is installed",
 *     "Try restarting your terminal",
 *   ]}
 * />
 *
 * @design PHASE 3 — Hands-On, Labs, Exercises & Interactive Components
 */

import * as React from 'react'
import { cn } from '../utils'
import { TerminalBlock } from './TerminalBlock'

export interface CheckWorkProps {
    /** Command to verify completion */
    verifyCommand: string
    /** List of success criteria */
    successCriteria: string[]
    /** Optional failure hints */
    failureHints?: string[]
    /** Additional CSS classes */
    className?: string
}

export function CheckWork({
    verifyCommand,
    successCriteria,
    failureHints,
    className,
}: CheckWorkProps) {
    return (
        <div
            className={cn(
                // Base card
                "relative rounded-2xl",
                "bg-emerald-50/50 dark:bg-emerald-950/20",
                "border border-emerald-200/50 dark:border-emerald-800/50",
                // Padding
                "p-6",
                className
            )}
        >
            {/* Header */}
            <div className="flex items-center gap-3 mb-4">
                <span className="text-2xl">✅</span>
                <h3 className="text-lg font-semibold text-neutral-900 dark:text-white">
                    Check Your Work
                </h3>
            </div>

            {/* Instruction */}
            <p className="text-sm text-neutral-600 dark:text-neutral-400 mb-4">
                Run this command to verify your setup:
            </p>

            {/* Verify Command */}
            <TerminalBlock command={verifyCommand} title="Verify" />

            {/* Success Criteria */}
            <div className="mt-6">
                <h4 className="text-sm font-semibold text-emerald-700 dark:text-emerald-400 mb-2 flex items-center gap-2">
                    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                        <path strokeLinecap="round" strokeLinejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    Expected Results
                </h4>
                <ul className="space-y-2">
                    {successCriteria.map((criterion, index) => (
                        <li key={index} className="flex items-start gap-2 text-sm text-neutral-700 dark:text-neutral-300">
                            <span className="text-emerald-500 mt-0.5">•</span>
                            {criterion}
                        </li>
                    ))}
                </ul>
            </div>

            {/* Failure Hints */}
            {failureHints && failureHints.length > 0 && (
                <div className="mt-6 pt-4 border-t border-emerald-200/50 dark:border-emerald-800/50">
                    <h4 className="text-sm font-semibold text-amber-700 dark:text-amber-400 mb-2 flex items-center gap-2">
                        <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                            <path strokeLinecap="round" strokeLinejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                        </svg>
                        Troubleshooting
                    </h4>
                    <ul className="space-y-2">
                        {failureHints.map((hint, index) => (
                            <li key={index} className="flex items-start gap-2 text-sm text-neutral-600 dark:text-neutral-400">
                                <span className="text-amber-500 mt-0.5">→</span>
                                {hint}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    )
}

export default CheckWork
