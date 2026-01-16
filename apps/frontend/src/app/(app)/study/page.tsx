"use client"

/**
 * Studyroom - Premium Cosmic Design
 * Flashcards & Quiz för DOE25 + Linux 24/7
 *
 * ⚠️ VIKTIGT: Detta är HUVUDSIDAN för Tenta-Simulator!
 * - Denna sida visas i sidomenyn under "Studyroom"
 * - Här väljer användaren inställningar (tid, frågor, källa)
 * - Klick på "Starta" skickar till /study/tenta-simulator med URL-params
 *
 * Vid ändringar av frågekällor (t.ex. nya quiz-moduler):
 * → Uppdatera DENNA FIL FÖRST (study/page.tsx)
 * → tenta-simulator/page.tsx används för själva quiz-körningen
 */

import * as React from "react"
import { useState, useEffect, useMemo } from "react"
import Link from "next/link"
import { useRouter } from "next/navigation"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    BookOpen,
    Brain,
    CheckSquare,
    ArrowRight,
    Sparkles,
    Zap,
    Clock,
    Trophy,
    GraduationCap,
    Layers,
    ChevronRight,
    ChevronDown,
    Check,
    Square,
    Shuffle,
    Award
} from "lucide-react"

// Import module data
import { DOE25_MODULE } from "@/data/doe25-module"
import { LINUX247_MODULE } from "@/data/linux247-module"
import { HANDSON_MODULE } from "@/data/handson-module"
import { DOE25_TASK_FLASHCARDS } from "@/data/doe25-task-flashcards"
import { LINUX247_TASK_FLASHCARDS } from "@/data/linux247-task-flashcards"
import { HANDSON_TASK_FLASHCARDS } from "@/data/handson-task-flashcards"
// OMTENTA 2.0 - Nytt innehåll från Nod-filer
import { OMTENTA2_TOPICS, OMTENTA2_TOPIC_INFO, ALL_OMTENTA_2_QUESTIONS } from "@/data/omtenta-2.0-quiz"
import { ALL_OMTENTA_2_FLASHCARDS } from "@/data/omtenta-2.0-flashcards"

/* ============================================================================
   TYPES
   ============================================================================ */

interface StudyModule {
    id: string
    slug: string
    title: string
    description: string
    icon: string
    taskCount: number
    flashcardCount: number
    quizCount: number
    color: 'purple' | 'emerald' | 'amber'
    progress?: number
    tasks: { id: string; title: string; flashcardCount: number }[]
}

/* ============================================================================
   MODULE DATA
   ============================================================================ */

const STUDY_MODULES: StudyModule[] = [
    {
        id: 'doe25-tenta',
        slug: 'doe25-tenta',
        title: 'DOE25 Tentaplugg',
        description: 'Komplett förberedelse för Linux-tentan 7 januari 2026',
        icon: '🎓',
        taskCount: DOE25_MODULE.tasks.length,
        flashcardCount: DOE25_MODULE.tasks.length * 30,
        quizCount: DOE25_MODULE.tasks.length * 20,
        color: 'purple',
        tasks: DOE25_TASK_FLASHCARDS.map(t => ({
            id: t.taskId,
            title: t.taskTitle,
            flashcardCount: t.flashcards.length
        }))
    },
    {
        id: 'linux-247',
        slug: 'linux-247',
        title: 'Linux 24/7',
        description: 'Komplett Linux för DevOps - från grunden till produktion',
        icon: '🐧',
        taskCount: LINUX247_MODULE.tasks.length,
        flashcardCount: LINUX247_MODULE.tasks.length * 30,
        quizCount: LINUX247_MODULE.tasks.length * 20,
        color: 'emerald',
        tasks: LINUX247_TASK_FLASHCARDS.map(t => ({
            id: t.taskId,
            title: t.taskTitle,
            flashcardCount: t.flashcards.length
        }))
    },
    {
        id: 'hands-on-lab',
        slug: 'hands-on-lab',
        title: 'Hands-On Lab',
        description: 'Praktiska labbar - filsystem, SSH, Docker, LVM och mer',
        icon: '🔬',
        taskCount: HANDSON_MODULE.tasks.length,
        flashcardCount: HANDSON_MODULE.tasks.length * 30,
        quizCount: HANDSON_MODULE.tasks.length * 20,
        color: 'purple',
        tasks: HANDSON_TASK_FLASHCARDS.map(t => ({
            id: t.taskId,
            title: t.taskTitle,
            flashcardCount: t.flashcards.length
        }))
    },
    {
        id: 'omtenta-2',
        slug: 'omtenta-2',
        title: 'Omtenta 2.0',
        description: '800+ frågor & 500 flashcards från 10 Nod-moduler',
        icon: '🎯',
        taskCount: 10,
        flashcardCount: ALL_OMTENTA_2_FLASHCARDS.length,
        quizCount: ALL_OMTENTA_2_QUESTIONS.length,
        color: 'emerald',
        tasks: OMTENTA2_TOPICS.map(topic => ({
            id: topic,
            title: OMTENTA2_TOPIC_INFO[topic].name,
            flashcardCount: ALL_OMTENTA_2_FLASHCARDS.filter(f => f.topic === topic).length
        }))
    }
]

/* ============================================================================
   STUDYROOM PAGE
   ============================================================================ */

