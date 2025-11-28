/**
 * ============================================================================
 * API CLIENT — Centralized HTTP Client
 * ============================================================================
 *
 * Base API client with auth token handling, error handling, and typing.
 *
 * @phase A.3 - App Shell & Routing
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

/* ============================================================================
   TYPES
   ============================================================================ */

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

interface RequestOptions extends RequestInit {
    skipAuth?: boolean
}

/* ============================================================================
   TOKEN MANAGEMENT
   ============================================================================ */

function getAuthToken(): string | null {
    if (typeof window === "undefined") return null
    return localStorage.getItem("auth_token")
}

/* ============================================================================
   BASE REQUEST FUNCTION
   ============================================================================ */

export async function apiRequest<T>(
    endpoint: string,
    options: RequestOptions = {}
): Promise<ApiResult<T>> {
    const { skipAuth = false, ...fetchOptions } = options

    const headers: HeadersInit = {
        "Content-Type": "application/json",
        ...(fetchOptions.headers || {}),
    }

    // Add auth token if available and not skipped
    if (!skipAuth) {
        const token = getAuthToken()
        if (token) {
            ; (headers as Record<string, string>)["Authorization"] = `Bearer ${token}`
        }
    }

    try {
        const res = await fetch(`${API_BASE_URL}${endpoint}`, {
            ...fetchOptions,
            headers,
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Request failed" }))
            return {
                ok: false,
                status: res.status,
                message: error.detail || error.message || "Request failed",
            }
        }

        // Handle no-content responses
        if (res.status === 204) {
            return { ok: true, data: undefined as T }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return {
            ok: false,
            status: 0,
            message: error instanceof Error ? error.message : "Network error",
        }
    }
}

/* ============================================================================
   CONVENIENCE METHODS
   ============================================================================ */

export const api = {
    get: <T>(endpoint: string, options?: RequestOptions) =>
        apiRequest<T>(endpoint, { method: "GET", ...options }),

    post: <T>(endpoint: string, body?: unknown, options?: RequestOptions) =>
        apiRequest<T>(endpoint, {
            method: "POST",
            body: body ? JSON.stringify(body) : undefined,
            ...options,
        }),

    put: <T>(endpoint: string, body?: unknown, options?: RequestOptions) =>
        apiRequest<T>(endpoint, {
            method: "PUT",
            body: body ? JSON.stringify(body) : undefined,
            ...options,
        }),

    patch: <T>(endpoint: string, body?: unknown, options?: RequestOptions) =>
        apiRequest<T>(endpoint, {
            method: "PATCH",
            body: body ? JSON.stringify(body) : undefined,
            ...options,
        }),

    delete: <T>(endpoint: string, options?: RequestOptions) =>
        apiRequest<T>(endpoint, { method: "DELETE", ...options }),
}

export { API_BASE_URL }
