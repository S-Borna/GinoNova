"use client"

/**
 * Route-level error boundary for the App Router.
 * Keeps markup minimal to avoid SSR issues during static generation.
 */

export default function Error({
    error,
    reset,
}: {
    error: Error & { digest?: string }
    reset: () => void
}) {
    return (
        <div
            style={{
                minHeight: "100vh",
                display: "flex",
                flexDirection: "column",
                gap: "1rem",
                alignItems: "center",
                justifyContent: "center",
                fontFamily: "system-ui, -apple-system, sans-serif",
                padding: "2rem",
            }}
        >
            <h1 style={{ fontSize: "2rem", fontWeight: 700 }}>
                Something went wrong
            </h1>
            <p style={{ color: "#525252", maxWidth: 360, textAlign: "center" }}>
                {error?.message || "An unexpected error occurred while rendering this page."}
            </p>
            <div style={{ display: "flex", gap: "0.75rem" }}>
                <button
                    onClick={() => reset()}
                    style={{
                        padding: "0.75rem 1.5rem",
                        borderRadius: "0.75rem",
                        border: "none",
                        cursor: "pointer",
                        backgroundColor: "#6366f1",
                        color: "white",
                        fontWeight: 600,
                    }}
                >
                    Try again
                </button>
                {/* eslint-disable-next-line @next/next/no-html-link-for-pages */}
                <a
                    href="/"
                    style={{
                        padding: "0.75rem 1.5rem",
                        borderRadius: "0.75rem",
                        border: "1px solid #d4d4d4",
                        textDecoration: "none",
                        color: "#171717",
                        fontWeight: 600,
                    }}
                >
                    Go home
                </a>
            </div>
        </div>
    )
}
