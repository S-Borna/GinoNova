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
import { GlassCard } from "@/components/ui/glass-card"
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

    return (
        <Link href={action.href}>
            <GlassCard
                variant="default"
                padding="lg"
                radius="xl"
                interactive
                className={cn(
                    "h-full animate-fade-in-up group relative overflow-hidden",
                    "hover:shadow-glow transition-all duration-300",
                    action.isPrimary && "ring-2 ring-primary-200 dark:ring-primary-800"
                )}
                style={{ animationDelay: `${delay}ms` }}
            >
                {/* Gradient overlay for primary */}
                {action.isPrimary && (
                    <div className={cn(
                        "absolute inset-0 opacity-5 dark:opacity-10",
                        action.gradient
                    )} />
                )}

                <div className="relative z-10">
                    {/* Icon container */}
                    <div className={cn(
                        "w-14 h-14 rounded-2xl flex items-center justify-center mb-4",
                        "shadow-sm transition-transform duration-300",
                        "group-hover:scale-110 group-hover:shadow-md",
                        action.iconBg
                    )}>
                        <Icon className={cn(
                            "h-7 w-7",
                            action.isPrimary
                                ? "text-white"
                                : "text-neutral-700 dark:text-neutral-200"
                        )} />
                    </div>

                    {/* Content */}
                    <div className="space-y-1">
                        <h3 className="font-semibold text-neutral-900 dark:text-white flex items-center gap-2">
                            {action.title}
                            {action.isPrimary && (
                                <Sparkles className="h-4 w-4 text-primary-500" />
                            )}
                        </h3>
                        <p className="text-sm text-neutral-500 dark:text-neutral-400">
                            {action.description}
                        </p>
                    </div>

                    {/* Action indicator */}
                    <div className={cn(
                        "mt-4 flex items-center text-sm font-medium",
                        "text-primary-600 dark:text-primary-400",
                        "opacity-0 group-hover:opacity-100 transition-opacity"
                    )}>
                        <span>Get started</span>
                        <ArrowRight className="h-4 w-4 ml-1 transition-transform group-hover:translate-x-1" />
                    </div>
                </div>
            </GlassCard>
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
            iconBg: "bg-gradient-to-br from-emerald-100 to-teal-100 dark:from-emerald-900/50 dark:to-teal-900/50"
        },
        {
            id: "progress",
            title: "View Progress",
            description: "Track your learning journey",
            icon: TrendingUp,
            href: "/progress",
            gradient: "bg-gradient-to-br from-amber-500 to-orange-500",
            iconBg: "bg-gradient-to-br from-amber-100 to-orange-100 dark:from-amber-900/50 dark:to-orange-900/50"
        }
    ]

    return (
        <section className={cn("animate-fade-in", className)}>
            {/* Section header */}
            <div className="flex items-center justify-between mb-4">
                <h2 className="text-lg font-semibold text-neutral-900 dark:text-white">
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
