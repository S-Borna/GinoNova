"use client"

/**
 * ============================================================================
 * PROJECT DETAIL PAGE - Module Capstone Project
 * ============================================================================
 *
 * Features:
 * - Project header with overview
 * - Description section
 * - Requirements list
 * - Deliverables checklist
 * - Submission area (placeholder for future)
 * - Progress tracking
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
    FolderGit2,
    CheckCircle2,
    ArrowLeft,
    Loader2,
    Trophy,
    Star,
    FileText,
    Target,
    Upload,
    ExternalLink,
    GitBranch,
    AlertCircle,
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

const SAMPLE_PROJECT = {
    id: "project-01",
    title: "Personal DevOps Environment Setup",
    moduleId: "module-01",
    moduleName: "Environment Setup",
    trackSlug: "foundation",
    estimatedHours: 3,
    difficulty: "beginner" as const,
    xpReward: 500,
    description: `
## Project Overview

In this capstone project, you'll bring together everything you've learned in this module to create a fully configured personal development environment. This project simulates the real-world scenario of setting up a new development machine from scratch.

### What You'll Build

You'll create a documented, reproducible development environment setup that includes:

1. **Automated installation scripts** for all your development tools
2. **Configuration files** for Git, shell, and editor
3. **Documentation** that would allow you to recreate this setup on a new machine

### Why This Matters

Professional DevOps engineers need to be able to quickly set up and configure development environments. This skill is essential for:

- Onboarding to new teams quickly
- Disaster recovery scenarios
- Setting up CI/CD build agents
- Helping team members with their setups
    `,
    requirements: `
## Requirements

Before starting this project, ensure you have completed:

- ✅ All tasks in Module 01
- ✅ Labs 1-4 (Environment Setup Labs)

### Technical Requirements

- macOS, Linux, or Windows with WSL2
- Git installed and configured
- A GitHub account
- Basic command-line knowledge

### Time Estimate

This project should take approximately **2-3 hours** to complete, depending on your experience level and how thorough you want to be.
    `,
    deliverables: [
        {
            id: "d1",
            label: "GitHub repository created",
            description: "Public repo named 'dotfiles' or 'dev-setup'",
        },
        {
            id: "d2",
            label: "Installation script (install.sh)",
            description: "Automated script to install all tools",
        },
        {
            id: "d3",
            label: "Git configuration (.gitconfig)",
            description: "With aliases and preferred settings",
        },
        {
            id: "d4",
            label: "Shell configuration (.bashrc or .zshrc)",
            description: "With aliases, PATH, and customizations",
        },
        {
            id: "d5",
            label: "VS Code settings (settings.json)",
            description: "Editor preferences and extensions list",
        },
        {
            id: "d6",
            label: "README.md documentation",
            description: "How to use your setup scripts",
        },
        {
            id: "d7",
            label: "Successfully tested on a clean environment",
            description: "Or documented testing process",
        },
    ] as OutcomeItem[],
    hints: [
        {
            id: "h1",
            title: "Repository structure suggestion",
            level: "easy" as const,
            content: `
<p>Here's a recommended structure for your dotfiles repo:</p>
<pre>
dotfiles/
├── install.sh        # Main installation script
├── README.md         # Documentation
├── git/
│   └── .gitconfig
├── shell/
│   ├── .bashrc
│   └── .zshrc
├── vscode/
│   └── settings.json
└── scripts/
    └── helpers.sh
</pre>
            `,
        },
        {
            id: "h2",
            title: "Symbolic links for dotfiles",
            level: "medium" as const,
            content: `
<p>Use symbolic links to connect your repo files to their expected locations:</p>
<pre><code>ln -sf ~/dotfiles/git/.gitconfig ~/.gitconfig
ln -sf ~/dotfiles/shell/.zshrc ~/.zshrc</code></pre>
<p>This way, changes sync automatically between your repo and system config.</p>
            `,
        },
        {
            id: "h3",
            title: "Making install.sh cross-platform",
            level: "detailed" as const,
            content: `
<p>Detect the OS and use appropriate package managers:</p>
<pre><code>#!/bin/bash
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    brew install git vim
elif [[ -f /etc/debian_version ]]; then
    # Debian/Ubuntu
    sudo apt install git vim
fi</code></pre>
            `,
        },
    ] as HintItem[],
}

/* ============================================================================
   DIFFICULTY STYLING
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
    trackColor: string
}

function Breadcrumb({ moduleName, moduleId, trackColor }: BreadcrumbProps) {
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
            <span className="text-neutral-700 dark:text-neutral-200 font-medium">
                Project
            </span>
        </nav>
    )
}

/* ============================================================================
   PROJECT HEADER
   ============================================================================ */

