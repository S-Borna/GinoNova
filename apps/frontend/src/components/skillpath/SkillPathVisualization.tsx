"use client"

/**
 * ============================================================================
 * SKILLPATH VISUALIZATION — Interactive learning path skill tree
 * ============================================================================
 *
 * Visual node graph showing module connections like a skill tree in video games.
 * Features zoom, pan, and interactive module nodes.
 *
 * @phase SKILLPATH-VISUALIZATION
 */

import { useState, useRef, useEffect, useMemo } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    ZoomIn,
    ZoomOut,
    Maximize2,
    X,
    Filter,
    Search,
    ChevronDown
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { ModuleNode, ModuleNodeStatus, ModuleNodeDifficulty } from "./ModuleNode"
import { LearningPath, MODULE_POSITIONS } from "@/lib/learning-paths"
import { ModulePublic } from "@/lib/modules"

export interface SkillPathVisualizationProps {
    path: LearningPath
    modules: ModulePublic[]
    completedModules: string[]
    onModuleClick: (moduleSlug: string) => void
    className?: string
}

interface ModuleNodeData {
    slug: string
    title: string
    icon: string
    duration: number
    difficulty: ModuleNodeDifficulty
    status: ModuleNodeStatus
    color: string
    x: number
    y: number
    level: number
    progress?: number
}

/**
 * Get module metadata from skillsmaps
 */
const MODULE_METADATA: Record<string, { icon: string; color: string }> = {
    "linux-247": { icon: "🐧", color: "#FCC624" },
    "python-devops": { icon: "🐍", color: "#3776AB" },
    "docker-mastery": { icon: "🐳", color: "#2496ED" },
    "kubernetes-mastery": { icon: "☸️", color: "#326CE5" },
    "terraform-mastery": { icon: "🏗️", color: "#7B42BC" },
    "aws-devops": { icon: "☁️", color: "#FF9900" },
    "git-github-mastery": { icon: "🔀", color: "#F05032" },
    "cicd-mastery": { icon: "🚀", color: "#2088FF" },
    "bash-mastery": { icon: "💻", color: "#4EAA25" },
    "nodejs-mastery": { icon: "💚", color: "#339933" },
    "typescript-mastery": { icon: "🔷", color: "#3178C6" },
    "go-mastery": { icon: "🔵", color: "#00ADD8" },
    "ansible-mastery": { icon: "⚙️", color: "#EE0000" },
    "system-design": { icon: "🏛️", color: "#6366F1" },
    "mlops-mastery": { icon: "🤖", color: "#FF6B6B" },
    "ai-agents": { icon: "🤖", color: "#7C3AED" },
    "react-nextjs": { icon: "⚛️", color: "#61DAFB" },
    "azure-mastery": { icon: "☁️", color: "#0078D4" },
    "dotnet-mastery": { icon: "🟣", color: "#512BD4" },
}

function getModuleMeta(slug: string) {
    return MODULE_METADATA[slug] || { icon: "📚", color: "#6366F1" }
}

/**
 * SkillPathVisualization Component
 */
