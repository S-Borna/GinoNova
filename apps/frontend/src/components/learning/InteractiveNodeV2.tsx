"use client"

/**
 * ============================================================================
 * INTERACTIVE NODE V2 - Full node rendering with all 5 sections
 * ============================================================================
 * 
 * Renders a complete learning node with:
 * 1. Intro - Learning objectives
 * 2. Concepts - Structured explanations
 * 3. Practice - Simulated terminal
 * 4. Quiz - Flashcards + multiple choice
 * 5. Challenge - Practical application
 * 
 * Progress is tracked per section with XP distributed across activities.
 */

import { useState, useCallback } from "react"
import { cn } from "@saas/ui"
import { 
    Target, 
    BookOpen, 
    Terminal, 
    HelpCircle, 
    Trophy,
    CheckCircle2,
    ChevronRight,
    Clock
} from "lucide-react"
import { IntroBlock } from "./blocks/IntroBlock"
import { ConceptBlock } from "./blocks/ConceptBlock"
import { SimulatedTerminal } from "./blocks/SimulatedTerminal"
import { QuizBlock } from "./blocks/QuizBlock"
import { ChallengeBlock } from "./blocks/ChallengeBlock"

/* ============================================================================
   TYPES
   ============================================================================ */

interface NodeIntro {
    headline: string
    hook: string
    learning_objectives: string[]
    prerequisites?: string[]
    estimated_time?: string
}

interface NodeConcept {
    title: string
    explanation: string
    diagram?: string
    pro_tip?: string
    common_mistake?: string
}

interface PracticeStep {
    step: number
    title: string
    instruction: string
    command: string
    expected_output: string
    explanation: string
}

interface NodePractice {
    description: string
    exercises: PracticeStep[]
}

interface Flashcard {
    term: string
    definition: string
}

interface MultipleChoiceQuestion {
    question: string
    options: string[]
    correct_answer: number
    explanation: string
}

interface NodeQuiz {
    passing_score: number
    flashcards?: Flashcard[]
    multiple_choice: MultipleChoiceQuestion[]
}

interface NodeChallenge {
    title: string
    scenario: string
    requirements: string[]
    hints?: string[]
    solution?: string
    xp_bonus?: number
}

interface EstimatedTimePerSection {
    intro: number
    concepts: number
    practice: number
    quiz: number
    challenge: number
}

interface InteractiveNodeData {
    node_id: number
    title: string
    slug: string
    description: string
    difficulty: string
    estimated_minutes: number
    xp_reward: number
    estimated_time_per_section?: EstimatedTimePerSection
    intro: NodeIntro
    concepts: NodeConcept[]
    practice: NodePractice
    quiz: NodeQuiz
    challenge: NodeChallenge
    xp_breakdown?: {
        concepts_read: number
        practice_completed: number
        quiz_passed: number
        challenge_completed: number
    }
}

interface InteractiveNodeProps {
    data: InteractiveNodeData
    onComplete?: (xpEarned: number) => void
}

/* ============================================================================
   SECTION NAVIGATION
   ============================================================================ */

type SectionId = "intro" | "concepts" | "practice" | "quiz" | "challenge"

