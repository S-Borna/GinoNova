"use client"

/**
 * ============================================================================
 * CODE BLOCK — Design System v1.0
 * ============================================================================
 *
 * Styled code block to replace all <pre> usage in tasks.
 * Features:
 * - Surface background (#F6F8FA)
 * - 20px padding
 * - 12px border radius
 * - Subtle shadow (0 2px 8px rgba(0,0,0,0.05))
 * - Copy button
 * - Language detection label
 * - Overflow handling
 *
 * @example
 * <CodeBlock language="bash">
 *   npm install express
 * </CodeBlock>
 */

import * as React from 'react'
import { useState, useCallback } from 'react'
import { cn } from './utils'

export interface CodeBlockProps {
    children: React.ReactNode
    /** Programming language for syntax hints */
    language?: string
    /** Show copy button */
    showCopy?: boolean
    /** Show language label */
    showLanguage?: boolean
    /** Additional CSS classes */
    className?: string
    /** Title for the code block */
    title?: string
    /** File name to display */
    filename?: string
    /** Highlight specific lines (1-indexed) */
    highlightLines?: number[]
    /** Show line numbers */
    showLineNumbers?: boolean
}

// Language display names
const languageLabels: Record<string, string> = {
    bash: 'Bash',
    sh: 'Shell',
    shell: 'Shell',
    zsh: 'Zsh',
    javascript: 'JavaScript',
    js: 'JavaScript',
    typescript: 'TypeScript',
    ts: 'TypeScript',
    python: 'Python',
    py: 'Python',
    json: 'JSON',
    yaml: 'YAML',
    yml: 'YAML',
    dockerfile: 'Dockerfile',
    docker: 'Docker',
    sql: 'SQL',
    html: 'HTML',
    css: 'CSS',
    go: 'Go',
    rust: 'Rust',
    java: 'Java',
    c: 'C',
    cpp: 'C++',
    csharp: 'C#',
    ruby: 'Ruby',
    php: 'PHP',
    swift: 'Swift',
    kotlin: 'Kotlin',
    terraform: 'Terraform',
    hcl: 'HCL',
    nginx: 'NGINX',
    toml: 'TOML',
    ini: 'INI',
    xml: 'XML',
    markdown: 'Markdown',
    md: 'Markdown',
    graphql: 'GraphQL',
    plaintext: 'Text',
    text: 'Text',
}

export function CodeBlock({
    children,
    language,
    showCopy = true,
    showLanguage = true,
    className,
    title,
    filename,
    highlightLines = [],
    showLineNumbers = false,
}: CodeBlockProps) {
    const [copied, setCopied] = useState(false)

    // Extract text content from children
    const getTextContent = useCallback((node: React.ReactNode): string => {
        if (typeof node === 'string') return node
        if (typeof node === 'number') return String(node)
        if (Array.isArray(node)) return node.map(getTextContent).join('')
        if (React.isValidElement(node)) {
            const props = node.props as { children?: React.ReactNode }
            if (props.children) {
                return getTextContent(props.children)
            }
        }
        return ''
    }, [])

    const codeText = getTextContent(children).trim()

    const handleCopy = async () => {
        try {
            await navigator.clipboard.writeText(codeText)
            setCopied(true)
            setTimeout(() => setCopied(false), 2000)
        } catch (err) {
            console.error('Failed to copy:', err)
        }
    }

    const displayLanguage = language ? languageLabels[language.toLowerCase()] || language : null
    const displayLabel = filename || title || displayLanguage

    // Split into lines for line numbers
    const lines = codeText.split('\n')

    return (
        <div
            className={cn(
                // Container
                'relative group',
                'rounded-xl',                           // 12px radius
                'bg-[#F6F8FA] dark:bg-neutral-800',     // Surface background
                'shadow-[0_2px_8px_rgba(0,0,0,0.05)]',  // Code shadow token
                'dark:shadow-[0_2px_8px_rgba(0,0,0,0.2)]',
                // Border
                'border border-[rgba(0,0,0,0.05)] dark:border-neutral-700',
                // Margin
                'my-4',
                className
            )}
        >
            {/* Header bar (if has label) */}
            {displayLabel && (
                <div className="flex items-center justify-between px-4 py-2 border-b border-[rgba(0,0,0,0.05)] dark:border-neutral-700">
                    <span className="text-xs font-medium text-[#6B7280] dark:text-neutral-400">
                        {displayLabel}
                    </span>
                    {showCopy && (
                        <button
                            onClick={handleCopy}
                            className={cn(
                                'px-2 py-1 rounded-md text-xs font-medium transition-all',
                                'text-[#6B7280] dark:text-neutral-400',
                                'hover:bg-[rgba(0,0,0,0.05)] dark:hover:bg-neutral-700',
                                copied && 'text-emerald-600 dark:text-emerald-400'
                            )}
                        >
                            {copied ? '✓ Copied' : 'Copy'}
                        </button>
                    )}
                </div>
            )}

            {/* Code content */}
            <div className="relative">
                <pre
                    className={cn(
                        // Typography
                        'text-sm leading-[22px] font-mono',
                        'text-[#111827] dark:text-neutral-100',
                        // Padding
                        'p-5',                              // 20px padding
                        // Overflow
                        'overflow-x-auto',
                        'whitespace-pre',
                        // Scrollbar styling
                        'scrollbar-thin scrollbar-thumb-neutral-300 dark:scrollbar-thumb-neutral-600'
                    )}
                >
                    {showLineNumbers ? (
                        <code className="flex">
                            <span className="select-none pr-4 text-[#9CA3AF] dark:text-neutral-500 text-right min-w-[2rem]">
                                {lines.map((_, i) => (
                                    <span
                                        key={i}
                                        className={cn(
                                            'block',
                                            highlightLines.includes(i + 1) && 'bg-yellow-100 dark:bg-yellow-900/30'
                                        )}
                                    >
                                        {i + 1}
                                    </span>
                                ))}
                            </span>
                            <span className="flex-1">
                                {lines.map((line, i) => (
                                    <span
                                        key={i}
                                        className={cn(
                                            'block',
                                            highlightLines.includes(i + 1) && 'bg-yellow-100 dark:bg-yellow-900/30 -mx-5 px-5'
                                        )}
                                    >
                                        {line || ' '}
                                    </span>
                                ))}
                            </span>
                        </code>
                    ) : (
                        <code>{codeText}</code>
                    )}
                </pre>

                {/* Floating copy button (if no header) */}
                {showCopy && !displayLabel && (
                    <button
                        onClick={handleCopy}
                        className={cn(
                            'absolute top-3 right-3',
                            'px-2 py-1 rounded-md text-xs font-medium transition-all',
                            'bg-white dark:bg-neutral-700',
                            'text-[#6B7280] dark:text-neutral-300',
                            'shadow-sm',
                            'opacity-0 group-hover:opacity-100',
                            'hover:bg-neutral-100 dark:hover:bg-neutral-600',
                            copied && 'opacity-100 text-emerald-600 dark:text-emerald-400'
                        )}
                    >
                        {copied ? '✓ Copied' : 'Copy'}
                    </button>
                )}
            </div>
        </div>
    )
}

export default CodeBlock
