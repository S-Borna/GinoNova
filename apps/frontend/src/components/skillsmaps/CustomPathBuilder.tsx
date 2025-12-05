"use client"

/**
 * ============================================================================
 * CUSTOM PATH BUILDER — Create Your Own Learning Path
 * ============================================================================
 *
 * Premium wizard for creating custom learning paths:
 * - Browse and select modules from any SkillsMap
 * - Drag-and-drop reordering
 * - Save with custom name and description
 * - Track progress on custom paths
 *
 * @phase CUSTOM-PATHS
 */

import { useState, useEffect, useMemo } from "react"
import { motion, AnimatePresence, Reorder } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Plus,
    X,
    Check,
    Search,
    GripVertical,
    Sparkles,
    Save,
    ChevronRight,
    ChevronLeft,
    Trash2,
    Rocket,
    Clock,
    Zap,
    BookOpen,
    Layers,
    Star,
    Wand2,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { getSkillsMaps } from "@/lib/skillsmaps"

/* ============================================================================
   TYPES
   ============================================================================ */

interface ModuleOption {
    id: string
    slug: string
    title: string
    description: string
    icon: string
    color: string
    totalNodes: number
    totalXP: number
    estimatedHours: number
    skillsmapSlug: string
    skillsmapTitle: string
}

export interface CustomPath {
    id: string
    name: string
    description: string
    modules: ModuleOption[]
    createdAt: string
    totalNodes: number
    totalXP: number
    estimatedHours: number
}

interface CustomPathBuilderProps {
    isOpen: boolean
    onClose: () => void
    onSave: (path: CustomPath) => void
    existingPath?: CustomPath
}

/* ============================================================================
   LOCAL STORAGE
   ============================================================================ */

const CUSTOM_PATHS_KEY = "devopshub_custom_paths"

export function getCustomPaths(): CustomPath[] {
    if (typeof window === "undefined") return []
    const stored = localStorage.getItem(CUSTOM_PATHS_KEY)
    return stored ? JSON.parse(stored) : []
}

export function saveCustomPath(path: CustomPath): void {
    const paths = getCustomPaths()
    const existingIndex = paths.findIndex(p => p.id === path.id)
    if (existingIndex >= 0) {
        paths[existingIndex] = path
    } else {
        paths.push(path)
    }
    localStorage.setItem(CUSTOM_PATHS_KEY, JSON.stringify(paths))
}

export function deleteCustomPath(pathId: string): void {
    const paths = getCustomPaths().filter(p => p.id !== pathId)
    localStorage.setItem(CUSTOM_PATHS_KEY, JSON.stringify(paths))
}

/* ============================================================================
   STEP INDICATOR
   ============================================================================ */

function StepIndicator({ step, totalSteps }: { step: number; totalSteps: number }) {
    return (
        <div className="flex items-center gap-2 mb-6">
            {Array.from({ length: totalSteps }).map((_, i) => (
                <div key={i} className="flex items-center">
                    <motion.div
                        className={cn(
                            "w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold",
                            "transition-all duration-300",
                            i < step
                                ? "bg-emerald-500 text-white"
                                : i === step
                                    ? "bg-purple-500 text-white"
                                    : "bg-zinc-800 text-zinc-500"
                        )}
                        animate={i === step ? { scale: [1, 1.1, 1] } : {}}
                        transition={{ duration: 0.3 }}
                    >
                        {i < step ? <Check className="w-4 h-4" /> : i + 1}
                    </motion.div>
                    {i < totalSteps - 1 && (
                        <div className={cn(
                            "w-12 h-0.5 mx-1",
                            i < step ? "bg-emerald-500" : "bg-zinc-800"
                        )} />
                    )}
                </div>
            ))}
        </div>
    )
}

/* ============================================================================
   MODULE CARD (Selectable)
   ============================================================================ */

