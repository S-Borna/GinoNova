"use client"

/**
 * ============================================================================
 * PLAYGROUND PAGE - DevOps Code Practice Arena
 * ============================================================================
 *
 * Interactive code playground where users can practice DevOps commands and
 * scripts in-browser.
 *
 * Features:
 * - Multiple environments (Bash, Python, Docker, Kubernetes, Terraform)
 * - Monaco Editor with syntax highlighting
 * - Sample snippets library
 * - Tips and common commands
 * - Keyboard shortcuts
 * - Save/Load/Share functionality
 *
 * @phase PLAYGROUND
 */

import { useState } from 'react'
import { motion } from 'framer-motion'
import { cn } from '@/lib/utils'
import { PageLayout } from '@saas/ui'
import { CodePlayground } from '@/components/playground/CodePlayground'
import {
    Code2,
    Terminal,
    FileCode,
    Settings,
    Sparkles,
    Zap,
    BookOpen,
    Rocket,
    Target,
    Award,
    ArrowRight,
    LightbulbIcon,
    KeyboardIcon,
} from 'lucide-react'
import Link from 'next/link'

/* ============================================================================
   COSMIC AURORA BACKGROUND
   ============================================================================ */

function CosmicAurora() {
    return (
        <div className="fixed inset-0 pointer-events-none overflow-hidden">
            {/* Deep cosmic base */}
            <div className="absolute inset-0 bg-[#05050a]" />

            {/* Subtle grid pattern */}
            <div
                className="absolute inset-0 opacity-[0.03]"
                style={{
                    backgroundImage: `
                        linear-gradient(rgba(139, 92, 246, 0.3) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(139, 92, 246, 0.3) 1px, transparent 1px)
                    `,
                    backgroundSize: '60px 60px'
                }}
            />

            {/* Aurora orbs */}
            <motion.div
                className="absolute -top-40 -right-40 w-[800px] h-[800px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(139, 92, 246, 0.15) 0%, rgba(139, 92, 246, 0.05) 40%, transparent 70%)',
                }}
                animate={{
                    scale: [1, 1.1, 1],
                    opacity: [0.6, 0.8, 0.6],
                }}
                transition={{
                    duration: 8,
                    repeat: Infinity,
                    ease: "easeInOut"
                }}
            />

            <motion.div
                className="absolute -bottom-60 -left-60 w-[700px] h-[700px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(34, 211, 238, 0.12) 0%, rgba(34, 211, 238, 0.04) 40%, transparent 70%)',
                }}
                animate={{
                    scale: [1, 1.15, 1],
                    opacity: [0.5, 0.7, 0.5],
                }}
                transition={{
                    duration: 10,
                    repeat: Infinity,
                    ease: "easeInOut",
                    delay: 2
                }}
            />
        </div>
    )
}

/* ============================================================================
   HERO SECTION
   ============================================================================ */

