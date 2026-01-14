"use client"

/**
 * ============================================================================
 * CERTIFICATE GENERATOR — COSMIC EDITION
 * ============================================================================
 *
 * Beautiful, shareable certificates with:
 * - Cosmic purple/cyan gradient design
 * - Professional layout
 * - Downloadable as PNG/PDF
 * - QR code verification
 * - LinkedIn/Twitter sharing
 *
 * @phase GAMIFICATION
 */

import { useRef } from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
    Certificate,
    formatCertificateDate,
    getLinkedInShareUrl,
    getTwitterShareUrl,
} from "@/lib/certificates"
import {
    Download,
    Share2,
    Check,
    Award,
    Sparkles,
} from "lucide-react"

/* ============================================================================
   CERTIFICATE GENERATOR PROPS
   ============================================================================ */

interface CertificateGeneratorProps {
    certificate: Certificate
    userName: string
    onDownloadPNG?: () => void
    onDownloadPDF?: () => void
    className?: string
}

/* ============================================================================
   CERTIFICATE DESIGN
   ============================================================================ */

export function CertificateGenerator({
    certificate,
    userName,
    onDownloadPNG,
    onDownloadPDF,
    className,
}: CertificateGeneratorProps) {
    const certificateRef = useRef<HTMLDivElement>(null)

    const handleDownloadPNG = () => {
        if (onDownloadPNG) {
            onDownloadPNG()
        } else {
            // Placeholder: In production, use html2canvas
            alert("PNG download would use html2canvas library. Install with: npm install html2canvas")
        }
    }

    const handleDownloadPDF = () => {
        if (onDownloadPDF) {
            onDownloadPDF()
        } else {
            // Placeholder: In production, use jspdf
            alert("PDF download would use jspdf library. Install with: npm install jspdf html2canvas")
        }
    }

    const handleShareLinkedIn = () => {
        const url = getLinkedInShareUrl(certificate)
        window.open(url, "_blank", "width=600,height=600")
    }

    const handleShareTwitter = () => {
        const url = getTwitterShareUrl(certificate)
        window.open(url, "_blank", "width=600,height=600")
    }

    return (
        <div className={cn("space-y-6", className)}>
            {/* Certificate Preview */}
            <motion.div
                ref={certificateRef}
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
                className={cn(
                    "relative w-full aspect-[1.414/1] max-w-4xl mx-auto",
                    "bg-gradient-to-br from-[#0a0a0f] via-purple-950/30 to-[#0a0a0f]",
                    "border-4 border-purple-500/40",
                    "rounded-3xl overflow-hidden",
                    "shadow-[0_0_100px_rgba(139,92,246,0.3)]"
                )}
            >
                {/* Cosmic background effects */}
                <div className="absolute inset-0 pointer-events-none">
                    {/* Aurora orbs */}
                    <motion.div
                        className="absolute top-0 right-0 w-[600px] h-[600px] rounded-full"
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
                    <motion.div
                        className="absolute bottom-0 left-0 w-[500px] h-[500px] rounded-full"
                        style={{
                            background:
                                "radial-gradient(circle, rgba(34, 211, 238, 0.12) 0%, rgba(34, 211, 238, 0.04) 40%, transparent 70%)",
                        }}
                        animate={{
                            scale: [1, 1.15, 1],
                            opacity: [0.5, 0.7, 0.5],
                        }}
                        transition={{
                            duration: 10,
                            repeat: Infinity,
                            ease: "easeInOut",
                            delay: 2,
                        }}
                    />

                    {/* Grid pattern */}
                    <div
                        className="absolute inset-0 opacity-[0.03]"
                        style={{
                            backgroundImage: `
                                linear-gradient(rgba(139, 92, 246, 0.3) 1px, transparent 1px),
                                linear-gradient(90deg, rgba(139, 92, 246, 0.3) 1px, transparent 1px)
                            `,
                            backgroundSize: "60px 60px",
                        }}
                    />

                    {/* Decorative corner accents */}
                    <div className="absolute top-8 left-8 w-24 h-24 border-l-2 border-t-2 border-purple-500/30 rounded-tl-2xl" />
                    <div className="absolute top-8 right-8 w-24 h-24 border-r-2 border-t-2 border-cyan-500/30 rounded-tr-2xl" />
                    <div className="absolute bottom-8 left-8 w-24 h-24 border-l-2 border-b-2 border-cyan-500/30 rounded-bl-2xl" />
                    <div className="absolute bottom-8 right-8 w-24 h-24 border-r-2 border-b-2 border-purple-500/30 rounded-br-2xl" />
                </div>

                {/* Certificate Content */}
                <div className="relative h-full flex flex-col items-center justify-between p-12 md:p-16">
                    {/* Header */}
                    <div className="text-center space-y-4">
                        {/* Logo/Brand */}
                        <motion.div
                            initial={{ opacity: 0, y: -20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.2 }}
                            className="flex items-center justify-center gap-3"
                        >
                            <motion.div
                                className={cn(
                                    "w-16 h-16 rounded-2xl",
                                    "bg-gradient-to-br from-purple-500 to-cyan-500",
                                    "flex items-center justify-center"
                                )}
                                animate={{
                                    boxShadow: [
                                        "0 0 20px rgba(139, 92, 246, 0.5)",
                                        "0 0 40px rgba(139, 92, 246, 0.8)",
                                        "0 0 20px rgba(139, 92, 246, 0.5)",
                                    ],
                                }}
                                transition={{ duration: 3, repeat: Infinity }}
                            >
                                <Award className="w-8 h-8 text-white" />
                            </motion.div>
                            <div className="text-left">
                                <h1
                                    className={cn(
                                        "text-3xl md:text-4xl font-black",
                                        "bg-gradient-to-r from-purple-400 via-cyan-400 to-purple-400 bg-clip-text text-transparent"
                                    )}
                                >
                                    DevOpsHub
                                </h1>
                                <p className="text-zinc-500 text-sm uppercase tracking-wider">
                                    Certificate of Completion
                                </p>
                            </div>
                        </motion.div>
                    </div>

                    {/* Main Content */}
                    <motion.div
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ delay: 0.4 }}
                        className="text-center space-y-6"
                    >
                        {/* Achievement Badge */}
                        <motion.div
                            className="flex justify-center"
                            animate={{
                                rotate: [0, 5, -5, 0],
                            }}
                            transition={{
                                duration: 4,
                                repeat: Infinity,
                                ease: "easeInOut",
                            }}
                        >
                            <div
                                className={cn(
                                    "relative w-24 h-24 rounded-full",
                                    "bg-gradient-to-br from-amber-500 to-orange-600",
                                    "flex items-center justify-center",
                                    "border-4 border-amber-400/30"
                                )}
                                style={{
                                    boxShadow: "0 0 60px rgba(245, 158, 11, 0.5)",
                                }}
                            >
                                <Check className="w-12 h-12 text-white" strokeWidth={3} />
                                {/* Sparkle effects */}
                                <motion.div
                                    className="absolute -top-2 -right-2 text-amber-400"
                                    animate={{
                                        scale: [1, 1.3, 1],
                                        rotate: [0, 180, 360],
                                        opacity: [0.6, 1, 0.6],
                                    }}
                                    transition={{ duration: 2, repeat: Infinity }}
                                >
                                    <Sparkles className="w-6 h-6" />
                                </motion.div>
                            </div>
                        </motion.div>

                        <div className="space-y-3">
                            <p className="text-zinc-400 text-sm uppercase tracking-wider">
                                This certifies that
                            </p>
                            <h2
                                className={cn(
                                    "text-4xl md:text-5xl lg:text-6xl font-black",
                                    "bg-gradient-to-r from-white via-purple-200 to-cyan-200 bg-clip-text text-transparent"
                                )}
                            >
                                {userName}
                            </h2>
                            <p className="text-zinc-400 text-sm">
                                has successfully completed
                            </p>
                            <h3 className="text-2xl md:text-3xl font-bold text-purple-400">
                                {certificate.moduleName}
                            </h3>
                        </div>

                        {/* Skills */}
                        {certificate.skills && certificate.skills.length > 0 && (
                            <div className="flex flex-wrap justify-center gap-2 max-w-2xl mx-auto">
                                {certificate.skills.slice(0, 6).map((skill) => (
                                    <span
                                        key={skill}
                                        className={cn(
                                            "px-4 py-1.5 rounded-full text-xs font-medium",
                                            "bg-purple-500/20 text-purple-300",
                                            "border border-purple-500/30"
                                        )}
                                    >
                                        {skill}
                                    </span>
                                ))}
                            </div>
                        )}
                    </motion.div>

                    {/* Footer */}
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.6 }}
                        className="w-full"
                    >
                        <div className="flex justify-between items-end text-sm">
                            <div className="text-left space-y-1">
                                <p className="text-zinc-500 text-xs uppercase tracking-wider">
                                    Date Issued
                                </p>
                                <p className="text-zinc-300 font-semibold">
                                    {formatCertificateDate(certificate.issuedDate)}
                                </p>
                            </div>

                            {/* QR Code Placeholder */}
                            <div className="text-center space-y-1">
                                <div
                                    className={cn(
                                        "w-20 h-20 rounded-xl",
                                        "bg-white",
                                        "flex items-center justify-center",
                                        "border-2 border-purple-500/30"
                                    )}
                                >
                                    {/* In production: Use qrcode.react */}
                                    <div className="text-xs text-zinc-800 font-mono">
                                        QR
                                    </div>
                                </div>
                                <p className="text-zinc-500 text-xs">Scan to verify</p>
                            </div>

                            <div className="text-right space-y-1">
                                <p className="text-zinc-500 text-xs uppercase tracking-wider">
                                    Certificate ID
                                </p>
                                <p className="text-zinc-300 font-mono text-xs">
                                    {certificate.verificationCode}
                                </p>
                            </div>
                        </div>

                        {/* Signature line */}
                        <div className="mt-8 pt-4 border-t border-zinc-800">
                            <div className="flex justify-center">
                                <div className="text-center">
                                    <div className="w-48 border-t border-zinc-700 mb-2" />
                                    <p className="text-zinc-400 text-xs">
                                        DevOpsHub Certification Authority
                                    </p>
                                </div>
                            </div>
                        </div>
                    </motion.div>
                </div>
            </motion.div>

            {/* Action Buttons */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.8 }}
                className="flex flex-wrap justify-center gap-4"
            >
                <Button
                    onClick={handleDownloadPNG}
                    className={cn(
                        "rounded-xl bg-gradient-to-r from-purple-600 to-purple-700",
                        "hover:from-purple-700 hover:to-purple-800",
                        "shadow-lg shadow-purple-500/25"
                    )}
                >
                    <Download className="w-4 h-4 mr-2" />
                    Download PNG
                </Button>

                <Button
                    onClick={handleDownloadPDF}
                    variant="outline"
                    className={cn(
                        "rounded-xl border-purple-500/40",
                        "hover:bg-purple-500/10"
                    )}
                >
                    <Download className="w-4 h-4 mr-2" />
                    Download PDF
                </Button>

                <Button
                    onClick={handleShareLinkedIn}
                    variant="outline"
                    className={cn(
                        "rounded-xl border-blue-500/40",
                        "hover:bg-blue-500/10"
                    )}
                >
                    <Share2 className="w-4 h-4 mr-2" />
                    Share on LinkedIn
                </Button>

                <Button
                    onClick={handleShareTwitter}
                    variant="outline"
                    className={cn(
                        "rounded-xl border-cyan-500/40",
                        "hover:bg-cyan-500/10"
                    )}
                >
                    <Share2 className="w-4 h-4 mr-2" />
                    Share on Twitter
                </Button>
            </motion.div>

            {/* Installation Note (for demo) */}
            <div
                className={cn(
                    "text-center text-xs text-zinc-500 p-4 rounded-xl",
                    "bg-zinc-900/50 border border-zinc-800"
                )}
            >
                <p>
                    <strong>Note:</strong> Full download/QR functionality requires installing:
                    <code className="mx-1 px-2 py-1 bg-zinc-800 rounded text-cyan-400">
                        html2canvas
                    </code>
                    <code className="mx-1 px-2 py-1 bg-zinc-800 rounded text-cyan-400">
                        jspdf
                    </code>
                    <code className="mx-1 px-2 py-1 bg-zinc-800 rounded text-cyan-400">
                        qrcode.react
                    </code>
                </p>
            </div>
        </div>
    )
}

