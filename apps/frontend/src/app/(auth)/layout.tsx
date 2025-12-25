/**
 * ============================================================================
 * AUTH LAYOUT — Centered Premium Authentication Layout
 * ============================================================================
 *
 * Clean, centered authentication layout with cosmic background.
 * No split screen - just beautiful focused auth forms.
 *
 * @phase MILESTONE-2.0 - Premium Auth UI
 */

import { AuthProvider } from "@/components/auth"

export default function AuthLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <AuthProvider>
            <div className="min-h-screen flex items-center justify-center bg-[#030308] relative overflow-hidden">
                {/* Cosmic background effects */}
                <div className="absolute inset-0">
                    {/* Central cosmic glow */}
                    <div
                        className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] rounded-full"
                        style={{
                            background: "radial-gradient(circle, rgba(139,92,246,0.25) 0%, rgba(168,85,247,0.1) 40%, transparent 70%)",
                            filter: "blur(80px)",
                        }}
                    />
                    {/* Secondary glow */}
                    <div
                        className="absolute top-0 right-0 w-[600px] h-[600px] rounded-full"
                        style={{
                            background: "radial-gradient(circle, rgba(236,72,153,0.15) 0%, transparent 60%)",
                            filter: "blur(100px)",
                        }}
                    />
                    <div
                        className="absolute bottom-0 left-0 w-[500px] h-[500px] rounded-full"
                        style={{
                            background: "radial-gradient(circle, rgba(6,182,212,0.12) 0%, transparent 60%)",
                            filter: "blur(90px)",
                        }}
                    />
                    {/* Grid overlay */}
                    <div
                        className="absolute inset-0 opacity-[0.015]"
                        style={{
                            backgroundImage: `
                                linear-gradient(rgba(139,92,246,0.5) 1px, transparent 1px),
                                linear-gradient(90deg, rgba(139,92,246,0.5) 1px, transparent 1px)
                            `,
                            backgroundSize: '60px 60px'
                        }}
                    />
                </div>

                {/* Auth form container */}
                <div className="relative z-10 w-full max-w-md mx-4 p-8">
                    {children}
                </div>
            </div>
        </AuthProvider>
    )
}
