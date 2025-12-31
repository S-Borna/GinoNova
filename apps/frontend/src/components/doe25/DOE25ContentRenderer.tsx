"use client"

/**
 * ============================================================================
 * DOE25 CONTENT RENDERER - Interactive Block Components
 * ============================================================================
 *
 * Renders DOE25 content blocks as beautiful, interactive components:
 * - IntroBlock: Learning objectives with animated icons
 * - ConceptBlock: Explanations with diagrams
 * - CodeBlock: Syntax highlighted with copy button
 * - QuizBlock: Interactive multiple choice
 * - CheckpointBlock: Celebration animation
 *
 * @phase DOE25-REDESIGN
 */

import * as React from "react"
import { useState, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter"
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism"
import {
    Target,
    BookOpen,
    Code2,
    HelpCircle,
    CheckCircle2,
    XCircle,
    Copy,
    Check,
    Lightbulb,
    AlertTriangle,
    Trophy,
    Sparkles,
    ChevronDown,
    ChevronUp,
    Terminal,
    Zap,
    Brain,
    Rocket,
    ArrowRight
} from "lucide-react"
import { ContentBlock, QuizOption } from "@/data/doe25-module"

/* ============================================================================
   INTRO BLOCK - Learning Objectives
   ============================================================================ */

function IntroBlock({ block, index }: { block: ContentBlock; index: number }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
            className={cn(
                "relative overflow-hidden rounded-2xl",
                "bg-gradient-to-br from-purple-500/10 via-cyan-500/10 to-purple-500/10",
                "border border-purple-500/20",
                "p-6 md:p-8"
            )}
        >
            {/* Background glow */}
            <div className="absolute top-0 right-0 w-64 h-64 bg-purple-500/10 rounded-full blur-3xl" />
            
            <div className="relative">
                {/* Headline */}
                {block.headline && (
                    <h2 className="text-2xl md:text-3xl font-bold text-white mb-6 flex items-center gap-3">
                        <span>{block.headline}</span>
                    </h2>
                )}

                {/* Learning Objectives */}
                {block.learning_objectives && block.learning_objectives.length > 0 && (
                    <div className="space-y-3">
                        <div className="flex items-center gap-2 text-purple-400 font-medium mb-4">
                            <Target className="w-5 h-5" />
                            <span>Lärandemål</span>
                        </div>
                        <ul className="grid gap-3 md:grid-cols-2">
                            {block.learning_objectives.map((obj, i) => (
                                <motion.li
                                    key={i}
                                    initial={{ opacity: 0, x: -20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    transition={{ delay: 0.2 + i * 0.1 }}
                                    className={cn(
                                        "flex items-start gap-3 p-3 rounded-xl",
                                        "bg-white/5 border border-white/10",
                                        "hover:bg-white/10 transition-colors"
                                    )}
                                >
                                    <div className="w-6 h-6 rounded-full bg-purple-500/20 flex items-center justify-center shrink-0 mt-0.5">
                                        <CheckCircle2 className="w-4 h-4 text-purple-400" />
                                    </div>
                                    <span className="text-zinc-300">{obj}</span>
                                </motion.li>
                            ))}
                        </ul>
                    </div>
                )}
            </div>
        </motion.div>
    )
}

/* ============================================================================
   CONCEPT BLOCK - Explanations
   ============================================================================ */

function ConceptBlock({ block, index }: { block: ContentBlock; index: number }) {
    const [isExpanded, setIsExpanded] = useState(true)

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.05 }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-[#0d0d12] border border-zinc-800/50",
                "hover:border-purple-500/30 transition-colors duration-300"
            )}
        >
            {/* Header */}
            <button
                onClick={() => setIsExpanded(!isExpanded)}
                className="w-full flex items-center gap-4 p-5 text-left hover:bg-white/5 transition-colors"
            >
                <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-500/20 to-cyan-500/20 flex items-center justify-center border border-blue-500/30">
                    <Brain className="w-5 h-5 text-blue-400" />
                </div>
                <div className="flex-1">
                    <h3 className="text-lg font-semibold text-white">
                        {block.title || "Koncept"}
                    </h3>
                </div>
                <motion.div
                    animate={{ rotate: isExpanded ? 180 : 0 }}
                    transition={{ duration: 0.2 }}
                >
                    <ChevronDown className="w-5 h-5 text-zinc-500" />
                </motion.div>
            </button>

            {/* Content */}
            <AnimatePresence>
                {isExpanded && (
                    <motion.div
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: "auto", opacity: 1 }}
                        exit={{ height: 0, opacity: 0 }}
                        transition={{ duration: 0.3 }}
                        className="overflow-hidden"
                    >
                        <div className="px-5 pb-5">
                            {/* Explanation - render as preformatted for diagrams */}
                            {block.explanation && (
                                <div className="rounded-xl bg-[#0a0a0f] border border-zinc-800 p-4 overflow-x-auto">
                                    <pre className="text-sm text-zinc-300 font-mono whitespace-pre leading-relaxed">
                                        {block.explanation}
                                    </pre>
                                </div>
                            )}

                            {/* Pro Tip */}
                            {block.pro_tip && (
                                <div className="mt-4 flex items-start gap-3 p-4 rounded-xl bg-amber-500/10 border border-amber-500/20">
                                    <Lightbulb className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
                                    <div>
                                        <span className="font-medium text-amber-400">Pro-tip: </span>
                                        <span className="text-amber-200/80">{block.pro_tip}</span>
                                    </div>
                                </div>
                            )}

                            {/* Warning */}
                            {block.warning && (
                                <div className={cn(
                                    "mt-4 flex items-start gap-3 p-4 rounded-xl",
                                    block.warning_level === "danger" 
                                        ? "bg-red-500/10 border border-red-500/20"
                                        : "bg-amber-500/10 border border-amber-500/20"
                                )}>
                                    <AlertTriangle className={cn(
                                        "w-5 h-5 shrink-0 mt-0.5",
                                        block.warning_level === "danger" ? "text-red-400" : "text-amber-400"
                                    )} />
                                    <div>
                                        <span className={cn(
                                            "font-medium",
                                            block.warning_level === "danger" ? "text-red-400" : "text-amber-400"
                                        )}>
                                            {block.warning_level === "danger" ? "Varning: " : "OBS: "}
                                        </span>
                                        <span className={cn(
                                            block.warning_level === "danger" ? "text-red-200/80" : "text-amber-200/80"
                                        )}>
                                            {block.warning}
                                        </span>
                                    </div>
                                </div>
                            )}
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </motion.div>
    )
}

