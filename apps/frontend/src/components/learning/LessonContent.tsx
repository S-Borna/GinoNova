"use client"

/**
 * ============================================================================
 * LESSON CONTENT — PREMIUM VIBRANT DESIGN
 * ============================================================================
 *
 * A stunning, colorful lesson viewer with:
 * - Gradient progress bars
 * - Color-coded sections
 * - Vibrant callout boxes
 * - Premium code blocks with syntax highlighting
 * - Interactive elements
 * - Beautiful typography
 *
 * @design VIBRANT-PREMIUM-2024
 */

import { useState, useEffect, useRef } from "react"
import ReactMarkdown from "react-markdown"
import rehypeHighlight from "rehype-highlight"
import remarkGfm from "remark-gfm"
import { cn } from "@saas/ui"
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
    Zap,
    Terminal,
    Rocket,
    AlertTriangle,
    Info,
    Star,
    Sparkles,
    Brain,
    Flame,
    Shield,
    Award,
} from "lucide-react"

import "highlight.js/styles/github-dark.css"

interface LessonContentProps {
    content: string
    title?: string
    estimatedMinutes?: number
    onProgressUpdate?: (progress: number) => void
}

/* ============================================================================
   VIBRANT COLOR PALETTE
   ============================================================================ */

const COLORS = {
    // Primary gradients
    primary: "from-violet-600 via-purple-600 to-indigo-600",
    secondary: "from-cyan-500 via-blue-500 to-indigo-500",
    accent: "from-amber-500 via-orange-500 to-red-500",

    // Section colors
    tldr: {
        bg: "bg-gradient-to-r from-emerald-500/10 via-teal-500/10 to-cyan-500/10",
        border: "border-emerald-500/30",
        text: "text-emerald-400",
        icon: "text-emerald-400",
        glow: "shadow-emerald-500/20",
    },
    important: {
        bg: "bg-gradient-to-r from-amber-500/10 via-orange-500/10 to-red-500/10",
        border: "border-amber-500/30",
        text: "text-amber-400",
        icon: "text-amber-400",
        glow: "shadow-amber-500/20",
    },
    tip: {
        bg: "bg-gradient-to-r from-blue-500/10 via-indigo-500/10 to-violet-500/10",
        border: "border-blue-500/30",
        text: "text-blue-400",
        icon: "text-blue-400",
        glow: "shadow-blue-500/20",
    },
    warning: {
        bg: "bg-gradient-to-r from-rose-500/10 via-pink-500/10 to-fuchsia-500/10",
        border: "border-rose-500/30",
        text: "text-rose-400",
        icon: "text-rose-400",
        glow: "shadow-rose-500/20",
    },
    success: {
        bg: "bg-gradient-to-r from-green-500/10 via-emerald-500/10 to-teal-500/10",
        border: "border-green-500/30",
        text: "text-green-400",
        icon: "text-green-400",
        glow: "shadow-green-500/20",
    },
    code: {
        bg: "bg-gradient-to-br from-slate-900 via-zinc-900 to-neutral-900",
        border: "border-violet-500/20",
        header: "bg-gradient-to-r from-violet-600/20 via-purple-600/20 to-indigo-600/20",
    },
}

/* ============================================================================
   HELPER: Extract code text from React children (fixes [object Object] bug)
   ============================================================================ */

function extractCodeText(children: React.ReactNode): string {
    if (typeof children === 'string') return children
    if (typeof children === 'number') return String(children)
    if (children == null) return ''
    if (Array.isArray(children)) return children.map(extractCodeText).join('')
    if (typeof children === 'object' && 'props' in children) {
        const element = children as React.ReactElement<{ children?: React.ReactNode }>
        return extractCodeText(element.props?.children)
    }
    const str = String(children)
    if (str === '[object Object]') {
        try { return JSON.stringify(children, null, 2) } catch { return '' }
    }
    return str
}

