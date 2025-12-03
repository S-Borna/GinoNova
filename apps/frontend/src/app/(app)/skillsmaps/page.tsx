"use client"

/**
 * ============================================================================
 * SKILLSMAPS LIST PAGE — Premium Design
 * ============================================================================
 *
 * Main SkillsMaps page with:
 * - Platform check (shows PlatformSelector if OS not chosen)
 * - Premium SkillsMapSelector grid
 * - Category filtering and search
 * - Progress tracking
 *
 * @phase SKILLSMAPS-INTEGRATION
 */

import { useState, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { PageLayout, Section } from "@saas/ui"
import { usePlatform } from "@/hooks/useOperatingSystem"
import { PlatformSelector } from "@/components/onboarding"
import { SkillsMapSelector, SkillsMapCardProps } from "@/components/skillsmaps"
import { RefreshCw, AlertCircle } from "lucide-react"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"

/* ============================================================================
   MOCK DATA — Will be replaced with API calls
   ============================================================================ */

const MOCK_SKILLSMAPS: SkillsMapCardProps[] = [
    {
        id: "1",
        slug: "python",
        title: "Python for DevOps",
        description: "Lär dig Python från grunden med fokus på automation, scripting och DevOps-verktyg",
        icon: "🐍",
        color: "#3776AB",
        totalNodes: 21,
        completedNodes: 0,
        totalXP: 2100,
        estimatedHours: 25,
        status: "not_started",
        difficulty: "beginner",
        tags: ["Scripting", "Automation", "API"],
    },
    {
        id: "2",
        slug: "linux",
        title: "Linux Mastery",
        description: "Behärska Linux från kommandoraden till systemadministration och säkerhet",
        icon: "🐧",
        color: "#FCC624",
        totalNodes: 20,
        completedNodes: 5,
        totalXP: 2000,
        estimatedHours: 30,
        status: "in_progress",
        difficulty: "beginner",
        tags: ["CLI", "System Admin", "Shell"],
    },
    {
        id: "3",
        slug: "docker",
        title: "Docker",
        description: "Containerisering från grunderna till produktion med Docker och Docker Compose",
        icon: "🐳",
        color: "#2496ED",
        totalNodes: 20,
        completedNodes: 20,
        totalXP: 2000,
        estimatedHours: 20,
        status: "complete",
        difficulty: "intermediate",
        tags: ["Containers", "DevOps", "Microservices"],
    },
    {
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
        status: "not_started",
        difficulty: "advanced",
        tags: ["Orchestration", "Cloud Native", "DevOps"],
    },
    {
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
        status: "not_started",
        difficulty: "intermediate",
        tags: ["IaC", "Cloud", "Automation"],
    },
    {
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
        status: "not_started",
        difficulty: "intermediate",
        tags: ["Cloud", "Infrastructure", "Serverless"],
    },
    {
        id: "7",
        slug: "git",
        title: "Git & GitHub",
        description: "Versionskontroll, branching strategier och samarbete med Git och GitHub",
        icon: "🔀",
        color: "#F05032",
        totalNodes: 15,
        completedNodes: 15,
        totalXP: 1500,
        estimatedHours: 12,
        status: "complete",
        difficulty: "beginner",
        tags: ["Version Control", "Collaboration", "DevOps"],
    },
    {
        id: "8",
        slug: "cicd",
        title: "CI/CD Pipelines",
        description: "Bygg robusta CI/CD pipelines med GitHub Actions, Jenkins och GitLab CI",
        icon: "🚀",
        color: "#2088FF",
        totalNodes: 20,
        completedNodes: 8,
        totalXP: 2000,
        estimatedHours: 22,
        status: "in_progress",
        difficulty: "intermediate",
        tags: ["Automation", "Pipelines", "DevOps"],
    },
    {
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
        status: "not_started",
        difficulty: "beginner",
        tags: ["Scripting", "CLI", "Automation"],
    },
    {
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
        status: "not_started",
        difficulty: "beginner",
        tags: ["Programming", "Web", "Node.js"],
    },
    {
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
        status: "not_started",
        difficulty: "intermediate",
        tags: ["Programming", "Types", "JavaScript"],
    },
    {
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
        status: "not_started",
        difficulty: "intermediate",
        tags: ["Programming", "Systems", "Cloud Native"],
    },
    {
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
        status: "not_started",
        difficulty: "intermediate",
        tags: ["Configuration", "Automation", "IaC"],
    },
    {
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
        status: "not_started",
        difficulty: "beginner",
        tags: ["Database", "Queries", "Data"],
    },
    {
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
        status: "not_started",
        difficulty: "advanced",
        tags: ["Architecture", "Scalability", "Distributed"],
    },
    {
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
        status: "not_started",
        difficulty: "intermediate",
        tags: ["Backend", "API", "JavaScript"],
    },
    {
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
        status: "not_started",
        difficulty: "beginner",
        tags: ["AI", "LLM", "GPT"],
    },
]

/* ============================================================================
   LOADING SKELETON
   ============================================================================ */

function PageSkeleton() {
    return (
        <div className="space-y-8 animate-pulse">
            <div className="h-48 rounded-3xl bg-zinc-800/50" />
            <div className="flex gap-3">
                {Array.from({ length: 5 }).map((_, i) => (
                    <div key={i} className="h-10 w-28 rounded-xl bg-zinc-800/50" />
                ))}
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {Array.from({ length: 6 }).map((_, i) => (
                    <div key={i} className="h-72 rounded-2xl bg-zinc-800/50" />
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
                Kunde inte ladda SkillsMaps
            </h2>
            <p className="text-zinc-400 mb-6">{error}</p>
            <Button onClick={onRetry} className="rounded-xl">
                <RefreshCw className="w-4 h-4 mr-2" />
                Försök igen
            </Button>
        </div>
    )
}

/* ============================================================================
   SKILLSMAPS PAGE
   ============================================================================ */

export default function SkillsMapsPage() {
    const { hasSelected, isLoading: platformLoading } = usePlatform()
    const [skillsmaps, setSkillsmaps] = useState<SkillsMapCardProps[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    // Track if user explicitly completed the platform selection
    const [platformComplete, setPlatformComplete] = useState(false)

    const fetchSkillsMaps = async () => {
        setLoading(true)
        setError(null)

        try {
            // TODO: Replace with actual API call
            // const result = await getSkillsMaps()
            await new Promise(resolve => setTimeout(resolve, 500)) // Simulate API
            setSkillsmaps(MOCK_SKILLSMAPS)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Ett fel uppstod")
        } finally {
            setLoading(false)
        }
    }

    useEffect(() => {
        fetchSkillsMaps()
    }, [])

    // If platform was already selected on page load, mark as complete
    useEffect(() => {
        if (!platformLoading && hasSelected) {
            setPlatformComplete(true)
        }
    }, [hasSelected, platformLoading])

    // Handle platform selection complete
    const handlePlatformComplete = () => {
        console.log("[SkillsMaps] Platform selection complete, showing content")
        setPlatformComplete(true)
    }

    // Determine if we should show SkillsMaps content
    // hasSelected is from localStorage (persisted), platformComplete is from user action this session
    const shouldShowContent = platformComplete || hasSelected

    // Debug logging
    useEffect(() => {
        console.log("[SkillsMaps] State:", { platformLoading, hasSelected, platformComplete, shouldShowContent })
    }, [platformLoading, hasSelected, platformComplete, shouldShowContent])

    // Platform loading
    if (platformLoading) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <PageSkeleton />
            </PageLayout>
        )
    }

    // Show platform selector if not yet completed
    if (!shouldShowContent) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <div className="min-h-[70vh] flex items-center justify-center py-12">
                    <PlatformSelector onComplete={handlePlatformComplete} />
                </div>
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
                <ErrorState error={error} onRetry={fetchSkillsMaps} />
            </PageLayout>
        )
    }

    return (
        <PageLayout maxWidth="wide" background="gray">
            <AnimatePresence>
                <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 0.3 }}
                >
                    <Section spacing="none">
                        <SkillsMapSelector skillsmaps={skillsmaps} />
                    </Section>
                </motion.div>
            </AnimatePresence>
        </PageLayout>
    )
}
