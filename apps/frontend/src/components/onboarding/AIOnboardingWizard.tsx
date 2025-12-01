"use client"

/**
 * ============================================================================
 * AI ONBOARDING WIZARD - Full-Screen Welcome Experience
 * ============================================================================
 *
 * A beautiful multi-step wizard that welcomes new users and introduces them
 * to the DevOps AI Assistant. Triggered on first sign-in.
 *
 * Steps:
 * 1. Welcome - Introduction to the platform
 * 2. Profile - Name and experience level
 * 3. Goals - What do you want to learn?
 * 4. Meet AI - Introduction to your DevOps Wizard
 * 5. Start - Begin your journey
 *
 * @phase AI-WIZARD-FAS-1
 */

import { useState, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import {
    Sparkles,
    ChevronRight,
    ChevronLeft,
    User,
    Target,
    Rocket,
    Bot,
    Terminal,
    Cloud,
    Code,
    Server,
    Shield,
    Zap,
    Check,
    X,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface AIOnboardingWizardProps {
    onComplete: (data: OnboardingData) => void
    onSkip?: () => void
    userName?: string
}

interface OnboardingData {
    firstName: string
    lastName: string
    experienceLevel: ExperienceLevel
    goals: string[]
    studyTime: StudyTime
    hasMetAI: boolean
}

type ExperienceLevel = "beginner" | "intermediate" | "advanced"
type StudyTime = "30min" | "1hour" | "2hours"

/* ============================================================================
   CONSTANTS
   ============================================================================ */

const EXPERIENCE_LEVELS = [
    {
        id: "beginner" as ExperienceLevel,
        label: "Beginner",
        description: "New to DevOps, learning the basics",
        icon: Sparkles,
        color: "from-green-500 to-emerald-600",
    },
    {
        id: "intermediate" as ExperienceLevel,
        label: "Intermediate",
        description: "Familiar with Linux, Git, basic cloud",
        icon: Terminal,
        color: "from-blue-500 to-indigo-600",
    },
    {
        id: "advanced" as ExperienceLevel,
        label: "Advanced",
        description: "Production experience, seeking mastery",
        icon: Rocket,
        color: "from-purple-500 to-pink-600",
    },
]

const LEARNING_GOALS = [
    { id: "linux", label: "Master Linux", icon: Terminal },
    { id: "docker", label: "Learn Docker", icon: Server },
    { id: "kubernetes", label: "Kubernetes", icon: Cloud },
    { id: "aws", label: "AWS Cloud", icon: Cloud },
    { id: "cicd", label: "CI/CD Pipelines", icon: Zap },
    { id: "terraform", label: "Infrastructure as Code", icon: Code },
    { id: "security", label: "DevSecOps", icon: Shield },
    { id: "career", label: "Career Change", icon: Target },
]

const STUDY_TIMES = [
    { id: "30min" as StudyTime, label: "30 min/day", description: "Quick daily sessions" },
    { id: "1hour" as StudyTime, label: "1 hour/day", description: "Balanced learning" },
    { id: "2hours" as StudyTime, label: "2+ hours/day", description: "Intensive mode" },
]

const WIZARD_MESSAGES = [
    "Hey there! I'm your DevOps Wizard 🧙‍♂️",
    "I know everything about Linux, Docker, Kubernetes, AWS, and more.",
    "I'll be here whenever you need help - just click the chat bubble!",
    "Let's start your DevOps journey together.",
]

/* ============================================================================
   STEP COMPONENTS
   ============================================================================ */

function StepWelcome({ onNext }: { onNext: () => void }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="text-center space-y-8"
        >
            {/* Logo/Icon */}
            <motion.div
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                transition={{ type: "spring", delay: 0.2 }}
                className="w-24 h-24 mx-auto rounded-3xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shadow-2xl shadow-indigo-500/30"
            >
                <Rocket className="w-12 h-12 text-white" />
            </motion.div>

            {/* Title */}
            <div className="space-y-4">
                <motion.h1
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.3 }}
                    className="text-4xl md:text-5xl font-bold text-white"
                >
                    Welcome to{" "}
                    <span className="bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent">
                        DevOpsHub
                    </span>
                </motion.h1>
                <motion.p
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.4 }}
                    className="text-xl text-gray-400 max-w-lg mx-auto"
                >
                    Your journey to DevOps mastery starts here. Let&apos;s set you up for success.
                </motion.p>
            </div>

            {/* CTA */}
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.5 }}
            >
                <Button
                    onClick={onNext}
                    size="lg"
                    className="bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-600 hover:to-purple-700 text-white px-8 py-6 text-lg rounded-2xl shadow-xl shadow-indigo-500/30 transition-all hover:scale-105"
                >
                    Get Started
                    <ChevronRight className="w-5 h-5 ml-2" />
                </Button>
            </motion.div>
        </motion.div>
    )
}

