"use client"

/**
 * Protected Route HOC
 * Phase 1.3: Redirect to /login if no user
 */

import { useEffect } from "react"
import { useRouter } from "next/navigation"
import { useAuth } from "./AuthProvider"

interface ProtectedProps {
    children: React.ReactNode
}

export function Protected({ children }: ProtectedProps) {
    const { user, loading } = useAuth()
    const router = useRouter()

    useEffect(() => {
        if (!loading && !user) {
            router.push("/login")
        }
    }, [user, loading, router])

    // Show loading state
    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-screen">
                <div className="text-lg">Loading...</div>
            </div>
        )
    }

    // Don't render children if no user
    if (!user) {
        return null
    }

    return <>{children}</>
}
