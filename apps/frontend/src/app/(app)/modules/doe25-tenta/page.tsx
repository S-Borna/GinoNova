"use client"

/**
 * ============================================================================
 * DOE25 TENTA MODULE PAGE — Uses Shared Module Component
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

import { SharedModulePage } from "@/components/modules/SharedModulePage"

export default function DOE25TentaPage() {
    return (
        <SharedModulePage
            slug="doe25-tenta"
            backHref="/modules"
            backLabel="Tillbaka till Camp DevOps"
        />
    )
}
