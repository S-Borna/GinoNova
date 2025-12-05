"use client"

/**
 * ============================================================================
 * MODULES LIST PAGE — Design System v2.0 + Platform Selection
 * ============================================================================
 *
 * Updated with @saas/ui design system components:
 * - PageLayout for consistent layout
 * - Headline for typography
 * - Section/Block for content organization
 * - PlatformSelector for OS/distro selection with wave animation
 *
 * @phase DS.2 - Design System Application Layer
 * @phase FAS-3.1 - OS-Adaptive Content System
 */

import { useState, useEffect } from "react"
import Link from "next/link"
import { useRouter } from "next/navigation"
import { motion, AnimatePresence } from "framer-motion"
import { getModules, ModulePublic } from "@/lib/modules"
import { getTasksForModule, TaskPublic } from "@/lib/tasks"
import { getUserProgress, ProgressPublic } from "@/lib/progress"
import { useAuth } from "@/components/auth"
import { usePlatform, LINUX_DISTROS } from "@/hooks/useOperatingSystem"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { ModuleCard, ModuleStatus } from "@/components/modules"
import { PlatformBadge } from "@/components/onboarding"
import { BookOpen, Trophy, RefreshCw, AlertCircle, Settings2, Sparkles } from "lucide-react"

// @saas/ui Design System
import { PageLayout, Section, Block, Headline, Subtext } from "@saas/ui"

/* ============================================================================
   TYPES
   ============================================================================ */

interface EnhancedModule extends ModulePublic {
    orderIndex: number
    icon: string
    progress: number
    tasksCompleted: number
    totalTasks: number
    status: ModuleStatus
    estimatedHours: number
    prerequisiteModule?: string
    tags?: string[]
    xp?: number
}

/* ============================================================================
   MODULE ICONS (emoji mapping)
   ============================================================================ */

const moduleIcons: Record<string, string> = {
    onboarding: "🚀",
    foundations: "📚",
    linux: "🐧",
    shell: "💻",
    git: "🔀",
    networking: "🌐",
    cloud: "☁️",
    aws: "☁️",
    iac: "🏗️",
    terraform: "🏗️",
    containers: "📦",
    docker: "🐳",
    kubernetes: "⚙️",
    k8s: "⚙️",
    default: "📖",
}

function getModuleIcon(name: string): string {
    const lower = name.toLowerCase()
    for (const [key, icon] of Object.entries(moduleIcons)) {
        if (lower.includes(key)) {
            return icon
        }
    }
    return moduleIcons.default
}

/* ============================================================================
   MOCK MODULES DATA — Fallback when backend is unavailable
   ============================================================================ */

