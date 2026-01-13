/**
 * ============================================================================
 * LEARNING PATHS — Career-focused DevOps learning paths
 * ============================================================================
 *
 * Defines multiple career paths with modules, timelines, and job market data.
 * Used by the SkillPath Board visualization.
 *
 * @phase SKILLPATH-VISUALIZATION
 */

export interface LearningPath {
    id: string
    name: string
    description: string
    icon: string
    color: string
    modules: string[] // module slugs in order
    estimatedMonths: number
    avgSalary: {
        junior: string
        mid: string
        senior: string
    }
    jobDemand: number // percentage (0-100)
    skills: string[]
    prerequisites?: string[] // prerequisite path IDs
}

export interface ModulePosition {
    x: number
    y: number
    level: number // vertical level (0 = start, higher = later in path)
}

/**
 * Module coordinates for visualization
 * Key is module slug, value is position
 */
export const MODULE_POSITIONS: Record<string, ModulePosition> = {
    // Foundation Level (Level 0-1)
    "linux-247": { x: 100, y: 100, level: 0 },
    "git-github-mastery": { x: 300, y: 100, level: 0 },
    "bash-mastery": { x: 100, y: 250, level: 1 },

    // Core DevOps (Level 2-3)
    "docker-mastery": { x: 300, y: 250, level: 2 },
    "python-devops": { x: 500, y: 100, level: 2 },
    "kubernetes-mastery": { x: 300, y: 400, level: 3 },
    "cicd-mastery": { x: 500, y: 250, level: 3 },

    // Cloud & Infrastructure (Level 4-5)
    "terraform-mastery": { x: 500, y: 400, level: 4 },
    "aws-devops": { x: 700, y: 250, level: 4 },
    "azure-mastery": { x: 700, y: 400, level: 5 },

    // Advanced & Specialized (Level 6+)
    "ansible-mastery": { x: 700, y: 100, level: 5 },
    "system-design": { x: 900, y: 250, level: 6 },
    "mlops-mastery": { x: 900, y: 400, level: 6 },
    "ai-agents": { x: 1100, y: 250, level: 7 },

    // Programming & Backend (parallel tracks)
    "nodejs-mastery": { x: 100, y: 550, level: 2 },
    "typescript-mastery": { x: 300, y: 550, level: 3 },
    "go-mastery": { x: 500, y: 550, level: 4 },
    "react-nextjs": { x: 700, y: 550, level: 5 },
    "dotnet-mastery": { x: 900, y: 550, level: 5 },
}

/**
 * All available learning paths
 */