export default function StudyPage() {
    const router = useRouter()
    const [selectedModule, setSelectedModule] = useState<string | null>(null)
    const [selectedTasks, setSelectedTasks] = useState<string[]>([])
    const [showTaskSelector, setShowTaskSelector] = useState(true)
    const [studyMode, setStudyMode] = useState<'flashcards' | 'quiz' | null>(null)
    const [shuffleMode, setShuffleMode] = useState(false)
    const [difficulty, setDifficulty] = useState<'all' | 'beginner' | 'intermediate' | 'advanced'>('all')
    const [questionCount, setQuestionCount] = useState<number>(20)
    const [progress, setProgress] = useState<Record<string, number>>({})

    // Tenta-simulator settings
    const [tentaTime, setTentaTime] = useState<number>(90)
    const [tentaCount, setTentaCount] = useState<number>(200)
    const [tentaGradingMode, setTentaGradingMode] = useState<'live' | 'end'>('live')
    const [tentaDifficulty, setTentaDifficulty] = useState<'G' | 'VG' | 'both'>('both')
    const [tentaSource, setTentaSource] = useState<'handson' | 'linux' | 'linux-tenta' | 'omtenta-2'>('omtenta-2')
    const [omtenta2SelectedNodes, setOmtenta2SelectedNodes] = useState<string[]>(OMTENTA2_TOPICS)
    const [showNodeSelector, setShowNodeSelector] = useState(false)

    // Get current module
    const currentModule = useMemo(() =>
        STUDY_MODULES.find(m => m.slug === selectedModule),
        [selectedModule]
    )

    // Calculate selected flashcard count
    const selectedFlashcardCount = useMemo(() => {
        if (!currentModule || selectedTasks.length === 0) return 0
        return currentModule.tasks
            .filter(t => selectedTasks.includes(t.id))
            .reduce((sum, t) => sum + t.flashcardCount, 0)
    }, [currentModule, selectedTasks])

    useEffect(() => {
        const doe25Progress = localStorage.getItem('doe25-progress')
        const linux247Progress = localStorage.getItem('linux247-progress')

        setProgress({
            'doe25-tenta': doe25Progress ? JSON.parse(doe25Progress).length : 0,
            'linux-247': linux247Progress ? JSON.parse(linux247Progress).length : 0
        })
    }, [])

    const totalFlashcards = STUDY_MODULES.reduce((acc, m) => acc + m.flashcardCount, 0)
    const totalQuiz = STUDY_MODULES.reduce((acc, m) => acc + m.quizCount, 0)

    const handleModuleSelect = (moduleSlug: string) => {
        setSelectedModule(moduleSlug)
        setStudyMode(null)
        setSelectedTasks([]) // Reset task selection
        setShowTaskSelector(false)
    }

    const handleToggleTask = (taskId: string) => {
        setSelectedTasks(prev =>
            prev.includes(taskId)
                ? prev.filter(id => id !== taskId)
                : [...prev, taskId]
        )
    }

    const handleSelectAllTasks = () => {
        if (currentModule) {
            setSelectedTasks(currentModule.tasks.map(t => t.id))
        }
    }

    const handleDeselectAllTasks = () => {
        setSelectedTasks([])
    }

    const handleStartStudy = () => {
        if (selectedModule && studyMode && selectedTasks.length > 0) {
            const tasksParam = selectedTasks.join(',')
            const shuffleParam = shuffleMode ? '&shuffle=true' : ''
            const difficultyParam = difficulty !== 'all' ? `&difficulty=${difficulty}` : ''
            const countParam = studyMode === 'quiz' ? `&count=${questionCount}` : ''
            router.push(`/study/${selectedModule}/${studyMode}?tasks=${tasksParam}${shuffleParam}${difficultyParam}${countParam}`)
        }
    }

    return (
        <div className="min-h-screen bg-[#05050a]">
            {/* Background effects */}
            <div className="fixed inset-0 pointer-events-none">
                <div className="absolute top-0 left-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-[120px]" />
                <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-emerald-500/10 rounded-full blur-[120px]" />
                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-blue-500/5 rounded-full blur-[150px]" />
            </div>

            <div className="relative max-w-6xl mx-auto px-4 py-12">
                {/* Header */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="text-center mb-12"
                >
                    <motion.div
                        className="inline-flex items-center gap-3 mb-6"
                        animate={{
                            boxShadow: [
                                "0 0 20px rgba(168, 85, 247, 0.3)",
                                "0 0 40px rgba(168, 85, 247, 0.5)",
                                "0 0 20px rgba(168, 85, 247, 0.3)"
                            ]
                        }}
                        transition={{ duration: 2, repeat: Infinity }}
                    >
                        <div className={cn(
                            "w-16 h-16 rounded-2xl flex items-center justify-center text-3xl",
                            "bg-gradient-to-br from-purple-500/20 to-blue-500/20",
                            "border border-purple-500/30"
                        )}>
                            📚
                        </div>
                    </motion.div>

                    <h1 className="text-4xl md:text-5xl font-black text-white mb-4">
                        Studyroom
                    </h1>
                    <p className="text-lg text-zinc-400 max-w-2xl mx-auto">
                        Förstärk dina DevOps-kunskaper med flashcards och quiz
                    </p>
                </motion.div>

                {/* Tenta-Simulator Banner - Glassmorphism Design */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.15 }}
                    className="mb-12"
                >
                    {/* Hero Header */}
                    <div className="text-center mb-6">
                        <motion.div
                            className="inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-gradient-to-br from-purple-500/30 to-pink-500/30 backdrop-blur-xl border border-purple-500/20 mb-4 relative overflow-hidden"
                            whileHover={{ scale: 1.05, rotate: 5 }}
                            transition={{ type: "spring", stiffness: 300 }}
                        >
                            <motion.div
                                className="absolute inset-0 bg-gradient-to-br from-purple-500/20 to-pink-500/20"
                                animate={{ scale: [1, 1.2, 1], opacity: [0.5, 0.8, 0.5] }}
                                transition={{ duration: 3, repeat: Infinity }}
                            />
                            <span className="text-4xl relative z-10">🎯</span>
                        </motion.div>
                        <h3 className="text-3xl font-bold bg-gradient-to-r from-white via-purple-200 to-pink-200 bg-clip-text text-transparent mb-2">
                            Tenta-Simulator
                        </h3>
                        <p className="text-zinc-400">
                            Välj <span className="text-purple-400 font-semibold">DOE25</span> för tentafokus, <span className="text-emerald-400 font-semibold">Hands-On</span> för praktik, eller <span className="text-orange-400 font-semibold">Linux Kommandon 💻</span>
                        </p>
                    </div>

                    {/* Main Settings Card */}
                    <div className="relative bg-gradient-to-br from-zinc-900/80 via-zinc-900/50 to-zinc-900/80 backdrop-blur-xl border border-zinc-800/50 rounded-3xl p-6 overflow-hidden">
                        {/* Subtle glow */}
                        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl pointer-events-none" />

                        <div className="relative z-10">
                            {/* Settings grid - 3 columns */}
                            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                                {/* Time selection */}
                                <div className="bg-zinc-800/30 rounded-2xl p-4 border border-zinc-700/30">
                                    <div className="flex items-center gap-2 mb-3">
                                        <Clock className="w-4 h-4 text-purple-400" />
                                        <span className="text-sm font-semibold text-white">Tid</span>
                                    </div>
                                    <div className="grid grid-cols-4 gap-1.5">
                                        {[60, 75, 90, 120].map(mins => (
                                            <motion.button
                                                key={mins}
                                                onClick={() => setTentaTime(mins)}
                                                whileHover={{ scale: 1.02 }}
                                                whileTap={{ scale: 0.98 }}
                                                className={cn(
                                                    "py-2 rounded-lg text-xs font-semibold transition-all",
                                                    tentaTime === mins
                                                        ? "bg-gradient-to-br from-purple-500/40 to-pink-500/40 border border-purple-400/50 text-purple-200"
                                                        : "bg-zinc-800/50 border border-zinc-700/50 text-zinc-400 hover:border-zinc-600"
                                                )}
                                            >
                                                {mins} min
                                            </motion.button>
                                        ))}
                                    </div>
                                </div>

                                {/* Question count */}
                                <div className="bg-zinc-800/30 rounded-2xl p-4 border border-zinc-700/30">
                                    <div className="flex items-center gap-2 mb-3">
                                        <Brain className="w-4 h-4 text-blue-400" />
                                        <span className="text-sm font-semibold text-white">Antal frågor</span>
                                    </div>
                                    <div className="grid grid-cols-4 gap-1.5">
                                        {[100, 200, 300, 'Alla'].map(count => (
                                            <motion.button
                                                key={count}
                                                onClick={() => setTentaCount(count === 'Alla' ? 999 : count as number)}
                                                whileHover={{ scale: 1.02 }}
                                                whileTap={{ scale: 0.98 }}
                                                className={cn(
                                                    "py-2 rounded-lg text-xs font-semibold transition-all",
                                                    tentaCount === (count === 'Alla' ? 999 : count)
                                                        ? "bg-gradient-to-br from-blue-500/40 to-cyan-500/40 border border-blue-400/50 text-blue-200"
                                                        : "bg-zinc-800/50 border border-zinc-700/50 text-zinc-400 hover:border-zinc-600"
                                                )}
                                            >
                                                {count}
                                            </motion.button>
                                        ))}
                                    </div>
                                </div>

                                {/* Grading mode */}
                                <div className="bg-zinc-800/30 rounded-2xl p-4 border border-zinc-700/30">
                                    <div className="flex items-center gap-2 mb-3">
                                        <CheckSquare className="w-4 h-4 text-emerald-400" />
                                        <span className="text-sm font-semibold text-white">Rättning</span>
                                    </div>
                                    <div className="space-y-1.5">
                                        <motion.button
                                            onClick={() => setTentaGradingMode('live')}
                                            whileHover={{ scale: 1.01 }}
                                            whileTap={{ scale: 0.99 }}
                                            className={cn(
                                                "w-full py-2 px-3 rounded-lg text-xs font-semibold transition-all flex items-center gap-2",
                                                tentaGradingMode === 'live'
                                                    ? "bg-gradient-to-br from-emerald-500/40 to-teal-500/40 border border-emerald-400/50 text-emerald-200"
                                                    : "bg-zinc-800/50 border border-zinc-700/50 text-zinc-400 hover:border-zinc-600"
                                            )}
                                        >
                                            <Zap className="w-3 h-3" />
                                            Live-rättning
                                        </motion.button>
                                        <motion.button
                                            onClick={() => setTentaGradingMode('end')}
                                            whileHover={{ scale: 1.01 }}
                                            whileTap={{ scale: 0.99 }}
                                            className={cn(
                                                "w-full py-2 px-3 rounded-lg text-xs font-semibold transition-all flex items-center gap-2",
                                                tentaGradingMode === 'end'
                                                    ? "bg-gradient-to-br from-emerald-500/40 to-teal-500/40 border border-emerald-400/50 text-emerald-200"
                                                    : "bg-zinc-800/50 border border-zinc-700/50 text-zinc-400 hover:border-zinc-600"
                                            )}
                                        >
                                            <Clock className="w-3 h-3" />
                                            Rättning efteråt
                                        </motion.button>
                                    </div>
                                </div>
                            </div>

                            {/* G/VG Difficulty Selection */}
                            <div className="bg-zinc-800/30 rounded-2xl p-4 border border-zinc-700/30 mb-4">
                                <div className="flex items-center gap-2 mb-3">
                                    <Award className="w-4 h-4 text-yellow-400" />
                                    <span className="text-sm font-semibold text-white">Betygsnivå</span>
                                </div>
                                <div className="grid grid-cols-3 gap-2">
                                    <motion.button
                                        onClick={() => setTentaDifficulty('G')}
                                        whileHover={{ scale: 1.02 }}
                                        whileTap={{ scale: 0.98 }}
                                        className={cn(
                                            "py-3 rounded-xl transition-all flex flex-col items-center gap-1",
                                            tentaDifficulty === 'G'
                                                ? "bg-gradient-to-br from-green-500/40 to-emerald-500/40 border border-green-400/50 text-green-200"
                                                : "bg-zinc-800/50 border border-zinc-700/50 text-zinc-400 hover:border-zinc-600"
                                        )}
                                    >
                                        <span className="text-xl font-bold">G</span>
                                        <span className="text-[10px] opacity-70">Godkänt</span>
                                    </motion.button>
                                    <motion.button
                                        onClick={() => setTentaDifficulty('VG')}
                                        whileHover={{ scale: 1.02 }}
                                        whileTap={{ scale: 0.98 }}
                                        className={cn(
                                            "py-3 rounded-xl transition-all flex flex-col items-center gap-1",
                                            tentaDifficulty === 'VG'
                                                ? "bg-gradient-to-br from-purple-500/40 to-violet-500/40 border border-purple-400/50 text-purple-200"
                                                : "bg-zinc-800/50 border border-zinc-700/50 text-zinc-400 hover:border-zinc-600"
                                        )}
                                    >
                                        <span className="text-xl font-bold">VG</span>
                                        <span className="text-[10px] opacity-70">Väl Godkänt</span>
                                    </motion.button>
                                    <motion.button
                                        onClick={() => setTentaDifficulty('both')}
                                        whileHover={{ scale: 1.02 }}
                                        whileTap={{ scale: 0.98 }}
                                        className={cn(
                                            "py-3 rounded-xl transition-all flex flex-col items-center gap-1",
                                            tentaDifficulty === 'both'
                                                ? "bg-gradient-to-br from-yellow-500/40 via-orange-500/40 to-pink-500/40 border border-yellow-400/50 text-yellow-200"
                                                : "bg-zinc-800/50 border border-zinc-700/50 text-zinc-400 hover:border-zinc-600"
                                        )}
                                    >
                                        <span className="text-xl font-bold">G+VG</span>
                                        <span className="text-[10px] opacity-70">Mixad</span>
                                    </motion.button>
                                </div>
                            </div>

                            {/* Question Source Selection */}
                            <div className="bg-zinc-800/30 rounded-2xl p-4 border border-zinc-700/30 mb-4">
                                <div className="flex items-center gap-2 mb-3">
                                    <BookOpen className="w-4 h-4 text-cyan-400" />
                                    <span className="text-sm font-semibold text-white">Frågekälla</span>
                                </div>
                                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                                    <motion.button
                                        onClick={() => setTentaSource('omtenta-2')}
                                        whileHover={{ scale: 1.02 }}
                                        whileTap={{ scale: 0.98 }}
                                        className={cn(
                                            "py-3 rounded-xl transition-all flex flex-col items-center gap-1",
                                            tentaSource === 'omtenta-2'
                                                ? "bg-gradient-to-br from-teal-500/40 to-emerald-500/40 border border-teal-400/50 text-teal-200"
                                                : "bg-zinc-800/50 border border-zinc-700/50 text-zinc-400 hover:border-zinc-600"
                                        )}
                                    >
                                        <span className="text-lg">🎯</span>
                                        <span className="text-[10px] font-semibold">Omtenta 2.0</span>
                                        <span className="text-[9px] opacity-60">{ALL_OMTENTA_2_QUESTIONS.length} frågor</span>
                                    </motion.button>
                                    <motion.button
                                        onClick={() => setTentaSource('handson')}
                                        whileHover={{ scale: 1.02 }}
                                        whileTap={{ scale: 0.98 }}
                                        className={cn(
                                            "py-3 rounded-xl transition-all flex flex-col items-center gap-1",
                                            tentaSource === 'handson'
                                                ? "bg-gradient-to-br from-emerald-500/40 to-green-500/40 border border-emerald-400/50 text-emerald-200"
                                                : "bg-zinc-800/50 border border-zinc-700/50 text-zinc-400 hover:border-zinc-600"
                                        )}
                                    >
                                        <span className="text-lg">🔧</span>
                                        <span className="text-[10px] font-semibold">Hands-On</span>
                                        <span className="text-[9px] opacity-60">1051 frågor</span>
                                    </motion.button>
                                    <motion.button
                                        onClick={() => setTentaSource('linux')}
                                        whileHover={{ scale: 1.02 }}
                                        whileTap={{ scale: 0.98 }}
                                        className={cn(
                                            "py-3 rounded-xl transition-all flex flex-col items-center gap-1",
                                            tentaSource === 'linux'
                                                ? "bg-gradient-to-br from-orange-500/40 to-amber-500/40 border border-orange-400/50 text-orange-200"
                                                : "bg-zinc-800/50 border border-zinc-700/50 text-zinc-400 hover:border-zinc-600"
                                        )}
                                    >
                                        <span className="text-lg">💻</span>
                                        <span className="text-[10px] font-semibold">Linux Kommandon</span>
                                        <span className="text-[9px] opacity-60">350+ frågor</span>
                                    </motion.button>
                                    <motion.button
                                        onClick={() => setTentaSource('linux-tenta')}
                                        whileHover={{ scale: 1.02 }}
                                        whileTap={{ scale: 0.98 }}
                                        className={cn(
                                            "py-3 rounded-xl transition-all flex flex-col items-center gap-1",
                                            tentaSource === 'linux-tenta'
                                                ? "bg-gradient-to-br from-red-500/40 to-rose-500/40 border border-red-400/50 text-red-200"
                                                : "bg-zinc-800/50 border border-zinc-700/50 text-zinc-400 hover:border-zinc-600"
                                        )}
                                    >
                                        <span className="text-lg">📝</span>
                                        <span className="text-[10px] font-semibold">Linux Tentan</span>
                                        <span className="text-[9px] opacity-60">20 frågor</span>
                                    </motion.button>
                                </div>
                                <p className="text-[10px] text-zinc-500 mt-2 text-center">
                                    {tentaSource === 'omtenta-2' && "🎯 Rekommenderat - 10 Nod-moduler med quiz & scenarios"}
                                    {tentaSource === 'handson' && "🔧 Praktiska frågor"}
                                    {tentaSource === 'linux' && "🐧 Terminal & DevOps kommandon"}
                                    {tentaSource === 'linux-tenta' && "📝 Original tentafrågor"}
                                </p>
                            </div>

                            {/* Omtenta 2.0 Node Selection */}
                            {tentaSource === 'omtenta-2' && (
                                <div className="bg-zinc-800/30 rounded-2xl p-4 border border-zinc-700/30 mb-4">
                                    <div className="flex items-center justify-between mb-3">
                                        <div className="flex items-center gap-2">
                                            <Layers className="w-4 h-4 text-teal-400" />
                                            <span className="text-sm font-semibold text-white">Välj moduler</span>
                                            <span className="text-xs text-zinc-500">({omtenta2SelectedNodes.length}/{OMTENTA2_TOPICS.length})</span>
                                        </div>
                                        <button
                                            onClick={() => setShowNodeSelector(!showNodeSelector)}
                                            className="flex items-center gap-1 px-2 py-1 rounded-lg text-xs bg-zinc-800/50 border border-zinc-700/50 hover:bg-zinc-800 text-zinc-400"
                                        >
                                            {showNodeSelector ? 'Dölj' : 'Visa'}
                                            <ChevronDown className={cn("w-3 h-3 transition-transform", showNodeSelector && "rotate-180")} />
                                        </button>
                                    </div>

                                    <div className="flex gap-2 mb-2">
                                        <button onClick={() => setOmtenta2SelectedNodes(OMTENTA2_TOPICS)} className="px-3 py-1.5 rounded-lg text-xs bg-zinc-800/50 border border-zinc-700/50 hover:bg-zinc-800 text-zinc-400">Alla</button>
                                        <button onClick={() => setOmtenta2SelectedNodes([])} className="px-3 py-1.5 rounded-lg text-xs bg-zinc-800/50 border border-zinc-700/50 hover:bg-zinc-800 text-zinc-400">Inga</button>
                                        {omtenta2SelectedNodes.length > 0 && (
                                            <span className="ml-auto flex items-center gap-1 px-2 py-1 rounded-lg text-xs bg-teal-500/20 text-teal-300 border border-teal-500/30">
                                                <Brain className="w-3 h-3" />
                                                {ALL_OMTENTA_2_QUESTIONS.filter(q => omtenta2SelectedNodes.includes(q.topic)).length}
                                            </span>
                                        )}
                                    </div>

                                    <AnimatePresence>
                                        {showNodeSelector && (
                                            <motion.div initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: 'auto' }} exit={{ opacity: 0, height: 0 }} className="overflow-hidden">
                                                <div className="bg-zinc-900/50 rounded-xl p-2 max-h-48 overflow-y-auto">
                                                    <div className="grid grid-cols-2 gap-1">
                                                        {OMTENTA2_TOPICS.map((topic) => {
                                                            const info = OMTENTA2_TOPIC_INFO[topic]
                                                            const isSelected = omtenta2SelectedNodes.includes(topic)
                                                            const shortName = info.name.includes(':') ? info.name.split(':')[1].trim() : info.name
                                                            return (
                                                                <button
                                                                    key={topic}
                                                                    onClick={() => setOmtenta2SelectedNodes(prev => isSelected ? prev.filter(t => t !== topic) : [...prev, topic])}
                                                                    className={cn(
                                                                        "flex items-center gap-2 py-2 px-2 rounded-lg text-xs transition-all text-left",
                                                                        isSelected ? "bg-teal-500/20 text-teal-200 border border-teal-500/40" : "bg-zinc-800/30 text-zinc-400 hover:bg-zinc-800/50 border border-transparent"
                                                                    )}
                                                                >
                                                                    <div className={cn("w-4 h-4 rounded flex items-center justify-center shrink-0", isSelected ? "bg-teal-500" : "bg-zinc-700")}>
                                                                        {isSelected && <Check className="w-3 h-3 text-white" />}
                                                                    </div>
                                                                    <span className="truncate">{shortName}</span>
                                                                </button>
                                                            )
                                                        })}
                                                    </div>
                                                </div>
                                            </motion.div>
                                        )}
                                    </AnimatePresence>
                                    {omtenta2SelectedNodes.length === 0 && <p className="text-[10px] text-orange-400 mt-2 text-center">⚠️ Välj minst en modul</p>}
                                </div>
                            )}

                            {/* Start button */}
                            <Link href={`/study/tenta-simulator?time=${tentaTime}&count=${tentaCount}&grading=${tentaGradingMode}&difficulty=${tentaDifficulty}&source=${tentaSource}${tentaSource === 'omtenta-2' ? `&nodes=${omtenta2SelectedNodes.join(',')}` : ''}`}>
                                <motion.button
                                    whileHover={{ scale: 1.02, y: -2 }}
                                    whileTap={{ scale: 0.98 }}
                                    disabled={tentaSource === 'omtenta-2' && omtenta2SelectedNodes.length === 0}
                                    className={cn(
                                        "w-full py-4 rounded-2xl font-bold text-base relative overflow-hidden group",
                                        "bg-gradient-to-r from-purple-600 via-pink-600 to-purple-600 text-white",
                                        "shadow-xl shadow-purple-500/30 hover:shadow-purple-500/50 transition-all",
                                        "flex items-center justify-center gap-2",
                                        tentaSource === 'omtenta-2' && omtenta2SelectedNodes.length === 0 && "opacity-50 cursor-not-allowed"
                                    )}
                                >
                                    <motion.div
                                        className="absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent"
                                        animate={{ x: ['-200%', '200%'] }}
                                        transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
                                    />
                                    <Zap className="w-5 h-5 relative z-10" />
                                    <span className="relative z-10">Starta Tenta-Simulator</span>
                                    <ChevronRight className="w-5 h-5 relative z-10" />
                                </motion.button>
                            </Link>
                        </div>
                    </div>
                </motion.div>

                {/* Module Selection */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.2 }}
                    className="mb-8"
                >
                    {/* Flashy header */}
                    <div className="flex items-center justify-center gap-4 mb-8">
                        <div className="h-px flex-1 bg-gradient-to-r from-transparent via-purple-500/50 to-transparent" />
                        <div className="flex items-center gap-3">
                            <motion.span
                                className="text-4xl"
                                animate={{ rotate: [0, 10, -10, 0] }}
                                transition={{ duration: 2, repeat: Infinity }}
                            >
                                📚
                            </motion.span>
                            <div className="flex items-center gap-2">
                                <span className="px-3 py-1.5 rounded-lg bg-purple-500/20 border border-purple-500/30 text-purple-300 font-bold">
                                    Flashcards
                                </span>
                                <span className="text-zinc-500 font-bold">+</span>
                                <span className="px-3 py-1.5 rounded-lg bg-emerald-500/20 border border-emerald-500/30 text-emerald-300 font-bold">
                                    Quiz
                                </span>
                            </div>
                            <motion.span
                                className="text-4xl"
                                animate={{ rotate: [0, -10, 10, 0] }}
                                transition={{ duration: 2, repeat: Infinity, delay: 0.5 }}
                            >
                                🧠
                            </motion.span>
                        </div>
                        <div className="h-px flex-1 bg-gradient-to-r from-transparent via-emerald-500/50 to-transparent" />
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {STUDY_MODULES.map((module, index) => {
                            const isSelected = selectedModule === module.slug
                            const moduleProgress = progress[module.slug] || 0
                            const progressPercent = (moduleProgress / module.taskCount) * 100

                            return (
                                <motion.button
                                    key={module.id}
                                    initial={{ opacity: 0, x: -20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    transition={{ delay: 0.2 + index * 0.1 }}
                                    onClick={() => handleModuleSelect(module.slug)}
                                    className={cn(
                                        "relative text-left p-6 rounded-2xl transition-all duration-300",
                                        "border-2 group",
                                        isSelected
                                            ? module.color === 'purple'
                                                ? "bg-purple-500/10 border-purple-500/50"
                                                : module.color === 'amber'
                                                    ? "bg-amber-500/10 border-amber-500/50"
                                                    : "bg-emerald-500/10 border-emerald-500/50"
                                            : "bg-zinc-900/50 border-zinc-800/50 hover:border-zinc-700"
                                    )}
                                >
                                    {isSelected && (
                                        <motion.div
                                            layoutId="module-selection"
                                            className={cn(
                                                "absolute inset-0 rounded-2xl -z-10",
                                                module.color === 'purple'
                                                    ? "bg-gradient-to-br from-purple-500/20 to-transparent"
                                                    : module.color === 'amber'
                                                        ? "bg-gradient-to-br from-amber-500/20 to-transparent"
                                                        : "bg-gradient-to-br from-emerald-500/20 to-transparent"
                                            )}
                                        />
                                    )}

                                    <div className="flex items-start gap-4">
                                        <div className={cn(
                                            "w-14 h-14 rounded-xl flex items-center justify-center text-2xl shrink-0",
                                            "transition-all duration-300",
                                            isSelected
                                                ? module.color === 'purple'
                                                    ? "bg-purple-500/30 shadow-lg shadow-purple-500/20"
                                                    : module.color === 'amber'
                                                        ? "bg-amber-500/30 shadow-lg shadow-amber-500/20"
                                                        : "bg-emerald-500/30 shadow-lg shadow-emerald-500/20"
                                                : "bg-zinc-800"
                                        )}>
                                            {module.icon}
                                        </div>

                                        <div className="flex-1 min-w-0">
                                            <div className="flex items-center gap-2 mb-1">
                                                <h3 className={cn(
                                                    "text-xl font-bold transition-colors",
                                                    isSelected
                                                        ? module.color === 'purple' ? "text-purple-300" : module.color === 'amber' ? "text-amber-300" : "text-emerald-300"
                                                        : "text-white group-hover:text-zinc-200"
                                                )}>
                                                    {module.title}
                                                </h3>
                                                {isSelected && (
                                                    <CheckSquare className={cn(
                                                        "w-5 h-5",
                                                        module.color === 'purple' ? "text-purple-400" : module.color === 'amber' ? "text-amber-400" : "text-emerald-400"
                                                    )} />
                                                )}
                                            </div>

                                            <p className="text-sm text-zinc-400 mb-4">
                                                {module.description}
                                            </p>

                                            <div className="flex flex-wrap gap-4 text-sm">
                                                <span className="flex items-center gap-1.5 text-zinc-500">
                                                    <Layers className="w-4 h-4" />
                                                    {module.taskCount} tasks
                                                </span>
                                                <span className="flex items-center gap-1.5 text-zinc-500">
                                                    <BookOpen className="w-4 h-4" />
                                                    {module.flashcardCount} flashcards
                                                </span>
                                                <span className="flex items-center gap-1.5 text-zinc-500">
                                                    <Brain className="w-4 h-4" />
                                                    {module.quizCount} quiz
                                                </span>
                                            </div>

                                            {moduleProgress > 0 && (
                                                <div className="mt-4">
                                                    <div className="flex items-center justify-between text-xs mb-1">
                                                        <span className="text-zinc-500">Progress</span>
                                                        <span className={module.color === 'purple' ? "text-purple-400" : module.color === 'amber' ? "text-amber-400" : "text-emerald-400"}>
                                                            {moduleProgress}/{module.taskCount} tasks
                                                        </span>
                                                    </div>
                                                    <div className="h-1.5 bg-zinc-800 rounded-full overflow-hidden">
                                                        <motion.div
                                                            className={cn(
                                                                "h-full rounded-full",
                                                                module.color === 'purple'
                                                                    ? "bg-gradient-to-r from-purple-500 to-pink-500"
                                                                    : module.color === 'amber'
                                                                        ? "bg-gradient-to-r from-amber-500 to-orange-500"
                                                                        : "bg-gradient-to-r from-emerald-500 to-teal-500"
                                                            )}
                                                            initial={{ width: 0 }}
                                                            animate={{ width: `${progressPercent}%` }}
                                                            transition={{ duration: 0.5 }}
                                                        />
                                                    </div>
                                                </div>
                                            )}
                                        </div>

                                        <ChevronRight className={cn(
                                            "w-6 h-6 shrink-0 transition-all",
                                            isSelected
                                                ? module.color === 'purple' ? "text-purple-400" : module.color === 'amber' ? "text-amber-400" : "text-emerald-400"
                                                : "text-zinc-600 group-hover:text-zinc-400"
                                        )} />
                                    </div>
                                </motion.button>
                            )
                        })}
                    </div>
                </motion.div>

                {/* Task Selection */}
                <AnimatePresence>
                    {selectedModule && currentModule && (
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0, y: -20 }}
                            className="mb-8"
                        >
                            <div className="flex items-center justify-between mb-4">
                                <h2 className="text-xl font-bold text-white flex items-center gap-3">
                                    <Layers className="w-6 h-6 text-blue-400" />
                                    Välj tasks
                                    <span className="text-sm font-normal text-zinc-500">
                                        ({selectedTasks.length}/{currentModule.tasks.length} valda)
                                    </span>
                                </h2>
                                <button
                                    onClick={() => setShowTaskSelector(!showTaskSelector)}
                                    className={cn(
                                        "flex items-center gap-2 px-4 py-2 rounded-xl text-sm",
                                        "bg-zinc-800/50 border border-zinc-700/50",
                                        "hover:bg-zinc-800 transition-colors"
                                    )}
                                >
                                    {showTaskSelector ? 'Dölj' : 'Visa tasks'}
                                    <ChevronDown className={cn(
                                        "w-4 h-4 transition-transform",
                                        showTaskSelector && "rotate-180"
                                    )} />
                                </button>
                            </div>

                            {/* Quick select buttons */}
                            <div className="flex gap-3 mb-4">
                                <button
                                    onClick={handleSelectAllTasks}
                                    className={cn(
                                        "px-4 py-2 rounded-xl text-sm font-medium",
                                        "bg-zinc-800/50 border border-zinc-700/50",
                                        "hover:bg-zinc-800 hover:border-zinc-600 transition-colors",
                                        "text-zinc-300"
                                    )}
                                >
                                    Välj alla
                                </button>
                                <button
                                    onClick={handleDeselectAllTasks}
                                    className={cn(
                                        "px-4 py-2 rounded-xl text-sm font-medium",
                                        "bg-zinc-800/50 border border-zinc-700/50",
                                        "hover:bg-zinc-800 hover:border-zinc-600 transition-colors",
                                        "text-zinc-300"
                                    )}
                                >
                                    Avmarkera alla
                                </button>
                                {selectedTasks.length > 0 && (
                                    <span className={cn(
                                        "ml-auto flex items-center gap-2 px-4 py-2 rounded-xl text-sm",
                                        currentModule.color === 'purple'
                                            ? "bg-purple-500/20 text-purple-300 border border-purple-500/30"
                                            : "bg-emerald-500/20 text-emerald-300 border border-emerald-500/30"
                                    )}>
                                        <BookOpen className="w-4 h-4" />
                                        {selectedFlashcardCount} flashcards
                                    </span>
                                )}
                            </div>

                            {/* Task list */}
                            <AnimatePresence>
                                {showTaskSelector && (
                                    <motion.div
                                        initial={{ opacity: 0, height: 0 }}
                                        animate={{ opacity: 1, height: 'auto' }}
                                        exit={{ opacity: 0, height: 0 }}
                                        className="overflow-hidden"
                                    >
                                        <div className={cn(
                                            "rounded-2xl border p-4 max-h-80 overflow-y-auto",
                                            "bg-zinc-900/50 border-zinc-800/50"
                                        )}>
                                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                                {currentModule.tasks.map((task, index) => {
                                                    const isTaskSelected = selectedTasks.includes(task.id)
                                                    return (
                                                        <motion.button
                                                            key={task.id}
                                                            initial={{ opacity: 0, x: -10 }}
                                                            animate={{ opacity: 1, x: 0 }}
                                                            transition={{ delay: index * 0.02 }}
                                                            onClick={() => handleToggleTask(task.id)}
                                                            className={cn(
                                                                "flex items-center gap-3 p-3 rounded-xl text-left transition-all",
                                                                "border",
                                                                isTaskSelected
                                                                    ? currentModule.color === 'purple'
                                                                        ? "bg-purple-500/10 border-purple-500/40"
                                                                        : currentModule.color === 'amber'
                                                                            ? "bg-amber-500/10 border-amber-500/40"
                                                                            : "bg-emerald-500/10 border-emerald-500/40"
                                                                    : "bg-zinc-800/30 border-zinc-700/30 hover:border-zinc-600"
                                                            )}
                                                        >
                                                            <div className={cn(
                                                                "w-5 h-5 rounded flex items-center justify-center shrink-0",
                                                                isTaskSelected
                                                                    ? currentModule.color === 'purple'
                                                                        ? "bg-purple-500"
                                                                        : currentModule.color === 'amber'
                                                                            ? "bg-amber-500"
                                                                            : "bg-emerald-500"
                                                                    : "bg-zinc-700"
                                                            )}>
                                                                {isTaskSelected && <Check className="w-3 h-3 text-white" />}
                                                            </div>
                                                            <div className="flex-1 min-w-0">
                                                                <p className={cn(
                                                                    "text-sm font-medium truncate",
                                                                    isTaskSelected ? "text-white" : "text-zinc-300"
                                                                )}>
                                                                    {task.title}
                                                                </p>
                                                                <p className="text-xs text-zinc-500">
                                                                    {task.flashcardCount} flashcards
                                                                </p>
                                                            </div>
                                                        </motion.button>
                                                    )
                                                })}
                                            </div>
                                        </div>
                                    </motion.div>
                                )}
                            </AnimatePresence>
                        </motion.div>
                    )}
                </AnimatePresence>

                {/* Study Mode Selection */}
                <AnimatePresence>
                    {selectedModule && selectedTasks.length > 0 && (
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0, y: -20 }}
                            className="mb-8"
                        >
                            <h2 className="text-xl font-bold text-white mb-6 flex items-center gap-3">
                                <Sparkles className="w-6 h-6 text-amber-400" />
                                Välj studieläge
                            </h2>

                            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                                <motion.button
                                    initial={{ opacity: 0, x: -20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    onClick={() => setStudyMode('flashcards')}
                                    className={cn(
                                        "relative p-6 rounded-2xl text-left transition-all duration-300",
                                        "border-2 group",
                                        studyMode === 'flashcards'
                                            ? "bg-purple-500/10 border-purple-500/50"
                                            : "bg-zinc-900/50 border-zinc-800/50 hover:border-purple-500/30"
                                    )}
                                >
                                    <div className="flex items-center gap-4 mb-4">
                                        <div className={cn(
                                            "w-12 h-12 rounded-xl flex items-center justify-center",
                                            "transition-all duration-300",
                                            studyMode === 'flashcards'
                                                ? "bg-purple-500/30 shadow-lg shadow-purple-500/20"
                                                : "bg-purple-500/10"
                                        )}>
                                            <BookOpen className={cn(
                                                "w-6 h-6",
                                                studyMode === 'flashcards' ? "text-purple-300" : "text-purple-400"
                                            )} />
                                        </div>
                                        <div>
                                            <h3 className={cn(
                                                "text-lg font-bold transition-colors",
                                                studyMode === 'flashcards' ? "text-purple-300" : "text-white"
                                            )}>
                                                Flashcards
                                            </h3>
                                            <p className="text-sm text-zinc-500">Memorera koncept och kommandon</p>
                                        </div>
                                    </div>

                                    <ul className="space-y-2 text-sm text-zinc-400">
                                        <li className="flex items-center gap-2">
                                            <Zap className="w-4 h-4 text-amber-400" />
                                            Snabb repetition
                                        </li>
                                        <li className="flex items-center gap-2">
                                            <Clock className="w-4 h-4 text-blue-400" />
                                            Perfekt före tentan
                                        </li>
                                    </ul>
                                </motion.button>

                                <motion.button
                                    initial={{ opacity: 0, x: 20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    onClick={() => setStudyMode('quiz')}
                                    className={cn(
                                        "relative p-6 rounded-2xl text-left transition-all duration-300",
                                        "border-2 group",
                                        studyMode === 'quiz'
                                            ? "bg-emerald-500/10 border-emerald-500/50"
                                            : "bg-zinc-900/50 border-zinc-800/50 hover:border-emerald-500/30"
                                    )}
                                >
                                    <div className="flex items-center gap-4 mb-4">
                                        <div className={cn(
                                            "w-12 h-12 rounded-xl flex items-center justify-center",
                                            "transition-all duration-300",
                                            studyMode === 'quiz'
                                                ? "bg-emerald-500/30 shadow-lg shadow-emerald-500/20"
                                                : "bg-emerald-500/10"
                                        )}>
                                            <Brain className={cn(
                                                "w-6 h-6",
                                                studyMode === 'quiz' ? "text-emerald-300" : "text-emerald-400"
                                            )} />
                                        </div>
                                        <div>
                                            <h3 className={cn(
                                                "text-lg font-bold transition-colors",
                                                studyMode === 'quiz' ? "text-emerald-300" : "text-white"
                                            )}>
                                                Quiz
                                            </h3>
                                            <p className="text-sm text-zinc-500">Testa dina kunskaper</p>
                                        </div>
                                    </div>

                                    <ul className="space-y-2 text-sm text-zinc-400">
                                        <li className="flex items-center gap-2">
                                            <Trophy className="w-4 h-4 text-amber-400" />
                                            Samla XP poäng
                                        </li>
                                        <li className="flex items-center gap-2">
                                            <GraduationCap className="w-4 h-4 text-purple-400" />
                                            Tentasimulering
                                        </li>
                                    </ul>
                                </motion.button>
                            </div>
                        </motion.div>
                    )}
                </AnimatePresence>

                {/* Settings Section */}
                <AnimatePresence>
                    {selectedModule && studyMode && selectedTasks.length > 0 && (
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0, y: -20 }}
                            className="mb-8 space-y-4"
                        >
                            <h2 className="text-xl font-bold text-white mb-6 flex items-center gap-3">
                                <Shuffle className="w-6 h-6 text-pink-400" />
                                Inställningar
                            </h2>

                            {/* Difficulty Selection - Only for Quiz */}
                            {studyMode === 'quiz' && (
                                <div className="p-5 rounded-2xl bg-zinc-900/50 border-2 border-zinc-800/50">
                                    <h3 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
                                        🎯 Svårighetsgrad
                                    </h3>
                                    <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                                        {[
                                            { value: 'all', label: 'Alla', emoji: '📚', color: 'purple' },
                                            { value: 'beginner', label: 'Nybörjare', emoji: '🌱', color: 'emerald' },
                                            { value: 'intermediate', label: 'Medel', emoji: '⚡', color: 'amber' },
                                            { value: 'advanced', label: 'Avancerad', emoji: '🔥', color: 'red' }
                                        ].map((opt) => (
                                            <button
                                                key={opt.value}
                                                onClick={() => setDifficulty(opt.value as typeof difficulty)}
                                                className={cn(
                                                    "p-3 rounded-xl text-center transition-all duration-200",
                                                    "border-2",
                                                    difficulty === opt.value
                                                        ? opt.color === 'purple' ? "bg-purple-500/20 border-purple-500/50 text-purple-300"
                                                            : opt.color === 'emerald' ? "bg-emerald-500/20 border-emerald-500/50 text-emerald-300"
                                                                : opt.color === 'amber' ? "bg-amber-500/20 border-amber-500/50 text-amber-300"
                                                                    : "bg-red-500/20 border-red-500/50 text-red-300"
                                                        : "bg-zinc-800/50 border-zinc-700/50 text-zinc-400 hover:border-zinc-600"
                                                )}
                                            >
                                                <span className="text-xl block mb-1">{opt.emoji}</span>
                                                <span className="text-sm font-medium">{opt.label}</span>
                                            </button>
                                        ))}
                                    </div>
                                </div>
                            )}

                            {/* Question Count - Only for Quiz */}
                            {studyMode === 'quiz' && (
                                <div className="p-5 rounded-2xl bg-zinc-900/50 border-2 border-zinc-800/50">
                                    <h3 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
                                        🔢 Antal frågor
                                    </h3>
                                    <div className="grid grid-cols-4 md:grid-cols-6 gap-2">
                                        {[10, 20, 30, 50, 75, 100].map((count) => (
                                            <button
                                                key={count}
                                                onClick={() => setQuestionCount(count)}
                                                className={cn(
                                                    "py-2 px-3 rounded-lg text-center transition-all duration-200",
                                                    "border-2 font-medium",
                                                    questionCount === count
                                                        ? "bg-blue-500/20 border-blue-500/50 text-blue-300"
                                                        : "bg-zinc-800/50 border-zinc-700/50 text-zinc-400 hover:border-zinc-600"
                                                )}
                                            >
                                                {count}
                                            </button>
                                        ))}
                                    </div>
                                </div>
                            )}

                            {/* Shuffle Toggle */}
                            <button
                                onClick={() => setShuffleMode(!shuffleMode)}
                                className={cn(
                                    "w-full p-5 rounded-2xl text-left transition-all duration-300",
                                    "border-2 group",
                                    shuffleMode
                                        ? "bg-gradient-to-r from-pink-500/20 to-orange-500/20 border-pink-500/50"
                                        : "bg-zinc-900/50 border-zinc-800/50 hover:border-pink-500/30"
                                )}
                            >
                                <div className="flex items-center justify-between">
                                    <div className="flex items-center gap-4">
                                        <div className={cn(
                                            "w-12 h-12 rounded-xl flex items-center justify-center",
                                            "transition-all duration-300",
                                            shuffleMode
                                                ? "bg-pink-500/30 shadow-lg shadow-pink-500/20"
                                                : "bg-zinc-800"
                                        )}>
                                            <Shuffle className={cn(
                                                "w-6 h-6 transition-colors",
                                                shuffleMode ? "text-pink-300" : "text-zinc-400"
                                            )} />
                                        </div>
                                        <div>
                                            <h3 className={cn(
                                                "text-lg font-bold transition-colors",
                                                shuffleMode ? "text-pink-300" : "text-white"
                                            )}>
                                                🎲 Shuffle-läge
                                            </h3>
                                            <p className="text-sm text-zinc-400">
                                                Blanda frågor från alla valda tasks slumpmässigt
                                            </p>
                                        </div>
                                    </div>

                                    {/* Toggle Switch */}
                                    <div className={cn(
                                        "w-14 h-8 rounded-full p-1 transition-all duration-300",
                                        shuffleMode
                                            ? "bg-gradient-to-r from-pink-500 to-orange-500"
                                            : "bg-zinc-700"
                                    )}>
                                        <motion.div
                                            className="w-6 h-6 bg-white rounded-full shadow-md"
                                            animate={{ x: shuffleMode ? 24 : 0 }}
                                            transition={{ type: "spring", stiffness: 500, damping: 30 }}
                                        />
                                    </div>
                                </div>

                                {shuffleMode && (
                                    <motion.p
                                        initial={{ opacity: 0, height: 0 }}
                                        animate={{ opacity: 1, height: 'auto' }}
                                        className="mt-4 text-sm text-pink-300/80 pl-16"
                                    >
                                        ✨ Perfekt för att testa att du verkligen kan materialet oavsett ordning!
                                    </motion.p>
                                )}
                            </button>
                        </motion.div>
                    )}
                </AnimatePresence>

                {/* Start Button */}
                <AnimatePresence>
                    {selectedModule && studyMode && selectedTasks.length > 0 && (
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0, y: -20 }}
                            className="text-center"
                        >
                            <motion.button
                                onClick={handleStartStudy}
                                className={cn(
                                    "inline-flex items-center gap-3 px-8 py-4 rounded-2xl",
                                    "font-bold text-lg text-white",
                                    "transition-all duration-300",
                                    studyMode === 'flashcards'
                                        ? "bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 shadow-lg shadow-purple-500/25 hover:shadow-purple-500/40"
                                        : "bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 shadow-lg shadow-emerald-500/25 hover:shadow-emerald-500/40"
                                )}
                                whileHover={{ scale: 1.05 }}
                                whileTap={{ scale: 0.98 }}
                            >
                                {shuffleMode && <Shuffle className="w-5 h-5" />}
                                {!shuffleMode && <Sparkles className="w-5 h-5" />}
                                Starta {studyMode === 'flashcards' ? 'Flashcards' : 'Quiz'}
                                {shuffleMode && ' (Shuffle)'}
                                <ArrowRight className="w-5 h-5" />
                            </motion.button>

                            <p className="mt-4 text-sm text-zinc-500">
                                {selectedTasks.length} task{selectedTasks.length !== 1 ? 's' : ''} valda • {' '}
                                {studyMode === 'flashcards'
                                    ? `${selectedFlashcardCount} flashcards`
                                    : `~${Math.round(selectedFlashcardCount * 0.66)} quiz-frågor`
                                }
                                {shuffleMode && ' • 🎲 Shuffle aktivt'}
                            </p>
                        </motion.div>
                    )}
                </AnimatePresence>

                {/* Quick Links to Modules */}
                <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.4 }}
                    className="mt-16 pt-8 border-t border-zinc-800/50"
                >
                    <h3 className="text-sm font-medium text-zinc-500 mb-4">Eller gå direkt till modulerna:</h3>
                    <div className="flex flex-wrap gap-3">
                        <Link
                            href="/modules/doe25-tenta"
                            className={cn(
                                "flex items-center gap-2 px-4 py-2 rounded-lg",
                                "bg-zinc-900/50 border border-zinc-800/50",
                                "hover:border-purple-500/30 hover:bg-zinc-900",
                                "text-sm text-zinc-400 hover:text-purple-300",
                                "transition-all duration-200"
                            )}
                        >
                            🎓 DOE25 Tentaplugg
                            <ArrowRight className="w-4 h-4" />
                        </Link>
                        <Link
                            href="/modules/linux-247"
                            className={cn(
                                "flex items-center gap-2 px-4 py-2 rounded-lg",
                                "bg-zinc-900/50 border border-zinc-800/50",
                                "hover:border-emerald-500/30 hover:bg-zinc-900",
                                "text-sm text-zinc-400 hover:text-emerald-300",
                                "transition-all duration-200"
                            )}
                        >
                            🐧 Linux 24/7
                            <ArrowRight className="w-4 h-4" />
                        </Link>
                    </div>
                </motion.div>
            </div>
        </div>
    )
}
