"use client"

/**
 * ============================================================================
 * SKILLSMAP SELECTOR — MILESTONE 2.0: DISNEY + NETFLIX + GOOGLE
 * ============================================================================
 *
 * 🎬 Premium SkillsMap selection with:
 * - Cosmic deep space background
 * - Floating aurora particles
 * - Netflix-smooth animations
 * - Apple-level glassmorphism
 * - Disney magical sparkles
 *
 * @phase MILESTONE-2.0
 */

import { useState, useMemo, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { SkillsMapCard, SkillsMapCardProps } from "./SkillsMapCard"
import { CustomPathBuilder, getCustomPaths, CustomPath } from "./CustomPathBuilder"
import { CustomPathsSection } from "./CustomPathsSection"
import {
    Search,
    Filter,
    Sparkles,
    BookOpen,
    Code2,
    Cloud,
    Server,
    Brain,
    Layers,
    Terminal,
    Database,
    Shield,
    Rocket,
    Plus,
    Wand2,
    Star,
    Zap,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export type SkillsMapCategory =
    | "all"
    | "devops"
    | "programming"
    | "cloud"
    | "ai"
    | "architecture"
    | "security"

export interface SkillsMapSelectorProps {
    skillsmaps: SkillsMapCardProps[]
    onSelect?: (slug: string) => void
    className?: string
}

/* ============================================================================
   CATEGORY CONFIG
   ============================================================================ */

const categories: { id: SkillsMapCategory; label: string; icon: React.ElementType; color: string }[] = [
    { id: "all", label: "Alla", icon: Layers, color: "from-purple-500 to-indigo-500" },
    { id: "devops", label: "DevOps", icon: Rocket, color: "from-orange-500 to-red-500" },
    { id: "programming", label: "Programmering", icon: Code2, color: "from-blue-500 to-cyan-500" },
    { id: "cloud", label: "Cloud", icon: Cloud, color: "from-sky-500 to-blue-500" },
    { id: "ai", label: "AI/ML", icon: Brain, color: "from-pink-500 to-purple-500" },
    { id: "architecture", label: "Arkitektur", icon: Server, color: "from-emerald-500 to-teal-500" },
    { id: "security", label: "Säkerhet", icon: Shield, color: "from-red-500 to-orange-500" },
]

/* ============================================================================
   MAP SKILLSMAP TO CATEGORY
   ============================================================================ */

function getCategory(slug: string): SkillsMapCategory {
    const categoryMap: Record<string, SkillsMapCategory> = {
        // DevOps
        linux: "devops",
        docker: "devops",
        kubernetes: "devops",
        terraform: "devops",
        ansible: "devops",
        cicd: "devops",
        git: "devops",
        bash: "devops",

        // Programming
        python: "programming",
        javascript: "programming",
        typescript: "programming",
        go: "programming",
        nodejs: "programming",

        // Cloud
        aws: "cloud",

        // AI
        prompt_engineering: "ai",
        mlops: "ai",
        ai_agents: "ai",

        // Architecture
        system_design: "architecture",
        sql: "architecture",
    }
    return categoryMap[slug] || "devops"
}

/* ============================================================================
   FLOATING PARTICLES — Aurora Effect ✨
   ============================================================================ */

function FloatingParticles() {
    return (
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
            {/* Aurora gradient orbs */}
            <motion.div
                className="absolute -top-40 -left-40 w-[600px] h-[600px] rounded-full opacity-30"
                style={{
                    background: "radial-gradient(circle, rgba(168,85,247,0.4) 0%, transparent 70%)",
                    filter: "blur(60px)",
                }}
                animate={{
                    scale: [1, 1.2, 1],
                    x: [0, 50, 0],
                    y: [0, 30, 0],
                }}
                transition={{
                    duration: 8,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
            />
            <motion.div
                className="absolute -bottom-40 -right-40 w-[500px] h-[500px] rounded-full opacity-25"
                style={{
                    background: "radial-gradient(circle, rgba(6,182,212,0.4) 0%, transparent 70%)",
                    filter: "blur(60px)",
                }}
                animate={{
                    scale: [1, 1.3, 1],
                    x: [0, -30, 0],
                    y: [0, -50, 0],
                }}
                transition={{
                    duration: 10,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
            />
            
            {/* Floating sparkle particles */}
            {[...Array(20)].map((_, i) => (
                <motion.div
                    key={i}
                    className={cn(
                        "absolute rounded-full",
                        i % 3 === 0 ? "w-1.5 h-1.5 bg-purple-400/40" : 
                        i % 3 === 1 ? "w-1 h-1 bg-cyan-400/30" :
                        "w-2 h-2 bg-pink-400/20"
                    )}
                    initial={{
                        x: `${Math.random() * 100}%`,
                        y: "110%",
                        scale: Math.random() * 0.5 + 0.5,
                    }}
                    animate={{
                        y: "-10%",
                        opacity: [0, 0.8, 0],
                        transition: {
                            duration: Math.random() * 10 + 15,
                            repeat: Infinity,
                            ease: "linear",
                            delay: Math.random() * 10,
                        },
                    }}
                />
            ))}
        </div>
    )
}

/* ============================================================================
   HEADER COMPONENT — Netflix Premium Hero Style 🎬
   ============================================================================ */

function SelectorHeader({
    totalMaps,
    completedMaps,
    searchQuery,
    onSearchChange,
    onCreatePath,
}: {
    totalMaps: number
    completedMaps: number
    searchQuery: string
    onSearchChange: (query: string) => void
    onCreatePath: () => void
}) {
    const progress = totalMaps > 0 ? Math.round((completedMaps / totalMaps) * 100) : 0

    return (
        <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "relative overflow-hidden rounded-3xl mb-8",
                "bg-[#0a0a0f]", // Deep cosmic background
                "border border-purple-500/30",
                "p-8 md:p-10"
            )}
            style={{
                boxShadow: "0 0 80px rgba(168,85,247,0.15), 0 0 40px rgba(6,182,212,0.1)",
            }}
        >
            {/* EPIC AMBIENT GLOW — Multi-layered */}
            <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-purple-600/20 rounded-full blur-[120px] -translate-y-1/2 translate-x-1/4" />
            <div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-cyan-500/15 rounded-full blur-[100px] translate-y-1/2 -translate-x-1/4" />
            <div className="absolute top-1/2 left-1/2 w-[300px] h-[300px] bg-pink-500/10 rounded-full blur-[80px] -translate-x-1/2 -translate-y-1/2" />
            
            {/* Grid pattern overlay */}
            <div 
                className="absolute inset-0 opacity-[0.03]"
                style={{
                    backgroundImage: "linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px)",
                    backgroundSize: "40px 40px",
                }}
            />

            <div className="relative">
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-6">
                    <div>
                        <div className="flex items-center gap-3 mb-4">
                            <motion.div 
                                className={cn(
                                    "p-3 rounded-2xl",
                                    "bg-gradient-to-br from-purple-600/30 to-cyan-500/20",
                                    "border border-purple-400/40"
                                )}
                                animate={{ 
                                    boxShadow: [
                                        "0 0 20px rgba(168,85,247,0.3)",
                                        "0 0 40px rgba(168,85,247,0.5)",
                                        "0 0 20px rgba(168,85,247,0.3)",
                                    ]
                                }}
                                transition={{ duration: 2, repeat: Infinity }}
                            >
                                <BookOpen className="w-6 h-6 text-purple-300" />
                            </motion.div>
                            <span className="text-purple-300 font-bold text-sm uppercase tracking-[0.2em]">
                                SkillsMaps
                            </span>
                        </div>
                        <div className="flex items-center gap-4 flex-wrap">
                            <h1 className={cn(
                                "text-4xl md:text-5xl font-black tracking-tight",
                                "bg-gradient-to-r from-white via-purple-200 to-cyan-200 bg-clip-text text-transparent"
                            )}
                            style={{
                                textShadow: "0 0 40px rgba(168,85,247,0.3)",
                            }}>
                                Dina SkillsMaps
                            </h1>

                            {/* CREATE CUSTOM PATH BUTTON — Netflix Glow */}
                            <motion.button
                                onClick={onCreatePath}
                                className={cn(
                                    "flex items-center gap-2 px-5 py-2.5 rounded-xl",
                                    "bg-gradient-to-r from-amber-500 to-orange-500",
                                    "border border-amber-400/50",
                                    "text-black text-sm font-bold",
                                    "transition-all duration-300"
                                )}
                                whileHover={{ 
                                    scale: 1.05,
                                    boxShadow: "0 0 30px rgba(251,191,36,0.5)",
                                }}
                                whileTap={{ scale: 0.95 }}
                            >
                                <Plus className="w-4 h-4" />
                                Skapa egen SkillsMap
                            </motion.button>
                        </div>
                        <p className="text-zinc-400 mt-3 text-lg">
                            <span className="text-purple-400 font-semibold">{totalMaps}</span> kunskapsstigar • 
                            <span className="text-green-400 font-semibold"> {completedMaps}</span> klara
                        </p>
                    </div>

                    {/* Search — Glassmorphism */}
                    <div className="relative">
                        <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-purple-400" />
                        <input
                            type="text"
                            placeholder="Sök SkillsMaps..."
                            value={searchQuery}
                            onChange={(e) => onSearchChange(e.target.value)}
                            className={cn(
                                "w-full md:w-80 pl-12 pr-4 py-3.5 rounded-xl",
                                "bg-white/5 backdrop-blur-xl",
                                "border border-purple-500/30",
                                "text-white placeholder-zinc-500",
                                "focus:outline-none focus:border-purple-400/60 focus:bg-white/10",
                                "transition-all duration-300"
                            )}
                            style={{
                                boxShadow: "inset 0 0 20px rgba(168,85,247,0.1)",
                            }}
                        />
                    </div>
                </div>

                {/* Progress — Premium Animated Bar */}
                <div className={cn(
                    "mt-8 p-5 rounded-2xl",
                    "bg-white/5 backdrop-blur-xl",
                    "border border-purple-500/20"
                )}>
                    <div className="flex items-center justify-between text-sm mb-3">
                        <span className="text-zinc-300 font-medium">Total Progress</span>
                        <span className="font-black text-2xl bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent">{progress}%</span>
                    </div>
                    <div className="h-3 bg-zinc-800/80 rounded-full overflow-hidden">
                        <motion.div
                            className="h-full bg-gradient-to-r from-purple-600 via-pink-500 to-cyan-400 relative"
                            initial={{ width: 0 }}
                            animate={{ width: `${progress}%` }}
                            transition={{ duration: 1.5, ease: [0.16, 1, 0.3, 1] }}
                        >
                            {/* Shimmer effect */}
                            <motion.div
                                className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent"
                                animate={{ x: ["-100%", "200%"] }}
                                transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
                            />
                        </motion.div>
                    </div>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   CATEGORY TABS — Netflix Style Horizontal Scroll ✨
   ============================================================================ */

function CategoryTabs({
    activeCategory,
    onCategoryChange,
    counts,
}: {
    activeCategory: SkillsMapCategory
    onCategoryChange: (cat: SkillsMapCategory) => void
    counts: Record<SkillsMapCategory, number>
}) {
    return (
        <div className="flex flex-wrap gap-3 mb-10">
            {categories.map((cat) => {
                const Icon = cat.icon
                const isActive = activeCategory === cat.id
                const count = counts[cat.id] || 0

                return (
                    <motion.button
                        key={cat.id}
                        onClick={() => onCategoryChange(cat.id)}
                        className={cn(
                            "relative flex items-center gap-2.5 px-5 py-3 rounded-2xl",
                            "text-sm font-semibold transition-all duration-300",
                            "border backdrop-blur-sm",
                            isActive
                                ? "text-white border-purple-400/50"
                                : "bg-white/5 text-zinc-400 border-white/10 hover:border-purple-500/30 hover:text-zinc-200 hover:bg-white/10"
                        )}
                        style={isActive ? {
                            background: "linear-gradient(135deg, rgba(168,85,247,0.3) 0%, rgba(6,182,212,0.2) 100%)",
                            boxShadow: "0 0 30px rgba(168,85,247,0.3), inset 0 0 20px rgba(168,85,247,0.1)",
                        } : undefined}
                        whileHover={{ scale: 1.03, y: -2 }}
                        whileTap={{ scale: 0.97 }}
                    >
                        <Icon className={cn("w-4 h-4", isActive && "text-purple-300")} />
                        <span>{cat.label}</span>
                        <span className={cn(
                            "px-2 py-0.5 rounded-lg text-xs font-bold",
                            isActive 
                                ? "bg-white/20 text-white" 
                                : "bg-white/10 text-zinc-500"
                        )}>
                            {count}
                        </span>
                        
                        {/* Active indicator glow */}
                        {isActive && (
                            <motion.div
                                className="absolute inset-0 rounded-2xl"
                                style={{
                                    background: "linear-gradient(135deg, rgba(168,85,247,0.2) 0%, transparent 100%)",
                                }}
                                layoutId="activeTab"
                                transition={{ type: "spring", bounce: 0.2, duration: 0.6 }}
                            />
                        )}
                    </motion.button>
                )
            })}
        </div>
    )
}

/* ============================================================================
   SKILLSMAP SELECTOR COMPONENT
   ============================================================================ */

export function SkillsMapSelector({
    skillsmaps,
    onSelect,
    className,
}: SkillsMapSelectorProps) {
    const [searchQuery, setSearchQuery] = useState("")
    const [activeCategory, setActiveCategory] = useState<SkillsMapCategory>("all")
    const [showPathBuilder, setShowPathBuilder] = useState(false)
    const [editingPath, setEditingPath] = useState<CustomPath | undefined>(undefined)
    const [customPaths, setCustomPaths] = useState<CustomPath[]>([])

    // Load custom paths from localStorage
    useEffect(() => {
        setCustomPaths(getCustomPaths())
    }, [])

    const refreshCustomPaths = () => {
        setCustomPaths(getCustomPaths())
    }

    const handleEditPath = (path: CustomPath) => {
        setEditingPath(path)
        setShowPathBuilder(true)
    }

    const handleCreatePath = () => {
        setEditingPath(undefined)
        setShowPathBuilder(true)
    }

    const handleSavePath = (path: CustomPath) => {
        refreshCustomPaths()
    }

    // Calculate category counts
    const categoryCounts = useMemo(() => {
        const counts: Record<SkillsMapCategory, number> = {
            all: skillsmaps.length,
            devops: 0,
            programming: 0,
            cloud: 0,
            ai: 0,
            architecture: 0,
            security: 0,
        }

        skillsmaps.forEach((sm) => {
            const cat = getCategory(sm.slug)
            counts[cat]++
        })

        return counts
    }, [skillsmaps])

    // Filter skillsmaps
    const filteredMaps = useMemo(() => {
        return skillsmaps.filter((sm) => {
            // Search filter
            if (searchQuery) {
                const query = searchQuery.toLowerCase()
                const matchesSearch =
                    sm.title.toLowerCase().includes(query) ||
                    sm.description.toLowerCase().includes(query) ||
                    sm.tags?.some(t => t.toLowerCase().includes(query))
                if (!matchesSearch) return false
            }

            // Category filter
            if (activeCategory !== "all") {
                const smCategory = getCategory(sm.slug)
                if (smCategory !== activeCategory) return false
            }

            return true
        })
    }, [skillsmaps, searchQuery, activeCategory])

    const completedMaps = skillsmaps.filter(sm => sm.status === "complete").length

    return (
        <div className={cn("relative", className)}>
            <FloatingParticles />

            <SelectorHeader
                totalMaps={skillsmaps.length}
                completedMaps={completedMaps}
                searchQuery={searchQuery}
                onSearchChange={setSearchQuery}
                onCreatePath={handleCreatePath}
            />

            {/* Custom Paths Section */}
            <CustomPathsSection
                paths={customPaths}
                onEdit={handleEditPath}
                onRefresh={refreshCustomPaths}
            />

            <CategoryTabs
                activeCategory={activeCategory}
                onCategoryChange={setActiveCategory}
                counts={categoryCounts}
            />

            {/* Grid */}
            <motion.div
                className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
                layout
            >
                <AnimatePresence mode="popLayout">
                    {filteredMaps.map((sm, index) => (
                        <motion.div
                            key={sm.slug}
                            initial={{ opacity: 0, y: 20, scale: 0.95 }}
                            animate={{ opacity: 1, y: 0, scale: 1 }}
                            exit={{ opacity: 0, y: -20, scale: 0.95 }}
                            transition={{
                                duration: 0.3,
                                delay: index * 0.05,
                            }}
                            layout
                        >
                            <SkillsMapCard {...sm} />
                        </motion.div>
                    ))}
                </AnimatePresence>
            </motion.div>

            {/* Empty state */}
            {filteredMaps.length === 0 && (
                <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    className="text-center py-16"
                >
                    <div className="w-16 h-16 mx-auto mb-4 rounded-full bg-zinc-800 flex items-center justify-center">
                        <Search className="w-8 h-8 text-zinc-600" />
                    </div>
                    <h3 className="text-xl font-semibold text-white mb-2">
                        Inga SkillsMaps hittades
                    </h3>
                    <p className="text-zinc-500">
                        Prova att ändra din sökning eller kategori
                    </p>
                </motion.div>
            )}

            {/* Custom Path Builder Modal */}
            <CustomPathBuilder
                isOpen={showPathBuilder}
                onClose={() => {
                    setShowPathBuilder(false)
                    setEditingPath(undefined)
                }}
                onSave={handleSavePath}
                existingPath={editingPath}
            />
        </div>
    )
}

export default SkillsMapSelector