const MOCK_MODULES: EnhancedModule[] = [
    {
        id: "m1",
        name: "DevOps Foundations",
        slug: "devops-foundations",
        description: "Introduktion till DevOps-kultur, principer och practices. Lär dig grunderna i continuous integration och delivery.",
        order_index: 1,
        orderIndex: 1,
        difficulty: "beginner",
        estimated_hours: 4,
        estimatedHours: 4,
        prerequisites: [],
        is_active: true,
        track_id: "bootcamp",
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
        icon: "🚀",
        progress: 0,
        tasksCompleted: 0,
        totalTasks: 8,
        status: "not_started",
        tags: ["Culture", "CI/CD", "Basics"],
        xp: 400,
    },
    {
        id: "m2",
        name: "Linux Fundamentals",
        slug: "linux-fundamentals",
        description: "Behärska Linux från kommandoraden. Filhantering, permissions, processhantering och shell scripting.",
        order_index: 2,
        orderIndex: 2,
        difficulty: "beginner",
        estimated_hours: 8,
        estimatedHours: 8,
        prerequisites: ["m1"],
        is_active: true,
        track_id: "bootcamp",
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
        icon: "🐧",
        progress: 0,
        tasksCompleted: 0,
        totalTasks: 12,
        status: "not_started",
        tags: ["CLI", "System Admin", "Shell"],
        xp: 800,
    },
    {
        id: "m3",
        name: "Git & Version Control",
        slug: "git-version-control",
        description: "Versionskontroll med Git. Branches, merging, rebasing och samarbete med GitHub/GitLab.",
        order_index: 3,
        orderIndex: 3,
        difficulty: "beginner",
        estimated_hours: 6,
        estimatedHours: 6,
        prerequisites: ["m2"],
        is_active: true,
        track_id: "bootcamp",
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
        icon: "🔀",
        progress: 0,
        tasksCompleted: 0,
        totalTasks: 10,
        status: "not_started",
        tags: ["Version Control", "GitHub", "Collaboration"],
        xp: 600,
    },
    {
        id: "m4",
        name: "Docker Containers",
        slug: "docker-containers",
        description: "Containerisering med Docker. Images, containers, networking, volumes och Docker Compose.",
        order_index: 4,
        orderIndex: 4,
        difficulty: "intermediate",
        estimated_hours: 10,
        estimatedHours: 10,
        prerequisites: ["m3"],
        is_active: true,
        track_id: "bootcamp",
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
        icon: "🐳",
        progress: 0,
        tasksCompleted: 0,
        totalTasks: 15,
        status: "not_started",
        tags: ["Containers", "DevOps", "Microservices"],
        xp: 1000,
    },
    {
        id: "m5",
        name: "CI/CD Pipelines",
        slug: "cicd-pipelines",
        description: "Bygg automatiserade pipelines med GitHub Actions, Jenkins och GitLab CI. Test, build och deploy.",
        order_index: 5,
        orderIndex: 5,
        difficulty: "intermediate",
        estimated_hours: 8,
        estimatedHours: 8,
        prerequisites: ["m4"],
        is_active: true,
        track_id: "bootcamp",
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
        icon: "🚀",
        progress: 0,
        tasksCompleted: 0,
        totalTasks: 12,
        status: "not_started",
        tags: ["Pipelines", "Automation", "Deploy"],
        xp: 800,
    },
    {
        id: "m6",
        name: "Cloud Fundamentals (AWS)",
        slug: "cloud-aws",
        description: "Amazon Web Services grunderna. EC2, S3, IAM, VPC och grundläggande arkitektur.",
        order_index: 6,
        orderIndex: 6,
        difficulty: "intermediate",
        estimated_hours: 12,
        estimatedHours: 12,
        prerequisites: ["m5"],
        is_active: true,
        track_id: "bootcamp",
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
        icon: "☁️",
        progress: 0,
        tasksCompleted: 0,
        totalTasks: 16,
        status: "not_started",
        tags: ["Cloud", "AWS", "Infrastructure"],
        xp: 1200,
    },
    {
        id: "m7",
        name: "Infrastructure as Code",
        slug: "infrastructure-as-code",
        description: "Terraform och Ansible för att automatisera infrastruktur. Provisioning, konfiguration och state management.",
        order_index: 7,
        orderIndex: 7,
        difficulty: "advanced",
        estimated_hours: 10,
        estimatedHours: 10,
        prerequisites: ["m6"],
        is_active: true,
        track_id: "bootcamp",
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
        icon: "🏗️",
        progress: 0,
        tasksCompleted: 0,
        totalTasks: 14,
        status: "not_started",
        tags: ["IaC", "Terraform", "Ansible"],
        xp: 1000,
    },
    {
        id: "m8",
        name: "Kubernetes Orchestration",
        slug: "kubernetes-orchestration",
        description: "Container orchestration med Kubernetes. Pods, deployments, services, ingress och Helm.",
        order_index: 8,
        orderIndex: 8,
        difficulty: "advanced",
        estimated_hours: 14,
        estimatedHours: 14,
        prerequisites: ["m7"],
        is_active: true,
        track_id: "bootcamp",
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
        icon: "☸️",
        progress: 0,
        tasksCompleted: 0,
        totalTasks: 18,
        status: "not_started",
        tags: ["K8s", "Orchestration", "Helm"],
        xp: 1400,
    },
]