function StepProfile({
    data,
    onUpdate,
    onNext,
    onBack,
}: {
    data: OnboardingData
    onUpdate: (data: Partial<OnboardingData>) => void
    onNext: () => void
    onBack: () => void
}) {
    const [selectedLevel, setSelectedLevel] = useState<ExperienceLevel | null>(
        data.experienceLevel || null
    )

    const handleLevelSelect = (level: ExperienceLevel) => {
        setSelectedLevel(level)
        onUpdate({ experienceLevel: level })
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="space-y-8"
        >
            {/* Header */}
            <div className="text-center space-y-2">
                <h2 className="text-3xl font-bold text-white">Tell us about yourself</h2>
                <p className="text-gray-400">This helps us personalize your experience</p>
            </div>

            {/* Name inputs */}
            <div className="grid grid-cols-2 gap-4 max-w-md mx-auto">
                <div className="space-y-2">
                    <label className="text-sm text-gray-400">First Name</label>
                    <Input
                        value={data.firstName}
                        onChange={(e) => onUpdate({ firstName: e.target.value })}
                        placeholder="John"
                        className="bg-white/5 border-white/10 text-white placeholder:text-gray-500 rounded-xl"
                    />
                </div>
                <div className="space-y-2">
                    <label className="text-sm text-gray-400">Last Name</label>
                    <Input
                        value={data.lastName}
                        onChange={(e) => onUpdate({ lastName: e.target.value })}
                        placeholder="Doe"
                        className="bg-white/5 border-white/10 text-white placeholder:text-gray-500 rounded-xl"
                    />
                </div>
            </div>

            {/* Experience Level */}
            <div className="space-y-4">
                <label className="text-sm text-gray-400 block text-center">
                    What&apos;s your DevOps experience?
                </label>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-2xl mx-auto">
                    {EXPERIENCE_LEVELS.map((level) => {
                        const Icon = level.icon
                        const isSelected = selectedLevel === level.id
                        return (
                            <motion.button
                                key={level.id}
                                whileHover={{ scale: 1.02 }}
                                whileTap={{ scale: 0.98 }}
                                onClick={() => handleLevelSelect(level.id)}
                                className={cn(
                                    "relative p-6 rounded-2xl border-2 transition-all text-left",
                                    isSelected
                                        ? "border-indigo-500 bg-indigo-500/10"
                                        : "border-white/10 bg-white/5 hover:border-white/20"
                                )}
                            >
                                {isSelected && (
                                    <motion.div
                                        initial={{ scale: 0 }}
                                        animate={{ scale: 1 }}
                                        className="absolute top-3 right-3 w-6 h-6 rounded-full bg-indigo-500 flex items-center justify-center"
                                    >
                                        <Check className="w-4 h-4 text-white" />
                                    </motion.div>
                                )}
                                <div
                                    className={cn(
                                        "w-12 h-12 rounded-xl mb-4 flex items-center justify-center bg-gradient-to-br",
                                        level.color
                                    )}
                                >
                                    <Icon className="w-6 h-6 text-white" />
                                </div>
                                <h3 className="font-semibold text-white mb-1">{level.label}</h3>
                                <p className="text-sm text-gray-400">{level.description}</p>
                            </motion.button>
                        )
                    })}
                </div>
            </div>

            {/* Navigation */}
            <div className="flex justify-between max-w-2xl mx-auto pt-4">
                <Button
                    variant="ghost"
                    onClick={onBack}
                    className="text-gray-400 hover:text-white"
                >
                    <ChevronLeft className="w-4 h-4 mr-2" />
                    Back
                </Button>
                <Button
                    onClick={onNext}
                    disabled={!selectedLevel || !data.firstName}
                    className="bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-600 hover:to-purple-700 text-white px-6 rounded-xl disabled:opacity-50"
                >
                    Continue
                    <ChevronRight className="w-4 h-4 ml-2" />
                </Button>
            </div>
        </motion.div>
    )
}

