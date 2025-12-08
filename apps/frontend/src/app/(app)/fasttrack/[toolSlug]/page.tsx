"use client"

/**
 * FastTrack Tool Detail Page
 *
 * Complete information about a specific DevOps tool:
 * - Description & use cases
 * - Installation commands
 * - Key features
 * - External links
 * - Quick access to Flashcards & Quiz
 */

import * as React from "react"
import { useParams, notFound } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import {
    ArrowLeft,
    BookOpen,
    Brain,
    ExternalLink,
    Terminal,
    Copy,
    Check,
    Sparkles,
    Target,
    Link as LinkIcon,
    Box,
    Code,
    Cloud,
    GitBranch,
    Monitor,
    Cpu,
    Network,
    Database,
    Shield,
    FileJson,
    Layers,
    Container,
} from "lucide-react"
import { TOOLS_DATA, TOOL_CATEGORIES, type Tool } from "@/data/fasttrack-tools"

/* ============================================================================
   COPY BUTTON COMPONENT
   ============================================================================ */

function CopyButton({ text }: { text: string }) {
    const [copied, setCopied] = React.useState(false)

    async function handleCopy() {
        await navigator.clipboard.writeText(text)
        setCopied(true)
        setTimeout(() => setCopied(false), 2000)
    }

    return (
        <button
            onClick={handleCopy}
            className={cn(
                "p-1.5 rounded-lg transition-all",
                copied
                    ? "bg-emerald-500/20 text-emerald-400"
                    : "bg-zinc-800 text-zinc-400 hover:text-white hover:bg-zinc-700"
            )}
        >
            {copied ? <Check className="w-4 h-4" /> : <Copy className="w-4 h-4" />}
        </button>
    )
}

/* ============================================================================
   CATEGORY ICONS
   ============================================================================ */

const CATEGORY_ICONS: Record<string, React.ElementType> = {
    dataformat: FileJson,
    containers: Box,
    orchestration: Container,
    linux: Terminal,
    python: Code,
    virtualization: Monitor,
    cloud: Cloud,
    cicd: GitBranch,
    monitoring: Cpu,
    network: Network,
    database: Database,
    security: Shield,
}

/* ============================================================================
   TOOL DETAIL PAGE
   ============================================================================ */

