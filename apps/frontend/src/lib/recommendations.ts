/**
 * ============================================================================
 * 🎯 SMART RECOMMENDATIONS ENGINE
 * ============================================================================
 *
 * AI-powered recommendations system that analyzes:
 * - User's completed modules
 * - Skill gaps based on career goals
 * - Job market demand trends
 * - Learning velocity and patterns
 *
 * Returns personalized next-best-module suggestions with reasoning
 *
 * @phase MILESTONE-4.0-RECOMMENDATIONS
 */

/* ============================================================================
   TYPES
   ============================================================================ */

export interface Module {
    id: string
    name: string
    slug: string
    difficulty: "beginner" | "intermediate" | "advanced" | "expert"
    prerequisites: string[]
    estimatedHours: number
    skills: string[]
    jobRelevance: number // 0-100, how relevant for job market
    tags: string[]
}

export interface UserProgress {
    completedModules: string[]
    inProgressModules: string[]
    totalXP: number
    skillsLearned: string[]
    weeklyHours: number
    careerGoal?: "first-job" | "level-up" | "switch-to-devops" | "side-project"
}

export interface Recommendation {
    module: Module
    priority: "critical" | "high" | "medium" | "low"
    reason: string
    skillGaps: string[]
    estimatedImpact: number // 0-100, how much it will help achieve goal
    jobDemand: number // 0-100, market demand
}

/* ============================================================================
   MODULE DATABASE (In production, fetch from backend)
   ============================================================================ */

const MODULE_DATABASE: Module[] = [
    {
        id: "devops-foundations",
        name: "DevOps Foundations",
        slug: "devops-foundations",
        difficulty: "beginner",
        prerequisites: [],
        estimatedHours: 4,
        skills: ["DevOps Culture", "CI/CD Basics", "Agile", "Version Control Basics"],
        jobRelevance: 70,
        tags: ["fundamentals", "culture", "beginner"],
    },
    {
        id: "linux-fundamentals",
        name: "Linux Fundamentals",
        slug: "linux-fundamentals",
        difficulty: "beginner",
        prerequisites: ["devops-foundations"],
        estimatedHours: 8,
        skills: ["Linux CLI", "File Systems", "Process Management", "Shell Scripting"],
        jobRelevance: 95,
        tags: ["linux", "cli", "essential"],
    },
    {
        id: "git-version-control",
        name: "Git & Version Control",
        slug: "git-version-control",
        difficulty: "beginner",
        prerequisites: ["linux-fundamentals"],
        estimatedHours: 6,
        skills: ["Git", "GitHub", "Branching", "Merging", "Collaboration"],
        jobRelevance: 100,
        tags: ["git", "vcs", "essential"],
    },
    {
        id: "docker-containers",
        name: "Docker Containers",
        slug: "docker-containers",
        difficulty: "intermediate",
        prerequisites: ["git-version-control"],
        estimatedHours: 10,
        skills: ["Docker", "Containers", "Images", "Networking", "Volumes", "Docker Compose"],
        jobRelevance: 98,
        tags: ["docker", "containers", "critical"],
    },
    {
        id: "cicd-pipelines",
        name: "CI/CD Pipelines",
        slug: "cicd-pipelines",
        difficulty: "intermediate",
        prerequisites: ["docker-containers"],
        estimatedHours: 8,
        skills: ["Jenkins", "GitHub Actions", "GitLab CI", "Automation", "Testing"],
        jobRelevance: 95,
        tags: ["cicd", "automation", "critical"],
    },
    {
        id: "kubernetes-orchestration",
        name: "Kubernetes Orchestration",
        slug: "kubernetes-orchestration",
        difficulty: "advanced",
        prerequisites: ["docker-containers"],
        estimatedHours: 14,
        skills: ["Kubernetes", "Pods", "Services", "Deployments", "Helm", "Ingress"],
        jobRelevance: 100,
        tags: ["kubernetes", "k8s", "orchestration", "critical"],
    },
    {
        id: "cloud-aws",
        name: "AWS Cloud Fundamentals",
        slug: "cloud-aws",
        difficulty: "intermediate",
        prerequisites: ["cicd-pipelines"],
        estimatedHours: 12,
        skills: ["AWS", "EC2", "S3", "IAM", "VPC", "Cloud Architecture"],
        jobRelevance: 97,
        tags: ["aws", "cloud", "critical"],
    },
    {
        id: "infrastructure-as-code",
        name: "Infrastructure as Code",
        slug: "infrastructure-as-code",
        difficulty: "advanced",
        prerequisites: ["cloud-aws"],
        estimatedHours: 10,
        skills: ["Terraform", "Ansible", "IaC", "Provisioning", "Configuration Management"],
        jobRelevance: 92,
        tags: ["iac", "terraform", "ansible"],
    },
    {
        id: "cicd-advanced",
        name: "CI/CD Pipelines Advanced",
        slug: "cicd-advanced",
        difficulty: "advanced",
        prerequisites: ["cicd-pipelines", "kubernetes-orchestration"],
        estimatedHours: 10,
        skills: ["Advanced CI/CD", "ArgoCD", "Spinnaker", "GitOps", "Blue-Green Deployment"],
        jobRelevance: 88,
        tags: ["cicd", "gitops", "advanced"],
    },
    {
        id: "monitoring-observability",
        name: "Monitoring & Observability",
        slug: "monitoring-observability",
        difficulty: "advanced",
        prerequisites: ["kubernetes-orchestration"],
        estimatedHours: 8,
        skills: ["Prometheus", "Grafana", "ELK Stack", "Logging", "Metrics", "Alerting"],
        jobRelevance: 85,
        tags: ["monitoring", "observability", "prometheus"],
    },
]

