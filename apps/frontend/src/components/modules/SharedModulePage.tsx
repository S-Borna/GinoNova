/**
 * ============================================================================
 * SHARED MODULE PAGE COMPONENT
 * ============================================================================
 *
 * EN komponent för att visa moduler - används av:
 * - Camp DevOps (/modules/[slug])
 * - SkillsMaps (/skillsmaps/[slug])
 * - Alla andra sidor som visar moduler
 *
 * Hämtar data från backend API: /api/modules/full/{slug}
 * Ingen statisk data i frontend - backend är källan.
 *
 * @phase ARCHITECTURE-UNIFICATION
 */

"use client"

import { useState, useEffect } from "react"
import Link from "next/link"
import { useRouter } from "next/navigation"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { CosmicAurora } from "@/components/ui/cosmic-aurora"
import { TentaCountdown } from "@/components/ui/tenta-countdown"
import { saveLastActivity } from "@/components/dashboard/ContinueLearning"
import { TutorialSection } from "@/components/tutorials"
import { findTutorialsByModule, TUTORIALS } from "@/data/tutorials"
import {
    ArrowLeft,
    CheckCircle2,
    Circle,
    Clock,
    BookOpen,
    Zap,
    Trophy,
    Target,
    ChevronRight,
    Play,
    Terminal,
    Server,
    Container,
    Network,
    FileText,
    Shield,
    Settings,
    Bot,
    Sparkles,
    AlertCircle,
    RefreshCw
} from "lucide-react"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

// ============================================================================
// TYPES - Matches backend content structure
// ============================================================================

interface ModuleTask {
    title: string
    slug?: string
    description: string
    difficulty: string
    estimated_minutes: number
    xp_reward: number
    order_index?: number
    content?: string
}

interface ModuleGroup {
    id: string
    title: string
    subtitle: string
    icon: string
    color: string
    bgGlow: string
    taskIds: string[]
}

interface FullModule {
    id: string
    slug: string
    title?: string
    name?: string
    description: string
    icon?: string
    difficulty: string
    estimated_hours: number
    exam_date?: string
    tasks: ModuleTask[]
    groups?: ModuleGroup[]
    tags?: string[]
}

// ============================================================================
// ICON MAPPING
// ============================================================================

const iconMap: Record<string, React.ReactNode> = {
    "Network": <Network className="w-6 h-6" />,
    "Terminal": <Terminal className="w-6 h-6" />,
    "Server": <Server className="w-6 h-6" />,
    "Container": <Container className="w-6 h-6" />,
    "FileText": <FileText className="w-6 h-6" />,
    "Shield": <Shield className="w-6 h-6" />,
    "Settings": <Settings className="w-6 h-6" />,
    "Bot": <Bot className="w-6 h-6" />,
    "BookOpen": <BookOpen className="w-6 h-6" />,
}

function getIcon(iconName: string): React.ReactNode {
    return iconMap[iconName] || <BookOpen className="w-6 h-6" />
}

// Remove "Modul X:" prefix from group titles to show cleaner names
function cleanGroupTitle(title: string): string {
    return title.replace(/^Modul \d+:\s*/i, '')
}

// ============================================================================
// MODULE CONFIG - Colors and display settings
// ============================================================================

const moduleConfig: Record<string, { color: string; icon: string; tags: string[] }> = {
    "doe25-tenta": {
        color: "#F59E0B",
        icon: "📝",
        tags: ["Tenta", "Linux", "Bash", "DevOps"]
    },
    "linux-247": {
        color: "#FCC624",
        icon: "🐧",
        tags: ["Linux", "CLI", "System Admin"]
    },
}

function getModuleConfig(slug: string) {
    return moduleConfig[slug] || { color: "#6366F1", icon: "📚", tags: ["DevOps"] }
}

// ============================================================================
// STATS CARD
// ============================================================================