export default function ToolDetailPage() {
    const params = useParams()
    const toolSlug = params?.toolSlug as string

    // Find tool
    const tool = TOOLS_DATA.find(t => t.slug === toolSlug)

    if (!tool) {
        notFound()
    }

    const CategoryIcon = CATEGORY_ICONS[tool.category] || Layers
    const categoryLabel = TOOL_CATEGORIES.find(c => c.id === tool.category)?.label || tool.category

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-8">
            <div className="max-w-4xl mx-auto">
                {/* Back Link */}
                <Link
                    href="/fasttrack"
                    className="inline-flex items-center gap-2 text-zinc-400 hover:text-white mb-6 transition-colors"
                >
                    <ArrowLeft className="w-4 h-4" />
                    Tillbaka till FastTrack
                </Link>

                {/* Header */}
                <div className="flex items-start gap-6 mb-8">
                    <div className={cn(
                        "w-20 h-20 rounded-2xl flex items-center justify-center text-4xl",
                        "bg-gradient-to-br from-zinc-800 to-zinc-900",
                        "border border-zinc-700"
                    )}>
                        {tool.icon}
                    </div>
                    <div className="flex-1">
                        <div className="flex items-center gap-3 mb-2">
                            <h1 className="text-3xl font-bold">{tool.name}</h1>
                            <div className={cn(
                                "flex items-center gap-1.5 px-3 py-1 rounded-full",
                                "bg-zinc-800 border border-zinc-700"
                            )}>
                                <CategoryIcon className="w-3.5 h-3.5 text-zinc-400" />
                                <span className="text-xs text-zinc-400 capitalize">{categoryLabel}</span>
                            </div>
                        </div>
                        <p className="text-lg text-zinc-400">{tool.shortDesc}</p>
                    </div>
                </div>

                {/* Quick Actions */}
                <div className="grid grid-cols-2 gap-4 mb-8">
                    <Link
                        href={`/fasttrack/${tool.slug}/flashcards`}
                        className={cn(
                            "flex items-center justify-center gap-3 p-5 rounded-2xl",
                            "bg-gradient-to-br from-purple-600/20 to-purple-900/20",
                            "border border-purple-500/30",
                            "hover:border-purple-500/50 hover:from-purple-600/30 hover:to-purple-900/30",
                            "transition-all duration-300"
                        )}
                    >
                        <BookOpen className="w-6 h-6 text-purple-400" />
                        <div>
                            <p className="font-semibold text-white">Flashcards</p>
                            <p className="text-sm text-purple-400">{tool.flashcardCount} kort</p>
                        </div>
                    </Link>
                    <Link
                        href={`/fasttrack/${tool.slug}/quiz`}
                        className={cn(
                            "flex items-center justify-center gap-3 p-5 rounded-2xl",
                            "bg-gradient-to-br from-blue-600/20 to-blue-900/20",
                            "border border-blue-500/30",
                            "hover:border-blue-500/50 hover:from-blue-600/30 hover:to-blue-900/30",
                            "transition-all duration-300"
                        )}
                    >
                        <Brain className="w-6 h-6 text-blue-400" />
                        <div>
                            <p className="font-semibold text-white">Quiz</p>
                            <p className="text-sm text-blue-400">{tool.quizCount} frågor</p>
                        </div>
                    </Link>
                </div>

                {/* Description */}
                <section className="mb-8">
                    <h2 className="text-lg font-semibold mb-3 flex items-center gap-2">
                        <Sparkles className="w-5 h-5 text-amber-400" />
                        Om {tool.name}
                    </h2>
                    <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl p-5">
                        <p className="text-zinc-300 leading-relaxed">{tool.description}</p>
                    </div>
                </section>

                {/* Installation */}
                <section className="mb-8">
                    <h2 className="text-lg font-semibold mb-3 flex items-center gap-2">
                        <Terminal className="w-5 h-5 text-emerald-400" />
                        Installation
                    </h2>
                    <div className="space-y-3">
                        {tool.installation.apt && (
                            <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl p-4">
                                <div className="flex items-center justify-between mb-2">
                                    <span className="text-sm font-medium text-zinc-400">APT (Debian/Ubuntu)</span>
                                    <CopyButton text={tool.installation.apt} />
                                </div>
                                <code className="text-emerald-400 text-sm font-mono">{tool.installation.apt}</code>
                            </div>
                        )}
                        {tool.installation.brew && (
                            <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl p-4">
                                <div className="flex items-center justify-between mb-2">
                                    <span className="text-sm font-medium text-zinc-400">Homebrew (macOS)</span>
                                    <CopyButton text={tool.installation.brew} />
                                </div>
                                <code className="text-emerald-400 text-sm font-mono">{tool.installation.brew}</code>
                            </div>
                        )}
                        {tool.installation.pip && (
                            <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl p-4">
                                <div className="flex items-center justify-between mb-2">
                                    <span className="text-sm font-medium text-zinc-400">pip (Python)</span>
                                    <CopyButton text={tool.installation.pip} />
                                </div>
                                <code className="text-emerald-400 text-sm font-mono">{tool.installation.pip}</code>
                            </div>
                        )}
                        {tool.installation.npm && (
                            <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl p-4">
                                <div className="flex items-center justify-between mb-2">
                                    <span className="text-sm font-medium text-zinc-400">npm (Node.js)</span>
                                    <CopyButton text={tool.installation.npm} />
                                </div>
                                <code className="text-emerald-400 text-sm font-mono">{tool.installation.npm}</code>
                            </div>
                        )}
                        {tool.installation.other && (
                            <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl p-4">
                                <div className="flex items-center justify-between mb-2">
                                    <span className="text-sm font-medium text-zinc-400">Annat</span>
                                    <CopyButton text={tool.installation.other} />
                                </div>
                                <code className="text-emerald-400 text-sm font-mono break-all">{tool.installation.other}</code>
                            </div>
                        )}
                    </div>
                </section>

                {/* Use Cases */}
                <section className="mb-8">
                    <h2 className="text-lg font-semibold mb-3 flex items-center gap-2">
                        <Target className="w-5 h-5 text-blue-400" />
                        Användningsområden
                    </h2>
                    <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl p-5">
                        <div className="flex flex-wrap gap-2">
                            {tool.useCases.map((useCase, i) => (
                                <span
                                    key={i}
                                    className={cn(
                                        "px-3 py-1.5 rounded-lg text-sm",
                                        "bg-blue-500/10 text-blue-400 border border-blue-500/20"
                                    )}
                                >
                                    {useCase}
                                </span>
                            ))}
                        </div>
                    </div>
                </section>

                {/* Key Features */}
                <section className="mb-8">
                    <h2 className="text-lg font-semibold mb-3 flex items-center gap-2">
                        <Sparkles className="w-5 h-5 text-purple-400" />
                        Nyckelfunktioner
                    </h2>
                    <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl p-5">
                        <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
                            {tool.keyFeatures.map((feature, i) => (
                                <div
                                    key={i}
                                    className={cn(
                                        "flex items-center gap-2 px-3 py-2 rounded-lg",
                                        "bg-zinc-800/60 border border-zinc-700"
                                    )}
                                >
                                    <div className="w-2 h-2 rounded-full bg-purple-400" />
                                    <span className="text-sm text-zinc-300">{feature}</span>
                                </div>
                            ))}
                        </div>
                    </div>
                </section>

                {/* External Links */}
                {(tool.officialUrl || tool.docsUrl) && (
                    <section className="mb-8">
                        <h2 className="text-lg font-semibold mb-3 flex items-center gap-2">
                            <LinkIcon className="w-5 h-5 text-amber-400" />
                            Resurser
                        </h2>
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            {tool.officialUrl && (
                                <a
                                    href={tool.officialUrl}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className={cn(
                                        "flex items-center justify-between p-4 rounded-xl",
                                        "bg-zinc-900/60 border border-zinc-800",
                                        "hover:border-amber-500/30 hover:bg-zinc-800/60",
                                        "transition-all duration-200"
                                    )}
                                >
                                    <div>
                                        <p className="font-medium text-white">Officiell webbplats</p>
                                        <p className="text-sm text-zinc-500 truncate">{tool.officialUrl}</p>
                                    </div>
                                    <ExternalLink className="w-5 h-5 text-zinc-500" />
                                </a>
                            )}
                            {tool.docsUrl && (
                                <a
                                    href={tool.docsUrl}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className={cn(
                                        "flex items-center justify-between p-4 rounded-xl",
                                        "bg-zinc-900/60 border border-zinc-800",
                                        "hover:border-amber-500/30 hover:bg-zinc-800/60",
                                        "transition-all duration-200"
                                    )}
                                >
                                    <div>
                                        <p className="font-medium text-white">Dokumentation</p>
                                        <p className="text-sm text-zinc-500 truncate">{tool.docsUrl}</p>
                                    </div>
                                    <ExternalLink className="w-5 h-5 text-zinc-500" />
                                </a>
                            )}
                        </div>
                    </section>
                )}

                {/* Bottom CTA */}
                <div className="mt-12 p-6 rounded-2xl bg-gradient-to-r from-amber-500/10 to-orange-500/10 border border-amber-500/20">
                    <div className="flex items-center justify-between">
                        <div>
                            <h3 className="font-semibold text-white mb-1">Redo att lära dig {tool.name}?</h3>
                            <p className="text-sm text-zinc-400">
                                {tool.flashcardCount} flashcards och {tool.quizCount} quiz-frågor väntar!
                            </p>
                        </div>
                        <div className="flex gap-3">
                            <Link
                                href={`/fasttrack/${tool.slug}/flashcards`}
                                className={cn(
                                    "flex items-center gap-2 px-5 py-2.5 rounded-xl",
                                    "bg-purple-600 hover:bg-purple-500",
                                    "font-medium transition-all"
                                )}
                            >
                                <BookOpen className="w-4 h-4" />
                                Flashcards
                            </Link>
                            <Link
                                href={`/fasttrack/${tool.slug}/quiz`}
                                className={cn(
                                    "flex items-center gap-2 px-5 py-2.5 rounded-xl",
                                    "bg-blue-600 hover:bg-blue-500",
                                    "font-medium transition-all"
                                )}
                            >
                                <Brain className="w-4 h-4" />
                                Quiz
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
