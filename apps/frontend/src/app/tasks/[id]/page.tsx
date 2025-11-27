"use client"

/**
 * Task Details Page
 * Phase 3.0: Display full task details
 */

import { useState, useEffect } from "react"
import { useParams } from "next/navigation"
import Link from "next/link"
import { getTask, TaskPublic, getDifficultyColor } from "@/lib/tasks"
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
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

export default function TaskDetailsPage() {
    const params = useParams()
    const taskId = params?.id as string | undefined

    const [task, setTask] = useState<TaskPublic | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        async function fetchTask() {
            if (!taskId) {
                setError("Task ID not provided")
                setLoading(false)
                return
            }

            const result = await getTask(taskId)
            if (result.ok) {
                setTask(result.data)
            } else {
                setError(result.message)
            }
            setLoading(false)
        }

        fetchTask()
    }, [taskId])

    if (loading) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gray-50">
                <p className="text-gray-600">Loading task...</p>
            </div>
        )
    }

    if (error) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gray-50">
                <div className="text-center">
                    <p className="text-red-500 mb-4">{error}</p>
                    <Link href="/tasks">
                        <Button variant="outline">Back to Tasks</Button>
                    </Link>
                </div>
            </div>
        )
    }

    if (!task) {
        return null
    }

    return (
        <div className="min-h-screen bg-gray-50 py-8">
            <div className="max-w-4xl mx-auto px-4">
                {/* Breadcrumb */}
                <nav className="mb-6 text-sm">
                    <Link href="/tasks" className="text-blue-600 hover:text-blue-500">
                        Tasks
                    </Link>
                    <span className="mx-2 text-gray-400">/</span>
                    <span className="text-gray-600">{task.title}</span>
                </nav>

                <Card>
                    <CardHeader>
                        <div className="flex items-start justify-between">
                            <div>
                                <CardTitle className="text-2xl">{task.title}</CardTitle>
                                <div className="mt-2 flex items-center gap-2">
                                    <span
                                        className={`px-3 py-1 text-sm font-medium rounded-full capitalize ${getDifficultyColor(
                                            task.difficulty
                                        )}`}
                                    >
                                        {task.difficulty}
                                    </span>
                                    <Badge variant={task.is_active ? "success" : "inactive"}>
                                        {task.is_active ? "Active" : "Inactive"}
                                    </Badge>
                                </div>
                            </div>
                            <Link href={`/modules/${task.module_id}`}>
                                <Button variant="outline">View Module</Button>
                            </Link>
                        </div>
                    </CardHeader>
                    <CardContent className="space-y-6">
                        {/* Description */}
                        <div>
                            <Label className="text-gray-500 text-sm">Description</Label>
                            <p className="mt-1 text-gray-900">
                                {task.description || "No description provided"}
                            </p>
                        </div>

                        {/* Module Link */}
                        <div className="py-3 border-t border-b">
                            <Label className="text-gray-500 text-sm">Parent Module</Label>
                            <div className="mt-1">
                                <Link
                                    href={`/modules/${task.module_id}`}
                                    className="text-blue-600 hover:text-blue-500 font-mono text-sm"
                                >
                                    {task.module_id}
                                </Link>
                            </div>
                        </div>

                        {/* Timestamps */}
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <Label className="text-gray-500 text-sm">Created At</Label>
                                <p className="mt-1 text-gray-900">
                                    {formatDate(task.created_at)}
                                </p>
                            </div>
                            <div>
                                <Label className="text-gray-500 text-sm">Updated At</Label>
                                <p className="mt-1 text-gray-900">
                                    {formatDate(task.updated_at)}
                                </p>
                            </div>
                        </div>

                        {/* UUID */}
                        <div>
                            <Label className="text-gray-500 text-sm">Task ID (UUID)</Label>
                            <p className="mt-1 text-gray-600 font-mono text-sm break-all">
                                {task.id}
                            </p>
                        </div>
                    </CardContent>
                </Card>

                {/* Back link */}
                <div className="mt-6 flex gap-4">
                    <Link href="/tasks">
                        <Button variant="secondary">← Back to Tasks</Button>
                    </Link>
                    <Link href={`/modules/${task.module_id}/tasks`}>
                        <Button variant="outline">View Module Tasks</Button>
                    </Link>
                </div>
            </div>
        </div>
    )
}