function PlaygroundHero() {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
            className={cn(
                "relative overflow-hidden rounded-3xl",
                "bg-gradient-to-br from-[#0a0a0f] via-purple-950/20 to-[#0a0a0f]",
                "border border-purple-500/20",
                "p-8 md:p-12",
                "shadow-[0_0_80px_rgba(139,92,246,0.15)]",
                "mb-8"
            )}
        >
            {/* Cosmic glow effects */}
            <div className="absolute top-0 right-0 w-[600px] h-[600px] bg-purple-500/10 rounded-full blur-[120px] -translate-y-1/2 translate-x-1/4" />
            <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-cyan-500/8 rounded-full blur-[100px] translate-y-1/2 -translate-x-1/4" />

            {/* Animated particles */}
            <motion.div
                className="absolute top-8 right-20 text-purple-400/60"
                animate={{
                    rotate: 360,
                    scale: [1, 1.3, 1],
                    opacity: [0.4, 0.8, 0.4]
                }}
                transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
            >
                <Sparkles className="w-6 h-6" />
            </motion.div>

            <div className="relative">
                <motion.div
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
                    className="flex items-center gap-3 mb-4"
                >
                    <motion.div
                        className={cn(
                            "relative p-2.5 rounded-xl",
                            "bg-gradient-to-br from-purple-500/30 to-purple-600/20",
                            "border border-purple-500/40"
                        )}
                        animate={{
                            boxShadow: [
                                '0 0 20px rgba(139, 92, 246, 0.3)',
                                '0 0 40px rgba(139, 92, 246, 0.5)',
                                '0 0 20px rgba(139, 92, 246, 0.3)',
                            ]
                        }}
                        transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                    >
                        <Code2 className="w-5 h-5 text-purple-400" />
                    </motion.div>
                    <span className="text-purple-400 font-semibold text-sm uppercase tracking-wider">
                        Interactive Playground
                    </span>
                </motion.div>

                <motion.h1
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.3, ease: [0.16, 1, 0.3, 1] }}
                    className={cn(
                        "text-3xl md:text-4xl lg:text-5xl font-black mb-4",
                        "bg-gradient-to-r from-white via-purple-200 to-cyan-200 bg-clip-text text-transparent"
                    )}
                >
                    Practice DevOps In-Browser
                </motion.h1>

                <motion.p
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.4, ease: [0.16, 1, 0.3, 1] }}
                    className="text-zinc-400 text-lg max-w-3xl mb-6"
                >
                    Master DevOps tools and commands with our interactive code playground. Practice Bash, Python, Docker, Kubernetes, and Terraform right in your browser with instant feedback.
                </motion.p>

                <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.5 }}
                    className="flex flex-wrap gap-3"
                >
                    <Link href="/playground/challenges">
                        <motion.button
                            className={cn(
                                "px-6 py-3 rounded-xl",
                                "bg-gradient-to-r from-purple-600 to-purple-700",
                                "hover:from-purple-500 hover:to-purple-600",
                                "text-white font-semibold",
                                "shadow-[0_0_30px_rgba(139,92,246,0.3)]",
                                "flex items-center gap-2"
                            )}
                            whileHover={{ scale: 1.05 }}
                            whileTap={{ scale: 0.95 }}
                        >
                            <Target className="w-5 h-5" />
                            Try Challenges
                            <ArrowRight className="w-5 h-5" />
                        </motion.button>
                    </Link>
                </motion.div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   ENVIRONMENT CARDS
   ============================================================================ */