/* ============================================================================
   SKELETON COMPONENTS — Matches SkillsMapCard Design
   ============================================================================ */

function ModuleCardSkeleton() {
    return (
        <div className="bg-gradient-to-br from-zinc-900/90 via-zinc-900/95 to-zinc-950/90 rounded-2xl border border-white/[0.08] p-6 animate-pulse">
            {/* Top row: Icon + Status */}
            <div className="flex items-start justify-between mb-4">
                <div className="w-14 h-14 rounded-xl bg-zinc-800" />
                <div className="w-24 h-7 rounded-full bg-zinc-800" />
            </div>
            {/* Title */}
            <div className="h-6 w-3/4 rounded bg-zinc-800 mb-2" />
            {/* Description */}
            <div className="space-y-2 mb-4">
                <div className="h-4 w-full rounded bg-zinc-800" />
                <div className="h-4 w-2/3 rounded bg-zinc-800" />
            </div>
            {/* Tags */}
            <div className="flex gap-2 mb-4">
                <div className="h-5 w-16 rounded bg-zinc-800" />
                <div className="h-5 w-20 rounded bg-zinc-800" />
                <div className="h-5 w-14 rounded bg-zinc-800" />
            </div>
            {/* Progress */}
            <div className="mb-4">
                <div className="flex justify-between mb-2">
                    <div className="h-3 w-20 rounded bg-zinc-800" />
                    <div className="h-3 w-10 rounded bg-zinc-800" />
                </div>
                <div className="h-2 w-full rounded-full bg-zinc-800" />
            </div>
            {/* Meta row */}
            <div className="flex gap-4 mb-4">
                <div className="h-4 w-16 rounded bg-zinc-800" />
                <div className="h-4 w-12 rounded bg-zinc-800" />
                <div className="h-4 w-16 rounded bg-zinc-800" />
            </div>
            {/* Button */}
            <div className="h-12 w-full rounded-xl bg-zinc-800" />
        </div>
    )
}

