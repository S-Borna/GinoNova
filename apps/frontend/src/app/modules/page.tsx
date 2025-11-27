"use client"

/**
 * Modules List Page
 * Phase 2.0: Modules Foundation
 */

import { useState, useEffect } from "react"
import Link from "next/link"
import { getModules, ModulePublic } from "@/lib/modules"

export default function ModulesPage() {
    const [modules, setModules] = useState<ModulePublic[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        async function fetchModules() {
            try {
                const data = await getModules()
                setModules(data)
            } catch (err) {
                setError(err instanceof Error ? err.message : "Failed to load modules")
            } finally {
                setLoading(false)
            }
        }

        fetchModules()
    }, [])

    if (loading) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gray-50">
                <p className="text-gray-600">Loading modules...</p>
            </div>
        )
    }

    if (error) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gray-50">
                <div className="text-center">
                    <p className="text-red-500 mb-4">{error}</p>
                    <button
                        onClick={() => window.location.reload()}
                        className="text-blue-600 hover:text-blue-500"
                    >
                        Retry
                    </button>
                </div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-gray-50 py-8">
            <div className="max-w-4xl mx-auto px-4">
                <div className="bg-white rounded-lg shadow p-6">
                    <h1 className="text-2xl font-bold text-gray-900 mb-2">
                        Modules Online
                    </h1>
                    <p className="text-gray-600 mb-6">Phase 2.0 - Modules Foundation</p>

                    {modules.length === 0 ? (
                        <p className="text-gray-500">No modules found.</p>
                    ) : (
                        <ul className="divide-y divide-gray-200">
                            {modules.map((module) => (
                                <li key={module.id} className="py-3">
                                    <Link
                                        href={`/modules/${module.id}`}
                                        className="text-blue-600 hover:text-blue-500"
                                    >
                                        {module.name}
                                    </Link>
                                </li>
                            ))}
                        </ul>
                    )}
                </div>
            </div>
        </div>
    )
}
