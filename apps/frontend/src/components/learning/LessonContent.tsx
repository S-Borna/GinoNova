"use client"

/**
 * ============================================================================
 * LESSON CONTENT - Pedagogisk och visuellt tilltalande lektionsvy
 * ============================================================================
 *
 * Features:
 * - Progressbar för läsning
 * - Highlight av nyckelbegrepp
 * - Collapsible sektioner för quiz/svar
 * - Bättre kod-block med copy-funktion
 * - Visuella diagram och tabeller
 *
 * @phase 4.1 - Enhanced Learning Experience
 */

import { useState, useEffect, useRef } from "react"
import ReactMarkdown from "react-markdown"
import rehypeHighlight from "rehype-highlight"
import remarkGfm from "remark-gfm"
import { cn } from "@saas/ui"
import { GlassCard } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import {
    Copy,
    Check,
    ChevronDown,
    ChevronRight,
    BookOpen,
    Target,
    Lightbulb,
    Code2,
    FileText,
    HelpCircle,
    CheckCircle2,
    Clock,
} from "lucide-react"

import "highlight.js/styles/github-dark.css"

interface LessonContentProps {
    content: string
    title?: string
    estimatedMinutes?: number
    onProgressUpdate?: (progress: number) => void
}

/* ============================================================================
   HELPER: Extract code text from React children (fixes [object Object] bug)
   ============================================================================ */

function extractCodeText(children: React.ReactNode): string {
    // If it's already a string, return it
    if (typeof children === 'string') {
        return children
    }

    // If it's a number, convert to string
    if (typeof children === 'number') {
        return String(children)
    }

    // If it's null or undefined, return empty
    if (children == null) {
        return ''
    }

    // If it's an array, recursively extract and join
    if (Array.isArray(children)) {
        return children.map(extractCodeText).join('')
    }

    // If it's a React element, try to get its children
    if (typeof children === 'object' && 'props' in children) {
        const element = children as React.ReactElement<{ children?: React.ReactNode }>
        return extractCodeText(element.props?.children)
    }

    // Fallback: try to stringify (but avoid [object Object])
    const str = String(children)
    if (str === '[object Object]') {
        // Try JSON.stringify as last resort
        try {
            return JSON.stringify(children, null, 2)
        } catch {
            return ''
        }
    }

    return str
}

/* ============================================================================
   COPY BUTTON FOR CODE BLOCKS
   ============================================================================ */

function CopyButton({ code }: { code: string }) {
    const [copied, setCopied] = useState(false)

    const handleCopy = async () => {
        await navigator.clipboard.writeText(code)
        setCopied(true)
        setTimeout(() => setCopied(false), 2000)
    }

    return (
        <button
            onClick={handleCopy}
            className={cn(
                "absolute top-3 right-3 p-2 rounded-lg transition-all",
                "bg-neutral-700/50 hover:bg-neutral-600/50",
                "text-neutral-400 hover:text-white",
                "opacity-0 group-hover:opacity-100"
            )}
            title="Copy code"
        >
            {copied ? (
                <Check className="w-4 h-4 text-emerald-400" />
            ) : (
                <Copy className="w-4 h-4" />
            )}
        </button>
    )
}

/* ============================================================================
   COLLAPSIBLE DETAILS (for quiz answers)
   ============================================================================ */

function CollapsibleDetails({ summary, children }: { summary: string; children: React.ReactNode }) {
    const [isOpen, setIsOpen] = useState(false)

    return (
        <div className="my-4 rounded-xl border border-indigo-200 dark:border-indigo-800 overflow-hidden">
            <button
                onClick={() => setIsOpen(!isOpen)}
                className={cn(
                    "w-full flex items-center gap-2 px-4 py-3 text-left",
                    "bg-indigo-50 dark:bg-indigo-950/50",
                    "text-indigo-700 dark:text-indigo-300 font-medium",
                    "hover:bg-indigo-100 dark:hover:bg-indigo-900/50 transition-colors"
                )}
            >
                {isOpen ? (
                    <ChevronDown className="w-4 h-4" />
                ) : (
                    <ChevronRight className="w-4 h-4" />
                )}
                <HelpCircle className="w-4 h-4" />
                {summary}
            </button>
            {isOpen && (
                <div className="px-4 py-3 bg-white dark:bg-neutral-900 border-t border-indigo-200 dark:border-indigo-800">
                    {children}
                </div>
            )}
        </div>
    )
}

