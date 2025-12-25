"use client"

/**
 * FastTrack - DevOps Tools Library — COSMIC EDITION 🌌
 *
 * Complete reference for all DevOps tools with:
 * - Tool cards with info, installation, usage
 * - Flashcards & Quiz for each tool
 * - Combine mode to study multiple tools
 * - Search & filter by category
 *
 * COSMIC DESIGN: Deep space bg, aurora orbs, pulsating glows
 * @phase MILESTONE-2.0-COSMIC
 */

import * as React from "react"
import { useState, useMemo } from "react"
import Link from "next/link"
import { useRouter } from "next/navigation"
import { motion } from "framer-motion"
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
   COSMIC AURORA BACKGROUND
   ============================================================================ */

function CosmicAurora() {
    return (
        <div className="fixed inset-0 pointer-events-none overflow-hidden">
            <div className="absolute inset-0 bg-[#05050a]" />
            <div
                className="absolute inset-0 opacity-[0.03]"
                style={{
                    backgroundImage: `
                        linear-gradient(rgba(245, 158, 11, 0.3) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(245, 158, 11, 0.3) 1px, transparent 1px)
                    `,
                    backgroundSize: '60px 60px'
                }}
            />
            <motion.div
                className="absolute -top-40 -right-40 w-[700px] h-[700px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(245, 158, 11, 0.12) 0%, rgba(249, 115, 22, 0.04) 40%, transparent 70%)',
                }}
                animate={{ scale: [1, 1.1, 1], opacity: [0.5, 0.7, 0.5] }}
                transition={{ duration: 8, repeat: Infinity, ease: "easeInOut" }}
            />
            <motion.div
                className="absolute -bottom-60 -left-60 w-[600px] h-[600px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(139, 92, 246, 0.1) 0%, transparent 60%)',
                }}
                animate={{ scale: [1, 1.15, 1], opacity: [0.4, 0.6, 0.4] }}
                transition={{ duration: 10, repeat: Infinity, ease: "easeInOut", delay: 2 }}
            />
            <motion.div
                className="absolute top-1/2 left-1/3 w-[500px] h-[500px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(59, 130, 246, 0.06) 0%, transparent 60%)',
                }}
                animate={{ scale: [1, 1.2, 1], opacity: [0.3, 0.5, 0.3] }}
                transition={{ duration: 12, repeat: Infinity, ease: "easeInOut", delay: 4 }}
            />
        </div>
    )
}

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
        <div className="min-h-screen bg-[#05050a] text-white p-8 relative">
            <CosmicAurora />

            <div className="max-w-7xl mx-auto relative z-10">
                {/* Header with cosmic glow */}
                <motion.div
                    className="mb-8"
                    initial={{ opacity: 0, y: -20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ ease: [0.16, 1, 0.3, 1] }}
                >
                    <div className="flex items-center gap-3 mb-2">
                        <motion.div
                            className="p-2.5 rounded-xl bg-gradient-to-br from-amber-500 to-orange-600"
                            animate={{
                                boxShadow: [
                                    '0 0 15px rgba(245, 158, 11, 0.4)',
                                    '0 0 35px rgba(245, 158, 11, 0.7)',
                                    '0 0 15px rgba(245, 158, 11, 0.4)',
                                ]
                            }}
                            transition={{ duration: 2.5, repeat: Infinity, ease: "easeInOut" }}
                        >
                            <Zap className="w-6 h-6 text-white" />
                        </motion.div>
                        <h1 className="text-3xl font-bold bg-gradient-to-r from-amber-400 via-orange-400 to-amber-400 bg-clip-text text-transparent">
                            FastTrack
                        </h1>
                    </div>
                    <p className="text-zinc-400">
                        Komplett verktygsbibliotek för DevOps - lär dig med Flashcards & Quiz
                    </p>
                </motion.div>

                {/* Stats Bar with cosmic styling */}
                <div className="grid grid-cols-3 gap-4 mb-8">
                    <motion.div
                        className="bg-gradient-to-br from-amber-500/15 to-amber-600/5 border border-amber-500/40 rounded-xl p-4 text-center backdrop-blur-sm"
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
                        whileHover={{ scale: 1.02 }}
                        style={{ boxShadow: '0 0 30px rgba(245, 158, 11, 0.1)' }}
                    >
                        <p className="text-2xl font-bold text-amber-400">{totalStats.tools}</p>
                        <p className="text-sm text-zinc-500">Verktyg</p>
                    </motion.div>
                    <motion.div
                        className="bg-gradient-to-br from-purple-500/15 to-purple-600/5 border border-purple-500/40 rounded-xl p-4 text-center backdrop-blur-sm"
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
                        whileHover={{ scale: 1.02 }}
                        style={{ boxShadow: '0 0 30px rgba(139, 92, 246, 0.1)' }}
                    >
                        <p className="text-2xl font-bold text-purple-400">{totalStats.flashcards}</p>
                        <p className="text-sm text-zinc-500">Flashcards</p>
                    </motion.div>
                    <motion.div
                        className="bg-gradient-to-br from-blue-500/15 to-blue-600/5 border border-blue-500/40 rounded-xl p-4 text-center backdrop-blur-sm"
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.3, ease: [0.16, 1, 0.3, 1] }}
                        whileHover={{ scale: 1.02 }}
                        style={{ boxShadow: '0 0 30px rgba(59, 130, 246, 0.1)' }}
                    >
                        <p className="text-2xl font-bold text-blue-400">{totalStats.quiz}</p>
                        <p className="text-sm text-zinc-500">Quiz-frågor</p>
                    </motion.div>
                </div>

                {/* Search & Filter with cosmic styling */}
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
                                "bg-[#0a0a0f] border border-amber-500/30",
                                "text-white placeholder-zinc-500",
                                "focus:outline-none focus:border-amber-500/60 focus:shadow-[0_0_20px_rgba(245,158,11,0.15)]",
                                "transition-all duration-300"
                            )}
                        />
                    </div>

                    {!combineMode ? (
                        <motion.button
                            onClick={() => setCombineMode(true)}
                            className={cn(
                                "flex items-center gap-2 px-6 py-3 rounded-xl",
                                "bg-gradient-to-r from-amber-600 to-orange-600",
                                "hover:from-amber-500 hover:to-orange-500",
                                "font-medium transition-all"
                            )}
                            whileHover={{ scale: 1.02, boxShadow: '0 0 30px rgba(245, 158, 11, 0.4)' }}
                            whileTap={{ scale: 0.98 }}
                        >
                            <Combine className="w-5 h-5" />
                            Kombinera verktyg
                        </motion.button>
                    ) : (
                        <button
                            onClick={exitCombineMode}
                            className={cn(
                                "flex items-center gap-2 px-6 py-3 rounded-xl",
                                "bg-zinc-800/80 border border-zinc-700",
                                "hover:bg-zinc-700",
                                "font-medium transition-all"
                            )}
                        >
                            <X className="w-5 h-5" />
                            Avbryt
                        </button>
                    )}
                </div>

                {/* Category Filter with cosmic styling */}
                <div className="flex flex-wrap gap-2 mb-8">
                    {TOOL_CATEGORIES.map((cat) => {
                        const Icon = cat.icon
                        const isActive = selectedCategory === cat.id
                        return (
                            <motion.button
                                key={cat.id}
                                onClick={() => setSelectedCategory(cat.id)}
                                className={cn(
                                    "flex items-center gap-2 px-4 py-2 rounded-lg",
                                    "transition-all duration-300",
                                    isActive
                                        ? "bg-amber-500/25 text-amber-400 border border-amber-500/50"
                                        : "bg-[#0a0a0f] text-zinc-400 border border-zinc-800 hover:border-amber-500/30"
                                )}
                                whileHover={{ scale: 1.02 }}
                                whileTap={{ scale: 0.98 }}
                                style={isActive ? { boxShadow: '0 0 20px rgba(245, 158, 11, 0.15)' } : {}}
                            >
                                <Icon className="w-4 h-4" />
                                {cat.label}
                            </motion.button>
                        )
                    })}
                </div>

                {/* Combine Mode Selection Bar - cosmic styled */}
                {combineMode && selectedTools.size > 0 && (
                    <motion.div
                        className={cn(
                            "fixed bottom-0 left-0 right-0 z-50",
                            "bg-[#0a0a0f]/95 backdrop-blur-lg border-t border-amber-500/40",
                            "p-4"
                        )}
                        initial={{ y: 100 }}
                        animate={{ y: 0 }}
                        transition={{ ease: [0.16, 1, 0.3, 1] }}
                        style={{ boxShadow: '0 -10px 40px rgba(245, 158, 11, 0.15)' }}
                    >
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
                                <motion.div whileHover={{ scale: 1.03 }} whileTap={{ scale: 0.97 }}>
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
                                </motion.div>
                                <motion.div whileHover={{ scale: 1.03 }} whileTap={{ scale: 0.97 }}>
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
                                </motion.div>
                            </div>
                        </div>
                    </motion.div>
                )}

                {/* Tools Grid - cosmic cards */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 pb-24">
                    {filteredTools.map((tool, idx) => {
                        const isSelected = selectedTools.has(tool.slug)
                        const CategoryIcon = CATEGORY_ICONS[tool.category] || Layers

                        return (
                            <motion.div
                                key={tool.slug}
                                onClick={() => toggleTool(tool.slug)}
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: idx * 0.03, ease: [0.16, 1, 0.3, 1] }}
                                whileHover={{ scale: 1.02, y: -3 }}
                                className={cn(
                                    "group relative rounded-2xl p-5 cursor-pointer",
                                    "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14] border transition-all duration-300",
                                    combineMode && isSelected
                                        ? "border-amber-500 bg-amber-500/15"
                                        : "border-zinc-800/80 hover:border-amber-500/40"
                                )}
                                style={combineMode && isSelected ? { boxShadow: '0 0 30px rgba(245, 158, 11, 0.25)' } : {}}
                            >
                                {combineMode && (
                                    <div className="absolute top-4 right-4">
                                        {isSelected ? (
                                            <motion.div
                                                animate={{ scale: [1, 1.2, 1] }}
                                                transition={{ duration: 0.3 }}
                                            >
                                                <CheckSquare className="w-5 h-5 text-amber-400" />
                                            </motion.div>
                                        ) : (
                                            <Square className="w-5 h-5 text-zinc-600" />
                                        )}
                                    </div>
                                )}

                                <div className="flex items-start gap-4 mb-4">
                                    <motion.div
                                        className={cn(
                                            "w-14 h-14 rounded-xl flex items-center justify-center text-2xl",
                                            "bg-gradient-to-br from-zinc-800/80 to-zinc-900/80",
                                            "border border-zinc-700/50"
                                        )}
                                        whileHover={{
                                            boxShadow: '0 0 20px rgba(245, 158, 11, 0.3)'
                                        }}
                                    >
                                        {tool.icon}
                                    </motion.div>
                                    <div className="flex-1 min-w-0">
                                        <h3 className="font-semibold text-white text-lg truncate group-hover:text-amber-300 transition-colors">
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
                                    <motion.div
                                        className={cn(
                                            "absolute top-1/2 right-4 -translate-y-1/2",
                                            "opacity-0 group-hover:opacity-100 transition-opacity"
                                        )}
                                        animate={{
                                            x: [0, 5, 0]
                                        }}
                                        transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
                                    >
                                        <ArrowRight className="w-5 h-5 text-amber-400" />
                                    </motion.div>
                                )}
                            </motion.div>
                        )
                    })}
                </div>

                {filteredTools.length === 0 && (
                    <motion.div
                        className="text-center py-20"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                    >
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
                    </motion.div>
                )}
            </div>
        </div>
    )
}
