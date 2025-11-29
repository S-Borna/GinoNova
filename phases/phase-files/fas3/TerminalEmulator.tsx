"use client"

/**
 * ============================================================================
 * TERMINAL EMULATOR — Interactive Shell for Learning
 * ============================================================================
 * 
 * Features:
 * - Command history (up/down arrows)
 * - Tab completion
 * - Command validation against expected outputs
 * - Hints system
 * - Multiple shell modes (bash, python, etc.)
 * - Copy/paste support
 * - Simulated filesystem
 * 
 * @phase FAS 3.1 - Terminal integration
 * @location apps/frontend/src/components/content/TerminalEmulator.tsx
 */

import * as React from "react"
import { useState, useEffect, useRef, useCallback } from "react"
import { 
  Terminal as TerminalIcon, 
  Copy, 
  Check, 
  Lightbulb,
  RotateCcw,
  Maximize2,
  Minimize2,
  X
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface ExpectedCommand {
  command: string
  regex?: string
  output?: string
  explanation: string
  allow_variations?: boolean
}

interface HistoryEntry {
  command: string
  output: string
  isCorrect: boolean
  timestamp: Date
}

interface TerminalEmulatorProps {
  id?: string
  title?: string
  instructions?: string
  expectedCommands?: ExpectedCommand[]
  hints?: string[]
  initialDirectory?: string
  shellType?: 'bash' | 'python' | 'node'
  onComplete?: () => void
  onCommandExecuted?: (command: string, isCorrect: boolean) => void
  className?: string
}

/* ============================================================================
   SIMULATED FILESYSTEM
   ============================================================================ */

const SIMULATED_FS: Record<string, string[]> = {
  '~': ['documents', 'projects', 'scripts', '.bashrc', '.profile'],
  '~/documents': ['notes.txt', 'readme.md'],
  '~/projects': ['devops-app', 'terraform-config', 'kubernetes-manifests'],
  '~/scripts': ['deploy.sh', 'backup.sh', 'monitor.py'],
  '~/projects/devops-app': ['src', 'tests', 'Dockerfile', 'docker-compose.yml', 'package.json'],
}

const SIMULATED_FILE_CONTENTS: Record<string, string> = {
  '~/scripts/deploy.sh': `#!/bin/bash
# Deployment script
echo "Starting deployment..."
docker-compose up -d
echo "Deployment complete!"`,
  '~/.bashrc': `# ~/.bashrc
export PATH=$PATH:/usr/local/bin
alias ll='ls -la'
alias gs='git status'`,
}

/* ============================================================================
   BUILT-IN COMMANDS
   ============================================================================ */

function executeBuiltInCommand(
  command: string, 
  currentDir: string
): { output: string; newDir?: string } | null {
  const parts = command.trim().split(/\s+/)
  const cmd = parts[0]
  const args = parts.slice(1)

  switch (cmd) {
    case 'pwd':
      return { output: currentDir.replace('~', '/home/user') }
    
    case 'ls':
      const lsDir = args[0] ? `${currentDir}/${args[0]}`.replace('//', '/') : currentDir
      const contents = SIMULATED_FS[lsDir] || SIMULATED_FS[currentDir]
      if (contents) {
        if (args.includes('-la') || args.includes('-l')) {
          return { 
            output: contents.map(f => 
              `${f.includes('.') ? '-rw-r--r--' : 'drwxr-xr-x'}  1 user user  4096 Nov 29 10:00 ${f}`
            ).join('\n')
          }
        }
        return { output: contents.join('  ') }
      }
      return { output: `ls: cannot access '${lsDir}': No such file or directory` }
    
    case 'cd':
      const target = args[0] || '~'
      if (target === '..') {
        const parentDir = currentDir.split('/').slice(0, -1).join('/') || '~'
        return { output: '', newDir: parentDir }
      }
      const newPath = target.startsWith('~') ? target : `${currentDir}/${target}`
      if (SIMULATED_FS[newPath]) {
        return { output: '', newDir: newPath }
      }
      return { output: `cd: ${target}: No such file or directory` }
    
    case 'cat':
      const filePath = args[0]?.startsWith('~') ? args[0] : `${currentDir}/${args[0]}`
      const content = SIMULATED_FILE_CONTENTS[filePath]
      if (content) {
        return { output: content }
      }
      return { output: `cat: ${args[0]}: No such file or directory` }
    
    case 'echo':
      return { output: args.join(' ').replace(/["']/g, '') }
    
    case 'whoami':
      return { output: 'devops-student' }
    
    case 'date':
      return { output: new Date().toString() }
    
    case 'clear':
      return { output: '__CLEAR__' }
    
    case 'help':
      return { 
        output: `Available commands:
  pwd     - Print working directory
  ls      - List directory contents
  cd      - Change directory
  cat     - Display file contents
  echo    - Print text
  whoami  - Print current user
  date    - Print current date
  clear   - Clear terminal
  help    - Show this help`
      }
    
    default:
      return null
  }
}

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function TerminalEmulator({
  id,
  title = "Terminal",
  instructions,
  expectedCommands = [],
  hints = [],
  initialDirectory = "~",
  shellType = "bash",
  onComplete,
  onCommandExecuted,
  className = "",
}: TerminalEmulatorProps) {
  const [input, setInput] = useState("")
  const [history, setHistory] = useState<HistoryEntry[]>([])
  const [historyIndex, setHistoryIndex] = useState(-1)
  const [currentDir, setCurrentDir] = useState(initialDirectory)
  const [currentCommandIndex, setCurrentCommandIndex] = useState(0)
  const [showHints, setShowHints] = useState(false)
  const [hintIndex, setHintIndex] = useState(0)
  const [isFullscreen, setIsFullscreen] = useState(false)
  const [copied, setCopied] = useState(false)
  
  const inputRef = useRef<HTMLInputElement>(null)
  const terminalRef = useRef<HTMLDivElement>(null)

  const isComplete = currentCommandIndex >= expectedCommands.length && expectedCommands.length > 0

  // Auto-scroll to bottom
  useEffect(() => {
    if (terminalRef.current) {
      terminalRef.current.scrollTop = terminalRef.current.scrollHeight
    }
  }, [history])

  // Focus input on click
  const focusInput = useCallback(() => {
    inputRef.current?.focus()
  }, [])

  // Handle command execution
  const executeCommand = useCallback(() => {
    if (!input.trim()) return

    const command = input.trim()
    let output = ""
    let isCorrect = false

    // Check if it's a built-in command first
    const builtInResult = executeBuiltInCommand(command, currentDir)
    
    if (builtInResult) {
      if (builtInResult.output === '__CLEAR__') {
        setHistory([])
        setInput("")
        return
      }
      output = builtInResult.output
      if (builtInResult.newDir) {
        setCurrentDir(builtInResult.newDir)
      }
    }

    // Check against expected commands
    if (expectedCommands.length > 0 && currentCommandIndex < expectedCommands.length) {
      const expected = expectedCommands[currentCommandIndex]
      
      if (expected.regex) {
        isCorrect = new RegExp(expected.regex).test(command)
      } else if (expected.allow_variations) {
        // Allow minor variations (extra spaces, quotes, etc.)
        const normalizedCommand = command.replace(/\s+/g, ' ').trim()
        const normalizedExpected = expected.command.replace(/\s+/g, ' ').trim()
        isCorrect = normalizedCommand === normalizedExpected
      } else {
        isCorrect = command === expected.command
      }

      if (isCorrect) {
        output = expected.output || output || "✓ Correct!"
        setCurrentCommandIndex(prev => prev + 1)
        setShowHints(false)
        setHintIndex(0)
        
        // Check if all commands complete
        if (currentCommandIndex + 1 >= expectedCommands.length) {
          onComplete?.()
        }
      } else if (!builtInResult) {
        output = `Command not recognized. ${expected.explanation}`
      }
    } else if (!builtInResult) {
      output = `${command}: command not found`
    }

    // Add to history
    setHistory(prev => [...prev, {
      command,
      output,
      isCorrect,
      timestamp: new Date()
    }])

    onCommandExecuted?.(command, isCorrect)
    setInput("")
    setHistoryIndex(-1)
  }, [input, currentDir, expectedCommands, currentCommandIndex, onComplete, onCommandExecuted])

  // Handle key events
  const handleKeyDown = useCallback((e: React.KeyboardEvent) => {
    switch (e.key) {
      case 'Enter':
        executeCommand()
        break
      
      case 'ArrowUp':
        e.preventDefault()
        if (history.length > 0) {
          const newIndex = historyIndex < history.length - 1 ? historyIndex + 1 : historyIndex
          setHistoryIndex(newIndex)
          setInput(history[history.length - 1 - newIndex]?.command || "")
        }
        break
      
      case 'ArrowDown':
        e.preventDefault()
        if (historyIndex > 0) {
          const newIndex = historyIndex - 1
          setHistoryIndex(newIndex)
          setInput(history[history.length - 1 - newIndex]?.command || "")
        } else {
          setHistoryIndex(-1)
          setInput("")
        }
        break
      
      case 'Tab':
        e.preventDefault()
        // Simple tab completion
        const files = SIMULATED_FS[currentDir] || []
        const match = files.find(f => f.startsWith(input.split(' ').pop() || ''))
        if (match) {
          const parts = input.split(' ')
          parts[parts.length - 1] = match
          setInput(parts.join(' '))
        }
        break
      
      case 'c':
        if (e.ctrlKey) {
          setInput("")
        }
        break
      
      case 'l':
        if (e.ctrlKey) {
          e.preventDefault()
          setHistory([])
        }
        break
    }
  }, [executeCommand, history, historyIndex, currentDir, input])

  // Copy terminal content
  const copyTerminal = async () => {
    const content = history.map(h => `$ ${h.command}\n${h.output}`).join('\n\n')
    await navigator.clipboard.writeText(content)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  // Reset terminal
  const resetTerminal = () => {
    setHistory([])
    setCurrentCommandIndex(0)
    setCurrentDir(initialDirectory)
    setShowHints(false)
    setHintIndex(0)
    setInput("")
  }

  // Show next hint
  const showNextHint = () => {
    setShowHints(true)
    setHintIndex(prev => Math.min(prev + 1, hints.length - 1))
  }

  // Get prompt string
  const getPrompt = () => {
    const dir = currentDir.replace('~', '~')
    return `${shellType === 'python' ? '>>>' : `devops@hub:${dir}$`}`
  }

  return (
    <div 
      className={`
        ${isFullscreen ? 'fixed inset-4 z-50' : 'relative'}
        bg-gray-900 rounded-xl border border-gray-800 overflow-hidden
        ${className}
      `}
    >
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-2 bg-gray-800 border-b border-gray-700">
        <div className="flex items-center gap-3">
          {/* Traffic lights */}
          <div className="flex items-center gap-1.5">
            <div className="w-3 h-3 rounded-full bg-red-500" />
            <div className="w-3 h-3 rounded-full bg-yellow-500" />
            <div className="w-3 h-3 rounded-full bg-green-500" />
          </div>
          
          <div className="flex items-center gap-2">
            <TerminalIcon className="w-4 h-4 text-gray-400" />
            <span className="text-sm font-medium text-gray-300">{title}</span>
          </div>
        </div>

        <div className="flex items-center gap-2">
          {/* Progress */}
          {expectedCommands.length > 0 && (
            <span className="text-xs text-gray-500">
              {currentCommandIndex}/{expectedCommands.length}
            </span>
          )}
          
          {/* Actions */}
          <button
            onClick={copyTerminal}
            className="p-1.5 rounded hover:bg-gray-700 text-gray-400 hover:text-white transition-colors"
            title="Copy"
          >
            {copied ? <Check className="w-4 h-4 text-green-400" /> : <Copy className="w-4 h-4" />}
          </button>
          
          <button
            onClick={resetTerminal}
            className="p-1.5 rounded hover:bg-gray-700 text-gray-400 hover:text-white transition-colors"
            title="Reset"
          >
            <RotateCcw className="w-4 h-4" />
          </button>
          
          <button
            onClick={() => setIsFullscreen(!isFullscreen)}
            className="p-1.5 rounded hover:bg-gray-700 text-gray-400 hover:text-white transition-colors"
            title={isFullscreen ? "Exit fullscreen" : "Fullscreen"}
          >
            {isFullscreen ? <Minimize2 className="w-4 h-4" /> : <Maximize2 className="w-4 h-4" />}
          </button>
        </div>
      </div>

      {/* Instructions */}
      {instructions && (
        <div className="px-4 py-2 bg-gray-800/50 border-b border-gray-800">
          <p className="text-sm text-gray-400">{instructions}</p>
        </div>
      )}

      {/* Terminal Content */}
      <div 
        ref={terminalRef}
        onClick={focusInput}
        className={`
          font-mono text-sm p-4 overflow-y-auto cursor-text
          ${isFullscreen ? 'h-[calc(100%-120px)]' : 'h-80'}
        `}
      >
        {/* Welcome message */}
        {history.length === 0 && (
          <div className="text-gray-500 mb-4">
            Welcome to DevOpsHub Terminal. Type 'help' for available commands.
          </div>
        )}

        {/* History */}
        {history.map((entry, i) => (
          <div key={i} className="mb-3">
            <div className="flex items-start gap-2">
              <span className="text-green-400 flex-shrink-0">{getPrompt()}</span>
              <span className="text-white">{entry.command}</span>
            </div>
            {entry.output && (
              <div className={`ml-0 mt-1 whitespace-pre-wrap ${
                entry.isCorrect ? 'text-green-400' : 
                entry.output.includes('not found') || entry.output.includes('No such') 
                  ? 'text-red-400' 
                  : 'text-gray-300'
              }`}>
                {entry.output}
              </div>
            )}
          </div>
        ))}

        {/* Current Input */}
        {!isComplete && (
          <div className="flex items-start gap-2">
            <span className="text-green-400 flex-shrink-0">{getPrompt()}</span>
            <input
              ref={inputRef}
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              className="flex-1 bg-transparent text-white outline-none caret-white"
              autoFocus
              spellCheck={false}
              autoComplete="off"
            />
          </div>
        )}

        {/* Completion Message */}
        {isComplete && (
          <div className="mt-4 p-3 bg-green-500/10 border border-green-500/30 rounded-lg">
            <div className="flex items-center gap-2 text-green-400">
              <Check className="w-5 h-5" />
              <span className="font-medium">All commands completed!</span>
            </div>
          </div>
        )}
      </div>

      {/* Hints */}
      {hints.length > 0 && !isComplete && (
        <div className="px-4 py-2 bg-gray-800/50 border-t border-gray-800">
          {showHints && hints[hintIndex] ? (
            <div className="flex items-start gap-2 text-sm">
              <Lightbulb className="w-4 h-4 text-yellow-400 flex-shrink-0 mt-0.5" />
              <p className="text-yellow-300">{hints[hintIndex]}</p>
            </div>
          ) : (
            <button
              onClick={showNextHint}
              className="text-sm text-gray-400 hover:text-white transition-colors"
            >
              Need a hint? ({hintIndex + 1}/{hints.length})
            </button>
          )}
        </div>
      )}

      {/* Current Task */}
      {expectedCommands.length > 0 && currentCommandIndex < expectedCommands.length && (
        <div className="px-4 py-2 bg-indigo-500/10 border-t border-indigo-500/30">
          <p className="text-sm text-indigo-300">
            <span className="font-medium">Task {currentCommandIndex + 1}:</span>{' '}
            {expectedCommands[currentCommandIndex].explanation}
          </p>
        </div>
      )}
    </div>
  )
}

export default TerminalEmulator
