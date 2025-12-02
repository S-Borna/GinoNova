"use client"

/**
 * ============================================================================
 * HELP PAGE — Premium Polish Edition
 * ============================================================================
 *
 * User help and support center
 *
 * Sections:
 * - FAQ (Frequently Asked Questions)
 * - Quick Start Guide
 * - Contact Support
 * - Documentation Links
 * - Dallas AI Assistant
 *
 * @phase Premium Upgrade Phase 2
 */

import * as React from "react"
import { useState } from "react"
import { cn } from "@/lib/utils"
import {
    HelpCircle,
    BookOpen,
    MessageCircle,
    Mail,
    ExternalLink,
    ChevronDown,
    ChevronUp,
    Search,
    Zap,
    Target,
    Rocket,
    Shield,
    Clock,
    Star,
    Play,
    FileText,
    Github,
} from "lucide-react"

/* ============================================================================
   FAQ DATA
   ============================================================================ */

interface FAQItem {
    question: string
    answer: string
    category: string
}

const FAQ_DATA: FAQItem[] = [
    {
        category: "Getting Started",
        question: "How do I start learning?",
        answer: "Head to the Modules page and pick a track that matches your goals. Each module contains tasks that build on each other, so we recommend starting from the beginning of a track. Complete tasks to earn XP and track your progress!"
    },
    {
        category: "Getting Started",
        question: "What are XP points and how do I earn them?",
        answer: "XP (Experience Points) are earned by completing tasks, maintaining streaks, and achieving milestones. They represent your progress and unlock achievements. Different tasks award different XP based on difficulty."
    },
    {
        category: "Getting Started",
        question: "What is a learning streak?",
        answer: "A streak counts consecutive days of learning. Complete at least one task per day to maintain your streak. Longer streaks unlock special badges and bonus XP!"
    },
    {
        category: "Features",
        question: "Who is Dallas?",
        answer: "Dallas is your AI-powered DevOps guide. Click the wolf icon (🐺) in the top bar to chat with Dallas. He can answer questions, explain concepts, and help you when you're stuck."
    },
    {
        category: "Features",
        question: "How do bookmarks work?",
        answer: "Click the star icon on any task to bookmark it. Bookmarked tasks appear in your sidebar for quick access. Great for marking tasks you want to revisit or study later!"
    },
    {
        category: "Features",
        question: "What is the SkillPath Board?",
        answer: "The SkillPath Board is a visual map of DevOps skills. It shows how different technologies connect and helps you plan your learning journey. Each node represents a skill you can master."
    },
    {
        category: "Account",
        question: "How do I change my password?",
        answer: "Go to Settings > Security to change your password. You'll need to enter your current password and then set a new one."
    },
    {
        category: "Account",
        question: "Can I delete my account?",
        answer: "Yes, you can delete your account from Settings > Danger Zone. Please note this action is irreversible and will permanently delete all your progress and data."
    },
    {
        category: "Technical",
        question: "What browsers are supported?",
        answer: "DevOpsHub works best on modern browsers: Chrome, Firefox, Safari, and Edge. We recommend keeping your browser updated for the best experience."
    },
    {
        category: "Technical",
        question: "Is my progress saved automatically?",
        answer: "Yes! Your progress is saved automatically as you complete tasks. You can log out and log back in from any device to continue where you left off."
    },
]

/* ============================================================================
   QUICK START GUIDE
   ============================================================================ */

const QUICK_START_STEPS = [
    {
        icon: Target,
        title: "1. Choose Your Path",
        description: "Visit the Modules page and select a learning track that aligns with your goals."
    },
    {
        icon: Play,
        title: "2. Complete Tasks",
        description: "Work through tasks in order. Each task builds on previous knowledge."
    },
    {
        icon: Star,
        title: "3. Earn XP & Badges",
        description: "Gain experience points and unlock achievements as you progress."
    },
    {
        icon: Zap,
        title: "4. Keep Your Streak",
        description: "Learn daily to maintain your streak and earn bonus rewards."
    },
]

/* ============================================================================
   DOCUMENTATION LINKS
   ============================================================================ */

const DOC_LINKS = [
    { icon: BookOpen, label: "Learning Guide", href: "/modules", description: "Browse all learning modules" },
    { icon: FileText, label: "API Documentation", href: "#", description: "Developer API reference" },
    { icon: Github, label: "GitHub Repository", href: "https://github.com/S-Ebadi/saas-project", description: "View source code" },
]

/* ============================================================================
   FAQ ACCORDION COMPONENT
   ============================================================================ */

