"use client"

/**
 * Module Tasks Page
 * Phase 3.0: List all tasks for a specific module
 */

import { useState, useEffect } from "react"
import { useParams } from "next/navigation"
import Link from "next/link"
import { getTasksForModule, TaskPublic, truncateText, getDifficultyColor } from "@/lib/tasks"
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

export default function ModuleTasksPage() {
    const params = useParams()
    const moduleId = params?.id as string | undefined

    const [tasks, setTasks] = useState<TaskPublic[]>([])
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

            // Fetch module and tasks in parallel
            const [moduleResult, tasksResult] = await Promise.all([
                getModule(moduleId),
                getTasksForModule(moduleId),
            ])

            if (!moduleResult.ok) {
                setError(moduleResult.message)
                setLoading(false)
                return
            }

            if (!tasksResult.ok) {
                setError(tasksResult.message)
                setLoading(false)
                return
            }

            setModule(moduleResult.data)
            setTasks(tasksResult.data)
            setLoading(false)
        }

        fetchData()
    }, [moduleId])

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
                    <span className="text-gray-600">Tasks</span>
                </nav>

                {/* Header */}
                <div className="flex items-center justify-between mb-10">
                    <div>
                        <h1 className="text-3xl font-bold text-gray-900">
                            Tasks in &quot;{module.name}&quot;
                        </h1>
                        <p className="text-gray-600 mt-1">
                            {tasks.length} task{tasks.length !== 1 ? "s" : ""} in this module
                        </p>
                    </div>
                    <Link href={`/modules/${module.id}`}>
                        <Button variant="outline">Back to Module</Button>
                    </Link>
                </div>

                {/* Tasks Grid */}
                {tasks.length === 0 ? (
                    <Card className="p-8 text-center">
                        <p className="text-gray-500 mb-4">No tasks in this module yet.</p>
                        <p className="text-sm text-gray-400">
                            Tasks can be added via the API.
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
                                        <Badge
                                            variant={task.is_active ? "success" : "inactive"}
                                        >
                                            {task.is_active ? "Active" : "Inactive"}
                                        </Badge>
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
