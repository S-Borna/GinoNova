"use client"

/**
 * Studyflow Flashcards & Quiz Page
 * Välj modul → välj topics → öva
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
    ArrowLeft,
} from "lucide-react"

const API_BASE_URL = "https://saas-project-production-9de8.up.railway.app"

/* ============================================================================
   TYPES
   ============================================================================ */

interface StudyflowModule {
    slug: string
    title: string
    description: string
    icon: string
    topic_count: number
    flashcard_count: number
    quiz_count: number
}

interface StudyflowTopic {
    id: string
    title: string
    flashcard_count: number
    quiz_count: number
}

interface StudyflowModuleDetail {
    slug: string
    title: string
    description: string
    icon: string
    topics: StudyflowTopic[]
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
   STUDYFLOW PRACTICE PAGE
   ============================================================================ */

export default function StudyflowPracticePage() {
    const [modules, setModules] = useState<StudyflowModule[]>([])
    const [selectedModule, setSelectedModule] = useState<StudyflowModuleDetail | null>(null)
    const [selectedTopics, setSelectedTopics] = useState<Set<string>>(new Set())
    const [randomize, setRandomize] = useState(false)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        fetchModules()
    }, [])

    async function fetchModules() {
        try {
            setLoading(true)
            const res = await fetch(`${API_BASE_URL}/api/studyflow/modules`)
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
            const res = await fetch(`${API_BASE_URL}/api/studyflow/modules/${slug}`)
            if (!res.ok) throw new Error("Failed to fetch module")
            const data = await res.json()
            setSelectedModule(data)
            setSelectedTopics(new Set())
        } catch (err) {
            setError(err instanceof Error ? err.message : "Error loading module")
        } finally {
            setLoading(false)
        }
    }

    function toggleTopic(topicId: string) {
        setSelectedTopics(prev => {
            const newSet = new Set(prev)
            if (newSet.has(topicId)) {
                newSet.delete(topicId)
            } else {
                newSet.add(topicId)
            }
            return newSet
        })
    }

    function selectAllTopics() {
        if (!selectedModule) return
        setSelectedTopics(new Set(selectedModule.topics.map(t => t.id)))
    }

    function clearAllTopics() {
        setSelectedTopics(new Set())
    }

    function goBack() {
        setSelectedModule(null)
        setSelectedTopics(new Set())
    }

    function getStudyUrl(type: "flashcards" | "quiz") {
        if (!selectedModule) return "#"

        const topicsParam = selectedTopics.size > 0
            ? `topics=${Array.from(selectedTopics).join(",")}`
            : ""
        const shuffleParam = randomize ? "shuffle=true" : ""
        const params = [topicsParam, shuffleParam].filter(Boolean).join("&")

        return `/studyflow/practice/${selectedModule.slug}/${type}${params ? `?${params}` : ""}`
    }

    const selectedStats = selectedModule?.topics
        .filter(t => selectedTopics.size === 0 || selectedTopics.has(t.id))
        .reduce(
            (acc, t) => ({
                flashcards: acc.flashcards + t.flashcard_count,
                quiz: acc.quiz + t.quiz_count,
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
                        <Link href="/studyflow" className="flex items-center gap-2 text-zinc-400 hover:text-white mb-4 transition-colors">
                            <ArrowLeft className="w-4 h-4" />
                            Tillbaka till Studyflow
                        </Link>
                        <h1 className="text-3xl font-bold mb-2">Öva</h1>
                        <p className="text-zinc-400">
                            Välj en modul och öva med flashcards eller quiz för att förstärka dina kunskaper.
                        </p>
                    </div>

                    {error && (
                        <div className="bg-red-500/10 border border-red-500/30 rounded-lg p-4 mb-6">
                            <p className="text-red-400">{error}</p>
                        </div>
                    )}

                    {loading && (
                        <div className="flex items-center justify-center py-20">
                            <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-purple-500" />
                        </div>
                    )}

                    {!loading && modules.length > 0 && (
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                            {modules.map((module) => (
                                <button
                                    key={module.slug}
                                    onClick={() => selectModule(module.slug)}
                                    className="bg-zinc-900/50 hover:bg-zinc-800/50 border border-zinc-800 hover:border-purple-500/50 rounded-xl p-6 text-left transition-all group"
                                >
                                    <div className="flex items-start gap-4">
                                        <div className="w-12 h-12 rounded-lg bg-purple-500/10 flex items-center justify-center text-purple-400 group-hover:bg-purple-500/20 transition-colors">
                                            {ICON_MAP[module.icon] || <BookOpen className="w-6 h-6" />}
                                        </div>
                                        <div className="flex-1">
                                            <h3 className="font-semibold text-lg mb-1 group-hover:text-purple-400 transition-colors">
                                                {module.title}
                                            </h3>
                                            <p className="text-sm text-zinc-500 mb-3">
                                                {module.description}
                                            </p>
                                            <div className="flex items-center gap-4 text-xs text-zinc-500">
                                                <span>{module.topic_count} topics</span>
                                                <span>{module.flashcard_count} flashcards</span>
                                                <span>{module.quiz_count} quiz</span>
                                            </div>
                                        </div>
                                    </div>
                                </button>
                            ))}
                        </div>
                    )}

                    {!loading && modules.length === 0 && !error && (
                        <div className="text-center py-20 text-zinc-500">
                            <BookOpen className="w-12 h-12 mx-auto mb-4 opacity-50" />
                            <p>Inga moduler tillgängliga ännu</p>
                        </div>
                    )}
                </div>
            </div>
        )
    }

    /* ============================================================================
       RENDER: Topic Selection
       ============================================================================ */

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-8">
            <div className="max-w-4xl mx-auto">
                <button
                    onClick={goBack}
                    className="flex items-center gap-2 text-zinc-400 hover:text-white mb-6 transition-colors"
                >
                    <ArrowLeft className="w-4 h-4" />
                    Tillbaka till moduler
                </button>

                {/* Module Header */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6 mb-6">
                    <div className="flex items-center gap-4 mb-4">
                        <div className="w-14 h-14 rounded-lg bg-purple-500/10 flex items-center justify-center text-purple-400">
                            {ICON_MAP[selectedModule.icon] || <BookOpen className="w-7 h-7" />}
                        </div>
                        <div>
                            <h1 className="text-2xl font-bold">{selectedModule.title}</h1>
                            <p className="text-zinc-400">{selectedModule.description}</p>
                        </div>
                    </div>
                </div>

                {/* Topic Selection */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6 mb-6">
                    <div className="flex items-center justify-between mb-4">
                        <h2 className="font-semibold">Välj topics att öva på</h2>
                        <div className="flex items-center gap-2">
                            <button
                                onClick={selectAllTopics}
                                className="text-sm text-purple-400 hover:text-purple-300 transition-colors"
                            >
                                Välj alla
                            </button>
                            <span className="text-zinc-600">|</span>
                            <button
                                onClick={clearAllTopics}
                                className="text-sm text-zinc-400 hover:text-zinc-300 transition-colors"
                            >
                                Rensa
                            </button>
                        </div>
                    </div>

                    <div className="space-y-2">
                        {selectedModule.topics.map((topic) => (
                            <button
                                key={topic.id}
                                onClick={() => toggleTopic(topic.id)}
                                className={cn(
                                    "w-full flex items-center gap-3 p-3 rounded-lg border transition-all text-left",
                                    selectedTopics.has(topic.id)
                                        ? "bg-purple-500/10 border-purple-500/30"
                                        : "bg-zinc-800/30 border-zinc-700/50 hover:border-zinc-600"
                                )}
                            >
                                {selectedTopics.has(topic.id) ? (
                                    <CheckSquare className="w-5 h-5 text-purple-400 flex-shrink-0" />
                                ) : (
                                    <Square className="w-5 h-5 text-zinc-500 flex-shrink-0" />
                                )}
                                <span className="flex-1">{topic.title}</span>
                                <span className="text-xs text-zinc-500">
                                    {topic.flashcard_count} fc / {topic.quiz_count} q
                                </span>
                            </button>
                        ))}
                    </div>
                </div>

                {/* Options */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6 mb-6">
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-3">
                            <Shuffle className="w-5 h-5 text-zinc-400" />
                            <span>Slumpa ordning</span>
                        </div>
                        <button
                            onClick={() => setRandomize(!randomize)}
                            className={cn(
                                "w-12 h-6 rounded-full transition-colors relative",
                                randomize ? "bg-purple-500" : "bg-zinc-700"
                            )}
                        >
                            <div
                                className={cn(
                                    "absolute top-1 w-4 h-4 rounded-full bg-white transition-transform",
                                    randomize ? "translate-x-7" : "translate-x-1"
                                )}
                            />
                        </button>
                    </div>
                </div>

                {/* Study Actions */}
                <div className="grid grid-cols-2 gap-4">
                    <Link
                        href={getStudyUrl("flashcards")}
                        className={cn(
                            "flex items-center justify-center gap-3 p-6 rounded-xl border transition-all",
                            selectedStats.flashcards > 0
                                ? "bg-gradient-to-br from-blue-500/10 to-purple-500/10 border-blue-500/30 hover:border-blue-400/50"
                                : "bg-zinc-800/30 border-zinc-700/30 opacity-50 pointer-events-none"
                        )}
                    >
                        <BookOpen className="w-6 h-6 text-blue-400" />
                        <div className="text-left">
                            <div className="font-semibold">Flashcards</div>
                            <div className="text-sm text-zinc-400">
                                {selectedStats.flashcards} kort
                            </div>
                        </div>
                        <ArrowRight className="w-5 h-5 text-zinc-400 ml-auto" />
                    </Link>

                    <Link
                        href={getStudyUrl("quiz")}
                        className={cn(
                            "flex items-center justify-center gap-3 p-6 rounded-xl border transition-all",
                            selectedStats.quiz > 0
                                ? "bg-gradient-to-br from-green-500/10 to-emerald-500/10 border-green-500/30 hover:border-green-400/50"
                                : "bg-zinc-800/30 border-zinc-700/30 opacity-50 pointer-events-none"
                        )}
                    >
                        <Brain className="w-6 h-6 text-green-400" />
                        <div className="text-left">
                            <div className="font-semibold">Quiz</div>
                            <div className="text-sm text-zinc-400">
                                {selectedStats.quiz} frågor
                            </div>
                        </div>
                        <ArrowRight className="w-5 h-5 text-zinc-400 ml-auto" />
                    </Link>
                </div>

                {selectedTopics.size === 0 && (
                    <p className="text-center text-zinc-500 text-sm mt-4">
                        💡 Välj inga topics för att inkludera alla, eller välj specifika topics att fokusera på
                    </p>
                )}
            </div>
        </div>
    )
}
