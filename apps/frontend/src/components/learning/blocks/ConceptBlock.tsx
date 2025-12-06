"use client"

/**
 * ============================================================================
 * CONCEPT BLOCK - Structured concept explanation
 * ============================================================================
 * 
 * Displays a single concept with:
 * - Title
 * - Explanation (markdown)
 * - Optional ASCII diagram
 * - Pro tip
 * - Common mistake warning
 */

import { useState } from "react"
import ReactMarkdown from "react-markdown"
import remarkGfm from "remark-gfm"
import { cn } from "@saas/ui"
import { 
    Lightbulb, 
    AlertTriangle,
    ChevronDown,
    ChevronRight,
    BookOpen
} from "lucide-react"

interface ConceptBlockProps {
    title: string
    explanation: string
    diagram?: string
    proTip?: string
    commonMistake?: string
    isExpanded?: boolean
}

export function ConceptBlock({
    title,
    explanation,
    diagram,
    proTip,
    commonMistake,
    isExpanded: initialExpanded = true
}: ConceptBlockProps) {
    const [isExpanded, setIsExpanded] = useState(initialExpanded)

    return (
        <div className={cn(
            "bg-zinc-800/50 border border-zinc-700/50",
            "rounded-xl overflow-hidden",
            "transition-all duration-200"
        )}>
            {/* Header */}
            <button
                onClick={() => setIsExpanded(!isExpanded)}
                className={cn(
                    "w-full flex items-center justify-between",
                    "p-4 md:p-6",
                    "hover:bg-zinc-800/80 transition-colors",
                    "text-left"
                )}
            >
                <div className="flex items-center gap-3">
                    <BookOpen className="w-5 h-5 text-purple-400" />
                    <h3 className="text-lg font-semibold text-white">
                        {title}
                    </h3>
                </div>
                {isExpanded ? (
                    <ChevronDown className="w-5 h-5 text-zinc-400" />
                ) : (
                    <ChevronRight className="w-5 h-5 text-zinc-400" />
                )}
            </button>

            {/* Content */}
            {isExpanded && (
                <div className="p-4 md:p-6 pt-0 space-y-6">
                    {/* Explanation */}
                    <div className="prose prose-invert prose-zinc max-w-none">
                        <ReactMarkdown remarkPlugins={[remarkGfm]}>
                            {explanation}
                        </ReactMarkdown>
                    </div>

                    {/* Diagram */}
                    {diagram && (
                        <div className={cn(
                            "bg-zinc-900/80 rounded-lg p-4",
                            "font-mono text-sm text-zinc-300",
                            "overflow-x-auto"
                        )}>
                            <pre className="whitespace-pre">{diagram}</pre>
                        </div>
                    )}

                    {/* Pro Tip */}
                    {proTip && (
                        <div className={cn(
                            "bg-emerald-900/20 border border-emerald-500/30",
                            "rounded-lg p-4",
                            "flex items-start gap-3"
                        )}>
                            <Lightbulb className="w-5 h-5 text-emerald-400 flex-shrink-0 mt-0.5" />
                            <div>
                                <span className="text-sm font-semibold text-emerald-400 block mb-1">
                                    💡 Pro Tip
                                </span>
                                <p className="text-sm text-zinc-300">{proTip}</p>
                            </div>
                        </div>
                    )}

                    {/* Common Mistake */}
                    {commonMistake && (
                        <div className={cn(
                            "bg-red-900/20 border border-red-500/30",
                            "rounded-lg p-4",
                            "flex items-start gap-3"
                        )}>
                            <AlertTriangle className="w-5 h-5 text-red-400 flex-shrink-0 mt-0.5" />
                            <div>
                                <span className="text-sm font-semibold text-red-400 block mb-1">
                                    ⚠️ Vanligt Misstag
                                </span>
                                <p className="text-sm text-zinc-300">{commonMistake}</p>
                            </div>
                        </div>
                    )}
                </div>
            )}
        </div>
    )
}

export default ConceptBlock
