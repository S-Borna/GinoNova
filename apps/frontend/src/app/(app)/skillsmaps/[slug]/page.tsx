"use client"

/**
 * ============================================================================
 * SKILLSMAP DETAIL PAGE — REDIRECTS TO CAMP DEVOPS
 * ============================================================================
 *
 * SkillsMaps and Camp DevOps share the SAME modules with SAME design.
 * This page redirects to the Camp DevOps module page.
 *
 * @phase DESIGN-UNIFICATION
 */

import { useEffect } from "react"
import { useParams, useRouter } from "next/navigation"

export default function SkillsMapDetailPage() {
    const params = useParams()
    const router = useRouter()
    const slug = params?.slug as string

    useEffect(() => {
        if (slug) {
            // Redirect to Camp DevOps module page - same content, same design
            router.replace(`/modules/${slug}`)
        }
    }, [slug, router])

    // Loading state while redirecting
    return (
        <div className="min-h-screen bg-[#05050a] flex items-center justify-center">
            <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-purple-500" />
        </div>
    )
}
