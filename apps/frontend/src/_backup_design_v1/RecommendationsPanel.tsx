"use client"

/**
 * RecommendationsPanel Component
 * Phase 6.2: AI-powered recommendations (placeholder for Phase 7 integration)
 */

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"

// ============================================================================
// TYPES
// ============================================================================

interface Recommendation {
    id: string
    type: "task" | "module" | "studyflow" | "tip"
    title: string
    description: string
    priority: "high" | "medium" | "low"
    action?: {
        label: string
        href: string
    }
}

interface RecommendationsPanelProps {
    recommendations?: Recommendation[]
    isLoading?: boolean
    isEnabled?: boolean
}

// ============================================================================
// PLACEHOLDER DATA
// ============================================================================

const placeholderRecommendations: Recommendation[] = [
    {
        id: "1",
        type: "task",
        title: "Complete Docker Basics",
        description: "You're 80% through this module. Finish the last task to earn bonus XP!",
        priority: "high",
        action: { label: "Continue", href: "/tasks/docker-basics" }
    },
    {
        id: "2",
        type: "tip",
        title: "Optimal Study Time",
        description: "Based on your patterns, you're most productive between 9-11 AM.",
        priority: "medium"
    },
    {
        id: "3",
        type: "module",
        title: "Try Kubernetes Next",
        description: "Your Docker skills are ready! Kubernetes is the logical next step.",
        priority: "low",
        action: { label: "View Module", href: "/modules/kubernetes" }
    }
]

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

function getPriorityColor(priority: string): string {
    switch (priority) {
        case "high": return "bg-rose-100 text-rose-700 border-rose-200"
        case "medium": return "bg-amber-100 text-amber-700 border-amber-200"
        case "low": return "bg-blue-100 text-blue-700 border-blue-200"
        default: return "bg-gray-100 text-gray-600 border-gray-200"
    }
}

function getTypeIcon(type: string): string {
    switch (type) {
        case "task": return "✅"
        case "module": return "📚"
        case "studyflow": return "🎯"
        case "tip": return "💡"
        default: return "✨"
    }
}

// ============================================================================
// COMPONENT
// ============================================================================

export function RecommendationsPanel({
    recommendations,
    isLoading = false,
    isEnabled = false,
}: RecommendationsPanelProps) {
    // Use placeholder data when AI is not enabled
    const displayRecommendations = isEnabled && recommendations?.length
        ? recommendations
        : placeholderRecommendations

    return (
        <Card className="rounded-xl border-0 shadow-md bg-white overflow-hidden">
            <CardHeader className="pb-2 bg-gradient-to-r from-indigo-50 to-purple-50">
                <div className="flex items-center justify-between">
                    <CardTitle className="text-base font-semibold text-gray-900 flex items-center gap-2">
                        <span className="text-lg">🤖</span>
                        AI Recommendations
                    </CardTitle>
                    <Badge
                        variant="outline"
                        className={isEnabled
                            ? "bg-emerald-100 text-emerald-700 border-emerald-200"
                            : "bg-amber-100 text-amber-700 border-amber-200"
                        }
                    >
                        {isEnabled ? "AI Active" : "Preview Mode"}
                    </Badge>
                </div>
            </CardHeader>
            <CardContent className="pt-4">
                {!isEnabled && (
                    <div className="mb-4 p-3 rounded-lg bg-gradient-to-r from-indigo-50 to-purple-50 border border-indigo-100">
                        <div className="flex items-start gap-2">
                            <span className="text-lg">✨</span>
                            <div>
                                <p className="text-xs font-medium text-indigo-900">AI Engine Coming Soon</p>
                                <p className="text-[10px] text-indigo-600">
                                    Personalized recommendations powered by your learning patterns.
                                </p>
                            </div>
                        </div>
                    </div>
                )}

                {isLoading ? (
                    <div className="space-y-3">
                        {[1, 2, 3].map((i) => (
                            <div key={i} className="animate-pulse p-3 rounded-lg bg-gray-50">
                                <div className="flex items-start gap-3">
                                    <div className="w-8 h-8 rounded-lg bg-gray-200" />
                                    <div className="flex-1">
                                        <div className="h-4 w-24 bg-gray-200 rounded mb-2" />
                                        <div className="h-3 w-full bg-gray-200 rounded" />
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                ) : (
                    <div className="space-y-3">
                        {displayRecommendations.map((rec) => (
                            <div
                                key={rec.id}
                                className="group p-3 rounded-lg border border-gray-100 hover:border-gray-200 hover:shadow-sm transition-all duration-200"
                            >
                                <div className="flex items-start gap-3">
                                    {/* Icon */}
                                    <div className="w-8 h-8 rounded-lg bg-gray-100 flex items-center justify-center flex-shrink-0">
                                        <span className="text-sm">{getTypeIcon(rec.type)}</span>
                                    </div>

                                    {/* Content */}
                                    <div className="flex-1 min-w-0">
                                        <div className="flex items-center gap-2 mb-1">
                                            <h4 className="text-sm font-medium text-gray-900 truncate">
                                                {rec.title}
                                            </h4>
                                            <Badge
                                                variant="outline"
                                                className={`text-[9px] px-1.5 py-0 border ${getPriorityColor(rec.priority)}`}
                                            >
                                                {rec.priority}
                                            </Badge>
                                        </div>
                                        <p className="text-xs text-gray-500 line-clamp-2">
                                            {rec.description}
                                        </p>

                                        {rec.action && (
                                            <Button
                                                variant="ghost"
                                                size="sm"
                                                className="h-6 px-2 mt-2 text-[10px] font-medium text-indigo-600 hover:text-indigo-700 hover:bg-indigo-50"
                                                asChild
                                            >
                                                <a href={rec.action.href}>
                                                    {rec.action.label}
                                                    <span className="ml-1">→</span>
                                                </a>
                                            </Button>
                                        )}
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                )}

                {/* AI Integration Note */}
                <div className="mt-4 pt-3 border-t border-gray-100 text-center">
                    <p className="text-[10px] text-gray-400">
                        Powered by DevOpsHub AI Engine (Phase 7)
                    </p>
                </div>
            </CardContent>
        </Card>
    )
}
