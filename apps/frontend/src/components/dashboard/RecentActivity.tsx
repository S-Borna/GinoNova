"use client"

/**
 * ============================================================================
 * RECENT ACTIVITY - Apple-Inspired Activity Timeline
 * ============================================================================
 * 
 * Design Philosophy:
 * - Inspired by Apple Fitness activity feed
 * - Clean timeline with subtle animations
 * - Relative timestamps for freshness
 * - Icon-based activity indicators
 * 
 * Features:
 * - Activity type icons with color coding
 * - Relative time formatting (just now, 5m ago, 2h ago, yesterday)
 * - Empty state with encouraging message
 * - Staggered fade-in animations
 * 
 * @phase D.2 - Dashboard UI Complete
 * @design Apple Fitness+ activity feed aesthetic
 */

import { cn } from "@/lib/utils"
import { GlassCard } from "@/components/ui/glass-card"
import {
    BookOpen,
    CheckCircle2,
    Trophy,
    Zap,
    Target,
    Clock,
    Star,
    Flame,
    Award,
    type LucideIcon
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export type ActivityType = 
    | "task_completed" 
    | "module_completed" 
    | "xp_earned" 
    | "streak_milestone"
    | "level_up"
    | "achievement"
    | "study_session"
    | "badge_earned"

export interface Activity {
    id: string
    type: ActivityType
    title: string
    description?: string
    xp?: number
    timestamp: string | Date
    metadata?: {
        moduleId?: string
        moduleName?: string
        taskId?: string
        taskName?: string
        badgeName?: string
        level?: number
        streakDays?: number
    }
}

interface RecentActivityProps {
    activities?: Activity[]
    className?: string
    maxItems?: number
}

/* ============================================================================
   ACTIVITY CONFIG
   ============================================================================ */

interface ActivityConfig {
    icon: LucideIcon
    color: string
    bgColor: string
}

const activityConfig: Record<ActivityType, ActivityConfig> = {
    task_completed: {
        icon: CheckCircle2,
        color: "text-emerald-600 dark:text-emerald-400",
        bgColor: "bg-emerald-100 dark:bg-emerald-900/30"
    },
    module_completed: {
        icon: BookOpen,
        color: "text-primary-600 dark:text-primary-400",
        bgColor: "bg-primary-100 dark:bg-primary-900/30"
    },
    xp_earned: {
        icon: Zap,
        color: "text-amber-600 dark:text-amber-400",
        bgColor: "bg-amber-100 dark:bg-amber-900/30"
    },
    streak_milestone: {
        icon: Flame,
        color: "text-orange-600 dark:text-orange-400",
        bgColor: "bg-orange-100 dark:bg-orange-900/30"
    },
    level_up: {
        icon: Star,
        color: "text-purple-600 dark:text-purple-400",
        bgColor: "bg-purple-100 dark:bg-purple-900/30"
    },
    achievement: {
        icon: Trophy,
        color: "text-yellow-600 dark:text-yellow-400",
        bgColor: "bg-yellow-100 dark:bg-yellow-900/30"
    },
    study_session: {
        icon: Clock,
        color: "text-blue-600 dark:text-blue-400",
        bgColor: "bg-blue-100 dark:bg-blue-900/30"
    },
    badge_earned: {
        icon: Award,
        color: "text-rose-600 dark:text-rose-400",
        bgColor: "bg-rose-100 dark:bg-rose-900/30"
    }
}

/* ============================================================================
   HELPERS
   ============================================================================ */

function getRelativeTime(timestamp: string | Date): string {
    const now = new Date()
    const date = new Date(timestamp)
    const diffInSeconds = Math.floor((now.getTime() - date.getTime()) / 1000)
    
    if (diffInSeconds < 60) {
        return "just now"
    }
    
    const diffInMinutes = Math.floor(diffInSeconds / 60)
    if (diffInMinutes < 60) {
        return `${diffInMinutes}m ago`
    }
    
    const diffInHours = Math.floor(diffInMinutes / 60)
    if (diffInHours < 24) {
        return `${diffInHours}h ago`
    }
    
    const diffInDays = Math.floor(diffInHours / 24)
    if (diffInDays === 1) {
        return "yesterday"
    }
    
    if (diffInDays < 7) {
        return `${diffInDays}d ago`
    }
    
    // Format as date for older items
    return date.toLocaleDateString("en-US", { 
        month: "short", 
        day: "numeric" 
    })
}

/* ============================================================================
   ACTIVITY ITEM COMPONENT
   ============================================================================ */

interface ActivityItemProps {
    activity: Activity
    isLast: boolean
    delay?: number
}

function ActivityItem({ activity, isLast, delay = 0 }: ActivityItemProps) {
    const config = activityConfig[activity.type]
    const Icon = config.icon
    const relativeTime = getRelativeTime(activity.timestamp)

    return (
        <div 
            className={cn(
                "relative flex gap-4 pb-4 animate-fade-in-up",
                !isLast && "border-l-2 border-neutral-200 dark:border-neutral-700 ml-4"
            )}
            style={{ animationDelay: `${delay}ms` }}
        >
            {/* Timeline dot */}
            <div className={cn(
                "absolute -left-3 w-6 h-6 rounded-full flex items-center justify-center",
                "ring-4 ring-white dark:ring-neutral-900",
                config.bgColor
            )}>
                <Icon className={cn("h-3 w-3", config.color)} />
            </div>

            {/* Content */}
            <div className="flex-1 ml-6">
                <div className="flex items-start justify-between gap-2">
                    <div className="space-y-0.5">
                        <p className="text-sm font-medium text-neutral-900 dark:text-white">
                            {activity.title}
                        </p>
                        {activity.description && (
                            <p className="text-xs text-neutral-500 dark:text-neutral-400">
                                {activity.description}
                            </p>
                        )}
                    </div>
                    <span className="text-xs text-neutral-400 dark:text-neutral-500 whitespace-nowrap">
                        {relativeTime}
                    </span>
                </div>

                {/* XP badge if applicable */}
                {activity.xp && activity.xp > 0 && (
                    <div className="mt-1.5">
                        <span className={cn(
                            "inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium",
                            "bg-amber-100 dark:bg-amber-900/30 text-amber-700 dark:text-amber-400"
                        )}>
                            <Zap className="h-3 w-3" />
                            +{activity.xp} XP
                        </span>
                    </div>
                )}
            </div>
        </div>
    )
}

/* ============================================================================
   EMPTY STATE
   ============================================================================ */

function EmptyState() {
    return (
        <div className="py-8 text-center animate-fade-in">
            <div className={cn(
                "w-16 h-16 mx-auto mb-4 rounded-2xl flex items-center justify-center",
                "bg-gradient-to-br from-primary-100 to-primary-50",
                "dark:from-primary-900/30 dark:to-primary-800/20"
            )}>
                <Target className="h-8 w-8 text-primary-600 dark:text-primary-400" />
            </div>
            <h4 className="font-semibold text-neutral-900 dark:text-white mb-1">
                No activity yet
            </h4>
            <p className="text-sm text-neutral-500 dark:text-neutral-400 max-w-xs mx-auto">
                Complete tasks and modules to see your progress here
            </p>
        </div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function RecentActivity({ 
    activities = [], 
    className,
    maxItems = 5
}: RecentActivityProps) {
    // Sample activities for demo if none provided
    const displayActivities = activities.length > 0 ? activities : [
        {
            id: "1",
            type: "task_completed" as ActivityType,
            title: "Completed 'Install VS Code'",
            description: "Linux Basics Module",
            xp: 25,
            timestamp: new Date(Date.now() - 15 * 60 * 1000) // 15 min ago
        },
        {
            id: "2",
            type: "streak_milestone" as ActivityType,
            title: "3-day streak achieved! 🔥",
            description: "Keep it up!",
            xp: 50,
            timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000) // 2 hours ago
        },
        {
            id: "3",
            type: "xp_earned" as ActivityType,
            title: "Earned bonus XP",
            description: "First task of the day",
            xp: 15,
            timestamp: new Date(Date.now() - 24 * 60 * 60 * 1000) // yesterday
        }
    ]

    const limitedActivities = displayActivities.slice(0, maxItems)

    return (
        <GlassCard
            variant="default"
            padding="lg"
            radius="xl"
            className={cn("animate-fade-in", className)}
        >
            {/* Header */}
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-neutral-900 dark:text-white">
                    Recent Activity
                </h3>
                {displayActivities.length > maxItems && (
                    <button className={cn(
                        "text-sm font-medium text-primary-600 dark:text-primary-400",
                        "hover:text-primary-700 dark:hover:text-primary-300",
                        "transition-colors"
                    )}>
                        View all
                    </button>
                )}
            </div>

            {/* Activity list or empty state */}
            {limitedActivities.length > 0 ? (
                <div className="space-y-0">
                    {limitedActivities.map((activity, index) => (
                        <ActivityItem
                            key={activity.id}
                            activity={activity}
                            isLast={index === limitedActivities.length - 1}
                            delay={index * 100}
                        />
                    ))}
                </div>
            ) : (
                <EmptyState />
            )}
        </GlassCard>
    )
}

export default RecentActivity