function StepGoals({
    data,
    onUpdate,
    onNext,
    onBack,
}: {
    data: OnboardingData
    onUpdate: (data: Partial<OnboardingData>) => void
    onNext: () => void
    onBack: () => void
}) {
    const [selectedGoals, setSelectedGoals] = useState<string[]>(data.goals || [])
    const [selectedTime, setSelectedTime] = useState<StudyTime | null>(data.studyTime || null)

    const toggleGoal = (goalId: string) => {
        const updated = selectedGoals.includes(goalId)
            ? selectedGoals.filter((g) => g !== goalId)
            : [...selectedGoals, goalId]
        setSelectedGoals(updated)
        onUpdate({ goals: updated })
    }

    const selectTime = (time: StudyTime) => {
        setSelectedTime(time)
        onUpdate({ studyTime: time })
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="space-y-8"
        >
            {/* Header */}
            <div className="text-center space-y-2">
                <h2 className="text-3xl font-bold text-white">What do you want to learn?</h2>
                <p className="text-gray-400">Select all that interest you</p>
            </div>

            {/* Goals Grid */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-3 max-w-2xl mx-auto">
                {LEARNING_GOALS.map((goal) => {
                    const Icon = goal.icon
                    const isSelected = selectedGoals.includes(goal.id)
                    return (
                        <motion.button
                            key={goal.id}
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                            onClick={() => toggleGoal(goal.id)}
                            className={cn(
                                "p-4 rounded-xl border-2 transition-all flex flex-col items-center gap-2",
                                isSelected
                                    ? "border-indigo-500 bg-indigo-500/10"
                                    : "border-white/10 bg-white/5 hover:border-white/20"
                            )}
                        >
                            <Icon
                                className={cn(
                                    "w-6 h-6 transition-colors",
                                    isSelected ? "text-indigo-400" : "text-gray-400"
                                )}
                            />
                            <span
                                className={cn(
                                    "text-sm font-medium transition-colors",
                                    isSelected ? "text-white" : "text-gray-400"
                                )}
                            >
                                {goal.label}
                            </span>
                        </motion.button>
                    )
                })}
            </div>

            {/* Study Time */}
            <div className="space-y-4">
                <label className="text-sm text-gray-400 block text-center">
                    How much time can you dedicate?
                </label>
                <div className="flex justify-center gap-4">
                    {STUDY_TIMES.map((time) => (
                        <motion.button
                            key={time.id}
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                            onClick={() => selectTime(time.id)}
                            className={cn(
                                "px-6 py-3 rounded-xl border-2 transition-all",
                                selectedTime === time.id
                                    ? "border-indigo-500 bg-indigo-500/10 text-white"
                                    : "border-white/10 bg-white/5 text-gray-400 hover:border-white/20"
                            )}
                        >
                            <div className="font-medium">{time.label}</div>
                            <div className="text-xs opacity-70">{time.description}</div>
                        </motion.button>
                    ))}
                </div>
            </div>

            {/* Navigation */}
            <div className="flex justify-between max-w-2xl mx-auto pt-4">
                <Button
                    variant="ghost"
                    onClick={onBack}
                    className="text-gray-400 hover:text-white"
                >
                    <ChevronLeft className="w-4 h-4 mr-2" />
                    Back
                </Button>
                <Button
                    onClick={onNext}
                    disabled={selectedGoals.length === 0 || !selectedTime}
                    className="bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-600 hover:to-purple-700 text-white px-6 rounded-xl disabled:opacity-50"
                >
                    Continue
                    <ChevronRight className="w-4 h-4 ml-2" />
                </Button>
            </div>
        </motion.div>
    )
}

function StepMeetAI({
    firstName,
    onNext,
    onBack,
}: {
    firstName: string
    onNext: () => void
    onBack: () => void
}) {
    const [currentMessage, setCurrentMessage] = useState(0)
    const [isTyping, setIsTyping] = useState(true)

    useEffect(() => {
        if (currentMessage < WIZARD_MESSAGES.length - 1) {
            const timer = setTimeout(() => {
                setIsTyping(true)
                setTimeout(() => {
                    setCurrentMessage((prev) => prev + 1)
                    setIsTyping(false)
                }, 500)
            }, 2000)
            return () => clearTimeout(timer)
        }
    }, [currentMessage])

    useEffect(() => {
        const timer = setTimeout(() => setIsTyping(false), 500)
        return () => clearTimeout(timer)
    }, [])

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="space-y-8"
        >
            {/* AI Avatar */}
            <div className="flex flex-col items-center">
                <motion.div
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    transition={{ type: "spring", delay: 0.2 }}
                    className="relative"
                >
                    <div className="w-32 h-32 rounded-full bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center shadow-2xl shadow-purple-500/30">
                        <Bot className="w-16 h-16 text-white" />
                    </div>
                    {/* Pulse effect */}
                    <motion.div
                        animate={{ scale: [1, 1.2, 1], opacity: [0.5, 0, 0.5] }}
                        transition={{ duration: 2, repeat: Infinity }}
                        className="absolute inset-0 rounded-full bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500"
                    />
                </motion.div>
            </div>

            {/* Chat Bubble */}
            <div className="max-w-md mx-auto">
                <AnimatePresence mode="wait">
                    <motion.div
                        key={currentMessage}
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -10 }}
                        className="bg-white/10 backdrop-blur-xl rounded-2xl p-6 border border-white/10"
                    >
                        {isTyping ? (
                            <div className="flex gap-1">
                                <motion.div
                                    animate={{ y: [0, -5, 0] }}
                                    transition={{ duration: 0.5, repeat: Infinity, delay: 0 }}
                                    className="w-2 h-2 bg-indigo-400 rounded-full"
                                />
                                <motion.div
                                    animate={{ y: [0, -5, 0] }}
                                    transition={{ duration: 0.5, repeat: Infinity, delay: 0.1 }}
                                    className="w-2 h-2 bg-indigo-400 rounded-full"
                                />
                                <motion.div
                                    animate={{ y: [0, -5, 0] }}
                                    transition={{ duration: 0.5, repeat: Infinity, delay: 0.2 }}
                                    className="w-2 h-2 bg-indigo-400 rounded-full"
                                />
                            </div>
                        ) : (
                            <p className="text-white text-lg">
                                {currentMessage === 0
                                    ? `Hey ${firstName}! I'm your DevOps Wizard 🧙‍♂️`
                                    : WIZARD_MESSAGES[currentMessage]}
                            </p>
                        )}
                    </motion.div>
                </AnimatePresence>

                {/* Progress dots */}
                <div className="flex justify-center gap-2 mt-4">
                    {WIZARD_MESSAGES.map((_, i) => (
                        <div
                            key={i}
                            className={cn(
                                "w-2 h-2 rounded-full transition-all",
                                i <= currentMessage ? "bg-indigo-500" : "bg-white/20"
                            )}
                        />
                    ))}
                </div>
            </div>

            {/* Navigation */}
            <div className="flex justify-between max-w-2xl mx-auto pt-4">
                <Button
                    variant="ghost"
                    onClick={onBack}
                    className="text-gray-400 hover:text-white"
                >
                    <ChevronLeft className="w-4 h-4 mr-2" />
                    Back
                </Button>
                <Button
                    onClick={onNext}
                    className="bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-600 hover:to-purple-700 text-white px-6 rounded-xl"
                >
                    Let&apos;s Go!
                    <Rocket className="w-4 h-4 ml-2" />
                </Button>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function AIOnboardingWizard({
    onComplete,
    onSkip,
    userName,
}: AIOnboardingWizardProps) {
    const [step, setStep] = useState(0)
    const [data, setData] = useState<OnboardingData>({
        firstName: userName?.split(" ")[0] || "",
        lastName: userName?.split(" ").slice(1).join(" ") || "",
        experienceLevel: "beginner",
        goals: [],
        studyTime: "1hour",
        hasMetAI: false,
    })

    const updateData = (updates: Partial<OnboardingData>) => {
        setData((prev) => ({ ...prev, ...updates }))
    }

    const handleComplete = () => {
        onComplete({ ...data, hasMetAI: true })
    }

    const STEPS = [
        <StepWelcome key="welcome" onNext={() => setStep(1)} />,
        <StepProfile
            key="profile"
            data={data}
            onUpdate={updateData}
            onNext={() => setStep(2)}
            onBack={() => setStep(0)}
        />,
        <StepGoals
            key="goals"
            data={data}
            onUpdate={updateData}
            onNext={() => setStep(3)}
            onBack={() => setStep(1)}
        />,
        <StepMeetAI
            key="meetai"
            firstName={data.firstName || "there"}
            onNext={handleComplete}
            onBack={() => setStep(2)}
        />,
    ]

    return (
        <div className="fixed inset-0 z-50 bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 flex items-center justify-center p-4">
            {/* Background effects */}
            <div className="absolute inset-0 overflow-hidden">
                <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-indigo-500/20 rounded-full blur-3xl" />
                <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-purple-500/20 rounded-full blur-3xl" />
            </div>

            {/* Skip button */}
            {onSkip && (
                <button
                    onClick={onSkip}
                    className="absolute top-6 right-6 text-gray-500 hover:text-gray-300 transition-colors flex items-center gap-2"
                >
                    Skip
                    <X className="w-4 h-4" />
                </button>
            )}

            {/* Progress indicator */}
            <div className="absolute top-6 left-1/2 -translate-x-1/2 flex gap-2">
                {[0, 1, 2, 3].map((i) => (
                    <div
                        key={i}
                        className={cn(
                            "h-1 rounded-full transition-all duration-300",
                            i === step
                                ? "w-8 bg-indigo-500"
                                : i < step
                                    ? "w-4 bg-indigo-500/50"
                                    : "w-4 bg-white/20"
                        )}
                    />
                ))}
            </div>

            {/* Step content */}
            <div className="relative z-10 w-full max-w-3xl">
                <AnimatePresence mode="wait">
                    {STEPS[step]}
                </AnimatePresence>
            </div>
        </div>
    )
}

export default AIOnboardingWizard
