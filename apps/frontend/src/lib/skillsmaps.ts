/**
 * ============================================================================
 * SKILLSMAPS API CLIENT — NO MOCK DATA, REAL API CALLS ONLY
 * ============================================================================
 *
 * Fetches SkillsMaps data from backend modules/tasks API.
 * Maps module data to SkillsMap format for frontend display.
 *
 * @phase SKILLSMAPS-API-INTEGRATION
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

/* ============================================================================
   TYPES
   ============================================================================ */

export type SkillsMapStatus = "not_started" | "in_progress" | "complete"
export type SkillsMapDifficulty = "beginner" | "intermediate" | "advanced" | "expert"
export type NodeType = "concept" | "practice" | "quiz" | "challenge" | "project"
export type NodeStatus = "not_started" | "in_progress" | "complete"
export type NodeDifficulty = "easy" | "medium" | "hard"

export interface SkillsMapCard {
    id: string
    slug: string
    title: string
    description: string
    icon: string
    color: string
    totalNodes: number
    completedNodes: number
    totalXP: number
    estimatedHours: number
    status: SkillsMapStatus
    difficulty: SkillsMapDifficulty
    tags: string[]
}

export interface SkillsMapNode {
    id: string
    orderIndex: number
    title: string
    description: string
    type: NodeType
    difficulty: NodeDifficulty
    xpReward: number
    estimatedMinutes: number
    status: NodeStatus
    content?: string
}

export interface SkillsMapDetail {
    id: string
    slug: string
    title: string
    description: string
    icon: string
    color: string
    totalNodes: number
    completedNodes: number
    totalXP: number
    estimatedHours: number
    difficulty: SkillsMapDifficulty
    nodes: SkillsMapNode[]
}

// API response types
export interface ApiSuccess<T> {
    ok: true
    data: T
}

export interface ApiFailure {
    ok: false
    status: number
    message: string
}

export type ApiResult<T> = ApiSuccess<T> | ApiFailure

/* ============================================================================
   SKILLSMAP METADATA — Icons, Colors, Tags for each module
   ============================================================================ */

interface SkillsMapMeta {
    icon: string
    color: string
    tags: string[]
}

const SKILLSMAP_METADATA: Record<string, SkillsMapMeta> = {
    "python-devops": { icon: "🐍", color: "#3776AB", tags: ["Scripting", "Automation", "API"] },
    "linux-mastery": { icon: "🐧", color: "#FCC624", tags: ["CLI", "System Admin", "Shell"] },
    "docker-mastery": { icon: "🐳", color: "#2496ED", tags: ["Containers", "DevOps", "Microservices"] },
    "kubernetes-mastery": { icon: "☸️", color: "#326CE5", tags: ["Orchestration", "Cloud Native", "DevOps"] },
    "terraform-mastery": { icon: "🏗️", color: "#7B42BC", tags: ["IaC", "Cloud", "Automation"] },
    "aws-devops": { icon: "☁️", color: "#FF9900", tags: ["Cloud", "Infrastructure", "Serverless"] },
    "git-github-mastery": { icon: "🔀", color: "#F05032", tags: ["Version Control", "Collaboration", "DevOps"] },
    "cicd-mastery": { icon: "🚀", color: "#2088FF", tags: ["Automation", "Pipelines", "DevOps"] },
    "bash-mastery": { icon: "💻", color: "#4EAA25", tags: ["Scripting", "CLI", "Automation"] },
    "javascript-mastery": { icon: "📜", color: "#F7DF1E", tags: ["Programming", "Web", "Node.js"] },
    "typescript-mastery": { icon: "🔷", color: "#3178C6", tags: ["Programming", "Types", "JavaScript"] },
    "go-mastery": { icon: "🔵", color: "#00ADD8", tags: ["Programming", "Systems", "Cloud Native"] },
    "ansible-mastery": { icon: "⚙️", color: "#EE0000", tags: ["Configuration", "Automation", "IaC"] },
    "sql-mastery": { icon: "🗃️", color: "#336791", tags: ["Database", "Queries", "Data"] },
    "system-design": { icon: "🏛️", color: "#6366F1", tags: ["Architecture", "Scalability", "Distributed"] },
    "nodejs-mastery": { icon: "💚", color: "#339933", tags: ["Backend", "API", "JavaScript"] },
    "prompt-engineering": { icon: "🧠", color: "#EC4899", tags: ["AI", "LLM", "GPT"] },
    "mlops-mastery": { icon: "🤖", color: "#FF6B6B", tags: ["ML", "AI", "Production"] },
}

// Default metadata for unknown modules
const DEFAULT_META: SkillsMapMeta = {
    icon: "📚",
    color: "#6366F1",
    tags: ["DevOps", "Learning"]
}

function getMetaForSlug(slug: string): SkillsMapMeta {
    return SKILLSMAP_METADATA[slug] || DEFAULT_META
}

/* ============================================================================
   API FUNCTIONS — REAL DATA FROM BACKEND
   ============================================================================ */

/**
 * Get all SkillsMaps (modules) from backend
 */
