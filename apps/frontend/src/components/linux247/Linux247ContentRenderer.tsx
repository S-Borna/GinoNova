"use client"

/**
 * Linux247ContentRenderer - Premium Content Blocks for Linux 24/7 Module
 * Same design as DOE25ContentRenderer with emerald/teal theme
 */

import * as React from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter"
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism"
import {
    Target,
    Copy,
    Check,
    CheckCircle2,
    XCircle,
    Lightbulb,
    AlertTriangle,
    Sparkles,
    BookOpen,
    Code2,
    HelpCircle
} from "lucide-react"
import type { ContentBlock } from "@/data/linux247-module"

// ============================================================================
// INTRO BLOCK - Learning Objectives
// ============================================================================
function IntroBlock({ block }: { block: ContentBlock }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "relative rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-emerald-500/10 via-teal-500/5 to-transparent",
                "border border-emerald-500/20",
                "p-6"
            )}
        >
            {/* Glow effect */}
            <div className="absolute top-0 left-0 w-32 h-32 bg-emerald-500/20 rounded-full blur-3xl" />

            <div className="relative">
                <div className="flex items-center gap-3 mb-4">
                    <div className={cn(
                        "w-10 h-10 rounded-xl flex items-center justify-center",
                        "bg-gradient-to-br from-emerald-500 to-teal-600",
                        "shadow-lg shadow-emerald-500/25"
                    )}>
                        <Target className="w-5 h-5 text-white" />
                    </div>
                    <h3 className="text-lg font-bold text-white">{block.title}</h3>
                </div>

                <ul className="space-y-2">
                    {block.objectives?.map((objective, i) => (
                        <motion.li
                            key={i}
                            initial={{ opacity: 0, x: -10 }}
                            animate={{ opacity: 1, x: 0 }}
                            transition={{ delay: i * 0.1 }}
                            className="flex items-start gap-3"
                        >
                            <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />
                            <span className="text-zinc-300">{objective}</span>
                        </motion.li>
                    ))}
                </ul>
            </div>
        </motion.div>
    )
}

// ============================================================================
// CONCEPT BLOCK - Explanations
// ============================================================================
function ConceptBlock({ block }: { block: ContentBlock }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "rounded-2xl",
                "bg-zinc-900/50 border border-zinc-800/50",
                "p-6"
            )}
        >
            <div className="flex items-center gap-3 mb-4">
                <div className={cn(
                    "w-9 h-9 rounded-lg flex items-center justify-center",
                    "bg-teal-500/10 border border-teal-500/20"
                )}>
                    <BookOpen className="w-4 h-4 text-teal-400" />
                </div>
                <h3 className="text-lg font-semibold text-white">{block.title}</h3>
            </div>

            <div className="text-zinc-300 leading-relaxed whitespace-pre-line">
                {block.content}
            </div>
        </motion.div>
    )
}