function PageSkeleton() {
    return (
        <div className="space-y-8">
            {/* Header skeleton */}
            <div className="rounded-3xl bg-gradient-to-br from-zinc-900 via-purple-950/30 to-zinc-900 border border-purple-500/20 p-8">
                <div className="flex items-center gap-3 mb-3">
                    <div className="w-10 h-10 rounded-xl bg-zinc-800" />
                    <div className="h-4 w-24 rounded bg-zinc-800" />
                </div>
                <div className="h-10 w-64 rounded bg-zinc-800 mb-2" />
                <div className="h-5 w-40 rounded bg-zinc-800 mb-6" />
                <div className="bg-zinc-800/50 rounded-2xl p-5">
                    <div className="flex justify-between mb-3">
                        <div className="h-4 w-28 rounded bg-zinc-700" />
                        <div className="h-5 w-12 rounded bg-zinc-700" />
                    </div>
                    <div className="h-3 w-full rounded-full bg-zinc-700" />
                </div>
            </div>
            {/* Grid skeleton */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {Array.from({ length: 6 }).map((_, i) => (
                    <ModuleCardSkeleton key={i} />
                ))}
            </div>
        </div>
    )
}

/* ============================================================================
   ERROR STATE
   ============================================================================ */

function ErrorState({ error, onRetry }: { error: string; onRetry: () => void }) {
    return (
        <div className="bg-white dark:bg-neutral-800 rounded-xl shadow-sm border border-gray-100 dark:border-neutral-700 p-8 max-w-md mx-auto text-center">
            <div className="w-16 h-16 rounded-full mx-auto mb-4 bg-red-100 dark:bg-red-900/30 flex items-center justify-center">
                <AlertCircle className="w-8 h-8 text-red-500" />
            </div>
            <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                Unable to Load Modules
            </h2>
            <p className="text-gray-600 dark:text-neutral-400 mb-6">{error}</p>
            <Button onClick={onRetry} className="rounded-xl">
                <RefreshCw className="w-4 h-4 mr-2" />
                Try Again
            </Button>
        </div>
    )
}

/* ============================================================================
   EMPTY STATE
   ============================================================================ */

function EmptyState() {
    return (
        <div className="bg-white dark:bg-neutral-800 rounded-xl shadow-sm border border-gray-100 dark:border-neutral-700 p-8 max-w-md mx-auto text-center">
            <div className="w-16 h-16 rounded-full mx-auto mb-4 bg-indigo-100 dark:bg-indigo-900/30 flex items-center justify-center">
                <BookOpen className="w-8 h-8 text-indigo-500" />
            </div>
            <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                No Modules Yet
            </h2>
            <p className="text-gray-600 dark:text-neutral-400 mb-6">
                Modules will appear here once they&apos;re added to your learning path.
            </p>
            <Link href="/modules/new">
                <Button className="rounded-xl">Create First Module</Button>
            </Link>
        </div>
    )
}

/* ============================================================================
   PREMIUM HEADER COMPONENT
   ============================================================================ */

interface HeaderProps {
    totalModules: number
    completedModules: number
    overallProgress: number
    onRefresh: () => void
    isRefreshing: boolean
    onChangePlatform?: () => void
}

function Header({
    totalModules,
    completedModules,
    overallProgress,
    onRefresh,
    isRefreshing,
}: HeaderProps) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "relative overflow-hidden rounded-3xl mb-8",
                "bg-gradient-to-br from-zinc-900 via-purple-950/30 to-zinc-900",
                "border border-purple-500/20",
                "p-8"
            )}
        >
            {/* Ambient glow effects */}
            <div className="absolute top-0 right-0 w-[400px] h-[400px] bg-purple-500/15 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/4" />
            <div className="absolute bottom-0 left-0 w-[300px] h-[300px] bg-emerald-500/10 rounded-full blur-[80px] translate-y-1/2 -translate-x-1/4" />

            {/* Animated sparkles */}
            <motion.div
                className="absolute top-6 right-16 text-purple-400/50"
                animate={{ rotate: 360 }}
                transition={{ duration: 8, repeat: Infinity, ease: "linear" }}
            >
                <Sparkles className="w-5 h-5" />
            </motion.div>

            <div className="relative">
                <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
                    <div>
                        <div className="flex items-center gap-3 mb-3">
                            <div className={cn(
                                "p-2 rounded-xl",
                                "bg-gradient-to-br from-purple-500/20 to-purple-600/10",
                                "border border-purple-500/30"
                            )}>
                                <BookOpen className="w-5 h-5 text-purple-400" />
                            </div>
                            <span className="text-purple-400 font-semibold text-sm uppercase tracking-wider">
                                Learning Path
                            </span>
                        </div>
                        <h1 className={cn(
                            "text-3xl md:text-4xl font-black mb-2",
                            "bg-gradient-to-r from-white via-purple-200 to-white bg-clip-text text-transparent"
                        )}>
                            Your DevOps Journey
                        </h1>
                        <p className="text-zinc-400">
                            {totalModules} modules • {completedModules} completed
                        </p>
                    </div>

                    <div className="flex items-center gap-3">
                        {/* Platform Badge */}
                        <PlatformBadge />

                        {/* Trophy badge with glow */}
                        <div className={cn(
                            "flex items-center gap-2 px-4 py-3 rounded-xl",
                            "bg-gradient-to-br from-amber-600/20 to-amber-500/10",
                            "border border-amber-500/30",
                            "shadow-[0_0_25px_rgba(245,158,11,0.15)]"
                        )}>
                            <div className={cn(
                                "w-8 h-8 rounded-lg",
                                "bg-gradient-to-br from-amber-500 to-orange-600",
                                "flex items-center justify-center"
                            )}>
                                <Trophy className="w-4 h-4 text-white" />
                            </div>
                            <span className="font-bold text-amber-400">
                                {completedModules}/{totalModules}
                            </span>
                        </div>

                        {/* Refresh button */}
                        <Button
                            variant="ghost"
                            size="sm"
                            onClick={onRefresh}
                            disabled={isRefreshing}
                            className="rounded-xl text-zinc-400 hover:text-white hover:bg-white/10"
                        >
                            <RefreshCw className={cn("w-4 h-4", isRefreshing && "animate-spin")} />
                        </Button>
                    </div>
                </div>

                {/* Overall progress bar with glow */}
                <div className={cn(
                    "mt-6 p-5 rounded-2xl",
                    "bg-gradient-to-br from-zinc-800/80 to-zinc-900/80",
                    "border border-zinc-700/50"
                )}>
                    <div className="flex items-center justify-between text-sm mb-3">
                        <span className="text-zinc-400 font-medium">Overall Progress</span>
                        <span className={cn(
                            "font-bold text-lg",
                            overallProgress === 100 ? "text-emerald-400" : "text-purple-400"
                        )}>
                            {overallProgress}%
                        </span>
                    </div>
                    <div className="relative w-full h-3 bg-zinc-800 rounded-full overflow-hidden">
                        <motion.div
                            initial={{ width: 0 }}
                            animate={{ width: `${overallProgress}%` }}
                            transition={{ duration: 1, ease: "easeOut" }}
                            className={cn(
                                "h-full rounded-full",
                                overallProgress === 100
                                    ? "bg-gradient-to-r from-emerald-500 to-teal-400"
                                    : "bg-gradient-to-r from-purple-600 to-purple-400",
                                overallProgress === 100
                                    ? "shadow-[0_0_20px_rgba(16,185,129,0.5)]"
                                    : "shadow-[0_0_20px_rgba(139,92,246,0.5)]"
                            )}
                        />
                    </div>
                    <p className="text-sm text-zinc-500 mt-3">
                        {overallProgress === 100
                            ? "🎉 Amazing! You've completed all modules!"
                            : `Keep crushing it! ${totalModules - completedModules} modules to go 🚀`}
                    </p>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MODULES PAGE
   ============================================================================ */

