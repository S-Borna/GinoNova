/**
 * Shared types for Tenta Simulator components
 */
import { type Omtenta2Topic } from "@/data/omtenta-2.0-quiz"

// All available question sources
export type QuestionSource = 'handson' | 'linux-commands' | 'linux-tenta' | 'omtenta-2' | 'tenta-floden' | 'manpage-floden'

// Unified question type for simulator (always has G/VG difficulty)
export interface SimulatorQuestion {
    id: string
    question: string
    options: string[]
    correctIndex?: 0 | 1 | 2 | 3  // For single-select (legacy)
    correctIndices: number[]       // For multi-select support
    explanation: string
    difficulty: 'G' | 'VG'
    category: string
    source: QuestionSource
    scenario?: string // Optional scenario context
    isMultiSelect: boolean
    nodeTopic?: Omtenta2Topic // For Omtenta 2.0 node filtering
    questionType?: 'scenario' | 'flow' | 'standard' // For Flöden questions
}

export interface SimulatorSettings {
    duration: number // minutes
    questionCount: number
    includeG: boolean
    includeVG: boolean
    showTimer: boolean
    gradingMode: 'live' | 'end' // live = immediate feedback, end = feedback after completion
    selectedSources: QuestionSource[] // Multi-select question sources
    selectedNodes: Omtenta2Topic[] // For Omtenta 2.0 node filtering
    randomizeQuestions: boolean // Randomize question order
    randomizeAnswers: boolean // Randomize answer order per question
}

export interface QuizResult {
    questionId: string
    correct: boolean
    selectedIndex?: number         // Legacy single-select
    selectedIndices: number[]      // Multi-select support
    correctIndex?: number          // Legacy single-select
    correctIndices: number[]       // Multi-select support
    timeSpent: number
}

export type SimulatorPhase = 'setup' | 'quiz' | 'review' | 'results'

export const DEFAULT_SETTINGS: SimulatorSettings = {
    duration: 90,
    questionCount: 200,
    includeG: true,
    includeVG: true,
    showTimer: true,
    gradingMode: 'live',
    selectedSources: ['omtenta-2'], // Default to Omtenta 2.0
    selectedNodes: [], // Will be set to OMTENTA2_TOPICS by consumer
    randomizeQuestions: true, // Randomize question order by default
    randomizeAnswers: true // Randomize answer options by default
}
