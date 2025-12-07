"use client"

/**
 * Study Page - Kombinera moduler och öva!
 *
 * Flow:
 * 1. Se alla moduler + reklam för flashcards/quiz
 * 2. Klicka "Kombinera moduler" för att välja flera
 * 3. Välj svårighetsgrad
 * 4. Starta Flashcards eller Quiz
 */

import * as React from "react"
import { useState, useEffect } from "react"
import Link from "next/link"
import { useRouter } from "next/navigation"
import { cn } from "@/lib/utils"
import {
    BookOpen,
    Brain,
    CheckSquare,
    Square,
    ArrowRight,
    Terminal,
    Box,
    Shield,
    Cloud,
    GitBranch,
    Layers,
    Server,
    Code,
    Combine,
    X,
    Sparkles,
} from "lucide-react"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

/* ============================================================================
   TYPES
   ============================================================================ */

interface StudyModule {
    slug: string
    title: string
    description: string
    icon: string
    lesson_count: number
    flashcard_count: number
    quiz_count: number
}

/* ============================================================================
   ICON MAPPING
   ============================================================================ */

const ICON_MAP: Record<string, React.ReactNode> = {
    "Terminal": <Terminal className="w-6 h-6" />,
    "Box": <Box className="w-6 h-6" />,
    "Shield": <Shield className="w-6 h-6" />,
    "Cloud": <Cloud className="w-6 h-6" />,
    "GitBranch": <GitBranch className="w-6 h-6" />,
    "Layers": <Layers className="w-6 h-6" />,
    "Server": <Server className="w-6 h-6" />,
    "Code": <Code className="w-6 h-6" />,
}

/* ============================================================================
   STUDY PAGE COMPONENT
   ============================================================================ */

