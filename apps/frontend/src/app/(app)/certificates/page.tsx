"use client"

/**
 * ============================================================================
 * CERTIFICATES SHOWCASE PAGE
 * ============================================================================
 *
 * Gallery of all earned certificates with:
 * - Grid layout with hover effects
 * - Filters by module, date, category
 * - Share and download buttons
 * - Total certificates count
 * - Progress tracking
 *
 * @phase GAMIFICATION
 */

import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth"
import { PageLayout } from "@saas/ui"
import {
    Certificate,
    getMockCertificates,
} from "@/lib/certificates"
import {
    CertificateCard,
    CertificateGenerator,
} from "@/components/certificates/CertificateGenerator"
import { Button } from "@/components/ui/button"
import {
    Award,
    Filter,
    Download,
    Calendar,
    Trophy,
    TrendingUp,
    X,
    Sparkles,
} from "lucide-react"

/* ============================================================================
   FILTERS
   ============================================================================ */

type FilterType = "all" | "recent" | "oldest"

/* ============================================================================
   CERTIFICATES PAGE
   ============================================================================ */

export default function CertificatesPage() {
    const { user } = useAuth()
    // Use empty array instead of mock data - real certificates come from API
    const [certificates] = useState<Certificate[]>([])
    const [filter, setFilter] = useState<FilterType>("all")
    const [selectedCertificate, setSelectedCertificate] = useState<Certificate | null>(null)

    // Sort certificates based on filter
    const sortedCertificates = [...certificates].sort((a, b) => {
        if (filter === "recent") {
            return b.issuedDate.getTime() - a.issuedDate.getTime()
        } else if (filter === "oldest") {
            return a.issuedDate.getTime() - b.issuedDate.getTime()
        }
        return 0
    })

    const userName = user?.full_name || "DevOps Learner"

    return (
        <PageLayout maxWidth="wide" background="cosmic">
            {/* Cosmic Aurora Background */}
            <div className="fixed inset-0 pointer-events-none overflow-hidden">
                <div className="absolute inset-0 bg-[#05050a]" />
                <motion.div
                    className="absolute -top-40 -right-40 w-[800px] h-[800px] rounded-full"
                    style={{
                        background:
                            "radial-gradient(circle, rgba(139, 92, 246, 0.15) 0%, rgba(139, 92, 246, 0.05) 40%, transparent 70%)",
                    }}
                    animate={{
                        scale: [1, 1.1, 1],
                        opacity: [0.6, 0.8, 0.6],
                    }}
                    transition={{
                        duration: 8,
                        repeat: Infinity,
                        ease: "easeInOut",
                    }}
                />
            </div>

            <div className="relative z-10 space-y-8">
                {/* Certificate Detail Modal */}
                <AnimatePresence>
                    {selectedCertificate && (
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm"
                            onClick={() => setSelectedCertificate(null)}
                        >
                            <motion.div
                                initial={{ scale: 0.9, y: 20 }}
                                animate={{ scale: 1, y: 0 }}
                                exit={{ scale: 0.9, y: 20 }}
                                onClick={(e) => e.stopPropagation()}
                                className="relative w-full max-w-6xl max-h-[90vh] overflow-y-auto rounded-3xl bg-[#0a0a0f] p-6"
                            >
                                <Button
                                    onClick={() => setSelectedCertificate(null)}
                                    variant="ghost"
                                    className="absolute top-4 right-4 z-10 rounded-full"
                                >
                                    <X className="w-5 h-5" />
                                </Button>
                                <CertificateGenerator
                                    certificate={selectedCertificate}
                                    userName={userName}
                                />
                            </motion.div>
                        </motion.div>
                    )}
                </AnimatePresence>

                {/* Hero Section */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
                    className={cn(
                        "relative overflow-hidden rounded-3xl",
                        "bg-gradient-to-br from-[#0a0a0f] via-purple-950/20 to-[#0a0a0f]",
                        "border border-purple-500/20",
                        "p-8 md:p-10",
                        "shadow-[0_0_80px_rgba(139,92,246,0.15)]"
                    )}
                >
                    {/* Cosmic glow effects */}
                    <div className="absolute top-0 right-0 w-[600px] h-[600px] bg-purple-500/10 rounded-full blur-[120px] -translate-y-1/2 translate-x-1/4" />

                    <div className="relative flex flex-col md:flex-row md:items-center md:justify-between gap-6">
                        <div>
                            <motion.div
                                initial={{ opacity: 0, x: -20 }}
                                animate={{ opacity: 1, x: 0 }}
                                transition={{ delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
                                className="flex items-center gap-3 mb-3"
                            >
                                <motion.div
                                    className={cn(
                                        "relative p-2.5 rounded-xl",
                                        "bg-gradient-to-br from-amber-500/30 to-orange-600/20",
                                        "border border-amber-500/40"
                                    )}
                                    animate={{
                                        boxShadow: [
                                            "0 0 20px rgba(245, 158, 11, 0.3)",
                                            "0 0 40px rgba(245, 158, 11, 0.5)",
                                            "0 0 20px rgba(245, 158, 11, 0.3)",
                                        ],
                                    }}
                                    transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                                >
                                    <Award className="w-5 h-5 text-amber-400" />
                                </motion.div>
                                <span className="text-amber-400 font-semibold text-sm uppercase tracking-wider">
                                    My Certificates
                                </span>
                            </motion.div>

                            <motion.h1
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.3, ease: [0.16, 1, 0.3, 1] }}
                                className={cn(
                                    "text-3xl md:text-4xl lg:text-5xl font-black mb-3",
                                    "bg-gradient-to-r from-white via-amber-200 to-orange-200 bg-clip-text text-transparent"
                                )}
                            >
                                Your Achievements
                            </motion.h1>

                            <motion.p
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                                transition={{ delay: 0.4, ease: [0.16, 1, 0.3, 1] }}
                                className="text-zinc-400 text-lg max-w-xl"
                            >
                                All your earned certificates in one place. Share them with the world!
                            </motion.p>
                        </div>

                        {/* Stats */}
                        <motion.div
                            initial={{ opacity: 0, scale: 0.9 }}
                            animate={{ opacity: 1, scale: 1 }}
                            transition={{ delay: 0.5, ease: [0.16, 1, 0.3, 1] }}
                            className="flex gap-4"
                        >
                            <motion.div
                                className={cn(
                                    "flex items-center gap-3 px-6 py-4 rounded-2xl",
                                    "bg-gradient-to-br from-amber-600/25 to-orange-500/10",
                                    "border border-amber-500/40",
                                    "backdrop-blur-sm"
                                )}
                                whileHover={{ scale: 1.02 }}
                                animate={{
                                    boxShadow: [
                                        "0 0 30px rgba(245, 158, 11, 0.2)",
                                        "0 0 50px rgba(245, 158, 11, 0.35)",
                                        "0 0 30px rgba(245, 158, 11, 0.2)",
                                    ],
                                }}
                                transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
                            >
                                <motion.div
                                    className={cn(
                                        "w-12 h-12 rounded-xl",
                                        "bg-gradient-to-br from-amber-500 to-orange-600",
                                        "flex items-center justify-center"
                                    )}
                                    animate={{
                                        boxShadow: [
                                            "0 0 15px rgba(245, 158, 11, 0.5)",
                                            "0 0 30px rgba(245, 158, 11, 0.8)",
                                            "0 0 15px rgba(245, 158, 11, 0.5)",
                                        ],
                                    }}
                                    transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                                >
                                    <Trophy className="w-6 h-6 text-white" />
                                </motion.div>
                                <div>
                                    <p className="text-zinc-500 text-xs uppercase tracking-wider">
                                        Total Certificates
                                    </p>
                                    <p className="text-2xl font-bold text-amber-400">
                                        {certificates.length}
                                    </p>
                                </div>
                            </motion.div>
                        </motion.div>
                    </div>
                </motion.div>

                {/* Filters & Actions */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.6 }}
                    className="flex flex-wrap items-center justify-between gap-4"
                >
                    <div className="flex items-center gap-2">
                        <Filter className="w-4 h-4 text-zinc-500" />
                        <span className="text-sm text-zinc-500">Filter by:</span>
                        <div className="flex gap-2">
                            <Button
                                onClick={() => setFilter("all")}
                                variant={filter === "all" ? "default" : "ghost"}
                                size="sm"
                                className={cn(
                                    "rounded-xl",
                                    filter === "all" &&
                                    "bg-purple-600 hover:bg-purple-700"
                                )}
                            >
                                All
                            </Button>
                            <Button
                                onClick={() => setFilter("recent")}
                                variant={filter === "recent" ? "default" : "ghost"}
                                size="sm"
                                className={cn(
                                    "rounded-xl",
                                    filter === "recent" &&
                                    "bg-purple-600 hover:bg-purple-700"
                                )}
                            >
                                <Calendar className="w-3 h-3 mr-1" />
                                Recent
                            </Button>
                            <Button
                                onClick={() => setFilter("oldest")}
                                variant={filter === "oldest" ? "default" : "ghost"}
                                size="sm"
                                className={cn(
                                    "rounded-xl",
                                    filter === "oldest" &&
                                    "bg-purple-600 hover:bg-purple-700"
                                )}
                            >
                                <TrendingUp className="w-3 h-3 mr-1" />
                                Oldest
                            </Button>
                        </div>
                    </div>

                    <Button
                        variant="outline"
                        className={cn(
                            "rounded-xl border-purple-500/40",
                            "hover:bg-purple-500/10"
                        )}
                        onClick={() => {
                            alert(
                                "Download All as ZIP would be implemented with JSZip library. Install with: npm install jszip"
                            )
                        }}
                    >
                        <Download className="w-4 h-4 mr-2" />
                        Download All as ZIP
                    </Button>
                </motion.div>

                {/* Certificates Grid */}
                {sortedCertificates.length === 0 ? (
                    <motion.div
                        initial={{ opacity: 0, scale: 0.95 }}
                        animate={{ opacity: 1, scale: 1 }}
                        className={cn(
                            "text-center p-12 rounded-2xl",
                            "bg-gradient-to-br from-zinc-900/50 to-zinc-800/30",
                            "border border-zinc-800"
                        )}
                    >
                        <div className="w-20 h-20 mx-auto mb-6 rounded-2xl bg-gradient-to-br from-purple-500/20 to-purple-600/10 flex items-center justify-center">
                            <Award className="w-10 h-10 text-purple-400" />
                        </div>
                        <h3 className="text-xl font-semibold text-white mb-2">
                            No Certificates Yet
                        </h3>
                        <p className="text-zinc-400 mb-6">
                            Complete modules to earn your first certificate!
                        </p>
                        <Button
                            onClick={() => (window.location.href = "/modules")}
                            className={cn(
                                "rounded-xl bg-gradient-to-r from-purple-600 to-purple-700",
                                "hover:from-purple-700 hover:to-purple-800"
                            )}
                        >
                            <Sparkles className="w-4 h-4 mr-2" />
                            Start Learning
                        </Button>
                    </motion.div>
                ) : (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ delay: 0.7 }}
                        className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
                    >
                        {sortedCertificates.map((certificate, index) => (
                            <motion.div
                                key={certificate.id}
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.1 * index }}
                            >
                                <CertificateCard
                                    certificate={certificate}
                                    onClick={() => setSelectedCertificate(certificate)}
                                />
                            </motion.div>
                        ))}
                    </motion.div>
                )}

                {/* Progress to Next Certificate */}
                {sortedCertificates.length > 0 && (
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.9 }}
                        className={cn(
                            "relative p-6 rounded-2xl",
                            "bg-gradient-to-br from-purple-600/20 to-cyan-600/10",
                            "border border-purple-500/30",
                            "backdrop-blur-sm"
                        )}
                    >
                        <div className="flex items-center gap-4">
                            <motion.div
                                className={cn(
                                    "w-14 h-14 rounded-xl shrink-0",
                                    "bg-gradient-to-br from-purple-500 to-cyan-500",
                                    "flex items-center justify-center"
                                )}
                                animate={{
                                    boxShadow: [
                                        "0 0 20px rgba(139, 92, 246, 0.4)",
                                        "0 0 40px rgba(139, 92, 246, 0.6)",
                                        "0 0 20px rgba(139, 92, 246, 0.4)",
                                    ],
                                }}
                                transition={{ duration: 2, repeat: Infinity }}
                            >
                                <Sparkles className="w-7 h-7 text-white" />
                            </motion.div>
                            <div className="flex-1">
                                <h3 className="text-lg font-semibold text-white mb-1">
                                    Keep Learning!
                                </h3>
                                <p className="text-zinc-400 text-sm">
                                    Complete more modules to earn additional certificates and showcase your
                                    expertise.
                                </p>
                            </div>
                            <Button
                                onClick={() => (window.location.href = "/modules")}
                                className={cn(
                                    "rounded-xl bg-gradient-to-r from-purple-600 to-cyan-600",
                                    "hover:from-purple-700 hover:to-cyan-700"
                                )}
                            >
                                Browse Modules
                            </Button>
                        </div>
                    </motion.div>
                )}
            </div>
        </PageLayout>
    )
}