function SelectableModuleCard({
    module,
    isSelected,
    onToggle,
}: {
    module: ModuleOption
    isSelected: boolean
    onToggle: () => void
}) {
    return (
        <motion.button
            onClick={onToggle}
            className={cn(
                "relative w-full p-4 rounded-xl text-left",
                "transition-all duration-300",
                "border",
                isSelected
                    ? "bg-purple-500/20 border-purple-500/50"
                    : "bg-zinc-900/50 border-zinc-800 hover:border-zinc-700"
            )}
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
        >
            {/* Selection indicator */}
            <div className={cn(
                "absolute top-3 right-3 w-6 h-6 rounded-full",
                "flex items-center justify-center transition-all",
                isSelected
                    ? "bg-purple-500 text-white"
                    : "bg-zinc-800 border border-zinc-700"
            )}>
                {isSelected && <Check className="w-4 h-4" />}
            </div>

            <div className="flex items-start gap-3">
                <div
                    className="w-10 h-10 rounded-lg flex items-center justify-center text-xl"
                    style={{ backgroundColor: `${module.color}20` }}
                >
                    {module.icon}
                </div>
                <div className="flex-1 pr-8">
                    <h4 className="font-semibold text-white text-sm">{module.title}</h4>
                    <p className="text-xs text-zinc-500 line-clamp-1 mt-0.5">
                        {module.skillsmapTitle}
                    </p>
                    <div className="flex items-center gap-3 mt-2 text-xs text-zinc-500">
                        <span className="flex items-center gap-1">
                            <BookOpen className="w-3 h-3" />
                            {module.totalNodes} noder
                        </span>
                        <span className="flex items-center gap-1 text-amber-400">
                            <Zap className="w-3 h-3" />
                            {module.totalXP} XP
                        </span>
                    </div>
                </div>
            </div>
        </motion.button>
    )
}

/* ============================================================================
   REORDERABLE MODULE ITEM
   ============================================================================ */

function ReorderableModuleItem({
    module,
    index,
    onRemove,
}: {
    module: ModuleOption
    index: number
    onRemove: () => void
}) {
    return (
        <Reorder.Item
            value={module}
            className={cn(
                "relative flex items-center gap-3 p-4 rounded-xl",
                "bg-zinc-900/80 border border-zinc-800",
                "cursor-grab active:cursor-grabbing"
            )}
        >
            <div className="text-zinc-600 hover:text-zinc-400">
                <GripVertical className="w-5 h-5" />
            </div>

            <div className="flex items-center justify-center w-8 h-8 rounded-lg bg-zinc-800 text-sm font-bold text-zinc-400">
                {index + 1}
            </div>

            <div
                className="w-10 h-10 rounded-lg flex items-center justify-center text-xl"
                style={{ backgroundColor: `${module.color}20` }}
            >
                {module.icon}
            </div>

            <div className="flex-1">
                <h4 className="font-semibold text-white text-sm">{module.title}</h4>
                <div className="flex items-center gap-3 mt-1 text-xs text-zinc-500">
                    <span>{module.totalNodes} noder</span>
                    <span className="text-amber-400">{module.totalXP} XP</span>
                    <span>{module.estimatedHours}h</span>
                </div>
            </div>

            <button
                onClick={onRemove}
                className="p-2 rounded-lg text-zinc-500 hover:text-red-400 hover:bg-red-500/10 transition-colors"
            >
                <Trash2 className="w-4 h-4" />
            </button>
        </Reorder.Item>
    )
}

/* ============================================================================
   CUSTOM PATH BUILDER
   ============================================================================ */