/* ============================================================================
   CODE BLOCK - Syntax Highlighted
   ============================================================================ */

const customCodeStyle = {
    ...oneDark,
    'pre[class*="language-"]': {
        ...oneDark['pre[class*="language-"]'],
        background: "transparent",
        margin: 0,
        padding: "1rem",
        fontSize: "0.875rem",
    },
    'code[class*="language-"]': {
        ...oneDark['code[class*="language-"]'],
        background: "transparent",
        fontSize: "0.875rem",
    },
}

function CodeBlockComponent({ block, index }: { block: ContentBlock; index: number }) {
    const [copied, setCopied] = useState(false)

    const handleCopy = async () => {
        if (!block.code) return
        try {
            await navigator.clipboard.writeText(block.code)
            setCopied(true)
            setTimeout(() => setCopied(false), 2000)
        } catch (err) {
            console.error("Failed to copy:", err)
        }
    }

    const language = block.language || "bash"

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.05 }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-[#0a0a0f] border border-zinc-800",
                "hover:border-emerald-500/30 transition-colors duration-300"
            )}
        >
            {/* Header */}
            <div className="flex items-center justify-between px-4 py-3 bg-zinc-900/50 border-b border-zinc-800">
                <div className="flex items-center gap-3">
                    {/* Terminal dots */}
                    <div className="flex items-center gap-1.5">
                        <div className="w-3 h-3 rounded-full bg-red-500/80" />
                        <div className="w-3 h-3 rounded-full bg-yellow-500/80" />
                        <div className="w-3 h-3 rounded-full bg-green-500/80" />
                    </div>
                    
                    {/* Title & Language */}
                    <div className="flex items-center gap-2 ml-2">
                        <Terminal className="w-4 h-4 text-emerald-400" />
                        <span className="text-sm font-medium text-zinc-300">
                            {block.title || language.toUpperCase()}
                        </span>
                    </div>
                </div>

                {/* Copy Button */}
                <button
                    onClick={handleCopy}
                    className={cn(
                        "flex items-center gap-2 px-3 py-1.5 rounded-lg",
                        "text-xs font-medium transition-all duration-200",
                        copied 
                            ? "bg-emerald-500/20 text-emerald-400"
                            : "bg-zinc-800 text-zinc-400 hover:bg-zinc-700 hover:text-white"
                    )}
                >
                    {copied ? (
                        <>
                            <Check className="w-3.5 h-3.5" />
                            Kopierat!
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
            <div className="overflow-x-auto">
                <SyntaxHighlighter
                    language={language}
                    style={customCodeStyle}
                    showLineNumbers
                    wrapLongLines={false}
                    customStyle={{
                        background: "transparent",
                        margin: 0,
                    }}
                >
                    {block.code || ""}
                </SyntaxHighlighter>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   QUIZ BLOCK - Interactive Multiple Choice
   ============================================================================ */

function QuizBlockComponent({ block, index }: { block: ContentBlock; index: number }) {
    const [selectedOption, setSelectedOption] = useState<number | null>(null)
    const [showResult, setShowResult] = useState(false)
    const [showHint, setShowHint] = useState(false)

    const handleSelect = (optionIndex: number) => {
        if (showResult) return
        setSelectedOption(optionIndex)
    }

    const handleSubmit = () => {
        if (selectedOption === null) return
        setShowResult(true)
    }

    const handleRetry = () => {
        setSelectedOption(null)
        setShowResult(false)
        setShowHint(false)
    }

    const isCorrect = selectedOption !== null && block.options?.[selectedOption]?.correct

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.05 }}
            className={cn(
                "relative rounded-2xl overflow-hidden",
                "bg-[#0d0d12] border",
                showResult 
                    ? isCorrect 
                        ? "border-emerald-500/50" 
                        : "border-red-500/50"
                    : "border-cyan-500/30"
            )}
        >
            {/* Success confetti overlay */}
            {showResult && isCorrect && (
                <div className="absolute inset-0 pointer-events-none overflow-hidden">
                    {[...Array(20)].map((_, i) => (
                        <motion.div
                            key={i}
                            initial={{
                                x: "50%",
                                y: "50%",
                                scale: 0,
                            }}
                            animate={{
                                x: `${Math.random() * 100}%`,
                                y: `${Math.random() * 100}%`,
                                scale: [0, 1, 0],
                                rotate: Math.random() * 360,
                            }}
                            transition={{
                                duration: 1.5,
                                delay: i * 0.02,
                            }}
                            className="absolute w-3 h-3 rounded-full"
                            style={{
                                background: ['#10b981', '#6366f1', '#f59e0b', '#ec4899'][i % 4]
                            }}
                        />
                    ))}
                </div>
            )}

            {/* Header */}
            <div className="flex items-center gap-3 p-5 bg-gradient-to-r from-cyan-500/10 to-purple-500/10 border-b border-white/5">
                <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-500/20 to-purple-500/20 flex items-center justify-center border border-cyan-500/30">
                    <HelpCircle className="w-5 h-5 text-cyan-400" />
                </div>
                <div>
                    <span className="text-xs font-medium text-cyan-400 uppercase tracking-wider">Quiz</span>
                    <h3 className="text-lg font-semibold text-white">{block.question}</h3>
                </div>
            </div>

            {/* Options */}
            <div className="p-5 space-y-3">
                {block.options?.map((option, i) => {
                    const isSelected = selectedOption === i
                    const isCorrectOption = option.correct
                    
                    let optionStyle = "border-zinc-700 hover:border-purple-500/50 hover:bg-white/5"
                    if (showResult) {
                        if (isCorrectOption) {
                            optionStyle = "border-emerald-500 bg-emerald-500/10"
                        } else if (isSelected && !isCorrectOption) {
                            optionStyle = "border-red-500 bg-red-500/10"
                        } else {
                            optionStyle = "border-zinc-800 opacity-50"
                        }
                    } else if (isSelected) {
                        optionStyle = "border-purple-500 bg-purple-500/10"
                    }

                    return (
                        <motion.button
                            key={i}
                            onClick={() => handleSelect(i)}
                            disabled={showResult}
                            whileHover={!showResult ? { scale: 1.01 } : {}}
                            whileTap={!showResult ? { scale: 0.99 } : {}}
                            className={cn(
                                "w-full flex items-center gap-4 p-4 rounded-xl",
                                "text-left transition-all duration-200",
                                "border-2",
                                optionStyle
                            )}
                        >
                            {/* Option Letter */}
                            <div className={cn(
                                "w-8 h-8 rounded-lg flex items-center justify-center shrink-0",
                                "font-bold text-sm",
                                showResult && isCorrectOption
                                    ? "bg-emerald-500 text-white"
                                    : showResult && isSelected && !isCorrectOption
                                        ? "bg-red-500 text-white"
                                        : isSelected
                                            ? "bg-purple-500 text-white"
                                            : "bg-zinc-800 text-zinc-400"
                            )}>
                                {String.fromCharCode(65 + i)}
                            </div>

                            {/* Option Text */}
                            <span className={cn(
                                "flex-1",
                                showResult && isCorrectOption
                                    ? "text-emerald-300"
                                    : showResult && isSelected && !isCorrectOption
                                        ? "text-red-300"
                                        : "text-zinc-300"
                            )}>
                                {option.text}
                            </span>

                            {/* Result Icon */}
                            {showResult && (
                                <div>
                                    {isCorrectOption ? (
                                        <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                                    ) : isSelected ? (
                                        <XCircle className="w-5 h-5 text-red-400" />
                                    ) : null}
                                </div>
                            )}
                        </motion.button>
                    )
                })}
            </div>

            {/* Feedback */}
            <AnimatePresence>
                {showResult && selectedOption !== null && (
                    <motion.div
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: "auto" }}
                        exit={{ opacity: 0, height: 0 }}
                        className="overflow-hidden"
                    >
                        <div className={cn(
                            "mx-5 mb-5 p-4 rounded-xl",
                            isCorrect 
                                ? "bg-emerald-500/10 border border-emerald-500/30"
                                : "bg-red-500/10 border border-red-500/30"
                        )}>
                            <div className="flex items-start gap-3">
                                {isCorrect ? (
                                    <Sparkles className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />
                                ) : (
                                    <XCircle className="w-5 h-5 text-red-400 shrink-0 mt-0.5" />
                                )}
                                <div>
                                    <p className={cn(
                                        "font-medium",
                                        isCorrect ? "text-emerald-400" : "text-red-400"
                                    )}>
                                        {isCorrect ? "Rätt svar! 🎉" : "Fel svar"}
                                    </p>
                                    {block.options?.[selectedOption]?.feedback && (
                                        <p className="text-sm text-zinc-400 mt-1">
                                            {block.options[selectedOption].feedback}
                                        </p>
                                    )}
                                </div>
                            </div>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>

            {/* Actions */}
            <div className="flex items-center gap-3 px-5 pb-5">
                {!showResult ? (
                    <>
                        {block.hint && (
                            <button
                                onClick={() => setShowHint(!showHint)}
                                className={cn(
                                    "flex items-center gap-2 px-4 py-2 rounded-xl",
                                    "text-sm font-medium transition-all",
                                    showHint
                                        ? "bg-amber-500/20 text-amber-400"
                                        : "bg-zinc-800 text-zinc-400 hover:bg-zinc-700"
                                )}
                            >
                                <Lightbulb className="w-4 h-4" />
                                {showHint ? "Dölj ledtråd" : "Visa ledtråd"}
                            </button>
                        )}
                        <button
                            onClick={handleSubmit}
                            disabled={selectedOption === null}
                            className={cn(
                                "flex-1 flex items-center justify-center gap-2",
                                "px-4 py-2.5 rounded-xl font-medium",
                                "transition-all duration-200",
                                selectedOption !== null
                                    ? "bg-gradient-to-r from-purple-600 to-cyan-600 text-white hover:opacity-90"
                                    : "bg-zinc-800 text-zinc-500 cursor-not-allowed"
                            )}
                        >
                            Svara
                            <ArrowRight className="w-4 h-4" />
                        </button>
                    </>
                ) : !isCorrect && (
                    <button
                        onClick={handleRetry}
                        className={cn(
                            "flex-1 flex items-center justify-center gap-2",
                            "px-4 py-2.5 rounded-xl font-medium",
                            "bg-zinc-800 text-zinc-300 hover:bg-zinc-700",
                            "transition-all duration-200"
                        )}
                    >
                        Försök igen
                    </button>
                )}
            </div>

            {/* Hint */}
            <AnimatePresence>
                {showHint && block.hint && !showResult && (
                    <motion.div
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: "auto" }}
                        exit={{ opacity: 0, height: 0 }}
                        className="overflow-hidden"
                    >
                        <div className="mx-5 mb-5 p-4 rounded-xl bg-amber-500/10 border border-amber-500/20">
                            <div className="flex items-start gap-3">
                                <Lightbulb className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
                                <p className="text-sm text-amber-200/80">{block.hint}</p>
                            </div>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </motion.div>
    )
}

