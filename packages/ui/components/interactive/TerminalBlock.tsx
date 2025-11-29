"use client"

/**
 * ============================================================================
 * TERMINAL BLOCK COMPONENT — Design System v1.0
 * ============================================================================
 *
 * Simulated terminal environment for commands.
 * Dark background, monospace font, copy button.
 *
 * @example
 * <TerminalBlock command="docker ps -a" />
 * <TerminalBlock command={["cd project", "npm install", "npm start"]} />
 *
 * @design PHASE 3 — Hands-On, Labs, Exercises & Interactive Components
 */

import * as React from 'react'
import { cn } from '../utils'

export interface TerminalBlockProps {
    /** Single command or array of commands */
    command: string | string[]
    /** Show line numbers */
    showLineNumbers?: boolean
    /** Terminal title */
    title?: string
    /** Additional CSS classes */
    className?: string
}

export function TerminalBlock({
    command,
    showLineNumbers = false,
    title = "Terminal",
    className,
}: TerminalBlockProps) {
    const [copied, setCopied] = React.useState(false)
    const commands = Array.isArray(command) ? command : [command]
    const fullCommand = commands.join('\n')

    const handleCopy = async () => {
        try {
            await navigator.clipboard.writeText(fullCommand)
            setCopied(true)
            setTimeout(() => setCopied(false), 2000)
        } catch (err) {
            console.error('Failed to copy:', err)
        }
    }

    return (
        <div
            className={cn(
                // Base
                "relative rounded-xl overflow-hidden",
                "bg-[#0D1117]",
                "border border-neutral-800",
                "shadow-lg",
                className
            )}
        >
            {/* Header Bar */}
            <div
                className={cn(
                    "flex items-center justify-between",
                    "px-4 py-2",
                    "bg-neutral-900",
                    "border-b border-neutral-800"
                )}
            >
                {/* Window buttons */}
                <div className="flex items-center gap-2">
                    <div className="w-3 h-3 rounded-full bg-red-500" />
                    <div className="w-3 h-3 rounded-full bg-yellow-500" />
                    <div className="w-3 h-3 rounded-full bg-green-500" />
                </div>

                {/* Title */}
                <span className="text-xs text-neutral-500 font-medium">
                    {title}
                </span>

                {/* Copy Button */}
                <button
                    onClick={handleCopy}
                    className={cn(
                        "flex items-center gap-1.5",
                        "px-2 py-1 rounded",
                        "text-xs font-medium",
                        "transition-colors duration-200",
                        copied
                            ? "text-emerald-400 bg-emerald-500/10"
                            : "text-neutral-400 hover:text-white hover:bg-neutral-800"
                    )}
                >
                    {copied ? (
                        <>
                            <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                                <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                            </svg>
                            Copied!
                        </>
                    ) : (
                        <>
                            <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                                <path strokeLinecap="round" strokeLinejoin="round" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                            </svg>
                            Copy
                        </>
                    )}
                </button>
            </div>

            {/* Terminal Content */}
            <div className="p-4 overflow-x-auto">
                <div className="font-mono text-sm">
                    {commands.map((cmd, index) => (
                        <div key={index} className="flex">
                            {showLineNumbers && (
                                <span className="select-none text-neutral-600 w-8 flex-shrink-0">
                                    {index + 1}
                                </span>
                            )}
                            <span className="text-emerald-400 select-none mr-2">$</span>
                            <span className="text-neutral-100">{cmd}</span>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default TerminalBlock
