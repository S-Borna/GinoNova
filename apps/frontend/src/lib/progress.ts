/**
 * Progress API Client
 * Phase 5.0: Progress Engine Foundation with standardized error handling
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

// Types
export type ProgressStatus = "not_started" | "in_progress" | "completed"
export type TargetType = "module" | "task" | "studyflow"

// Types matching backend schemas
export interface ProgressPublic {
    id: string
    user_id: string
    module_id: string | null
    task_id: string | null
    studyflow_id: string | null
    status: ProgressStatus
    progress: number
    created_at: string
    updated_at: string
}

export interface ProgressCreate {
    user_id: string
    module_id?: string | null
    task_id?: string | null
    studyflow_id?: string | null
    progress?: number
}

export interface ProgressUpdate {
    progress?: number
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

// Helper functions
export function getTargetType(progress: ProgressPublic): TargetType {
    if (progress.module_id) return "module"
    if (progress.task_id) return "task"
    if (progress.studyflow_id) return "studyflow"
    return "module" // fallback
}

export function getTargetId(progress: ProgressPublic): string | null {
    return progress.module_id || progress.task_id || progress.studyflow_id
}

export function mapStatusToColor(status: ProgressStatus): string {
    switch (status) {
        case "completed":
            return "bg-green-100 text-green-800"
        case "in_progress":
            return "bg-yellow-100 text-yellow-800"
        case "not_started":
        default:
            return "bg-gray-100 text-gray-800"
    }
}

export function mapStatusToLabel(status: ProgressStatus): string {
    switch (status) {
        case "completed":
            return "Completed"
        case "in_progress":
            return "In Progress"
        case "not_started":
        default:
            return "Not Started"
    }
}

export function mapTargetTypeToColor(targetType: TargetType): string {
    switch (targetType) {
        case "module":
            return "bg-blue-100 text-blue-800"
        case "task":
            return "bg-purple-100 text-purple-800"
        case "studyflow":
            return "bg-indigo-100 text-indigo-800"
        default:
            return "bg-gray-100 text-gray-800"
    }
}

export function mapTargetTypeToLabel(targetType: TargetType): string {
    switch (targetType) {
        case "module":
            return "Module"
        case "task":
            return "Task"
        case "studyflow":
            return "Studyflow"
        default:
            return "Unknown"
    }
}

export function getTargetLink(progress: ProgressPublic): string {
    const targetType = getTargetType(progress)
    const targetId = getTargetId(progress)

    if (!targetId) return "#"

    switch (targetType) {
        case "module":
            return `/modules/${targetId}`
        case "task":
            return `/tasks/${targetId}`
        case "studyflow":
            return `/studyflow/${targetId}`
        default:
            return "#"
    }
}

/**
 * Get all progress records for a specific user
 */
export async function getUserProgress(userId: string): Promise<ApiResult<ProgressPublic[]>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/progress/user/${userId}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch progress" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch progress" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Get a single progress record by ID
 */
export async function getProgress(id: string): Promise<ApiResult<ProgressPublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/progress/${id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch progress" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch progress" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Create a new progress record
 */
export async function createProgress(data: ProgressCreate): Promise<ApiResult<ProgressPublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/progress/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to create progress" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to create progress" }
        }

        const responseData = await res.json()
        return { ok: true, data: responseData }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Update an existing progress record
 */
export async function updateProgress(id: string, data: ProgressUpdate): Promise<ApiResult<ProgressPublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/progress/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to update progress" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to update progress" }
        }

        const responseData = await res.json()
        return { ok: true, data: responseData }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}
