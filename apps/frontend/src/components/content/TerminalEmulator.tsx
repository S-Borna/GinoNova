"use client"

/**
 * ============================================================================
 * TERMINAL EMULATOR COMPONENT - Interactive Terminal for Learning
 * ============================================================================
 *
 * Features:
 * - xterm.js powered terminal
 * - Command validation against expected commands
 * - Hint system for guidance
 * - Progress tracking integration
 * - Mock command execution for learning
 *
 * @phase ILE Phase 2 - Terminal Component
 */

import * as React from "react"
import { useEffect, useRef, useState, useCallback } from "react"
import { cn } from "@/lib/utils"
import { Terminal, Lightbulb, CheckCircle2, XCircle, RotateCcw } from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface TerminalCommand {
    command: string
    description?: string
    output?: string
    successMessage?: string
}

export interface TerminalEmulatorProps {
    blockId: string
    prompt?: string
    initialCommands?: string[]
    expectedCommands?: TerminalCommand[]
    hints?: string[]
    onCommandExecuted?: (command: string, isCorrect: boolean) => void
    onComplete?: (history: string[]) => void
    className?: string
    readOnly?: boolean
}

interface HistoryEntry {
    type: "input" | "output" | "success" | "error"
    content: string
}

/* ============================================================================
   MOCK COMMAND RESPONSES
   ============================================================================ */

const mockResponses: Record<string, string> = {
    "ls": "Documents  Downloads  Pictures  Projects  README.md",
    "ls -la": `total 32
drwxr-xr-x  8 user user 4096 Jan 15 10:30 .
drwxr-xr-x  3 user user 4096 Jan 15 09:00 ..
drwxr-xr-x  2 user user 4096 Jan 15 10:30 Documents
drwxr-xr-x  2 user user 4096 Jan 15 10:30 Downloads
drwxr-xr-x  2 user user 4096 Jan 15 10:30 Pictures
drwxr-xr-x  5 user user 4096 Jan 15 10:30 Projects
-rw-r--r--  1 user user  512 Jan 15 10:30 README.md`,
    "pwd": "/home/user",
    "whoami": "devops-learner",
    "echo $USER": "devops-learner",
    "date": new Date().toUTCString(),
    "uname -a": "Linux devops-vm 5.15.0-generic #1 SMP x86_64 GNU/Linux",
    "cat README.md": "# Welcome to DevOps Learning!\n\nThis is your practice environment.",
    "docker --version": "Docker version 24.0.7, build afdd53b",
    "docker ps": "CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES",
    "kubectl version --client": "Client Version: v1.28.4",
    "terraform --version": "Terraform v1.6.5",
    "git --version": "git version 2.43.0",
    "git status": `On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean`,
    "python --version": "Python 3.11.6",
    "node --version": "v20.10.0",
    "npm --version": "10.2.3",
    "help": `Available commands:
  ls, pwd, whoami, date, echo, cat, clear
  docker, kubectl, terraform, git
  python, node, npm
  help - show this message`,
    "clear": "__CLEAR__",
}

/* ============================================================================
   HELPER FUNCTIONS
   ============================================================================ */

function normalizeCommand(cmd: string): string {
    return cmd.trim().toLowerCase().replace(/\s+/g, " ")
}

