"use client"

/**
 * AuthContext Provider
 * Phase 1.4: React context with error clearing on route change
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
import {
    UserPublic,
    login as authLogin,
    register as authRegister,
    getMe,
    logout as authLogout,
    getToken,
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

export function AuthProvider({ children }: AuthProviderProps) {
    const [user, setUser] = useState<UserPublic | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const pathname = usePathname()

    // Clear error on route change
    useEffect(() => {
        setError(null)
    }, [pathname])

    // Load user on mount if token exists
    useEffect(() => {
        const loadUser = async () => {
            const token = getToken()
            if (!token) {
                setLoading(false)
                return
            }

            try {
                const userData = await getMe()
                setUser(userData)
            } catch {
                // Token invalid or expired
                setUser(null)
            } finally {
                setLoading(false)
            }
        }

        loadUser()
    }, [])

    const clearError = useCallback(() => {
        setError(null)
    }, [])

    const refreshUser = useCallback(async () => {
        const token = getToken()
        if (!token) return
        try {
            const userData = await getMe()
            setUser(userData)
        } catch {
            // Token invalid or expired
            setUser(null)
        }
    }, [])

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

    const logout = useCallback(() => {
        authLogout()
        setUser(null)
        setError(null)
    }, [])

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