function FAQAccordion({ items }: { items: FAQItem[] }) {
    const [openIndex, setOpenIndex] = useState<number | null>(null)

    return (
        <div className="space-y-3">
            {items.map((item, index) => (
                <div
                    key={index}
                    className={cn(
                        "rounded-xl overflow-hidden",
                        "bg-zinc-800/30 border border-zinc-700/30",
                        "transition-all"
                    )}
                >
                    <button
                        onClick={() => setOpenIndex(openIndex === index ? null : index)}
                        className="w-full flex items-center justify-between p-4 text-left"
                    >
                        <span className="text-sm font-medium text-zinc-200">{item.question}</span>
                        {openIndex === index ? (
                            <ChevronUp className="w-5 h-5 text-zinc-400 shrink-0" />
                        ) : (
                            <ChevronDown className="w-5 h-5 text-zinc-400 shrink-0" />
                        )}
                    </button>
                    {openIndex === index && (
                        <div className="px-4 pb-4">
                            <p className="text-sm text-zinc-400 leading-relaxed">{item.answer}</p>
                        </div>
                    )}
                </div>
            ))}
        </div>
    )
}

/* ============================================================================
   MAIN PAGE
   ============================================================================ */

export default function HelpPage() {
    const [searchQuery, setSearchQuery] = useState("")
    const [activeCategory, setActiveCategory] = useState("all")

    const categories = ["all", ...Array.from(new Set(FAQ_DATA.map(f => f.category)))]

    const filteredFAQ = FAQ_DATA.filter(item => {
        const matchesSearch = searchQuery === "" ||
            item.question.toLowerCase().includes(searchQuery.toLowerCase()) ||
            item.answer.toLowerCase().includes(searchQuery.toLowerCase())
        const matchesCategory = activeCategory === "all" || item.category === activeCategory
        return matchesSearch && matchesCategory
    })

    return (
        <div className="min-h-screen bg-zinc-950">
            <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
                {/* Header */}
                <div className={cn(
                    "relative overflow-hidden rounded-2xl",
                    "bg-gradient-to-br from-zinc-900 via-blue-950/30 to-zinc-900",
                    "border border-blue-500/20",
                    "p-8"
                )}>
                    <div className="absolute top-0 right-0 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2" />

                    <div className="relative flex items-center gap-4">
                        <div className={cn(
                            "w-14 h-14 rounded-2xl flex items-center justify-center",
                            "bg-gradient-to-br from-blue-500 to-cyan-600",
                            "shadow-[0_0_30px_rgba(59,130,246,0.4)]"
                        )}>
                            <HelpCircle className="w-7 h-7 text-white" />
                        </div>
                        <div>
                            <h1 className="text-2xl md:text-3xl font-bold text-zinc-100">
                                Help Center
                            </h1>
                            <p className="text-zinc-400 mt-1">
                                Find answers, guides, and support
                            </p>
                        </div>
                    </div>
                </div>

                {/* Quick Start Guide */}
                <div className={cn(
                    "rounded-2xl p-6",
                    "bg-zinc-900/80 border border-zinc-800/60"
                )}>
                    <div className="flex items-center gap-2 mb-4">
                        <Rocket className="w-5 h-5 text-emerald-400" />
                        <h2 className="text-lg font-semibold text-zinc-100">Quick Start Guide</h2>
                    </div>

                    <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
                        {QUICK_START_STEPS.map((step, index) => (
                            <div
                                key={index}
                                className={cn(
                                    "p-4 rounded-xl",
                                    "bg-zinc-800/40 border border-zinc-700/30"
                                )}
                            >
                                <div className={cn(
                                    "w-10 h-10 rounded-lg flex items-center justify-center mb-3",
                                    "bg-emerald-500/20"
                                )}>
                                    <step.icon className="w-5 h-5 text-emerald-400" />
                                </div>
                                <h3 className="text-sm font-semibold text-zinc-200 mb-1">{step.title}</h3>
                                <p className="text-xs text-zinc-500">{step.description}</p>
                            </div>
                        ))}
                    </div>
                </div>

                {/* FAQ Section */}
                <div className={cn(
                    "rounded-2xl p-6",
                    "bg-zinc-900/80 border border-zinc-800/60"
                )}>
                    <div className="flex items-center justify-between mb-6">
                        <div className="flex items-center gap-2">
                            <MessageCircle className="w-5 h-5 text-purple-400" />
                            <h2 className="text-lg font-semibold text-zinc-100">Frequently Asked Questions</h2>
                        </div>
                    </div>

                    {/* Search */}
                    <div className="mb-6">
                        <div className="relative">
                            <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-zinc-500" />
                            <input
                                type="text"
                                value={searchQuery}
                                onChange={(e) => setSearchQuery(e.target.value)}
                                placeholder="Search questions..."
                                className={cn(
                                    "w-full pl-12 pr-4 py-3 rounded-xl",
                                    "bg-zinc-800/50 border border-zinc-700/50",
                                    "text-zinc-100 placeholder:text-zinc-500",
                                    "focus:outline-none focus:border-purple-500/50",
                                    "transition-colors"
                                )}
                            />
                        </div>
                    </div>

                    {/* Category Filter */}
                    <div className="flex flex-wrap gap-2 mb-6">
                        {categories.map((cat) => (
                            <button
                                key={cat}
                                onClick={() => setActiveCategory(cat)}
                                className={cn(
                                    "px-4 py-1.5 rounded-full text-sm font-medium",
                                    "transition-all",
                                    activeCategory === cat
                                        ? "bg-purple-500/30 text-purple-300 border border-purple-500/50"
                                        : "bg-zinc-800/50 text-zinc-400 border border-zinc-700/30 hover:text-zinc-200"
                                )}
                            >
                                {cat === "all" ? "All" : cat}
                            </button>
                        ))}
                    </div>

                    {/* FAQ List */}
                    {filteredFAQ.length > 0 ? (
                        <FAQAccordion items={filteredFAQ} />
                    ) : (
                        <div className="text-center py-8">
                            <p className="text-zinc-500">No matching questions found</p>
                        </div>
                    )}
                </div>

                {/* Contact & Documentation */}
                <div className="grid md:grid-cols-2 gap-6">
                    {/* Contact Support */}
                    <div className={cn(
                        "rounded-2xl p-6",
                        "bg-zinc-900/80 border border-zinc-800/60"
                    )}>
                        <div className="flex items-center gap-2 mb-4">
                            <Mail className="w-5 h-5 text-amber-400" />
                            <h2 className="text-lg font-semibold text-zinc-100">Contact Support</h2>
                        </div>

                        <p className="text-sm text-zinc-400 mb-4">
                            Can&apos;t find what you&apos;re looking for? Our team is here to help.
                        </p>

                        <div className="space-y-3">
                            <a
                                href="mailto:support@devopshub.com"
                                className={cn(
                                    "flex items-center gap-3 p-3 rounded-xl",
                                    "bg-zinc-800/40 border border-zinc-700/30",
                                    "hover:border-amber-500/30 transition-all"
                                )}
                            >
                                <Mail className="w-5 h-5 text-amber-400" />
                                <div>
                                    <p className="text-sm font-medium text-zinc-200">Email Support</p>
                                    <p className="text-xs text-zinc-500">support@devopshub.com</p>
                                </div>
                            </a>

                            <div className={cn(
                                "flex items-center gap-3 p-3 rounded-xl",
                                "bg-gradient-to-r from-purple-900/30 to-blue-900/30",
                                "border border-purple-500/30"
                            )}>
                                <span className="text-2xl">🐺</span>
                                <div>
                                    <p className="text-sm font-medium text-zinc-200">Ask Dallas</p>
                                    <p className="text-xs text-zinc-400">Click the wolf icon in the header</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Documentation */}
                    <div className={cn(
                        "rounded-2xl p-6",
                        "bg-zinc-900/80 border border-zinc-800/60"
                    )}>
                        <div className="flex items-center gap-2 mb-4">
                            <BookOpen className="w-5 h-5 text-cyan-400" />
                            <h2 className="text-lg font-semibold text-zinc-100">Documentation</h2>
                        </div>

                        <p className="text-sm text-zinc-400 mb-4">
                            Explore guides and technical documentation.
                        </p>

                        <div className="space-y-3">
                            {DOC_LINKS.map((link, index) => (
                                <a
                                    key={index}
                                    href={link.href}
                                    className={cn(
                                        "flex items-center justify-between p-3 rounded-xl",
                                        "bg-zinc-800/40 border border-zinc-700/30",
                                        "hover:border-cyan-500/30 transition-all group"
                                    )}
                                >
                                    <div className="flex items-center gap-3">
                                        <link.icon className="w-5 h-5 text-cyan-400" />
                                        <div>
                                            <p className="text-sm font-medium text-zinc-200">{link.label}</p>
                                            <p className="text-xs text-zinc-500">{link.description}</p>
                                        </div>
                                    </div>
                                    <ExternalLink className="w-4 h-4 text-zinc-600 group-hover:text-cyan-400 transition-colors" />
                                </a>
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
