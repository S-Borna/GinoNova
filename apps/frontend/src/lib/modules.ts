/**
 * Modules API Client
 * Phase 2.0: Modules Foundation
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
}

export interface ModuleUpdate {
    name?: string
    description?: string | null
    is_active?: boolean
}

export interface ApiError {
    detail: string
}

/**
 * Get all modules
 */
export async function getModules(): Promise<ModulePublic[]> {
    const res = await fetch(`${API_BASE_URL}/api/modules/`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    })

    if (!res.ok) {
        const error: ApiError = await res.json()
        throw new Error(error.detail || "Failed to fetch modules")
    }

    return res.json()
}

/**
 * Get a single module by ID
 */
export async function getModule(id: string): Promise<ModulePublic> {
    const res = await fetch(`${API_BASE_URL}/api/modules/${id}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    })

    if (!res.ok) {
        const error: ApiError = await res.json()
        throw new Error(error.detail || "Failed to fetch module")
    }

    return res.json()
}

/**
 * Create a new module
 */
export async function createModule(data: ModuleCreate): Promise<ModulePublic> {
    const res = await fetch(`${API_BASE_URL}/api/modules/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })

    if (!res.ok) {
        const error: ApiError = await res.json()
        throw new Error(error.detail || "Failed to create module")
    }

    return res.json()
}

/**
 * Update an existing module
 */
export async function updateModule(id: string, data: ModuleUpdate): Promise<ModulePublic> {
    const res = await fetch(`${API_BASE_URL}/api/modules/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })

    if (!res.ok) {
        const error: ApiError = await res.json()
        throw new Error(error.detail || "Failed to update module")
    }

    return res.json()
}

/**
 * Delete a module
 */
export async function deleteModule(id: string): Promise<void> {
    const res = await fetch(`${API_BASE_URL}/api/modules/${id}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
    })

    if (!res.ok) {
        const error: ApiError = await res.json()
        throw new Error(error.detail || "Failed to delete module")
    }
}
