"use client"

/**
 * Studyroom - Premium Cosmic Design
 * Flashcards & Quiz för DOE25 + Linux 24/7
 */

import * as React from "react"
import { useState, useEffect } from "react"
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
  ChevronRight
} from "lucide-react"

// Import module data
import { DOE25_MODULE } from "@/data/doe25-module"
import { LINUX247_MODULE } from "@/data/linux247-module"

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
  color: 'purple' | 'emerald'
  progress?: number
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
    color: 'purple'
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
    color: 'emerald'
  }
]

/* ============================================================================
   STUDYROOM PAGE
   ============================================================================ */

export default function StudyPage() {
  const router = useRouter()
  const [selectedModule, setSelectedModule] = useState<string | null>(null)
  const [studyMode, setStudyMode] = useState<'flashcards' | 'quiz' | null>(null)
  const [progress, setProgress] = useState<Record<string, number>>({})

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
  }

  const handleStartStudy = () => {
    if (selectedModule && studyMode) {
      router.push(`/study/${selectedModule}/${studyMode}`)
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

        {/* Stats Overview */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12"
        >
          {[
            { icon: <Layers className="w-5 h-5" />, label: "Moduler", value: STUDY_MODULES.length, color: "text-blue-400" },
            { icon: <BookOpen className="w-5 h-5" />, label: "Flashcards", value: totalFlashcards.toLocaleString(), color: "text-purple-400" },
            { icon: <Brain className="w-5 h-5" />, label: "Quiz-frågor", value: totalQuiz.toLocaleString(), color: "text-emerald-400" },
            { icon: <Trophy className="w-5 h-5" />, label: "XP möjligt", value: "5000+", color: "text-amber-400" }
          ].map((stat, i) => (
            <motion.div
              key={stat.label}
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: 0.1 + i * 0.05 }}
              className={cn(
                "rounded-xl p-4",
                "bg-zinc-900/50 border border-zinc-800/50",
                "backdrop-blur-xl"
              )}
            >
              <div className={cn("mb-2", stat.color)}>{stat.icon}</div>
              <div className="text-2xl font-bold text-white">{stat.value}</div>
              <div className="text-sm text-zinc-500">{stat.label}</div>
            </motion.div>
          ))}
        </motion.div>

        {/* Module Selection */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="mb-8"
        >
          <h2 className="text-xl font-bold text-white mb-6 flex items-center gap-3">
            <GraduationCap className="w-6 h-6 text-purple-400" />
            Välj modul
          </h2>

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
                            ? module.color === 'purple' ? "text-purple-300" : "text-emerald-300"
                            : "text-white group-hover:text-zinc-200"
                        )}>
                          {module.title}
                        </h3>
                        {isSelected && (
                          <CheckSquare className={cn(
                            "w-5 h-5",
                            module.color === 'purple' ? "text-purple-400" : "text-emerald-400"
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
                            <span className={module.color === 'purple' ? "text-purple-400" : "text-emerald-400"}>
                              {moduleProgress}/{module.taskCount} tasks
                            </span>
                          </div>
                          <div className="h-1.5 bg-zinc-800 rounded-full overflow-hidden">
                            <motion.div
                              className={cn(
                                "h-full rounded-full",
                                module.color === 'purple'
                                  ? "bg-gradient-to-r from-purple-500 to-pink-500"
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
                        ? module.color === 'purple' ? "text-purple-400" : "text-emerald-400"
                        : "text-zinc-600 group-hover:text-zinc-400"
                    )} />
                  </div>
                </motion.button>
              )
            })}
          </div>
        </motion.div>

        {/* Study Mode Selection */}
        <AnimatePresence>
          {selectedModule && (
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

        {/* Start Button */}
        <AnimatePresence>
          {selectedModule && studyMode && (
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
                <Sparkles className="w-5 h-5" />
                Starta {studyMode === 'flashcards' ? 'Flashcards' : 'Quiz'}
                <ArrowRight className="w-5 h-5" />
              </motion.button>

              <p className="mt-4 text-sm text-zinc-500">
                {STUDY_MODULES.find(m => m.slug === selectedModule)?.title} • {' '}
                {studyMode === 'flashcards' 
                  ? `${STUDY_MODULES.find(m => m.slug === selectedModule)?.flashcardCount} kort`
                  : `${STUDY_MODULES.find(m => m.slug === selectedModule)?.quizCount} frågor`
                }
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
