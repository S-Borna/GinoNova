"use client"

/**
 * ============================================================================
 * SKILLSMAP NODE DETAIL PAGE — Individual Node/Lesson View
 * ============================================================================
 *
 * Features:
 * - Enhanced lesson content with progress tracking
 * - Interactive content blocks (quiz, terminal, checkpoint)
 * - Progress tracking with read progress bar
 * - Mark as complete button
 * - Navigation to next node
 *
 * @phase SKILLSMAPS-INTEGRATION
 */

import { useState, useEffect, useCallback, useMemo } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import {
    PageLayout,
    Section,
    Block,
    Headline,
    Subtext,
    TaskFooter,
    cn
} from "@saas/ui"
import { GlassCard } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import { useAuth } from "@/components/auth"
import { getToken } from "@/lib/auth"
import { LessonContent } from "@/components/learning"
import { usePlatform, filterContentByPlatform } from "@/hooks/useOperatingSystem"
import {
    ArrowLeft,
    CheckCircle2,
    Clock,
    BookOpen,
    RefreshCw,
    AlertCircle,
    Zap,
    Play,
    Sparkles,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

type NodeType = "concept" | "practice" | "quiz" | "challenge" | "project"
type NodeStatus = "not_started" | "in_progress" | "complete"
type NodeDifficulty = "easy" | "medium" | "hard"

interface SkillsMapNode {
    id: string
    orderIndex: number
    title: string
    description: string
    type: NodeType
    difficulty: NodeDifficulty
    xpReward: number
    estimatedMinutes: number
    status: NodeStatus
    content?: string
}

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
    nodes: SkillsMapNode[]
}

/* ============================================================================
   MOCK DATA — Will be replaced with API
   ============================================================================ */

