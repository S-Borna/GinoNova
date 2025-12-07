"use client"

/**
 * Study Page - Simple, clean study flow
 * 
 * Flow:
 * 1. Select module
 * 2. Select lessons (checkboxes)
 * 3. Choose: Flashcards or Multiple Choice Quiz
 * 4. Study!
 */

import * as React from "react"
import { useState, useEffect } from "react"
import Link from "next/link"
import { cn } from "@/lib/utils"
import {
    BookOpen,
    Brain,
    CheckSquare,
    Square,
    ArrowRight,
    Shuffle,
    Terminal,
    Box,
    Shield,
    Cloud,
    GitBranch,
    Layers,
    Server,
    Code,
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

interface StudyLesson {
    id: string
    title: string
    flashcard_count: number
    quiz_count: number
}

interface StudyModuleDetail {
    slug: string
    title: string
    description: string
    icon: string
    lessons: StudyLesson[]
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
    const [modules, setModules] = useState<StudyModule[]>([])
    const [selectedModule, setSelectedModule] = useState<StudyModuleDetail | null>(null)
    const [selectedLessons, setSelectedLessons] = useState<Set<string>>(new Set())
    const [randomize, setRandomize] = useState(false)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    // Fetch modules on mount
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

    async function selectModule(slug: string) {
        try {
            setLoading(true)
            const res = await fetch(`${API_BASE_URL}/api/study/modules/${slug}`)
            if (!res.ok) throw new Error("Failed to fetch module")
            const data = await res.json()
            setSelectedModule(data)
            setSelectedLessons(new Set()) // Reset selection
        } catch (err) {
            setError(err instanceof Error ? err.message : "Error loading module")
        } finally {
            setLoading(false)
        }
    }

    function toggleLesson(lessonId: string) {
        setSelectedLessons(prev => {
            const newSet = new Set(prev)
            if (newSet.has(lessonId)) {
                newSet.delete(lessonId)
            } else {
                newSet.add(lessonId)
            }
            return newSet
        })
    }

    function selectAllLessons() {
        if (!selectedModule) return
        setSelectedLessons(new Set(selectedModule.lessons.map(l => l.id)))
    }

    function clearAllLessons() {
        setSelectedLessons(new Set())
    }

    function goBack() {
        setSelectedModule(null)
        setSelectedLessons(new Set())
    }

    function getStudyUrl(type: "flashcards" | "quiz") {
        if (!selectedModule) return "#"
        
        const lessonsParam = selectedLessons.size > 0 
            ? `&lessons=${Array.from(selectedLessons).join(",")}`
            : ""
        const shuffleParam = randomize ? "&shuffle=true" : ""
        
        return `/study/${selectedModule.slug}/${type}?${lessonsParam}${shuffleParam}`
    }

    // Calculate totals for selected lessons
    const selectedStats = selectedModule?.lessons
        .filter(l => selectedLessons.size === 0 || selectedLessons.has(l.id))
        .reduce(
            (acc, l) => ({
                flashcards: acc.flashcards + l.flashcard_count,
                quiz: acc.quiz + l.quiz_count,
            }),
            { flashcards: 0, quiz: 0 }
        ) || { flashcards: 0, quiz: 0 }

    /* ============================================================================
       RENDER: Module Selection
       ============================================================================ */

    if (!selectedModule) {
        return (
            <div className="min-h-screen bg-zinc-950 text-white p-8">
                <div className="max-w-6xl mx-auto">
                    {/* Header */}
                    <div className="mb-8">
                        <h1 className="text-3xl font-bold mb-2">Study</h1>
                        <p className="text-zinc-400">
                            Öva med flashcards, quiz och terminal-simulator för att förstärka dina kunskaper. Välj en modul för att börja öva.
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

                    {/* Module Grid */}
                    {!loading && (
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                            {modules.map(module => (
                                <button
                                    key={module.slug}
                                    onClick={() => selectModule(module.slug)}
                                    className={cn(
                                        "group text-left p-6 rounded-xl",
                                        "bg-zinc-900/50 border border-zinc-800",
                                        "hover:border-purple-500/50 hover:bg-zinc-900",
                                        "transition-all duration-200"
                                    )}
                                >
                                    <div className="flex items-start gap-4">
                                        <div className={cn(
                                            "w-12 h-12 rounded-lg flex items-center justify-center",
                                            "bg-purple-500/20 text-purple-400"
                                        )}>
                                            {ICON_MAP[module.icon] || <BookOpen className="w-6 h-6" />}
                                        </div>
                                        <div className="flex-1">
                                            <h3 className="font-semibold text-lg mb-1 group-hover:text-purple-300 transition-colors">
                                                {module.title}
                                            </h3>
                                            <p className="text-sm text-zinc-500 mb-3">
                                                {module.description}
                                            </p>
                                            <div className="flex gap-4 text-xs text-zinc-600">
                                                <span>{module.flashcard_count} flashcards</span>
                                                <span>{module.quiz_count} quiz-frågor</span>
                                            </div>
                                        </div>
                                    </div>
                                </button>
                            ))}
                        </div>
                    )}
                </div>
            </div>
        )
    }

    /* ============================================================================
       RENDER: Lesson Selection
       ============================================================================ */

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-8">
            <div className="max-w-4xl mx-auto">
                {/* Back Button */}
                <button
                    onClick={goBack}
                    className="text-zinc-400 hover:text-white mb-6 flex items-center gap-2"
                >
                    ← Tillbaka
                </button>

                {/* Module Header */}
                <div className="mb-8">
                    <h1 className="text-3xl font-bold mb-2">{selectedModule.title}</h1>
                    <p className="text-zinc-400">{selectedModule.description}</p>
                </div>

                {/* Lesson Selection */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6 mb-6">
                    <div className="flex items-center justify-between mb-4">
                        <div>
                            <h2 className="font-semibold text-lg">Välj lessons att öva på</h2>
                            <p className="text-sm text-zinc-500">
                                Välj en eller flera lessons, eller lämna tomt för hela modulen
                            </p>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={selectAllLessons}
                                className="px-3 py-1.5 text-sm bg-zinc-800 hover:bg-zinc-700 rounded-lg transition-colors"
                            >
                                Välj alla
                            </button>
                            <button
                                onClick={clearAllLessons}
                                className="px-3 py-1.5 text-sm bg-zinc-800 hover:bg-zinc-700 rounded-lg transition-colors"
                            >
                                Rensa alla
                            </button>
                        </div>
                    </div>

                    {/* Lessons Grid */}
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                        {selectedModule.lessons.map(lesson => (
                            <button
                                key={lesson.id}
                                onClick={() => toggleLesson(lesson.id)}
                                className={cn(
                                    "flex items-center gap-3 p-4 rounded-lg text-left",
                                    "border transition-all duration-200",
                                    selectedLessons.has(lesson.id)
                                        ? "bg-purple-500/20 border-purple-500/50"
                                        : "bg-zinc-800/50 border-zinc-700 hover:border-zinc-600"
                                )}
                            >
                                {selectedLessons.has(lesson.id) ? (
                                    <CheckSquare className="w-5 h-5 text-purple-400 shrink-0" />
                                ) : (
                                    <Square className="w-5 h-5 text-zinc-600 shrink-0" />
                                )}
                                <span className="truncate">{lesson.title}</span>
                            </button>
                        ))}
                    </div>
                </div>

                {/* Settings */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6 mb-6">
                    <h2 className="font-semibold text-lg mb-4">Inställningar</h2>
                    
                    <button
                        onClick={() => setRandomize(!randomize)}
                        className="flex items-center gap-3"
                    >
                        {randomize ? (
                            <CheckSquare className="w-5 h-5 text-purple-400" />
                        ) : (
                            <Square className="w-5 h-5 text-zinc-600" />
                        )}
                        <div className="text-left">
                            <p className="font-medium">Randomisera ordning</p>
                            <p className="text-sm text-zinc-500">
                                När ingen specifik lesson är vald kommer flashcards/quiz att visas i slumpmässig ordning
                            </p>
                        </div>
                    </button>
                </div>

                {/* Study Mode Selection */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {/* Flashcards */}
                    <Link
                        href={getStudyUrl("flashcards")}
                        className={cn(
                            "group p-6 rounded-xl",
                            "bg-gradient-to-br from-purple-600/20 to-purple-900/20",
                            "border border-purple-500/30",
                            "hover:border-purple-500/60 hover:from-purple-600/30",
                            "transition-all duration-200"
                        )}
                    >
                        <div className="flex items-center gap-4 mb-3">
                            <div className="w-12 h-12 rounded-xl bg-purple-500/20 flex items-center justify-center">
                                <BookOpen className="w-6 h-6 text-purple-400" />
                            </div>
                            <div>
                                <h3 className="font-semibold text-lg">Flashcards</h3>
                                <p className="text-sm text-zinc-400">Öva med flashcards för att memorera</p>
                            </div>
                        </div>
                        <p className="text-sm text-zinc-500">
                            Klicka för att börja öva med flashcards
                        </p>
                        <p className="text-xs text-purple-400 mt-2">
                            {selectedStats.flashcards} flashcards tillgängliga
                        </p>
                    </Link>

                    {/* Quiz */}
                    <Link
                        href={getStudyUrl("quiz")}
                        className={cn(
                            "group p-6 rounded-xl",
                            "bg-gradient-to-br from-blue-600/20 to-blue-900/20",
                            "border border-blue-500/30",
                            "hover:border-blue-500/60 hover:from-blue-600/30",
                            "transition-all duration-200"
                        )}
                    >
                        <div className="flex items-center gap-4 mb-3">
                            <div className="w-12 h-12 rounded-xl bg-blue-500/20 flex items-center justify-center">
                                <Brain className="w-6 h-6 text-blue-400" />
                            </div>
                            <div>
                                <h3 className="font-semibold text-lg">Multiple Choice Quiz</h3>
                                <p className="text-sm text-zinc-400">Testa dina kunskaper med frågor</p>
                            </div>
                        </div>
                        <p className="text-sm text-zinc-500">
                            Klicka för att börja quiz
                        </p>
                        <p className="text-xs text-blue-400 mt-2">
                            {selectedStats.quiz} quiz-frågor tillgängliga
                        </p>
                    </Link>
                </div>
            </div>
        </div>
    )
}
