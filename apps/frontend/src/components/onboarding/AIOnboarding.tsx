"use client"

/**
 * ============================================================================
 * 🤖 AI ONBOARDING FLOW — Personalized Learning Path Creator
 * ============================================================================
 *
 * Interactive onboarding with Dallas AI assistant that:
 * - Assesses user's DevOps experience level
 * - Identifies career goals
 * - Runs skill assessment quiz
 * - Creates personalized learning path
 * - Estimates timeline based on availability
 *
 * Design: Cosmic purple/cyan/pink theme with smooth animations
 *
 * @phase MILESTONE-4.0-AI-ONBOARDING
 */

import { useState, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
    Sparkles,
    Rocket,
    Target,
    Clock,
    TrendingUp,
    CheckCircle2,
    ChevronRight,
    Brain,
    Star,
    Zap,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

type ExperienceLevel = "beginner" | "some-experience" | "intermediate" | "advanced"
type CareerGoal = "first-job" | "level-up" | "switch-to-devops" | "side-project"
type WeeklyHours = "5-10" | "10-15" | "15-20" | "20+"

interface OnboardingData {
    experienceLevel: ExperienceLevel | null
    careerGoal: CareerGoal | null
    weeklyHours: WeeklyHours | null
    skillAssessment: {
        score: number
        answers: Record<number, string>
    }
    recommendedPath: string[]
    estimatedWeeks: number
}

interface SkillQuestion {
    id: number
    question: string
    options: { value: string; label: string; correct?: boolean }[]
    difficulty: "easy" | "medium" | "hard"
}

/* ============================================================================
   SKILL ASSESSMENT QUESTIONS
   ============================================================================ */

const SKILL_QUESTIONS: SkillQuestion[] = [
    {
        id: 1,
        question: "What does DevOps primarily focus on?",
        difficulty: "easy",
        options: [
            { value: "a", label: "Just writing code faster" },
            { value: "b", label: "Collaboration between Dev and Ops teams", correct: true },
            { value: "c", label: "Only infrastructure management" },
            { value: "d", label: "Database optimization" },
        ],
    },
    {
        id: 2,
        question: "Which command lists files in a Linux directory?",
        difficulty: "easy",
        options: [
            { value: "a", label: "dir" },
            { value: "b", label: "list" },
            { value: "c", label: "ls", correct: true },
            { value: "d", label: "show" },
        ],
    },
    {
        id: 3,
        question: "What is Docker primarily used for?",
        difficulty: "medium",
        options: [
            { value: "a", label: "Containerization", correct: true },
            { value: "b", label: "Database management" },
            { value: "c", label: "Version control" },
            { value: "d", label: "Web design" },
        ],
    },
    {
        id: 4,
        question: "What does CI/CD stand for?",
        difficulty: "medium",
        options: [
            { value: "a", label: "Computer Integration / Computer Development" },
            { value: "b", label: "Continuous Integration / Continuous Deployment", correct: true },
            { value: "c", label: "Code Integration / Code Delivery" },
            { value: "d", label: "Cloud Infrastructure / Cloud Deployment" },
        ],
    },
    {
        id: 5,
        question: "In Kubernetes, what is a Pod?",
        difficulty: "hard",
        options: [
            { value: "a", label: "A type of database" },
            { value: "b", label: "A group of one or more containers", correct: true },
            { value: "c", label: "A configuration file" },
            { value: "d", label: "A network protocol" },
        ],
    },
]

/* ============================================================================
   COSMIC DALLAS AVATAR
   ============================================================================ */

function DallasAvatar({ pulse = false }: { pulse?: boolean }) {
    return (
        <motion.div
            className="relative w-20 h-20 mx-auto mb-6"
            animate={pulse ? {
                scale: [1, 1.05, 1],
            } : {}}
            transition={{ duration: 2, repeat: Infinity }}
        >
            {/* Outer glow rings */}
            <motion.div
                className="absolute inset-0 rounded-full bg-purple-500/20 blur-xl"
                animate={{
                    scale: [1, 1.3, 1],
                    opacity: [0.3, 0.6, 0.3],
                }}
                transition={{ duration: 3, repeat: Infinity }}
            />
            <motion.div
                className="absolute inset-0 rounded-full bg-cyan-500/20 blur-lg"
                animate={{
                    scale: [1.2, 1, 1.2],
                    opacity: [0.2, 0.5, 0.2],
                }}
                transition={{ duration: 2.5, repeat: Infinity }}
            />

            {/* Core avatar */}
            <div className={cn(
                "relative w-20 h-20 rounded-full",
                "bg-gradient-to-br from-purple-600 via-purple-500 to-cyan-500",
                "flex items-center justify-center",
                "border-2 border-white/20",
                "shadow-[0_0_30px_rgba(139,92,246,0.6)]"
            )}>
                <Brain className="w-10 h-10 text-white" />
            </div>
        </motion.div>
    )
}

/* ============================================================================
   STEP INDICATOR
   ============================================================================ */

interface StepIndicatorProps {
    currentStep: number
    totalSteps: number
}

function StepIndicator({ currentStep, totalSteps }: StepIndicatorProps) {
    return (
        <div className="flex items-center justify-center gap-2 mb-8">
            {Array.from({ length: totalSteps }).map((_, index) => {
                const step = index + 1
                const isActive = step === currentStep
                const isCompleted = step < currentStep

                return (
                    <motion.div
                        key={step}
                        initial={{ scale: 0 }}
                        animate={{ scale: 1 }}
                        transition={{ delay: index * 0.1 }}
                        className="flex items-center"
                    >
                        <div
                            className={cn(
                                "w-10 h-10 rounded-full flex items-center justify-center text-sm font-bold transition-all duration-300",
                                isCompleted && "bg-gradient-to-br from-purple-600 to-purple-500 text-white shadow-[0_0_20px_rgba(139,92,246,0.5)]",
                                isActive && "bg-gradient-to-br from-cyan-600 to-cyan-500 text-white shadow-[0_0_20px_rgba(6,182,212,0.6)] scale-110",
                                !isActive && !isCompleted && "bg-zinc-800 text-zinc-500"
                            )}
                        >
                            {isCompleted ? <CheckCircle2 className="w-5 h-5" /> : step}
                        </div>
                        {index < totalSteps - 1 && (
                            <div
                                className={cn(
                                    "w-8 h-1 mx-1 rounded-full transition-all duration-300",
                                    isCompleted ? "bg-purple-500" : "bg-zinc-800"
                                )}
                            />
                        )}
                    </motion.div>
                )
            })}
        </div>
    )
}

/* ============================================================================
   OPTION CARD
   ============================================================================ */

interface OptionCardProps {
    icon: React.ElementType
    title: string
    description: string
    selected: boolean
    onClick: () => void
    color?: string
}

function OptionCard({ icon: Icon, title, description, selected, onClick, color = "purple" }: OptionCardProps) {
    const colorMap = {
        purple: {
            gradient: "from-purple-600/25 to-purple-500/10",
            border: "border-purple-500/50",
            glow: "shadow-[0_0_30px_rgba(139,92,246,0.4)]",
        },
        cyan: {
            gradient: "from-cyan-600/25 to-cyan-500/10",
            border: "border-cyan-500/50",
            glow: "shadow-[0_0_30px_rgba(6,182,212,0.4)]",
        },
        pink: {
            gradient: "from-pink-600/25 to-pink-500/10",
            border: "border-pink-500/50",
            glow: "shadow-[0_0_30px_rgba(236,72,153,0.4)]",
        },
        emerald: {
            gradient: "from-emerald-600/25 to-emerald-500/10",
            border: "border-emerald-500/50",
            glow: "shadow-[0_0_30px_rgba(16,185,129,0.4)]",
        },
    }

    const colors = colorMap[color as keyof typeof colorMap] || colorMap.purple

    return (
        <motion.button
            onClick={onClick}
            whileHover={{ scale: 1.02, y: -2 }}
            whileTap={{ scale: 0.98 }}
            className={cn(
                "w-full p-5 rounded-2xl text-left transition-all duration-300 cursor-pointer",
                "bg-gradient-to-br from-zinc-900/80 to-zinc-950/80",
                "border-2",
                selected ? cn("bg-gradient-to-br", colors.gradient, colors.border, colors.glow) : "border-zinc-800 hover:border-zinc-700"
            )}
        >
            <div className="flex items-start gap-4">
                <div className={cn(
                    "w-12 h-12 rounded-xl flex items-center justify-center shrink-0",
                    selected ? "bg-gradient-to-br from-purple-500 to-purple-600" : "bg-zinc-800"
                )}>
                    <Icon className="w-6 h-6 text-white" />
                </div>
                <div className="flex-1">
                    <h3 className="text-lg font-bold text-white mb-1">{title}</h3>
                    <p className="text-sm text-zinc-400">{description}</p>
                </div>
                {selected && (
                    <CheckCircle2 className="w-6 h-6 text-purple-400 shrink-0" />
                )}
            </div>
        </motion.button>
    )
}

/* ============================================================================
   MAIN AI ONBOARDING COMPONENT
   ============================================================================ */

interface AIOnboardingProps {
    onComplete: (data: OnboardingData) => void
}

export function AIOnboarding({ onComplete }: AIOnboardingProps) {
    const [currentStep, setCurrentStep] = useState(1)
    const [data, setData] = useState<OnboardingData>({
        experienceLevel: null,
        careerGoal: null,
        weeklyHours: null,
        skillAssessment: {
            score: 0,
            answers: {},
        },
        recommendedPath: [],
        estimatedWeeks: 0,
    })
    const [currentQuestion, setCurrentQuestion] = useState(0)

    const totalSteps = 5

    // Calculate score when assessment is complete
    const calculateScore = () => {
        let score = 0
        Object.entries(data.skillAssessment.answers).forEach(([questionId, answer]) => {
            const question = SKILL_QUESTIONS.find(q => q.id === parseInt(questionId))
            const correctOption = question?.options.find(o => o.correct)
            if (correctOption?.value === answer) {
                score += 1
            }
        })
        return score
    }

    // Generate personalized recommendations
    const generateRecommendations = () => {
        const score = calculateScore()
        const scorePercent = (score / SKILL_QUESTIONS.length) * 100

        let recommendedPath: string[] = []
        let estimatedWeeks = 0

        // Determine path based on experience and score
        if (data.experienceLevel === "beginner" || scorePercent < 40) {
            recommendedPath = [
                "DevOps Foundations",
                "Linux Fundamentals",
                "Git & Version Control",
                "Docker Containers",
            ]
            estimatedWeeks = 12
        } else if (data.experienceLevel === "some-experience" || scorePercent < 60) {
            recommendedPath = [
                "Docker Containers",
                "CI/CD Pipelines",
                "Cloud Fundamentals (AWS)",
                "Infrastructure as Code",
            ]
            estimatedWeeks = 10
        } else if (data.experienceLevel === "intermediate" || scorePercent < 80) {
            recommendedPath = [
                "CI/CD Pipelines Advanced",
                "Kubernetes Orchestration",
                "Infrastructure as Code",
                "Cloud Architecture",
            ]
            estimatedWeeks = 8
        } else {
            recommendedPath = [
                "Kubernetes Advanced",
                "Cloud Architecture",
                "Security & Compliance",
                "Site Reliability Engineering",
            ]
            estimatedWeeks = 6
        }

        // Adjust based on weekly hours
        if (data.weeklyHours === "5-10") estimatedWeeks *= 1.5
        else if (data.weeklyHours === "20+") estimatedWeeks *= 0.7

        setData(prev => ({
            ...prev,
            skillAssessment: { ...prev.skillAssessment, score },
            recommendedPath,
            estimatedWeeks: Math.ceil(estimatedWeeks),
        }))
    }

    const handleNext = () => {
        if (currentStep === 4 && currentQuestion < SKILL_QUESTIONS.length - 1) {
            setCurrentQuestion(prev => prev + 1)
        } else {
            if (currentStep === 4) {
                generateRecommendations()
            }
            setCurrentStep(prev => prev + 1)
        }
    }

    const canProceed = () => {
        if (currentStep === 1) return data.experienceLevel !== null
        if (currentStep === 2) return data.careerGoal !== null
        if (currentStep === 3) return data.weeklyHours !== null
        if (currentStep === 4) return data.skillAssessment.answers[SKILL_QUESTIONS[currentQuestion].id] !== undefined
        return true
    }

    return (
        <div className="min-h-screen bg-[#05050a] relative overflow-hidden flex items-center justify-center p-4">
            {/* Cosmic background */}
            <div className="absolute inset-0 overflow-hidden pointer-events-none">
                <motion.div
                    className="absolute -top-40 -right-40 w-[600px] h-[600px] rounded-full bg-purple-500/15 blur-[100px]"
                    animate={{
                        scale: [1, 1.2, 1],
                        opacity: [0.3, 0.5, 0.3],
                    }}
                    transition={{ duration: 8, repeat: Infinity }}
                />
                <motion.div
                    className="absolute -bottom-40 -left-40 w-[600px] h-[600px] rounded-full bg-cyan-500/15 blur-[100px]"
                    animate={{
                        scale: [1, 1.3, 1],
                        opacity: [0.2, 0.4, 0.2],
                    }}
                    transition={{ duration: 10, repeat: Infinity }}
                />
            </div>

            {/* Content */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="relative z-10 w-full max-w-3xl"
            >
                <div className={cn(
                    "rounded-3xl p-8 md:p-10",
                    "bg-gradient-to-br from-zinc-900/90 via-zinc-900/95 to-zinc-950/90",
                    "border border-white/10",
                    "shadow-[0_0_80px_rgba(139,92,246,0.2)]"
                )}>
                    {/* Dallas Avatar */}
                    <DallasAvatar pulse={currentStep !== totalSteps} />

                    {/* Step Indicator */}
                    <StepIndicator currentStep={currentStep} totalSteps={totalSteps} />

                    <AnimatePresence mode="wait">
                        {/* Step 1: Experience Level */}
                        {currentStep === 1 && (
                            <motion.div
                                key="step1"
                                initial={{ opacity: 0, x: 20 }}
                                animate={{ opacity: 1, x: 0 }}
                                exit={{ opacity: 0, x: -20 }}
                                className="space-y-6"
                            >
                                <div className="text-center mb-8">
                                    <h2 className="text-3xl font-black text-white mb-3">
                                        What&apos;s your DevOps experience?
                                    </h2>
                                    <p className="text-zinc-400">
                                        Dallas will personalize your learning path
                                    </p>
                                </div>

                                <div className="space-y-4">
                                    <OptionCard
                                        icon={Sparkles}
                                        title="Complete Beginner"
                                        description="Never touched DevOps, ready to start from scratch"
                                        selected={data.experienceLevel === "beginner"}
                                        onClick={() => setData(prev => ({ ...prev, experienceLevel: "beginner" }))}
                                        color="purple"
                                    />
                                    <OptionCard
                                        icon={Rocket}
                                        title="Some Experience"
                                        description="Know basics of Linux and Git, want to learn more"
                                        selected={data.experienceLevel === "some-experience"}
                                        onClick={() => setData(prev => ({ ...prev, experienceLevel: "some-experience" }))}
                                        color="cyan"
                                    />
                                    <OptionCard
                                        icon={TrendingUp}
                                        title="Intermediate"
                                        description="Comfortable with containers, looking to master orchestration"
                                        selected={data.experienceLevel === "intermediate"}
                                        onClick={() => setData(prev => ({ ...prev, experienceLevel: "intermediate" }))}
                                        color="pink"
                                    />
                                    <OptionCard
                                        icon={Star}
                                        title="Advanced"
                                        description="Deep expertise, want advanced patterns and architecture"
                                        selected={data.experienceLevel === "advanced"}
                                        onClick={() => setData(prev => ({ ...prev, experienceLevel: "advanced" }))}
                                        color="emerald"
                                    />
                                </div>
                            </motion.div>
                        )}

                        {/* Step 2: Career Goal */}
                        {currentStep === 2 && (
                            <motion.div
                                key="step2"
                                initial={{ opacity: 0, x: 20 }}
                                animate={{ opacity: 1, x: 0 }}
                                exit={{ opacity: 0, x: -20 }}
                                className="space-y-6"
                            >
                                <div className="text-center mb-8">
                                    <h2 className="text-3xl font-black text-white mb-3">
                                        What&apos;s your goal?
                                    </h2>
                                    <p className="text-zinc-400">
                                        This helps Dallas prioritize what you learn
                                    </p>
                                </div>

                                <div className="space-y-4">
                                    <OptionCard
                                        icon={Target}
                                        title="Get My First Job"
                                        description="Land my first DevOps role in 3-6 months"
                                        selected={data.careerGoal === "first-job"}
                                        onClick={() => setData(prev => ({ ...prev, careerGoal: "first-job" }))}
                                        color="purple"
                                    />
                                    <OptionCard
                                        icon={TrendingUp}
                                        title="Level Up Career"
                                        description="Senior role, better salary, more responsibility"
                                        selected={data.careerGoal === "level-up"}
                                        onClick={() => setData(prev => ({ ...prev, careerGoal: "level-up" }))}
                                        color="cyan"
                                    />
                                    <OptionCard
                                        icon={Rocket}
                                        title="Switch to DevOps"
                                        description="Coming from Dev/IT, transitioning to DevOps"
                                        selected={data.careerGoal === "switch-to-devops"}
                                        onClick={() => setData(prev => ({ ...prev, careerGoal: "switch-to-devops" }))}
                                        color="pink"
                                    />
                                    <OptionCard
                                        icon={Zap}
                                        title="Build Side Project"
                                        description="Create and deploy my own projects"
                                        selected={data.careerGoal === "side-project"}
                                        onClick={() => setData(prev => ({ ...prev, careerGoal: "side-project" }))}
                                        color="emerald"
                                    />
                                </div>
                            </motion.div>
                        )}

                        {/* Step 3: Weekly Hours */}
                        {currentStep === 3 && (
                            <motion.div
                                key="step3"
                                initial={{ opacity: 0, x: 20 }}
                                animate={{ opacity: 1, x: 0 }}
                                exit={{ opacity: 0, x: -20 }}
                                className="space-y-6"
                            >
                                <div className="text-center mb-8">
                                    <h2 className="text-3xl font-black text-white mb-3">
                                        How much time can you commit?
                                    </h2>
                                    <p className="text-zinc-400">
                                        Dallas will estimate your timeline
                                    </p>
                                </div>

                                <div className="space-y-4">
                                    <OptionCard
                                        icon={Clock}
                                        title="5-10 hours/week"
                                        description="Taking it slow, learning alongside work/school"
                                        selected={data.weeklyHours === "5-10"}
                                        onClick={() => setData(prev => ({ ...prev, weeklyHours: "5-10" }))}
                                        color="purple"
                                    />
                                    <OptionCard
                                        icon={Clock}
                                        title="10-15 hours/week"
                                        description="Steady pace, consistent progress"
                                        selected={data.weeklyHours === "10-15"}
                                        onClick={() => setData(prev => ({ ...prev, weeklyHours: "10-15" }))}
                                        color="cyan"
                                    />
                                    <OptionCard
                                        icon={Clock}
                                        title="15-20 hours/week"
                                        description="Serious commitment, fast progress"
                                        selected={data.weeklyHours === "15-20"}
                                        onClick={() => setData(prev => ({ ...prev, weeklyHours: "15-20" }))}
                                        color="pink"
                                    />
                                    <OptionCard
                                        icon={Zap}
                                        title="20+ hours/week"
                                        description="Full throttle, career change mode"
                                        selected={data.weeklyHours === "20+"}
                                        onClick={() => setData(prev => ({ ...prev, weeklyHours: "20+" }))}
                                        color="emerald"
                                    />
                                </div>
                            </motion.div>
                        )}

                        {/* Step 4: Skill Assessment */}
                        {currentStep === 4 && (
                            <motion.div
                                key="step4"
                                initial={{ opacity: 0, x: 20 }}
                                animate={{ opacity: 1, x: 0 }}
                                exit={{ opacity: 0, x: -20 }}
                                className="space-y-6"
                            >
                                <div className="text-center mb-8">
                                    <h2 className="text-3xl font-black text-white mb-3">
                                        Quick Skill Check
                                    </h2>
                                    <p className="text-zinc-400">
                                        Question {currentQuestion + 1} of {SKILL_QUESTIONS.length}
                                    </p>
                                </div>

                                <div className={cn(
                                    "p-6 rounded-2xl mb-6",
                                    "bg-gradient-to-br from-purple-600/20 to-purple-500/10",
                                    "border border-purple-500/30"
                                )}>
                                    <p className="text-xl font-semibold text-white">
                                        {SKILL_QUESTIONS[currentQuestion].question}
                                    </p>
                                </div>

                                <div className="space-y-3">
                                    {SKILL_QUESTIONS[currentQuestion].options.map((option) => (
                                        <button
                                            key={option.value}
                                            onClick={() => setData(prev => ({
                                                ...prev,
                                                skillAssessment: {
                                                    ...prev.skillAssessment,
                                                    answers: {
                                                        ...prev.skillAssessment.answers,
                                                        [SKILL_QUESTIONS[currentQuestion].id]: option.value,
                                                    },
                                                },
                                            }))}
                                            className={cn(
                                                "w-full p-4 rounded-xl text-left transition-all duration-200",
                                                "border-2",
                                                data.skillAssessment.answers[SKILL_QUESTIONS[currentQuestion].id] === option.value
                                                    ? "bg-gradient-to-br from-cyan-600/25 to-cyan-500/10 border-cyan-500/50 shadow-[0_0_20px_rgba(6,182,212,0.3)]"
                                                    : "bg-zinc-800/50 border-zinc-700 hover:border-zinc-600"
                                            )}
                                        >
                                            <span className="text-white font-medium">{option.label}</span>
                                        </button>
                                    ))}
                                </div>
                            </motion.div>
                        )}

                        {/* Step 5: Results & Recommendations */}
                        {currentStep === 5 && (
                            <motion.div
                                key="step5"
                                initial={{ opacity: 0, scale: 0.95 }}
                                animate={{ opacity: 1, scale: 1 }}
                                exit={{ opacity: 0, scale: 0.95 }}
                                className="space-y-8"
                            >
                                <div className="text-center">
                                    <motion.div
                                        initial={{ scale: 0 }}
                                        animate={{ scale: 1 }}
                                        transition={{ type: "spring", bounce: 0.5 }}
                                        className="w-24 h-24 mx-auto mb-6 rounded-full bg-gradient-to-br from-emerald-500 to-teal-500 flex items-center justify-center shadow-[0_0_40px_rgba(16,185,129,0.5)]"
                                    >
                                        <Sparkles className="w-12 h-12 text-white" />
                                    </motion.div>
                                    <h2 className="text-3xl font-black text-white mb-3">
                                        Your Path is Ready!
                                    </h2>
                                    <p className="text-zinc-400">
                                        Dallas analyzed your profile and created a personalized plan
                                    </p>
                                </div>

                                {/* Score */}
                                <div className={cn(
                                    "p-6 rounded-2xl text-center",
                                    "bg-gradient-to-br from-purple-600/20 to-purple-500/10",
                                    "border border-purple-500/30"
                                )}>
                                    <p className="text-sm text-zinc-400 mb-2">Skill Assessment Score</p>
                                    <p className="text-4xl font-black text-purple-400">
                                        {data.skillAssessment.score}/{SKILL_QUESTIONS.length}
                                    </p>
                                </div>

                                {/* Recommended Path */}
                                <div>
                                    <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
                                        <Rocket className="w-5 h-5 text-cyan-400" />
                                        Your Learning Path
                                    </h3>
                                    <div className="space-y-3">
                                        {data.recommendedPath.map((module, index) => (
                                            <motion.div
                                                key={module}
                                                initial={{ opacity: 0, x: -20 }}
                                                animate={{ opacity: 1, x: 0 }}
                                                transition={{ delay: index * 0.1 }}
                                                className={cn(
                                                    "p-4 rounded-xl flex items-center gap-4",
                                                    "bg-gradient-to-br from-zinc-800/80 to-zinc-900/80",
                                                    "border border-zinc-700"
                                                )}
                                            >
                                                <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-purple-500 to-purple-600 flex items-center justify-center text-white font-bold">
                                                    {index + 1}
                                                </div>
                                                <span className="text-white font-medium">{module}</span>
                                            </motion.div>
                                        ))}
                                    </div>
                                </div>

                                {/* Timeline */}
                                <div className={cn(
                                    "p-6 rounded-2xl",
                                    "bg-gradient-to-br from-cyan-600/20 to-cyan-500/10",
                                    "border border-cyan-500/30"
                                )}>
                                    <div className="flex items-center justify-between">
                                        <div>
                                            <p className="text-sm text-zinc-400 mb-1">Estimated Timeline</p>
                                            <p className="text-2xl font-black text-cyan-400">
                                                {data.estimatedWeeks} weeks
                                            </p>
                                        </div>
                                        <Clock className="w-12 h-12 text-cyan-400/50" />
                                    </div>
                                </div>
                            </motion.div>
                        )}
                    </AnimatePresence>

                    {/* Navigation */}
                    <div className="flex items-center justify-between mt-8 pt-8 border-t border-zinc-800">
                        {currentStep > 1 && currentStep < 5 && (
                            <Button
                                variant="ghost"
                                onClick={() => {
                                    if (currentStep === 4 && currentQuestion > 0) {
                                        setCurrentQuestion(prev => prev - 1)
                                    } else {
                                        setCurrentStep(prev => prev - 1)
                                    }
                                }}
                                className="text-zinc-400 hover:text-white"
                            >
                                Back
                            </Button>
                        )}
                        {currentStep < 5 ? (
                            <Button
                                onClick={handleNext}
                                disabled={!canProceed()}
                                className={cn(
                                    "ml-auto px-8 py-6 rounded-xl font-bold text-lg",
                                    "bg-gradient-to-r from-purple-600 to-purple-500",
                                    "hover:from-purple-500 hover:to-purple-400",
                                    "shadow-[0_0_30px_rgba(139,92,246,0.4)]",
                                    "disabled:opacity-50 disabled:cursor-not-allowed"
                                )}
                            >
                                {currentStep === 4 && currentQuestion < SKILL_QUESTIONS.length - 1 ? "Next Question" : "Continue"}
                                <ChevronRight className="w-5 h-5 ml-2" />
                            </Button>
                        ) : (
                            <Button
                                onClick={() => onComplete(data)}
                                className={cn(
                                    "w-full px-8 py-6 rounded-xl font-bold text-lg",
                                    "bg-gradient-to-r from-emerald-600 to-teal-500",
                                    "hover:from-emerald-500 hover:to-teal-400",
                                    "shadow-[0_0_30px_rgba(16,185,129,0.4)]"
                                )}
                            >
                                Start Learning Journey
                                <Rocket className="w-5 h-5 ml-2" />
                            </Button>
                        )}
                    </div>
                </div>
            </motion.div>
        </div>
    )
}

export default AIOnboarding
