"use client"

/**
 * Tasks List Page
 * Phase 3.0: Display all tasks with difficulty badges and module links
 */

import { useState, useEffect } from "react"
import Link from "next/link"
import { getTasks, TaskPublic, truncateText, getDifficultyColor } from "@/lib/tasks"
import { Button } from "@/components/ui/button"
import {
    Card,
    CardHeader,
    CardTitle,
    CardDescription,
    CardContent,
} from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

export default function TasksPage() {
    const [tasks, setTasks] = useState<TaskPublic[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        async function fetchTasks() {
            const result = await getTasks()
            if (result.ok) {
                setTasks(result.data)
            } else {
                setError(result.message)
            }
            setLoading(false)
        }

        fetchTasks()
    }, [])

    if (loading) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gray-50">
                <p className="text-gray-600">Loading tasks...</p>
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
                        <h1 className="text-3xl font-bold text-gray-900">Tasks</h1>
                        <p className="text-gray-600 mt-1">
                            Browse all learning tasks
                        </p>
                    </div>
                    <Link href="/modules">
                        <Button variant="outline">View Modules</Button>
                    </Link>
                </div>

                {/* Tasks Grid */}
                {tasks.length === 0 ? (
                    <Card className="p-8 text-center">
                        <p className="text-gray-500 mb-4">No tasks found.</p>
                        <p className="text-sm text-gray-400">
                            Tasks are created within modules. Go to a module to add tasks.
                        </p>
                    </Card>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {tasks.map((task) => (
                            <Link key={task.id} href={`/tasks/${task.id}`}>
                                <Card className="h-full hover:shadow-lg transition-shadow cursor-pointer">
                                    <CardHeader>
                                        <div className="flex items-start justify-between gap-2">
                                            <CardTitle className="text-lg">
                                                {task.title}
                                            </CardTitle>
                                            <span
                                                className={`px-2 py-1 text-xs font-medium rounded-full capitalize ${getDifficultyColor(
                                                    task.difficulty
                                                )}`}
                                            >
                                                {task.difficulty}
                                            </span>
                                        </div>
                                        <CardDescription>
                                            {truncateText(task.description, 120) || "No description"}
                                        </CardDescription>
                                    </CardHeader>
                                    <CardContent>
                                        <div className="flex items-center justify-between">
                                            <Link
                                                href={`/modules/${task.module_id}`}
                                                className="text-xs text-blue-600 hover:text-blue-500"
                                                onClick={(e) => e.stopPropagation()}
                                            >
                                                View Module →
                                            </Link>
                                            <Badge
                                                variant={task.is_active ? "success" : "inactive"}
                                            >
                                                {task.is_active ? "Active" : "Inactive"}
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
