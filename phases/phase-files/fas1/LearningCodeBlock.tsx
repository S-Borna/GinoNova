"use client"

/**
 * ============================================================================
 * LEARNING CODE BLOCK — Syntax Highlighted Code with Shell Toggle
 * ============================================================================
 * 
 * Features:
 * - Shell toggle (Bash/Python/YAML/HCL/JSON)
 * - Syntax highlighting
 * - Copy button
 * - Line numbers
 * - Filename display
 * - Explanation tooltip
 * 
 * @phase FAS 1.1 - Fix [object Object] rendering
 */

import * as React from "react"
import { useState } from "react"
import { Check, Copy, ChevronDown } from "lucide-react"
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism'

/* ============================================================================
   TYPES
   ============================================================================ */

interface CodeVariants {
  bash?: string
  python?: string
  yaml?: string
  hcl?: string
  json?: string
  dockerfile?: string
  javascript?: string
  typescript?: string
}

interface LearningCodeBlockProps {
  language: string
  code: string | object | CodeVariants
  filename?: string
  highlightLines?: number[]
  explanation?: string
  availableShells?: string[]
  className?: string
}

/* ============================================================================
   SHELL CONFIGURATION
   ============================================================================ */

const SHELL_CONFIG: Record<string, { label: string; color: string }> = {
  bash: { label: 'Bash', color: 'text-green-400' },
  python: { label: 'Python', color: 'text-blue-400' },
  yaml: { label: 'YAML', color: 'text-yellow-400' },
  hcl: { label: 'HCL', color: 'text-purple-400' },
  json: { label: 'JSON', color: 'text-orange-400' },
  dockerfile: { label: 'Dockerfile', color: 'text-cyan-400' },
  javascript: { label: 'JavaScript', color: 'text-yellow-300' },
  typescript: { label: 'TypeScript', color: 'text-blue-300' },
}

/* ============================================================================
   HELPER: Safely convert code to string
   ============================================================================ */

function codeToString(code: string | object | undefined | null): string {
  if (code === null || code === undefined) {
    return ''
  }
  
  if (typeof code === 'string') {
    return code
  }
  
  if (typeof code === 'object') {
    try {
      return JSON.stringify(code, null, 2)
    } catch {
      return String(code)
    }
  }
  
  return String(code)
}

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function LearningCodeBlock({
  language,
  code,
  filename,
  highlightLines = [],
  explanation,
  availableShells,
  className = "",
}: LearningCodeBlockProps) {
  const [copied, setCopied] = useState(false)
  const [activeShell, setActiveShell] = useState(language || 'bash')
  const [showShellMenu, setShowShellMenu] = useState(false)

  // Determine if we have multiple shell variants
  const hasVariants = typeof code === 'object' && !Array.isArray(code) && code !== null
  const shells = availableShells || (hasVariants ? Object.keys(code as CodeVariants) : [language])

  // Get the current code to display
  const getDisplayCode = (): string => {
    if (hasVariants) {
      const variants = code as CodeVariants
      const variantCode = variants[activeShell as keyof CodeVariants]
      return codeToString(variantCode) || codeToString(Object.values(variants)[0])
    }
    return codeToString(code)
  }

  const displayCode = getDisplayCode()

  // Copy to clipboard
  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(displayCode)
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    } catch (err) {
      console.error('Failed to copy:', err)
    }
  }

  return (
    <div className={`relative group rounded-xl overflow-hidden bg-[#1e1e1e] border border-gray-800 ${className}`}>
      {/* Header Bar */}
      <div className="flex items-center justify-between px-4 py-2 bg-gray-900/80 border-b border-gray-800">
        <div className="flex items-center gap-3">
          {/* Shell Toggle */}
          {shells.length > 1 ? (
            <div className="relative">
              <button
                onClick={() => setShowShellMenu(!showShellMenu)}
                className="flex items-center gap-1.5 px-2 py-1 rounded-md bg-gray-800 hover:bg-gray-700 transition-colors"
              >
                <span className={`text-sm font-medium ${SHELL_CONFIG[activeShell]?.color || 'text-gray-400'}`}>
                  {SHELL_CONFIG[activeShell]?.label || activeShell}
                </span>
                <ChevronDown className="w-3 h-3 text-gray-500" />
              </button>
              
              {showShellMenu && (
                <div className="absolute top-full left-0 mt-1 py-1 bg-gray-800 rounded-lg shadow-xl border border-gray-700 z-10 min-w-[120px]">
                  {shells.map((shell) => (
                    <button
                      key={shell}
                      onClick={() => {
                        setActiveShell(shell)
                        setShowShellMenu(false)
                      }}
                      className={`w-full px-3 py-1.5 text-left text-sm hover:bg-gray-700 transition-colors ${
                        activeShell === shell ? 'bg-gray-700' : ''
                      }`}
                    >
                      <span className={SHELL_CONFIG[shell]?.color || 'text-gray-400'}>
                        {SHELL_CONFIG[shell]?.label || shell}
                      </span>
                    </button>
                  ))}
                </div>
              )}
            </div>
          ) : (
            <span className={`text-sm font-medium ${SHELL_CONFIG[activeShell]?.color || 'text-gray-400'}`}>
              {SHELL_CONFIG[activeShell]?.label || activeShell}
            </span>
          )}

          {/* Filename */}
          {filename && (
            <>
              <span className="text-gray-600">•</span>
              <span className="text-sm text-gray-500">{filename}</span>
            </>
          )}
        </div>

        {/* Copy Button */}
        <button
          onClick={handleCopy}
          className="flex items-center gap-1.5 px-2 py-1 rounded-md text-gray-400 hover:text-white hover:bg-gray-800 transition-colors"
        >
          {copied ? (
            <>
              <Check className="w-4 h-4 text-green-400" />
              <span className="text-xs text-green-400">Copied!</span>
            </>
          ) : (
            <>
              <Copy className="w-4 h-4" />
              <span className="text-xs">Copy</span>
            </>
          )}
        </button>
      </div>

      {/* Code Content */}
      <div className="overflow-x-auto">
        <SyntaxHighlighter
          language={activeShell}
          style={oneDark}
          showLineNumbers
          wrapLines
          lineProps={(lineNumber) => ({
            style: {
              backgroundColor: highlightLines.includes(lineNumber) 
                ? 'rgba(99, 102, 241, 0.2)' 
                : 'transparent',
              display: 'block',
              width: '100%',
            },
          })}
          customStyle={{
            margin: 0,
            padding: '1rem',
            background: 'transparent',
            fontSize: '0.875rem',
            lineHeight: '1.5',
          }}
          codeTagProps={{
            style: {
              fontFamily: 'ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace',
            },
          }}
        >
          {displayCode}
        </SyntaxHighlighter>
      </div>

      {/* Explanation */}
      {explanation && (
        <div className="px-4 py-3 bg-gray-900/50 border-t border-gray-800">
          <p className="text-sm text-gray-400">
            <span className="text-indigo-400 font-medium">💡 </span>
            {explanation}
          </p>
        </div>
      )}
    </div>
  )
}

export default LearningCodeBlock
