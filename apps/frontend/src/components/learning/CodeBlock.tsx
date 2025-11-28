"use client"

/**
 * ============================================================================
 * CODE BLOCK COMPONENT - Syntax Highlighted Code Display
 * ============================================================================
 *
 * Features:
 * - Syntax highlighting with react-syntax-highlighter
 * - Line numbers
 * - Line highlighting
 * - Filename header
 * - Copy to clipboard
 * - Optional explanation
 *
 * @phase ILE Phase 3 - Content Blocks
 */

import * as React from "react"
import { useState } from "react"
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter"
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism"
import { cn } from "@/lib/utils"
import { Copy, Check, FileCode, Terminal } from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface LearningCodeBlockProps {
    language: string
    code: string
    filename?: string
    highlightLines?: number[]
    explanation?: string
    showLineNumbers?: boolean
    className?: string
}

/* ============================================================================
   LANGUAGE ICONS
   ============================================================================ */

const languageIcons: Record<string, React.ReactNode> = {
    bash: <Terminal className="h-4 w-4" />,
    sh: <Terminal className="h-4 w-4" />,
    shell: <Terminal className="h-4 w-4" />,
    zsh: <Terminal className="h-4 w-4" />,
}

const languageLabels: Record<string, string> = {
    js: "JavaScript",
    javascript: "JavaScript",
    ts: "TypeScript",
    typescript: "TypeScript",
    jsx: "JSX",
    tsx: "TSX",
    py: "Python",
    python: "Python",
    bash: "Bash",
    sh: "Shell",
    shell: "Shell",
    zsh: "Zsh",
    yaml: "YAML",
    yml: "YAML",
    json: "JSON",
    html: "HTML",
    css: "CSS",
    scss: "SCSS",
    sql: "SQL",
    go: "Go",
    rust: "Rust",
    java: "Java",
    c: "C",
    cpp: "C++",
    dockerfile: "Dockerfile",
    docker: "Docker",
    terraform: "Terraform",
    hcl: "HCL",
    markdown: "Markdown",
    md: "Markdown",
}

/* ============================================================================
   CUSTOM STYLE
   ============================================================================ */

const customStyle = {
    ...oneDark,
    'pre[class*="language-"]': {
        ...oneDark['pre[class*="language-"]'],
        background: "#0a0a0f",
        margin: 0,
        padding: "1rem",
    },
    'code[class*="language-"]': {
        ...oneDark['code[class*="language-"]'],
        background: "transparent",
    },
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function LearningCodeBlock({
    language,
    code,
    filename,
    highlightLines = [],
    explanation,
    showLineNumbers = true,
    className,
}: LearningCodeBlockProps) {
    const [copied, setCopied] = useState(false)

    const handleCopy = async () => {
        try {
            await navigator.clipboard.writeText(code)
            setCopied(true)
            setTimeout(() => setCopied(false), 2000)
        } catch (err) {
            console.error("Failed to copy:", err)
        }
    }

    const displayLanguage = languageLabels[language.toLowerCase()] || language.toUpperCase()
    const icon = languageIcons[language.toLowerCase()] || <FileCode className="h-4 w-4" />

    // Line props for highlighting
    const lineProps = (lineNumber: number) => {
        const style: React.CSSProperties = { display: "block" }
        if (highlightLines.includes(lineNumber)) {
            style.backgroundColor = "rgba(251, 191, 36, 0.15)"
            style.borderLeft = "3px solid #fbbf24"
            style.marginLeft = "-3px"
            style.paddingLeft = "calc(1em - 3px)"
        }
        return { style }
    }

    return (
        <div className={cn("rounded-xl overflow-hidden border border-neutral-800 my-4", className)}>
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
                        {icon}
                        <span>{filename || displayLanguage}</span>
                    </div>
                </div>

                {/* Copy button */}
                <button
                    onClick={handleCopy}
                    className={cn(
                        "flex items-center gap-1.5 px-2 py-1 rounded-md text-xs font-medium",
                        "bg-neutral-700 hover:bg-neutral-600 text-neutral-300",
                        "transition-colors duration-150"
                    )}
                >
                    {copied ? (
                        <>
                            <Check className="h-3.5 w-3.5 text-green-400" />
                            <span className="text-green-400">Copied!</span>
                        </>
                    ) : (
                        <>
                            <Copy className="h-3.5 w-3.5" />
                            <span>Copy</span>
                        </>
                    )}
                </button>
            </div>

            {/* Code */}
            <SyntaxHighlighter
                language={language}
                style={customStyle}
                showLineNumbers={showLineNumbers}
                wrapLines={true}
                lineProps={lineProps}
                customStyle={{
                    margin: 0,
                    borderRadius: 0,
                    fontSize: "0.875rem",
                }}
                lineNumberStyle={{
                    color: "#4b5563",
                    paddingRight: "1em",
                    userSelect: "none",
                }}
            >
                {code}
            </SyntaxHighlighter>

            {/* Explanation */}
            {explanation && (
                <div className="px-4 py-3 bg-neutral-900/50 border-t border-neutral-800">
                    <p className="text-sm text-neutral-400 italic">
                        💡 {explanation}
                    </p>
                </div>
            )}
        </div>
    )
}

export default LearningCodeBlock
