"use client"

/**
 * Module Details Page
 * Phase 2.0: Modules Foundation
 */

import { useState, useEffect } from "react"
import { useParams } from "next/navigation"
import Link from "next/link"
import { getModule, ModulePublic } from "@/lib/modules"

export default function ModuleDetailsPage() {
    const params = useParams()
    const moduleId = params?.id as string | undefined

    const [module, setModule] = useState<ModulePublic | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        async function fetchModule() {
            if (!moduleId) {
                setError("Module ID not provided")
                setLoading(false)
                return
            }

            try {
                const data = await getModule(moduleId)
                setModule(data)
            } catch (err) {
                setError(err instanceof Error ? err.message : "Failed to load module")
            } finally {
                setLoading(false)
            }
        }

        fetchModule()
    }, [moduleId])

    if (loading) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gray-50">
                <p className="text-gray-600">Loading module...</p>
            </div>
        )
    }

    if (error) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gray-50">
                <div className="text-center">
                    <p className="text-red-500 mb-4">{error}</p>
                    <Link href="/modules" className="text-blue-600 hover:text-blue-500">
                        Back to Modules
                    </Link>
                </div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-gray-50 py-8">
            <div className="max-w-4xl mx-auto px-4">
                <div className="bg-white rounded-lg shadow p-6">
                    <div className="mb-4">
                        <Link href="/modules" className="text-blue-600 hover:text-blue-500 text-sm">
                            ← Back to Modules
                        </Link>
                    </div>

                    <h1 className="text-2xl font-bold text-gray-900 mb-2">
                        Module Details Online
                    </h1>
                    <p className="text-gray-600 mb-6">Phase 2.0 - Modules Foundation</p>

                    {module && (
                        <div className="space-y-4">
                            <div>
                                <span className="font-medium text-gray-700">Name:</span>
                                <span className="ml-2 text-gray-900">{module.name}</span>
                            </div>
                            {module.description && (
                                <div>
                                    <span className="font-medium text-gray-700">Description:</span>
                                    <span className="ml-2 text-gray-900">{module.description}</span>
                                </div>
                            )}
                            <div>
                                <span className="font-medium text-gray-700">Status:</span>
                                <span className={`ml-2 ${module.is_active ? "text-green-600" : "text-red-600"}`}>
                                    {module.is_active ? "Active" : "Inactive"}
                                </span>
                            </div>
                            <div>
                                <span className="font-medium text-gray-700">ID:</span>
                                <span className="ml-2 text-gray-500 text-sm font-mono">{module.id}</span>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    )
}
