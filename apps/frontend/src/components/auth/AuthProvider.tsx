"use client"

/**
 * AuthContext Provider
 * Phase 1.4: React context with error clearing on route change
 * Phase OAuth: Integration with NextAuth for social login
 */

import {
    createContext,
    useContext,
    useEffect,
    useState,
    useCallback,
    ReactNode,
} from "react"
import { usePathname } from "next/navigation"
import { useSession, signOut as nextAuthSignOut } from "next-auth/react"
import {
    UserPublic,
    login as authLogin,
    register as authRegister,
    getMe,
    logout as authLogout,
    getToken,
    storeToken,
    normalizeEmail,
} from "@/lib/auth"

interface AuthContextType {
    user: UserPublic | null
    loading: boolean
    error: string | null
    login: (email: string, password: string) => Promise<void>
    register: (email: string, password: string, fullName?: string) => Promise<void>
    logout: () => void
    clearError: () => void
    refreshUser: () => Promise<void>
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

interface AuthProviderProps {
    children: ReactNode
}

// DEV BYPASS: Skip auth in development mode
const DEV_BYPASS_AUTH = process.env.NODE_ENV === 'development' && process.env.NEXT_PUBLIC_DEV_BYPASS_AUTH === 'true'

// Mock user for dev bypass
const DEV_USER: UserPublic = {
    id: 'dev-user-12345' as unknown as `${string}-${string}-${string}-${string}-${string}`,
    email: 'dev@localhost',
    full_name: 'Dev User',
    is_active: true,
    is_admin: true,
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
}

export function AuthProvider({ children }: AuthProviderProps) {
    const [user, setUser] = useState<UserPublic | null>(DEV_BYPASS_AUTH ? DEV_USER : null)
    const [loading, setLoading] = useState(DEV_BYPASS_AUTH ? false : true)
    const [error, setError] = useState<string | null>(null)
    const pathname = usePathname()

    // NextAuth session for OAuth
    const { data: session, status: sessionStatus } = useSession()

    // Clear error on route change
    useEffect(() => {
        setError(null)
    }, [pathname])

    // Handle OAuth session from NextAuth
    useEffect(() => {
        // Skip if DEV_BYPASS is enabled
        if (DEV_BYPASS_AUTH) {
            console.log('[Auth] DEV BYPASS ENABLED - skipping authentication')
            return
        }

        const handleOAuthSession = async () => {
            if (sessionStatus === "loading") return

            // If we have a NextAuth session with backend token, use it
            if (session?.accessToken && session?.backendUser) {
                storeToken(session.accessToken)
                setUser({
                    id: session.backendUser.id as unknown as `${string}-${string}-${string}-${string}-${string}`,
                    email: session.backendUser.email,
                    full_name: session.backendUser.full_name,
                    is_active: true,
                    is_admin: session.backendUser.is_admin,
                    created_at: new Date().toISOString(),
                    updated_at: new Date().toISOString(),
                } as UserPublic)
                setLoading(false)
                return
            }

            // Otherwise, check for existing JWT token
            const token = getToken()
            if (!token) {
                setLoading(false)
                return
            }

            try {
                const userData = await getMe()
                setUser(userData)
            } catch (err) {
                // FIXED: Distinguish between auth errors and network errors
                const isNetworkError = err instanceof TypeError && err.message.includes('fetch')

                if (isNetworkError) {
                    // Network error - don't log out user, keep token for retry
                    console.warn('[Auth] Network error validating token - keeping session')
                    // User stays null but we don't remove token - they can retry
                } else {
                    // Token actually invalid (401/403) - clear it
                    console.warn('[Auth] Token invalid or expired - logging out')
                    setUser(null)
                    // Import removeToken if needed, or just leave user null
                }
            } finally {
                setLoading(false)
            }
        }

        handleOAuthSession()
    }, [session, sessionStatus])

    const clearError = useCallback(() => {
        setError(null)
    }, [])

    const refreshUser = useCallback(async () => {
        const token = getToken()
        if (!token) return
        try {
            const userData = await getMe()
            setUser(userData)
        } catch (err) {
            // FIXED: Only clear user on actual auth errors, not network issues
            const isNetworkError = err instanceof TypeError && err.message.includes('fetch')
            if (!isNetworkError) {
                setUser(null)
            } else {
                console.warn('[Auth] Network error during refresh - keeping session')
            }
        }
    }, [])

    // Heartbeat: Update last_activity_at for online status tracking
    useEffect(() => {
        if (!user) return

        // FIXED: Use environment variable consistently
        const API_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

        const heartbeat = async () => {
            // Try localStorage token first
            let token = getToken()

            // If no localStorage token, try to get from NextAuth session
            if (!token && session?.accessToken) {
                token = session.accessToken
                // Also store it in localStorage for other API calls
                storeToken(token)
            }

            if (!token) {
                console.warn('[Heartbeat] No token found in localStorage or session')
                return
            }

            try {
                // Call backend /me endpoint to update last_activity_at
                const response = await fetch(`${API_URL}/api/auth/me`, {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                })
                if (!response.ok) {
                    console.warn('[Heartbeat] Failed:', response.status)
                    // If 401, token is expired - try to refresh from session
                    if (response.status === 401 && session?.accessToken) {
                        storeToken(session.accessToken)
                    }
                }
            } catch (err) {
                console.warn('[Heartbeat] Error:', err)
            }
        }

        // Send heartbeat immediately on mount
        heartbeat()

        // Then every 1 minute for accurate online status
        const interval = setInterval(heartbeat, 60 * 1000)

        // Also send heartbeat when window regains focus
        const handleFocus = () => heartbeat()
        window.addEventListener('focus', handleFocus)

        // Send heartbeat on visibility change (tab becomes visible)
        const handleVisibility = () => {
            if (document.visibilityState === 'visible') {
                heartbeat()
            }
        }
        document.addEventListener('visibilitychange', handleVisibility)

        return () => {
            clearInterval(interval)
            window.removeEventListener('focus', handleFocus)
            document.removeEventListener('visibilitychange', handleVisibility)
        }
    }, [user])

    const login = useCallback(async (email: string, password: string) => {
        setError(null)
        setLoading(true)
        try {
            // Normalize email before sending
            await authLogin(normalizeEmail(email), password)
            const userData = await getMe()
            setUser(userData)
        } catch (err) {
            const message = err instanceof Error ? err.message : "Login failed"
            setError(message)
            throw err
        } finally {
            setLoading(false)
        }
    }, [])

    const register = useCallback(
        async (email: string, password: string, fullName?: string) => {
            setError(null)
            setLoading(true)
            try {
                // Normalize email before sending
                await authRegister(normalizeEmail(email), password, fullName)
                const userData = await getMe()
                setUser(userData)
            } catch (err) {
                const message = err instanceof Error ? err.message : "Registration failed"
                setError(message)
                throw err
            } finally {
                setLoading(false)
            }
        },
        []
    )

    const logout = useCallback(async () => {
        // Notify backend and clear local auth
        await authLogout()
        setUser(null)
        setError(null)

        // Also sign out of NextAuth if using OAuth
        if (session) {
            await nextAuthSignOut({ redirect: false })
        }
    }, [session])

    return (
        <AuthContext.Provider
            value={{ user, loading, error, login, register, logout, clearError, refreshUser }}
        >
            {children}
        </AuthContext.Provider>
    )
}

// SSR-safe default values
const ssrSafeDefaults: AuthContextType = {
    user: null,
    loading: true,
    error: null,
    login: async () => { throw new Error("AuthProvider not available") },
    register: async () => { throw new Error("AuthProvider not available") },
    logout: () => { },
    clearError: () => { },
    refreshUser: async () => { },
}

export function useAuth() {
    const context = useContext(AuthContext)
    // Return safe defaults during SSR to prevent build errors
    if (context === undefined) {
        // Check if we're on the server
        if (typeof window === 'undefined') {
            return ssrSafeDefaults
        }
        throw new Error("useAuth must be used within an AuthProvider")
    }
    return context
}
