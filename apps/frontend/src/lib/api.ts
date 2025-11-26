export interface SystemInfo {
    service: string
    version: string
}

export async function getSystemInfo(): Promise<SystemInfo> {
    const res = await fetch("http://localhost:8000/api/system/info")
    const json = await res.json()
    return json as SystemInfo
}