// ============================================================================
// CODE BLOCK - Syntax Highlighted Code
// ============================================================================
function CodeBlockComponent({ block }: { block: ContentBlock }) {
    const [copied, setCopied] = React.useState(false)

    const handleCopy = async () => {
        if (block.code) {
            await navigator.clipboard.writeText(block.code)
            setCopied(true)
            setTimeout(() => setCopied(false), 2000)
        }
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-[#0d1117] border border-zinc-800/50"
            )}
        >
            {/* Header */}
            <div className="flex items-center justify-between px-4 py-3 bg-zinc-900/80 border-b border-zinc-800/50">
                <div className="flex items-center gap-2">
                    <Code2 className="w-4 h-4 text-emerald-400" />
                    <span className="text-sm font-medium text-zinc-300">{block.title}</span>
                    {block.language && (
                        <span className="px-2 py-0.5 rounded-full text-xs bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                            {block.language}
                        </span>
                    )}
                </div>
                <button
                    onClick={handleCopy}
                    className={cn(
                        "flex items-center gap-1.5 px-3 py-1.5 rounded-lg",
                        "text-xs font-medium transition-all duration-200",
                        copied
                            ? "bg-emerald-500/20 text-emerald-300"
                            : "bg-zinc-800 text-zinc-400 hover:text-white hover:bg-zinc-700"
                    )}
                >
                    {copied ? (
                        <>
                            <Check className="w-3.5 h-3.5" />
                            Kopierad!
                        </>
                    ) : (
                        <>
                            <Copy className="w-3.5 h-3.5" />
                            Kopiera
                        </>
                    )}
                </button>
            </div>

            {/* Code */}
            <div className="p-4 overflow-x-auto">
                <SyntaxHighlighter
                    language={block.language || "bash"}
                    style={oneDark}
                    customStyle={{
                        background: "transparent",
                        padding: 0,
                        margin: 0,
                        fontSize: "0.875rem"
                    }}
                >
                    {block.code || ""}
                </SyntaxHighlighter>
            </div>
        </motion.div>
    )
}

// ============================================================================
// QUIZ BLOCK - Interactive Quiz
// ============================================================================
function QuizBlockComponent({ block }: { block: ContentBlock }) {
    const [selected, setSelected] = React.useState<number | null>(null)
    const [showResult, setShowResult] = React.useState(false)

    const isCorrect = selected === block.correctIndex

    const handleSelect = (index: number) => {
        if (showResult) return
        setSelected(index)
    }

    const handleCheck = () => {
        if (selected !== null) {
            setShowResult(true)
        }
    }

    const handleReset = () => {
        setSelected(null)
        setShowResult(false)
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-zinc-900/50 border border-zinc-800/50",
                "p-6"
            )}
        >
            <div className="flex items-center gap-3 mb-4">
                <div className={cn(
                    "w-9 h-9 rounded-lg flex items-center justify-center",
                    "bg-cyan-500/10 border border-cyan-500/20"
                )}>
                    <HelpCircle className="w-4 h-4 text-cyan-400" />
                </div>
                <h3 className="text-lg font-semibold text-white">Quiz</h3>
            </div>

            <p className="text-zinc-200 mb-4 font-medium">{block.question}</p>

            <div className="space-y-2 mb-4">
                {block.options?.map((option, i) => {
                    const isSelected = selected === i
                    const isCorrectOption = i === block.correctIndex

                    return (
                        <button
                            key={i}
                            onClick={() => handleSelect(i)}
                            disabled={showResult}
                            className={cn(
                                "w-full text-left px-4 py-3 rounded-xl",
                                "border transition-all duration-200",
                                !showResult && !isSelected && "border-zinc-700 hover:border-zinc-600 bg-zinc-800/50 hover:bg-zinc-800",
                                !showResult && isSelected && "border-cyan-500 bg-cyan-500/10",
                                showResult && isCorrectOption && "border-emerald-500 bg-emerald-500/10",
                                showResult && isSelected && !isCorrectOption && "border-red-500 bg-red-500/10"
                            )}
                        >
                            <div className="flex items-center gap-3">
                                <div className={cn(
                                    "w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold",
                                    !showResult && !isSelected && "bg-zinc-700 text-zinc-400",
                                    !showResult && isSelected && "bg-cyan-500 text-white",
                                    showResult && isCorrectOption && "bg-emerald-500 text-white",
                                    showResult && isSelected && !isCorrectOption && "bg-red-500 text-white"
                                )}>
                                    {showResult && isCorrectOption ? (
                                        <Check className="w-3.5 h-3.5" />
                                    ) : showResult && isSelected && !isCorrectOption ? (
                                        <XCircle className="w-3.5 h-3.5" />
                                    ) : (
                                        String.fromCharCode(65 + i)
                                    )}
                                </div>
                                <span className={cn(
                                    "text-sm",
                                    showResult && isCorrectOption && "text-emerald-300",
                                    showResult && isSelected && !isCorrectOption && "text-red-300",
                                    !showResult && "text-zinc-300"
                                )}>
                                    {option}
                                </span>
                            </div>
                        </button>
                    )
                })}
            </div>

            {/* Result */}
            <AnimatePresence>
                {showResult && (
                    <motion.div
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: "auto" }}
                        exit={{ opacity: 0, height: 0 }}
                        className={cn(
                            "rounded-xl p-4 mb-4",
                            isCorrect ? "bg-emerald-500/10 border border-emerald-500/20" : "bg-amber-500/10 border border-amber-500/20"
                        )}
                    >
                        <div className="flex items-start gap-3">
                            {isCorrect ? (
                                <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />
                            ) : (
                                <Lightbulb className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
                            )}
                            <div>
                                <p className={cn(
                                    "font-semibold mb-1",
                                    isCorrect ? "text-emerald-300" : "text-amber-300"
                                )}>
                                    {isCorrect ? "Rätt svar! 🎉" : "Inte riktigt..."}
                                </p>
                                <p className="text-sm text-zinc-400">{block.explanation}</p>
                            </div>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>

            {/* Actions */}
            <div className="flex gap-2">
                {!showResult ? (
                    <button
                        onClick={handleCheck}
                        disabled={selected === null}
                        className={cn(
                            "px-4 py-2 rounded-lg font-medium text-sm transition-all",
                            selected === null
                                ? "bg-zinc-800 text-zinc-500 cursor-not-allowed"
                                : "bg-cyan-500 text-white hover:bg-cyan-400"
                        )}
                    >
                        Kontrollera svar
                    </button>
                ) : (
                    <button
                        onClick={handleReset}
                        className="px-4 py-2 rounded-lg bg-zinc-800 text-zinc-300 hover:bg-zinc-700 font-medium text-sm transition-all"
                    >
                        Försök igen
                    </button>
                )}
            </div>
        </motion.div>
    )
}

