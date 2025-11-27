"use client"

/**
 * Module Details Page
 * Phase 2.1: Enhanced card layout with breadcrumb
 */

import { useState, useEffect } from "react"
import { useParams } from "next/navigation"
import Link from "next/link"
import { getModule, ModulePublic } from "@/lib/modules"
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Switch } from "@/components/ui/switch"
import { Label } from "@/components/ui/label"

function formatDate(dateStr: string): string {
    return new Date(dateStr).toLocaleString("en-US", {
        year: "numeric",
        month: "short",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
    })
}

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

            const result = await getModule(moduleId)
            if (result.ok) {
                setModule(result.data)
            } else {
                setError(result.message)
            }
            setLoading(false)
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
                    <Link href="/modules">
                        <Button variant="outline">Back to Modules</Button>
                    </Link>
                </div>
            </div>
        )
    }

    if (!module) {
        return null
    }

    return (
        <div className="min-h-screen bg-gray-50 py-8">
            <div className="max-w-4xl mx-auto px-4">
                {/* Breadcrumb */}
                <nav className="mb-6 text-sm">
                    <Link href="/modules" className="text-blue-600 hover:text-blue-500">
                        Modules
                    </Link>
                    <span className="mx-2 text-gray-400">/</span>
                    <span className="text-gray-600">{module.name}</span>
                </nav>

                <Card>
                    <CardHeader>
                        <div className="flex items-start justify-between">
                            <div>
                                <CardTitle className="text-2xl">{module.name}</CardTitle>
                                <div className="mt-2">
                                    <Badge variant={module.is_active ? "success" : "inactive"}>
                                        {module.is_active ? "Active" : "Inactive"}
                                    </Badge>
                                </div>
                            </div>
                            <Link href={`/modules/${module.id}/edit`}>
                                <Button variant="outline">Edit</Button>
                            </Link>
                        </div>
                    </CardHeader>
                    <CardContent className="space-y-6">
                        {/* Description */}
                        <div>
                            <Label className="text-gray-500 text-sm">Description</Label>
                            <p className="mt-1 text-gray-900">
                                {module.description || "No description provided"}
                            </p>
                        </div>

                        {/* Status toggle (disabled - UI only) */}
                        <div className="flex items-center justify-between py-3 border-t border-b">
                            <div>
                                <Label>Active Status</Label>
                                <p className="text-xs text-gray-500">
                                    Toggle to enable/disable this module
                                </p>
                            </div>
                            <Switch
                                checked={module.is_active}
                                disabled={true}
                                aria-label="Module active status"
                            />
                        </div>

                        {/* Timestamps */}
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <Label className="text-gray-500 text-sm">Created At</Label>
                                <p className="mt-1 text-gray-900">
                                    {formatDate(module.created_at)}
                                </p>
                            </div>
                            <div>
                                <Label className="text-gray-500 text-sm">Updated At</Label>
                                <p className="mt-1 text-gray-900">
                                    {formatDate(module.updated_at)}
                                </p>
                            </div>
                        </div>

                        {/* UUID */}
                        <div>
                            <Label className="text-gray-500 text-sm">Module ID (UUID)</Label>
                            <p className="mt-1 text-gray-600 font-mono text-sm break-all">
                                {module.id}
                            </p>
                        </div>
                    </CardContent>
                </Card>

                {/* Back link */}
                <div className="mt-6">
                    <Link href="/modules">
                        <Button variant="secondary">← Back to Modules</Button>
                    </Link>
                </div>
            </div>
        </div>
    )
}
