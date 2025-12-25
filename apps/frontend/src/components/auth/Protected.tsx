"use client"

/**
 * Protected Route Component
 * MILESTONE 2.0: Now a SOFT gate - shows content but prompts for login
 * for premium features only (AI Quiz, saved progress, etc.)
 *
 * Use this ONLY for truly premium features, not for content access.
 */

import { useEffect, useState } from "react"
import { useRouter } from "next/navigation"
import { useAuth } from "./AuthProvider"

interface ProtectedProps {
    children: React.ReactNode
    /** If true, shows a soft prompt instead of blocking */
    softPrompt?: boolean
    /** Feature name for the prompt message */
    featureName?: string
}

export function Protected({ children, softPrompt = false, featureName = "this feature" }: ProtectedProps) {
    const { user, loading } = useAuth()
    const router = useRouter()
    const [showPrompt, setShowPrompt] = useState(false)

    useEffect(() => {
        if (!loading && !user) {
            if (softPrompt) {
                // Show soft prompt instead of redirect
                setShowPrompt(true)
            } else {
                // Only redirect for hard-protected features
                router.push("/login")
            }
        }
    }, [user, loading, router, softPrompt])

    // Show loading state
    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-[200px]">
                <div className="text-lg text-zinc-400">Loading...</div>
            </div>
        )
    }

    // Soft prompt mode - show upgrade modal
    if (showPrompt && softPrompt) {
        return (
            <div className="relative">
                {/* Blurred preview of content */}
                <div className="blur-sm pointer-events-none opacity-50">
                    {children}
                </div>

                {/* Upgrade prompt overlay */}
                <div className="absolute inset-0 flex items-center justify-center bg-zinc-950/80 backdrop-blur-sm rounded-xl">
                    <div className="text-center p-8 max-w-md">
                        <div className="text-4xl mb-4">🔐</div>
                        <h3 className="text-xl font-bold text-white mb-2">
                            Logga in för {featureName}
                        </h3>
                        <p className="text-zinc-400 mb-6">
                            Skapa ett gratis konto för att spara dina framsteg och
                            få tillgång till premium-funktioner.
                        </p>
                        <div className="flex gap-3 justify-center">
                            <button
                                onClick={() => router.push("/login")}
                                className="px-6 py-2 bg-purple-600 hover:bg-purple-500 text-white rounded-lg font-medium transition-colors"
                            >
                                Logga in gratis
                            </button>
                            <button
                                onClick={() => setShowPrompt(false)}
                                className="px-6 py-2 bg-zinc-800 hover:bg-zinc-700 text-white rounded-lg font-medium transition-colors"
                            >
                                Kanske senare
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

    // Hard block - don't render children if no user (will redirect)
    if (!user && !softPrompt) {
        return null
    }

    return <>{children}</>
}
