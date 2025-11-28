"use client"

/**
 * ============================================================================
 * LAB DETAIL PAGE - Hands-on Lab Experience
 * ============================================================================
 *
 * Features:
 * - Lab header with metadata (title, time, difficulty)
 * - Overview section
 * - Instructions (markdown)
 * - Expected Outcomes checklist
 * - Expandable hints
 * - Completion button with celebration
 *
 * @phase C.3 - Labs & Projects Display
 */

import * as React from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { MarkdownRenderer } from "@/components/content/MarkdownRenderer"
import { OutcomeChecklist, OutcomeItem } from "@/components/content/OutcomeChecklist"
import { Hints, HintItem } from "@/components/content/Hints"
import { GlassCard } from "@/components/ui/glass-card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import {
    ChevronRight,
    Clock,
    Zap,
    FlaskConical,
    CheckCircle2,
    ArrowLeft,
    ArrowRight,
    Loader2,
    Trophy,
    Terminal,
    Star,
} from "lucide-react"

/* ============================================================================
   TRACK COLORS (from design system)
   ============================================================================ */

const TRACK_COLORS: Record<string, string> = {
    foundation: "#6366f1",
    cloud: "#8b5cf6",
    containers: "#06b6d4",
    platform: "#f97316",
}

function getTrackColor(trackSlug?: string): string {
    if (!trackSlug) return TRACK_COLORS.foundation
    return TRACK_COLORS[trackSlug.toLowerCase()] || TRACK_COLORS.foundation
}

/* ============================================================================
   SAMPLE DATA (would come from API)
   ============================================================================ */

const SAMPLE_LAB = {
    id: "lab-1",
    title: "Setting Up Your Development Environment",
    moduleId: "module-01",
    moduleName: "Environment Setup",
    trackSlug: "foundation",
    estimatedMinutes: 45,
    difficulty: "beginner" as const,
    xpReward: 150,
    overview: `
In this hands-on lab, you'll set up a complete local development environment for DevOps work.
By the end of this lab, you'll have all the essential tools installed and configured.
    `,
    instructions: `
# Lab: Setting Up Your Development Environment

## Prerequisites

Before starting this lab, ensure you have:
- A computer running macOS, Linux, or Windows
- Administrator/sudo access
- At least 10GB of free disk space

## Step 1: Install a Package Manager

### macOS

Install Homebrew by running:

\`\`\`bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
\`\`\`

Verify the installation:

\`\`\`bash
brew --version
\`\`\`

### Linux (Ubuntu/Debian)

Update your package manager:

\`\`\`bash
sudo apt update && sudo apt upgrade -y
\`\`\`

## Step 2: Install Git

### macOS

\`\`\`bash
brew install git
\`\`\`

### Linux

\`\`\`bash
sudo apt install git -y
\`\`\`

Verify installation:

\`\`\`bash
git --version
\`\`\`

## Step 3: Configure Git

Set your username and email:

\`\`\`bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
\`\`\`

> **Pro Tip:** Use the same email as your GitHub account for better integration.

## Step 4: Install a Code Editor

We recommend Visual Studio Code for this bootcamp.

### macOS

\`\`\`bash
brew install --cask visual-studio-code
\`\`\`

### Linux

\`\`\`bash
sudo snap install code --classic
\`\`\`

## Step 5: Install Docker

### macOS

\`\`\`bash
brew install --cask docker
\`\`\`

### Linux

Follow the official Docker installation guide for your distribution.

Verify Docker is working:

\`\`\`bash
docker --version
docker run hello-world
\`\`\`

## Verification Checklist

Run the following commands to verify everything is installed:

\`\`\`bash
# Check all installations
echo "Checking installations..."
git --version
code --version
docker --version
echo "All tools installed successfully! ✓"
\`\`\`

## Troubleshooting

### Common Issues

1. **Permission denied errors**: Ensure you have sudo/admin rights
2. **Command not found**: Check if the tool is in your PATH
3. **Docker not starting**: Restart Docker Desktop and try again

## What's Next?

Once you've completed this lab, move on to the next task to learn about basic Git commands.
    `,
    outcomes: [
        { id: "o1", label: "Package manager installed", description: "Homebrew (macOS) or apt (Linux)" },
        { id: "o2", label: "Git installed and configured", description: "With username and email set" },
        { id: "o3", label: "VS Code installed", description: "With terminal access" },
        { id: "o4", label: "Docker installed and running", description: "Successfully ran hello-world container" },
        { id: "o5", label: "All verification commands passed", description: "No errors in output" },
    ] as OutcomeItem[],
    hints: [
        {
            id: "h1",
            title: "Package manager installation issues",
            level: "easy" as const,
            content: `
<p>If you're having trouble installing the package manager:</p>
<ul>
<li><strong>macOS:</strong> Make sure Xcode Command Line Tools are installed first: <code>xcode-select --install</code></li>
<li><strong>Linux:</strong> Ensure your user has sudo privileges</li>
</ul>
            `,
        },
        {
            id: "h2",
            title: "Git configuration not persisting",
            level: "medium" as const,
            content: `
<p>If your Git config doesn't seem to save:</p>
<ol>
<li>Check your config file location: <code>git config --list --show-origin</code></li>
<li>Make sure you're using the <code>--global</code> flag</li>
<li>Try editing directly: <code>code ~/.gitconfig</code></li>
</ol>
            `,
        },
        {
            id: "h3",
            title: "Docker permission denied on Linux",
            level: "detailed" as const,
            content: `
<p>On Linux, you may need to add your user to the docker group:</p>
<pre><code>sudo usermod -aG docker $USER</code></pre>
<p>Then log out and back in. Verify with: <code>groups</code> (should show docker)</p>
<p>If still not working, try: <code>newgrp docker</code></p>
            `,
        },
    ] as HintItem[],
}