export async function getSkillsMaps(): Promise<ApiResult<SkillsMapCard[]>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/modules/`, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
            cache: "no-store",
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch skillsmaps" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch skillsmaps" }
        }

        const modules = await res.json()

        // Exclude deprecated modules (replaced by *-mastery versions)
        const excludedSlugs = ["docker-fundamentals", "docker-advanced-production"]
        const filteredModules = modules.filter((m: any) => !excludedSlugs.includes(m.slug))

        // Transform modules to SkillsMapCard format
        const skillsmaps: SkillsMapCard[] = filteredModules.map((m: any) => {
            const meta = getMetaForSlug(m.slug)
            const totalXP = m.estimated_hours ? Math.round(m.estimated_hours * 100) : 2000

            return {
                id: m.id,
                slug: m.slug,
                title: m.name,
                description: m.description || "",
                icon: meta.icon,
                color: meta.color,
                totalNodes: 20, // Will be updated with actual task count
                completedNodes: 0, // Will be updated with user progress
                totalXP,
                estimatedHours: m.estimated_hours || 20,
                status: "not_started" as SkillsMapStatus,
                difficulty: m.difficulty || "intermediate",
                tags: meta.tags,
            }
        })

        return { ok: true, data: skillsmaps }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Get a single SkillsMap with all its nodes (tasks)
 */
export async function getSkillsMap(slug: string): Promise<ApiResult<SkillsMapDetail>> {
    try {
        // Fetch module
        const moduleRes = await fetch(`${API_BASE_URL}/api/modules/slug/${slug}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
            cache: "no-store",
        })

        if (!moduleRes.ok) {
            const error = await moduleRes.json().catch(() => ({ detail: "SkillsMap not found" }))
            return { ok: false, status: moduleRes.status, message: error.detail || "SkillsMap not found" }
        }

        const moduleData = await moduleRes.json()

        // Fetch tasks for this module
        const tasksRes = await fetch(`${API_BASE_URL}/api/tasks/module/slug/${slug}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
            cache: "no-store",
        })

        let tasks: any[] = []
        if (tasksRes.ok) {
            tasks = await tasksRes.json()
        }

        // Transform tasks to nodes
        const nodes: SkillsMapNode[] = tasks.map((t: any, index: number) => ({
            id: t.id,
            orderIndex: t.order_index || index + 1,
            title: t.title,
            description: t.description || "",
            type: mapDifficultyToType(t.difficulty, index),
            difficulty: t.difficulty || "medium",
            xpReward: t.xp_reward || 100,
            estimatedMinutes: t.estimated_minutes || 30,
            status: "not_started" as NodeStatus,
            content: t.content || "",
        }))

        // Sort by order_index
        nodes.sort((a, b) => a.orderIndex - b.orderIndex)

        const meta = getMetaForSlug(slug)
        const totalXP = nodes.reduce((sum, n) => sum + n.xpReward, 0)

        const skillsmap: SkillsMapDetail = {
            id: moduleData.id,
            slug: moduleData.slug,
            title: moduleData.name,
            description: moduleData.description || "",
            icon: meta.icon,
            color: meta.color,
            totalNodes: nodes.length,
            completedNodes: 0, // Will be updated with user progress
            totalXP,
            estimatedHours: moduleData.estimated_hours || Math.ceil(nodes.length * 0.5),
            difficulty: moduleData.difficulty || "intermediate",
            nodes,
        }

        return { ok: true, data: skillsmap }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Get a single node (task) by ID
 */
export async function getNode(taskId: string): Promise<ApiResult<SkillsMapNode>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/tasks/${taskId}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
            cache: "no-store",
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Node not found" }))
            return { ok: false, status: res.status, message: error.detail || "Node not found" }
        }

        const task = await res.json()

        const node: SkillsMapNode = {
            id: task.id,
            orderIndex: task.order_index || 1,
            title: task.title,
            description: task.description || "",
            type: mapDifficultyToType(task.difficulty, task.order_index),
            difficulty: task.difficulty || "medium",
            xpReward: task.xp_reward || 100,
            estimatedMinutes: task.estimated_minutes || 30,
            status: "not_started" as NodeStatus,
            content: task.content || "",
        }

        return { ok: true, data: node }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/* ============================================================================
   HELPER FUNCTIONS
   ============================================================================ */

/**
 * Map difficulty and position to node type
 */
function mapDifficultyToType(difficulty: string, index: number): NodeType {
    // First few are concepts/basics
    if (index < 4) return index % 2 === 0 ? "concept" : "practice"
    // Middle are practice heavy
    if (index < 12) return index % 3 === 0 ? "concept" : "practice"
    // Later are challenges
    if (index < 18) return index % 4 === 0 ? "challenge" : "practice"
    // Last ones are quizzes
    return "quiz"
}

/**
 * Get user progress for a skillsmap (from localStorage or API)
 */
export function getLocalProgress(slug: string): { completedNodes: string[] } {
    if (typeof window === "undefined") return { completedNodes: [] }

    const key = `skillsmap_${slug}_progress`
    const stored = localStorage.getItem(key)
    if (stored) {
        try {
            return JSON.parse(stored)
        } catch {
            return { completedNodes: [] }
        }
    }
    return { completedNodes: [] }
}

/**
 * Mark a node as complete (localStorage)
 */
export function markNodeComplete(slug: string, nodeId: string): void {
    if (typeof window === "undefined") return

    const progress = getLocalProgress(slug)
    if (!progress.completedNodes.includes(nodeId)) {
        progress.completedNodes.push(nodeId)
        localStorage.setItem(`skillsmap_${slug}_progress`, JSON.stringify(progress))
    }
}

/**
 * Check if a node is complete
 */
export function isNodeComplete(slug: string, nodeId: string): boolean {
    const progress = getLocalProgress(slug)
    return progress.completedNodes.includes(nodeId)
}
