/**
 * ============================================================================
 * DIFFICULTY CONFIGURATION — DevOpsHub Learning Levels
 * ============================================================================
 *
 * Three-tier system: Rookie (Beginner), Junior (Intermediate), Senior (Advanced)
 * Each level has distinct visual identity, career mapping, and learning outcomes.
 */

export type DifficultyLevel = 'rookie' | 'junior' | 'senior'

export interface DifficultyConfig {
  level: DifficultyLevel
  label: string
  description: string
  icon: string
  color: {
    from: string
    to: string
    glow: string
    text: string
    bg: string
    border: string
  }
  estimatedMonths: number
  salaryRange: {
    min: number
    max: number
    currency: string
  }
  prerequisites: string
  careerLevel: string
  skills: string[]
}

export const DIFFICULTY_CONFIG: Record<DifficultyLevel, DifficultyConfig> = {
  rookie: {
    level: 'rookie',
    label: 'Rookie',
    description: 'No prerequisites, start here',
    icon: '🌱',
    color: {
      from: '#10b981', // emerald-500
      to: '#059669',   // emerald-600
      glow: 'rgba(16, 185, 129, 0.4)',
      text: '#10b981',
      bg: 'rgba(16, 185, 129, 0.1)',
      border: 'rgba(16, 185, 129, 0.3)',
    },
    estimatedMonths: 4,
    salaryRange: {
      min: 38000,
      max: 45000,
      currency: 'SEK',
    },
    prerequisites: 'None - perfect for beginners',
    careerLevel: 'Junior DevOps Engineer',
    skills: [
      'Linux fundamentals',
      'Git basics',
      'Python scripting',
      'Docker basics',
      'CI/CD introduction',
    ],
  },
  junior: {
    level: 'junior',
    label: 'Junior',
    description: 'Some experience needed',
    icon: '⚡',
    color: {
      from: '#3b82f6', // blue-500
      to: '#2563eb',   // blue-600
      glow: 'rgba(59, 130, 246, 0.4)',
      text: '#3b82f6',
      bg: 'rgba(59, 130, 246, 0.1)',
      border: 'rgba(59, 130, 246, 0.3)',
    },
    estimatedMonths: 6,
    salaryRange: {
      min: 45000,
      max: 60000,
      currency: 'SEK',
    },
    prerequisites: 'Rookie level completed or 6+ months experience',
    careerLevel: 'DevOps Engineer',
    skills: [
      'AWS/Cloud fundamentals',
      'Terraform IaC',
      'Advanced CI/CD',
      'Kubernetes basics',
      'Monitoring & observability',
    ],
  },
  senior: {
    level: 'senior',
    label: 'Senior',
    description: 'For experienced engineers',
    icon: '🔥',
    color: {
      from: '#f97316', // orange-500
      to: '#ea580c',   // orange-600
      glow: 'rgba(249, 115, 22, 0.4)',
      text: '#f97316',
      bg: 'rgba(249, 115, 22, 0.1)',
      border: 'rgba(249, 115, 22, 0.3)',
    },
    estimatedMonths: 12,
    salaryRange: {
      min: 60000,
      max: 75000,
      currency: 'SEK',
    },
    prerequisites: 'Junior level + 2+ years DevOps experience',
    careerLevel: 'Senior DevOps/SRE Engineer',
    skills: [
      'Kubernetes orchestration',
      'Multi-cloud architecture',
      'DevSecOps practices',
      'SRE & reliability engineering',
      'Advanced automation',
    ],
  },
}

/**
 * Get difficulty config by level
 */
export function getDifficultyConfig(level: DifficultyLevel): DifficultyConfig {
  return DIFFICULTY_CONFIG[level]
}

/**
 * Map legacy difficulty strings to new system
 */
export function normalizeDifficulty(difficulty: string | undefined): DifficultyLevel {
  if (!difficulty) return 'rookie'

  const lower = difficulty.toLowerCase()

  if (lower === 'beginner' || lower === 'rookie' || lower === 'easy') {
    return 'rookie'
  }

  if (lower === 'intermediate' || lower === 'junior' || lower === 'medium') {
    return 'junior'
  }

  if (lower === 'advanced' || lower === 'senior' || lower === 'expert' || lower === 'hard') {
    return 'senior'
  }

  return 'rookie'
}

/**
 * Get all difficulty levels in order
 */
export function getAllDifficulties(): DifficultyLevel[] {
  return ['rookie', 'junior', 'senior']
}

/**
 * Check if user is ready for difficulty level based on progress
 */
export function isReadyForLevel(
  level: DifficultyLevel,
  completedRookie: number,
  completedJunior: number
): boolean {
  switch (level) {
    case 'rookie':
      return true // Always ready for rookie
    case 'junior':
      return completedRookie >= 3 // Need at least 3 rookie modules
    case 'senior':
      return completedJunior >= 3 // Need at least 3 junior modules
    default:
      return false
  }
}