/* ============================================================================
   JOB MARKET DEMAND DATA (Updated periodically)
   ============================================================================ */

const JOB_MARKET_TRENDS = {
    "kubernetes": 100,
    "docker": 98,
    "aws": 97,
    "cicd": 95,
    "terraform": 92,
    "linux": 95,
    "git": 100,
    "ansible": 80,
    "monitoring": 85,
    "gitops": 75,
}

/* ============================================================================
   SKILL GAP ANALYSIS
   ============================================================================ */

function analyzeSkillGaps(
    userSkills: string[],
    targetSkills: string[]
): string[] {
    return targetSkills.filter(skill =>
        !userSkills.some(userSkill =>
            userSkill.toLowerCase().includes(skill.toLowerCase()) ||
            skill.toLowerCase().includes(userSkill.toLowerCase())
        )
    )
}

/* ============================================================================
   CALCULATE MODULE SCORE
   ============================================================================ */

function calculateModuleScore(
    module: Module,
    progress: UserProgress,
    completedModules: Module[]
): number {
    let score = 0

    // Factor 1: Job relevance (weight: 30%)
    score += module.jobRelevance * 0.3

    // Factor 2: Prerequisites met (critical - blocks if not met)
    const prerequisitesMet = module.prerequisites.every(prereqId =>
        progress.completedModules.includes(prereqId)
    )
    if (!prerequisitesMet) return 0 // Can't recommend if prereqs not met

    // Factor 3: Skill gaps (weight: 25%)
    const skillGaps = analyzeSkillGaps(progress.skillsLearned, module.skills)
    const skillGapScore = (skillGaps.length / module.skills.length) * 100
    score += skillGapScore * 0.25

    // Factor 4: Career goal alignment (weight: 20%)
    if (progress.careerGoal === "first-job") {
        // Prioritize high job relevance and fundamentals
        if (module.jobRelevance > 90) score += 20
        if (module.difficulty === "beginner" || module.difficulty === "intermediate") score += 10
    } else if (progress.careerGoal === "level-up") {
        // Prioritize advanced topics and specializations
        if (module.difficulty === "advanced" || module.difficulty === "expert") score += 20
        if (module.jobRelevance > 85) score += 10
    } else if (progress.careerGoal === "switch-to-devops") {
        // Prioritize breadth and practical skills
        if (module.jobRelevance > 90) score += 25
        if (module.tags.includes("essential") || module.tags.includes("critical")) score += 15
    } else if (progress.careerGoal === "side-project") {
        // Prioritize practical, project-oriented modules
        if (module.tags.includes("docker") || module.tags.includes("cicd")) score += 20
        if (module.estimatedHours <= 8) score += 10 // Prefer shorter modules
    }

    // Factor 5: Learning velocity match (weight: 15%)
    const hoursPerWeek = progress.weeklyHours
    if (hoursPerWeek >= 15 && module.estimatedHours >= 10) score += 15 // Big commitment matches long modules
    else if (hoursPerWeek < 10 && module.estimatedHours <= 8) score += 15 // Low time matches short modules

    // Factor 6: Job market demand (weight: 10%)
    const moduleDemand = module.skills.reduce((max, skill) => {
        const demand = JOB_MARKET_TRENDS[skill.toLowerCase() as keyof typeof JOB_MARKET_TRENDS] || 50
        return Math.max(max, demand)
    }, 0)
    score += moduleDemand * 0.1

    return Math.min(score, 100) // Cap at 100
}

/* ============================================================================
   PRIORITY CALCULATION
   ============================================================================ */

function determinePriority(score: number): "critical" | "high" | "medium" | "low" {
    if (score >= 85) return "critical"
    if (score >= 70) return "high"
    if (score >= 50) return "medium"
    return "low"
}

/* ============================================================================
   GENERATE REASONING
   ============================================================================ */