function EnvironmentCard({ icon: Icon, name, description, color, examples }: any) {
    const [expanded, setExpanded] = useState(false)

    const colorMap: any = {
        emerald: {
            bg: "from-emerald-600/20 to-emerald-500/5",
            border: "border-emerald-500/40",
            text: "text-emerald-400",
            icon: "from-emerald-500 to-teal-600",
        },
        blue: {
            bg: "from-blue-600/20 to-blue-500/5",
            border: "border-blue-500/40",
            text: "text-blue-400",
            icon: "from-blue-500 to-indigo-600",
        },
        cyan: {
            bg: "from-cyan-600/20 to-cyan-500/5",
            border: "border-cyan-500/40",
            text: "text-cyan-400",
            icon: "from-cyan-500 to-cyan-600",
        },
        purple: {
            bg: "from-purple-600/20 to-purple-500/5",
            border: "border-purple-500/40",
            text: "text-purple-400",
            icon: "from-purple-500 to-purple-700",
        },
        violet: {
            bg: "from-violet-600/20 to-violet-500/5",
            border: "border-violet-500/40",
            text: "text-violet-400",
            icon: "from-violet-500 to-violet-700",
        },
    }

    const styles = colorMap[color] || colorMap.purple

    return (
        <motion.div
            className={cn(
                "p-6 rounded-2xl",
                "bg-gradient-to-br",
                styles.bg,
                "border",
                styles.border,
                "backdrop-blur-sm",
                "cursor-pointer"
            )}
            whileHover={{ scale: 1.02, y: -3 }}
            onClick={() => setExpanded(!expanded)}
        >
            <div className="flex items-start gap-4">
                <motion.div
                    className={cn(
                        "w-12 h-12 rounded-xl shrink-0",
                        "bg-gradient-to-br",
                        styles.icon,
                        "flex items-center justify-center"
                    )}
                >
                    <Icon className="w-6 h-6 text-white" />
                </motion.div>
                <div className="flex-1">
                    <h3 className={cn("text-lg font-semibold mb-1", styles.text)}>{name}</h3>
                    <p className="text-zinc-400 text-sm">{description}</p>
                    {expanded && (
                        <motion.div
                            initial={{ opacity: 0, height: 0 }}
                            animate={{ opacity: 1, height: 'auto' }}
                            className="mt-3 pt-3 border-t border-zinc-700/50"
                        >
                            <p className="text-xs text-zinc-500 mb-2">Common commands:</p>
                            <div className="space-y-1">
                                {examples.map((ex: string, idx: number) => (
                                    <code key={idx} className="block text-xs text-zinc-400 font-mono">
                                        {ex}
                                    </code>
                                ))}
                            </div>
                        </motion.div>
                    )}
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   TIPS & SHORTCUTS
   ============================================================================ */

function TipsSection() {
    return (
        <div className="grid md:grid-cols-2 gap-6 mb-8">
            {/* Tips */}
            <motion.div
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.6 }}
                className={cn(
                    "p-6 rounded-2xl",
                    "bg-gradient-to-br from-amber-600/20 to-amber-500/5",
                    "border border-amber-500/40"
                )}
            >
                <div className="flex items-center gap-3 mb-4">
                    <LightbulbIcon className="w-5 h-5 text-amber-400" />
                    <h3 className="text-lg font-semibold text-amber-400">Tips & Tricks</h3>
                </div>
                <ul className="space-y-2 text-sm text-zinc-400">
                    <li className="flex items-start gap-2">
                        <span className="text-amber-400 mt-1">•</span>
                        <span>Use the snippet library to load common examples</span>
                    </li>
                    <li className="flex items-start gap-2">
                        <span className="text-amber-400 mt-1">•</span>
                        <span>All code runs securely in your browser</span>
                    </li>
                    <li className="flex items-start gap-2">
                        <span className="text-amber-400 mt-1">•</span>
                        <span>Python uses Pyodide for real execution</span>
                    </li>
                    <li className="flex items-start gap-2">
                        <span className="text-amber-400 mt-1">•</span>
                        <span>Docker & Kubernetes commands are simulated</span>
                    </li>
                    <li className="flex items-start gap-2">
                        <span className="text-amber-400 mt-1">•</span>
                        <span>Share your code with the share button</span>
                    </li>
                </ul>
            </motion.div>

            {/* Keyboard Shortcuts */}
            <motion.div
                initial={{ opacity: 0, x: 20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.7 }}
                className={cn(
                    "p-6 rounded-2xl",
                    "bg-gradient-to-br from-cyan-600/20 to-cyan-500/5",
                    "border border-cyan-500/40"
                )}
            >
                <div className="flex items-center gap-3 mb-4">
                    <KeyboardIcon className="w-5 h-5 text-cyan-400" />
                    <h3 className="text-lg font-semibold text-cyan-400">Keyboard Shortcuts</h3>
                </div>
                <div className="space-y-3 text-sm">
                    <div className="flex items-center justify-between">
                        <span className="text-zinc-400">Run code</span>
                        <kbd className="px-2 py-1 rounded bg-zinc-800 text-cyan-400 font-mono text-xs">
                            Cmd/Ctrl + Enter
                        </kbd>
                    </div>
                    <div className="flex items-center justify-between">
                        <span className="text-zinc-400">Save code</span>
                        <kbd className="px-2 py-1 rounded bg-zinc-800 text-cyan-400 font-mono text-xs">
                            Cmd/Ctrl + S
                        </kbd>
                    </div>
                    <div className="flex items-center justify-between">
                        <span className="text-zinc-400">Format code</span>
                        <kbd className="px-2 py-1 rounded bg-zinc-800 text-cyan-400 font-mono text-xs">
                            Shift + Alt + F
                        </kbd>
                    </div>
                    <div className="flex items-center justify-between">
                        <span className="text-zinc-400">Toggle comment</span>
                        <kbd className="px-2 py-1 rounded bg-zinc-800 text-cyan-400 font-mono text-xs">
                            Cmd/Ctrl + /
                        </kbd>
                    </div>
                </div>
            </motion.div>
        </div>
    )
}