const SECTIONS: { id: SectionId; label: string; icon: React.ReactNode }[] = [
    { id: "intro", label: "Intro", icon: <Target className="w-4 h-4" /> },
    { id: "concepts", label: "Koncept", icon: <BookOpen className="w-4 h-4" /> },
    { id: "practice", label: "Praktik", icon: <Terminal className="w-4 h-4" /> },
    { id: "quiz", label: "Quiz", icon: <HelpCircle className="w-4 h-4" /> },
    { id: "challenge", label: "Challenge", icon: <Trophy className="w-4 h-4" /> },
]

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function InteractiveNodeV2({ data, onComplete }: InteractiveNodeProps) {
    const [activeSection, setActiveSection] = useState<SectionId>("intro")
    const [completedSections, setCompletedSections] = useState<Set<SectionId>>(new Set())
    const [xpEarned, setXpEarned] = useState(0)

    const xpBreakdown = data.xp_breakdown || {
        concepts_read: 20,
        practice_completed: 30,
        quiz_passed: 30,
        challenge_completed: 20
    }

    const timePerSection = data.estimated_time_per_section || {
        intro: 2,
        concepts: 8,
        practice: 10,
        quiz: 5,
        challenge: 5
    }

    const markSectionComplete = useCallback((section: SectionId, xp: number = 0) => {
        if (!completedSections.has(section)) {
            setCompletedSections(prev => new Set([...prev, section]))
            setXpEarned(prev => prev + xp)
        }
    }, [completedSections])

    const handlePracticeComplete = useCallback(() => {
        markSectionComplete("practice", xpBreakdown.practice_completed)
    }, [markSectionComplete, xpBreakdown])

    const handleQuizComplete = useCallback((passed: boolean, score: number) => {
        if (passed) {
            markSectionComplete("quiz", xpBreakdown.quiz_passed)
        }
    }, [markSectionComplete, xpBreakdown])

    const handleChallengeComplete = useCallback(() => {
        markSectionComplete("challenge", xpBreakdown.challenge_completed)
        onComplete?.(xpEarned + xpBreakdown.challenge_completed)
    }, [markSectionComplete, xpBreakdown, xpEarned, onComplete])

    const goToNextSection = () => {
        const currentIndex = SECTIONS.findIndex(s => s.id === activeSection)
        if (currentIndex < SECTIONS.length - 1) {
            // Mark current section as complete
            if (activeSection === "intro") {
                markSectionComplete("intro")
            } else if (activeSection === "concepts") {
                markSectionComplete("concepts", xpBreakdown.concepts_read)
            }
            setActiveSection(SECTIONS[currentIndex + 1].id)
        }
    }

    const totalProgress = (completedSections.size / SECTIONS.length) * 100

    return (
        <div className="space-y-6">
            {/* Progress Header */}
            <div className={cn(
                "bg-zinc-800/50 border border-zinc-700/50",
                "rounded-xl p-4"
            )}>
                <div className="flex items-center justify-between mb-3">
                    <div className="flex items-center gap-2">
                        <Clock className="w-4 h-4 text-zinc-400" />
                        <span className="text-sm text-zinc-400">
                            {data.estimated_minutes} min totalt
                        </span>
                    </div>
                    <div className="flex items-center gap-2">
                        <span className="text-sm text-amber-400 font-medium">
                            {xpEarned} / {data.xp_reward} XP
                        </span>
                    </div>
                </div>

                {/* Section Navigation */}
                <div className="flex gap-2">
                    {SECTIONS.map((section, index) => {
                        const isActive = activeSection === section.id
                        const isCompleted = completedSections.has(section.id)
                        const time = timePerSection[section.id]

                        return (
                            <button
                                key={section.id}
                                onClick={() => setActiveSection(section.id)}
                                className={cn(
                                    "flex-1 py-2 px-3 rounded-lg",
                                    "flex flex-col items-center gap-1",
                                    "transition-all duration-200",
                                    "text-xs",
                                    isActive && "bg-purple-900/30 border border-purple-500/50",
                                    !isActive && isCompleted && "bg-emerald-900/20 border border-emerald-500/30",
                                    !isActive && !isCompleted && "bg-zinc-700/30 border border-transparent hover:border-zinc-600"
                                )}
                            >
                                <div className={cn(
                                    "flex items-center gap-1",
                                    isActive && "text-purple-400",
                                    isCompleted && !isActive && "text-emerald-400",
                                    !isActive && !isCompleted && "text-zinc-400"
                                )}>
                                    {isCompleted ? (
                                        <CheckCircle2 className="w-4 h-4" />
                                    ) : (
                                        section.icon
                                    )}
                                </div>
                                <span className={cn(
                                    isActive && "text-white",
                                    isCompleted && !isActive && "text-emerald-300",
                                    !isActive && !isCompleted && "text-zinc-400"
                                )}>
                                    {section.label}
                                </span>
                                <span className="text-zinc-500 text-[10px]">
                                    {time} min
                                </span>
                            </button>
                        )
                    })}
                </div>

                {/* Progress Bar */}
                <div className="mt-3 h-1.5 bg-zinc-700 rounded-full overflow-hidden">
                    <div 
                        className="h-full bg-gradient-to-r from-purple-500 to-emerald-500 transition-all duration-500"
                        style={{ width: `${totalProgress}%` }}
                    />
                </div>
            </div>

            {/* Section Content */}
            <div className={cn(
                "bg-zinc-900/80 backdrop-blur-xl",
                "rounded-2xl border border-zinc-700/50",
                "p-6 md:p-8"
            )}>
                {/* INTRO */}
                {activeSection === "intro" && (
                    <div className="space-y-6">
                        <IntroBlock
                            headline={data.intro.headline}
                            hook={data.intro.hook}
                            learningObjectives={data.intro.learning_objectives}
                            prerequisites={data.intro.prerequisites}
                            estimatedMinutes={data.estimated_minutes}
                        />
                        <div className="flex justify-end">
                            <button
                                onClick={goToNextSection}
                                className={cn(
                                    "flex items-center gap-2 px-6 py-3",
                                    "bg-purple-600 hover:bg-purple-500",
                                    "rounded-xl text-white font-medium",
                                    "transition-colors"
                                )}
                            >
                                Fortsätt till Koncept
                                <ChevronRight className="w-5 h-5" />
                            </button>
                        </div>
                    </div>
                )}

                {/* CONCEPTS */}
                {activeSection === "concepts" && (
                    <div className="space-y-6">
                        <h2 className="text-2xl font-bold text-white mb-6">
                            📖 Koncept
                        </h2>
                        {data.concepts.map((concept, index) => (
                            <ConceptBlock
                                key={index}
                                title={concept.title}
                                explanation={concept.explanation}
                                diagram={concept.diagram}
                                proTip={concept.pro_tip}
                                commonMistake={concept.common_mistake}
                                isExpanded={index === 0}
                            />
                        ))}
                        <div className="flex justify-end">
                            <button
                                onClick={goToNextSection}
                                className={cn(
                                    "flex items-center gap-2 px-6 py-3",
                                    "bg-purple-600 hover:bg-purple-500",
                                    "rounded-xl text-white font-medium",
                                    "transition-colors"
                                )}
                            >
                                Fortsätt till Praktik
                                <ChevronRight className="w-5 h-5" />
                            </button>
                        </div>
                    </div>
                )}

                {/* PRACTICE */}
                {activeSection === "practice" && (
                    <SimulatedTerminal
                        description={data.practice.description}
                        exercises={data.practice.exercises.map(e => ({
                            ...e,
                            expectedOutput: e.expected_output
                        }))}
                        onComplete={handlePracticeComplete}
                    />
                )}

                {/* QUIZ */}
                {activeSection === "quiz" && (
                    <QuizBlock
                        flashcards={data.quiz.flashcards?.map(f => ({
                            term: f.term,
                            definition: f.definition
                        }))}
                        questions={data.quiz.multiple_choice.map(q => ({
                            question: q.question,
                            options: q.options,
                            correctAnswer: q.correct_answer,
                            explanation: q.explanation
                        }))}
                        passingScore={data.quiz.passing_score}
                        onComplete={handleQuizComplete}
                    />
                )}

                {/* CHALLENGE */}
                {activeSection === "challenge" && (
                    <ChallengeBlock
                        title={data.challenge.title}
                        scenario={data.challenge.scenario}
                        requirements={data.challenge.requirements}
                        hints={data.challenge.hints}
                        solution={data.challenge.solution}
                        xpBonus={data.challenge.xp_bonus || xpBreakdown.challenge_completed}
                        onComplete={handleChallengeComplete}
                    />
                )}
            </div>
        </div>
    )
}

export default InteractiveNodeV2
