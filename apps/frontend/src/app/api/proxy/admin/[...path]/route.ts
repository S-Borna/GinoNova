import { NextRequest, NextResponse } from "next/server"

// Proxy admin API requests to backend to bypass browser/network CORS edge cases.
// Usage: /api/proxy/admin/<endpoint>?<query>
// Forwards Authorization header if present.

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

export async function GET(req: NextRequest, { params }: { params: { path: string[] } }) {
    const path = params.path.join("/")
    const url = new URL(req.url)
    const target = `${API_BASE_URL}/api/admin/${path}${url.search}`

    const headers: Record<string, string> = {}
    const auth = req.headers.get("authorization")
    if (auth) headers["authorization"] = auth

    try {
        const res = await fetch(target, {
            method: "GET",
            headers,
            // No need for credentials; server-to-server
        })

        const body = await res.text()

        return new NextResponse(body, {
            status: res.status,
            headers: {
                "content-type": res.headers.get("content-type") || "application/json",
            }
        })
    } catch (err) {
        return NextResponse.json({ detail: err instanceof Error ? err.message : "Proxy error" }, { status: 502 })
    }
}