/* ============================================================================
   DIFFICULTY BADGE
   ============================================================================ */

function getDifficultyColor(difficulty: string): string {
    switch (difficulty.toLowerCase()) {
        case "beginner":
            return "bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400"
        case "intermediate":
            return "bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400"
        case "advanced":
            return "bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400"
        default:
            return "bg-neutral-100 text-neutral-700 dark:bg-neutral-800 dark:text-neutral-300"
    }
}

function getDifficultyStars(difficulty: string): number {
    switch (difficulty.toLowerCase()) {
        case "beginner":
            return 1
        case "intermediate":
            return 2
        case "advanced":
            return 3
        default:
            return 1
    }
}

/* ============================================================================
   BREADCRUMB COMPONENT
   ============================================================================ */

interface BreadcrumbProps {
    moduleName: string
    moduleId: string
    labTitle: string
    trackColor: string
}

function Breadcrumb({ moduleName, moduleId, labTitle, trackColor }: BreadcrumbProps) {
    return (
        <nav className="flex items-center gap-1 text-sm mb-6 flex-wrap">
            <Link
                href="/modules"
                className="text-neutral-500 hover:text-neutral-700 dark:hover:text-neutral-300 transition-colors"
            >
                Modules
            </Link>
            <ChevronRight className="h-4 w-4 text-neutral-400" />
            <Link
                href={`/modules/${moduleId}`}
                className="hover:underline transition-colors"
                style={{ color: trackColor }}
            >
                {moduleName}
            </Link>
            <ChevronRight className="h-4 w-4 text-neutral-400" />
            <span className="text-neutral-500">Labs</span>
            <ChevronRight className="h-4 w-4 text-neutral-400" />
            <span className="text-neutral-700 dark:text-neutral-200 font-medium truncate max-w-[200px]">
                {labTitle}
            </span>
        </nav>
    )
}

/* ============================================================================
   LAB HEADER
   ============================================================================ */

interface LabHeaderProps {
    lab: typeof SAMPLE_LAB
    trackColor: string
}

