"use client"

/**
 * ============================================================================
 * SIMULATED TERMINAL - Interactive terminal practice
 * ============================================================================
 *
 * A simulated terminal that:
 * - Accepts predefined commands
 * - Shows expected output
 * - Validates user input
 * - Provides hints
 * - Tracks completion
 */

import { useState, useRef, useEffect } from "react"
import { cn } from "@saas/ui"
import {
    Terminal,
    CheckCircle2,
    XCircle,
    Lightbulb,
    RotateCcw,
    ChevronRight
} from "lucide-react"
import { Button } from "@/components/ui/button"

interface PracticeStep {
    step: number
    title: string
    instruction: string
    command: string
    expectedOutput: string
    explanation: string
}

interface SimulatedTerminalProps {
    description: string
    exercises: PracticeStep[]
    onComplete?: () => void
}

interface TerminalLine {
    type: "input" | "output" | "error" | "success"
    content: string
}

export function SimulatedTerminal({
    description,
    exercises,
    onComplete
}: SimulatedTerminalProps) {
    const [currentStep, setCurrentStep] = useState(0)
    const [input, setInput] = useState("")
    const [history, setHistory] = useState<TerminalLine[]>([])
    const [completed, setCompleted] = useState<boolean[]>(new Array(exercises.length).fill(false))
    const [showHint, setShowHint] = useState(false)
    const inputRef = useRef<HTMLInputElement>(null)
    const terminalRef = useRef<HTMLDivElement>(null)

    const currentExercise = exercises[currentStep]
    const allCompleted = completed.every(Boolean)

    // Auto-scroll terminal
    useEffect(() => {
        if (terminalRef.current) {
            terminalRef.current.scrollTop = terminalRef.current.scrollHeight
        }
    }, [history])

    // Focus input on mount
    useEffect(() => {
        inputRef.current?.focus()
    }, [])

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault()

        if (!input.trim()) return

        const trimmedInput = input.trim()
        const expectedCommand = currentExercise.command.trim()

        // Add input to history
        setHistory(prev => [...prev, { type: "input", content: `$ ${trimmedInput}` }])

        // Check if command matches (case-insensitive, flexible whitespace)
        const normalizedInput = trimmedInput.replace(/\s+/g, ' ').toLowerCase()
        const normalizedExpected = expectedCommand.replace(/\s+/g, ' ').toLowerCase()

        const isCorrect = normalizedInput === normalizedExpected ||
            trimmedInput === expectedCommand ||
            // Allow minor variations
            normalizedInput.includes(normalizedExpected.split(' ').slice(0, 3).join(' '))

        if (isCorrect) {
            // Show expected output
            if (currentExercise.expectedOutput) {
                setHistory(prev => [...prev, {
                    type: "output",
                    content: currentExercise.expectedOutput
                }])
            }

            // Mark step as completed
            const newCompleted = [...completed]
            newCompleted[currentStep] = true
            setCompleted(newCompleted)

            // Success message
            setHistory(prev => [...prev, {
                type: "success",
                content: `✅ Korrekt! ${currentExercise.explanation}`
            }])

            // Move to next step after delay
            setTimeout(() => {
                if (currentStep < exercises.length - 1) {
                    setCurrentStep(currentStep + 1)
                    setShowHint(false)
                } else {
                    // All done
                    setHistory(prev => [...prev, {
                        type: "success",
                        content: "🎉 Alla övningar slutförda!"
                    }])
                    onComplete?.()
                }
            }, 1500)
        } else {
            // Wrong command
            setHistory(prev => [...prev, {
                type: "error",
                content: `❌ Inte riktigt. Försök igen eller visa ledtråd.`
            }])
        }

        setInput("")
    }

    const handleReset = () => {
        setCurrentStep(0)
        setHistory([])
        setCompleted(new Array(exercises.length).fill(false))
        setShowHint(false)
        setInput("")
    }

    const handleShowHint = () => {
        setShowHint(true)
        // Show first few characters of command
        const hint = currentExercise.command.substring(0, Math.min(20, currentExercise.command.length))
        setHistory(prev => [...prev, {
            type: "output",
            content: `💡 Ledtråd: Kommandot börjar med "${hint}..."`
        }])
    }

    return (
        <div className="space-y-4">
            {/* Header */}
            <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                    <Terminal className="w-5 h-5 text-emerald-400" />
                    <h3 className="text-lg font-semibold text-white">
                        Praktik - Simulerad Terminal
                    </h3>
                </div>
                <div className="flex items-center gap-2">
                    <span className="text-sm text-zinc-400">
                        Steg {currentStep + 1} av {exercises.length}
                    </span>
                    <Button
                        variant="ghost"
                        size="sm"
                        onClick={handleReset}
                        className="text-zinc-400 hover:text-white"
                    >
                        <RotateCcw className="w-4 h-4" />
                    </Button>
                </div>
            </div>

            {/* Description */}
            <p className="text-zinc-400">{description}</p>

            {/* Progress */}
            <div className="flex gap-2">
                {exercises.map((_, index) => (
                    <div
                        key={index}
                        className={cn(
                            "h-2 flex-1 rounded-full transition-colors",
                            completed[index] ? "bg-emerald-500" :
                                index === currentStep ? "bg-purple-500" :
                                    "bg-zinc-700"
                        )}
                    />
                ))}
            </div>

            {/* Current instruction */}
            {!allCompleted && (
                <div className={cn(
                    "bg-purple-900/20 border border-purple-500/30",
                    "rounded-lg p-4"
                )}>
                    <div className="flex items-center gap-2 mb-2">
                        <ChevronRight className="w-4 h-4 text-purple-400" />
                        <span className="text-sm font-semibold text-purple-400">
                            Steg {currentExercise.step}: {currentExercise.title}
                        </span>
                    </div>
                    <p className="text-zinc-300">{currentExercise.instruction}</p>
                </div>
            )}

            {/* Terminal */}
            <div className={cn(
                "bg-zinc-950 rounded-lg border border-zinc-700",
                "font-mono text-sm"
            )}>
                {/* Terminal header */}
                <div className="flex items-center gap-2 px-4 py-2 bg-zinc-900 border-b border-zinc-700 rounded-t-lg">
                    <div className="w-3 h-3 rounded-full bg-red-500" />
                    <div className="w-3 h-3 rounded-full bg-yellow-500" />
                    <div className="w-3 h-3 rounded-full bg-green-500" />
                    <span className="ml-2 text-zinc-500 text-xs">bash</span>
                </div>

                {/* Terminal content */}
                <div
                    ref={terminalRef}
                    className="p-4 h-64 overflow-y-auto"
                >
                    {history.map((line, index) => (
                        <div
                            key={index}
                            className={cn(
                                "mb-1 whitespace-pre-wrap",
                                line.type === "input" && "text-emerald-400",
                                line.type === "output" && "text-zinc-300",
                                line.type === "error" && "text-red-400",
                                line.type === "success" && "text-emerald-400"
                            )}
                        >
                            {line.content}
                        </div>
                    ))}

                    {/* Input line */}
                    {!allCompleted && (
                        <form onSubmit={handleSubmit} className="flex items-center">
                            <span className="text-emerald-400 mr-2">$</span>
                            <input
                                ref={inputRef}
                                type="text"
                                value={input}
                                onChange={(e) => setInput(e.target.value)}
                                className={cn(
                                    "flex-1 bg-transparent text-white",
                                    "outline-none border-none",
                                    "font-mono"
                                )}
                                placeholder="Skriv kommandot här..."
                                autoComplete="off"
                                spellCheck={false}
                            />
                        </form>
                    )}
                </div>
            </div>

            {/* Actions */}
            {!allCompleted && (
                <div className="flex gap-3">
                    <Button
                        variant="outline"
                        size="sm"
                        onClick={handleShowHint}
                        disabled={showHint}
                        className="text-amber-400 border-amber-500/30 hover:bg-amber-500/10"
                    >
                        <Lightbulb className="w-4 h-4 mr-2" />
                        Visa ledtråd
                    </Button>
                    <Button
                        variant="outline"
                        size="sm"
                        onClick={() => setInput(currentExercise.command)}
                        className="text-zinc-400 hover:text-white"
                    >
                        Visa lösning
                    </Button>
                </div>
            )}

            {/* Completion message */}
            {allCompleted && (
                <div className={cn(
                    "bg-emerald-900/20 border border-emerald-500/30",
                    "rounded-lg p-6 text-center"
                )}>
                    <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto mb-3" />
                    <h4 className="text-lg font-semibold text-white mb-2">
                        Praktik slutförd!
                    </h4>
                    <p className="text-zinc-400">
                        Du har genomfört alla {exercises.length} övningar.
                    </p>
                </div>
            )}
        </div>
    )
}

export default SimulatedTerminal