/* ============================================================================
   COMPACT CERTIFICATE CARD (for galleries)
   ============================================================================ */

interface CertificateCardProps {
    certificate: Certificate
    onClick?: () => void
    className?: string
}

export function CertificateCard({
    certificate,
    onClick,
    className,
}: CertificateCardProps) {
    return (
        <motion.div
            whileHover={{ scale: 1.03, y: -5 }}
            onClick={onClick}
            className={cn(
                "relative p-6 rounded-2xl cursor-pointer",
                "bg-gradient-to-br from-purple-600/20 to-cyan-600/10",
                "border border-purple-500/30",
                "backdrop-blur-sm",
                "transition-all duration-300",
                "hover:border-purple-500/50",
                "hover:shadow-[0_0_50px_rgba(139,92,246,0.3)]",
                className
            )}
        >
            {/* Badge */}
            <div className="absolute -top-3 -right-3">
                <motion.div
                    className={cn(
                        "w-12 h-12 rounded-full",
                        "bg-gradient-to-br from-amber-500 to-orange-600",
                        "flex items-center justify-center",
                        "border-2 border-amber-400/30"
                    )}
                    animate={{
                        boxShadow: [
                            "0 0 20px rgba(245, 158, 11, 0.4)",
                            "0 0 30px rgba(245, 158, 11, 0.6)",
                            "0 0 20px rgba(245, 158, 11, 0.4)",
                        ],
                    }}
                    transition={{ duration: 2, repeat: Infinity }}
                >
                    <Award className="w-6 h-6 text-white" />
                </motion.div>
            </div>

            <div className="space-y-3">
                <h3 className="text-xl font-bold text-white">
                    {certificate.moduleName}
                </h3>
                <p className="text-zinc-400 text-sm">
                    Issued {formatCertificateDate(certificate.issuedDate)}
                </p>

                {/* Skills */}
                {certificate.skills && certificate.skills.length > 0 && (
                    <div className="flex flex-wrap gap-2">
                        {certificate.skills.slice(0, 3).map((skill) => (
                            <span
                                key={skill}
                                className={cn(
                                    "px-3 py-1 rounded-full text-xs",
                                    "bg-purple-500/20 text-purple-300",
                                    "border border-purple-500/30"
                                )}
                            >
                                {skill}
                            </span>
                        ))}
                        {certificate.skills.length > 3 && (
                            <span className="text-zinc-500 text-xs self-center">
                                +{certificate.skills.length - 3} more
                            </span>
                        )}
                    </div>
                )}

                <div className="pt-3 border-t border-zinc-800 flex justify-between items-center">
                    <span className="text-xs text-zinc-500 font-mono">
                        {certificate.verificationCode}
                    </span>
                    {certificate.completionScore && (
                        <span className="text-sm font-semibold text-emerald-400">
                            {certificate.completionScore}% Score
                        </span>
                    )}
                </div>
            </div>
        </motion.div>
    )
}
