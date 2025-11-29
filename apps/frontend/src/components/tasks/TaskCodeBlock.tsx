"use client"

/**
 * ============================================================================
 * TASK CODE BLOCK — Material 3 + Tesla Style
 * ============================================================================
 *
 * Code block component with:
 * - Background: #f6f8fa
 * - Border-radius: 12px
 * - Shadow: 0 2px 8px rgba(0,0,0,0.05)
 * - Padding: 20px
 * - Hover brighten effect
 * - Copy button
 * - Language badge
 *
 * @version 2.0
 * @date 2025-11-29
 */

import { useState } from "react"
import { cn } from "@/lib/utils"
import { Check, Copy, Terminal } from "lucide-react"

interface TaskCodeBlockProps {
    code: string
    language?: string
    filename?: string
    showLineNumbers?: boolean
    caption?: string
    className?: string
}

export function TaskCodeBlock({
    code,
    language = "bash",
    filename,
    showLineNumbers = false,
    caption,
    className
}: TaskCodeBlockProps) {
    const [copied, setCopied] = useState(false)

    const handleCopy = async () => {
        try {
            await navigator.clipboard.writeText(code)
            setCopied(true)
            setTimeout(() => setCopied(false), 2000)
        } catch (err) {
            console.error("Failed to copy:", err)
        }
    }

    const lines = code.split("\n")

    return (
        <div className={cn("my-7", className)}>
            {/* Code block container */}
            <div
                className={cn(
                    // Background
                    "bg-[#f6f8fa] dark:bg-[#1e1e1e]",
                    // Border radius
                    "rounded-xl",
                    // Shadow
                    "shadow-[0_2px_8px_rgba(0,0,0,0.05)]",
                    // Overflow
                    "overflow-hidden",
                    // Transition for hover effect
                    "transition-all duration-200",
                    "hover:brightness-[1.02] dark:hover:brightness-110"
                )}
            >
                {/* Header with language/filename */}
                <div className="flex items-center justify-between px-4 py-2.5 border-b border-black/5 dark:border-white/10">
                    <div className="flex items-center gap-2">
                        <Terminal className="w-4 h-4 text-neutral-400" />
                        <span className="text-xs font-medium text-neutral-500 dark:text-neutral-400 uppercase tracking-wider">
                            {filename || language}
                        </span>
                    </div>

                    {/* Copy button */}
                    <button
                        onClick={handleCopy}
                        className={cn(
                            "flex items-center gap-1.5 px-2.5 py-1 rounded-lg",
                            "text-xs font-medium",
                            "transition-all duration-200",
                            copied
                                ? "bg-emerald-100 dark:bg-emerald-900/30 text-emerald-600 dark:text-emerald-400"
                                : "bg-neutral-200/50 dark:bg-neutral-700/50 text-neutral-500 dark:text-neutral-400 hover:bg-neutral-200 dark:hover:bg-neutral-700"
                        )}
                    >
                        {copied ? (
                            <>
                                <Check className="w-3.5 h-3.5" />
                                Copied
                            </>
                        ) : (
                            <>
                                <Copy className="w-3.5 h-3.5" />
                                Copy
                            </>
                        )}
                    </button>
                </div>

                {/* Code content */}
                <div className="p-5 overflow-x-auto">
                    <pre className="text-sm font-mono leading-relaxed">
                        <code className="text-neutral-800 dark:text-neutral-200">
                            {showLineNumbers ? (
                                <table className="border-collapse">
                                    <tbody>
                                        {lines.map((line, i) => (
                                            <tr key={i} className="hover:bg-black/[0.02] dark:hover:bg-white/[0.02]">
                                                <td className="pr-4 text-right text-neutral-400 dark:text-neutral-600 select-none w-8">
                                                    {i + 1}
                                                </td>
                                                <td className="whitespace-pre">{line}</td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            ) : (
                                code
                            )}
                        </code>
                    </pre>
                </div>
            </div>

            {/* Caption below code */}
            {caption && (
                <p className="mt-4 text-sm text-neutral-500 dark:text-neutral-400 leading-relaxed">
                    {caption}
                </p>
            )}
        </div>
    )
}

export default TaskCodeBlock
