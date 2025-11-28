"use client"

/**
 * ============================================================================
 * CODE BLOCK COMPONENT - Syntax Highlighted Code Display
 * ============================================================================
 *
 * Features:
 * - Language label
 * - Copy to clipboard button
 * - Line numbers (optional)
 * - Syntax highlighting via rehype-highlight
 * - Dark theme optimized
 *
 * @phase C.2 - Task Content Display
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { Check, Copy, Terminal } from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface CodeBlockProps {
    children: string
    language?: string
    showLineNumbers?: boolean
    filename?: string
    className?: string
}

/* ============================================================================
   LANGUAGE ICONS & LABELS
   ============================================================================ */

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
    plaintext: "Text",
    text: "Text",
}

function getLanguageLabel(lang?: string): string {
    if (!lang) return "Code"
    return languageLabels[lang.toLowerCase()] || lang.toUpperCase()
}

/* ============================================================================
   COPY BUTTON
   ============================================================================ */

interface CopyButtonProps {
    text: string
    className?: string
}

function CopyButton({ text, className }: CopyButtonProps) {
    const [copied, setCopied] = React.useState(false)

    const handleCopy = async () => {
        try {
            await navigator.clipboard.writeText(text)
            setCopied(true)
            setTimeout(() => setCopied(false), 2000)
        } catch (err) {
            console.error("Failed to copy:", err)
        }
    }

    return (
        <button
            onClick={handleCopy}
            className={cn(
                "flex items-center gap-1.5 px-2 py-1 rounded-md text-xs font-medium",
                "bg-neutral-700 hover:bg-neutral-600 text-neutral-300",
                "transition-colors duration-150",
                className
            )}
            aria-label={copied ? "Copied" : "Copy code"}
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
    )
}

/* ============================================================================
   LINE NUMBERS
   ============================================================================ */

interface LineNumbersProps {
    count: number
}

function LineNumbers({ count }: LineNumbersProps) {
    return (
        <div
            className="select-none text-right pr-4 text-neutral-500 text-sm font-mono"
            aria-hidden="true"
        >
            {Array.from({ length: count }, (_, i) => (
                <div key={i + 1} className="leading-6">
                    {i + 1}
                </div>
            ))}
        </div>
    )
}

/* ============================================================================
   MAIN CODE BLOCK COMPONENT
   ============================================================================ */

export function CodeBlock({
    children,
    language,
    showLineNumbers = false,
    filename,
    className,
}: CodeBlockProps) {
    const lines = children.split("\n")
    const lineCount = lines.length

    // Remove trailing empty line if present
    const code = children.endsWith("\n") ? children.slice(0, -1) : children

    return (
        <div
            className={cn(
                "relative rounded-xl overflow-hidden",
                "bg-neutral-900 border border-neutral-800",
                "my-4",
                className
            )}
        >
            {/* Header Bar */}
            <div className="flex items-center justify-between px-4 py-2 bg-neutral-800/50 border-b border-neutral-800">
                <div className="flex items-center gap-2">
                    {/* Terminal dots */}
                    <div className="flex items-center gap-1.5">
                        <div className="w-3 h-3 rounded-full bg-red-500/80" />
                        <div className="w-3 h-3 rounded-full bg-yellow-500/80" />
                        <div className="w-3 h-3 rounded-full bg-green-500/80" />
                    </div>

                    {/* Language or filename */}
                    <div className="flex items-center gap-1.5 ml-3 text-neutral-400 text-sm">
                        <Terminal className="h-3.5 w-3.5" />
                        <span>{filename || getLanguageLabel(language)}</span>
                    </div>
                </div>

                {/* Copy button */}
                <CopyButton text={code} />
            </div>

            {/* Code content */}
            <div className="overflow-x-auto">
                <div className="flex min-w-full">
                    {/* Line numbers */}
                    {showLineNumbers && (
                        <div className="flex-shrink-0 py-4 pl-4 bg-neutral-900/50 border-r border-neutral-800">
                            <LineNumbers count={lineCount} />
                        </div>
                    )}

                    {/* Code */}
                    <pre
                        className={cn(
                            "flex-1 p-4 overflow-x-auto",
                            "text-sm font-mono leading-6",
                            "text-neutral-100"
                        )}
                    >
                        <code className={language ? `language-${language}` : ""}>
                            {code}
                        </code>
                    </pre>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   INLINE CODE COMPONENT
   ============================================================================ */

interface InlineCodeProps {
    children: React.ReactNode
    className?: string
}

export function InlineCode({ children, className }: InlineCodeProps) {
    return (
        <code
            className={cn(
                "px-1.5 py-0.5 rounded-md",
                "bg-neutral-100 dark:bg-neutral-800",
                "text-primary-600 dark:text-primary-400",
                "text-sm font-mono",
                className
            )}
        >
            {children}
        </code>
    )
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default CodeBlock
