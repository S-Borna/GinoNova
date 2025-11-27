"use client"

/**
 * Modules List Page
 * Phase 2.1: Card grid with create button
 */

import { useState, useEffect } from "react"
import Link from "next/link"
import { getModules, ModulePublic, truncateText } from "@/lib/modules"
import { Button } from "@/components/ui/button"
import {
    Card,
    CardHeader,
    CardTitle,
    CardDescription,
    CardContent,
} from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

export default function ModulesPage() {
    const [modules, setModules] = useState<ModulePublic[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        async function fetchModules() {
            const result = await getModules()
            if (result.ok) {
                setModules(result.data)
            } else {
                setError(result.message)
            }
            setLoading(false)
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
                    <Button
                        onClick={() => window.location.reload()}
                        variant="outline"
                    >
                        Retry
                    </Button>
                </div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-gray-50 py-8">
            <div className="max-w-6xl mx-auto px-4">
                {/* Header */}
                <div className="flex items-center justify-between mb-10">
                    <div>
                        <h1 className="text-3xl font-bold text-gray-900">Modules</h1>
                        <p className="text-gray-600 mt-1">
                            Manage your learning modules
                        </p>
                    </div>
                    <Link href="/modules/new">
                        <Button>Create Module</Button>
                    </Link>
                </div>

                {/* Modules Grid */}
                {modules.length === 0 ? (
                    <Card className="p-8 text-center">
                        <p className="text-gray-500 mb-4">No modules found.</p>
                        <Link href="/modules/new">
                            <Button variant="outline">Create your first module</Button>
                        </Link>
                    </Card>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {modules.map((module) => (
                            <Link key={module.id} href={`/modules/${module.id}`}>
                                <Card className="h-full hover:shadow-lg transition-shadow cursor-pointer">
                                    <CardHeader>
                                        <div className="flex items-start justify-between gap-2">
                                            <CardTitle className="text-lg">
                                                {module.name}
                                            </CardTitle>
                                            <Badge
                                                variant={module.is_active ? "success" : "inactive"}
                                            >
                                                {module.is_active ? "Active" : "Inactive"}
                                            </Badge>
                                        </div>
                                        <CardDescription>
                                            {truncateText(module.description, 120) || "No description"}
                                        </CardDescription>
                                    </CardHeader>
                                    <CardContent>
                                        <p className="text-xs text-gray-400">
                                            ID: {module.id.slice(0, 8)}...
                                        </p>
                                    </CardContent>
                                </Card>
                            </Link>
                        ))}
                    </div>
                )}
            </div>
        </div>
    )
}
