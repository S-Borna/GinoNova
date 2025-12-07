"use client"

/**
 * Study Session Setup - Välj inställningar innan övning
 *
 * Användaren väljer:
 * 1. Svårighetsgrad (Easy, Medium, Hard, eller alla)
 * 2. Typ (Flashcards eller Quiz)
 * 3. Antal (10, 20, 30 eller valfritt 1-30)
 */

import * as React from "react"
import { useState, useEffect, Suspense } from "react"
import { useRouter, useSearchParams } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import {
    ArrowLeft,
    ArrowRight,
    BookOpen,
    Brain,
    Zap,
    Scale,
    Flame,
    Shuffle,
    Hash,
} from "lucide-react"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

/* ============================================================================
   TYPES
   ============================================================================ */

interface ModuleInfo {
    slug: string
    title: string
    flashcard_count: number
    quiz_count: number
}

/* ============================================================================
   STUDY SESSION SETUP COMPONENT
   ============================================================================ */

function StudySessionSetup() {
    const router = useRouter()
    const searchParams = useSearchParams()

    // Hämta valda moduler från URL
    const modulesParam = searchParams?.get("modules") || ""
    const selectedModules = modulesParam.split(",").filter(Boolean)

    // State
    const [moduleInfos, setModuleInfos] = useState<ModuleInfo[]>([])
    const [loading, setLoading] = useState(true)

    // Inställningar
    const [difficulty, setDifficulty] = useState<"all" | "easy" | "medium" | "hard">("all")
    const [studyType, setStudyType] = useState<"flashcards" | "quiz">("flashcards")
    const [count, setCount] = useState<number>(20)
    const [customCount, setCustomCount] = useState<string>("")
    const [shuffle, setShuffle] = useState(true)

    // Hämta modulinformation (parallellt för snabbhet)
    useEffect(() => {
        async function fetchModuleInfo() {
            if (selectedModules.length === 0) {
                router.push("/study")
                return
            }

            try {
                setLoading(true)

                // Parallella anrop istället för sekventiella
                const promises = selectedModules.map(async (slug) => {
                    const res = await fetch(`${API_BASE_URL}/api/study/modules/${slug}`)
                    if (res.ok) {
                        const data = await res.json()
                        return {
                            slug,
                            title: data.title,
                            flashcard_count: data.flashcard_count || 90,
                            quiz_count: data.quiz_count || 60,
                        }
                    }
                    return null
                })

                const results = await Promise.all(promises)
                setModuleInfos(results.filter((r): r is ModuleInfo => r !== null))
            } catch (err) {
                console.error("Error fetching module info:", err)
            } finally {
                setLoading(false)
            }
        }

        fetchModuleInfo()
    }, [selectedModules, router])

    // Beräkna totalt tillgängligt
    const totalFlashcards = moduleInfos.reduce((acc, m) => acc + m.flashcard_count, 0)
    const totalQuiz = moduleInfos.reduce((acc, m) => acc + m.quiz_count, 0)
    const maxAvailable = studyType === "flashcards" ? totalFlashcards : totalQuiz

    // Hantera count-val
    function handleCountSelect(value: number | "custom") {
        if (value === "custom") {
            setCount(0)
            setCustomCount("")
        } else {
            setCount(value)
            setCustomCount("")
        }
    }

    function handleCustomCountChange(e: React.ChangeEvent<HTMLInputElement>) {
        const val = e.target.value
        setCustomCount(val)
        const num = parseInt(val)
        if (!isNaN(num) && num >= 1 && num <= 30) {
            setCount(num)
        }
    }

    // Starta session
    function startSession() {
        const finalCount = count || parseInt(customCount) || 20
        const diffParam = difficulty === "all" ? "easy,medium,hard" : difficulty

        let url: string
        if (selectedModules.length === 1) {
            url = `/study/${selectedModules[0]}/${studyType}?difficulties=${diffParam}&count=${finalCount}`
        } else {
            url = `/study/combined/${studyType}?modules=${modulesParam}&difficulties=${diffParam}&count=${finalCount}`
        }

        if (shuffle) {
            url += "&shuffle=true"
        }

        router.push(url)
    }

    if (loading) {
        return (
            <div className="min-h-screen bg-zinc-950 text-white p-8">
                <div className="max-w-2xl mx-auto">
                    {/* Skeleton header */}
                    <div className="mb-8">
                        <div className="h-4 w-24 bg-zinc-800 rounded mb-4 animate-pulse" />
                        <div className="h-8 w-64 bg-zinc-800 rounded animate-pulse" />
                    </div>

                    {/* Skeleton cards */}
                    <div className="space-y-6">
                        <div className="h-32 bg-zinc-900/50 rounded-2xl border border-zinc-800 animate-pulse" />
                        <div className="h-32 bg-zinc-900/50 rounded-2xl border border-zinc-800 animate-pulse" />
                        <div className="h-32 bg-zinc-900/50 rounded-2xl border border-zinc-800 animate-pulse" />
                    </div>
                </div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-8">
            <div className="max-w-2xl mx-auto">
                {/* Header */}
                <div className="mb-8">
                    <Link
                        href="/study"
                        className="text-zinc-400 hover:text-white flex items-center gap-2 mb-4"
                    >
                        <ArrowLeft className="w-4 h-4" />
                        Tillbaka till Studyroom
                    </Link>
                    <h1 className="text-3xl font-bold mb-2">Konfigurera övning</h1>
                    <p className="text-zinc-400">
                        Välj inställningar för din session
                    </p>
                </div>

                {/* Valda moduler */}
                <div className="bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 mb-6">
                    <h2 className="text-sm font-semibold text-zinc-400 mb-3">VALDA MODULER</h2>
                    <div className="flex flex-wrap gap-2">
                        {moduleInfos.map((m) => (
                            <span
                                key={m.slug}
                                className="px-3 py-1.5 bg-purple-500/20 text-purple-300 rounded-lg text-sm"
                            >
                                {m.title}
                            </span>
                        ))}
                    </div>
                </div>

                {/* ============================================================
                    SVÅRIGHETSGRAD
                    ============================================================ */}
                <div className="bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 mb-6">
                    <h2 className="text-sm font-semibold text-zinc-400 mb-4">SVÅRIGHETSGRAD</h2>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                        {[
                            { value: "all", label: "Alla", icon: Scale, color: "purple" },
                            { value: "easy", label: "Lätt", icon: Zap, color: "emerald" },
                            { value: "medium", label: "Mellan", icon: Scale, color: "amber" },
                            { value: "hard", label: "Svår", icon: Flame, color: "red" },
                        ].map((opt) => (
                            <button
                                key={opt.value}
                                onClick={() => setDifficulty(opt.value as typeof difficulty)}
                                className={cn(
                                    "flex flex-col items-center gap-2 p-4 rounded-xl border transition-all",
                                    difficulty === opt.value
                                        ? `bg-${opt.color}-500/20 border-${opt.color}-500/50 text-${opt.color}-400`
                                        : "bg-zinc-800/50 border-zinc-700 text-zinc-400 hover:border-zinc-600"
                                )}
                                style={{
                                    backgroundColor: difficulty === opt.value
                                        ? opt.color === "purple" ? "rgba(168, 85, 247, 0.2)"
                                            : opt.color === "emerald" ? "rgba(16, 185, 129, 0.2)"
                                                : opt.color === "amber" ? "rgba(245, 158, 11, 0.2)"
                                                    : "rgba(239, 68, 68, 0.2)"
                                        : undefined,
                                    borderColor: difficulty === opt.value
                                        ? opt.color === "purple" ? "rgba(168, 85, 247, 0.5)"
                                            : opt.color === "emerald" ? "rgba(16, 185, 129, 0.5)"
                                                : opt.color === "amber" ? "rgba(245, 158, 11, 0.5)"
                                                    : "rgba(239, 68, 68, 0.5)"
                                        : undefined,
                                }}
                            >
                                <opt.icon className="w-5 h-5" />
                                <span className="text-sm font-medium">{opt.label}</span>
                            </button>
                        ))}
                    </div>
                </div>

                {/* ============================================================
                    TYP AV ÖVNING
                    ============================================================ */}
                <div className="bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 mb-6">
                    <h2 className="text-sm font-semibold text-zinc-400 mb-4">TYP AV ÖVNING</h2>
                    <div className="grid grid-cols-2 gap-4">
                        <button
                            onClick={() => setStudyType("flashcards")}
                            className={cn(
                                "flex flex-col items-center gap-3 p-6 rounded-xl border transition-all",
                                studyType === "flashcards"
                                    ? "bg-purple-500/20 border-purple-500/50"
                                    : "bg-zinc-800/50 border-zinc-700 hover:border-zinc-600"
                            )}
                        >
                            <BookOpen className={cn(
                                "w-8 h-8",
                                studyType === "flashcards" ? "text-purple-400" : "text-zinc-500"
                            )} />
                            <div className="text-center">
                                <p className="font-semibold">Flashcards</p>
                                <p className="text-xs text-zinc-500">{totalFlashcards} tillgängliga</p>
                            </div>
                        </button>

                        <button
                            onClick={() => setStudyType("quiz")}
                            className={cn(
                                "flex flex-col items-center gap-3 p-6 rounded-xl border transition-all",
                                studyType === "quiz"
                                    ? "bg-blue-500/20 border-blue-500/50"
                                    : "bg-zinc-800/50 border-zinc-700 hover:border-zinc-600"
                            )}
                        >
                            <Brain className={cn(
                                "w-8 h-8",
                                studyType === "quiz" ? "text-blue-400" : "text-zinc-500"
                            )} />
                            <div className="text-center">
                                <p className="font-semibold">Multiple Quiz</p>
                                <p className="text-xs text-zinc-500">{totalQuiz} tillgängliga</p>
                            </div>
                        </button>
                    </div>
                </div>

                {/* ============================================================
                    ANTAL
                    ============================================================ */}
                <div className="bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 mb-6">
                    <h2 className="text-sm font-semibold text-zinc-400 mb-4">ANTAL FRÅGOR</h2>
                    <div className="grid grid-cols-4 gap-3 mb-4">
                        {[10, 20, 30].map((num) => (
                            <button
                                key={num}
                                onClick={() => handleCountSelect(num)}
                                className={cn(
                                    "flex items-center justify-center gap-2 p-3 rounded-xl border transition-all",
                                    count === num && !customCount
                                        ? "bg-purple-500/20 border-purple-500/50 text-purple-300"
                                        : "bg-zinc-800/50 border-zinc-700 text-zinc-400 hover:border-zinc-600"
                                )}
                            >
                                <span className="font-semibold">{num}</span>
                            </button>
                        ))}
                        <div className="relative">
                            <input
                                type="number"
                                min={1}
                                max={30}
                                value={customCount}
                                onChange={handleCustomCountChange}
                                placeholder="1-30"
                                className={cn(
                                    "w-full p-3 rounded-xl border text-center",
                                    "bg-zinc-800/50 border-zinc-700 text-white",
                                    "placeholder:text-zinc-500",
                                    "focus:outline-none focus:border-purple-500/50",
                                    customCount && "border-purple-500/50 bg-purple-500/20"
                                )}
                            />
                            <Hash className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-500" />
                        </div>
                    </div>
                    <p className="text-xs text-zinc-500 text-center">
                        Max {maxAvailable} {studyType === "flashcards" ? "flashcards" : "frågor"} tillgängliga
                    </p>
                </div>

                {/* ============================================================
                    SLUMPA ORDNING
                    ============================================================ */}
                <div className="bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 mb-8">
                    <label className="flex items-center justify-between cursor-pointer">
                        <div className="flex items-center gap-3">
                            <Shuffle className="w-5 h-5 text-zinc-400" />
                            <span className="font-medium">Slumpa ordning</span>
                        </div>
                        <button
                            onClick={() => setShuffle(!shuffle)}
                            className={cn(
                                "w-12 h-6 rounded-full transition-colors relative",
                                shuffle ? "bg-purple-500" : "bg-zinc-700"
                            )}
                        >
                            <span
                                className={cn(
                                    "absolute top-1 w-4 h-4 bg-white rounded-full transition-transform",
                                    shuffle ? "translate-x-7" : "translate-x-1"
                                )}
                            />
                        </button>
                    </label>
                </div>

                {/* ============================================================
                    STARTA KNAPP
                    ============================================================ */}
                <button
                    onClick={startSession}
                    disabled={count === 0 && !customCount}
                    className={cn(
                        "w-full flex items-center justify-center gap-3 p-4 rounded-xl",
                        "bg-gradient-to-r from-purple-600 to-blue-600",
                        "hover:from-purple-500 hover:to-blue-500",
                        "font-semibold text-lg transition-all",
                        "disabled:opacity-50 disabled:cursor-not-allowed"
                    )}
                >
                    Starta {studyType === "flashcards" ? "Flashcards" : "Quiz"}
                    <ArrowRight className="w-5 h-5" />
                </button>

                {/* Sammanfattning */}
                <p className="text-center text-zinc-500 text-sm mt-4">
                    {count || parseInt(customCount) || 20} {studyType === "flashcards" ? "flashcards" : "frågor"} • {difficulty === "all" ? "Alla nivåer" : difficulty === "easy" ? "Lätt" : difficulty === "medium" ? "Mellan" : "Svår"} • {shuffle ? "Slumpad" : "I ordning"}
                </p>
            </div>
        </div>
    )
}

/* ============================================================================
   EXPORT WITH SUSPENSE
   ============================================================================ */

export default function StudySessionPage() {
    return (
        <Suspense fallback={
            <div className="min-h-screen bg-zinc-950 text-white flex items-center justify-center">
                <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-purple-500" />
            </div>
        }>
            <StudySessionSetup />
        </Suspense>
    )
}
