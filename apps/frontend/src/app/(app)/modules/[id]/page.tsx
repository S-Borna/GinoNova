"use client"

/**
 * ============================================================================
 * DYNAMIC MODULE PAGE — Uses Shared Module Component
 * ============================================================================
 *
 * This page handles dynamic module slugs via /modules/[id]
 * All module pages use the SAME SharedModulePage component.
 * Data is fetched from backend API: /api/modules/full/{slug}
 * 
 * Single source of truth: Backend
 * Single design: SharedModulePage
 *
 * @phase ARCHITECTURE-UNIFICATION
 */

import { useParams } from "next/navigation"
import { SharedModulePage } from "@/components/modules/SharedModulePage"

export default function ModuleDetailPage() {
    const params = useParams()
    const slug = params?.id as string

    return (
        <SharedModulePage
            slug={slug}
            backHref="/modules"
            backLabel="Tillbaka till Camp DevOps"
        />
    )
}
