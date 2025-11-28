/**
 * Auth Client Module
 * Phase 1.4: JWT authentication with email normalization and validation
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
const TOKEN_KEY = "auth_token"

// Validation constants
export const PASSWORD_MIN_LENGTH = 8
export const PASSWORD_MAX_LENGTH = 128

// Types matching backend schemas
export interface UserPublic {
    id: string
    email: string
    full_name: string | null
    is_active: boolean
    is_admin: boolean
    created_at: string
    updated_at: string
}

export interface TokenResponse {
    access_token: string
    token_type: string
}

export interface AuthError {
    detail: string
}

export interface ValidationResult {
    valid: boolean
    error?: string
}

/**
 * Normalize email to lowercase and trim whitespace
 */
export function normalizeEmail(email: string): string {
    return email.toLowerCase().trim()
}

/**
 * Validate email format
 */
export function validateEmail(email: string): ValidationResult {
    const normalized = normalizeEmail(email)
    if (!normalized) {
        return { valid: false, error: "Email is required" }
    }
    // Basic email regex
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(normalized)) {
        return { valid: false, error: "Invalid email format" }
    }
    return { valid: true }
}

/**
 * Validate password strength
 */
export function validatePassword(password: string): ValidationResult {
    if (!password) {
        return { valid: false, error: "Password is required" }
    }
    if (password.length < PASSWORD_MIN_LENGTH) {
        return { valid: false, error: `Password must be at least ${PASSWORD_MIN_LENGTH} characters` }
    }
    if (password.length > PASSWORD_MAX_LENGTH) {
        return { valid: false, error: `Password must be at most ${PASSWORD_MAX_LENGTH} characters` }
    }
    return { valid: true }
}

/**
 * Store JWT token in localStorage
 */
export function storeToken(token: string): void {
    if (typeof window !== "undefined") {
        localStorage.setItem(TOKEN_KEY, token)
    }
}

/**
 * Get JWT token from localStorage
 */
export function getToken(): string | null {
    if (typeof window !== "undefined") {
        return localStorage.getItem(TOKEN_KEY)
    }
    return null
}

/**
 * Remove JWT token from localStorage
 */
export function removeToken(): void {
    if (typeof window !== "undefined") {
        localStorage.removeItem(TOKEN_KEY)
    }
}

/**
 * Register a new user
 */
export async function register(
    email: string,
    password: string,
    fullName?: string
): Promise<TokenResponse> {
    // Normalize email before sending
    const normalizedEmail = normalizeEmail(email)

    const res = await fetch(`${API_BASE_URL}/api/auth/register`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            email: normalizedEmail,
            password,
            full_name: fullName || null,
        }),
    })

    if (!res.ok) {
        const error: AuthError = await res.json()
        throw new Error(error.detail || "Registration failed")
    }

    const data: TokenResponse = await res.json()
    storeToken(data.access_token)
    return data
}

/**
 * Login with email and password
 */
export async function login(
    email: string,
    password: string
): Promise<TokenResponse> {
    // Normalize email before sending
    const normalizedEmail = normalizeEmail(email)

    const res = await fetch(`${API_BASE_URL}/api/auth/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ email: normalizedEmail, password }),
    })

    if (!res.ok) {
        const error: AuthError = await res.json()
        throw new Error(error.detail || "Login failed")
    }

    const data: TokenResponse = await res.json()
    storeToken(data.access_token)
    return data
}

/**
 * Get current user info
 */
export async function getMe(): Promise<UserPublic> {
    const token = getToken()

    if (!token) {
        throw new Error("No auth token")
    }

    const res = await fetch(`${API_BASE_URL}/api/auth/me`, {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    })

    if (!res.ok) {
        if (res.status === 401) {
            removeToken()
            throw new Error("Session expired")
        }
        const error: AuthError = await res.json()
        throw new Error(error.detail || "Failed to get user info")
    }

    return res.json()
}

/**
 * Logout - remove token
 */
export function logout(): void {
    removeToken()
}

/**
 * Reset all user progress
 */
export async function resetProgress(): Promise<{ ok: boolean; deleted_records: number }> {
    const token = getToken()

    if (!token) {
        throw new Error("No auth token")
    }

    const res = await fetch(`${API_BASE_URL}/api/auth/me/reset-progress`, {
        method: "POST",
        headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
        },
    })

    if (!res.ok) {
        if (res.status === 401) {
            removeToken()
            throw new Error("Session expired")
        }
        const error: AuthError = await res.json()
        throw new Error(error.detail || "Failed to reset progress")
    }

    return res.json()
}
