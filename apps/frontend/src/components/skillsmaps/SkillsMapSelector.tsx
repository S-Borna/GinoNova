"use client"

/**
 * ============================================================================
 * SKILLSMAP SELECTOR — Premium Glassmorphism Grid
 * ============================================================================
 *
 * Premium SkillsMap selection grid matching PlatformSelector design:
 * - Glassmorphism cards with holographic borders
 * - Animated gradient backgrounds
 * - Floating particles effect
 * - 3D hover transforms
 * - Category filtering
 *
 * @phase SKILLSMAPS-INTEGRATION
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
   FLOATING PARTICLES
   ============================================================================ */

function FloatingParticles() {
    return (
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
            {[...Array(15)].map((_, i) => (
                <motion.div
                    key={i}
                    className="absolute w-1 h-1 bg-purple-500/20 rounded-full"
                    initial={{
                        x: `${Math.random() * 100}%`,
                        y: "110%",
                        scale: Math.random() * 0.5 + 0.5,
                    }}
                    animate={{
                        y: "-10%",
                        transition: {
                            duration: Math.random() * 15 + 20,
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
   HEADER COMPONENT
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
                "bg-gradient-to-br from-zinc-900 via-purple-950/20 to-zinc-900",
                "border border-purple-500/20",
                "p-8"
            )}
        >
            {/* Ambient glow */}
            <div className="absolute top-0 right-0 w-[400px] h-[400px] bg-purple-500/10 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/4" />
            <div className="absolute bottom-0 left-0 w-[300px] h-[300px] bg-indigo-500/10 rounded-full blur-[80px] translate-y-1/2 -translate-x-1/4" />

            <div className="relative">
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-6">
                    <div>
                        <div className="flex items-center gap-3 mb-3">
                            <div className={cn(
                                "p-2 rounded-xl",
                                "bg-gradient-to-br from-purple-500/20 to-indigo-500/20",
                                "border border-purple-500/30"
                            )}>
                                <BookOpen className="w-5 h-5 text-purple-400" />
                            </div>
                            <span className="text-purple-400 font-semibold text-sm uppercase tracking-wider">
                                SkillsMaps
                            </span>
                        </div>
                        <div className="flex items-center gap-4 flex-wrap">
                            <h1 className={cn(
                                "text-3xl md:text-4xl font-black",
                                "bg-gradient-to-r from-white via-purple-200 to-white bg-clip-text text-transparent"
                            )}>
                                Välj din lärstig
                            </h1>
                            
                            {/* CREATE CUSTOM PATH BUTTON */}
                            <motion.button
                                onClick={onCreatePath}
                                className={cn(
                                    "flex items-center gap-2 px-4 py-2 rounded-xl",
                                    "bg-gradient-to-r from-amber-500/20 to-orange-500/20",
                                    "border border-amber-500/30",
                                    "text-amber-300 text-sm font-medium",
                                    "hover:from-amber-500/30 hover:to-orange-500/30",
                                    "transition-all duration-300"
                                )}
                                whileHover={{ scale: 1.02 }}
                                whileTap={{ scale: 0.98 }}
                            >
                                <Plus className="w-4 h-4" />
                                Skapa egen lärstig
                            </motion.button>
                        </div>
                        <p className="text-zinc-400 mt-2">
                            {totalMaps} kunskapsstigar • {completedMaps} klara
                        </p>
                    </div>

                    {/* Search */}
                    <div className="relative">
                        <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-zinc-500" />
                        <input
                            type="text"
                            placeholder="Sök SkillsMaps..."
                            value={searchQuery}
                            onChange={(e) => onSearchChange(e.target.value)}
                            className={cn(
                                "w-full md:w-80 pl-12 pr-4 py-3 rounded-xl",
                                "bg-zinc-800/50 border border-zinc-700/50",
                                "text-white placeholder-zinc-500",
                                "focus:outline-none focus:border-purple-500/50",
                                "transition-all duration-300"
                            )}
                        />
                    </div>
                </div>

                {/* Progress */}
                <div className={cn(
                    "mt-6 p-4 rounded-xl",
                    "bg-zinc-800/50 border border-zinc-700/50"
                )}>
                    <div className="flex items-center justify-between text-sm mb-2">
                        <span className="text-zinc-400">Total Progress</span>
                        <span className="font-bold text-purple-400">{progress}%</span>
                    </div>
                    <div className="h-2 bg-zinc-700 rounded-full overflow-hidden">
                        <motion.div
                            className="h-full bg-gradient-to-r from-purple-600 to-indigo-500"
                            initial={{ width: 0 }}
                            animate={{ width: `${progress}%` }}
                            transition={{ duration: 1, ease: "easeOut" }}
                            style={{ boxShadow: "0 0 20px rgba(139, 92, 246, 0.5)" }}
                        />
                    </div>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   CATEGORY TABS
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
        <div className="flex flex-wrap gap-2 mb-8">
            {categories.map((cat) => {
                const Icon = cat.icon
                const isActive = activeCategory === cat.id
                const count = counts[cat.id] || 0

                return (
                    <motion.button
                        key={cat.id}
                        onClick={() => onCategoryChange(cat.id)}
                        className={cn(
                            "flex items-center gap-2 px-4 py-2.5 rounded-xl",
                            "text-sm font-medium transition-all duration-300",
                            "border",
                            isActive
                                ? "bg-gradient-to-r text-white border-transparent shadow-lg"
                                : "bg-zinc-900/50 text-zinc-400 border-zinc-800 hover:border-zinc-700 hover:text-zinc-300"
                        )}
                        style={isActive ? {
                            backgroundImage: `linear-gradient(to right, var(--tw-gradient-stops))`,
                            // @ts-ignore
                            "--tw-gradient-from": cat.color.split(" ")[0].replace("from-", ""),
                            "--tw-gradient-to": cat.color.split(" ")[1].replace("to-", ""),
                        } : undefined}
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                    >
                        <Icon className="w-4 h-4" />
                        <span>{cat.label}</span>
                        <span className={cn(
                            "px-1.5 py-0.5 rounded text-xs",
                            isActive ? "bg-white/20" : "bg-zinc-800"
                        )}>
                            {count}
                        </span>
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
