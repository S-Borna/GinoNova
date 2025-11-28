"use client"

/**
 * ============================================================================
 * CONTENT BLOCK RENDERER - Renders All Interactive Content Blocks
 * ============================================================================
 *
 * This component renders an array of content blocks for interactive tasks:
 * - TextBlock: Markdown content
 * - CodeBlock: Syntax-highlighted code
 * - TerminalBlock: Interactive terminal
 * - QuizBlock: Multiple choice questions
 * - CheckpointBlock: Progress milestones
 *
 * @phase ILE Phase 3 - Content Blocks
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { TextBlock } from "./TextBlock"
import { LearningCodeBlock } from "./CodeBlock"
import { QuizBlock, QuizOption } from "./QuizBlock"
import { CheckpointBlock } from "./CheckpointBlock"
import { TerminalEmulator, TerminalCommand } from "@/components/content/TerminalEmulator"

/* ============================================================================
   TYPES
   ============================================================================ */

// Content block types from backend
interface TextBlockType {
    type: "text"
    content: string
}

interface CodeBlockType {
    type: "code"
    language: string
    code: string
    filename?: string
    highlight_lines?: number[]
    explanation?: string
}

interface ExpectedCommand {
    command: string
    regex?: string
    output?: string
    explanation: string
    allow_variations?: boolean
}

interface TerminalBlockType {
    type: "terminal"
    id?: string
    instructions: string
    expected_commands: ExpectedCommand[]
    hints?: string[]
}

interface QuizBlockType {
    type: "quiz"
    id?: string
    question: string
    options: QuizOption[]
    explanation: string
    xp_bonus?: number
}

interface CheckpointBlockType {
    type: "checkpoint"
    title: string
    description: string
}

type ContentBlock =
    | TextBlockType
    | CodeBlockType
    | TerminalBlockType
    | QuizBlockType
    | CheckpointBlockType

// Progress tracking types
interface BlockProgress {
    block_index: number
    completed: boolean
    attempts: number
    completed_at?: string
}

interface QuizAnswer {
    block_index: number
    selected_option: number
    is_correct: boolean
    answered_at: string
}

interface TerminalCommandRecord {
    block_index: number
    command_index: number
    command: string
    was_correct: boolean
    timestamp: string
}

interface TaskProgress {
    user_id: string
    task_id: string
    status: string
    block_progress: BlockProgress[]
    quiz_answers: QuizAnswer[]
    terminal_history: TerminalCommandRecord[]
    started_at?: string
    completed_at?: string
    total_time_spent: number
    xp_earned: number
}

// API result types
interface QuizResult {
    is_correct: boolean
    feedback?: string
    explanation: string
    xp_bonus?: number
}

interface TerminalResult {
    is_correct: boolean
    feedback?: string
    hint?: string
    expected_output?: string
}

export interface ContentBlockRendererProps {
    blocks: ContentBlock[]
    taskId: string
    progress?: TaskProgress
    onBlockComplete: (blockIndex: number, blockType: string) => void
    onQuizAnswer: (blockIndex: number, optionIndex: number) => Promise<QuizResult>
    onTerminalCommand: (blockIndex: number, commandIndex: number, command: string, wasCorrect: boolean) => Promise<TerminalResult>
    className?: string
}

/* ============================================================================
   HELPER FUNCTIONS
   ============================================================================ */

function convertExpectedCommands(commands: ExpectedCommand[]): TerminalCommand[] {
    return commands.map(cmd => ({
        command: cmd.command,
        output: cmd.output,
        description: cmd.explanation,
        successMessage: cmd.explanation,
    }))
}

function calculateXpSoFar(progress: TaskProgress | undefined, blocks: ContentBlock[]): number {
    if (!progress) return 0

    let xp = 0

    // Add XP for correct quiz answers
    for (const answer of progress.quiz_answers) {
        if (answer.is_correct) {
            const block = blocks[answer.block_index]
            if (block && block.type === "quiz") {
                xp += (block as QuizBlockType).xp_bonus || 5
            }
        }
    }

    return xp
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function ContentBlockRenderer({
    blocks,
    taskId,
    progress,
    onBlockComplete,
    onQuizAnswer,
    onTerminalCommand,
    className,
}: ContentBlockRendererProps) {

    // Find quiz answer for a specific block
    const getQuizAnswer = (blockIndex: number) => {
        if (!progress) return undefined
        const answer = progress.quiz_answers.find(a => a.block_index === blockIndex)
        if (!answer) return undefined
        return {
            selectedOption: answer.selected_option,
            isCorrect: answer.is_correct,
        }
    }

    // Check if terminal block is completed
    const isTerminalCompleted = (blockIndex: number, expectedCommands: ExpectedCommand[]) => {
        if (!progress) return false
        const commands = progress.terminal_history.filter(c => c.block_index === blockIndex && c.was_correct)
        return commands.length >= expectedCommands.length
    }

    // Calculate XP earned so far
    const xpSoFar = calculateXpSoFar(progress, blocks)

    return (
        <div className={cn("space-y-6", className)}>
            {blocks.map((block, index) => {
                const key = `block-${index}`

                switch (block.type) {
                    case "text":
                        return (
                            <TextBlock
                                key={key}
                                content={block.content}
                            />
                        )

                    case "code":
                        return (
                            <LearningCodeBlock
                                key={key}
                                language={block.language}
                                code={block.code}
                                filename={block.filename}
                                highlightLines={block.highlight_lines}
                                explanation={block.explanation}
                            />
                        )

                    case "terminal":
                        const terminalCommands = convertExpectedCommands(block.expected_commands)
                        return (
                            <div key={key} className="space-y-2">
                                {block.instructions && (
                                    <p className="text-sm text-neutral-400">
                                        {block.instructions}
                                    </p>
                                )}
                                <TerminalEmulator
                                    blockId={block.id || `terminal-${index}`}
                                    expectedCommands={terminalCommands}
                                    hints={block.hints}
                                    onCommandExecuted={(command, isCorrect) => {
                                        // Find which command index this matches
                                        const cmdIndex = block.expected_commands.findIndex(
                                            ec => ec.command.toLowerCase() === command.toLowerCase()
                                        )
                                        onTerminalCommand(index, cmdIndex >= 0 ? cmdIndex : 0, command, isCorrect)
                                    }}
                                    onComplete={() => {
                                        onBlockComplete(index, "terminal")
                                    }}
                                />
                            </div>
                        )

                    case "quiz":
                        const quizAnswer = getQuizAnswer(index)
                        return (
                            <QuizBlock
                                key={key}
                                blockId={block.id || `quiz-${index}`}
                                question={block.question}
                                options={block.options}
                                explanation={block.explanation}
                                xpBonus={block.xp_bonus}
                                answered={quizAnswer}
                                onAnswer={async (_, optionIndex) => {
                                    await onQuizAnswer(index, optionIndex)
                                }}
                            />
                        )

                    case "checkpoint":
                        return (
                            <CheckpointBlock
                                key={key}
                                title={block.title}
                                description={block.description}
                                xpSoFar={xpSoFar}
                                isReached={true}
                            />
                        )

                    default:
                        console.warn("Unknown block type:", (block as any).type)
                        return null
                }
            })}
        </div>
    )
}

export default ContentBlockRenderer