/* ============================================================================
   PREMIUM COPY BUTTON
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
                "absolute top-3 right-3 p-2.5 rounded-xl transition-all duration-300",
                "bg-white/5 backdrop-blur-sm",
                "border border-white/10 hover:border-violet-500/50",
                "text-zinc-400 hover:text-white",
                "opacity-0 group-hover:opacity-100",
                "hover:bg-violet-500/20 hover:shadow-lg hover:shadow-violet-500/20",
                "transform hover:scale-105"
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
   VIBRANT CALLOUT BOX
   ============================================================================ */

type CalloutType = 'tldr' | 'important' | 'tip' | 'warning' | 'success'

function CalloutBox({ type, children }: { type: CalloutType; children: React.ReactNode }) {
    const config = {
        tldr: {
            ...COLORS.tldr,
            title: "TL;DR",
            Icon: Zap,
        },
        important: {
            ...COLORS.important,
            title: "Viktigt",
            Icon: AlertTriangle,
        },
        tip: {
            ...COLORS.tip,
            title: "Tips",
            Icon: Lightbulb,
        },
        warning: {
            ...COLORS.warning,
            title: "Varning",
            Icon: Shield,
        },
        success: {
            ...COLORS.success,
            title: "Bra jobbat!",
            Icon: CheckCircle2,
        },
    }[type]

    const { bg, border, text, icon, glow, title, Icon } = config

    return (
        <div className={cn(
            "my-8 rounded-2xl overflow-hidden",
            "border-l-4",
            border,
            "shadow-xl",
            glow
        )}>
            <div className={cn(bg, "p-6")}>
                <div className="flex items-start gap-4">
                    <div className={cn(
                        "w-10 h-10 rounded-xl flex items-center justify-center",
                        "bg-gradient-to-br",
                        type === 'tldr' && "from-emerald-500 to-teal-500",
                        type === 'important' && "from-amber-500 to-orange-500",
                        type === 'tip' && "from-blue-500 to-indigo-500",
                        type === 'warning' && "from-rose-500 to-pink-500",
                        type === 'success' && "from-green-500 to-emerald-500",
                        "shadow-lg"
                    )}>
                        <Icon className="w-5 h-5 text-white" />
                    </div>
                    <div className="flex-1">
                        <span className={cn("text-sm font-bold uppercase tracking-wider", text)}>
                            {title}
                        </span>
                        <div className="mt-2 text-zinc-300 leading-relaxed">
                            {children}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   COLLAPSIBLE SECTION
   ============================================================================ */

function CollapsibleDetails({ summary, children }: { summary: string; children: React.ReactNode }) {
    const [isOpen, setIsOpen] = useState(false)

    return (
        <div className={cn(
            "my-6 rounded-2xl overflow-hidden",
            "border border-violet-500/30",
            "bg-gradient-to-r from-violet-500/5 via-purple-500/5 to-indigo-500/5",
            "shadow-xl shadow-violet-500/10"
        )}>
            <button
                onClick={() => setIsOpen(!isOpen)}
                className={cn(
                    "w-full flex items-center gap-3 px-5 py-4 text-left",
                    "bg-gradient-to-r from-violet-600/20 via-purple-600/20 to-indigo-600/20",
                    "text-violet-300 font-semibold",
                    "hover:from-violet-600/30 hover:via-purple-600/30 hover:to-indigo-600/30",
                    "transition-all duration-300"
                )}
            >
                <div className={cn(
                    "w-8 h-8 rounded-lg flex items-center justify-center",
                    "bg-violet-500/20 transition-transform duration-300",
                    isOpen && "rotate-90"
                )}>
                    <ChevronRight className="w-4 h-4 text-violet-400" />
                </div>
                <HelpCircle className="w-5 h-5 text-violet-400" />
                <span>{summary}</span>
            </button>
            {isOpen && (
                <div className="px-5 py-4 border-t border-violet-500/20 text-zinc-300">
                    {children}
                </div>
            )}
        </div>
    )
}

/* ============================================================================
   VIBRANT SECTION HEADER
   ============================================================================ */

function SectionHeader({ children, variant = 'default' }: { children: React.ReactNode; variant?: string }) {
    const text = String(children).toLowerCase()

    // Determine color based on content
    let gradient = "from-violet-500 via-purple-500 to-indigo-500"
    let Icon = FileText

    if (text.includes("varför") || text.includes("mål") || text.includes("target")) {
        gradient = "from-amber-500 via-orange-500 to-red-500"
        Icon = Target
    } else if (text.includes("praktisk") || text.includes("övning") || text.includes("example")) {
        gradient = "from-cyan-500 via-blue-500 to-indigo-500"
        Icon = Code2
    } else if (text.includes("quiz") || text.includes("checkpoint") || text.includes("testa")) {
        gradient = "from-fuchsia-500 via-pink-500 to-rose-500"
        Icon = HelpCircle
    } else if (text.includes("tips") || text.includes("pro")) {
        gradient = "from-emerald-500 via-teal-500 to-cyan-500"
        Icon = Lightbulb
    } else if (text.includes("referens") || text.includes("copy-paste") || text.includes("cheat")) {
        gradient = "from-yellow-500 via-amber-500 to-orange-500"
        Icon = Star
    } else if (text.includes("varning") || text.includes("obs") || text.includes("danger")) {
        gradient = "from-rose-500 via-red-500 to-orange-500"
        Icon = AlertTriangle
    } else if (text.includes("kom ihåg") || text.includes("summary") || text.includes("sammanfatt")) {
        gradient = "from-green-500 via-emerald-500 to-teal-500"
        Icon = Brain
    } else if (text.includes("grund") || text.includes("basic") || text.includes("introduk")) {
        gradient = "from-blue-500 via-indigo-500 to-violet-500"
        Icon = BookOpen
    }

    return (
        <div className="relative mt-12 mb-6">
            {/* Glow effect */}
            <div className={cn(
                "absolute -inset-1 rounded-2xl blur-xl opacity-30",
                `bg-gradient-to-r ${gradient}`
            )} />

            <div className={cn(
                "relative flex items-center gap-4 p-4 rounded-2xl",
                "bg-zinc-900/80 backdrop-blur-sm",
                "border border-white/10"
            )}>
                <div className={cn(
                    "w-12 h-12 rounded-xl flex items-center justify-center",
                    `bg-gradient-to-br ${gradient}`,
                    "shadow-lg"
                )}>
                    <Icon className="w-6 h-6 text-white" />
                </div>
                <h2 className={cn(
                    "text-2xl font-bold bg-clip-text text-transparent",
                    `bg-gradient-to-r ${gradient}`
                )}>
                    {children}
                </h2>
            </div>
        </div>
    )
}

/* ============================================================================
   PREMIUM TABLE
   ============================================================================ */

function PremiumTable({ children }: { children: React.ReactNode }) {
    return (
        <div className={cn(
            "my-8 rounded-2xl overflow-hidden",
            "border border-violet-500/20",
            "shadow-xl shadow-violet-500/10",
            "bg-gradient-to-br from-zinc-900/80 via-zinc-900/60 to-zinc-800/40"
        )}>
            <div className="overflow-x-auto">
                <table className="w-full text-sm">
                    {children}
                </table>
            </div>
        </div>
    )
}

/* ============================================================================
   PREMIUM CODE BLOCK
   ============================================================================ */

function PremiumCodeBlock({ children, language = 'bash' }: { children: string; language?: string }) {
    const langColors: Record<string, string> = {
        bash: "from-emerald-500 to-teal-500",
        shell: "from-emerald-500 to-teal-500",
        sh: "from-emerald-500 to-teal-500",
        javascript: "from-yellow-500 to-amber-500",
        js: "from-yellow-500 to-amber-500",
        typescript: "from-blue-500 to-indigo-500",
        ts: "from-blue-500 to-indigo-500",
        python: "from-blue-400 to-yellow-500",
        py: "from-blue-400 to-yellow-500",
        sql: "from-orange-500 to-red-500",
        yaml: "from-pink-500 to-rose-500",
        yml: "from-pink-500 to-rose-500",
        json: "from-amber-500 to-orange-500",
        dockerfile: "from-cyan-500 to-blue-500",
        docker: "from-cyan-500 to-blue-500",
        nginx: "from-green-500 to-emerald-500",
        plaintext: "from-zinc-400 to-zinc-500",
        ini: "from-violet-500 to-purple-500",
    }

    const gradient = langColors[language.toLowerCase()] || "from-violet-500 to-purple-500"

    return (
        <div className="group relative my-6">
            {/* Glow effect */}
            <div className={cn(
                "absolute -inset-0.5 rounded-2xl blur-lg opacity-30",
                `bg-gradient-to-r ${gradient}`
            )} />

            <div className={cn(
                "relative rounded-2xl overflow-hidden",
                "border border-white/10",
                COLORS.code.bg
            )}>
                {/* Language badge */}
                <div className={cn(
                    "flex items-center justify-between px-4 py-2",
                    "border-b border-white/5",
                    COLORS.code.header
                )}>
                    <div className="flex items-center gap-2">
                        <Terminal className="w-4 h-4 text-violet-400" />
                        <span className={cn(
                            "text-xs font-bold uppercase tracking-wider",
                            "bg-clip-text text-transparent",
                            `bg-gradient-to-r ${gradient}`
                        )}>
                            {language}
                        </span>
                    </div>
                    <div className="flex items-center gap-1.5">
                        <div className="w-3 h-3 rounded-full bg-red-500/60" />
                        <div className="w-3 h-3 rounded-full bg-yellow-500/60" />
                        <div className="w-3 h-3 rounded-full bg-green-500/60" />
                    </div>
                </div>

                {/* Code content */}
                <pre className="p-4 overflow-x-auto">
                    <code className="text-sm font-mono text-zinc-100 leading-relaxed">
                        {children.trim()}
                    </code>
                </pre>

                <CopyButton code={children.trim()} />
            </div>
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
            const scrolled = Math.max(0, -rect.top + windowHeight * 0.5)
            const progress = Math.min(100, (scrolled / elementHeight) * 100)
            setReadProgress(Math.round(progress))
            onProgressUpdate?.(Math.round(progress))
        }

        window.addEventListener("scroll", handleScroll)
        return () => window.removeEventListener("scroll", handleScroll)
    }, [onProgressUpdate])

    // Detect if content starts with TL;DR blockquote
    const detectCalloutType = (text: string): CalloutType | null => {
        const lower = text.toLowerCase()
        if (lower.includes("tl;dr") || lower.includes("tldr")) return 'tldr'
        if (lower.includes("varning") || lower.includes("obs!") || lower.includes("⚠️")) return 'warning'
        if (lower.includes("tips") || lower.includes("💡")) return 'tip'
        if (lower.includes("viktigt") || lower.includes("notera") || lower.includes("🎯")) return 'important'
        return null
    }

    return (
        <div className="relative">
            {/* Premium Progress Bar */}
            <div className={cn(
                "sticky top-0 z-10 -mx-6 md:-mx-8 px-6 md:px-8 py-4",
                "bg-zinc-900/90 backdrop-blur-xl",
                "border-b border-white/5"
            )}>
                <div className="flex items-center justify-between mb-3">
                    <div className="flex items-center gap-3">
                        <div className={cn(
                            "w-8 h-8 rounded-lg flex items-center justify-center",
                            "bg-gradient-to-br from-violet-500 to-purple-500"
                        )}>
                            <BookOpen className="w-4 h-4 text-white" />
                        </div>
                        <span className="text-sm font-medium text-zinc-400">Läsframsteg</span>
                    </div>
                    <div className="flex items-center gap-4">
                        {estimatedMinutes && (
                            <span className="flex items-center gap-1.5 text-sm text-zinc-500">
                                <Clock className="w-4 h-4" />
                                ~{estimatedMinutes} min
                            </span>
                        )}
                        <span className={cn(
                            "text-lg font-bold bg-clip-text text-transparent",
                            "bg-gradient-to-r from-violet-400 to-purple-400"
                        )}>
                            {readProgress}%
                        </span>
                    </div>
                </div>

                {/* Animated gradient progress bar */}
                <div className="relative h-2 rounded-full bg-zinc-800 overflow-hidden">
                    <div
                        className={cn(
                            "absolute inset-y-0 left-0 rounded-full",
                            "bg-gradient-to-r from-violet-500 via-purple-500 to-indigo-500",
                            "transition-all duration-500 ease-out"
                        )}
                        style={{ width: `${readProgress}%` }}
                    />
                    {/* Shimmer effect */}
                    <div
                        className={cn(
                            "absolute inset-y-0 w-1/3 -skew-x-12",
                            "bg-gradient-to-r from-transparent via-white/20 to-transparent"
                        )}
                        style={{
                            left: `${Math.max(0, readProgress - 30)}%`,
                            opacity: readProgress > 0 && readProgress < 100 ? 1 : 0,
                            animation: "shimmer 2s infinite"
                        }}
                    />
                </div>
            </div>

            {/* Lesson Content */}
            <div ref={contentRef} className="pt-8">
                <article className="prose prose-invert max-w-none">
                    <ReactMarkdown
                        remarkPlugins={[remarkGfm]}
                        rehypePlugins={[rehypeHighlight]}
                        components={{
                            // Premium H1
                            h1: ({ children }) => (
                                <h1 className={cn(
                                    "text-4xl md:text-5xl font-black mb-8 mt-0",
                                    "bg-clip-text text-transparent",
                                    "bg-gradient-to-r from-white via-zinc-200 to-zinc-400"
                                )}>
                                    {children}
                                </h1>
                            ),

                            // Vibrant H2 sections
                            h2: ({ children }) => (
                                <SectionHeader>{children}</SectionHeader>
                            ),

                            // Styled H3
                            h3: ({ children }) => {
                                const text = String(children).toLowerCase()
                                let gradient = "from-zinc-100 to-zinc-300"

                                if (text.includes("exempel") || text.includes("example")) {
                                    gradient = "from-cyan-400 to-blue-400"
                                } else if (text.includes("syntax") || text.includes("format")) {
                                    gradient = "from-violet-400 to-purple-400"
                                } else if (text.includes("vanlig") || text.includes("common")) {
                                    gradient = "from-amber-400 to-orange-400"
                                }

                                return (
                                    <h3 className={cn(
                                        "text-xl font-bold mt-8 mb-4",
                                        "bg-clip-text text-transparent",
                                        `bg-gradient-to-r ${gradient}`
                                    )}>
                                        {children}
                                    </h3>
                                )
                            },

                            // Clean paragraphs
                            p: ({ children }) => (
                                <p className="text-base text-zinc-300 leading-8 mb-5">
                                    {children}
                                </p>
                            ),

                            // Premium lists
                            ul: ({ children }) => (
                                <ul className="my-5 space-y-3 list-none pl-0">
                                    {children}
                                </ul>
                            ),
                            ol: ({ children }) => (
                                <ol className="my-5 space-y-3 list-none pl-0 counter-reset-[item]">
                                    {children}
                                </ol>
                            ),
                            li: ({ children, ...props }) => {
                                const isOrdered = (props as any).ordered
                                return (
                                    <li className="flex items-start gap-3 text-zinc-300">
                                        {isOrdered ? (
                                            <span className={cn(
                                                "flex-shrink-0 w-7 h-7 rounded-lg flex items-center justify-center",
                                                "bg-gradient-to-br from-violet-500 to-purple-500",
                                                "text-xs font-bold text-white"
                                            )}>
                                                {(props as any).index + 1}
                                            </span>
                                        ) : (
                                            <span className={cn(
                                                "flex-shrink-0 w-2 h-2 mt-2.5 rounded-full",
                                                "bg-gradient-to-r from-violet-500 to-purple-500"
                                            )} />
                                        )}
                                        <span className="flex-1">{children}</span>
                                    </li>
                                )
                            },

                            // Premium tables
                            table: ({ children }) => (
                                <PremiumTable>{children}</PremiumTable>
                            ),
                            thead: ({ children }) => (
                                <thead className={cn(
                                    "bg-gradient-to-r from-violet-600/20 via-purple-600/20 to-indigo-600/20"
                                )}>
                                    {children}
                                </thead>
                            ),
                            th: ({ children }) => (
                                <th className={cn(
                                    "px-4 py-3 text-left font-bold",
                                    "text-violet-300 border-b border-violet-500/30"
                                )}>
                                    {children}
                                </th>
                            ),
                            td: ({ children }) => (
                                <td className={cn(
                                    "px-4 py-3 text-zinc-300",
                                    "border-b border-white/5"
                                )}>
                                    {children}
                                </td>
                            ),

                            // Premium code blocks
                            pre: ({ children }) => {
                                const code = extractCodeText(children)
                                let language = 'plaintext'

                                if (typeof children === 'object' && children !== null && 'props' in children) {
                                    const childElement = children as React.ReactElement<{ className?: string }>
                                    const className = childElement?.props?.className || ''
                                    const languageMatch = className.match(/language-(\w+)/)
                                    if (languageMatch) language = languageMatch[1]
                                }

                                return (
                                    <PremiumCodeBlock language={language}>
                                        {code}
                                    </PremiumCodeBlock>
                                )
                            },

                            // Vibrant inline code
                            code: ({ className, children, ...props }) => {
                                const isInline = !className
                                if (isInline) {
                                    return (
                                        <code className={cn(
                                            "px-2 py-1 rounded-lg font-mono text-sm",
                                            "bg-gradient-to-r from-violet-500/20 to-purple-500/20",
                                            "text-violet-300 border border-violet-500/30"
                                        )} {...props}>
                                            {children}
                                        </code>
                                    )
                                }
                                return <code className={className} {...props}>{children}</code>
                            },

                            // Vibrant blockquotes/callouts
                            blockquote: ({ children }) => {
                                const text = extractCodeText(children)
                                const type = detectCalloutType(text)

                                if (type) {
                                    return <CalloutBox type={type}>{children}</CalloutBox>
                                }

                                return (
                                    <CalloutBox type="tip">{children}</CalloutBox>
                                )
                            },

                            // Collapsible details
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
                            summary: () => null,

                            // Premium dividers
                            hr: () => (
                                <div className="my-12 flex items-center gap-4">
                                    <div className="flex-1 h-px bg-gradient-to-r from-transparent via-violet-500/50 to-transparent" />
                                    <Sparkles className="w-5 h-5 text-violet-500" />
                                    <div className="flex-1 h-px bg-gradient-to-r from-transparent via-violet-500/50 to-transparent" />
                                </div>
                            ),

                            // Bold text
                            strong: ({ children }) => (
                                <strong className="font-bold text-white">
                                    {children}
                                </strong>
                            ),

                            // Links
                            a: ({ href, children }) => (
                                <a
                                    href={href}
                                    className={cn(
                                        "text-violet-400 hover:text-violet-300",
                                        "underline decoration-violet-500/30 hover:decoration-violet-500",
                                        "transition-colors"
                                    )}
                                    target={href?.startsWith('http') ? '_blank' : undefined}
                                    rel={href?.startsWith('http') ? 'noopener noreferrer' : undefined}
                                >
                                    {children}
                                </a>
                            ),
                        }}
                    >
                        {content}
                    </ReactMarkdown>
                </article>
            </div>

            {/* Completion celebration */}
            {readProgress >= 90 && (
                <div className={cn(
                    "mt-12 relative rounded-2xl overflow-hidden",
                    "border border-emerald-500/30"
                )}>
                    {/* Background glow */}
                    <div className="absolute inset-0 bg-gradient-to-r from-emerald-500/10 via-teal-500/10 to-cyan-500/10" />

                    <div className="relative p-6 flex items-center gap-5">
                        <div className={cn(
                            "w-14 h-14 rounded-2xl flex items-center justify-center",
                            "bg-gradient-to-br from-emerald-500 to-teal-500",
                            "shadow-xl shadow-emerald-500/30"
                        )}>
                            <Award className="w-7 h-7 text-white" />
                        </div>
                        <div>
                            <p className={cn(
                                "text-lg font-bold",
                                "bg-clip-text text-transparent",
                                "bg-gradient-to-r from-emerald-400 to-teal-400"
                            )}>
                                Utmärkt! Du har läst igenom lektionen!
                            </p>
                            <p className="text-sm text-emerald-300/70 mt-1">
                                Markera som slutförd för att samla dina XP och fortsätt till nästa nod.
                            </p>
                        </div>
                    </div>
                </div>
            )}
        </div>
    )
}

export default LessonContent