export function CustomPathBuilder({
    isOpen,
    onClose,
    onSave,
    existingPath,
}: CustomPathBuilderProps) {
    const [step, setStep] = useState(0)
    const [availableModules, setAvailableModules] = useState<ModuleOption[]>([])
    const [selectedModules, setSelectedModules] = useState<ModuleOption[]>(
        existingPath?.modules || []
    )
    const [pathName, setPathName] = useState(existingPath?.name || "")
    const [pathDescription, setPathDescription] = useState(existingPath?.description || "")
    const [searchQuery, setSearchQuery] = useState("")
    const [loading, setLoading] = useState(true)

    // Load available modules from all SkillsMaps
    useEffect(() => {
        if (!isOpen) return

        async function loadModules() {
            setLoading(true)
            try {
                const result = await getSkillsMaps()
                if (result.ok) {
                    // Convert SkillsMaps to ModuleOptions
                    const modules: ModuleOption[] = result.data.map(sm => ({
                        id: sm.slug,
                        slug: sm.slug,
                        title: sm.title,
                        description: sm.description,
                        icon: sm.icon,
                        color: sm.color,
                        totalNodes: sm.totalNodes,
                        totalXP: sm.totalXP,
                        estimatedHours: sm.estimatedHours,
                        skillsmapSlug: sm.slug,
                        skillsmapTitle: sm.title,
                    }))
                    setAvailableModules(modules)
                }
            } catch (err) {
                console.error("Failed to load modules:", err)
            } finally {
                setLoading(false)
            }
        }

        loadModules()
    }, [isOpen])

    // Filter modules by search
    const filteredModules = useMemo(() => {
        if (!searchQuery) return availableModules
        const query = searchQuery.toLowerCase()
        return availableModules.filter(m =>
            m.title.toLowerCase().includes(query) ||
            m.description.toLowerCase().includes(query)
        )
    }, [availableModules, searchQuery])

    // Calculate totals
    const totals = useMemo(() => ({
        nodes: selectedModules.reduce((sum, m) => sum + m.totalNodes, 0),
        xp: selectedModules.reduce((sum, m) => sum + m.totalXP, 0),
        hours: selectedModules.reduce((sum, m) => sum + m.estimatedHours, 0),
    }), [selectedModules])

    const toggleModule = (module: ModuleOption) => {
        setSelectedModules(prev => {
            const exists = prev.find(m => m.id === module.id)
            if (exists) {
                return prev.filter(m => m.id !== module.id)
            }
            return [...prev, module]
        })
    }

    const removeModule = (moduleId: string) => {
        setSelectedModules(prev => prev.filter(m => m.id !== moduleId))
    }

    const handleSave = () => {
        const path: CustomPath = {
            id: existingPath?.id || `custom-${Date.now()}`,
            name: pathName,
            description: pathDescription,
            modules: selectedModules,
            createdAt: existingPath?.createdAt || new Date().toISOString(),
            totalNodes: totals.nodes,
            totalXP: totals.xp,
            estimatedHours: totals.hours,
        }
        saveCustomPath(path)
        onSave(path)
        onClose()
    }

    const canProceed = step === 0 ? selectedModules.length > 0 : pathName.trim().length > 0
    const totalSteps = 3

    if (!isOpen) return null

    return (
        <AnimatePresence>
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm"
                onClick={onClose}
            >
                <motion.div
                    initial={{ scale: 0.95, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    exit={{ scale: 0.95, opacity: 0 }}
                    onClick={(e) => e.stopPropagation()}
                    className={cn(
                        "relative w-full max-w-4xl max-h-[90vh] overflow-hidden",
                        "bg-zinc-950 rounded-3xl",
                        "border border-purple-500/20",
                        "shadow-2xl shadow-purple-500/10"
                    )}
                >
                    {/* Header */}
                    <div className="relative p-6 border-b border-zinc-800">
                        <div className="absolute top-0 right-0 w-64 h-64 bg-purple-500/10 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/2" />

                        <div className="relative flex items-center justify-between">
                            <div className="flex items-center gap-3">
                                <div className={cn(
                                    "p-2 rounded-xl",
                                    "bg-gradient-to-br from-purple-500/20 to-indigo-500/20",
                                    "border border-purple-500/30"
                                )}>
                                    <Wand2 className="w-5 h-5 text-purple-400" />
                                </div>
                                <div>
                                    <h2 className="text-xl font-bold text-white">
                                        {existingPath ? "Redigera SkillsMap" : "Skapa egen SkillsMap"}
                                    </h2>
                                    <p className="text-sm text-zinc-500">
                                        Bygg din personliga inlärningsresa
                                    </p>
                                </div>
                            </div>

                            <button
                                onClick={onClose}
                                className="p-2 rounded-xl text-zinc-500 hover:text-white hover:bg-zinc-800 transition-colors"
                            >
                                <X className="w-5 h-5" />
                            </button>
                        </div>

                        <div className="mt-6">
                            <StepIndicator step={step} totalSteps={totalSteps} />
                        </div>
                    </div>

                    {/* Content */}
                    <div className="p-6 overflow-y-auto max-h-[calc(90vh-200px)]">
                        <AnimatePresence mode="wait">
                            {/* Step 0: Select Modules */}
                            {step === 0 && (
                                <motion.div
                                    key="step-0"
                                    initial={{ opacity: 0, x: 20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    exit={{ opacity: 0, x: -20 }}
                                >
                                    <h3 className="text-lg font-semibold text-white mb-4">
                                        Välj moduler
                                    </h3>
                                    <p className="text-zinc-400 text-sm mb-6">
                                        Välj de moduler du vill inkludera i din SkillsMap. Du kan välja från alla tillgängliga kunskapsstigar.
                                    </p>

                                    {/* Search */}
                                    <div className="relative mb-6">
                                        <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-zinc-500" />
                                        <input
                                            type="text"
                                            placeholder="Sök moduler..."
                                            value={searchQuery}
                                            onChange={(e) => setSearchQuery(e.target.value)}
                                            className={cn(
                                                "w-full pl-12 pr-4 py-3 rounded-xl",
                                                "bg-zinc-900 border border-zinc-800",
                                                "text-white placeholder-zinc-500",
                                                "focus:outline-none focus:border-purple-500/50"
                                            )}
                                        />
                                    </div>

                                    {/* Selected count */}
                                    <div className="flex items-center justify-between mb-4">
                                        <span className="text-sm text-zinc-500">
                                            {filteredModules.length} tillgängliga moduler
                                        </span>
                                        <span className="text-sm font-medium text-purple-400">
                                            {selectedModules.length} valda
                                        </span>
                                    </div>

                                    {/* Module grid */}
                                    {loading ? (
                                        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                                            {Array.from({ length: 6 }).map((_, i) => (
                                                <div key={i} className="h-24 rounded-xl bg-zinc-800/50 animate-pulse" />
                                            ))}
                                        </div>
                                    ) : (
                                        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                                            {filteredModules.map((module) => (
                                                <SelectableModuleCard
                                                    key={module.id}
                                                    module={module}
                                                    isSelected={selectedModules.some(m => m.id === module.id)}
                                                    onToggle={() => toggleModule(module)}
                                                />
                                            ))}
                                        </div>
                                    )}
                                </motion.div>
                            )}

                            {/* Step 1: Arrange Order */}
                            {step === 1 && (
                                <motion.div
                                    key="step-1"
                                    initial={{ opacity: 0, x: 20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    exit={{ opacity: 0, x: -20 }}
                                >
                                    <h3 className="text-lg font-semibold text-white mb-4">
                                        Ordna modulerna
                                    </h3>
                                    <p className="text-zinc-400 text-sm mb-6">
                                        Dra och släpp för att arrangera modulerna i den ordning du vill lära dig dem.
                                    </p>

                                    <Reorder.Group
                                        axis="y"
                                        values={selectedModules}
                                        onReorder={setSelectedModules}
                                        className="space-y-3"
                                    >
                                        {selectedModules.map((module, index) => (
                                            <ReorderableModuleItem
                                                key={module.id}
                                                module={module}
                                                index={index}
                                                onRemove={() => removeModule(module.id)}
                                            />
                                        ))}
                                    </Reorder.Group>

                                    {selectedModules.length === 0 && (
                                        <div className="text-center py-12">
                                            <Layers className="w-12 h-12 text-zinc-600 mx-auto mb-3" />
                                            <p className="text-zinc-500">Inga moduler valda</p>
                                            <button
                                                onClick={() => setStep(0)}
                                                className="mt-3 text-purple-400 hover:text-purple-300 text-sm"
                                            >
                                                Gå tillbaka och välj moduler
                                            </button>
                                        </div>
                                    )}
                                </motion.div>
                            )}

                            {/* Step 2: Name and Save */}
                            {step === 2 && (
                                <motion.div
                                    key="step-2"
                                    initial={{ opacity: 0, x: 20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    exit={{ opacity: 0, x: -20 }}
                                >
                                    <h3 className="text-lg font-semibold text-white mb-4">
                                        Namnge din SkillsMap
                                    </h3>
                                    <p className="text-zinc-400 text-sm mb-6">
                                        Ge din SkillsMap ett unikt namn och beskrivning.
                                    </p>

                                    <div className="space-y-4">
                                        <div>
                                            <label className="block text-sm font-medium text-zinc-300 mb-2">
                                                Namn *
                                            </label>
                                            <input
                                                type="text"
                                                value={pathName}
                                                onChange={(e) => setPathName(e.target.value)}
                                                placeholder="T.ex. 'Min DevOps SkillsMap'"
                                                className={cn(
                                                    "w-full px-4 py-3 rounded-xl",
                                                    "bg-zinc-900 border border-zinc-800",
                                                    "text-white placeholder-zinc-500",
                                                    "focus:outline-none focus:border-purple-500/50"
                                                )}
                                            />
                                        </div>

                                        <div>
                                            <label className="block text-sm font-medium text-zinc-300 mb-2">
                                                Beskrivning (valfritt)
                                            </label>
                                            <textarea
                                                value={pathDescription}
                                                onChange={(e) => setPathDescription(e.target.value)}
                                                placeholder="Beskriv din SkillsMap..."
                                                rows={3}
                                                className={cn(
                                                    "w-full px-4 py-3 rounded-xl",
                                                    "bg-zinc-900 border border-zinc-800",
                                                    "text-white placeholder-zinc-500",
                                                    "focus:outline-none focus:border-purple-500/50",
                                                    "resize-none"
                                                )}
                                            />
                                        </div>

                                        {/* Summary */}
                                        <div className={cn(
                                            "p-4 rounded-xl",
                                            "bg-gradient-to-br from-purple-500/10 to-indigo-500/10",
                                            "border border-purple-500/20"
                                        )}>
                                            <h4 className="font-semibold text-white mb-3 flex items-center gap-2">
                                                <Sparkles className="w-4 h-4 text-purple-400" />
                                                Sammanfattning
                                            </h4>
                                            <div className="grid grid-cols-3 gap-4 text-center">
                                                <div>
                                                    <div className="text-2xl font-bold text-white">
                                                        {selectedModules.length}
                                                    </div>
                                                    <div className="text-xs text-zinc-500">Moduler</div>
                                                </div>
                                                <div>
                                                    <div className="text-2xl font-bold text-amber-400">
                                                        {totals.xp.toLocaleString()}
                                                    </div>
                                                    <div className="text-xs text-zinc-500">Total XP</div>
                                                </div>
                                                <div>
                                                    <div className="text-2xl font-bold text-white">
                                                        ~{totals.hours}h
                                                    </div>
                                                    <div className="text-xs text-zinc-500">Uppskattad tid</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </motion.div>
                            )}
                        </AnimatePresence>
                    </div>

                    {/* Footer */}
                    <div className="p-6 border-t border-zinc-800 flex items-center justify-between">
                        <Button
                            variant="outline"
                            onClick={() => step > 0 ? setStep(step - 1) : onClose()}
                            className="rounded-xl"
                        >
                            <ChevronLeft className="w-4 h-4 mr-2" />
                            {step > 0 ? "Tillbaka" : "Avbryt"}
                        </Button>

                        <div className="flex items-center gap-3">
                            {step < totalSteps - 1 ? (
                                <Button
                                    onClick={() => setStep(step + 1)}
                                    disabled={!canProceed}
                                    className={cn(
                                        "rounded-xl",
                                        "bg-gradient-to-r from-purple-600 to-indigo-600",
                                        "hover:from-purple-500 hover:to-indigo-500",
                                        "disabled:opacity-50 disabled:cursor-not-allowed"
                                    )}
                                >
                                    Nästa
                                    <ChevronRight className="w-4 h-4 ml-2" />
                                </Button>
                            ) : (
                                <Button
                                    onClick={handleSave}
                                    disabled={!canProceed}
                                    className={cn(
                                        "rounded-xl",
                                        "bg-gradient-to-r from-emerald-600 to-teal-600",
                                        "hover:from-emerald-500 hover:to-teal-500",
                                        "disabled:opacity-50 disabled:cursor-not-allowed"
                                    )}
                                >
                                    <Save className="w-4 h-4 mr-2" />
                                    Spara SkillsMap
                                </Button>
                            )}
                        </div>
                    </div>
                </motion.div>
            </motion.div>
        </AnimatePresence>
    )
}

export default CustomPathBuilder
