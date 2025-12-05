"use client"

/**
 * ============================================================================
 * CUSTOM PATHS SECTION — Display User's Custom Learning Paths
 * ============================================================================
 *
 * Shows custom paths created by the user with:
 * - Progress tracking
 * - Edit/Delete actions
 * - Beautiful glassmorphism cards
 *
 * @phase CUSTOM-PATHS
 */

import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { useRouter } from "next/navigation"
import { cn } from "@/lib/utils"
import {
    Rocket,
    Star,
    Clock,
    Zap,
    MoreVertical,
    Pencil,
    Trash2,
    ChevronRight,
    Sparkles,
    BookOpen,
} from "lucide-react"
import { CustomPath, deleteCustomPath } from "./CustomPathBuilder"

/* ============================================================================
   CUSTOM PATH CARD
   ============================================================================ */

function CustomPathCard({
    path,
    onEdit,
    onDelete,
}: {
    path: CustomPath
    onEdit: () => void
    onDelete: () => void
}) {
    const router = useRouter()
    const [showMenu, setShowMenu] = useState(false)

    // Calculate progress (mock for now - would come from localStorage)
    const progress = 0 // TODO: Track progress per custom path

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "group relative overflow-hidden rounded-2xl",
                "bg-gradient-to-br from-zinc-900 via-zinc-900/95 to-zinc-950",
                "border border-amber-500/20",
                "transition-all duration-300",
                "hover:border-amber-500/40 hover:shadow-[0_0_30px_rgba(245,158,11,0.1)]"
            )}
        >
            {/* Glow effect */}
            <div className="absolute top-0 right-0 w-32 h-32 bg-amber-500/10 rounded-full blur-[60px] -translate-y-1/2 translate-x-1/2" />

            {/* Custom badge */}
            <div className="absolute top-4 left-4 flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-amber-500/20 border border-amber-500/30">
                <Star className="w-3 h-3 text-amber-400 fill-current" />
                <span className="text-xs font-medium text-amber-300">Egen SkillsMap</span>
            </div>

            {/* Menu button */}
            <div className="absolute top-4 right-4">
                <button
                    onClick={(e) => {
                        e.stopPropagation()
                        setShowMenu(!showMenu)
                    }}
                    className="p-2 rounded-lg text-zinc-500 hover:text-white hover:bg-zinc-800 transition-colors"
                >
                    <MoreVertical className="w-4 h-4" />
                </button>

                <AnimatePresence>
                    {showMenu && (
                        <motion.div
                            initial={{ opacity: 0, scale: 0.95 }}
                            animate={{ opacity: 1, scale: 1 }}
                            exit={{ opacity: 0, scale: 0.95 }}
                            className={cn(
                                "absolute top-10 right-0 z-10 min-w-[140px]",
                                "bg-zinc-900 border border-zinc-800 rounded-xl",
                                "shadow-xl overflow-hidden"
                            )}
                            onClick={(e) => e.stopPropagation()}
                        >
                            <button
                                onClick={() => {
                                    setShowMenu(false)
                                    onEdit()
                                }}
                                className="flex items-center gap-2 w-full px-4 py-2.5 text-sm text-zinc-300 hover:bg-zinc-800 transition-colors"
                            >
                                <Pencil className="w-4 h-4" />
                                Redigera
                            </button>
                            <button
                                onClick={() => {
                                    setShowMenu(false)
                                    onDelete()
                                }}
                                className="flex items-center gap-2 w-full px-4 py-2.5 text-sm text-red-400 hover:bg-red-500/10 transition-colors"
                            >
                                <Trash2 className="w-4 h-4" />
                                Ta bort
                            </button>
                        </motion.div>
                    )}
                </AnimatePresence>
            </div>

            {/* Content */}
            <div className="p-6 pt-14">
                <h3 className="text-xl font-bold text-white mb-2">{path.name}</h3>
                {path.description && (
                    <p className="text-sm text-zinc-400 line-clamp-2 mb-4">
                        {path.description}
                    </p>
                )}

                {/* Modules preview */}
                <div className="flex items-center gap-1.5 mb-4">
                    {path.modules.slice(0, 5).map((module, i) => (
                        <div
                            key={module.id}
                            className="w-8 h-8 rounded-lg flex items-center justify-center text-sm"
                            style={{ backgroundColor: `${module.color}20` }}
                            title={module.title}
                        >
                            {module.icon}
                        </div>
                    ))}
                    {path.modules.length > 5 && (
                        <div className="w-8 h-8 rounded-lg bg-zinc-800 flex items-center justify-center text-xs text-zinc-400">
                            +{path.modules.length - 5}
                        </div>
                    )}
                </div>

                {/* Stats */}
                <div className="flex items-center gap-4 text-sm text-zinc-400 mb-4">
                    <span className="flex items-center gap-1.5">
                        <BookOpen className="w-4 h-4" />
                        {path.modules.length} moduler
                    </span>
                    <span className="flex items-center gap-1.5 text-amber-400">
                        <Zap className="w-4 h-4" />
                        {path.totalXP.toLocaleString()} XP
                    </span>
                    <span className="flex items-center gap-1.5">
                        <Clock className="w-4 h-4" />
                        ~{path.estimatedHours}h
                    </span>
                </div>

                {/* Progress */}
                <div className="mb-4">
                    <div className="flex items-center justify-between text-sm mb-2">
                        <span className="text-zinc-500">Progress</span>
                        <span className="font-bold text-amber-400">{progress}%</span>
                    </div>
                    <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
                        <motion.div
                            className="h-full bg-gradient-to-r from-amber-500 to-orange-500"
                            initial={{ width: 0 }}
                            animate={{ width: `${progress}%` }}
                            transition={{ duration: 0.5 }}
                        />
                    </div>
                </div>

                {/* Action */}
                <button
                    onClick={() => router.push(`/skillsmaps/custom/${path.id}`)}
                    className={cn(
                        "w-full flex items-center justify-center gap-2",
                        "px-4 py-3 rounded-xl",
                        "bg-gradient-to-r from-amber-600 to-orange-600",
                        "hover:from-amber-500 hover:to-orange-500",
                        "text-white font-medium text-sm",
                        "transition-all duration-300"
                    )}
                >
                    <Rocket className="w-4 h-4" />
                    Öppna SkillsMap
                    <ChevronRight className="w-4 h-4" />
                </button>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   CUSTOM PATHS SECTION
   ============================================================================ */