function getMockSkillsMap(slug: string): SkillsMapDetailUI | null {
    // Generate 20 nodes for any SkillsMap
    const generateNodes = (prefix: string, baseColor: string): SkillsMapNode[] => {
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
   NODE CONTENT GENERATOR
   ============================================================================ */

function generateNodeContent(slug: string, node: SkillsMapNode): string {
    const skillsMapTitles: Record<string, string> = {
        python: "Python for DevOps",
        linux: "Linux Mastery",
        docker: "Docker",
        kubernetes: "Kubernetes",
        terraform: "Terraform",
        aws: "AWS",
        git: "Git & GitHub",
        cicd: "CI/CD Pipelines",
        bash: "Shell/Bash Scripting",
        javascript: "JavaScript",
        typescript: "TypeScript",
        go: "Go",
        ansible: "Ansible",
        sql: "SQL",
        system_design: "System Design",
        nodejs: "Node.js",
        prompt_engineering: "Prompt Engineering",
        mlops: "MLOps",
    }

    const skillTitle = skillsMapTitles[slug] || slug

    return `# ${node.title}

${node.description}

---

## Översikt

I denna lektion lär du dig om **${node.title.toLowerCase()}** inom ${skillTitle}.
Detta är en ${node.difficulty === 'easy' ? 'grundläggande' : node.difficulty === 'medium' ? 'mellansvår' : 'avancerad'} lektion som tar ungefär ${node.estimatedMinutes} minuter att slutföra.

## Lärandemål

Efter denna lektion kommer du att:

- Förstå grunderna i ${node.title.toLowerCase()}
- Kunna tillämpa koncepten praktiskt
- Ha färdigheter att gå vidare till nästa steg

## Huvudinnehåll

### Introduktion

${node.type === 'concept' ?
            'Denna lektion fokuserar på teoretiska koncept som är viktiga att förstå innan du börjar praktisera.' :
            node.type === 'practice' ?
                'Denna lektion är praktiskt orienterad. Du kommer att utföra övningar för att befästa dina kunskaper.' :
                node.type === 'quiz' ?
                    'Denna lektion testar dina kunskaper genom frågor och övningar.' :
                    node.type === 'challenge' ?
                        'Detta är en utmaning som testar dina färdigheter på en djupare nivå.' :
                        'Denna lektion kombinerar teori och praktik.'
        }

### Nyckelkoncept

1. **Grundläggande förståelse** - Vad innebär ${node.title.toLowerCase()}?
2. **Praktisk tillämpning** - Hur används detta i verkliga scenarion?
3. **Best practices** - Vilka är de bästa metoderna?

### Exempel

\`\`\`bash
# Exempelkommando för ${skillTitle}
echo "Övning: ${node.title}"
\`\`\`

## Sammanfattning

Du har nu lärt dig grunderna i **${node.title}**.
Fortsätt till nästa lektion för att bygga vidare på dessa kunskaper.

---

💡 **Tips:** Öva regelbundet för att befästa dina kunskaper!

🏆 **Belöning:** ${node.xpReward} XP vid slutförande
`
}

/* ============================================================================
   SKELETON
   ============================================================================ */

function NodeDetailSkeleton() {
    return (
        <div className="space-y-6 animate-pulse">
            <div className="h-8 w-48 rounded bg-zinc-800" />
            <div className="h-64 rounded-2xl bg-zinc-800" />
            <div className="space-y-3">
                <div className="h-4 w-full rounded bg-zinc-800" />
                <div className="h-4 w-3/4 rounded bg-zinc-800" />
                <div className="h-4 w-5/6 rounded bg-zinc-800" />
            </div>
        </div>
    )
}

/* ============================================================================
   ERROR STATE
   ============================================================================ */

function ErrorState({ error, onRetry, slug }: { error: string; onRetry: () => void; slug: string }) {
    return (
        <GlassCard
            variant="default"
            padding="xl"
            radius="xl"
            className="max-w-md mx-auto text-center"
        >
            <div
                className={cn(
                    "w-16 h-16 rounded-full mx-auto mb-4",
                    "bg-red-900/30",
                    "flex items-center justify-center"
                )}
            >
                <AlertCircle className="w-8 h-8 text-red-500" />
            </div>
            <h2 className="text-xl font-semibold text-white mb-2">
                Node hittades inte
            </h2>
            <p className="text-zinc-400 mb-6">{error}</p>
            <div className="flex gap-3 justify-center">
                <Link href={`/skillsmaps/${slug}`}>
                    <Button variant="outline" className="rounded-xl">
                        <ArrowLeft className="w-4 h-4 mr-2" />
                        Tillbaka till SkillsMap
                    </Button>
                </Link>
                <Button onClick={onRetry} className="rounded-xl">
                    <RefreshCw className="w-4 h-4 mr-2" />
                    Försök igen
                </Button>
            </div>
        </GlassCard>
    )
}

/* ============================================================================
   NODE DETAIL PAGE
   ============================================================================ */

export default function SkillsMapNodeDetailPage() {
    const params = useParams()
    const router = useRouter()
    const { user } = useAuth()
    const { platform: platformConfig, os, distro } = usePlatform()
    const slug = params?.slug as string
    const nodeId = params?.nodeId as string

    const [skillsmap, setSkillsmap] = useState<SkillsMapDetailUI | null>(null)
    const [node, setNode] = useState<SkillsMapNode | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [completing, setCompleting] = useState(false)
    const [isCompleted, setIsCompleted] = useState(false)

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
    const token = getToken()

    const fetchData = useCallback(async () => {
        setLoading(true)
        setError(null)

        try {
            // TODO: Replace with actual API call
            await new Promise(resolve => setTimeout(resolve, 300))

            const skillsmapData = getMockSkillsMap(slug)
            if (!skillsmapData) {
                setError("Denna SkillsMap finns inte")
                return
            }

            const nodeData = skillsmapData.nodes.find(n => n.id === nodeId)
            if (!nodeData) {
                setError("Denna nod finns inte")
                return
            }

            // Add generated content to node
            const nodeWithContent = {
                ...nodeData,
                content: generateNodeContent(slug, nodeData)
            }

            setSkillsmap(skillsmapData)
            setNode(nodeWithContent)

            // Check completion status from localStorage
            const completedKey = `skillsmap_${slug}_${nodeId}_completed`
            const wasCompleted = localStorage.getItem(completedKey) === 'true'
            setIsCompleted(wasCompleted)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Ett fel uppstod")
        } finally {
            setLoading(false)
        }
    }, [slug, nodeId])

    useEffect(() => {
        fetchData()
    }, [fetchData])

    const handleMarkComplete = async () => {
        setCompleting(true)
        await new Promise((resolve) => setTimeout(resolve, 500))

        // Save completion to localStorage
        const completedKey = `skillsmap_${slug}_${nodeId}_completed`
        localStorage.setItem(completedKey, 'true')

        setIsCompleted(true)
        setCompleting(false)
    }

    // Find current node index and next/prev nodes
    const allNodes = skillsmap?.nodes || []
    const currentIndex = allNodes.findIndex(n => n.id === nodeId)
    const nextNode = currentIndex >= 0 && currentIndex < allNodes.length - 1
        ? allNodes[currentIndex + 1]
        : null
    const prevNode = currentIndex > 0
        ? allNodes[currentIndex - 1]
        : null

    const handleContinue = () => {
        if (nextNode) {
            router.push(`/skillsmaps/${slug}/nodes/${nextNode.id}`)
        } else {
            // No more nodes, go back to skillsmap
            router.push(`/skillsmaps/${slug}`)
        }
    }

    // Filter content based on user's platform selection
    const filteredContent = node?.content
        ? filterContentByPlatform(node.content, os, distro)
        : null

    return (
        <PageLayout maxWidth="standard" background="gray">
            {/* Back button */}
            <Link
                href={`/skillsmaps/${slug}`}
                className={cn(
                    "inline-flex items-center gap-2 text-sm mb-6",
                    "text-zinc-500 hover:text-white",
                    "transition-colors"
                )}
            >
                <ArrowLeft className="w-4 h-4" />
                Tillbaka till {skillsmap?.title || "SkillsMap"}
            </Link>

            {loading ? (
                <NodeDetailSkeleton />
            ) : error ? (
                <ErrorState error={error} onRetry={fetchData} slug={slug} />
            ) : node && skillsmap ? (
                <div className="space-y-8">
                    {/* Node Header */}
                    <Section>
                        <Block className="bg-zinc-900/80 backdrop-blur-xl rounded-2xl border border-zinc-700/50 shadow-lg p-6 md:p-8">
                            <div className="flex flex-col md:flex-row md:items-start gap-4">
                                {/* Node info */}
                                <div className="flex-1">
                                    <div className="flex items-center gap-2 mb-2">
                                        <span className="text-xs font-medium text-zinc-400">
                                            Nod {node.orderIndex} av {skillsmap.totalNodes}
                                        </span>
                                        {isCompleted && (
                                            <span className="inline-flex items-center gap-1 text-xs text-emerald-500 font-medium">
                                                <CheckCircle2 className="w-3.5 h-3.5" />
                                                Slutförd
                                            </span>
                                        )}
                                    </div>
                                    <Headline level={1} className="mb-2 text-white">
                                        {node.title}
                                    </Headline>
                                    {node.description && (
                                        <Subtext className="mb-4 text-zinc-400">
                                            {node.description}
                                        </Subtext>
                                    )}

                                    {/* Meta */}
                                    <div className="flex flex-wrap items-center gap-4">
                                        <span className="flex items-center gap-1.5 text-sm text-zinc-500">
                                            <Clock className="w-4 h-4" />
                                            {node.estimatedMinutes} min
                                        </span>
                                        <span className="flex items-center gap-1.5 text-sm text-amber-400 font-medium">
                                            <Zap className="w-4 h-4" />
                                            +{node.xpReward} XP
                                        </span>
                                        <span className={cn(
                                            "px-2 py-0.5 rounded text-xs font-medium",
                                            node.difficulty === "easy" && "bg-emerald-900/50 text-emerald-400",
                                            node.difficulty === "medium" && "bg-amber-900/50 text-amber-400",
                                            node.difficulty === "hard" && "bg-red-900/50 text-red-400",
                                        )}>
                                            {node.difficulty === "easy" ? "Enkel" : node.difficulty === "medium" ? "Medel" : "Svår"}
                                        </span>
                                        <span className={cn(
                                            "px-2 py-0.5 rounded text-xs font-medium",
                                            "bg-purple-900/50 text-purple-400"
                                        )}>
                                            {node.type === "concept" ? "Koncept" :
                                                node.type === "practice" ? "Praktik" :
                                                    node.type === "quiz" ? "Quiz" :
                                                        node.type === "challenge" ? "Utmaning" : "Projekt"}
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </Block>
                    </Section>

                    {/* Lesson Content */}
                    <Section>
                        <Block className="bg-zinc-900/80 backdrop-blur-xl rounded-2xl border border-zinc-700/50 shadow-lg p-6 md:p-8">
                            <div className="flex items-center gap-2 mb-6 pb-4 border-b border-zinc-700">
                                <BookOpen className="w-5 h-5 text-purple-400" />
                                <Headline level={2} className="text-white">
                                    Lektionsinnehåll
                                </Headline>
                            </div>

                            <LessonContent
                                content={filteredContent || node.content || ""}
                                title={node.title}
                                estimatedMinutes={node.estimatedMinutes}
                            />
                        </Block>
                    </Section>

                    {/* Actions - Using TaskFooter from @saas/ui */}
                    <TaskFooter
                        prevTaskUrl={prevNode ? `/skillsmaps/${slug}/nodes/${prevNode.id}` : undefined}
                        nextTaskUrl={nextNode ? `/skillsmaps/${slug}/nodes/${nextNode.id}` : undefined}
                        onComplete={handleMarkComplete}
                        xp={node.xpReward}
                        difficulty={node.difficulty as 'easy' | 'medium' | 'hard'}
                        isCompleted={isCompleted}
                        isLoading={completing}
                    />
                </div>
            ) : null}
        </PageLayout>
    )
}