function StatCard({
    icon,
    label,
    value,
    color
}: {
    icon: React.ReactNode
    label: string
    value: string | number
    color: string
}) {
    return (
        <motion.div
            whileHover={{ scale: 1.02 }}
            className={cn(
                "flex items-center gap-4 p-4 rounded-xl",
                "bg-white/5 border border-white/10",
                "hover:border-white/20 transition-colors"
            )}
        >
            <div className={cn(
                "w-12 h-12 rounded-xl flex items-center justify-center",
                `bg-gradient-to-br ${color}`
            )}>
                {icon}
            </div>
            <div>
                <p className="text-2xl font-bold text-white">{value}</p>
                <p className="text-sm text-zinc-400">{label}</p>
            </div>
        </motion.div>
    )
}

// ============================================================================
// LOADING STATE
// ============================================================================

function LoadingSkeleton() {
    return (
        <div className="min-h-screen bg-[#05050a] relative">
            <CosmicAurora />
            <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                <div className="space-y-8 animate-pulse">
                    <div className="h-64 rounded-3xl bg-zinc-900/50" />
                    <div className="h-16 rounded-2xl bg-zinc-900/50" />
                    <div className="space-y-4">
                        {[1, 2, 3].map(i => (
                            <div key={i} className="h-48 rounded-2xl bg-zinc-900/50" />
                        ))}
                    </div>
                </div>
            </div>
        </div>
    )
}

// ============================================================================
// ERROR STATE
// ============================================================================

function ErrorState({ error, onRetry }: { error: string; onRetry: () => void }) {
    return (
        <div className="min-h-screen bg-[#05050a] relative">
            <CosmicAurora />
            <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                <div className="max-w-md mx-auto text-center p-8 rounded-3xl bg-zinc-900/50 border border-red-500/30">
                    <AlertCircle className="w-16 h-16 text-red-400 mx-auto mb-4" />
                    <h2 className="text-xl font-bold text-white mb-2">Kunde inte ladda modul</h2>
                    <p className="text-zinc-400 mb-6">{error}</p>
                    <button
                        onClick={onRetry}
                        className="px-6 py-3 rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-medium flex items-center gap-2 mx-auto"
                    >
                        <RefreshCw className="w-4 h-4" />
                        Försök igen
                    </button>
                </div>
            </div>
        </div>
    )
}

// ============================================================================
// DEFAULT GROUPS - Used if module doesn't define groups
// ============================================================================

function createDefaultGroups(tasks: ModuleTask[]): ModuleGroup[] {
    // Group tasks by category or create single group
    return [{
        id: "all-tasks",
        title: "Tasks",
        subtitle: `${tasks.length} lektioner`,
        icon: "BookOpen",
        color: "from-purple-500 to-violet-500",
        bgGlow: "rgba(139, 92, 246, 0.2)",
        taskIds: tasks.map((_, i) => `task-${i}`)
    }]
}

// ============================================================================
// MAIN COMPONENT
// ============================================================================

interface SharedModulePageProps {
    slug: string
    backHref?: string
    backLabel?: string
}