export const LEARNING_PATHS: LearningPath[] = [
    {
        id: "junior-devops",
        name: "Junior DevOps Engineer",
        description: "Get your first DevOps job in 3-4 months. Perfect for beginners who want to break into DevOps.",
        icon: "🚀",
        color: "#3B82F6", // blue
        modules: [
            "linux-247",
            "git-github-mastery",
            "bash-mastery",
            "docker-mastery",
            "python-devops",
            "kubernetes-mastery",
            "cicd-mastery"
        ],
        estimatedMonths: 3,
        avgSalary: {
            junior: "38-48k SEK",
            mid: "45-55k SEK",
            senior: "55-70k SEK"
        },
        jobDemand: 95,
        skills: ["Linux", "Docker", "Kubernetes", "CI/CD", "Python", "Git", "Bash"]
    },
    {
        id: "cloud-engineer",
        name: "Cloud Engineer",
        description: "Master AWS and Azure, become a cloud infrastructure expert. Build and manage cloud infrastructure at scale.",
        icon: "☁️",
        color: "#FF9900", // AWS orange
        modules: [
            "linux-247",
            "bash-mastery",
            "docker-mastery",
            "kubernetes-mastery",
            "terraform-mastery",
            "aws-devops",
            "azure-mastery",
            "python-devops"
        ],
        estimatedMonths: 4,
        avgSalary: {
            junior: "42-52k SEK",
            mid: "50-65k SEK",
            senior: "65-85k SEK"
        },
        jobDemand: 92,
        skills: ["AWS", "Azure", "Terraform", "Kubernetes", "Docker", "Linux", "Python"]
    },
    {
        id: "platform-engineer",
        name: "Platform Engineer",
        description: "Build internal developer platforms and tools. Create amazing developer experiences with modern infrastructure.",
        icon: "🏗️",
        color: "#7B42BC", // Terraform purple
        modules: [
            "linux-247",
            "git-github-mastery",
            "docker-mastery",
            "kubernetes-mastery",
            "terraform-mastery",
            "cicd-mastery",
            "python-devops",
            "go-mastery",
            "system-design"
        ],
        estimatedMonths: 5,
        avgSalary: {
            junior: "45-55k SEK",
            mid: "55-70k SEK",
            senior: "70-95k SEK"
        },
        jobDemand: 88,
        skills: ["Kubernetes", "Terraform", "Go", "Python", "System Design", "CI/CD", "Docker"]
    },
    {
        id: "sre-path",
        name: "Site Reliability Engineer (SRE)",
        description: "Ensure system reliability, performance, and scalability. Become an expert in monitoring and incident response.",
        icon: "🔧",
        color: "#10B981", // green
        modules: [
            "linux-247",
            "bash-mastery",
            "python-devops",
            "docker-mastery",
            "kubernetes-mastery",
            "terraform-mastery",
            "cicd-mastery",
            "system-design",
            "go-mastery"
        ],
        estimatedMonths: 5,
        avgSalary: {
            junior: "48-58k SEK",
            mid: "58-75k SEK",
            senior: "75-100k SEK"
        },
        jobDemand: 85,
        skills: ["Monitoring", "Incident Response", "Kubernetes", "Python", "Go", "System Design", "Linux"]
    },
    {
        id: "devsecops",
        name: "DevSecOps Engineer",
        description: "Integrate security into the DevOps pipeline. Protect applications and infrastructure from threats.",
        icon: "🔒",
        color: "#DC2626", // red
        modules: [
            "linux-247",
            "git-github-mastery",
            "bash-mastery",
            "docker-mastery",
            "kubernetes-mastery",
            "cicd-mastery",
            "terraform-mastery",
            "python-devops"
        ],
        estimatedMonths: 4,
        avgSalary: {
            junior: "45-55k SEK",
            mid: "55-70k SEK",
            senior: "70-90k SEK"
        },
        jobDemand: 80,
        skills: ["Security", "Docker", "Kubernetes", "CI/CD", "Terraform", "Python", "Linux"]
    },
    {
        id: "fullstack-devops",
        name: "Full-Stack DevOps",
        description: "Combine full-stack development with DevOps. Build and deploy modern web applications.",
        icon: "⚛️",
        color: "#EC4899", // pink
        modules: [
            "git-github-mastery",
            "docker-mastery",
            "nodejs-mastery",
            "typescript-mastery",
            "react-nextjs",
            "kubernetes-mastery",
            "cicd-mastery",
            "aws-devops"
        ],
        estimatedMonths: 5,
        avgSalary: {
            junior: "42-52k SEK",
            mid: "52-67k SEK",
            senior: "67-85k SEK"
        },
        jobDemand: 90,
        skills: ["React", "Next.js", "TypeScript", "Node.js", "Docker", "Kubernetes", "CI/CD"]
    },
    {
        id: "mlops-engineer",
        name: "MLOps Engineer",
        description: "Deploy and manage ML models in production. Bridge the gap between data science and operations.",
        icon: "🤖",
        color: "#8B5CF6", // purple
        modules: [
            "linux-247",
            "python-devops",
            "docker-mastery",
            "kubernetes-mastery",
            "terraform-mastery",
            "cicd-mastery",
            "mlops-mastery",
            "ai-agents"
        ],
        estimatedMonths: 6,
        avgSalary: {
            junior: "50-60k SEK",
            mid: "60-80k SEK",
            senior: "80-110k SEK"
        },
        jobDemand: 75,
        skills: ["Python", "ML", "Docker", "Kubernetes", "MLOps", "AI", "Data Engineering"]
    },
    {
        id: "automation-specialist",
        name: "Automation Specialist",
        description: "Automate everything. Master scripting, CI/CD, and infrastructure automation.",
        icon: "⚡",
        color: "#F59E0B", // amber
        modules: [
            "linux-247",
            "bash-mastery",
            "python-devops",
            "git-github-mastery",
            "ansible-mastery",
            "terraform-mastery",
            "cicd-mastery",
            "docker-mastery"
        ],
        estimatedMonths: 3,
        avgSalary: {
            junior: "40-50k SEK",
            mid: "48-62k SEK",
            senior: "62-78k SEK"
        },
        jobDemand: 87,
        skills: ["Python", "Bash", "Ansible", "Terraform", "CI/CD", "Git", "Automation"]
    }
]

/**
 * Get a learning path by ID
 */
export function getLearningPath(id: string): LearningPath | undefined {
    return LEARNING_PATHS.find(path => path.id === id)
}

/**
 * Get all modules required for a learning path
 */
export function getPathModules(pathId: string): string[] {
    const path = getLearningPath(pathId)
    return path ? path.modules : []
}

/**
 * Get all learning paths that include a specific module
 */
export function getPathsForModule(moduleSlug: string): LearningPath[] {
    return LEARNING_PATHS.filter(path => path.modules.includes(moduleSlug))
}

/**
 * Calculate progress for a learning path based on completed modules
 */
export function calculatePathProgress(pathId: string, completedModules: string[]): number {
    const path = getLearningPath(pathId)
    if (!path) return 0

    const totalModules = path.modules.length
    const completed = path.modules.filter(m => completedModules.includes(m)).length

    return totalModules > 0 ? Math.round((completed / totalModules) * 100) : 0
}

/**
 * Get next module to complete in a learning path
 */
export function getNextModule(pathId: string, completedModules: string[]): string | null {
    const path = getLearningPath(pathId)
    if (!path) return null

    return path.modules.find(m => !completedModules.includes(m)) || null
}

/**
 * Check if a module is unlocked (prerequisites met)
 */
export function isModuleUnlocked(moduleSlug: string, completedModules: string[]): boolean {
    // For now, all modules are unlocked
    // In the future, we can add prerequisite logic based on MODULE_POSITIONS
    return true
}

/**
 * Get difficulty color
 */
export function getDifficultyColor(difficulty: string): string {
    switch (difficulty) {
        case "beginner":
            return "#10B981" // green
        case "intermediate":
            return "#F59E0B" // amber
        case "advanced":
            return "#EF4444" // red
        case "expert":
            return "#8B5CF6" // purple
        default:
            return "#6B7280" // gray
    }
}

/**
 * Get difficulty label
 */
export function getDifficultyLabel(difficulty: string): string {
    switch (difficulty) {
        case "beginner":
            return "Nybörjare"
        case "intermediate":
            return "Medel"
        case "advanced":
            return "Avancerad"
        case "expert":
            return "Expert"
        default:
            return "Okänd"
    }
}
