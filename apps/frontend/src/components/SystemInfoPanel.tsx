"use client"

import { useEffect, useState } from "react"
import { getSystemInfo, SystemInfo } from "../lib/api"

export default function SystemInfoPanel() {
    const [info, setInfo] = useState<SystemInfo | null>(null)

    useEffect(() => {
        getSystemInfo().then(setInfo)
    }, [])

    if (!info) return <div>Loading system info...</div>

    return (
        <div>
            <h2>System Info</h2>
            <p>Service: {info.service}</p>
            <p>Version: {info.version}</p>
        </div>
    )
}
