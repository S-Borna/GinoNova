/**
 * ============================================================================
 * AUTH LAYOUT — Split Screen Authentication Layout
 * ============================================================================
 *
 * Premium authentication layout with branding panel on left
 * and auth form on right. Fully responsive.
 *
 * @phase A.2 - Authentication UI
 */

import { AuthBranding } from "@/components/auth/AuthBranding"

export default function AuthLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <div className="min-h-screen flex">
            {/* Left: Branding panel (hidden on mobile) */}
            <AuthBranding className="w-1/2 min-h-screen" />

            {/* Right: Auth form */}
            <div className="w-full lg:w-1/2 min-h-screen flex items-center justify-center p-6 sm:p-12 bg-white dark:bg-neutral-950">
                <div className="w-full max-w-md">
                    {children}
                </div>
            </div>
        </div>
    )
}