function generateReason(
    module: Module,
    progress: UserProgress,
    skillGaps: string[]
): string {
    const reasons: string[] = []

    // Job relevance
    if (module.jobRelevance >= 95) {
        reasons.push(`${module.jobRelevance}% of DevOps jobs require this skill`)
    }

    // Career goal alignment
    if (progress.careerGoal === "first-job" && module.tags.includes("essential")) {
        reasons.push("Essential for landing your first DevOps role")
    } else if (progress.careerGoal === "level-up" && module.difficulty === "advanced") {
        reasons.push("Advanced topic that will set you apart from other candidates")
    } else if (progress.careerGoal === "switch-to-devops" && module.tags.includes("critical")) {
        reasons.push("Critical skill for transitioning into DevOps")
    }

    // Skill gaps
    if (skillGaps.length > 0) {
        reasons.push(`Fills ${skillGaps.length} key skill gap${skillGaps.length > 1 ? 's' : ''}`)
    }

    // Prerequisites
    const completedPrereqs = module.prerequisites.filter(prereqId =>
        progress.completedModules.includes(prereqId)
    )
    if (completedPrereqs.length > 0) {
        reasons.push("Builds on modules you've already mastered")
    }

    // Market trends
    const trendingSkills = module.skills.filter(skill => {
        const demand = JOB_MARKET_TRENDS[skill.toLowerCase() as keyof typeof JOB_MARKET_TRENDS]
        return demand && demand >= 90
    })
    if (trendingSkills.length > 0) {
        reasons.push(`High market demand: ${trendingSkills.join(", ")}`)
    }

    return reasons.length > 0 ? reasons[0] : "Next logical step in your learning path"
}

/* ============================================================================
   MAIN RECOMMENDATION FUNCTION
   ============================================================================ */

export function getRecommendations(
    progress: UserProgress,
    limit: number = 5
): Recommendation[] {
    // Get all completed module objects
    const completedModules = MODULE_DATABASE.filter(m =>
        progress.completedModules.includes(m.id)
    )

    // Get skills learned from completed modules
    const allSkillsLearned = completedModules.reduce((skills, module) => {
        return [...skills, ...module.skills]
    }, progress.skillsLearned)

    const updatedProgress = {
        ...progress,
        skillsLearned: allSkillsLearned,
    }

    // Filter out completed and in-progress modules
    const availableModules = MODULE_DATABASE.filter(
        m => !progress.completedModules.includes(m.id) &&
             !progress.inProgressModules.includes(m.id)
    )

    // Calculate scores and create recommendations
    const recommendations: Recommendation[] = availableModules
        .map(module => {
            const score = calculateModuleScore(module, updatedProgress, completedModules)
            const skillGaps = analyzeSkillGaps(updatedProgress.skillsLearned, module.skills)

            return {
                module,
                priority: determinePriority(score),
                reason: generateReason(module, updatedProgress, skillGaps),
                skillGaps,
                estimatedImpact: score,
                jobDemand: module.jobRelevance,
            }
        })
        .filter(rec => rec.estimatedImpact > 0) // Only include valid recommendations
        .sort((a, b) => b.estimatedImpact - a.estimatedImpact) // Sort by impact
        .slice(0, limit) // Limit results

    return recommendations
}

/* ============================================================================
   GET NEXT BEST MODULE (Simple version)
   ============================================================================ */

export function getNextBestModule(progress: UserProgress): Recommendation | null {
    const recommendations = getRecommendations(progress, 1)
    return recommendations.length > 0 ? recommendations[0] : null
}

/* ============================================================================
   LEARNING PATH GENERATOR
   ============================================================================ */

export function generateLearningPath(
    progress: UserProgress,
    targetRole: "junior" | "mid-level" | "senior" = "junior"
): Module[] {
    const path: Module[] = []
    const remainingModules = [...MODULE_DATABASE]

    // Define target skills for each role
    const targetSkills = {
        junior: ["Linux CLI", "Git", "Docker", "CI/CD Basics", "AWS"],
        "mid-level": ["Kubernetes", "Terraform", "Advanced CI/CD", "Monitoring", "IaC"],
        senior: ["Kubernetes Advanced", "Cloud Architecture", "Security", "SRE", "Leadership"],
    }

    const goals = targetSkills[targetRole]

    // Build path by iteratively finding next best module
    let currentProgress = { ...progress }

    while (path.length < 10 && remainingModules.length > 0) {
        const next = getNextBestModule(currentProgress)
        if (!next) break

        path.push(next.module)
        currentProgress.completedModules.push(next.module.id)
        currentProgress.skillsLearned.push(...next.module.skills)

        // Remove from remaining
        const index = remainingModules.findIndex(m => m.id === next.module.id)
        if (index > -1) remainingModules.splice(index, 1)

        // Check if we've covered target skills
        const coveredSkills = goals.filter(goal =>
            currentProgress.skillsLearned.some(skill =>
                skill.toLowerCase().includes(goal.toLowerCase())
            )
        )
        if (coveredSkills.length === goals.length) break
    }

    return path
}

/* ============================================================================
   EXPORT UTILITIES
   ============================================================================ */

export function getModuleById(id: string): Module | undefined {
    return MODULE_DATABASE.find(m => m.id === id)
}

export function getAllModules(): Module[] {
    return MODULE_DATABASE
}

export function getPrerequisiteChain(moduleId: string): Module[] {
    const module = getModuleById(moduleId)
    if (!module) return []

    const chain: Module[] = []
    const visited = new Set<string>()

    function traverse(id: string) {
        if (visited.has(id)) return
        visited.add(id)

        const mod = getModuleById(id)
        if (!mod) return

        // Add prerequisites first (depth-first)
        mod.prerequisites.forEach(prereqId => traverse(prereqId))

        // Then add current module
        chain.push(mod)
    }

    traverse(moduleId)
    return chain
}
