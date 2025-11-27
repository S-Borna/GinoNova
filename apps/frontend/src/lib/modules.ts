/**
 * Modules API Client
 * Phase 2.1: Enhanced with standardized error handling
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

// Types matching backend schemas
export interface ModulePublic {
    id: string
    name: string
    description: string | null
    is_active: boolean
    created_at: string
    updated_at: string
}

export interface ModuleCreate {
    name: string
    description?: string | null
    is_active?: boolean
}

export interface ModuleUpdate {
    name?: string
    description?: string | null
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

// Validation
export const MODULE_NAME_MIN = 2
export const MODULE_NAME_MAX = 50
export const MODULE_DESC_MAX = 300

export function validateModuleName(name: string): { valid: boolean; error?: string } {
    const trimmed = name.trim()
    if (!trimmed) {
        return { valid: false, error: "Name is required" }
    }
    if (trimmed.length < MODULE_NAME_MIN) {
        return { valid: false, error: `Name must be at least ${MODULE_NAME_MIN} characters` }
    }
    if (trimmed.length > MODULE_NAME_MAX) {
        return { valid: false, error: `Name must be at most ${MODULE_NAME_MAX} characters` }
    }
    return { valid: true }
}

export function validateModuleDescription(desc: string | null | undefined): { valid: boolean; error?: string } {
    if (!desc) return { valid: true }
    if (desc.length > MODULE_DESC_MAX) {
        return { valid: false, error: `Description must be at most ${MODULE_DESC_MAX} characters` }
    }
    return { valid: true }
}

export function truncateText(text: string | null, maxLength: number): string {
    if (!text) return ""
    if (text.length <= maxLength) return text
    return text.slice(0, maxLength - 3) + "..."
}

/**
 * Get all modules
 */
export async function getModules(): Promise<ApiResult<ModulePublic[]>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/modules/`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch modules" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch modules" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Get a single module by ID
 */
export async function getModule(id: string): Promise<ApiResult<ModulePublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/modules/${id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch module" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch module" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Create a new module
 */
export async function createModule(data: ModuleCreate): Promise<ApiResult<ModulePublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/modules/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to create module" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to create module" }
        }

        const responseData = await res.json()
        return { ok: true, data: responseData }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Update an existing module
 */
export async function updateModule(id: string, data: ModuleUpdate): Promise<ApiResult<ModulePublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/modules/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to update module" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to update module" }
        }

        const responseData = await res.json()
        return { ok: true, data: responseData }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Delete a module
 */
export async function deleteModule(id: string): Promise<ApiResult<void>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/modules/${id}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to delete module" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to delete module" }
        }

        return { ok: true, data: undefined }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}
