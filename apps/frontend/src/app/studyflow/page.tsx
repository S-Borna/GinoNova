"use client"

/**
 * Studyflow List Page
 * Phase 4.0: Display all studyflows with order and module links
 */

import { useState, useEffect } from "react"
import Link from "next/link"
import { getStudyflows, StudyflowPublic, truncateText } from "@/lib/studyflow"
import { Button } from "@/components/ui/button"
import {
    Card,
    CardHeader,
    CardTitle,
    CardDescription,
    CardContent,
} from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

export default function StudyflowPage() {
    const [studyflows, setStudyflows] = useState<StudyflowPublic[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        async function fetchStudyflows() {
            const result = await getStudyflows()
            if (result.ok) {
                setStudyflows(result.data)
            } else {
                setError(result.message)
            }
            setLoading(false)
        }

        fetchStudyflows()
    }, [])

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
                        <h1 className="text-3xl font-bold text-gray-900">Studyflows</h1>
                        <p className="text-gray-600 mt-1">
                            Browse all learning studyflows
                        </p>
                    </div>
                    <Link href="/modules">
                        <Button variant="outline">View Modules</Button>
                    </Link>
                </div>

                {/* Studyflows Grid */}
                {studyflows.length === 0 ? (
                    <Card className="p-8 text-center">
                        <p className="text-gray-500 mb-4">No studyflows found.</p>
                        <p className="text-sm text-gray-400">
                            Studyflows are created within modules. Go to a module to add studyflows.
                        </p>
                    </Card>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {studyflows.map((studyflow) => (
                            <Link key={studyflow.id} href={`/studyflow/${studyflow.id}`}>
                                <Card className="h-full hover:shadow-lg transition-shadow cursor-pointer">
                                    <CardHeader>
                                        <div className="flex items-start justify-between gap-2">
                                            <CardTitle className="text-lg">
                                                {studyflow.title}
                                            </CardTitle>
                                            <span className="px-2 py-1 text-xs font-medium rounded-full bg-blue-100 text-blue-800">
                                                #{studyflow.order}
                                            </span>
                                        </div>
                                        <CardDescription>
                                            {truncateText(studyflow.description, 120) || "No description"}
                                        </CardDescription>
                                    </CardHeader>
                                    <CardContent>
                                        <div className="flex items-center justify-between">
                                            <Link
                                                href={`/modules/${studyflow.module_id}`}
                                                className="text-xs text-blue-600 hover:text-blue-500"
                                                onClick={(e) => e.stopPropagation()}
                                            >
                                                View Module →
                                            </Link>
                                            <Badge
                                                variant={studyflow.is_active ? "success" : "inactive"}
                                            >
                                                {studyflow.is_active ? "Active" : "Inactive"}
                                            </Badge>
                                        </div>
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
