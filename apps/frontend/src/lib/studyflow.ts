/**
 * Studyflow API Client
 * Phase 4.0: Studyflow Foundation with standardized error handling
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

// Types matching backend schemas
export interface StudyflowPublic {
    id: string
    module_id: string
    title: string
    description: string | null
    order: number
    is_active: boolean
    created_at: string
    updated_at: string
}

export interface StudyflowCreate {
    module_id: string
    title: string
    description?: string | null
    order?: number
}

export interface StudyflowUpdate {
    title?: string
    description?: string | null
    order?: number
    is_active?: boolean
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
export const STUDYFLOW_TITLE_MIN = 3
export const STUDYFLOW_TITLE_MAX = 100
export const STUDYFLOW_DESC_MAX = 500

export function validateStudyflowTitle(title: string): { valid: boolean; error?: string } {
    const trimmed = title.trim()
    if (!trimmed) {
        return { valid: false, error: "Title is required" }
    }
    if (trimmed.length < STUDYFLOW_TITLE_MIN) {
        return { valid: false, error: `Title must be at least ${STUDYFLOW_TITLE_MIN} characters` }
    }
    if (trimmed.length > STUDYFLOW_TITLE_MAX) {
        return { valid: false, error: `Title must be at most ${STUDYFLOW_TITLE_MAX} characters` }
    }
    return { valid: true }
}

export function validateStudyflowDescription(desc: string | null | undefined): { valid: boolean; error?: string } {
    if (!desc) return { valid: true }
    if (desc.length > STUDYFLOW_DESC_MAX) {
        return { valid: false, error: `Description must be at most ${STUDYFLOW_DESC_MAX} characters` }
    }
    return { valid: true }
}

export function validateStudyflowOrder(order: number): { valid: boolean; error?: string } {
    if (!Number.isInteger(order) || order <= 0) {
        return { valid: false, error: "Order must be a positive integer" }
    }
    return { valid: true }
}

export function truncateText(text: string | null, maxLength: number): string {
    if (!text) return ""
    if (text.length <= maxLength) return text
    return text.slice(0, maxLength - 3) + "..."
}

/**
 * Get all studyflows
 */
export async function getStudyflows(): Promise<ApiResult<StudyflowPublic[]>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/studyflow/`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch studyflows" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch studyflows" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Get all studyflows for a specific module
 */
export async function getStudyflowsByModule(moduleId: string): Promise<ApiResult<StudyflowPublic[]>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/studyflow/module/${moduleId}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch studyflows" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch studyflows" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Get a single studyflow by ID
 */
export async function getStudyflow(id: string): Promise<ApiResult<StudyflowPublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/studyflow/${id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch studyflow" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch studyflow" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Create a new studyflow
 */
export async function createStudyflow(data: StudyflowCreate): Promise<ApiResult<StudyflowPublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/studyflow/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to create studyflow" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to create studyflow" }
        }

        const responseData = await res.json()
        return { ok: true, data: responseData }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Update an existing studyflow
 */
export async function updateStudyflow(id: string, data: StudyflowUpdate): Promise<ApiResult<StudyflowPublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/studyflow/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to update studyflow" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to update studyflow" }
        }

        const responseData = await res.json()
        return { ok: true, data: responseData }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Delete a studyflow
 */
export async function deleteStudyflow(id: string): Promise<ApiResult<void>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/studyflow/${id}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to delete studyflow" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to delete studyflow" }
        }

        return { ok: true, data: undefined }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}