/* ============================================================================
   CHECKPOINT BLOCK - Celebration
   ============================================================================ */

function CheckpointBlockComponent({ block, index }: { block: ContentBlock; index: number }) {
    const [celebrated, setCelebrated] = useState(false)

    useEffect(() => {
        // Auto-celebrate on mount
        const timer = setTimeout(() => setCelebrated(true), 500)
        return () => clearTimeout(timer)
    }, [])

    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: index * 0.05, type: "spring" }}
            className={cn(
                "relative rounded-2xl overflow-hidden",
                "bg-gradient-to-r from-emerald-500/20 via-purple-500/20 to-cyan-500/20",
                "border border-emerald-500/30",
                "p-6 md:p-8"
            )}
        >
            {/* Animated background */}
            <motion.div
                animate={{
                    backgroundPosition: ["0% 50%", "100% 50%", "0% 50%"],
                }}
                transition={{ duration: 5, repeat: Infinity }}
                className="absolute inset-0 opacity-30"
                style={{
                    background: "linear-gradient(90deg, transparent, rgba(16,185,129,0.3), transparent)",
                    backgroundSize: "200% 100%",
                }}
            />

            <div className="relative flex items-center gap-6">
                {/* Trophy Icon */}
                <motion.div
                    animate={celebrated ? {
                        scale: [1, 1.2, 1],
                        rotate: [0, -10, 10, 0],
                    } : {}}
                    transition={{ duration: 0.5 }}
                    className={cn(
                        "w-16 h-16 rounded-2xl flex items-center justify-center shrink-0",
                        "bg-gradient-to-br from-amber-500 to-orange-500",
                        "shadow-lg shadow-amber-500/30"
                    )}
                >
                    <Trophy className="w-8 h-8 text-white" />
                </motion.div>

                {/* Message */}
                <div className="flex-1">
                    <motion.div
                        initial={{ opacity: 0, x: 20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: 0.3 }}
                    >
                        <h3 className="text-xl md:text-2xl font-bold text-white mb-2">
                            {block.message || "Checkpoint klar! 🎉"}
                        </h3>
                        <p className="text-emerald-300/80">
                            Bra jobbat! Du har slutfört denna sektion.
                        </p>
                    </motion.div>
                </div>

                {/* Sparkles */}
                <motion.div
                    animate={{
                        rotate: 360,
                        scale: [1, 1.1, 1],
                    }}
                    transition={{
                        rotate: { duration: 4, repeat: Infinity, ease: "linear" },
                        scale: { duration: 2, repeat: Infinity }
                    }}
                >
                    <Sparkles className="w-8 h-8 text-amber-400" />
                </motion.div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN RENDERER
   ============================================================================ */

interface DOE25ContentRendererProps {
    blocks: ContentBlock[]
    className?: string
}

export function DOE25ContentRenderer({ blocks, className }: DOE25ContentRendererProps) {
    return (
        <div className={cn("space-y-6", className)}>
            {blocks.map((block, index) => {
                switch (block.type) {
                    case "intro":
                        return <IntroBlock key={index} block={block} index={index} />
                    case "concept":
                        return <ConceptBlock key={index} block={block} index={index} />
                    case "code":
                        return <CodeBlockComponent key={index} block={block} index={index} />
                    case "quiz":
                        return <QuizBlockComponent key={index} block={block} index={index} />
                    case "checkpoint":
                        return <CheckpointBlockComponent key={index} block={block} index={index} />
                    default:
                        // Fallback for unknown types
                        return (
                            <div key={index} className="p-4 rounded-xl bg-zinc-800/50 border border-zinc-700">
                                <p className="text-zinc-400">Block type: {block.type}</p>
                            </div>
                        )
                }
            })}
        </div>
    )
}

export default DOE25ContentRenderer
