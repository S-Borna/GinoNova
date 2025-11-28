"use client"

import { useEffect } from "react"
import { useRouter } from "next/navigation"

/**
 * Redirect /register to /signup for consistency
 */
export default function RegisterPage() {
    const router = useRouter()

    useEffect(() => {
        router.replace("/signup")
    }, [router])

    return (
        <div className="min-h-screen flex items-center justify-center">
            <div className="animate-pulse text-neutral-500">
                Redirecting...
            </div>
        </div>
    )
}