export function CustomPathsSection({
    paths,
    onEdit,
    onRefresh,
}: {
    paths: CustomPath[]
    onEdit: (path: CustomPath) => void
    onRefresh: () => void
}) {
    const handleDelete = (pathId: string) => {
        if (confirm("Är du säker på att du vill ta bort denna lärstig?")) {
            deleteCustomPath(pathId)
            onRefresh()
        }
    }

    if (paths.length === 0) return null

    return (
        <div className="mb-8">
            <div className="flex items-center gap-3 mb-6">
                <div className={cn(
                    "p-2 rounded-xl",
                    "bg-gradient-to-br from-amber-500/20 to-orange-500/20",
                    "border border-amber-500/30"
                )}>
                    <Star className="w-5 h-5 text-amber-400" />
                </div>
                <div>
                    <h2 className="text-xl font-bold text-white">Mina SkillsMaps</h2>
                    <p className="text-sm text-zinc-500">{paths.length} egen{paths.length > 1 ? "a" : ""} SkillsMap{paths.length > 1 ? "s" : ""}</p>
                </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {paths.map((path) => (
                    <CustomPathCard
                        key={path.id}
                        path={path}
                        onEdit={() => onEdit(path)}
                        onDelete={() => handleDelete(path.id)}
                    />
                ))}
            </div>
        </div>
    )
}

export default CustomPathsSection
