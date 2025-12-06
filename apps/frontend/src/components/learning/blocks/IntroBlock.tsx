"use client"

/**
 * ============================================================================
 * INTRO BLOCK - Learning objectives and overview
 * ============================================================================
 * 
 * Displays the intro section with:
 * - Attention-grabbing headline
 * - Hook (why this matters)
 * - Learning objectives
 * - Prerequisites
 * - Estimated time
 */

import { cn } from "@saas/ui"
import { 
    Target, 
    Clock, 
    CheckCircle2,
    AlertCircle,
    Lightbulb 
} from "lucide-react"

interface IntroBlockProps {
    headline: string
    hook: string
    learningObjectives: string[]
    prerequisites?: string[]
    estimatedMinutes?: number
}

export function IntroBlock({
    headline,
    hook,
    learningObjectives,
    prerequisites,
    estimatedMinutes = 30
}: IntroBlockProps) {
    return (
        <div className="space-y-6">
            {/* Headline */}
            <div className="text-center mb-8">
                <h1 className="text-3xl md:text-4xl font-bold text-white mb-4">
                    {headline}
                </h1>
                <p className="text-lg text-zinc-300 max-w-2xl mx-auto">
                    {hook}
                </p>
            </div>

            {/* Time estimate */}
            <div className="flex items-center justify-center gap-2 text-zinc-400">
                <Clock className="w-5 h-5" />
                <span>Beräknad tid: {estimatedMinutes} minuter</span>
            </div>

            {/* Learning objectives */}
            <div className={cn(
                "bg-purple-900/20 border border-purple-500/30",
                "rounded-xl p-6"
            )}>
                <div className="flex items-center gap-2 mb-4">
                    <Target className="w-5 h-5 text-purple-400" />
                    <h2 className="text-lg font-semibold text-white">
                        Efter denna lektion kan du
                    </h2>
                </div>
                <ul className="space-y-3">
                    {learningObjectives.map((objective, index) => (
                        <li 
                            key={index}
                            className="flex items-start gap-3"
                        >
                            <CheckCircle2 className="w-5 h-5 text-purple-400 flex-shrink-0 mt-0.5" />
                            <span className="text-zinc-300">{objective}</span>
                        </li>
                    ))}
                </ul>
            </div>

            {/* Prerequisites */}
            {prerequisites && prerequisites.length > 0 && (
                <div className={cn(
                    "bg-amber-900/20 border border-amber-500/30",
                    "rounded-xl p-6"
                )}>
                    <div className="flex items-center gap-2 mb-4">
                        <AlertCircle className="w-5 h-5 text-amber-400" />
                        <h2 className="text-lg font-semibold text-white">
                            Förutsättningar
                        </h2>
                    </div>
                    <ul className="space-y-2">
                        {prerequisites.map((prereq, index) => (
                            <li 
                                key={index}
                                className="flex items-start gap-3"
                            >
                                <Lightbulb className="w-4 h-4 text-amber-400 flex-shrink-0 mt-1" />
                                <span className="text-zinc-300">{prereq}</span>
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    )
}

export default IntroBlock
