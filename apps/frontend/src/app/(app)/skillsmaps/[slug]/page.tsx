"use client"

/**
 * ============================================================================
 * SKILLSMAP DETAIL PAGE — View Single SkillsMap with Nodes
 * ============================================================================
 *
 * Shows:
 * - SkillsMap header with progress
 * - List of nodes (like tasks)
 * - Node content viewer
 * - Premium design matching modules page
 *
 * @phase SKILLSMAPS-INTEGRATION
 */

import { useState, useEffect } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import { motion, AnimatePresence } from "framer-motion"
import { PageLayout, Section, Block, Headline, Subtext } from "@saas/ui"
import { NodeCard, NodeCardProps, NodeType, NodeStatus } from "@/components/skillsmaps"
import { Button } from "@/components/ui/button"
import { ProgressBar } from "@/components/ui/progress-bar"
import { cn } from "@/lib/utils"
import {
    ArrowLeft,
    Play,
    CheckCircle2,
    Clock,
    BookOpen,
    Zap,
    RefreshCw,
    AlertCircle,
    Sparkles,
    ChevronRight,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface SkillsMapDetailUI {
    id: string
    slug: string
    title: string
    description: string
    icon: string
    color: string
    totalNodes: number
    completedNodes: number
    totalXP: number
    estimatedHours: number
    difficulty: "beginner" | "intermediate" | "advanced" | "expert"
    nodes: NodeCardProps[]
}

/* ============================================================================
   MOCK DATA — Will be replaced with API
   ============================================================================ */

function getMockSkillsMap(slug: string): SkillsMapDetailUI | null {
    // Generate 20 nodes for any SkillsMap
    const generateNodes = (prefix: string, baseColor: string): NodeCardProps[] => {
        const nodeTemplates = [
            // Block 1: Fundamentals (1-4)
            { title: "Introduktion", desc: "Grundläggande koncept och varför det är viktigt", type: "concept" as NodeType, diff: "easy" as const },
            { title: "Installation & Setup", desc: "Installera och konfigurera din utvecklingsmiljö", type: "practice" as NodeType, diff: "easy" as const },
            { title: "Första stegen", desc: "Dina första kommandon och grundläggande användning", type: "practice" as NodeType, diff: "easy" as const },
            { title: "Grundläggande struktur", desc: "Förstå den underliggande arkitekturen", type: "concept" as NodeType, diff: "easy" as const },
            // Block 2: Core Concepts (5-8)
            { title: "Konfiguration", desc: "Konfigurera och anpassa efter dina behov", type: "practice" as NodeType, diff: "medium" as const },
            { title: "Arbetsflöden", desc: "Best practices för dagligt arbete", type: "concept" as NodeType, diff: "medium" as const },
            { title: "Felsökning", desc: "Debugging och problemlösning", type: "practice" as NodeType, diff: "medium" as const },
            { title: "Optimering", desc: "Förbättra prestanda och effektivitet", type: "concept" as NodeType, diff: "medium" as const },
            // Block 3: Intermediate (9-12)
            { title: "Avancerade kommandon", desc: "Kraftfulla tekniker för erfarna användare", type: "practice" as NodeType, diff: "medium" as const },
            { title: "Automation", desc: "Automatisera repetitiva uppgifter", type: "practice" as NodeType, diff: "medium" as const },
            { title: "Integration", desc: "Integrera med andra verktyg och system", type: "concept" as NodeType, diff: "medium" as const },
            { title: "Säkerhet", desc: "Säkerhetsaspekter och best practices", type: "concept" as NodeType, diff: "medium" as const },
            // Block 4: Advanced (13-16)
            { title: "Skalning", desc: "Hantera större system och team", type: "concept" as NodeType, diff: "hard" as const },
            { title: "Produktionsmiljö", desc: "Förbereda för produktion", type: "practice" as NodeType, diff: "hard" as const },
            { title: "Monitoring", desc: "Övervakning och observability", type: "practice" as NodeType, diff: "hard" as const },
            { title: "CI/CD Integration", desc: "Integrera i continuous delivery pipelines", type: "practice" as NodeType, diff: "hard" as const },
            // Block 5: Expert (17-20)
            { title: "Enterprise patterns", desc: "Mönster för stora organisationer", type: "concept" as NodeType, diff: "hard" as const },
            { title: "Avancerad felsökning", desc: "Komplexa debugging-scenarion", type: "challenge" as NodeType, diff: "hard" as const },
            { title: "Performance tuning", desc: "Avancerad prestandaoptimering", type: "challenge" as NodeType, diff: "hard" as const },
            { title: "Certifieringsförberedelse", desc: "Sammanfattning och certifieringsguide", type: "quiz" as NodeType, diff: "hard" as const },
        ]

        return nodeTemplates.map((template, index) => ({
            id: `${prefix}${index + 1}`,
            orderIndex: index + 1,
            title: template.title,
            description: template.desc,
            type: template.type,
            difficulty: template.diff,
            xpReward: template.diff === "easy" ? 75 : template.diff === "medium" ? 100 : 150,
            estimatedMinutes: template.diff === "easy" ? 20 : template.diff === "medium" ? 30 : 45,
            status: "not_started" as NodeStatus,
        }))
    }

    const mockData: Record<string, SkillsMapDetailUI> = {
        python: {
            id: "1",
            slug: "python",
            title: "Python for DevOps",
            description: "Lär dig Python från grunden med fokus på automation, scripting och DevOps-verktyg",
            icon: "🐍",
            color: "#3776AB",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2000,
            estimatedHours: 25,
            difficulty: "beginner",
            nodes: generateNodes("py", "#3776AB"),
        },
        linux: {
            id: "2",
            slug: "linux",
            title: "Linux Mastery",
            description: "Behärska Linux från kommandoraden till systemadministration och säkerhet",
            icon: "🐧",
            color: "#FCC624",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2000,
            estimatedHours: 30,
            difficulty: "beginner",
            nodes: generateNodes("lx", "#FCC624"),
        },
        docker: {
            id: "3",
            slug: "docker",
            title: "Docker",
            description: "Containerisering från grunderna till produktion med Docker och Docker Compose",
            icon: "🐳",
            color: "#2496ED",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2000,
            estimatedHours: 20,
            difficulty: "intermediate",
            nodes: generateNodes("dk", "#2496ED"),
        },
        kubernetes: {
            id: "4",
            slug: "kubernetes",
            title: "Kubernetes",
            description: "Orkestrering av containers i skala med Kubernetes, Helm och GitOps",
            icon: "☸️",
            color: "#326CE5",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2500,
            estimatedHours: 35,
            difficulty: "advanced",
            nodes: generateNodes("k8s", "#326CE5"),
        },
        terraform: {
            id: "5",
            slug: "terraform",
            title: "Terraform",
            description: "Infrastructure as Code med Terraform för AWS, Azure och GCP",
            icon: "🏗️",
            color: "#7B42BC",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2200,
            estimatedHours: 25,
            difficulty: "intermediate",
            nodes: generateNodes("tf", "#7B42BC"),
        },
        aws: {
            id: "6",
            slug: "aws",
            title: "AWS",
            description: "Amazon Web Services från EC2 till serverless med fokus på best practices",
            icon: "☁️",
            color: "#FF9900",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2400,
            estimatedHours: 40,
            difficulty: "intermediate",
            nodes: generateNodes("aws", "#FF9900"),
        },
        git: {
            id: "7",
            slug: "git",
            title: "Git & GitHub",
            description: "Versionskontroll, branching strategier och samarbete med Git och GitHub",
            icon: "🔀",
            color: "#F05032",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 1500,
            estimatedHours: 12,
            difficulty: "beginner",
            nodes: generateNodes("git", "#F05032"),
        },
        cicd: {
            id: "8",
            slug: "cicd",
            title: "CI/CD Pipelines",
            description: "Bygg robusta CI/CD pipelines med GitHub Actions, Jenkins och GitLab CI",
            icon: "🚀",
            color: "#2088FF",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2000,
            estimatedHours: 22,
            difficulty: "intermediate",
            nodes: generateNodes("cicd", "#2088FF"),
        },
        bash: {
            id: "9",
            slug: "bash",
            title: "Shell/Bash Scripting",
            description: "Automatisera allt med Bash scripting, sed, awk och kraftfulla one-liners",
            icon: "💻",
            color: "#4EAA25",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 1800,
            estimatedHours: 18,
            difficulty: "beginner",
            nodes: generateNodes("sh", "#4EAA25"),
        },
        javascript: {
            id: "10",
            slug: "javascript",
            title: "JavaScript",
            description: "Modern JavaScript från ES6+ till Node.js för fullstack utveckling",
            icon: "📜",
            color: "#F7DF1E",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2000,
            estimatedHours: 28,
            difficulty: "beginner",
            nodes: generateNodes("js", "#F7DF1E"),
        },
        typescript: {
            id: "11",
            slug: "typescript",
            title: "TypeScript",
            description: "Typsäker JavaScript med TypeScript för robusta applikationer",
            icon: "🔷",
            color: "#3178C6",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2000,
            estimatedHours: 22,
            difficulty: "intermediate",
            nodes: generateNodes("ts", "#3178C6"),
        },
        go: {
            id: "12",
            slug: "go",
            title: "Go",
            description: "Systemsprogrammering och cloud-native utveckling med Go",
            icon: "🔵",
            color: "#00ADD8",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2200,
            estimatedHours: 30,
            difficulty: "intermediate",
            nodes: generateNodes("go", "#00ADD8"),
        },
        ansible: {
            id: "13",
            slug: "ansible",
            title: "Ansible",
            description: "Konfigurationshantering och automation med Ansible playbooks och roles",
            icon: "⚙️",
            color: "#EE0000",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2000,
            estimatedHours: 20,
            difficulty: "intermediate",
            nodes: generateNodes("ans", "#EE0000"),
        },
        sql: {
            id: "14",
            slug: "sql",
            title: "SQL",
            description: "Databashantering från grundläggande queries till avancerad optimering",
            icon: "🗃️",
            color: "#336791",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2000,
            estimatedHours: 24,
            difficulty: "beginner",
            nodes: generateNodes("sql", "#336791"),
        },
        system_design: {
            id: "15",
            slug: "system_design",
            title: "System Design",
            description: "Designa skalbara system från mikrotjänster till distributed systems",
            icon: "🏛️",
            color: "#6366F1",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2800,
            estimatedHours: 35,
            difficulty: "advanced",
            nodes: generateNodes("sd", "#6366F1"),
        },
        nodejs: {
            id: "16",
            slug: "nodejs",
            title: "Node.js",
            description: "Backend-utveckling med Node.js, Express och moderna API-mönster",
            icon: "💚",
            color: "#339933",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2000,
            estimatedHours: 26,
            difficulty: "intermediate",
            nodes: generateNodes("node", "#339933"),
        },
        prompt_engineering: {
            id: "17",
            slug: "prompt_engineering",
            title: "Prompt Engineering",
            description: "Behärska konsten att kommunicera effektivt med AI-modeller",
            icon: "🧠",
            color: "#EC4899",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2000,
            estimatedHours: 15,
            difficulty: "beginner",
            nodes: generateNodes("pe", "#EC4899"),
        },
        mlops: {
            id: "18",
            slug: "mlops",
            title: "MLOps",
            description: "Machine Learning Operations för produktion - modellträning till deployment",
            icon: "🤖",
            color: "#FF6B6B",
            totalNodes: 20,
            completedNodes: 0,
            totalXP: 2400,
            estimatedHours: 30,
            difficulty: "advanced",
            nodes: generateNodes("ml", "#FF6B6B"),
        },
    }

    return mockData[slug] || null
}

/* ============================================================================
   SKELETON
   ============================================================================ */

function DetailSkeleton() {
    return (
        <div className="space-y-6 animate-pulse">
            <div className="h-48 rounded-3xl bg-zinc-800/50" />
            <div className="space-y-4">
                {Array.from({ length: 5 }).map((_, i) => (
                    <div key={i} className="h-28 rounded-2xl bg-zinc-800/50" />
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
        <div className={cn(
            "max-w-md mx-auto text-center p-8 rounded-2xl",
            "bg-zinc-900/80 border border-zinc-800"
        )}>
            <div className={cn(
                "w-16 h-16 mx-auto mb-4 rounded-full",
                "bg-red-500/20 flex items-center justify-center"
            )}>
                <AlertCircle className="w-8 h-8 text-red-400" />
            </div>
            <h2 className="text-xl font-semibold text-white mb-2">
                SkillsMap hittades inte
            </h2>
            <p className="text-zinc-400 mb-6">{error}</p>
            <div className="flex gap-3 justify-center">
                <Link href="/skillsmaps">
                    <Button variant="outline" className="rounded-xl">
                        <ArrowLeft className="w-4 h-4 mr-2" />
                        Tillbaka
                    </Button>
                </Link>
                <Button onClick={onRetry} className="rounded-xl">
                    <RefreshCw className="w-4 h-4 mr-2" />
                    Försök igen
                </Button>
            </div>
        </div>
    )
}

/* ============================================================================
   HEADER COMPONENT
   ============================================================================ */

function SkillsMapHeader({ skillsmap }: { skillsmap: SkillsMapDetailUI }) {
    const progress = skillsmap.totalNodes > 0
        ? Math.round((skillsmap.completedNodes / skillsmap.totalNodes) * 100)
        : 0
    const isComplete = progress === 100

    return (
        <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "relative overflow-hidden rounded-3xl",
                "bg-gradient-to-br from-zinc-900 via-zinc-900/95 to-zinc-950",
                "border border-white/10",
                "p-8"
            )}
        >
            {/* Colored glow based on skillsmap color */}
            <div
                className="absolute top-0 right-0 w-[400px] h-[400px] rounded-full blur-[120px] opacity-20"
                style={{ backgroundColor: skillsmap.color }}
            />

            {/* Sparkle for complete */}
            {isComplete && (
                <motion.div
                    className="absolute top-6 right-6 text-emerald-400"
                    animate={{ rotate: 360 }}
                    transition={{ duration: 4, repeat: Infinity, ease: "linear" }}
                >
                    <Sparkles className="w-6 h-6" />
                </motion.div>
            )}

            <div className="relative flex flex-col md:flex-row md:items-start gap-6">
                {/* Icon */}
                <motion.div
                    className={cn(
                        "w-20 h-20 rounded-2xl flex items-center justify-center shrink-0",
                        "bg-gradient-to-br from-white/10 to-white/5",
                        "border border-white/10"
                    )}
                    style={{
                        boxShadow: `0 0 40px ${skillsmap.color}30`,
                    }}
                    whileHover={{ scale: 1.05 }}
                >
                    <span className="text-5xl">{skillsmap.icon}</span>
                </motion.div>

                {/* Content */}
                <div className="flex-1">
                    <h1 className={cn(
                        "text-3xl md:text-4xl font-black mb-2",
                        "bg-gradient-to-r from-white to-white/80 bg-clip-text text-transparent"
                    )}>
                        {skillsmap.title}
                    </h1>
                    <p className="text-zinc-400 mb-4 max-w-2xl">
                        {skillsmap.description}
                    </p>

                    {/* Meta row */}
                    <div className="flex flex-wrap items-center gap-4 mb-4 text-sm">
                        <span className="flex items-center gap-1.5 text-zinc-400">
                            <BookOpen className="w-4 h-4" />
                            {skillsmap.totalNodes} noder
                        </span>
                        <span className="flex items-center gap-1.5 text-zinc-400">
                            <Clock className="w-4 h-4" />
                            ~{skillsmap.estimatedHours}h
                        </span>
                        <span className="flex items-center gap-1.5 text-amber-400 font-medium">
                            <Zap className="w-4 h-4" />
                            {skillsmap.totalXP} XP totalt
                        </span>
                        <span className={cn(
                            "flex items-center gap-1.5 font-medium",
                            isComplete ? "text-emerald-400" : "text-purple-400"
                        )}>
                            <CheckCircle2 className="w-4 h-4" />
                            {skillsmap.completedNodes}/{skillsmap.totalNodes} klara
                        </span>
                    </div>

                    {/* Progress */}
                    <div className="max-w-md">
                        <div className="flex items-center justify-between text-sm mb-2">
                            <span className="text-zinc-500">Progress</span>
                            <span className={cn(
                                "font-bold",
                                isComplete ? "text-emerald-400" : "text-purple-400"
                            )}>
                                {progress}%
                            </span>
                        </div>
                        <div className="h-2.5 bg-zinc-800 rounded-full overflow-hidden">
                            <motion.div
                                className="h-full rounded-full"
                                style={{
                                    background: isComplete
                                        ? "linear-gradient(90deg, #10b981, #14b8a6)"
                                        : `linear-gradient(90deg, ${skillsmap.color}, ${skillsmap.color}cc)`,
                                    boxShadow: `0 0 15px ${isComplete ? "#10b981" : skillsmap.color}50`,
                                }}
                                initial={{ width: 0 }}
                                animate={{ width: `${progress}%` }}
                                transition={{ duration: 1, ease: "easeOut" }}
                            />
                        </div>
                    </div>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   SKILLSMAP DETAIL PAGE
   ============================================================================ */

export default function SkillsMapDetailPage() {
    const params = useParams()
    const router = useRouter()
    const slug = params?.slug as string

    const [skillsmap, setSkillsmap] = useState<SkillsMapDetailUI | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    const fetchSkillsMap = async () => {
        setLoading(true)
        setError(null)

        try {
            // TODO: Replace with actual API call
            await new Promise(resolve => setTimeout(resolve, 300))
            const data = getMockSkillsMap(slug)

            if (!data) {
                setError("Denna SkillsMap finns inte")
                return
            }

            setSkillsmap(data)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Ett fel uppstod")
        } finally {
            setLoading(false)
        }
    }

    useEffect(() => {
        if (slug) {
            fetchSkillsMap()
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [slug])

    const handleNodeClick = (nodeId: string) => {
        router.push(`/skillsmaps/${slug}/nodes/${nodeId}`)
    }

    // Find next incomplete node
    const nextNode = skillsmap?.nodes.find(n => n.status !== "complete")

    const handleContinue = () => {
        if (nextNode) {
            handleNodeClick(nextNode.id)
        }
    }

    return (
        <PageLayout maxWidth="standard" background="gray">
            {/* Back button */}
            <Link
                href="/skillsmaps"
                className={cn(
                    "inline-flex items-center gap-2 text-sm mb-6",
                    "text-zinc-500 hover:text-white",
                    "transition-colors"
                )}
            >
                <ArrowLeft className="w-4 h-4" />
                Tillbaka till SkillsMaps
            </Link>

            {loading ? (
                <DetailSkeleton />
            ) : error ? (
                <ErrorState error={error} onRetry={fetchSkillsMap} />
            ) : skillsmap ? (
                <motion.div
                    className="space-y-8"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                >
                    {/* Header */}
                    <SkillsMapHeader skillsmap={skillsmap} />

                    {/* Continue button */}
                    {nextNode && (
                        <motion.div
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.2 }}
                        >
                            <Button
                                onClick={handleContinue}
                                size="lg"
                                className={cn(
                                    "rounded-xl px-6",
                                    "bg-gradient-to-r from-purple-600 to-indigo-600",
                                    "hover:from-purple-500 hover:to-indigo-500",
                                    "shadow-[0_0_20px_rgba(139,92,246,0.3)]"
                                )}
                            >
                                <Play className="w-4 h-4 mr-2" />
                                Fortsätt: {nextNode.title}
                                <ChevronRight className="w-4 h-4 ml-2" />
                            </Button>
                        </motion.div>
                    )}

                    {/* Nodes list */}
                    <Section>
                        <Headline level={2} className="mb-4 text-white">
                            Noder
                        </Headline>
                        <div className="space-y-4">
                            {skillsmap.nodes.map((node, index) => (
                                <motion.div
                                    key={node.id}
                                    initial={{ opacity: 0, x: -20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    transition={{ delay: 0.1 + index * 0.05 }}
                                >
                                    <NodeCard
                                        {...node}
                                        onClick={handleNodeClick}
                                    />
                                </motion.div>
                            ))}
                        </div>
                    </Section>
                </motion.div>
            ) : null}
        </PageLayout>
    )
}