export function SkillPathVisualization({
    path,
    modules,
    completedModules,
    onModuleClick,
    className
}: SkillPathVisualizationProps) {
    const [zoom, setZoom] = useState(1)
    const [pan, setPan] = useState({ x: 0, y: 0 })
    const [isDragging, setIsDragging] = useState(false)
    const [dragStart, setDragStart] = useState({ x: 0, y: 0 })
    const [searchQuery, setSearchQuery] = useState("")
    const [difficultyFilter, setDifficultyFilter] = useState<string>("all")
    const containerRef = useRef<HTMLDivElement>(null)

    // Build module node data
    const moduleNodes: ModuleNodeData[] = useMemo(() => {
        return path.modules.map((moduleSlug, index) => {
            const module = modules.find(m => m.slug === moduleSlug)
            const position = MODULE_POSITIONS[moduleSlug] || {
                x: 100 + (index % 4) * 250,
                y: 100 + Math.floor(index / 4) * 200,
                level: Math.floor(index / 4)
            }
            const meta = getModuleMeta(moduleSlug)
            const isCompleted = completedModules.includes(moduleSlug)
            const prevModuleSlug = index > 0 ? path.modules[index - 1] : null
            const isPrevCompleted = prevModuleSlug ? completedModules.includes(prevModuleSlug) : true

            // Determine status
            let status: ModuleNodeStatus
            if (isCompleted) {
                status = "completed"
            } else if (index === 0 || isPrevCompleted) {
                status = "unlocked"
            } else {
                status = "locked"
            }

            return {
                slug: moduleSlug,
                title: module?.name || moduleSlug,
                icon: meta.icon,
                duration: module?.estimated_hours || 20,
                difficulty: (module?.difficulty || "intermediate") as ModuleNodeDifficulty,
                status,
                color: meta.color,
                x: position.x,
                y: position.y,
                level: position.level,
                progress: isCompleted ? 100 : 0
            }
        })
    }, [path, modules, completedModules])

    // Filter modules based on search and difficulty
    const filteredNodes = useMemo(() => {
        let filtered = moduleNodes

        // Search filter
        if (searchQuery) {
            filtered = filtered.filter(node =>
                node.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                node.slug.toLowerCase().includes(searchQuery.toLowerCase())
            )
        }

        // Difficulty filter
        if (difficultyFilter !== "all") {
            filtered = filtered.filter(node => node.difficulty === difficultyFilter)
        }

        return filtered
    }, [moduleNodes, searchQuery, difficultyFilter])

    // Draw connections between nodes
    const connections = useMemo(() => {
        const lines: Array<{ from: ModuleNodeData; to: ModuleNodeData }> = []
        for (let i = 1; i < moduleNodes.length; i++) {
            const fromNode = moduleNodes[i - 1]
            const toNode = moduleNodes[i]
            lines.push({ from: fromNode, to: toNode })
        }
        return lines
    }, [moduleNodes])

    // Zoom handlers
    const handleZoomIn = () => setZoom(prev => Math.min(prev + 0.2, 2))
    const handleZoomOut = () => setZoom(prev => Math.max(prev - 0.2, 0.5))
    const handleResetView = () => {
        setZoom(1)
        setPan({ x: 0, y: 0 })
    }

    // Pan handlers
    const handleMouseDown = (e: React.MouseEvent) => {
        if (e.button === 0) { // Left click only
            setIsDragging(true)
            setDragStart({ x: e.clientX - pan.x, y: e.clientY - pan.y })
        }
    }

    const handleMouseMove = (e: React.MouseEvent) => {
        if (isDragging) {
            setPan({
                x: e.clientX - dragStart.x,
                y: e.clientY - dragStart.y
            })
        }
    }

    const handleMouseUp = () => {
        setIsDragging(false)
    }

    // Calculate canvas size based on node positions
    const canvasSize = useMemo(() => {
        const maxX = Math.max(...moduleNodes.map(n => n.x)) + 200
        const maxY = Math.max(...moduleNodes.map(n => n.y)) + 200
        return { width: maxX, height: maxY }
    }, [moduleNodes])

    return (
        <div className={cn("relative w-full h-full rounded-2xl overflow-hidden bg-[#05050a] border border-purple-500/30", className)}>
            {/* Toolbar */}
            <div className="absolute top-4 left-4 right-4 z-20 flex items-center justify-between gap-4">
                {/* Search */}
                <div className="flex-1 max-w-xs">
                    <div className="relative">
                        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
                        <Input
                            type="text"
                            placeholder="Sök modul..."
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                            className="pl-10 bg-neutral-900/80 border-neutral-700 text-white placeholder:text-gray-500"
                        />
                    </div>
                </div>

                {/* Difficulty Filter */}
                <div className="relative">
                    <select
                        value={difficultyFilter}
                        onChange={(e) => setDifficultyFilter(e.target.value)}
                        className="px-4 py-2 rounded-lg bg-neutral-900/80 border border-neutral-700 text-white text-sm appearance-none pr-8 cursor-pointer"
                    >
                        <option value="all">Alla nivåer</option>
                        <option value="beginner">Nybörjare</option>
                        <option value="intermediate">Medel</option>
                        <option value="advanced">Avancerad</option>
                        <option value="expert">Expert</option>
                    </select>
                    <ChevronDown className="absolute right-2 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400 pointer-events-none" />
                </div>

                {/* Zoom Controls */}
                <div className="flex items-center gap-2 bg-neutral-900/80 border border-neutral-700 rounded-lg p-1">
                    <Button
                        onClick={handleZoomOut}
                        size="sm"
                        variant="ghost"
                        className="h-8 w-8 p-0"
                    >
                        <ZoomOut className="w-4 h-4" />
                    </Button>
                    <span className="text-sm text-white font-medium min-w-[3rem] text-center">
                        {Math.round(zoom * 100)}%
                    </span>
                    <Button
                        onClick={handleZoomIn}
                        size="sm"
                        variant="ghost"
                        className="h-8 w-8 p-0"
                    >
                        <ZoomIn className="w-4 h-4" />
                    </Button>
                    <Button
                        onClick={handleResetView}
                        size="sm"
                        variant="ghost"
                        className="h-8 w-8 p-0"
                    >
                        <Maximize2 className="w-4 h-4" />
                    </Button>
                </div>
            </div>

            {/* Canvas */}
            <div
                ref={containerRef}
                className="w-full h-full overflow-hidden cursor-move"
                onMouseDown={handleMouseDown}
                onMouseMove={handleMouseMove}
                onMouseUp={handleMouseUp}
                onMouseLeave={handleMouseUp}
            >
                <motion.div
                    className="relative"
                    style={{
                        width: canvasSize.width,
                        height: canvasSize.height,
                        transform: `scale(${zoom}) translate(${pan.x}px, ${pan.y}px)`,
                        transformOrigin: "0 0"
                    }}
                    transition={{ type: "spring", stiffness: 300, damping: 30 }}
                >
                    {/* SVG for connections */}
                    <svg
                        className="absolute inset-0 pointer-events-none"
                        width={canvasSize.width}
                        height={canvasSize.height}
                    >
                        <defs>
                            {/* Gradient definitions for lines */}
                            {connections.map((conn, idx) => (
                                <linearGradient
                                    key={`gradient-${idx}`}
                                    id={`gradient-${idx}`}
                                    x1="0%"
                                    y1="0%"
                                    x2="100%"
                                    y2="0%"
                                >
                                    <stop offset="0%" stopColor={conn.from.color} stopOpacity="0.6" />
                                    <stop offset="100%" stopColor={conn.to.color} stopOpacity="0.6" />
                                </linearGradient>
                            ))}
                        </defs>

                        {/* Connection lines */}
                        {connections.map((conn, idx) => {
                            const isVisible =
                                filteredNodes.includes(conn.from) &&
                                filteredNodes.includes(conn.to)

                            if (!isVisible) return null

                            const isCompleted =
                                conn.from.status === "completed" &&
                                conn.to.status === "completed"

                            return (
                                <motion.line
                                    key={idx}
                                    x1={conn.from.x + 80}
                                    y1={conn.from.y + 80}
                                    x2={conn.to.x + 80}
                                    y2={conn.to.y + 80}
                                    stroke={`url(#gradient-${idx})`}
                                    strokeWidth={isCompleted ? "4" : "2"}
                                    strokeDasharray={isCompleted ? "0" : "5,5"}
                                    initial={{ pathLength: 0 }}
                                    animate={{ pathLength: 1 }}
                                    transition={{ duration: 1, delay: idx * 0.1 }}
                                />
                            )
                        })}

                        {/* Animated particles along completed paths */}
                        {connections
                            .filter(conn => conn.from.status === "completed" && conn.to.status === "completed")
                            .map((conn, idx) => (
                                <motion.circle
                                    key={`particle-${idx}`}
                                    r="3"
                                    fill={conn.from.color}
                                    initial={{
                                        cx: conn.from.x + 80,
                                        cy: conn.from.y + 80
                                    }}
                                    animate={{
                                        cx: [conn.from.x + 80, conn.to.x + 80],
                                        cy: [conn.from.y + 80, conn.to.y + 80]
                                    }}
                                    transition={{
                                        duration: 2,
                                        repeat: Infinity,
                                        ease: "linear",
                                        delay: idx * 0.3
                                    }}
                                />
                            ))}
                    </svg>

                    {/* Module Nodes */}
                    <AnimatePresence>
                        {filteredNodes.map((node, index) => (
                            <motion.div
                                key={node.slug}
                                initial={{ opacity: 0, scale: 0 }}
                                animate={{ opacity: 1, scale: 1 }}
                                exit={{ opacity: 0, scale: 0 }}
                                transition={{ delay: index * 0.05 }}
                                style={{
                                    position: "absolute",
                                    left: node.x,
                                    top: node.y
                                }}
                            >
                                <ModuleNode
                                    id={node.slug}
                                    slug={node.slug}
                                    title={node.title}
                                    icon={node.icon}
                                    duration={node.duration}
                                    difficulty={node.difficulty}
                                    status={node.status}
                                    color={node.color}
                                    progress={node.progress}
                                    onClick={() => {
                                        if (node.status !== "locked") {
                                            onModuleClick(node.slug)
                                        }
                                    }}
                                    size="medium"
                                />
                            </motion.div>
                        ))}
                    </AnimatePresence>
                </motion.div>
            </div>

            {/* Legend */}
            <div className="absolute bottom-4 left-4 bg-neutral-900/90 border border-neutral-700 rounded-lg p-3 backdrop-blur-sm">
                <p className="text-xs font-semibold text-white mb-2">Status:</p>
                <div className="flex flex-col gap-1.5 text-xs">
                    <div className="flex items-center gap-2">
                        <div className="w-3 h-3 rounded-full bg-green-500" />
                        <span className="text-gray-300">Klar</span>
                    </div>
                    <div className="flex items-center gap-2">
                        <div className="w-3 h-3 rounded-full bg-blue-500" />
                        <span className="text-gray-300">Pågående</span>
                    </div>
                    <div className="flex items-center gap-2">
                        <div className="w-3 h-3 rounded-full bg-purple-500" />
                        <span className="text-gray-300">Olåst</span>
                    </div>
                    <div className="flex items-center gap-2">
                        <div className="w-3 h-3 rounded-full bg-gray-600" />
                        <span className="text-gray-300">Låst</span>
                    </div>
                </div>
            </div>

            {/* Stats */}
            <div className="absolute bottom-4 right-4 bg-neutral-900/90 border border-neutral-700 rounded-lg p-3 backdrop-blur-sm">
                <div className="flex flex-col gap-1.5 text-xs">
                    <div className="flex items-center justify-between gap-4">
                        <span className="text-gray-400">Totalt:</span>
                        <span className="text-white font-semibold">{moduleNodes.length} moduler</span>
                    </div>
                    <div className="flex items-center justify-between gap-4">
                        <span className="text-gray-400">Klara:</span>
                        <span className="text-green-400 font-semibold">
                            {moduleNodes.filter(n => n.status === "completed").length}
                        </span>
                    </div>
                    <div className="flex items-center justify-between gap-4">
                        <span className="text-gray-400">Olåsta:</span>
                        <span className="text-purple-400 font-semibold">
                            {moduleNodes.filter(n => n.status === "unlocked").length}
                        </span>
                    </div>
                </div>
            </div>
        </div>
    )
}