function executeCommand(cmd: string, expectedCommands?: TerminalCommand[]): { output: string; isExpected: boolean } {
    const normalizedCmd = normalizeCommand(cmd)

    // Check if it's an expected command
    if (expectedCommands) {
        const expected = expectedCommands.find(
            ec => normalizeCommand(ec.command) === normalizedCmd
        )
        if (expected) {
            return {
                output: expected.output || mockResponses[cmd] || `Command executed: ${cmd}`,
                isExpected: true
            }
        }
    }

    // Check mock responses
    const mockKey = Object.keys(mockResponses).find(
        key => normalizeCommand(key) === normalizedCmd
    )

    if (mockKey) {
        return { output: mockResponses[mockKey], isExpected: false }
    }

    // Unknown command
    if (cmd.startsWith("cd ")) {
        return { output: "", isExpected: false }
    }

    return { output: `bash: ${cmd.split(" ")[0]}: command not found`, isExpected: false }
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function TerminalEmulator({
    blockId,
    prompt = "$ ",
    initialCommands = [],
    expectedCommands = [],
    hints = [],
    onCommandExecuted,
    onComplete,
    className,
    readOnly = false,
}: TerminalEmulatorProps) {
    const [history, setHistory] = useState<HistoryEntry[]>([])
    const [commandHistory, setCommandHistory] = useState<string[]>([])
    const [historyIndex, setHistoryIndex] = useState(-1)
    const [currentInput, setCurrentInput] = useState("")
    const [completedCommands, setCompletedCommands] = useState<Set<string>>(new Set())
    const [showHints, setShowHints] = useState(false)
    const [currentHintIndex, setCurrentHintIndex] = useState(0)

    const inputRef = useRef<HTMLInputElement>(null)
    const terminalRef = useRef<HTMLDivElement>(null)

    // Auto-scroll to bottom
    useEffect(() => {
        if (terminalRef.current) {
            terminalRef.current.scrollTop = terminalRef.current.scrollHeight
        }
    }, [history])

    // Focus input on click
    const handleTerminalClick = useCallback(() => {
        if (inputRef.current && !readOnly) {
            inputRef.current.focus()
        }
    }, [readOnly])

    // Run initial commands
    useEffect(() => {
        if (initialCommands.length > 0) {
            const initialHistory: HistoryEntry[] = []
            initialCommands.forEach(cmd => {
                initialHistory.push({ type: "input", content: `${prompt}${cmd}` })
                const result = executeCommand(cmd, expectedCommands)
                if (result.output && result.output !== "__CLEAR__") {
                    initialHistory.push({ type: "output", content: result.output })
                }
            })
            setHistory(initialHistory)
        }
    }, [initialCommands, expectedCommands, prompt])

    // Handle command execution
    const handleExecute = useCallback(() => {
        if (!currentInput.trim()) return

        const cmd = currentInput.trim()

        // Add to command history
        setCommandHistory(prev => [...prev, cmd])
        setHistoryIndex(-1)

        // Handle clear command
        if (cmd.toLowerCase() === "clear") {
            setHistory([])
            setCurrentInput("")
            return
        }

        // Execute command
        const result = executeCommand(cmd, expectedCommands)

        // Build new history entries
        const newEntries: HistoryEntry[] = [
            { type: "input", content: `${prompt}${cmd}` }
        ]

        if (result.output) {
            newEntries.push({ type: "output", content: result.output })
        }

        // Check if this was an expected command
        if (result.isExpected && expectedCommands) {
            const expected = expectedCommands.find(
                ec => normalizeCommand(ec.command) === normalizeCommand(cmd)
            )
            if (expected) {
                setCompletedCommands(prev => new Set([...prev, normalizeCommand(cmd)]))
                if (expected.successMessage) {
                    newEntries.push({ type: "success", content: `✓ ${expected.successMessage}` })
                }
            }
        }

        setHistory(prev => [...prev, ...newEntries])
        setCurrentInput("")

        // Callback
        onCommandExecuted?.(cmd, result.isExpected)

        // Check if all expected commands completed
        const updatedCompleted = new Set([...completedCommands, normalizeCommand(cmd)])
        const allCompleted = expectedCommands.every(
            ec => updatedCompleted.has(normalizeCommand(ec.command))
        )

        if (allCompleted && expectedCommands.length > 0) {
            onComplete?.([...commandHistory, cmd])
        }
    }, [currentInput, expectedCommands, prompt, completedCommands, commandHistory, onCommandExecuted, onComplete])

    // Handle key events
    const handleKeyDown = useCallback((e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === "Enter") {
            e.preventDefault()
            handleExecute()
        } else if (e.key === "ArrowUp") {
            e.preventDefault()
            if (commandHistory.length > 0) {
                const newIndex = historyIndex === -1
                    ? commandHistory.length - 1
                    : Math.max(0, historyIndex - 1)
                setHistoryIndex(newIndex)
                setCurrentInput(commandHistory[newIndex])
            }
        } else if (e.key === "ArrowDown") {
            e.preventDefault()
            if (historyIndex !== -1) {
                const newIndex = historyIndex + 1
                if (newIndex >= commandHistory.length) {
                    setHistoryIndex(-1)
                    setCurrentInput("")
                } else {
                    setHistoryIndex(newIndex)
                    setCurrentInput(commandHistory[newIndex])
                }
            }
        } else if (e.key === "Tab") {
            e.preventDefault()
            // Simple tab completion for common commands
            const partialCmd = currentInput.toLowerCase()
            const completions = Object.keys(mockResponses).filter(
                cmd => cmd.toLowerCase().startsWith(partialCmd)
            )
            if (completions.length === 1) {
                setCurrentInput(completions[0])
            }
        }
    }, [handleExecute, commandHistory, historyIndex, currentInput])

    // Reset terminal
    const handleReset = useCallback(() => {
        setHistory([])
        setCommandHistory([])
        setCompletedCommands(new Set())
        setCurrentInput("")
        setHistoryIndex(-1)
    }, [])

    // Calculate progress
    const progress = expectedCommands.length > 0
        ? (completedCommands.size / expectedCommands.length) * 100
        : 0

    const allComplete = expectedCommands.length > 0 &&
        completedCommands.size === expectedCommands.length

    return (
        <div className={cn("rounded-xl overflow-hidden border border-neutral-800", className)}>
            {/* Header */}
            <div className="flex items-center justify-between px-4 py-2 bg-neutral-800/50 border-b border-neutral-800">
                <div className="flex items-center gap-2">
                    {/* Terminal dots */}
                    <div className="flex items-center gap-1.5">
                        <div className="w-3 h-3 rounded-full bg-red-500/80" />
                        <div className="w-3 h-3 rounded-full bg-yellow-500/80" />
                        <div className="w-3 h-3 rounded-full bg-green-500/80" />
                    </div>

                    <div className="flex items-center gap-1.5 ml-3 text-neutral-400 text-sm">
                        <Terminal className="h-3.5 w-3.5" />
                        <span>Interactive Terminal</span>
                    </div>
                </div>

                <div className="flex items-center gap-2">
                    {/* Progress indicator */}
                    {expectedCommands.length > 0 && (
                        <div className="flex items-center gap-2 text-xs">
                            <span className="text-neutral-500">
                                {completedCommands.size}/{expectedCommands.length}
                            </span>
                            <div className="w-16 h-1.5 bg-neutral-700 rounded-full overflow-hidden">
                                <div
                                    className={cn(
                                        "h-full transition-all duration-300",
                                        allComplete ? "bg-green-500" : "bg-primary-500"
                                    )}
                                    style={{ width: `${progress}%` }}
                                />
                            </div>
                            {allComplete && (
                                <CheckCircle2 className="h-4 w-4 text-green-500" />
                            )}
                        </div>
                    )}

                    {/* Hint button */}
                    {hints.length > 0 && (
                        <button
                            onClick={() => setShowHints(!showHints)}
                            className={cn(
                                "p-1.5 rounded-md transition-colors",
                                showHints
                                    ? "bg-yellow-500/20 text-yellow-400"
                                    : "text-neutral-400 hover:text-yellow-400"
                            )}
                            aria-label="Toggle hints"
                        >
                            <Lightbulb className="h-4 w-4" />
                        </button>
                    )}

                    {/* Reset button */}
                    <button
                        onClick={handleReset}
                        className="p-1.5 rounded-md text-neutral-400 hover:text-white transition-colors"
                        aria-label="Reset terminal"
                    >
                        <RotateCcw className="h-4 w-4" />
                    </button>
                </div>
            </div>

            {/* Expected Commands List */}
            {expectedCommands.length > 0 && (
                <div className="px-4 py-2 bg-neutral-900/50 border-b border-neutral-800">
                    <p className="text-xs text-neutral-500 mb-2">Complete these commands:</p>
                    <div className="flex flex-wrap gap-2">
                        {expectedCommands.map((ec, idx) => {
                            const isComplete = completedCommands.has(normalizeCommand(ec.command))
                            return (
                                <div
                                    key={idx}
                                    className={cn(
                                        "flex items-center gap-1.5 px-2 py-1 rounded-md text-xs font-mono",
                                        isComplete
                                            ? "bg-green-500/20 text-green-400 line-through"
                                            : "bg-neutral-800 text-neutral-300"
                                    )}
                                >
                                    {isComplete ? (
                                        <CheckCircle2 className="h-3 w-3" />
                                    ) : (
                                        <XCircle className="h-3 w-3 text-neutral-500" />
                                    )}
                                    <code>{ec.command}</code>
                                </div>
                            )
                        })}
                    </div>
                </div>
            )}

            {/* Hints Panel */}
            {showHints && hints.length > 0 && (
                <div className="px-4 py-3 bg-yellow-500/10 border-b border-yellow-500/20">
                    <div className="flex items-start gap-2">
                        <Lightbulb className="h-4 w-4 text-yellow-400 mt-0.5 flex-shrink-0" />
                        <div className="flex-1">
                            <p className="text-sm text-yellow-200">
                                {hints[currentHintIndex]}
                            </p>
                            {hints.length > 1 && (
                                <button
                                    onClick={() => setCurrentHintIndex((currentHintIndex + 1) % hints.length)}
                                    className="text-xs text-yellow-400 hover:text-yellow-300 mt-1"
                                >
                                    Next hint ({currentHintIndex + 1}/{hints.length})
                                </button>
                            )}
                        </div>
                    </div>
                </div>
            )}

            {/* Terminal Body */}
            <div
                ref={terminalRef}
                onClick={handleTerminalClick}
                className={cn(
                    "bg-neutral-950 p-4 font-mono text-sm",
                    "min-h-[200px] max-h-[400px] overflow-y-auto",
                    "cursor-text"
                )}
            >
                {/* History */}
                {history.map((entry, idx) => (
                    <div
                        key={idx}
                        className={cn(
                            "whitespace-pre-wrap break-all",
                            entry.type === "input" && "text-green-400",
                            entry.type === "output" && "text-neutral-300",
                            entry.type === "success" && "text-green-500 font-medium",
                            entry.type === "error" && "text-red-400"
                        )}
                    >
                        {entry.content}
                    </div>
                ))}

                {/* Current Input Line */}
                {!readOnly && (
                    <div className="flex items-center text-green-400">
                        <span>{prompt}</span>
                        <input
                            ref={inputRef}
                            type="text"
                            value={currentInput}
                            onChange={(e) => setCurrentInput(e.target.value)}
                            onKeyDown={handleKeyDown}
                            className={cn(
                                "flex-1 bg-transparent border-none outline-none",
                                "text-white font-mono caret-white"
                            )}
                            autoComplete="off"
                            autoCorrect="off"
                            autoCapitalize="off"
                            spellCheck={false}
                        />
                        <span className="animate-pulse text-white">▌</span>
                    </div>
                )}
            </div>
        </div>
    )
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default TerminalEmulator
