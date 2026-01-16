/**
 * Utility functions for Tenta Simulator
 */
import { type SimulatorQuestion } from "./types"

// Shuffle array helper
export function shuffleArray<T>(array: T[]): T[] {
    const shuffled = [...array]
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
    }
    return shuffled
}

// Shuffle options within a question and update correctIndices
export function shuffleQuestionOptions(question: SimulatorQuestion): SimulatorQuestion {
    // Create array of option objects with their original index
    const optionsWithIndex = question.options.map((option, index) => ({
        option,
        wasCorrect: question.correctIndices.includes(index)
    }))

    // Shuffle the options
    const shuffledOptions = shuffleArray(optionsWithIndex)

    // Find new correct indices
    const newCorrectIndices = shuffledOptions
        .map((o, idx) => o.wasCorrect ? idx : -1)
        .filter(idx => idx !== -1)

    return {
        ...question,
        options: shuffledOptions.map(o => o.option),
        correctIndices: newCorrectIndices,
        correctIndex: newCorrectIndices[0] as 0 | 1 | 2 | 3 | undefined
    }
}

// Calculate grade based on percentage
export function calculateGrade(percentage: number): { grade: string; color: string; message: string } {
    if (percentage >= 90) {
        return { grade: "A+", color: "text-green-600", message: "Enastående! Du är mer än redo för tentan!" }
    } else if (percentage >= 80) {
        return { grade: "A", color: "text-green-600", message: "Mycket bra! Fortsätt så här!" }
    } else if (percentage >= 70) {
        return { grade: "B", color: "text-blue-600", message: "Bra jobbat! Du är på rätt väg." }
    } else if (percentage >= 60) {
        return { grade: "C", color: "text-yellow-600", message: "Godkänt! Men öva mer på de svaga områdena." }
    } else if (percentage >= 50) {
        return { grade: "D", color: "text-orange-600", message: "Godkänt men precis. Mer övning behövs!" }
    } else {
        return { grade: "F", color: "text-red-600", message: "Underkänt. Fokusera på grunderna och öva mer." }
    }
}

// Format time from seconds
export function formatTime(seconds: number): string {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins}:${secs.toString().padStart(2, '0')}`
}

// Calculate average time spent per question
export function calculateAverageTime(totalTime: number, questionCount: number): string {
    const avg = totalTime / questionCount
    return `${Math.floor(avg)}s`
}