export default function StudyPage() {
    const router = useRouter()
    const [modules, setModules] = useState<StudyModule[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    
    // Kombinera-läge
    const [combineMode, setCombineMode] = useState(false)
    const [selectedModules, setSelectedModules] = useState<Set<string>>(new Set())
    
    // Svårighetsgrad
    const [selectedDifficulties, setSelectedDifficulties] = useState<Set<string>>(new Set(["easy", "medium", "hard"]))
    const [randomize, setRandomize] = useState(true)

    useEffect(() => {
        fetchModules()
    }, [])

    async function fetchModules() {
        try {
            setLoading(true)
            const res = await fetch(`${API_BASE_URL}/api/study/modules`)
            if (!res.ok) throw new Error("Failed to fetch modules")
            const data = await res.json()
            setModules(data)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Error loading modules")
        } finally {
            setLoading(false)
        }
    }

    function toggleModule(slug: string) {
        if (!combineMode) {
            // Normal mode - gå direkt till modul
            router.push(`/study/${slug}/flashcards?shuffle=true`)
            return
        }
        
        // Combine mode - toggle selection
        setSelectedModules(prev => {
            const newSet = new Set(prev)
            if (newSet.has(slug)) {
                newSet.delete(slug)
            } else {
                newSet.add(slug)
            }
            return newSet
        })
    }

    function toggleDifficulty(diff: string) {
        setSelectedDifficulties(prev => {
            const newSet = new Set(prev)
            if (newSet.has(diff)) {
                newSet.delete(diff)
            } else {
                newSet.add(diff)
            }
            return newSet
        })
    }

    function startCombinedStudy(type: "flashcards" | "quiz") {
        if (selectedModules.size === 0) return
        
        const modulesParam = Array.from(selectedModules).join(",")
        const diffParam = Array.from(selectedDifficulties).join(",")
        const shuffleParam = randomize ? "&shuffle=true" : ""
        
        // Om bara en modul, gå till vanliga sidan
        if (selectedModules.size === 1) {
            const slug = Array.from(selectedModules)[0]
            router.push(`/study/${slug}/${type}?difficulties=${diffParam}${shuffleParam}`)
        } else {
            // Flera moduler - kombinerad vy
            router.push(`/study/combined/${type}?modules=${modulesParam}&difficulties=${diffParam}${shuffleParam}`)
        }
    }

    function exitCombineMode() {
        setCombineMode(false)
        setSelectedModules(new Set())
    }

    // Beräkna totaler för valda moduler
    const selectedStats = modules
        .filter(m => selectedModules.has(m.slug))
        .reduce(
            (acc, m) => ({
                flashcards: acc.flashcards + m.flashcard_count,
                quiz: acc.quiz + m.quiz_count,
            }),
            { flashcards: 0, quiz: 0 }
        )

    // Totaler för alla moduler (för reklam)
    const totalStats = modules.reduce(
        (acc, m) => ({
            flashcards: acc.flashcards + m.flashcard_count,
            quiz: acc.quiz + m.quiz_count,
        }),
        { flashcards: 0, quiz: 0 }
    )

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-8">
            <div className="max-w-6xl mx-auto">
                {/* Header */}
                <div className="mb-8">
                    <h1 className="text-3xl font-bold mb-2">📚 Studyroom</h1>
                    <p className="text-zinc-400">
                        Öva med flashcards och quiz för att förstärka dina DevOps-kunskaper
                    </p>
                </div>

                {/* Error */}
                {error && (
                    <div className="bg-red-500/10 border border-red-500/30 rounded-lg p-4 mb-6">
                        <p className="text-red-400">{error}</p>
                    </div>
                )}

                {/* Loading */}
                {loading && (
                    <div className="flex items-center justify-center py-20">
                        <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-purple-500" />
                    </div>
                )}

                {!loading && (
                    <>
                        {/* ============================================================
                            REKLAM-KORT (Döda preview-kort)
                            ============================================================ */}
                        <div className="mb-8">
                            <h2 className="text-lg font-semibold mb-4 text-zinc-300">Öva på olika sätt</h2>
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                {/* Flashcard Preview (DÖD) */}
                                <div className={cn(
                                    "relative overflow-hidden rounded-2xl",
                                    "bg-gradient-to-br from-purple-600/20 to-purple-900/20",
                                    "border border-purple-500/30 p-6",
                                    "opacity-90"
                                )}>
                                    <div className="absolute top-3 right-3">
                                        <span className="text-xs bg-purple-500/30 text-purple-300 px-2 py-1 rounded-full">
                                            Preview
                                        </span>
                                    </div>
                                    
                                    {/* Mini Flashcard Preview */}
                                    <div className="mb-4">
                                        <div className={cn(
                                            "w-full aspect-[3/2] rounded-xl p-4",
                                            "bg-gradient-to-br from-purple-500/30 to-purple-700/30",
                                            "border border-purple-400/20",
                                            "flex flex-col items-center justify-center"
                                        )}>
                                            <p className="text-xs text-purple-300 mb-2">Fråga</p>
                                            <p className="text-sm text-center text-zinc-200">
                                                Vad gör kommandot `chmod 755`?
                                            </p>
                                            <p className="text-xs text-zinc-500 mt-3">
                                                Klicka för att vända
                                            </p>
                                        </div>
                                    </div>

                                    <div className="flex items-center gap-3">
                                        <div className="w-10 h-10 rounded-lg bg-purple-500/20 flex items-center justify-center">
                                            <BookOpen className="w-5 h-5 text-purple-400" />
                                        </div>
                                        <div>
                                            <h3 className="font-semibold">Flashcards</h3>
                                            <p className="text-xs text-zinc-500">
                                                {totalStats.flashcards} kort tillgängliga
                                            </p>
                                        </div>
                                    </div>
                                </div>

                                {/* Quiz Preview (DÖD) */}
                                <div className={cn(
                                    "relative overflow-hidden rounded-2xl",
                                    "bg-gradient-to-br from-blue-600/20 to-blue-900/20",
                                    "border border-blue-500/30 p-6",
                                    "opacity-90"
                                )}>
                                    <div className="absolute top-3 right-3">
                                        <span className="text-xs bg-blue-500/30 text-blue-300 px-2 py-1 rounded-full">
                                            Preview
                                        </span>
                                    </div>
                                    
                                    {/* Mini Quiz Preview */}
                                    <div className="mb-4 space-y-2">
                                        <p className="text-sm text-zinc-200 mb-3">
                                            Vilket kommando listar filer?
                                        </p>
                                        <div className="space-y-1.5">
                                            {["ls -la", "cd ..", "pwd", "cat file"].map((opt, i) => (
                                                <div 
                                                    key={i}
                                                    className={cn(
                                                        "flex items-center gap-2 p-2 rounded-lg text-xs",
                                                        i === 0 
                                                            ? "bg-emerald-500/20 border border-emerald-500/30" 
                                                            : "bg-zinc-800/50 border border-zinc-700/50"
                                                    )}
                                                >
                                                    <span className={cn(
                                                        "w-5 h-5 rounded-full flex items-center justify-center text-xs",
                                                        i === 0 ? "bg-emerald-500 text-white" : "bg-zinc-700 text-zinc-400"
                                                    )}>
                                                        {String.fromCharCode(65 + i)}
                                                    </span>
                                                    <span className={i === 0 ? "text-emerald-300" : "text-zinc-400"}>
                                                        {opt}
                                                    </span>
                                                </div>
                                            ))}
                                        </div>
                                    </div>

                                    <div className="flex items-center gap-3">
                                        <div className="w-10 h-10 rounded-lg bg-blue-500/20 flex items-center justify-center">
                                            <Brain className="w-5 h-5 text-blue-400" />
                                        </div>
                                        <div>
                                            <h3 className="font-semibold">Multiple Choice Quiz</h3>
                                            <p className="text-xs text-zinc-500">
                                                {totalStats.quiz} frågor tillgängliga
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        {/* ============================================================
                            KOMBINERA MODULER KNAPP
                            ============================================================ */}
                        <div className="flex items-center justify-between mb-6">
                            <h2 className="text-lg font-semibold text-zinc-300">Välj modul</h2>
                            
                            {!combineMode ? (
                                <button
                                    onClick={() => setCombineMode(true)}
                                    className={cn(
                                        "flex items-center gap-2 px-4 py-2 rounded-lg",
                                        "bg-gradient-to-r from-purple-600/30 to-blue-600/30",
                                        "border border-purple-500/30 hover:border-purple-500/50",
                                        "text-sm font-medium transition-all"
                                    )}
                                >
                                    <Combine className="w-4 h-4" />
                                    Kombinera moduler
                                </button>
                            ) : (
                                <button
                                    onClick={exitCombineMode}
                                    className={cn(
                                        "flex items-center gap-2 px-4 py-2 rounded-lg",
                                        "bg-zinc-800 hover:bg-zinc-700",
                                        "text-sm font-medium transition-all"
                                    )}
                                >
                                    <X className="w-4 h-4" />
                                    Avbryt
                                </button>
                            )}
                        </div>

                        {/* Combine Mode Info */}
                        {combineMode && (
                            <div className="bg-purple-500/10 border border-purple-500/30 rounded-xl p-4 mb-6">
                                <div className="flex items-center gap-3 mb-3">
                                    <Sparkles className="w-5 h-5 text-purple-400" />
                                    <p className="text-purple-300 font-medium">
                                        Kombinera-läge aktivt
                                    </p>
                                </div>
                                <p className="text-sm text-zinc-400 mb-4">
                                    Markera de moduler du vill kombinera, välj svårighetsgrad och klicka Klar.
                                </p>
                                
                                {/* Svårighetsgrad */}
                                <div className="flex flex-wrap gap-2 mb-4">
                                    {[
                                        { id: "easy", label: "Grundläggande", color: "emerald" },
                                        { id: "medium", label: "Medel", color: "yellow" },
                                        { id: "hard", label: "Avancerad", color: "red" },
                                    ].map(diff => {
                                        const isSelected = selectedDifficulties.has(diff.id)
                                        return (
                                            <button
                                                key={diff.id}
                                                onClick={() => toggleDifficulty(diff.id)}
                                                className={cn(
                                                    "flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm",
                                                    "border transition-all",
                                                    isSelected && diff.color === "emerald" && "bg-emerald-500/20 border-emerald-500/50 text-emerald-300",
                                                    isSelected && diff.color === "yellow" && "bg-yellow-500/20 border-yellow-500/50 text-yellow-300",
                                                    isSelected && diff.color === "red" && "bg-red-500/20 border-red-500/50 text-red-300",
                                                    !isSelected && "bg-zinc-800/50 border-zinc-700 text-zinc-500"
                                                )}
                                            >
                                                {isSelected ? (
                                                    <CheckSquare className="w-4 h-4" />
                                                ) : (
                                                    <Square className="w-4 h-4" />
                                                )}
                                                {diff.label}
                                            </button>
                                        )
                                    })}
                                </div>

                                {/* Valda moduler info */}
                                {selectedModules.size > 0 && (
                                    <div className="flex items-center justify-between pt-3 border-t border-purple-500/20">
                                        <div className="text-sm">
                                            <span className="text-purple-300 font-medium">
                                                {selectedModules.size} modul{selectedModules.size > 1 ? "er" : ""} valda
                                            </span>
                                            <span className="text-zinc-500 ml-2">
                                                ({selectedStats.flashcards} flashcards, {selectedStats.quiz} quiz)
                                            </span>
                                        </div>
                                        <div className="flex gap-2">
                                            <button
                                                onClick={() => startCombinedStudy("flashcards")}
                                                className={cn(
                                                    "flex items-center gap-2 px-4 py-2 rounded-lg",
                                                    "bg-purple-600 hover:bg-purple-500",
                                                    "text-sm font-medium transition-all"
                                                )}
                                            >
                                                <BookOpen className="w-4 h-4" />
                                                Flashcards
                                            </button>
                                            <button
                                                onClick={() => startCombinedStudy("quiz")}
                                                className={cn(
                                                    "flex items-center gap-2 px-4 py-2 rounded-lg",
                                                    "bg-blue-600 hover:bg-blue-500",
                                                    "text-sm font-medium transition-all"
                                                )}
                                            >
                                                <Brain className="w-4 h-4" />
                                                Quiz
                                            </button>
                                        </div>
                                    </div>
                                )}
                            </div>
                        )}

                        {/* ============================================================
                            MODUL GRID
                            ============================================================ */}
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                            {modules.map(module => {
                                const isSelected = selectedModules.has(module.slug)
                                
                                return (
                                    <button
                                        key={module.slug}
                                        onClick={() => toggleModule(module.slug)}
                                        className={cn(
                                            "group text-left p-6 rounded-xl",
                                            "border transition-all duration-200",
                                            combineMode && isSelected
                                                ? "bg-purple-500/20 border-purple-500/50"
                                                : "bg-zinc-900/50 border-zinc-800 hover:border-purple-500/50 hover:bg-zinc-900"
                                        )}
                                    >
                                        <div className="flex items-start gap-4">
                                            {combineMode && (
                                                <div className="pt-1">
                                                    {isSelected ? (
                                                        <CheckSquare className="w-5 h-5 text-purple-400" />
                                                    ) : (
                                                        <Square className="w-5 h-5 text-zinc-600" />
                                                    )}
                                                </div>
                                            )}
                                            <div className={cn(
                                                "w-12 h-12 rounded-lg flex items-center justify-center shrink-0",
                                                isSelected 
                                                    ? "bg-purple-500/30 text-purple-300"
                                                    : "bg-purple-500/20 text-purple-400"
                                            )}>
                                                {ICON_MAP[module.icon] || <BookOpen className="w-6 h-6" />}
                                            </div>
                                            <div className="flex-1 min-w-0">
                                                <h3 className={cn(
                                                    "font-semibold text-lg mb-1 transition-colors truncate",
                                                    isSelected 
                                                        ? "text-purple-300" 
                                                        : "group-hover:text-purple-300"
                                                )}>
                                                    {module.title}
                                                </h3>
                                                <p className="text-sm text-zinc-500 mb-3 line-clamp-2">
                                                    {module.description}
                                                </p>
                                                <div className="flex gap-4 text-xs text-zinc-600">
                                                    <span>{module.flashcard_count} flashcards</span>
                                                    <span>{module.quiz_count} quiz</span>
                                                </div>
                                            </div>
                                        </div>
                                        
                                        {/* Normal mode: visa pil */}
                                        {!combineMode && (
                                            <div className="flex justify-end mt-4">
                                                <ArrowRight className="w-5 h-5 text-zinc-600 group-hover:text-purple-400 transition-colors" />
                                            </div>
                                        )}
                                    </button>
                                )
                            })}
                        </div>
                    </>
                )}
            </div>
        </div>
    )
}