function LabHeader({ lab, trackColor }: LabHeaderProps) {
    const stars = getDifficultyStars(lab.difficulty)

    return (
        <div className="mb-8">
            {/* Icon and title */}
            <div className="flex items-start gap-4 mb-4">
                <div
                    className="p-3 rounded-xl flex-shrink-0"
                    style={{ backgroundColor: `${trackColor}15` }}
                >
                    <FlaskConical
                        className="h-8 w-8"
                        style={{ color: trackColor }}
                    />
                </div>
                <div>
                    <h1 className="text-2xl md:text-3xl font-bold text-neutral-900 dark:text-white">
                        {lab.title}
                    </h1>
                    <p className="text-neutral-500 dark:text-neutral-400 mt-1">
                        Hands-on Lab • {lab.moduleName}
                    </p>
                </div>
            </div>

            {/* Metadata bar */}
            <div className="flex flex-wrap items-center gap-4 pb-6 border-b border-neutral-200 dark:border-neutral-700">
                {/* Difficulty badge */}
                <Badge className={cn("capitalize", getDifficultyColor(lab.difficulty))}>
                    <div className="flex items-center gap-1">
                        {[...Array(3)].map((_, i) => (
                            <Star
                                key={i}
                                className={cn(
                                    "h-3 w-3",
                                    i < stars ? "fill-current" : "opacity-30"
                                )}
                            />
                        ))}
                        <span className="ml-1">{lab.difficulty}</span>
                    </div>
                </Badge>

                {/* Estimated time */}
                <div className="flex items-center gap-1.5 text-sm text-neutral-600 dark:text-neutral-400">
                    <Clock className="h-4 w-4" />
                    <span>~{lab.estimatedMinutes} min</span>
                </div>

                {/* Type badge */}
                <div className="flex items-center gap-1.5 text-sm text-neutral-600 dark:text-neutral-400">
                    <Terminal className="h-4 w-4" style={{ color: trackColor }} />
                    <span>Hands-on Lab</span>
                </div>

                {/* XP reward */}
                <div className="flex items-center gap-1.5 text-sm font-medium">
                    <Zap className="h-4 w-4 text-amber-500" />
                    <span className="text-amber-600 dark:text-amber-400">+{lab.xpReward} XP</span>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   OVERVIEW SECTION
   ============================================================================ */

interface OverviewSectionProps {
    overview: string
}

function OverviewSection({ overview }: OverviewSectionProps) {
    return (
        <div className="mb-8 p-4 rounded-lg bg-neutral-50 dark:bg-neutral-800/50 border border-neutral-200 dark:border-neutral-700">
            <h2 className="text-lg font-semibold text-neutral-900 dark:text-white mb-2">
                Overview
            </h2>
            <p className="text-neutral-600 dark:text-neutral-300 leading-relaxed">
                {overview.trim()}
            </p>
        </div>
    )
}

/* ============================================================================
   COMPLETION BUTTON
   ============================================================================ */

interface CompletionButtonProps {
    isCompleted: boolean
    isCompleting: boolean
    onComplete: () => void
    trackColor: string
}

function CompletionButton({
    isCompleted,
    isCompleting,
    onComplete,
    trackColor,
}: CompletionButtonProps) {
    if (isCompleted) {
        return (
            <div className="flex items-center justify-center gap-3 p-6 rounded-xl bg-gradient-to-r from-green-50 to-emerald-50 dark:from-green-950/30 dark:to-emerald-950/30 border border-green-200 dark:border-green-800">
                <div className="p-2 rounded-full bg-green-100 dark:bg-green-900/50">
                    <Trophy className="h-6 w-6 text-green-600 dark:text-green-400" />
                </div>
                <div className="text-center">
                    <p className="font-semibold text-green-700 dark:text-green-400">
                        Lab Completed!
                    </p>
                    <p className="text-sm text-green-600 dark:text-green-500">
                        Great work on finishing this hands-on lab
                    </p>
                </div>
            </div>
        )
    }

    return (
        <Button
            onClick={onComplete}
            disabled={isCompleting}
            size="lg"
            className="w-full gap-2 h-14 text-base"
            style={{ backgroundColor: trackColor }}
        >
            {isCompleting ? (
                <>
                    <Loader2 className="h-5 w-5 animate-spin" />
                    Completing Lab...
                </>
            ) : (
                <>
                    <CheckCircle2 className="h-5 w-5" />
                    Mark Lab as Complete
                </>
            )}
        </Button>
    )
}

/* ============================================================================
   SIDEBAR NAVIGATION
   ============================================================================ */

interface SidebarNavProps {
    moduleId: string
    trackColor: string
}

function SidebarNav({ moduleId, trackColor }: SidebarNavProps) {
    return (
        <GlassCard className="p-4 sticky top-24">
            <h3 className="font-semibold text-neutral-900 dark:text-white mb-4">
                Quick Navigation
            </h3>
            <nav className="space-y-1">
                {[
                    { label: "Overview", href: "#overview" },
                    { label: "Instructions", href: "#instructions" },
                    { label: "Expected Outcomes", href: "#outcomes" },
                    { label: "Hints", href: "#hints" },
                ].map((item) => (
                    <a
                        key={item.href}
                        href={item.href}
                        className={cn(
                            "block px-3 py-2 text-sm rounded-lg",
                            "text-neutral-600 dark:text-neutral-400",
                            "hover:bg-neutral-100 dark:hover:bg-neutral-800",
                            "transition-colors duration-150"
                        )}
                    >
                        {item.label}
                    </a>
                ))}
            </nav>

            <div className="mt-6 pt-4 border-t border-neutral-200 dark:border-neutral-700">
                <Link href={`/modules/${moduleId}`}>
                    <Button variant="outline" size="sm" className="w-full gap-2">
                        <ArrowLeft className="h-4 w-4" />
                        Back to Module
                    </Button>
                </Link>
            </div>
        </GlassCard>
    )
}

/* ============================================================================
   LOADING SKELETON
   ============================================================================ */

function LabDetailSkeleton() {
    return (
        <div className="min-h-screen bg-neutral-50 dark:bg-neutral-950">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {/* Breadcrumb skeleton */}
                <div className="flex items-center gap-2 mb-6">
                    <div className="h-4 w-16 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                    <div className="h-4 w-4 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                    <div className="h-4 w-24 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
                    {/* Main content skeleton */}
                    <div className="lg:col-span-3 space-y-6">
                        <div className="h-40 bg-neutral-200 dark:bg-neutral-800 rounded-xl animate-pulse" />
                        <div className="h-96 bg-neutral-200 dark:bg-neutral-800 rounded-xl animate-pulse" />
                    </div>

                    {/* Sidebar skeleton */}
                    <div className="hidden lg:block">
                        <div className="h-64 bg-neutral-200 dark:bg-neutral-800 rounded-xl animate-pulse" />
                    </div>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   MAIN PAGE COMPONENT
   ============================================================================ */

export default function LabDetailPage() {
    const params = useParams()
    const router = useRouter()
    const moduleId = params?.id as string
    const labId = params?.labId as string

    // State
    const [loading, setLoading] = React.useState(true)
    const [isCompleting, setIsCompleting] = React.useState(false)
    const [isCompleted, setIsCompleted] = React.useState(false)

    // Use sample data (would fetch from API in real app)
    const lab = SAMPLE_LAB
    const trackColor = getTrackColor(lab.trackSlug)

    // Simulate data loading
    React.useEffect(() => {
        const timer = setTimeout(() => setLoading(false), 500)
        return () => clearTimeout(timer)
    }, [])

    // Handle lab completion
    const handleComplete = async () => {
        setIsCompleting(true)

        // Simulate API call
        await new Promise((resolve) => setTimeout(resolve, 1000))

        setIsCompleted(true)
        setIsCompleting(false)
    }

    // Handle outcomes completion callback
    const handleAllOutcomesComplete = () => {
        // Could auto-enable completion button or show celebration
        console.log("All outcomes completed!")
    }

    if (loading) {
        return <LabDetailSkeleton />
    }

    return (
        <div className="min-h-screen bg-neutral-50 dark:bg-neutral-950">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {/* Breadcrumb */}
                <Breadcrumb
                    moduleName={lab.moduleName}
                    moduleId={lab.moduleId}
                    labTitle={lab.title}
                    trackColor={trackColor}
                />

                <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
                    {/* Main content */}
                    <div className="lg:col-span-3 space-y-8">
                        {/* Lab Header */}
                        <GlassCard className="p-6 md:p-8">
                            <LabHeader lab={lab} trackColor={trackColor} />

                            {/* Overview */}
                            <div id="overview">
                                <OverviewSection overview={lab.overview} />
                            </div>

                            {/* Instructions */}
                            <div id="instructions" className="prose-container">
                                <h2 className="text-xl font-semibold text-neutral-900 dark:text-white mb-4">
                                    Instructions
                                </h2>
                                <MarkdownRenderer content={lab.instructions} />
                            </div>
                        </GlassCard>

                        {/* Outcomes Checklist */}
                        <div id="outcomes">
                            <OutcomeChecklist
                                storageKey={`lab-${labId}`}
                                outcomes={lab.outcomes}
                                trackColor={trackColor}
                                title="Expected Outcomes"
                                onAllComplete={handleAllOutcomesComplete}
                            />
                        </div>

                        {/* Hints */}
                        <div id="hints">
                            <Hints
                                storageKey={`lab-${labId}`}
                                hints={lab.hints}
                                trackColor={trackColor}
                                title="Need Help?"
                                requireConfirmation={true}
                            />
                        </div>

                        {/* Completion Button */}
                        <GlassCard className="p-6">
                            <CompletionButton
                                isCompleted={isCompleted}
                                isCompleting={isCompleting}
                                onComplete={handleComplete}
                                trackColor={trackColor}
                            />
                        </GlassCard>

                        {/* Navigation */}
                        <div className="flex items-center justify-between">
                            <Link href={`/modules/${moduleId}`}>
                                <Button variant="outline" className="gap-2">
                                    <ArrowLeft className="h-4 w-4" />
                                    Back to Module
                                </Button>
                            </Link>
                            <Button className="gap-2" style={{ backgroundColor: trackColor }}>
                                Next Lab
                                <ArrowRight className="h-4 w-4" />
                            </Button>
                        </div>
                    </div>

                    {/* Sidebar */}
                    <div className="hidden lg:block">
                        <SidebarNav moduleId={moduleId} trackColor={trackColor} />
                    </div>
                </div>
            </div>
        </div>
    )
}
