"use client"

/**
 * Global Error Boundary for Next.js App Router
 *
 * Handles errors that occur during rendering.
 * Uses inline styles only - no external dependencies that could cause SSR issues.
 */

export default function GlobalError({
    error,
    reset,
}: {
    error: Error & { digest?: string }
    reset: () => void
}) {
    return (
        <html lang="en">
            <body
                style={{
                    minHeight: "100vh",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    backgroundColor: "#0a0a0a",
                    color: "#ffffff",
                    fontFamily: "system-ui, -apple-system, sans-serif",
                    margin: 0,
                    padding: 0,
                }}
            >
                <div style={{ textAlign: "center", padding: "2rem" }}>
                    <h1
                        style={{
                            fontSize: "6rem",
                            fontWeight: "bold",
                            margin: "0 0 1rem 0",
                            color: "#ef4444",
                        }}
                    >
                        500
                    </h1>
                    <h2
                        style={{
                            fontSize: "1.5rem",
                            fontWeight: 600,
                            marginBottom: "0.5rem",
                            color: "#fafafa",
                        }}
                    >
                        Something went wrong
                    </h2>
                    <p
                        style={{
                            color: "#a3a3a3",
                            marginBottom: "2rem",
                        }}
                    >
                        An unexpected error occurred. Please try again.
                    </p>
                    <div style={{ display: "flex", gap: "1rem", justifyContent: "center" }}>
                        <button
                            onClick={reset}
                            style={{
                                padding: "0.75rem 2rem",
                                borderRadius: "0.75rem",
                                backgroundColor: "#6366f1",
                                color: "#ffffff",
                                fontWeight: 600,
                                border: "none",
                                cursor: "pointer",
                            }}
                        >
                            Try Again
                        </button>
                        {/* eslint-disable-next-line @next/next/no-html-link-for-pages */}
                        <a
                            href="/"
                            style={{
                                display: "inline-flex",
                                alignItems: "center",
                                padding: "0.75rem 2rem",
                                borderRadius: "0.75rem",
                                border: "1px solid #3f3f46",
                                color: "#ffffff",
                                fontWeight: 600,
                                textDecoration: "none",
                                backgroundColor: "transparent",
                            }}
                        >
                            Go Home
                        </a>
                    </div>
                </div>
            </body>
        </html>
    )
}
