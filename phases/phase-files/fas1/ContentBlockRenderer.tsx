"use client"

/**
 * ============================================================================
 * CONTENT BLOCK RENDERER — Renders All Interactive Content Blocks
 * ============================================================================
 *
 * Renders an array of content blocks for interactive tasks:
 * - TextBlock: Markdown content
 * - CodeBlock: Syntax-highlighted code with shell toggle
 * - TerminalBlock: Interactive terminal
 * - QuizBlock: Multiple choice questions
 * - CheckpointBlock: Progress milestones
 *
 * @phase FAS 1.2 - Fix content block rendering
 */

import * as React from "react"
import { useState } from "react"
import ReactMarkdown from "react-markdown"
import remarkGfm from "remark-gfm"
import { LearningCodeBlock } from "./LearningCodeBlock"
import { 
  CheckCircle2, 
  Circle, 
  Lightbulb, 
  Terminal,
  ChevronDown,
  ChevronRight,
  AlertCircle,
  Award
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface TextBlockType {
  type: "text"
  content: string
}

interface CodeBlockType {
  type: "code"
  language: string
  code: string | object
  filename?: string
  highlight_lines?: number[]
  explanation?: string
  available_shells?: string[]
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

interface QuizOption {
  text: string
  is_correct: boolean
  feedback?: string
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

interface ContentBlockRendererProps {
  blocks: ContentBlock[]
  onBlockComplete?: (blockIndex: number) => void
  onQuizAnswer?: (blockIndex: number, optionIndex: number, isCorrect: boolean) => void
  onTerminalCommand?: (blockIndex: number, command: string, isCorrect: boolean) => void
  completedBlocks?: number[]
  className?: string
}

/* ============================================================================
   HELPER: Safe string conversion
   ============================================================================ */

function safeString(value: unknown): string {
  if (value === null || value === undefined) return ''
  if (typeof value === 'string') return value
  if (typeof value === 'object') {
    try {
      return JSON.stringify(value, null, 2)
    } catch {
      return String(value)
    }
  }
  return String(value)
}

/* ============================================================================
   TEXT BLOCK COMPONENT
   ============================================================================ */

function TextBlock({ content }: { content: string }) {
  const safeContent = safeString(content)
  
  return (
    <div className="prose prose-invert prose-lg max-w-none">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          h1: ({ children }) => (
            <h1 className="text-2xl font-bold text-white mt-8 mb-4 first:mt-0">{children}</h1>
          ),
          h2: ({ children }) => (
            <h2 className="text-xl font-semibold text-white mt-6 mb-3 flex items-center gap-2">
              <span className="w-1 h-6 bg-indigo-500 rounded-full" />
              {children}
            </h2>
          ),
          h3: ({ children }) => (
            <h3 className="text-lg font-medium text-gray-200 mt-4 mb-2">{children}</h3>
          ),
          p: ({ children }) => (
            <p className="text-gray-300 leading-relaxed mb-4">{children}</p>
          ),
          ul: ({ children }) => (
            <ul className="space-y-2 mb-4 ml-4">{children}</ul>
          ),
          li: ({ children }) => (
            <li className="text-gray-300 flex items-start gap-2">
              <span className="text-indigo-400 mt-1.5">•</span>
              <span>{children}</span>
            </li>
          ),
          code: ({ className, children }) => {
            const isInline = !className
            if (isInline) {
              return (
                <code className="px-1.5 py-0.5 bg-gray-800 rounded text-indigo-300 text-sm font-mono">
                  {children}
                </code>
              )
            }
            return <code className={className}>{children}</code>
          },
          blockquote: ({ children }) => (
            <blockquote className="border-l-4 border-indigo-500 pl-4 py-2 my-4 bg-indigo-500/10 rounded-r-lg">
              <div className="text-gray-300 italic">{children}</div>
            </blockquote>
          ),
          strong: ({ children }) => (
            <strong className="font-semibold text-white">{children}</strong>
          ),
        }}
      >
        {safeContent}
      </ReactMarkdown>
    </div>
  )
}

/* ============================================================================
   QUIZ BLOCK COMPONENT
   ============================================================================ */

interface QuizBlockProps {
  question: string
  options: QuizOption[]
  explanation: string
  xpBonus?: number
  onAnswer?: (optionIndex: number, isCorrect: boolean) => void
}

function QuizBlock({ question, options, explanation, xpBonus, onAnswer }: QuizBlockProps) {
  const [selectedOption, setSelectedOption] = useState<number | null>(null)
  const [showExplanation, setShowExplanation] = useState(false)

  const handleSelect = (index: number) => {
    if (selectedOption !== null) return // Already answered
    
    setSelectedOption(index)
    setShowExplanation(true)
    
    const isCorrect = options[index]?.is_correct || false
    onAnswer?.(index, isCorrect)
  }

  return (
    <div className="bg-gray-900/50 rounded-xl border border-gray-800 overflow-hidden">
      {/* Header */}
      <div className="flex items-center gap-2 px-4 py-3 bg-gray-800/50 border-b border-gray-800">
        <AlertCircle className="w-5 h-5 text-yellow-400" />
        <span className="font-medium text-white">Knowledge Check</span>
        {xpBonus && (
          <span className="ml-auto text-sm text-yellow-400">+{xpBonus} XP</span>
        )}
      </div>

      {/* Question */}
      <div className="p-4">
        <p className="text-lg text-white mb-4">{safeString(question)}</p>

        {/* Options */}
        <div className="space-y-2">
          {options.map((option, index) => {
            const isSelected = selectedOption === index
            const isCorrect = option.is_correct
            const showResult = selectedOption !== null

            let optionStyle = "border-gray-700 hover:border-gray-600 hover:bg-gray-800/50"
            if (showResult) {
              if (isCorrect) {
                optionStyle = "border-green-500 bg-green-500/10"
              } else if (isSelected && !isCorrect) {
                optionStyle = "border-red-500 bg-red-500/10"
              } else {
                optionStyle = "border-gray-800 opacity-50"
              }
            }

            return (
              <button
                key={index}
                onClick={() => handleSelect(index)}
                disabled={selectedOption !== null}
                className={`w-full flex items-center gap-3 p-3 rounded-lg border transition-all text-left ${optionStyle}`}
              >
                <div className={`w-5 h-5 rounded-full border-2 flex items-center justify-center ${
                  showResult && isCorrect ? 'border-green-500 bg-green-500' :
                  showResult && isSelected ? 'border-red-500 bg-red-500' :
                  'border-gray-600'
                }`}>
                  {showResult && isCorrect && <CheckCircle2 className="w-3 h-3 text-white" />}
                </div>
                <span className={`${showResult && isCorrect ? 'text-green-400' : 'text-gray-300'}`}>
                  {safeString(option.text)}
                </span>
              </button>
            )
          })}
        </div>

        {/* Explanation */}
        {showExplanation && (
          <div className="mt-4 p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-lg">
            <div className="flex items-start gap-2">
              <Lightbulb className="w-5 h-5 text-indigo-400 mt-0.5" />
              <p className="text-sm text-gray-300">{safeString(explanation)}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

/* ============================================================================
   TERMINAL BLOCK COMPONENT
   ============================================================================ */

interface TerminalBlockProps {
  instructions: string
  expectedCommands: ExpectedCommand[]
  hints?: string[]
  onCommand?: (command: string, isCorrect: boolean) => void
}

function TerminalBlock({ instructions, expectedCommands, hints, onCommand }: TerminalBlockProps) {
  const [input, setInput] = useState("")
  const [history, setHistory] = useState<Array<{ command: string; output: string; isCorrect: boolean }>>([])
  const [currentCommandIndex, setCurrentCommandIndex] = useState(0)
  const [showHint, setShowHint] = useState(false)
  const [hintIndex, setHintIndex] = useState(0)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim()) return

    const expectedCommand = expectedCommands[currentCommandIndex]
    if (!expectedCommand) return

    // Check if command matches
    let isCorrect = false
    if (expectedCommand.regex) {
      isCorrect = new RegExp(expectedCommand.regex).test(input.trim())
    } else {
      isCorrect = input.trim() === expectedCommand.command
    }

    // Add to history
    const output = isCorrect 
      ? expectedCommand.output || "✓ Correct!"
      : `✗ Try again. ${expectedCommand.explanation}`

    setHistory(prev => [...prev, { command: input, output, isCorrect }])
    onCommand?.(input, isCorrect)

    if (isCorrect) {
      setCurrentCommandIndex(prev => prev + 1)
      setShowHint(false)
      setHintIndex(0)
    }

    setInput("")
  }

  const handleShowHint = () => {
    if (hints && hints.length > 0) {
      setShowHint(true)
      setHintIndex(prev => Math.min(prev + 1, hints.length - 1))
    }
  }

  const isComplete = currentCommandIndex >= expectedCommands.length

  return (
    <div className="bg-gray-900 rounded-xl border border-gray-800 overflow-hidden">
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-2 bg-gray-800 border-b border-gray-700">
        <div className="flex items-center gap-2">
          <Terminal className="w-4 h-4 text-green-400" />
          <span className="text-sm font-medium text-gray-300">Terminal Practice</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-xs text-gray-500">
            {currentCommandIndex}/{expectedCommands.length} commands
          </span>
          {isComplete && (
            <span className="px-2 py-0.5 bg-green-500/20 text-green-400 text-xs rounded">
              Complete!
            </span>
          )}
        </div>
      </div>

      {/* Instructions */}
      <div className="px-4 py-3 bg-gray-800/50 border-b border-gray-800">
        <p className="text-sm text-gray-300">{safeString(instructions)}</p>
      </div>

      {/* Terminal */}
      <div className="p-4 font-mono text-sm">
        {/* History */}
        {history.map((entry, i) => (
          <div key={i} className="mb-2">
            <div className="flex items-center gap-2">
              <span className="text-green-400">$</span>
              <span className="text-white">{entry.command}</span>
            </div>
            <div className={`ml-4 ${entry.isCorrect ? 'text-green-400' : 'text-red-400'}`}>
              {entry.output}
            </div>
          </div>
        ))}

        {/* Input */}
        {!isComplete && (
          <form onSubmit={handleSubmit} className="flex items-center gap-2">
            <span className="text-green-400">$</span>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder={expectedCommands[currentCommandIndex]?.command || "Enter command..."}
              className="flex-1 bg-transparent text-white outline-none placeholder:text-gray-600"
              autoFocus
            />
          </form>
        )}

        {/* Hint */}
        {showHint && hints && hints[hintIndex] && (
          <div className="mt-3 p-2 bg-yellow-500/10 border border-yellow-500/30 rounded">
            <p className="text-sm text-yellow-300">
              <Lightbulb className="w-4 h-4 inline mr-1" />
              {hints[hintIndex]}
            </p>
          </div>
        )}
      </div>

      {/* Actions */}
      {!isComplete && hints && hints.length > 0 && (
        <div className="px-4 py-2 bg-gray-800/50 border-t border-gray-800">
          <button
            onClick={handleShowHint}
            className="text-sm text-gray-400 hover:text-white transition-colors"
          >
            Need a hint? ({hintIndex + 1}/{hints.length})
          </button>
        </div>
      )}
    </div>
  )
}

/* ============================================================================
   CHECKPOINT BLOCK COMPONENT
   ============================================================================ */

interface CheckpointBlockProps {
  title: string
  description: string
  isComplete?: boolean
  onComplete?: () => void
}

function CheckpointBlock({ title, description, isComplete, onComplete }: CheckpointBlockProps) {
  return (
    <div className={`rounded-xl border-2 overflow-hidden transition-all ${
      isComplete 
        ? 'border-green-500 bg-green-500/10' 
        : 'border-indigo-500 bg-indigo-500/10'
    }`}>
      <div className="flex items-center gap-3 px-4 py-3">
        <div className={`w-10 h-10 rounded-full flex items-center justify-center ${
          isComplete ? 'bg-green-500' : 'bg-indigo-500'
        }`}>
          {isComplete ? (
            <CheckCircle2 className="w-6 h-6 text-white" />
          ) : (
            <Award className="w-6 h-6 text-white" />
          )}
        </div>
        <div className="flex-1">
          <h4 className="font-semibold text-white">{safeString(title)}</h4>
          <p className="text-sm text-gray-400">{safeString(description)}</p>
        </div>
        {!isComplete && onComplete && (
          <button
            onClick={onComplete}
            className="px-4 py-2 bg-indigo-500 hover:bg-indigo-600 text-white text-sm font-medium rounded-lg transition-colors"
          >
            Mark Complete
          </button>
        )}
      </div>
    </div>
  )
}

/* ============================================================================
   MAIN RENDERER
   ============================================================================ */

export function ContentBlockRenderer({
  blocks,
  onBlockComplete,
  onQuizAnswer,
  onTerminalCommand,
  completedBlocks = [],
  className = "",
}: ContentBlockRendererProps) {
  if (!blocks || !Array.isArray(blocks)) {
    return (
      <div className="text-gray-500 italic">
        No content available for this task.
      </div>
    )
  }

  return (
    <div className={`space-y-6 ${className}`}>
      {blocks.map((block, index) => {
        if (!block || typeof block !== 'object') {
          return null
        }

        const key = `block-${index}`

        switch (block.type) {
          case 'text':
            return (
              <TextBlock
                key={key}
                content={(block as TextBlockType).content}
              />
            )

          case 'code':
            const codeBlock = block as CodeBlockType
            return (
              <LearningCodeBlock
                key={key}
                language={codeBlock.language || 'bash'}
                code={codeBlock.code}
                filename={codeBlock.filename}
                highlightLines={codeBlock.highlight_lines}
                explanation={codeBlock.explanation}
                availableShells={codeBlock.available_shells}
              />
            )

          case 'terminal':
            const terminalBlock = block as TerminalBlockType
            return (
              <TerminalBlock
                key={key}
                instructions={terminalBlock.instructions}
                expectedCommands={terminalBlock.expected_commands || []}
                hints={terminalBlock.hints}
                onCommand={(cmd, correct) => onTerminalCommand?.(index, cmd, correct)}
              />
            )

          case 'quiz':
            const quizBlock = block as QuizBlockType
            return (
              <QuizBlock
                key={key}
                question={quizBlock.question}
                options={quizBlock.options || []}
                explanation={quizBlock.explanation}
                xpBonus={quizBlock.xp_bonus}
                onAnswer={(optIdx, correct) => onQuizAnswer?.(index, optIdx, correct)}
              />
            )

          case 'checkpoint':
            const checkpointBlock = block as CheckpointBlockType
            return (
              <CheckpointBlock
                key={key}
                title={checkpointBlock.title}
                description={checkpointBlock.description}
                isComplete={completedBlocks.includes(index)}
                onComplete={() => onBlockComplete?.(index)}
              />
            )

          default:
            // Unknown block type - render as JSON for debugging
            return (
              <div key={key} className="p-4 bg-red-900/20 border border-red-500/50 rounded-lg">
                <p className="text-sm text-red-400 mb-2">Unknown block type: {(block as any).type}</p>
                <pre className="text-xs text-gray-400 overflow-auto">
                  {JSON.stringify(block, null, 2)}
                </pre>
              </div>
            )
        }
      })}
    </div>
  )
}

export default ContentBlockRenderer
