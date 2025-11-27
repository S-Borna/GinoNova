export interface SystemInfo {
    service: string
    version: string
}

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

export async function getSystemInfo(): Promise<SystemInfo> {
    const res = await fetch(`${API_BASE_URL}/api/system/info`)
    const json = await res.json()
    return json as SystemInfo
}
