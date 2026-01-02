"use client"

/**
 * ============================================================================
 * SKILLSMAP DETAIL PAGE — USES SHARED MODULE COMPONENT
 * ============================================================================
 *
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

export default function SkillsMapDetailPage() {
    const params = useParams()
    const slug = params?.slug as string

    return (
        <SharedModulePage
            slug={slug}
            backHref="/skillsmaps"
            backLabel="Tillbaka till SkillsMaps"
        />
    )
}