export default function ModulesPage() {
    const router = useRouter()
    const { user } = useAuth()
    const { hasSelected, isLoading: platformLoading, os, distro } = usePlatform()
    const [modules, setModules] = useState<EnhancedModule[]>([])
    const [loading, setLoading] = useState(true)
    const [refreshing, setRefreshing] = useState(false)
    const [error, setError] = useState<string | null>(null)

    const fetchModules = async (isRefresh = false) => {
        if (isRefresh) {
            setRefreshing(true)
        } else {
            setLoading(true)
        }
        setError(null)

        try {
            const result = await getModules()
            if (result.ok && result.data.length > 0) {
                // Fetch user progress if logged in
                let userProgress: ProgressPublic[] = []
                if (user?.id) {
                    const progressResult = await getUserProgress(user.id)
                    if (progressResult.ok) {
                        userProgress = progressResult.data
                    }
                }

                // Create a map of module_id -> progress
                const progressMap = new Map<string, ProgressPublic>()
                userProgress.forEach(p => {
                    if (p.module_id) {
                        progressMap.set(p.module_id, p)
                    }
                })

                // Create a map of task progress by task_id
                const taskProgressMap = new Map<string, ProgressPublic>()
                userProgress.forEach(p => {
                    if (p.task_id) {
                        taskProgressMap.set(p.task_id, p)
                    }
                })

                // Fetch tasks for each module to get accurate counts
                const modulesWithTasks = await Promise.all(
                    result.data.map(async (mod, index) => {
                        // Get tasks for this module
                        const tasksResult = await getTasksForModule(mod.id)
                        const tasks: TaskPublic[] = tasksResult.ok ? tasksResult.data : []
                        const totalTasks = tasks.length

                        // Count completed tasks from progress data
                        const completedTasks = tasks.filter(t => {
                            const taskProgress = taskProgressMap.get(t.id)
                            return taskProgress?.status === "completed"
                        }).length

                        // Calculate progress percentage
                        const progressPercent = totalTasks > 0
                            ? Math.round((completedTasks / totalTasks) * 100)
                            : 0

                        // Determine status - NO LOCKING, all modules open!
                        let status: ModuleStatus = "not_started"
                        if (progressPercent === 100) {
                            status = "complete"
                        } else if (progressPercent > 0) {
                            status = "in_progress"
                        }
                        // All modules are accessible - no prerequisites blocking

                        return {
                            ...mod,
                            orderIndex: mod.order_index || index + 1,
                            icon: getModuleIcon(mod.name),
                            progress: progressPercent,
                            tasksCompleted: completedTasks,
                            totalTasks,
                            status,
                            estimatedHours: mod.estimated_hours || 4 + index * 2,
                            prerequisiteModule: mod.prerequisites?.[0],
                        } as EnhancedModule
                    })
                )

                setModules(modulesWithTasks)
            } else {
                // Fallback to mock data when backend unavailable
                console.log("[Modules] Using mock data - backend unavailable or empty")
                setModules(MOCK_MODULES)
            }
        } catch {
            // Fallback to mock data on error
            console.log("[Modules] Using mock data - fetch error")
            setModules(MOCK_MODULES)
        } finally {
            setLoading(false)
            setRefreshing(false)
        }
    }

    useEffect(() => {
        fetchModules()
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [user?.id])

    const handleRefresh = () => {
        fetchModules(true)
    }

    // Calculate stats
    const totalModules = modules.length
    const completedModules = modules.filter((m) => m.status === "complete").length
    const overallProgress =
        totalModules > 0 ? Math.round((completedModules / totalModules) * 100) : 0

    // Redirect to /learn if OS not selected
    useEffect(() => {
        if (!platformLoading && !hasSelected) {
            console.log("[Modules] No OS selected, redirecting to /learn")
            router.push("/learn")
        }
    }, [platformLoading, hasSelected, router])

    // Platform selection loading or redirecting
    if (platformLoading || !hasSelected) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <PageSkeleton />
            </PageLayout>
        )
    }

    if (loading) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <PageSkeleton />
            </PageLayout>
        )
    }

    if (error) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <ErrorState error={error ?? "Ett fel uppstod"} onRetry={handleRefresh} />
            </PageLayout>
        )
    }

    if (modules.length === 0) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <EmptyState />
            </PageLayout>
        )
    }

    return (
        <PageLayout maxWidth="wide" background="gray">
            <AnimatePresence>
                <motion.div
                    className="space-y-8"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 0.3 }}
                >
                    {/* Header */}
                    <Section spacing="none">
                        <motion.div
                            initial={{ opacity: 0, y: -20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.1, duration: 0.4 }}
                        >
                            <Header
                                totalModules={totalModules}
                                completedModules={completedModules}
                                overallProgress={overallProgress}
                                onRefresh={handleRefresh}
                                isRefreshing={refreshing}
                            />
                        </motion.div>
                    </Section>

                    {/* Modules grid with wave animation */}
                    <Section spacing="none">
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                            {modules.map((module, index) => (
                                <motion.div
                                    key={module.id}
                                    initial={{ opacity: 0, y: 50, scale: 0.9 }}
                                    animate={{ opacity: 1, y: 0, scale: 1 }}
                                    transition={{
                                        type: "spring",
                                        stiffness: 100,
                                        damping: 15,
                                        delay: 0.2 + index * 0.08, // Wave effect
                                    }}
                                >
                                    <ModuleCard
                                        id={module.id}
                                        orderIndex={module.orderIndex}
                                        title={module.name}
                                        description={module.description || "No description available"}
                                        icon={module.icon}
                                        progress={module.progress}
                                        tasksCompleted={module.tasksCompleted}
                                        totalTasks={module.totalTasks}
                                        status={module.status}
                                        estimatedHours={module.estimatedHours}
                                        prerequisiteModule={module.prerequisiteModule}
                                        tags={module.tags}
                                        xp={module.xp}
                                        difficulty={module.difficulty as "beginner" | "intermediate" | "advanced" | "expert"}
                                    />
                                </motion.div>
                            ))}
                        </div>
                    </Section>
                </motion.div>
            </AnimatePresence>
        </PageLayout>
    )
}
