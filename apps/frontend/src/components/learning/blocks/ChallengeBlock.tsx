"use client"

/**
 * ============================================================================
 * CHALLENGE BLOCK - End-of-node practical challenge
 * ============================================================================
 * 
 * Features:
 * - Real-world scenario description
 * - Requirements checklist
 * - Progressive hints
 * - Collapsible solution
 * - Bonus XP for completion
 */

import { useState } from "react"
import { cn } from "@saas/ui"
import { 
    Trophy, 
    Target,
    CheckCircle2,
    Lightbulb,
    ChevronDown,
    ChevronRight,
    Eye,
    EyeOff,
    Rocket
} from "lucide-react"
import { Button } from "@/components/ui/button"

interface ChallengeBlockProps {
    title: string
    scenario: string
    requirements: string[]
    hints?: string[]
    solution?: string
    xpBonus?: number
    onComplete?: () => void
}

export function ChallengeBlock({
    title,
    scenario,
    requirements,
    hints = [],
    solution,
    xpBonus = 20,
    onComplete
}: ChallengeBlockProps) {
    const [checkedRequirements, setCheckedRequirements] = useState<Set<number>>(new Set())
    const [showHints, setShowHints] = useState(false)
    const [revealedHints, setRevealedHints] = useState(0)
    const [showSolution, setShowSolution] = useState(false)
    const [isCompleted, setIsCompleted] = useState(false)

    const allRequirementsMet = checkedRequirements.size === requirements.length
    const progress = (checkedRequirements.size / requirements.length) * 100

    const toggleRequirement = (index: number) => {
        const newChecked = new Set(checkedRequirements)
        if (newChecked.has(index)) {
            newChecked.delete(index)
        } else {
            newChecked.add(index)
        }
        setCheckedRequirements(newChecked)
    }

    const revealNextHint = () => {
        if (revealedHints < hints.length) {
            setRevealedHints(revealedHints + 1)
        }
    }

    const handleComplete = () => {
        setIsCompleted(true)
        onComplete?.()
    }

    return (
        <div className="space-y-6">
            {/* Header */}
            <div className={cn(
                "bg-gradient-to-r from-amber-900/30 to-orange-900/30",
                "border border-amber-500/30 rounded-xl p-6"
            )}>
                <div className="flex items-center gap-3 mb-4">
                    <div className={cn(
                        "w-12 h-12 rounded-xl",
                        "bg-amber-500/20 flex items-center justify-center"
                    )}>
                        <Trophy className="w-6 h-6 text-amber-400" />
                    </div>
                    <div>
                        <span className="text-xs text-amber-400 font-medium">CHALLENGE</span>
                        <h3 className="text-xl font-bold text-white">{title}</h3>
                    </div>
                    <div className="ml-auto">
                        <span className={cn(
                            "px-3 py-1 rounded-full text-sm font-medium",
                            "bg-amber-500/20 text-amber-400"
                        )}>
                            +{xpBonus} XP bonus
                        </span>
                    </div>
                </div>

                {/* Scenario */}
                <div className="prose prose-invert prose-sm max-w-none">
                    <p className="text-zinc-300 leading-relaxed">{scenario}</p>
                </div>
            </div>

            {/* Progress */}
            <div className="space-y-2">
                <div className="flex items-center justify-between text-sm">
                    <span className="text-zinc-400">Progress</span>
                    <span className="text-zinc-400">
                        {checkedRequirements.size} av {requirements.length} krav uppfyllda
                    </span>
                </div>
                <div className="h-2 bg-zinc-700 rounded-full overflow-hidden">
                    <div 
                        className={cn(
                            "h-full transition-all duration-300",
                            allRequirementsMet ? "bg-emerald-500" : "bg-amber-500"
                        )}
                        style={{ width: `${progress}%` }}
                    />
                </div>
            </div>

            {/* Requirements */}
            <div className={cn(
                "bg-zinc-800/50 border border-zinc-700/50",
                "rounded-xl p-6"
            )}>
                <div className="flex items-center gap-2 mb-4">
                    <Target className="w-5 h-5 text-purple-400" />
                    <h4 className="font-semibold text-white">Krav</h4>
                </div>

                <div className="space-y-3">
                    {requirements.map((req, index) => (
                        <label
                            key={index}
                            className={cn(
                                "flex items-start gap-3 p-3 rounded-lg cursor-pointer",
                                "transition-colors",
                                checkedRequirements.has(index)
                                    ? "bg-emerald-900/20 border border-emerald-500/30"
                                    : "bg-zinc-700/30 border border-transparent hover:border-zinc-600"
                            )}
                        >
                            <input
                                type="checkbox"
                                checked={checkedRequirements.has(index)}
                                onChange={() => toggleRequirement(index)}
                                className="sr-only"
                            />
                            <div className={cn(
                                "w-6 h-6 rounded flex items-center justify-center flex-shrink-0",
                                "border-2 transition-colors",
                                checkedRequirements.has(index)
                                    ? "bg-emerald-500 border-emerald-500"
                                    : "border-zinc-500"
                            )}>
                                {checkedRequirements.has(index) && (
                                    <CheckCircle2 className="w-4 h-4 text-white" />
                                )}
                            </div>
                            <span className={cn(
                                "text-sm",
                                checkedRequirements.has(index)
                                    ? "text-emerald-300 line-through"
                                    : "text-zinc-300"
                            )}>
                                {req}
                            </span>
                        </label>
                    ))}
                </div>
            </div>

            {/* Hints */}
            {hints.length > 0 && (
                <div className={cn(
                    "bg-zinc-800/50 border border-zinc-700/50",
                    "rounded-xl overflow-hidden"
                )}>
                    <button
                        onClick={() => setShowHints(!showHints)}
                        className={cn(
                            "w-full flex items-center justify-between",
                            "p-4 hover:bg-zinc-700/30 transition-colors"
                        )}
                    >
                        <div className="flex items-center gap-2">
                            <Lightbulb className="w-5 h-5 text-amber-400" />
                            <span className="font-medium text-white">Ledtrådar</span>
                            <span className="text-xs text-zinc-500">
                                ({revealedHints} av {hints.length} visade)
                            </span>
                        </div>
                        {showHints ? (
                            <ChevronDown className="w-5 h-5 text-zinc-400" />
                        ) : (
                            <ChevronRight className="w-5 h-5 text-zinc-400" />
                        )}
                    </button>

                    {showHints && (
                        <div className="p-4 pt-0 space-y-3">
                            {hints.slice(0, revealedHints).map((hint, index) => (
                                <div 
                                    key={index}
                                    className={cn(
                                        "bg-amber-900/20 border border-amber-500/30",
                                        "rounded-lg p-3"
                                    )}
                                >
                                    <span className="text-xs text-amber-400 font-medium">
                                        Ledtråd {index + 1}
                                    </span>
                                    <p className="text-sm text-zinc-300 mt-1">{hint}</p>
                                </div>
                            ))}

                            {revealedHints < hints.length && (
                                <Button
                                    variant="outline"
                                    size="sm"
                                    onClick={revealNextHint}
                                    className="text-amber-400 border-amber-500/30"
                                >
                                    <Eye className="w-4 h-4 mr-2" />
                                    Visa nästa ledtråd
                                </Button>
                            )}
                        </div>
                    )}
                </div>
            )}

            {/* Solution */}
            {solution && (
                <div className={cn(
                    "bg-zinc-800/50 border border-zinc-700/50",
                    "rounded-xl overflow-hidden"
                )}>
                    <button
                        onClick={() => setShowSolution(!showSolution)}
                        className={cn(
                            "w-full flex items-center justify-between",
                            "p-4 hover:bg-zinc-700/30 transition-colors"
                        )}
                    >
                        <div className="flex items-center gap-2">
                            {showSolution ? (
                                <EyeOff className="w-5 h-5 text-red-400" />
                            ) : (
                                <Eye className="w-5 h-5 text-zinc-400" />
                            )}
                            <span className="font-medium text-white">Lösning</span>
                            {!showSolution && (
                                <span className="text-xs text-zinc-500">
                                    (försök själv först!)
                                </span>
                            )}
                        </div>
                        {showSolution ? (
                            <ChevronDown className="w-5 h-5 text-zinc-400" />
                        ) : (
                            <ChevronRight className="w-5 h-5 text-zinc-400" />
                        )}
                    </button>

                    {showSolution && (
                        <div className="p-4 pt-0">
                            <pre className={cn(
                                "bg-zinc-900 rounded-lg p-4",
                                "text-sm text-zinc-300 overflow-x-auto",
                                "font-mono"
                            )}>
                                {solution}
                            </pre>
                        </div>
                    )}
                </div>
            )}

            {/* Complete Button */}
            {allRequirementsMet && !isCompleted && (
                <div className="flex justify-center">
                    <Button
                        onClick={handleComplete}
                        className={cn(
                            "bg-gradient-to-r from-amber-600 to-orange-600",
                            "hover:from-amber-500 hover:to-orange-500",
                            "text-white font-semibold px-8 py-3"
                        )}
                    >
                        <Rocket className="w-5 h-5 mr-2" />
                        Slutför Challenge (+{xpBonus} XP)
                    </Button>
                </div>
            )}

            {/* Completed State */}
            {isCompleted && (
                <div className={cn(
                    "bg-emerald-900/20 border border-emerald-500/30",
                    "rounded-xl p-6 text-center"
                )}>
                    <Trophy className="w-12 h-12 text-amber-400 mx-auto mb-3" />
                    <h4 className="text-xl font-bold text-white mb-2">
                        Challenge Slutförd! 🎉
                    </h4>
                    <p className="text-emerald-400 font-medium">
                        +{xpBonus} XP bonus intjänad!
                    </p>
                </div>
            )}
        </div>
    )
}

export default ChallengeBlock