/* ============================================================================
   SECTION HEADER (for ## headings)
   ============================================================================ */

function SectionHeader({ children, icon }: { children: React.ReactNode; icon?: React.ReactNode }) {
    return (
        <div className="flex items-center gap-3 mt-10 mb-4 pb-3 border-b-2 border-indigo-500/30">
            {icon && (
                <div className="w-8 h-8 rounded-lg bg-indigo-500/10 flex items-center justify-center text-indigo-500">
                    {icon}
                </div>
            )}
            <h2 className="text-xl font-bold text-neutral-900 dark:text-white">
                {children}
            </h2>
        </div>
    )
}

/* ============================================================================
   MAIN LESSON CONTENT COMPONENT
   ============================================================================ */

export function LessonContent({ content, title, estimatedMinutes, onProgressUpdate }: LessonContentProps) {
    const [readProgress, setReadProgress] = useState(0)
    const contentRef = useRef<HTMLDivElement>(null)

    // Track scroll progress
    useEffect(() => {
        const handleScroll = () => {
            if (!contentRef.current) return

            const element = contentRef.current
            const rect = element.getBoundingClientRect()
            const windowHeight = window.innerHeight
            const elementHeight = element.scrollHeight

            // Calculate how much has been scrolled through
            const scrolled = Math.max(0, -rect.top + windowHeight * 0.5)
            const progress = Math.min(100, (scrolled / elementHeight) * 100)

            setReadProgress(Math.round(progress))
            onProgressUpdate?.(Math.round(progress))
        }

        window.addEventListener("scroll", handleScroll)
        return () => window.removeEventListener("scroll", handleScroll)
    }, [onProgressUpdate])

    // Detect section types from heading content
    const getSectionIcon = (text: string) => {
        const lower = text.toLowerCase()
        if (lower.includes("lärandemål") || lower.includes("mål")) return <Target className="w-4 h-4" />
        if (lower.includes("praktisk") || lower.includes("övning")) return <Code2 className="w-4 h-4" />
        if (lower.includes("quiz") || lower.includes("testa")) return <HelpCircle className="w-4 h-4" />
        if (lower.includes("sammanfattning") || lower.includes("summary")) return <CheckCircle2 className="w-4 h-4" />
        if (lower.includes("tips") || lower.includes("💡")) return <Lightbulb className="w-4 h-4" />
        return <FileText className="w-4 h-4" />
    }

    return (
        <div className="relative">
            {/* Reading Progress Bar */}
            <div className="sticky top-0 z-10 -mx-6 md:-mx-8 px-6 md:px-8 py-2 bg-white/80 dark:bg-neutral-900/80 backdrop-blur-lg border-b border-neutral-200/50 dark:border-neutral-700/50">
                <div className="flex items-center justify-between mb-2">
                    <div className="flex items-center gap-2 text-sm text-neutral-500">
                        <BookOpen className="w-4 h-4" />
                        <span>Läsframsteg</span>
                    </div>
                    <div className="flex items-center gap-2 text-sm">
                        {estimatedMinutes && (
                            <span className="flex items-center gap-1 text-neutral-400">
                                <Clock className="w-3.5 h-3.5" />
                                ~{estimatedMinutes} min
                            </span>
                        )}
                        <span className="font-medium text-indigo-500">{readProgress}%</span>
                    </div>
                </div>
                <div className="h-1.5 bg-neutral-200 dark:bg-neutral-700 rounded-full overflow-hidden">
                    <div
                        className="h-full bg-gradient-to-r from-indigo-500 to-purple-500 rounded-full transition-all duration-300"
                        style={{ width: `${readProgress}%` }}
                    />
                </div>
            </div>

            {/* Lesson Content */}
            <div ref={contentRef} className="pt-6">
                <article className="prose prose-neutral dark:prose-invert max-w-none
                    prose-headings:text-neutral-900 dark:prose-headings:text-white
                    prose-p:text-neutral-700 dark:prose-p:text-neutral-300 prose-p:leading-relaxed
                    prose-li:text-neutral-700 dark:prose-li:text-neutral-300
                    prose-strong:text-neutral-900 dark:prose-strong:text-white
                    prose-a:text-indigo-600 dark:prose-a:text-indigo-400 prose-a:no-underline hover:prose-a:underline
                    prose-blockquote:border-l-indigo-500 prose-blockquote:bg-indigo-50/50 dark:prose-blockquote:bg-indigo-950/30 prose-blockquote:py-1 prose-blockquote:px-4 prose-blockquote:rounded-r-lg
                    prose-hr:border-neutral-300 dark:prose-hr:border-neutral-700
                ">
                    <ReactMarkdown
                        remarkPlugins={[remarkGfm]}
                        rehypePlugins={[rehypeHighlight]}
                        components={{
                            // Enhanced headings
                            h1: ({ children }) => (
                                <h1 className="text-3xl font-bold text-neutral-900 dark:text-white mb-6 mt-8 first:mt-0">
                                    {children}
                                </h1>
                            ),
                            h2: ({ children }) => {
                                const text = String(children)
                                return (
                                    <SectionHeader icon={getSectionIcon(text)}>
                                        {children}
                                    </SectionHeader>
                                )
                            },
                            h3: ({ children }) => (
                                <h3 className="text-lg font-semibold text-neutral-800 dark:text-neutral-200 mt-8 mb-3">
                                    {children}
                                </h3>
                            ),

                            // Better paragraphs
                            p: ({ children }) => (
                                <p className="text-base leading-7 mb-4">{children}</p>
                            ),

                            // Enhanced lists
                            ul: ({ children }) => (
                                <ul className="my-4 space-y-2 list-none pl-0">
                                    {children}
                                </ul>
                            ),
                            ol: ({ children }) => (
                                <ol className="my-4 space-y-2 list-decimal pl-6">
                                    {children}
                                </ol>
                            ),
                            li: ({ children, ...props }) => {
                                // Check if it's in an unordered list
                                const isUnordered = !(props as any).ordered
                                return (
                                    <li className={cn(
                                        "text-neutral-700 dark:text-neutral-300",
                                        isUnordered && "flex items-start gap-2 pl-0"
                                    )}>
                                        {isUnordered && (
                                            <span className="w-1.5 h-1.5 rounded-full bg-indigo-500 mt-2.5 flex-shrink-0" />
                                        )}
                                        <span>{children}</span>
                                    </li>
                                )
                            },

                            // Beautiful tables
                            table: ({ children }) => (
                                <div className="my-6 overflow-x-auto rounded-xl border border-neutral-200 dark:border-neutral-700">
                                    <table className="w-full text-sm">{children}</table>
                                </div>
                            ),
                            thead: ({ children }) => (
                                <thead className="bg-neutral-100 dark:bg-neutral-800">{children}</thead>
                            ),
                            th: ({ children }) => (
                                <th className="px-4 py-3 text-left font-semibold text-neutral-900 dark:text-white border-b border-neutral-200 dark:border-neutral-700">
                                    {children}
                                </th>
                            ),
                            td: ({ children }) => (
                                <td className="px-4 py-3 border-b border-neutral-200/50 dark:border-neutral-700/50">
                                    {children}
                                </td>
                            ),

                            // Code blocks with copy button
                            pre: ({ children }) => {
                                // Extract code text robustly (fixes [object Object] bug)
                                const code = extractCodeText(children)

                                // Try to get language from className
                                let language = 'plaintext'
                                if (typeof children === 'object' && children !== null && 'props' in children) {
                                    const childElement = children as React.ReactElement<{ className?: string }>
                                    const className = childElement?.props?.className || ''
                                    const languageMatch = className.match(/language-(\w+)/)
                                    if (languageMatch) {
                                        language = languageMatch[1]
                                    }
                                }

                                return (
                                    <div className="group relative my-6">
                                        <div className="absolute top-0 left-0 px-3 py-1 bg-neutral-700 text-neutral-400 text-xs rounded-br-lg rounded-tl-xl font-mono">
                                            {language}
                                        </div>
                                        <pre className="bg-neutral-900 rounded-xl p-4 pt-8 overflow-x-auto border border-neutral-800">
                                            <code className="text-sm font-mono text-neutral-100">
                                                {code.trim()}
                                            </code>
                                        </pre>
                                        <CopyButton code={code.trim()} />
                                    </div>
                                )
                            },

                            // Inline code
                            code: ({ className, children, ...props }) => {
                                const isInline = !className
                                if (isInline) {
                                    return (
                                        <code className="px-1.5 py-0.5 bg-indigo-100 dark:bg-indigo-900/50 text-indigo-700 dark:text-indigo-300 rounded font-mono text-sm" {...props}>
                                            {children}
                                        </code>
                                    )
                                }
                                return <code className={className} {...props}>{children}</code>
                            },

                            // Details/Summary for collapsible content
                            details: ({ children }) => {
                                const childArray = Array.isArray(children) ? children : [children]
                                const summary = childArray.find((child: any) => child?.type === 'summary')
                                const content = childArray.filter((child: any) => child?.type !== 'summary')

                                return (
                                    <CollapsibleDetails summary={String(summary?.props?.children || 'Visa mer')}>
                                        {content}
                                    </CollapsibleDetails>
                                )
                            },
                            summary: () => null, // Handled by details

                            // Horizontal rule as section divider
                            hr: () => (
                                <div className="my-8 flex items-center gap-4">
                                    <div className="flex-1 h-px bg-gradient-to-r from-transparent via-neutral-300 dark:via-neutral-700 to-transparent" />
                                    <div className="w-2 h-2 rounded-full bg-indigo-500/50" />
                                    <div className="flex-1 h-px bg-gradient-to-r from-transparent via-neutral-300 dark:via-neutral-700 to-transparent" />
                                </div>
                            ),

                            // Blockquotes as callouts
                            blockquote: ({ children }) => (
                                <div className="my-6 flex gap-3 p-4 bg-amber-50 dark:bg-amber-950/30 border-l-4 border-amber-500 rounded-r-xl">
                                    <Lightbulb className="w-5 h-5 text-amber-500 flex-shrink-0 mt-0.5" />
                                    <div className="text-amber-900 dark:text-amber-100">
                                        {children}
                                    </div>
                                </div>
                            ),
                        }}
                    >
                        {content}
                    </ReactMarkdown>
                </article>
            </div>

            {/* Completion indicator */}
            {readProgress >= 90 && (
                <div className="mt-8 p-4 bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800 rounded-xl">
                    <div className="flex items-center gap-3">
                        <div className="w-10 h-10 rounded-full bg-emerald-500/20 flex items-center justify-center">
                            <CheckCircle2 className="w-5 h-5 text-emerald-500" />
                        </div>
                        <div>
                            <p className="font-medium text-emerald-700 dark:text-emerald-300">
                                Bra jobbat! Du har läst igenom lektionen.
                            </p>
                            <p className="text-sm text-emerald-600 dark:text-emerald-400">
                                Glöm inte att markera som slutförd för att få dina XP!
                            </p>
                        </div>
                    </div>
                </div>
            )}
        </div>
    )
}

export default LessonContent
