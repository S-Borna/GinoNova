"use client"

/**
 * AuthContext Provider
 * Phase 1.3: React context for authentication state
 */

import {
    createContext,
    useContext,
    useEffect,
    useState,
    useCallback,
    ReactNode,
} from "react"
import {
    UserPublic,
    login as authLogin,
    register as authRegister,
    getMe,
    logout as authLogout,
    getToken,
} from "@/lib/auth"

interface AuthContextType {
    user: UserPublic | null
    loading: boolean
    error: string | null
    login: (email: string, password: string) => Promise<void>
    register: (email: string, password: string, fullName?: string) => Promise<void>
    logout: () => void
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

interface AuthProviderProps {
    children: ReactNode
}

export function AuthProvider({ children }: AuthProviderProps) {
    const [user, setUser] = useState<UserPublic | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

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

    const login = useCallback(async (email: string, password: string) => {
        setError(null)
        setLoading(true)
        try {
            await authLogin(email, password)
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
                await authRegister(email, password, fullName)
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
            value={{ user, loading, error, login, register, logout }}
        >
            {children}
        </AuthContext.Provider>
    )
}

export function useAuth() {
    const context = useContext(AuthContext)
    if (context === undefined) {
        throw new Error("useAuth must be used within an AuthProvider")
    }
    return context
}
