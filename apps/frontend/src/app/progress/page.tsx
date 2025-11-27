"use client"

/**
 * Progress List Page
 * Phase 5.0: Display all progress records for the current user
 */

import { useState, useEffect } from "react"
import Link from "next/link"
import {
    getUserProgress,
    ProgressPublic,
    getTargetType,
    getTargetLink,
    mapTargetTypeToColor,
    mapTargetTypeToLabel,
} from "@/lib/progress"
import { Button } from "@/components/ui/button"
import {
    Card,
    CardHeader,
    CardTitle,
    CardDescription,
    CardContent,
} from "@/components/ui/card"
import { ProgressBar } from "@/components/ui/progress-bar"
import { StatusBadge } from "@/components/ui/status-badge"

// Placeholder user ID - in a real app, this would come from auth context
const DEMO_USER_ID = "00000000-0000-0000-0000-000000000001"

export default function ProgressPage() {
    const [progressRecords, setProgressRecords] = useState<ProgressPublic[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        async function fetchProgress() {
            const result = await getUserProgress(DEMO_USER_ID)
            if (result.ok) {
                setProgressRecords(result.data)
            } else {
                setError(result.message)
            }
            setLoading(false)
        }

        fetchProgress()
    }, [])

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
                        <h1 className="text-3xl font-bold text-gray-900">My Progress</h1>
                        <p className="text-gray-600 mt-1">
                            Track your learning progress across modules, tasks, and studyflows
                        </p>
                    </div>
                    <Link href="/dashboard">
                        <Button variant="outline">Dashboard</Button>
                    </Link>
                </div>

                {/* Progress Records */}
                {progressRecords.length === 0 ? (
                    <Card className="p-8 text-center">
                        <p className="text-gray-500 mb-4">No progress records found.</p>
                        <p className="text-sm text-gray-400">
                            Start learning to track your progress!
                        </p>
                    </Card>
                ) : (
                    <div className="space-y-4">
                        {progressRecords.map((record) => {
                            const targetType = getTargetType(record)
                            const targetLink = getTargetLink(record)

                            return (
                                <Link key={record.id} href={`/progress/${record.id}`}>
                                    <Card className="hover:shadow-lg transition-shadow cursor-pointer">
                                        <CardHeader className="pb-2">
                                            <div className="flex items-center justify-between">
                                                <div className="flex items-center gap-3">
                                                    <span
                                                        className={`px-2.5 py-1 text-xs font-medium rounded-full ${mapTargetTypeToColor(
                                                            targetType
                                                        )}`}
                                                    >
                                                        {mapTargetTypeToLabel(targetType)}
                                                    </span>
                                                    <CardTitle className="text-lg">
                                                        {targetType.charAt(0).toUpperCase() + targetType.slice(1)} Progress
                                                    </CardTitle>
                                                </div>
                                                <StatusBadge status={record.status} />
                                            </div>
                                            <CardDescription className="mt-1">
                                                ID: {record.id.slice(0, 8)}...
                                            </CardDescription>
                                        </CardHeader>
                                        <CardContent>
                                            <ProgressBar value={record.progress} />
                                            <div className="mt-3 flex items-center justify-between text-sm">
                                                <Link
                                                    href={targetLink}
                                                    className="text-blue-600 hover:text-blue-500"
                                                    onClick={(e) => e.stopPropagation()}
                                                >
                                                    View {mapTargetTypeToLabel(targetType)} →
                                                </Link>
                                                <span className="text-gray-400">
                                                    Updated: {new Date(record.updated_at).toLocaleDateString()}
                                                </span>
                                            </div>
                                        </CardContent>
                                    </Card>
                                </Link>
                            )
                        })}
                    </div>
                )}
            </div>
        </div>
    )
}
