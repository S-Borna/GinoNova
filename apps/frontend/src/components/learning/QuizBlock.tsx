"use client"

/**
 * ============================================================================
 * QUIZ BLOCK COMPONENT - Interactive Multiple Choice Questions
 * ============================================================================
 *
 * Features:
 * - Radio buttons for options
 * - Submit button
 * - Correct/incorrect feedback
 * - Explanation after answering
 * - XP bonus display
 * - Disabled state after answering
 *
 * @phase ILE Phase 3 - Content Blocks
 */

import * as React from "react"
import { useState } from "react"
import { cn } from "@/lib/utils"
import { HelpCircle, CheckCircle2, XCircle, Sparkles, Lock } from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface QuizOption {
    text: string
    isCorrect: boolean
    feedback?: string
}

export interface QuizBlockProps {
    blockId: string
    question: string
    options: QuizOption[]
    explanation: string
    xpBonus?: number
    answered?: {
        selectedOption: number
        isCorrect: boolean
    }
    onAnswer: (blockId: string, optionIndex: number) => void
    className?: string
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function QuizBlock({
    blockId,
    question,
    options,
    explanation,
    xpBonus = 5,
    answered,
    onAnswer,
    className,
}: QuizBlockProps) {
    const [selectedOption, setSelectedOption] = useState<number | null>(
        answered?.selectedOption ?? null
    )
    const [hasSubmitted, setHasSubmitted] = useState(!!answered)
    const [isCorrect, setIsCorrect] = useState(answered?.isCorrect ?? false)

    const handleSubmit = () => {
        if (selectedOption === null || hasSubmitted) return

        const option = options[selectedOption]
        const correct = option.isCorrect

        setIsCorrect(correct)
        setHasSubmitted(true)
        onAnswer(blockId, selectedOption)
    }

    return (
        <div className={cn(
            "rounded-xl overflow-hidden border my-4",
            hasSubmitted
                ? isCorrect
                    ? "border-green-500/50 bg-green-500/5"
                    : "border-red-500/50 bg-red-500/5"
                : "border-neutral-800 bg-neutral-900/50",
            className
        )}>
            {/* Header */}
            <div className={cn(
                "flex items-center gap-3 px-4 py-3 border-b",
                hasSubmitted
                    ? isCorrect
                        ? "bg-green-500/10 border-green-500/30"
                        : "bg-red-500/10 border-red-500/30"
                    : "bg-neutral-800/50 border-neutral-800"
            )}>
                <div className={cn(
                    "p-2 rounded-lg",
                    hasSubmitted
                        ? isCorrect
                            ? "bg-green-500/20"
                            : "bg-red-500/20"
                        : "bg-primary-500/20"
                )}>
                    {hasSubmitted ? (
                        isCorrect ? (
                            <CheckCircle2 className="h-5 w-5 text-green-400" />
                        ) : (
                            <XCircle className="h-5 w-5 text-red-400" />
                        )
                    ) : (
                        <HelpCircle className="h-5 w-5 text-primary-400" />
                    )}
                </div>
                <div className="flex-1">
                    <span className="text-xs font-medium text-neutral-400 uppercase tracking-wide">
                        Quiz Question
                    </span>
                    {xpBonus > 0 && !hasSubmitted && (
                        <span className="ml-2 text-xs text-yellow-400">
                            +{xpBonus} XP
                        </span>
                    )}
                </div>
                {hasSubmitted && isCorrect && xpBonus > 0 && (
                    <div className="flex items-center gap-1 px-2 py-1 bg-yellow-500/20 rounded-md">
                        <Sparkles className="h-3.5 w-3.5 text-yellow-400" />
                        <span className="text-xs font-medium text-yellow-400">+{xpBonus} XP</span>
                    </div>
                )}
            </div>

            {/* Question */}
            <div className="px-4 py-4">
                <p className="text-lg font-medium text-white mb-4">
                    {question}
                </p>

                {/* Options */}
                <div className="space-y-2">
                    {options.map((option, index) => {
                        const isSelected = selectedOption === index
                        const showResult = hasSubmitted

                        return (
                            <label
                                key={index}
                                className={cn(
                                    "flex items-start gap-3 p-3 rounded-lg cursor-pointer transition-all",
                                    hasSubmitted && "cursor-default",
                                    !hasSubmitted && isSelected && "bg-primary-500/20 border border-primary-500/50",
                                    !hasSubmitted && !isSelected && "bg-neutral-800/50 border border-transparent hover:bg-neutral-800",
                                    showResult && option.isCorrect && "bg-green-500/20 border border-green-500/50",
                                    showResult && isSelected && !option.isCorrect && "bg-red-500/20 border border-red-500/50",
                                    showResult && !isSelected && !option.isCorrect && "bg-neutral-800/30 border border-transparent opacity-60"
                                )}
                            >
                                <input
                                    type="radio"
                                    name={`quiz-${blockId}`}
                                    checked={isSelected}
                                    onChange={() => !hasSubmitted && setSelectedOption(index)}
                                    disabled={hasSubmitted}
                                    className="sr-only"
                                />
                                <div className={cn(
                                    "w-5 h-5 rounded-full border-2 flex items-center justify-center flex-shrink-0 mt-0.5",
                                    !hasSubmitted && isSelected && "border-primary-500 bg-primary-500",
                                    !hasSubmitted && !isSelected && "border-neutral-600",
                                    showResult && option.isCorrect && "border-green-500 bg-green-500",
                                    showResult && isSelected && !option.isCorrect && "border-red-500 bg-red-500",
                                    showResult && !isSelected && !option.isCorrect && "border-neutral-700"
                                )}>
                                    {((isSelected && !hasSubmitted) || (showResult && option.isCorrect) || (showResult && isSelected)) && (
                                        <div className="w-2 h-2 rounded-full bg-white" />
                                    )}
                                </div>
                                <div className="flex-1">
                                    <span className={cn(
                                        "text-sm",
                                        showResult && option.isCorrect && "text-green-300 font-medium",
                                        showResult && isSelected && !option.isCorrect && "text-red-300",
                                        !showResult && "text-neutral-200"
                                    )}>
                                        {option.text}
                                    </span>
                                    {showResult && isSelected && option.feedback && (
                                        <p className={cn(
                                            "text-xs mt-1",
                                            option.isCorrect ? "text-green-400" : "text-red-400"
                                        )}>
                                            {option.feedback}
                                        </p>
                                    )}
                                </div>
                                {showResult && option.isCorrect && (
                                    <CheckCircle2 className="h-5 w-5 text-green-400 flex-shrink-0" />
                                )}
                                {showResult && isSelected && !option.isCorrect && (
                                    <XCircle className="h-5 w-5 text-red-400 flex-shrink-0" />
                                )}
                            </label>
                        )
                    })}
                </div>

                {/* Submit Button */}
                {!hasSubmitted && (
                    <button
                        onClick={handleSubmit}
                        disabled={selectedOption === null}
                        className={cn(
                            "mt-4 w-full py-2.5 rounded-lg font-medium transition-colors",
                            selectedOption !== null
                                ? "bg-primary-600 hover:bg-primary-500 text-white"
                                : "bg-neutral-800 text-neutral-500 cursor-not-allowed"
                        )}
                    >
                        Submit Answer
                    </button>
                )}

                {/* Explanation */}
                {hasSubmitted && (
                    <div className={cn(
                        "mt-4 p-3 rounded-lg",
                        isCorrect ? "bg-green-500/10" : "bg-neutral-800/50"
                    )}>
                        <p className="text-sm font-medium text-neutral-300 mb-1">
                            Explanation:
                        </p>
                        <p className="text-sm text-neutral-400">
                            {explanation}
                        </p>
                    </div>
                )}
            </div>
        </div>
    )
}

export default QuizBlock