// ============================================================================
// TIP BLOCK - Pro Tips
// ============================================================================
function TipBlock({ block }: { block: ContentBlock }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "rounded-2xl",
                "bg-gradient-to-br from-teal-500/10 to-cyan-500/5",
                "border border-teal-500/20",
                "p-6"
            )}
        >
            <div className="flex items-center gap-3 mb-3">
                <div className={cn(
                    "w-9 h-9 rounded-lg flex items-center justify-center",
                    "bg-teal-500/20 border border-teal-500/30"
                )}>
                    <Lightbulb className="w-4 h-4 text-teal-400" />
                </div>
                <h3 className="text-lg font-semibold text-teal-300">{block.title}</h3>
            </div>
            <div className="text-zinc-300 text-sm leading-relaxed whitespace-pre-line">
                {block.content}
            </div>
        </motion.div>
    )
}

// ============================================================================
// WARNING BLOCK - Important Warnings
// ============================================================================
function WarningBlock({ block }: { block: ContentBlock }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "rounded-2xl",
                "bg-gradient-to-br from-red-500/10 to-orange-500/5",
                "border border-red-500/20",
                "p-6"
            )}
        >
            <div className="flex items-center gap-3 mb-3">
                <div className={cn(
                    "w-9 h-9 rounded-lg flex items-center justify-center",
                    "bg-red-500/20 border border-red-500/30"
                )}>
                    <AlertTriangle className="w-4 h-4 text-red-400" />
                </div>
                <h3 className="text-lg font-semibold text-red-300">{block.title}</h3>
            </div>
            <div className="text-zinc-300 text-sm leading-relaxed">
                {block.content}
            </div>
        </motion.div>
    )
}

