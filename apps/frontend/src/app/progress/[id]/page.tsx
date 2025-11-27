"use client"

/**
 * Progress Details Page
 * Phase 5.0: Display full progress record details
 */

import { useState, useEffect } from "react"
import { useParams } from "next/navigation"
import Link from "next/link"
import {
    getProgress,
    ProgressPublic,
    getTargetType,
    getTargetId,
    getTargetLink,
    mapTargetTypeToColor,
    mapTargetTypeToLabel,
} from "@/lib/progress"
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { ProgressBar } from "@/components/ui/progress-bar"
import { StatusBadge } from "@/components/ui/status-badge"

function formatDate(dateStr: string): string {
    return new Date(dateStr).toLocaleString("en-US", {
        year: "numeric",
        month: "short",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
    })
}

export default function ProgressDetailsPage() {
    const params = useParams()
    const progressId = params?.id as string | undefined

    const [progress, setProgress] = useState<ProgressPublic | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        async function fetchProgress() {
            if (!progressId) {
                setError("Progress ID not provided")
                setLoading(false)
                return
            }

            const result = await getProgress(progressId)
            if (result.ok) {
                setProgress(result.data)
            } else {
                setError(result.message)
            }
            setLoading(false)
        }

        fetchProgress()
    }, [progressId])

    if (loading) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gray-50">
                <p className="text-gray-600">Loading progress...</p>
            </div>
        )
    }

    if (error) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gray-50">
                <div className="text-center">
                    <p className="text-red-500 mb-4">{error}</p>
                    <Link href="/progress">
                        <Button variant="outline">Back to Progress</Button>
                    </Link>
                </div>
            </div>
        )
    }

    if (!progress) {
        return null
    }

    const targetType = getTargetType(progress)
    const targetId = getTargetId(progress)
    const targetLink = getTargetLink(progress)

    return (
        <div className="min-h-screen bg-gray-50 py-8">
            <div className="max-w-4xl mx-auto px-4">
                {/* Breadcrumb */}
                <nav className="mb-6 text-sm">
                    <Link href="/progress" className="text-blue-600 hover:text-blue-500">
                        Progress
                    </Link>
                    <span className="mx-2 text-gray-400">/</span>
                    <span className="text-gray-600">Details</span>
                </nav>

                <Card>
                    <CardHeader>
                        <div className="flex items-start justify-between">
                            <div>
                                <div className="flex items-center gap-3 mb-2">
                                    <span
                                        className={`px-3 py-1 text-sm font-medium rounded-full ${mapTargetTypeToColor(
                                            targetType
                                        )}`}
                                    >
                                        {mapTargetTypeToLabel(targetType)}
                                    </span>
                                    <StatusBadge status={progress.status} />
                                </div>
                                <CardTitle className="text-2xl">Progress Record</CardTitle>
                            </div>
                            <Link href={targetLink}>
                                <Button variant="outline">
                                    View {mapTargetTypeToLabel(targetType)}
                                </Button>
                            </Link>
                        </div>
                    </CardHeader>
                    <CardContent className="space-y-6">
                        {/* Progress Bar */}
                        <div>
                            <Label className="text-gray-500 text-sm mb-2 block">Progress</Label>
                            <ProgressBar value={progress.progress} className="mt-2" />
                        </div>

                        {/* Target Info */}
                        <div className="py-3 border-t border-b">
                            <Label className="text-gray-500 text-sm">Target {mapTargetTypeToLabel(targetType)}</Label>
                            <div className="mt-1">
                                <Link
                                    href={targetLink}
                                    className="text-blue-600 hover:text-blue-500 font-mono text-sm"
                                >
                                    {targetId}
                                </Link>
                            </div>
                        </div>

                        {/* User ID */}
                        <div>
                            <Label className="text-gray-500 text-sm">User ID</Label>
                            <p className="mt-1 text-gray-600 font-mono text-sm">
                                {progress.user_id}
                            </p>
                        </div>

                        {/* Timestamps */}
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <Label className="text-gray-500 text-sm">Created At</Label>
                                <p className="mt-1 text-gray-900">
                                    {formatDate(progress.created_at)}
                                </p>
                            </div>
                            <div>
                                <Label className="text-gray-500 text-sm">Updated At</Label>
                                <p className="mt-1 text-gray-900">
                                    {formatDate(progress.updated_at)}
                                </p>
                            </div>
                        </div>

                        {/* UUID */}
                        <div>
                            <Label className="text-gray-500 text-sm">Progress ID (UUID)</Label>
                            <p className="mt-1 text-gray-600 font-mono text-sm break-all">
                                {progress.id}
                            </p>
                        </div>
                    </CardContent>
                </Card>

                {/* Back link */}
                <div className="mt-6">
                    <Link href="/progress">
                        <Button variant="secondary">← Back to Progress</Button>
                    </Link>
                </div>
            </div>
        </div>
    )
}
