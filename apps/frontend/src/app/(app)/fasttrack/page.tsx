"use client"

/**
 * FastTrack - DevOps Tools Library
 *
 * Complete reference for all DevOps tools with:
 * - Tool cards with info, installation, usage
 * - Flashcards & Quiz for each tool
 * - Combine mode to study multiple tools
 * - Search & filter by category
 */

import * as React from "react"
import { useState, useMemo } from "react"
import Link from "next/link"
import { useRouter } from "next/navigation"
import { cn } from "@/lib/utils"
import {
    Search,
    BookOpen,
    Brain,
    CheckSquare,
    Square,
    ArrowRight,
    Combine,
    X,
    ExternalLink,
    Terminal,
    Box,
    Cloud,
    Database,
    GitBranch,
    Shield,
    Code,
    Layers,
    Monitor,
    Cpu,
    Network,
    Zap,
    FileJson,
    Container,
} from "lucide-react"
import { TOOLS_DATA, TOOL_CATEGORIES } from "@/data/fasttrack-tools"

/* ============================================================================
   ICON COMPONENT MAPPING
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
   FASTTRACK PAGE COMPONENT
   ============================================================================ */

export default function FastTrackPage() {
    const router = useRouter()
    const [searchQuery, setSearchQuery] = useState("")
    const [selectedCategory, setSelectedCategory] = useState("all")

    // Combine mode
    const [combineMode, setCombineMode] = useState(false)
    const [selectedTools, setSelectedTools] = useState<Set<string>>(new Set())

    // Filter tools
    const filteredTools = useMemo(() => {
        return TOOLS_DATA.filter(tool => {
            const matchesSearch =
                tool.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                tool.shortDesc.toLowerCase().includes(searchQuery.toLowerCase()) ||
                tool.category.toLowerCase().includes(searchQuery.toLowerCase())

            const matchesCategory = selectedCategory === "all" || tool.category === selectedCategory

            return matchesSearch && matchesCategory
        })
    }, [searchQuery, selectedCategory])

    function toggleTool(slug: string) {
        if (!combineMode) {
            router.push(`/fasttrack/${slug}`)
            return
        }

        setSelectedTools(prev => {
            const newSet = new Set(prev)
            if (newSet.has(slug)) {
                newSet.delete(slug)
            } else {
                newSet.add(slug)
            }
            return newSet
        })
    }

    function exitCombineMode() {
        setCombineMode(false)
        setSelectedTools(new Set())
    }

    // Stats for selected tools
    const selectedStats = TOOLS_DATA
        .filter(t => selectedTools.has(t.slug))
        .reduce(
            (acc, t) => ({
                flashcards: acc.flashcards + t.flashcardCount,
                quiz: acc.quiz + t.quizCount,
            }),
            { flashcards: 0, quiz: 0 }
        )

    // Total stats
    const totalStats = TOOLS_DATA.reduce(
        (acc, t) => ({
            flashcards: acc.flashcards + t.flashcardCount,
            quiz: acc.quiz + t.quizCount,
            tools: acc.tools + 1,
        }),
        { flashcards: 0, quiz: 0, tools: 0 }
    )

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-8">
            <div className="max-w-7xl mx-auto">
                {/* Header */}
                <div className="mb-8">
                    <div className="flex items-center gap-3 mb-2">
                        <div className="p-2 rounded-xl bg-gradient-to-br from-amber-500 to-orange-600">
                            <Zap className="w-6 h-6 text-white" />
                        </div>
                        <h1 className="text-3xl font-bold">FastTrack</h1>
                    </div>
                    <p className="text-zinc-400">
                        Komplett verktygsbibliotek för DevOps - lär dig med Flashcards & Quiz
                    </p>
                </div>

                {/* Stats Bar */}
                <div className="grid grid-cols-3 gap-4 mb-8">
                    <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl p-4 text-center">
                        <p className="text-2xl font-bold text-amber-400">{totalStats.tools}</p>
                        <p className="text-sm text-zinc-500">Verktyg</p>
                    </div>
                    <div className="bg-zinc-900/60 border border-purple-500/30 rounded-xl p-4 text-center">
                        <p className="text-2xl font-bold text-purple-400">{totalStats.flashcards}</p>
                        <p className="text-sm text-zinc-500">Flashcards</p>
                    </div>
                    <div className="bg-zinc-900/60 border border-blue-500/30 rounded-xl p-4 text-center">
                        <p className="text-2xl font-bold text-blue-400">{totalStats.quiz}</p>
                        <p className="text-sm text-zinc-500">Quiz-frågor</p>
                    </div>
                </div>

                {/* Search & Filter */}
                <div className="flex flex-col md:flex-row gap-4 mb-6">
                    <div className="relative flex-1">
                        <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-zinc-500" />
                        <input
                            type="text"
                            placeholder="Sök verktyg..."
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                            className={cn(
                                "w-full pl-12 pr-4 py-3 rounded-xl",
                                "bg-zinc-900 border border-zinc-800",
                                "text-white placeholder-zinc-500",
                                "focus:outline-none focus:border-amber-500/50"
                            )}
                        />
                    </div>

                    {!combineMode ? (
                        <button
                            onClick={() => setCombineMode(true)}
                            className={cn(
                                "flex items-center gap-2 px-6 py-3 rounded-xl",
                                "bg-gradient-to-r from-amber-600 to-orange-600",
                                "hover:from-amber-500 hover:to-orange-500",
                                "font-medium transition-all"
                            )}
                        >
                            <Combine className="w-5 h-5" />
                            Kombinera verktyg
                        </button>
                    ) : (
                        <button
                            onClick={exitCombineMode}
                            className={cn(
                                "flex items-center gap-2 px-6 py-3 rounded-xl",
                                "bg-zinc-800 border border-zinc-700",
                                "hover:bg-zinc-700",
                                "font-medium transition-all"
                            )}
                        >
                            <X className="w-5 h-5" />
                            Avbryt
                        </button>
                    )}
                </div>

                {/* Category Filter */}
                <div className="flex flex-wrap gap-2 mb-8">
                    {TOOL_CATEGORIES.map((cat) => {
                        const Icon = cat.icon
                        const isActive = selectedCategory === cat.id
                        return (
                            <button
                                key={cat.id}
                                onClick={() => setSelectedCategory(cat.id)}
                                className={cn(
                                    "flex items-center gap-2 px-4 py-2 rounded-lg",
                                    "transition-all duration-200",
                                    isActive
                                        ? "bg-amber-500/20 text-amber-400 border border-amber-500/30"
                                        : "bg-zinc-900 text-zinc-400 border border-zinc-800 hover:border-zinc-700"
                                )}
                            >
                                <Icon className="w-4 h-4" />
                                {cat.label}
                            </button>
                        )
                    })}
                </div>

                {/* Combine Mode Selection Bar */}
                {combineMode && selectedTools.size > 0 && (
                    <div className={cn(
                        "fixed bottom-0 left-0 right-0 z-50",
                        "bg-zinc-900/95 backdrop-blur-lg border-t border-amber-500/30",
                        "p-4"
                    )}>
                        <div className="max-w-7xl mx-auto flex items-center justify-between">
                            <div className="flex items-center gap-4">
                                <div className="text-sm">
                                    <span className="text-amber-400 font-bold">{selectedTools.size}</span>
                                    <span className="text-zinc-400"> verktyg valda</span>
                                </div>
                                <div className="text-sm text-zinc-500">
                                    {selectedStats.flashcards} flashcards • {selectedStats.quiz} quiz-frågor
                                </div>
                            </div>
                            <div className="flex gap-3">
                                <Link
                                    href={`/fasttrack/session?tools=${Array.from(selectedTools).join(",")}&mode=flashcards`}
                                    className={cn(
                                        "flex items-center gap-2 px-6 py-2.5 rounded-xl",
                                        "bg-purple-600 hover:bg-purple-500",
                                        "font-medium transition-all"
                                    )}
                                >
                                    <BookOpen className="w-4 h-4" />
                                    Flashcards
                                </Link>
                                <Link
                                    href={`/fasttrack/session?tools=${Array.from(selectedTools).join(",")}&mode=quiz`}
                                    className={cn(
                                        "flex items-center gap-2 px-6 py-2.5 rounded-xl",
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
                )}

                {/* Tools Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 pb-24">
                    {filteredTools.map((tool) => {
                        const isSelected = selectedTools.has(tool.slug)
                        const CategoryIcon = CATEGORY_ICONS[tool.category] || Layers

                        return (
                            <div
                                key={tool.slug}
                                onClick={() => toggleTool(tool.slug)}
                                className={cn(
                                    "group relative rounded-2xl p-5 cursor-pointer",
                                    "bg-zinc-900/60 border transition-all duration-300",
                                    combineMode && isSelected
                                        ? "border-amber-500 bg-amber-500/10 shadow-[0_0_20px_rgba(245,158,11,0.2)]"
                                        : "border-zinc-800 hover:border-zinc-700 hover:bg-zinc-800/60"
                                )}
                            >
                                {combineMode && (
                                    <div className="absolute top-4 right-4">
                                        {isSelected ? (
                                            <CheckSquare className="w-5 h-5 text-amber-400" />
                                        ) : (
                                            <Square className="w-5 h-5 text-zinc-600" />
                                        )}
                                    </div>
                                )}

                                <div className="flex items-start gap-4 mb-4">
                                    <div className={cn(
                                        "w-14 h-14 rounded-xl flex items-center justify-center text-2xl",
                                        "bg-gradient-to-br from-zinc-800 to-zinc-900",
                                        "border border-zinc-700"
                                    )}>
                                        {tool.icon}
                                    </div>
                                    <div className="flex-1 min-w-0">
                                        <h3 className="font-semibold text-white text-lg truncate">
                                            {tool.name}
                                        </h3>
                                        <p className="text-sm text-zinc-400 truncate">
                                            {tool.shortDesc}
                                        </p>
                                    </div>
                                </div>

                                <div className="flex items-center gap-2 mb-3">
                                    <CategoryIcon className="w-3.5 h-3.5 text-zinc-500" />
                                    <span className="text-xs text-zinc-500 capitalize">
                                        {TOOL_CATEGORIES.find(c => c.id === tool.category)?.label || tool.category}
                                    </span>
                                </div>

                                <div className="flex items-center gap-4">
                                    <div className="flex items-center gap-1.5">
                                        <BookOpen className="w-4 h-4 text-purple-400" />
                                        <span className="text-sm text-zinc-400">{tool.flashcardCount}</span>
                                    </div>
                                    <div className="flex items-center gap-1.5">
                                        <Brain className="w-4 h-4 text-blue-400" />
                                        <span className="text-sm text-zinc-400">{tool.quizCount}</span>
                                    </div>
                                    {tool.officialUrl && (
                                        <ExternalLink className="w-4 h-4 text-zinc-600 ml-auto" />
                                    )}
                                </div>

                                {!combineMode && (
                                    <div className={cn(
                                        "absolute top-1/2 right-4 -translate-y-1/2",
                                        "opacity-0 group-hover:opacity-100 transition-opacity"
                                    )}>
                                        <ArrowRight className="w-5 h-5 text-amber-400" />
                                    </div>
                                )}
                            </div>
                        )
                    })}
                </div>

                {filteredTools.length === 0 && (
                    <div className="text-center py-20">
                        <Search className="w-16 h-16 text-zinc-700 mx-auto mb-4" />
                        <p className="text-zinc-400 text-lg">
                            Inga verktyg matchar din sökning
                        </p>
                        <button
                            onClick={() => {
                                setSearchQuery("")
                                setSelectedCategory("all")
                            }}
                            className="mt-4 text-amber-400 hover:text-amber-300"
                        >
                            Rensa filter
                        </button>
                    </div>
                )}
            </div>
        </div>
    )
}