export function SharedModulePage({
    slug,
    backHref = "/modules",
    backLabel = "Tillbaka"
}: SharedModulePageProps) {
    const router = useRouter()
    const [module, setModule] = useState<FullModule | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [completedTasks, setCompletedTasks] = useState<string[]>([])

    // Load progress from localStorage
    useEffect(() => {
        try {
            const saved = localStorage.getItem(`${slug}-completed-tasks`)
            if (saved) {
                setCompletedTasks(JSON.parse(saved))
            }
        } catch (e) {
            console.log("Could not load progress")
        }
    }, [slug])

    // Fetch module from backend
    const fetchModule = async () => {
        setLoading(true)
        setError(null)

        try {
            const res = await fetch(`${API_BASE_URL}/api/modules/full/${slug}`)

            if (!res.ok) {
                const err = await res.json().catch(() => ({ detail: "Modul hittades inte" }))
                throw new Error(err.detail || "Kunde inte hämta modul")
            }

            const data = await res.json()
            setModule(data)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Ett fel uppstod")
        } finally {
            setLoading(false)
        }
    }

    useEffect(() => {
        if (slug) {
            fetchModule()
        }
    }, [slug])

    // Track activity for Continue Learning feature
    useEffect(() => {
        if (module && !loading) {
            const moduleName = module.title || module.name || slug
            const totalTasks = module.tasks.length
            const completedCount = completedTasks.length
            const progressPercent = totalTasks > 0 ? Math.round((completedCount / totalTasks) * 100) : 0
            const totalMinutes = module.tasks.reduce((acc, t) => acc + (t.estimated_minutes || 30), 0)
            const remainingTasks = totalTasks - completedCount
            const avgMinutesPerTask = totalTasks > 0 ? totalMinutes / totalTasks : 30
            const estimatedMinutesRemaining = Math.round(remainingTasks * avgMinutesPerTask)

            // Find current task (first incomplete or last completed)
            const firstIncompleteTask = module.tasks.find(t => !completedTasks.includes(t.slug || t.title))
            const currentTaskTitle = firstIncompleteTask?.title || (completedCount > 0 ? "Review completed tasks" : undefined)

            saveLastActivity({
                moduleSlug: slug,
                moduleName,
                taskTitle: currentTaskTitle,
                progress: progressPercent,
                totalTasks,
                completedTasks: completedCount,
                estimatedMinutes: estimatedMinutesRemaining,
                icon: module.icon,
            })
        }
    }, [module, completedTasks, loading, slug])

    if (loading) return <LoadingSkeleton />
    if (error) return <ErrorState error={error} onRetry={fetchModule} />
    if (!module) return <ErrorState error="Modul hittades inte" onRetry={fetchModule} />

    const config = getModuleConfig(slug)
    const moduleName = module.title || module.name || slug
    const totalTasks = module.tasks.length
    const completedCount = completedTasks.length
    const progressPercent = totalTasks > 0 ? Math.round((completedCount / totalTasks) * 100) : 0
    const totalMinutes = module.tasks.reduce((acc, t) => acc + (t.estimated_minutes || 30), 0)
    const totalHours = Math.round(totalMinutes / 60)
    const totalXP = module.tasks.reduce((acc, t) => acc + (t.xp_reward || 100), 0)

    // Handle null/undefined/empty groups - use default if not properly defined
    const groups = (module.groups && module.groups.length > 0)
        ? module.groups
        : createDefaultGroups(module.tasks)

    const isTaskCompleted = (taskSlug: string) => completedTasks.includes(taskSlug)
    const getTaskByIndex = (index: number) => module.tasks[index]

    // Find first incomplete task
    const firstIncompleteTask = module.tasks.find(t => !completedTasks.includes(t.slug || t.title))

    return (
        <div className="min-h-screen bg-[#05050a] relative">
            <CosmicAurora />

            <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {/* Back Button */}
                <Link
                    href={backHref}
                    className={cn(
                        "inline-flex items-center gap-2 text-sm mb-8 px-4 py-2 rounded-xl",
                        "text-zinc-400 hover:text-white",
                        "bg-white/5 hover:bg-white/10 border border-white/10",
                        "transition-all duration-300"
                    )}
                >
                    <ArrowLeft className="w-4 h-4" />
                    {backLabel}
                </Link>

                {/* Hero Header */}
                <motion.div
                    initial={{ opacity: 0, y: -20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className={cn(
                        "relative overflow-hidden rounded-3xl mb-8",
                        "bg-gradient-to-br from-amber-500/10 via-orange-500/10 to-red-500/10",
                        "border border-amber-500/20",
                        "p-8 md:p-12"
                    )}
                    style={{
                        boxShadow: `0 0 80px ${config.color}20`
                    }}
                >
                    {/* Background Glow */}
                    <div
                        className="absolute top-0 right-0 w-96 h-96 rounded-full blur-[100px]"
                        style={{ backgroundColor: `${config.color}20` }}
                    />
                    <div className="absolute bottom-0 left-0 w-64 h-64 bg-purple-500/10 rounded-full blur-[80px]" />

                    <div className="relative">
                        <div className="flex flex-col md:flex-row md:items-start gap-6 mb-8">
                            {/* Icon */}
                            <motion.div
                                whileHover={{ scale: 1.05, rotate: 5 }}
                                className={cn(
                                    "w-24 h-24 rounded-3xl flex items-center justify-center shrink-0",
                                    "bg-gradient-to-br from-amber-500/30 to-orange-500/30",
                                    "border border-amber-500/40 shadow-lg"
                                )}
                                style={{ boxShadow: `0 0 40px ${config.color}30` }}
                            >
                                <span className="text-6xl">{config.icon}</span>
                            </motion.div>

                            <div className="flex-1">
                                <div className="flex items-center gap-3 mb-3">
                                    {config.tags.map(tag => (
                                        <span
                                            key={tag}
                                            className="px-3 py-1 rounded-full bg-amber-500/20 border border-amber-500/30 text-amber-400 text-xs font-bold uppercase tracking-wider"
                                        >
                                            {tag}
                                        </span>
                                    )).slice(0, 2)}
                                    <span className="px-3 py-1 rounded-full bg-purple-500/20 border border-purple-500/30 text-purple-400 text-xs font-bold">
                                        {totalTasks} Tasks
                                    </span>
                                </div>

                                <h1 className="text-3xl md:text-5xl font-black text-white mb-4">
                                    {moduleName}
                                </h1>

                                <p className="text-lg text-zinc-300 max-w-2xl mb-6">
                                    {module.description}
                                </p>

                                {/* Countdown for exam modules */}
                                {module.exam_date && (
                                    <TentaCountdown
                                        examDate={module.exam_date}
                                        className="mb-6"
                                    />
                                )}

                                {/* CTA */}
                                {firstIncompleteTask && (
                                    <Link href={`/modules/${slug}/tasks/${firstIncompleteTask.slug || firstIncompleteTask.title}`}>
                                        <motion.button
                                            whileHover={{ scale: 1.02 }}
                                            whileTap={{ scale: 0.98 }}
                                            className={cn(
                                                "flex items-center gap-3 px-6 py-3 rounded-xl",
                                                "bg-gradient-to-r from-purple-600 to-cyan-600",
                                                "text-white font-semibold",
                                                "shadow-lg shadow-purple-500/30",
                                                "hover:shadow-xl hover:shadow-purple-500/40",
                                                "transition-all duration-300"
                                            )}
                                        >
                                            <Play className="w-5 h-5 fill-white" />
                                            {completedCount > 0 ? "Fortsätt plugga" : "Börja plugga"}
                                            <ChevronRight className="w-5 h-5" />
                                        </motion.button>
                                    </Link>
                                )}
                            </div>
                        </div>

                        {/* Stats Grid */}
                        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                            <StatCard
                                icon={<Target className="w-6 h-6 text-white" />}
                                label="Tasks klara"
                                value={`${completedCount}/${totalTasks}`}
                                color="from-emerald-500 to-green-500"
                            />
                            <StatCard
                                icon={<Clock className="w-6 h-6 text-white" />}
                                label="Estimerad tid"
                                value={`${totalHours}h`}
                                color="from-blue-500 to-cyan-500"
                            />
                            <StatCard
                                icon={<Zap className="w-6 h-6 text-white" />}
                                label="XP att tjäna"
                                value={totalXP - (completedCount * 100)}
                                color="from-amber-500 to-orange-500"
                            />
                            <StatCard
                                icon={<Trophy className="w-6 h-6 text-white" />}
                                label="Progress"
                                value={`${progressPercent}%`}
                                color="from-purple-500 to-violet-500"
                            />
                        </div>
                    </div>
                </motion.div>

                {/* Progress Bar */}
                <div className="mb-8 p-4 rounded-2xl bg-zinc-900/50 border border-zinc-800">
                    <div className="flex justify-between text-sm mb-2">
                        <span className="text-zinc-400">Total progress</span>
                        <span className="text-purple-400 font-medium">{progressPercent}% klar</span>
                    </div>
                    <div className="h-3 bg-zinc-800 rounded-full overflow-hidden">
                        <motion.div
                            initial={{ width: 0 }}
                            animate={{ width: `${progressPercent}%` }}
                            transition={{ duration: 1, ease: "easeOut" }}
                            className="h-full bg-gradient-to-r from-purple-500 via-cyan-500 to-emerald-500 rounded-full"
                        />
                    </div>
                </div>

                {/* Task Groups */}
                <div className="space-y-6">
                    {groups.map((group, groupIndex) => {
                        // Find tasks for this group by matching slugs
                        // If group uses 'task-N' pattern, use all tasks
                        // Otherwise match by slug
                        const groupTasks = group.taskIds[0]?.startsWith('task-')
                            ? module.tasks
                            : module.tasks.filter(t => {
                                const taskSlug = t.slug || ''
                                return group.taskIds.includes(taskSlug)
                            })

                        // If no tasks found via slug, this is likely a default group - use all tasks
                        const tasksToShow = groupTasks.length > 0 ? groupTasks : module.tasks

                        const groupCompleted = tasksToShow.filter(t => isTaskCompleted(t.slug || t.title)).length
                        const groupPercent = tasksToShow.length > 0 ? Math.round((groupCompleted / tasksToShow.length) * 100) : 0

                        return (
                            <motion.div
                                key={group.id}
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: groupIndex * 0.1 }}
                                className={cn(
                                    "rounded-2xl overflow-hidden",
                                    "bg-[#0a0a0f] border border-zinc-800/50",
                                    "hover:border-purple-500/30 transition-colors duration-300"
                                )}
                                style={{
                                    boxShadow: `0 0 60px ${group.bgGlow}`,
                                }}
                            >
                                {/* Group Header */}
                                <div className="p-6 border-b border-zinc-800/50">
                                    <div className="flex items-center gap-4">
                                        <div className={cn(
                                            "w-14 h-14 rounded-xl flex items-center justify-center",
                                            `bg-gradient-to-br ${group.color}`
                                        )}>
                                            {getIcon(group.icon)}
                                        </div>
                                        <div className="flex-1">
                                            <h2 className="text-xl font-bold text-white">{cleanGroupTitle(group.title)}</h2>
                                            <p className="text-sm text-zinc-400">{group.subtitle}</p>
                                        </div>
                                        <div className="text-right">
                                            <p className="text-2xl font-bold text-white">{groupPercent}%</p>
                                            <p className="text-xs text-zinc-500">{groupCompleted}/{tasksToShow.length} klara</p>
                                        </div>
                                    </div>

                                    {/* Group Progress Bar */}
                                    <div className="mt-4 h-2 bg-zinc-800 rounded-full overflow-hidden">
                                        <motion.div
                                            initial={{ width: 0 }}
                                            animate={{ width: `${groupPercent}%` }}
                                            className={cn("h-full rounded-full", `bg-gradient-to-r ${group.color}`)}
                                        />
                                    </div>
                                </div>

                                {/* Tasks */}
                                <div className="p-4 grid gap-2">
                                    {tasksToShow.map((task, taskIndex) => {
                                        const completed = isTaskCompleted(task.slug || task.title)
                                        const taskSlug = task.slug || `task-${taskIndex}`

                                        return (
                                            <Link
                                                key={taskSlug}
                                                href={`/modules/${slug}/tasks/${taskSlug}`}
                                            >
                                                <motion.div
                                                    whileHover={{ scale: 1.01, x: 4 }}
                                                    className={cn(
                                                        "flex items-center gap-4 p-4 rounded-xl",
                                                        "transition-all duration-200 group",
                                                        completed
                                                            ? "bg-emerald-500/10 border border-emerald-500/20"
                                                            : "bg-white/5 border border-transparent hover:border-purple-500/30"
                                                    )}
                                                >
                                                    {/* Status */}
                                                    <div className={cn(
                                                        "w-8 h-8 rounded-full flex items-center justify-center shrink-0",
                                                        completed
                                                            ? "bg-emerald-500/20"
                                                            : "bg-zinc-800"
                                                    )}>
                                                        {completed ? (
                                                            <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                                                        ) : (
                                                            <Circle className="w-4 h-4 text-zinc-600" />
                                                        )}
                                                    </div>

                                                    {/* Info */}
                                                    <div className="flex-1 min-w-0">
                                                        <h3 className={cn(
                                                            "font-medium truncate",
                                                            completed ? "text-emerald-300" : "text-white group-hover:text-purple-300"
                                                        )}>
                                                            {task.title}
                                                        </h3>
                                                        <p className="text-sm text-zinc-500 truncate">
                                                            {task.description}
                                                        </p>
                                                    </div>

                                                    {/* Meta */}
                                                    <div className="flex items-center gap-3 shrink-0">
                                                        <span className="text-xs text-zinc-500 flex items-center gap-1">
                                                            <Clock className="w-3 h-3" />
                                                            {task.estimated_minutes}m
                                                        </span>
                                                        <ChevronRight className={cn(
                                                            "w-5 h-5 transition-transform",
                                                            completed ? "text-emerald-400" : "text-zinc-600 group-hover:text-purple-400 group-hover:translate-x-1"
                                                        )} />
                                                    </div>
                                                </motion.div>
                                            </Link>
                                        )
                                    })}
                                </div>
                            </motion.div>
                        )
                    })}
                </div>

                {/* Completion Message */}
                {completedCount === totalTasks && totalTasks > 0 && (
                    <motion.div
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        className={cn(
                            "mt-8 p-8 rounded-3xl text-center",
                            "bg-gradient-to-r from-emerald-500/20 via-purple-500/20 to-cyan-500/20",
                            "border border-emerald-500/30"
                        )}
                    >
                        <motion.div
                            animate={{ rotate: [0, 10, -10, 0] }}
                            transition={{ duration: 0.5, repeat: Infinity, repeatDelay: 2 }}
                            className="text-6xl mb-4"
                        >
                            🎉
                        </motion.div>
                        <h2 className="text-2xl font-bold text-white mb-2">
                            Grattis! Du har klarat alla tasks!
                        </h2>
                        <p className="text-zinc-300">
                            Du är redo! Lycka till! 🍀
                        </p>
                    </motion.div>
                )}

                {/* Recommended Tutorials */}
                {(() => {
                    // Find tutorials relevant to this module
                    const moduleTutorials = findTutorialsByModule(slug)
                    // Also try with common keywords based on module name
                    const keywords = moduleName.toLowerCase().split(/\s+/)
                    const keywordTutorials = TUTORIALS.filter(t =>
                        keywords.some(kw =>
                            t.topics.some(topic => topic.includes(kw) || kw.includes(topic))
                        )
                    )
                    const allTutorials = [...new Map([...moduleTutorials, ...keywordTutorials].map(t => [t.id, t])).values()]

                    if (allTutorials.length === 0) return null

                    return (
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.5 }}
                            className="mt-12"
                        >
                            <TutorialSection
                                title="📺 Rekommenderade Videos"
                                subtitle={`Kvalitets-tutorials för ${moduleName}`}
                                tutorials={allTutorials}
                                maxItems={3}
                                showViewAll={true}
                            />
                        </motion.div>
                    )
                })()}
            </div>
        </div>
    )
}

export default SharedModulePage