// ============================================================================
// CHECKPOINT BLOCK - Task Completion
// ============================================================================
function CheckpointBlock({ block, onComplete }: { block: ContentBlock; onComplete?: () => void }) {
    const [celebrated, setCelebrated] = React.useState(false)

    const handleComplete = () => {
        setCelebrated(true)
        onComplete?.()
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "relative rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-emerald-500/20 via-teal-500/10 to-cyan-500/5",
                "border border-emerald-500/30",
                "p-6"
            )}
        >
            {/* Celebration effect */}
            <AnimatePresence>
                {celebrated && (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className="absolute inset-0 pointer-events-none"
                    >
                        {[...Array(20)].map((_, i) => (
                            <motion.div
                                key={i}
                                className="absolute text-2xl"
                                initial={{
                                    x: "50%",
                                    y: "50%",
                                    scale: 0,
                                    rotate: 0
                                }}
                                animate={{
                                    x: `${Math.random() * 100}%`,
                                    y: `${Math.random() * 100}%`,
                                    scale: [0, 1, 0],
                                    rotate: Math.random() * 360
                                }}
                                transition={{
                                    duration: 1.5,
                                    delay: i * 0.05,
                                    ease: "easeOut"
                                }}
                            >
                                {['🎉', '⭐', '✨', '🚀', '💚'][i % 5]}
                            </motion.div>
                        ))}
                    </motion.div>
                )}
            </AnimatePresence>

            <div className="relative">
                <div className="flex items-center gap-3 mb-4">
                    <motion.div
                        className={cn(
                            "w-12 h-12 rounded-xl flex items-center justify-center",
                            "bg-gradient-to-br from-emerald-500 to-teal-600",
                            "shadow-lg shadow-emerald-500/25"
                        )}
                        animate={celebrated ? { scale: [1, 1.2, 1] } : {}}
                        transition={{ duration: 0.3 }}
                    >
                        {celebrated ? (
                            <CheckCircle2 className="w-6 h-6 text-white" />
                        ) : (
                            <Sparkles className="w-6 h-6 text-white" />
                        )}
                    </motion.div>
                    <div>
                        <h3 className="text-xl font-bold text-white">{block.title}</h3>
                        <p className="text-emerald-300 text-sm">Bra jobbat!</p>
                    </div>
                </div>

                <p className="text-zinc-300 mb-4">{block.content}</p>

                {!celebrated && (
                    <motion.button
                        onClick={handleComplete}
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                        className={cn(
                            "w-full py-3 rounded-xl font-semibold",
                            "bg-gradient-to-r from-emerald-500 to-teal-600",
                            "text-white shadow-lg shadow-emerald-500/25",
                            "hover:shadow-emerald-500/40 transition-shadow"
                        )}
                    >
                        ✅ Markera som klar
                    </motion.button>
                )}

                {celebrated && (
                    <motion.div
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        className="text-center py-3 text-emerald-300 font-semibold"
                    >
                        🎉 Task avklarad!
                    </motion.div>
                )}
            </div>
        </motion.div>
    )
}

// ============================================================================
// MAIN RENDERER
// ============================================================================
interface Linux247ContentRendererProps {
    blocks: ContentBlock[]
    onTaskComplete?: () => void
}

export function Linux247ContentRenderer({ blocks, onTaskComplete }: Linux247ContentRendererProps) {
    return (
        <div className="space-y-6">
            {blocks.map((block, index) => {
                switch (block.type) {
                    case 'intro':
                        return <IntroBlock key={index} block={block} />
                    case 'concept':
                        return <ConceptBlock key={index} block={block} />
                    case 'code':
                        return <CodeBlockComponent key={index} block={block} />
                    case 'quiz':
                        return <QuizBlockComponent key={index} block={block} />
                    case 'tip':
                        return <TipBlock key={index} block={block} />
                    case 'warning':
                        return <WarningBlock key={index} block={block} />
                    case 'checkpoint':
                        return <CheckpointBlock key={index} block={block} onComplete={onTaskComplete} />
                    default:
                        return null
                }
            })}
        </div>
    )
}

export default Linux247ContentRenderer
