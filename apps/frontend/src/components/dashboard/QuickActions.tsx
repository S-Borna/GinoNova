"use client"

/**
 * ============================================================================
 * QUICK ACTIONS - Apple-Inspired Action Buttons
 * ============================================================================
 *
 * Design Philosophy:
 * - Inspired by Apple's card-based quick actions
 * - Large, tappable targets with clear icons
 * - Gradient backgrounds with hover effects
 * - Encourages immediate action
 *
 * Features:
 * - Primary CTA: Start/Continue Studyflow
 * - Secondary actions: View modules, check progress
 * - Responsive grid layout
 * - Animated hover states
 *
 * @phase D.2 - Dashboard UI Complete
 * @design Apple Fitness+ quick action cards
 */

import Link from "next/link"
import { cn } from "@/lib/utils"
import {
    PlayCircle,
    BookOpen,
    TrendingUp,
    Sparkles,
    ArrowRight,
    type LucideIcon
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface QuickAction {
    id: string
    title: string
    description: string
    icon: LucideIcon
    href: string
    gradient: string
    iconBg: string
    isPrimary?: boolean
}

interface QuickActionsProps {
    className?: string
    hasActiveStudyflow?: boolean
    currentModule?: {
        id: string
        name: string
        progress: number
    }
}

/* ============================================================================
   ACTION CARD COMPONENT
   ============================================================================ */

interface ActionCardProps {
    action: QuickAction
    delay?: number
}

function ActionCard({ action, delay = 0 }: ActionCardProps) {
    const Icon = action.icon

    if (action.isPrimary) {
        // Primary action with gradient background
        return (
            <Link prefetch={false} href={action.href}>
                <div
                    className="flex items-center gap-4 p-6 bg-gradient-to-r from-indigo-500 to-purple-600 text-white rounded-xl hover:shadow-lg hover:-translate-y-0.5 transition-all duration-200 animate-fade-in-up"
                    style={{ animationDelay: `${delay}ms` }}
                >
                    <div className="w-12 h-12 rounded-xl bg-white/20 backdrop-blur-sm flex items-center justify-center">
                        <Icon className="h-6 w-6 text-white" />
                    </div>
                    <div>
                        <h3 className="font-semibold text-lg flex items-center gap-2">
                            {action.title}
                            <Sparkles className="h-4 w-4 text-white/80" />
                        </h3>
                        <p className="text-sm text-white/80">
                            {action.description}
                        </p>
                    </div>
                    <ArrowRight className="h-5 w-5 ml-auto" />
                </div>
            </Link>
        )
    }

    // Secondary action with white background
    return (
        <Link prefetch={false} href={action.href}>
            <div
                className="flex items-center gap-4 p-6 bg-white dark:bg-neutral-800 rounded-xl border border-gray-100 dark:border-neutral-700 shadow-sm hover:shadow-md hover:-translate-y-0.5 transition-all duration-200 animate-fade-in-up"
                style={{ animationDelay: `${delay}ms` }}
            >
                <div className={cn(
                    "w-12 h-12 rounded-xl flex items-center justify-center",
                    action.iconBg
                )}>
                    <Icon className="h-6 w-6 text-gray-700 dark:text-neutral-200" />
                </div>
                <div>
                    <h3 className="font-semibold text-gray-900 dark:text-white">
                        {action.title}
                    </h3>
                    <p className="text-sm text-gray-500 dark:text-neutral-400">
                        {action.description}
                    </p>
                </div>
                <ArrowRight className="h-5 w-5 ml-auto text-gray-400 dark:text-neutral-500" />
            </div>
        </Link>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function QuickActions({
    className,
    hasActiveStudyflow = false,
    currentModule
}: QuickActionsProps) {
    // Build actions based on context
    const actions: QuickAction[] = [
        {
            id: "studyflow",
            title: hasActiveStudyflow ? "Continue Studyflow" : "Start Studyflow",
            description: hasActiveStudyflow
                ? "Pick up where you left off"
                : "Begin your daily learning session",
            icon: PlayCircle,
            href: "/studyflow",
            gradient: "bg-gradient-to-br from-primary-500 to-primary-600",
            iconBg: "bg-gradient-to-br from-primary-500 to-primary-600",
            isPrimary: true
        },
        {
            id: "modules",
            title: currentModule ? `Continue ${currentModule.name}` : "Browse Modules",
            description: currentModule
                ? `${currentModule.progress}% complete`
                : "Explore all learning paths",
            icon: BookOpen,
            href: currentModule ? `/modules/${currentModule.id}` : "/modules",
            gradient: "bg-gradient-to-br from-emerald-500 to-teal-500",
            iconBg: "bg-emerald-100 dark:bg-emerald-900/50"
        },
        {
            id: "progress",
            title: "View Progress",
            description: "Track your learning journey",
            icon: TrendingUp,
            href: "/progress",
            gradient: "bg-gradient-to-br from-amber-500 to-orange-500",
            iconBg: "bg-amber-100 dark:bg-amber-900/50"
        }
    ]

    return (
        <section className={cn("", className)}>
            {/* Section header */}
            <div className="flex items-center justify-between mb-6">
                <h2 className="text-xl font-bold text-gray-900 dark:text-white">
                    Quick Actions
                </h2>
            </div>

            {/* Actions grid */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {actions.map((action, index) => (
                    <ActionCard
                        key={action.id}
                        action={action}
                        delay={index * 100}
                    />
                ))}
            </div>
        </section>
    )
}

export default QuickActions