/* ============================================================================
   MAIN PAGE
   ============================================================================ */

export default function PlaygroundPage() {
    return (
        <PageLayout maxWidth="wide" background="cosmic">
            <CosmicAurora />

            <div className="relative z-10 space-y-8">
                {/* Hero */}
                <PlaygroundHero />

                {/* Main Playground */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.3 }}
                >
                    <CodePlayground
                        defaultEnvironment="bash"
                        showEnvironmentSelector={true}
                        showSnippets={true}
                        showSaveLoad={true}
                        showShare={true}
                        height="600px"
                    />
                </motion.div>

                {/* Tips & Shortcuts */}
                <TipsSection />

                {/* Environment Cards */}
                <div className="space-y-4">
                    <h2 className="text-2xl font-bold text-white flex items-center gap-2">
                        <BookOpen className="w-6 h-6 text-purple-400" />
                        Available Environments
                    </h2>
                    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
                        <EnvironmentCard
                            icon={Terminal}
                            name="Bash Terminal"
                            description="Practice Linux shell commands"
                            color="emerald"
                            examples={['ls -la', 'pwd', 'cat file.txt', 'grep pattern file']}
                        />
                        <EnvironmentCard
                            icon={FileCode}
                            name="Python"
                            description="Execute Python scripts"
                            color="blue"
                            examples={['print("Hello")', 'for i in range(10):', 'import json']}
                        />
                        <EnvironmentCard
                            icon={Code2}
                            name="Docker"
                            description="Simulate Docker commands"
                            color="cyan"
                            examples={['docker ps', 'docker run nginx', 'docker images']}
                        />
                        <EnvironmentCard
                            icon={Settings}
                            name="Kubernetes"
                            description="Validate K8s YAML"
                            color="purple"
                            examples={['kind: Deployment', 'replicas: 3', 'containers:']}
                        />
                        <EnvironmentCard
                            icon={Sparkles}
                            name="Terraform"
                            description="Validate HCL syntax"
                            color="violet"
                            examples={['resource "aws_instance"', 'variable "region"']}
                        />
                    </div>
                </div>

                {/* CTA Section */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.8 }}
                    className={cn(
                        "p-8 rounded-2xl text-center",
                        "bg-gradient-to-br from-purple-600/20 to-purple-500/5",
                        "border border-purple-500/40"
                    )}
                >
                    <Rocket className="w-12 h-12 text-purple-400 mx-auto mb-4" />
                    <h3 className="text-2xl font-bold text-white mb-2">
                        Ready for a Challenge?
                    </h3>
                    <p className="text-zinc-400 mb-6 max-w-2xl mx-auto">
                        Test your skills with real-world DevOps challenges. Earn XP and level up your expertise!
                    </p>
                    <Link href="/playground/challenges">
                        <motion.button
                            className={cn(
                                "px-8 py-3 rounded-xl",
                                "bg-gradient-to-r from-purple-600 to-purple-700",
                                "hover:from-purple-500 hover:to-purple-600",
                                "text-white font-semibold",
                                "shadow-[0_0_30px_rgba(139,92,246,0.3)]",
                                "inline-flex items-center gap-2"
                            )}
                            whileHover={{ scale: 1.05 }}
                            whileTap={{ scale: 0.95 }}
                        >
                            <Award className="w-5 h-5" />
                            View Challenges
                            <ArrowRight className="w-5 h-5" />
                        </motion.button>
                    </Link>
                </motion.div>
            </div>
        </PageLayout>
    )
}
