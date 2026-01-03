"use client"

/**
 * ============================================================================
 * DOE25 TENTA MODULE PAGE — Exam Mode Enabled
 * ============================================================================
 *
 * Special page for DOE25 Tenta with Exam Mode Dashboard
 *
 * @phase EXAM-MODE-IMPLEMENTATION
 */

import { useState, useEffect } from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { CosmicAurora } from "@/components/ui/cosmic-aurora"
import { SharedModulePage } from "@/components/modules/SharedModulePage"
import { ExamModeDashboard } from "@/components/exam-mode/ExamModeDashboard"
import { useExamMode } from "@/contexts/ExamModeContext"
import { DOE25_MODULE } from "@/data/doe25-module"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { BookOpen, Target, Calendar } from "lucide-react"

export default function DOE25TentaPage() {
    const { state, activateExamMode } = useExamMode()
    const [activeTab, setActiveTab] = useState<"overview" | "exam-mode">("overview")

    // Activate exam mode on mount if not already active
    useEffect(() => {
        if (!state.isActive) {
            const examDate = new Date(DOE25_MODULE.exam_date)
            activateExamMode(examDate)
        }
    }, [state.isActive, activateExamMode])

    return (
        <div className="min-h-screen bg-[#05050a] relative">
            <CosmicAurora />

            <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {/* Tabs */}
                <Tabs value={activeTab} onValueChange={(v) => setActiveTab(v as any)} className="mb-8">
                    <TabsList className="grid w-full max-w-md grid-cols-2 bg-zinc-900/50 border border-zinc-700/50">
                        <TabsTrigger value="overview" className="flex items-center gap-2">
                            <BookOpen className="w-4 h-4" />
                            Översikt
                        </TabsTrigger>
                        <TabsTrigger value="exam-mode" className="flex items-center gap-2">
                            <Target className="w-4 h-4" />
                            Exam Mode
                        </TabsTrigger>
                    </TabsList>

                    <TabsContent value="overview" className="mt-6">
                        <SharedModulePage
                            slug="doe25-tenta"
                            backHref="/modules"
                            backLabel="Tillbaka till Camp DevOps"
                        />
                    </TabsContent>

                    <TabsContent value="exam-mode" className="mt-6">
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                        >
                            <div className="mb-6">
                                <h1 className="text-3xl font-bold text-white mb-2">
                                    Exam Mode Dashboard
                                </h1>
                                <p className="text-zinc-400">
                                    Spåra din progress, confidence scores och studieplan för DOE25 tentan
                                </p>
                            </div>
                            <ExamModeDashboard />
                        </motion.div>
                    </TabsContent>
                </Tabs>
            </div>
        </div>
    )
}