interface ProjectHeaderProps {
    project: typeof SAMPLE_PROJECT
    trackColor: string
}

function ProjectHeader({ project, trackColor }: ProjectHeaderProps) {
    const stars = getDifficultyStars(project.difficulty)

    return (
        <div className="mb-8">
            {/* Icon and title */}
            <div className="flex items-start gap-4 mb-4">
                <div
                    className="p-3 rounded-xl flex-shrink-0"
                    style={{ backgroundColor: `${trackColor}15` }}
                >
                    <FolderGit2
                        className="h-8 w-8"
                        style={{ color: trackColor }}
                    />
                </div>
                <div>
                    <div className="flex items-center gap-2 mb-1">
                        <Badge
                            className="text-xs font-medium"
                            style={{
                                backgroundColor: `${trackColor}20`,
                                color: trackColor,
                            }}
                        >
                            Capstone Project
                        </Badge>
                    </div>
                    <h1 className="text-2xl md:text-3xl font-bold text-neutral-900 dark:text-white">
                        {project.title}
                    </h1>
                    <p className="text-neutral-500 dark:text-neutral-400 mt-1">
                        {project.moduleName}
                    </p>
                </div>
            </div>

            {/* Metadata bar */}
            <div className="flex flex-wrap items-center gap-4 pb-6 border-b border-neutral-200 dark:border-neutral-700">
                {/* Difficulty badge */}
                <Badge className={cn("capitalize", getDifficultyColor(project.difficulty))}>
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
                        <span className="ml-1">{project.difficulty}</span>
                    </div>
                </Badge>

                {/* Estimated time */}
                <div className="flex items-center gap-1.5 text-sm text-neutral-600 dark:text-neutral-400">
                    <Clock className="h-4 w-4" />
                    <span>~{project.estimatedHours} hours</span>
                </div>

                {/* Deliverables count */}
                <div className="flex items-center gap-1.5 text-sm text-neutral-600 dark:text-neutral-400">
                    <Target className="h-4 w-4" style={{ color: trackColor }} />
                    <span>{project.deliverables.length} deliverables</span>
                </div>

                {/* XP reward */}
                <div className="flex items-center gap-1.5 text-sm font-medium">
                    <Zap className="h-4 w-4 text-amber-500" />
                    <span className="text-amber-600 dark:text-amber-400">+{project.xpReward} XP</span>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   REQUIREMENTS SECTION
   ============================================================================ */

interface RequirementsSectionProps {
    requirements: string
}

function RequirementsSection({ requirements }: RequirementsSectionProps) {
    return (
        <GlassCard className="p-6 border-l-4" style={{ borderLeftColor: "#f59e0b" }}>
            <div className="flex items-start gap-3">
                <AlertCircle className="h-5 w-5 text-amber-500 flex-shrink-0 mt-0.5" />
                <div className="prose prose-sm dark:prose-invert max-w-none">
                    <MarkdownRenderer content={requirements} />
                </div>
            </div>
        </GlassCard>
    )
}

/* ============================================================================
   SUBMISSION AREA (Future)
   ============================================================================ */

interface SubmissionAreaProps {
    trackColor: string
}

function SubmissionArea({ trackColor }: SubmissionAreaProps) {
    return (
        <GlassCard className="p-6">
            <h3 className="text-lg font-semibold text-neutral-900 dark:text-white mb-4 flex items-center gap-2">
                <Upload className="h-5 w-5" style={{ color: trackColor }} />
                Submit Your Project
            </h3>

            {/* GitHub link input */}
            <div className="space-y-4">
                <div>
                    <label className="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-2">
                        GitHub Repository URL
                    </label>
                    <div className="flex gap-2">
                        <div className="flex-1 relative">
                            <GitBranch className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-neutral-400" />
                            <input
                                type="url"
                                placeholder="https://github.com/username/repo"
                                className={cn(
                                    "w-full pl-10 pr-4 py-2.5 rounded-lg",
                                    "border border-neutral-200 dark:border-neutral-700",
                                    "bg-white dark:bg-neutral-800",
                                    "text-neutral-900 dark:text-white",
                                    "placeholder:text-neutral-400",
                                    "focus:outline-none focus:ring-2 focus:ring-offset-2",
                                    "transition-shadow duration-200"
                                )}
                                style={{ "--tw-ring-color": trackColor } as React.CSSProperties}
                            />
                        </div>
                        <Button
                            style={{ backgroundColor: trackColor }}
                            className="gap-2"
                        >
                            <ExternalLink className="h-4 w-4" />
                            Submit
                        </Button>
                    </div>
                    <p className="mt-2 text-xs text-neutral-500 dark:text-neutral-400">
                        Make sure your repository is public so reviewers can access it
                    </p>
                </div>

                {/* Additional notes */}
                <div>
                    <label className="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-2">
                        Additional Notes (Optional)
                    </label>
                    <textarea
                        placeholder="Any additional context about your submission..."
                        rows={3}
                        className={cn(
                            "w-full px-4 py-2.5 rounded-lg",
                            "border border-neutral-200 dark:border-neutral-700",
                            "bg-white dark:bg-neutral-800",
                            "text-neutral-900 dark:text-white",
                            "placeholder:text-neutral-400",
                            "focus:outline-none focus:ring-2 focus:ring-offset-2",
                            "transition-shadow duration-200 resize-none"
                        )}
                        style={{ "--tw-ring-color": trackColor } as React.CSSProperties}
                    />
                </div>
            </div>

            {/* Submission status hint */}
            <div className="mt-4 p-3 rounded-lg bg-neutral-50 dark:bg-neutral-800/50 border border-neutral-200 dark:border-neutral-700">
                <p className="text-sm text-neutral-600 dark:text-neutral-400 flex items-start gap-2">
                    <FileText className="h-4 w-4 mt-0.5 flex-shrink-0" />
                    <span>
                        After submission, your project will be reviewed. You&apos;ll receive feedback
                        and XP once approved.
                    </span>
                </p>
            </div>
        </GlassCard>
    )
}

/* ============================================================================
   COMPLETION STATUS
   ============================================================================ */

interface CompletionStatusProps {
    isCompleted: boolean
    isCompleting: boolean
    onComplete: () => void
    trackColor: string
}

function CompletionStatus({
    isCompleted,
    isCompleting,
    onComplete,
    trackColor,
}: CompletionStatusProps) {
    if (isCompleted) {
        return (
            <div className="flex items-center justify-center gap-3 p-6 rounded-xl bg-gradient-to-r from-amber-50 to-green-50 dark:from-amber-950/30 dark:to-green-950/30 border border-green-200 dark:border-green-800">
                <div className="p-3 rounded-full bg-gradient-to-r from-amber-100 to-green-100 dark:from-amber-900/50 dark:to-green-900/50">
                    <Trophy className="h-8 w-8 text-amber-500" />
                </div>
                <div className="text-center">
                    <p className="text-xl font-bold text-green-700 dark:text-green-400">
                        Project Completed!
                    </p>
                    <p className="text-sm text-green-600 dark:text-green-500">
                        Congratulations on finishing this capstone project
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
                    Submitting Project...
                </>
            ) : (
                <>
                    <CheckCircle2 className="h-5 w-5" />
                    Mark Project as Complete
                </>
            )}
        </Button>
    )
}

/* ============================================================================
   SIDEBAR
   ============================================================================ */

interface SidebarProps {
    project: typeof SAMPLE_PROJECT
    moduleId: string
    trackColor: string
}

function Sidebar({ project, moduleId, trackColor }: SidebarProps) {
    return (
        <div className="space-y-6">
            {/* Quick navigation */}
            <GlassCard className="p-4">
                <h3 className="font-semibold text-neutral-900 dark:text-white mb-4">
                    Project Sections
                </h3>
                <nav className="space-y-1">
                    {[
                        { label: "Description", href: "#description" },
                        { label: "Requirements", href: "#requirements" },
                        { label: "Deliverables", href: "#deliverables" },
                        { label: "Hints", href: "#hints" },
                        { label: "Submit", href: "#submit" },
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
            </GlassCard>

            {/* Project stats */}
            <GlassCard className="p-4">
                <h3 className="font-semibold text-neutral-900 dark:text-white mb-4">
                    Project Info
                </h3>
                <div className="space-y-3">
                    <div className="flex items-center justify-between text-sm">
                        <span className="text-neutral-500 dark:text-neutral-400">
                            Estimated Time
                        </span>
                        <span className="font-medium text-neutral-900 dark:text-white">
                            {project.estimatedHours} hours
                        </span>
                    </div>
                    <div className="flex items-center justify-between text-sm">
                        <span className="text-neutral-500 dark:text-neutral-400">
                            Deliverables
                        </span>
                        <span className="font-medium text-neutral-900 dark:text-white">
                            {project.deliverables.length}
                        </span>
                    </div>
                    <div className="flex items-center justify-between text-sm">
                        <span className="text-neutral-500 dark:text-neutral-400">
                            XP Reward
                        </span>
                        <span className="font-medium text-amber-600 dark:text-amber-400">
                            +{project.xpReward} XP
                        </span>
                    </div>
                </div>
            </GlassCard>

            {/* Back button */}
            <Link href={`/modules/${moduleId}`}>
                <Button variant="outline" className="w-full gap-2">
                    <ArrowLeft className="h-4 w-4" />
                    Back to Module
                </Button>
            </Link>
        </div>
    )
}

/* ============================================================================
   LOADING SKELETON
   ============================================================================ */

function ProjectDetailSkeleton() {
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
                        <div className="h-48 bg-neutral-200 dark:bg-neutral-800 rounded-xl animate-pulse" />
                        <div className="h-64 bg-neutral-200 dark:bg-neutral-800 rounded-xl animate-pulse" />
                        <div className="h-96 bg-neutral-200 dark:bg-neutral-800 rounded-xl animate-pulse" />
                    </div>

                    {/* Sidebar skeleton */}
                    <div className="hidden lg:block space-y-6">
                        <div className="h-48 bg-neutral-200 dark:bg-neutral-800 rounded-xl animate-pulse" />
                        <div className="h-32 bg-neutral-200 dark:bg-neutral-800 rounded-xl animate-pulse" />
                    </div>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   MAIN PAGE COMPONENT
   ============================================================================ */

export default function ProjectDetailPage() {
    const params = useParams()
    const router = useRouter()
    const moduleId = params?.id as string

    // State
    const [loading, setLoading] = React.useState(true)
    const [isCompleting, setIsCompleting] = React.useState(false)
    const [isCompleted, setIsCompleted] = React.useState(false)

    // Use sample data (would fetch from API in real app)
    const project = SAMPLE_PROJECT
    const trackColor = getTrackColor(project.trackSlug)

    // Simulate data loading
    React.useEffect(() => {
        const timer = setTimeout(() => setLoading(false), 500)
        return () => clearTimeout(timer)
    }, [])

    // Handle project completion
    const handleComplete = async () => {
        setIsCompleting(true)

        // Simulate API call
        await new Promise((resolve) => setTimeout(resolve, 1000))

        setIsCompleted(true)
        setIsCompleting(false)
    }

    // Handle deliverables completion callback
    const handleAllDeliverablesComplete = () => {
        console.log("All deliverables completed!")
    }

    if (loading) {
        return <ProjectDetailSkeleton />
    }

    return (
        <div className="min-h-screen bg-neutral-50 dark:bg-neutral-950">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {/* Breadcrumb */}
                <Breadcrumb
                    moduleName={project.moduleName}
                    moduleId={project.moduleId}
                    trackColor={trackColor}
                />

                <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
                    {/* Main content */}
                    <div className="lg:col-span-3 space-y-8">
                        {/* Project Header */}
                        <GlassCard className="p-6 md:p-8">
                            <ProjectHeader project={project} trackColor={trackColor} />

                            {/* Description */}
                            <div id="description" className="prose-container">
                                <MarkdownRenderer content={project.description} />
                            </div>
                        </GlassCard>

                        {/* Requirements */}
                        <div id="requirements">
                            <RequirementsSection requirements={project.requirements} />
                        </div>

                        {/* Deliverables Checklist */}
                        <div id="deliverables">
                            <OutcomeChecklist
                                storageKey={`project-${project.id}`}
                                outcomes={project.deliverables}
                                trackColor={trackColor}
                                title="Deliverables Checklist"
                                onAllComplete={handleAllDeliverablesComplete}
                            />
                        </div>

                        {/* Hints */}
                        <div id="hints">
                            <Hints
                                storageKey={`project-${project.id}`}
                                hints={project.hints}
                                trackColor={trackColor}
                                title="Project Hints"
                                requireConfirmation={true}
                            />
                        </div>

                        {/* Submission Area */}
                        <div id="submit">
                            <SubmissionArea trackColor={trackColor} />
                        </div>

                        {/* Completion */}
                        <GlassCard className="p-6">
                            <CompletionStatus
                                isCompleted={isCompleted}
                                isCompleting={isCompleting}
                                onComplete={handleComplete}
                                trackColor={trackColor}
                            />
                        </GlassCard>
                    </div>

                    {/* Sidebar */}
                    <div className="hidden lg:block">
                        <div className="sticky top-24">
                            <Sidebar
                                project={project}
                                moduleId={moduleId}
                                trackColor={trackColor}
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
