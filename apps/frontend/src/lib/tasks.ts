/**
 * Tasks API Client
 * Phase 3.0: Tasks Foundation with standardized error handling
 * Phase 4.0: Added task_tier and parent_task_id for related tasks (fördjupning)
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

// Difficulty type
export type DifficultyLevel = "easy" | "medium" | "hard"

// Task tier type (v4 feature)
export type TaskTier = "standard" | "advanced" | "deep_dive"

// Types matching backend schemas
export interface TaskPublic {
    id: string
    module_id: string
    title: string
    description: string | null
    content: string | null
    order_index: number
    difficulty: DifficultyLevel
    estimated_minutes: number
    xp_reward: number
    is_active: boolean
    task_tier: TaskTier       // v4: standard, advanced, or deep_dive
    parent_task_id: string | null  // v4: links to parent task for fördjupning
    created_at: string
    updated_at: string
}

export interface TaskCreate {
    module_id: string
    title: string
    description?: string | null
    content?: string | null
    order_index?: number
    difficulty?: DifficultyLevel
    estimated_minutes?: number
    xp_reward?: number
    task_tier?: TaskTier        // v4: default "standard"
    parent_task_id?: string | null  // v4: for linking fördjupning
}

export interface TaskUpdate {
    title?: string
    description?: string | null
    content?: string | null
    order_index?: number
    difficulty?: DifficultyLevel
    estimated_minutes?: number
    xp_reward?: number
    is_active?: boolean
    task_tier?: TaskTier        // v4
    parent_task_id?: string | null  // v4
}

// Standardized API response types
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

// Validation constants
export const TASK_TITLE_MIN = 3
export const TASK_TITLE_MAX = 100
export const TASK_DESC_MAX = 500
export const DIFFICULTY_LEVELS: DifficultyLevel[] = ["easy", "medium", "hard"]

export function validateTaskTitle(title: string): { valid: boolean; error?: string } {
    const trimmed = title.trim()
    if (!trimmed) {
        return { valid: false, error: "Title is required" }
    }
    if (trimmed.length < TASK_TITLE_MIN) {
        return { valid: false, error: `Title must be at least ${TASK_TITLE_MIN} characters` }
    }
    if (trimmed.length > TASK_TITLE_MAX) {
        return { valid: false, error: `Title must be at most ${TASK_TITLE_MAX} characters` }
    }
    return { valid: true }
}

export function validateTaskDescription(desc: string | null | undefined): { valid: boolean; error?: string } {
    if (!desc) return { valid: true }
    if (desc.length > TASK_DESC_MAX) {
        return { valid: false, error: `Description must be at most ${TASK_DESC_MAX} characters` }
    }
    return { valid: true }
}

export function truncateText(text: string | null, maxLength: number): string {
    if (!text) return ""
    if (text.length <= maxLength) return text
    return text.slice(0, maxLength - 3) + "..."
}

export function getDifficultyColor(difficulty: DifficultyLevel): string {
    switch (difficulty) {
        case "easy":
            return "bg-green-100 text-green-800"
        case "medium":
            return "bg-yellow-100 text-yellow-800"
        case "hard":
            return "bg-red-100 text-red-800"
        default:
            return "bg-gray-100 text-gray-800"
    }
}

/**
 * Get all tasks
 */
export async function getTasks(): Promise<ApiResult<TaskPublic[]>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/tasks/`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch tasks" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch tasks" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Get all tasks for a specific module
 */
export async function getTasksForModule(moduleId: string): Promise<ApiResult<TaskPublic[]>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/tasks/module/${moduleId}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch tasks" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch tasks" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Get a single task by ID
 */
export async function getTask(id: string): Promise<ApiResult<TaskPublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/tasks/${id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch task" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch task" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Create a new task
 */
export async function createTask(data: TaskCreate): Promise<ApiResult<TaskPublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/tasks/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to create task" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to create task" }
        }

        const responseData = await res.json()
        return { ok: true, data: responseData }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Update an existing task
 */
export async function updateTask(id: string, data: TaskUpdate): Promise<ApiResult<TaskPublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/tasks/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to update task" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to update task" }
        }

        const responseData = await res.json()
        return { ok: true, data: responseData }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Delete a task
 */
export async function deleteTask(id: string): Promise<ApiResult<void>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/tasks/${id}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to delete task" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to delete task" }
        }

        return { ok: true, data: undefined }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Get related tasks (fördjupning) for a task
 * Returns advanced/deep_dive tasks linked to the specified parent task
 */
export async function getRelatedTasks(taskId: string): Promise<ApiResult<TaskPublic[]>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/tasks/${taskId}/related`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch related tasks" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch related tasks" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Get task tier display info
 */
export function getTaskTierInfo(tier: TaskTier): { label: string; color: string; icon: string } {
    switch (tier) {
        case "advanced":
            return { label: "Fördjupning", color: "bg-purple-100 text-purple-800", icon: "🚀" }
        case "deep_dive":
            return { label: "Deep Dive", color: "bg-amber-100 text-amber-800", icon: "🎓" }
        default:
            return { label: "Standard", color: "bg-blue-100 text-blue-800", icon: "📘" }
    }
}
