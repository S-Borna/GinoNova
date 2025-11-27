"use client"

/**
 * Module Studyflows Page
 * Phase 4.0: List all studyflows for a specific module
 */

import { useState, useEffect } from "react"
import { useParams } from "next/navigation"
import Link from "next/link"
import { getStudyflowsByModule, StudyflowPublic, truncateText } from "@/lib/studyflow"
import { getModule, ModulePublic } from "@/lib/modules"
import { Button } from "@/components/ui/button"
import {
    Card,
    CardHeader,
    CardTitle,
    CardDescription,
    CardContent,
} from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

export default function ModuleStudyflowsPage() {
    const params = useParams()
    const moduleId = params?.id as string | undefined

    const [studyflows, setStudyflows] = useState<StudyflowPublic[]>([])
    const [module, setModule] = useState<ModulePublic | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        async function fetchData() {
            if (!moduleId) {
                setError("Module ID not provided")
                setLoading(false)
                return
            }

            // Fetch module and studyflows in parallel
            const [moduleResult, studyflowsResult] = await Promise.all([
                getModule(moduleId),
                getStudyflowsByModule(moduleId),
            ])

            if (!moduleResult.ok) {
                setError(moduleResult.message)
                setLoading(false)
                return
            }

            if (!studyflowsResult.ok) {
                setError(studyflowsResult.message)
                setLoading(false)
                return
            }

            setModule(moduleResult.data)
            setStudyflows(studyflowsResult.data)
            setLoading(false)
        }

        fetchData()
    }, [moduleId])

    if (loading) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gray-50">
                <p className="text-gray-600">Loading studyflows...</p>
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
            <div className="max-w-6xl mx-auto px-4">
                {/* Breadcrumb */}
                <nav className="mb-6 text-sm">
                    <Link href="/modules" className="text-blue-600 hover:text-blue-500">
                        Modules
                    </Link>
                    <span className="mx-2 text-gray-400">/</span>
                    <Link
                        href={`/modules/${module.id}`}
                        className="text-blue-600 hover:text-blue-500"
                    >
                        {module.name}
                    </Link>
                    <span className="mx-2 text-gray-400">/</span>
                    <span className="text-gray-600">Studyflows</span>
                </nav>

                {/* Header */}
                <div className="flex items-center justify-between mb-10">
                    <div>
                        <h1 className="text-3xl font-bold text-gray-900">
                            Studyflows in &quot;{module.name}&quot;
                        </h1>
                        <p className="text-gray-600 mt-1">
                            {studyflows.length} studyflow{studyflows.length !== 1 ? "s" : ""} in this module
                        </p>
                    </div>
                    <Link href={`/modules/${module.id}`}>
                        <Button variant="outline">Back to Module</Button>
                    </Link>
                </div>

                {/* Studyflows List (sorted by order) */}
                {studyflows.length === 0 ? (
                    <Card className="p-8 text-center">
                        <p className="text-gray-500 mb-4">No studyflows in this module yet.</p>
                        <p className="text-sm text-gray-400">
                            Studyflows can be added via the API.
                        </p>
                    </Card>
                ) : (
                    <div className="space-y-4">
                        {studyflows.map((studyflow) => (
                            <Link key={studyflow.id} href={`/studyflow/${studyflow.id}`}>
                                <Card className="hover:shadow-lg transition-shadow cursor-pointer">
                                    <CardHeader>
                                        <div className="flex items-center gap-4">
                                            <span className="flex-shrink-0 w-10 h-10 flex items-center justify-center text-lg font-bold rounded-full bg-blue-100 text-blue-800">
                                                {studyflow.order}
                                            </span>
                                            <div className="flex-1 min-w-0">
                                                <div className="flex items-center justify-between gap-2">
                                                    <CardTitle className="text-lg truncate">
                                                        {studyflow.title}
                                                    </CardTitle>
                                                    <Badge
                                                        variant={studyflow.is_active ? "success" : "inactive"}
                                                    >
                                                        {studyflow.is_active ? "Active" : "Inactive"}
                                                    </Badge>
                                                </div>
                                                <CardDescription className="mt-1">
                                                    {truncateText(studyflow.description, 150) || "No description"}
                                                </CardDescription>
                                            </div>
                                        </div>
                                    </CardHeader>
                                </Card>
                            </Link>
                        ))}
                    </div>
                )}
            </div>
        </div>
    )
}
