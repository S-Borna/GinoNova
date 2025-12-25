"use client"

/**
 * ============================================================================
 * COSMIC AURORA — MILESTONE 2.0 Unified Background ✨
 * ============================================================================
 *
 * Netflix + Disney + Tesla premium animated background
 *
 * Features:
 * - Animated purple, cyan, and pink aurora orbs
 * - Subtle grid overlay
 * - Blur effects for depth
 * - Consistent across ALL module pages
 *
 * @phase MILESTONE-2.0-COSMIC-REVOLUTION
 * @phase DESIGN-UNIFICATION
 */

import { motion } from "framer-motion"

interface CosmicAuroraProps {
    /** Intensity of the aurora effect (default: 1) */
    intensity?: number
    /** Whether to show the grid overlay (default: true) */
    showGrid?: boolean
    /** Custom z-index (default: 0) */
    zIndex?: number
}

export function CosmicAurora({
    intensity = 1,
    showGrid = true,
    zIndex = 0,
}: CosmicAuroraProps) {
    const opacityMultiplier = intensity

    return (
        <div 
            className="fixed inset-0 overflow-hidden pointer-events-none"
            style={{ zIndex }}
        >
            {/* Purple orb - top right - PRIMARY */}
            <motion.div
                className="absolute w-[600px] h-[600px] rounded-full"
                style={{
                    background: "radial-gradient(circle, rgba(139,92,246,0.15) 0%, transparent 70%)",
                    filter: "blur(60px)",
                    top: "-10%",
                    right: "-5%",
                }}
                animate={{
                    scale: [1, 1.2, 1],
                    opacity: [0.3 * opacityMultiplier, 0.5 * opacityMultiplier, 0.3 * opacityMultiplier],
                }}
                transition={{ duration: 8, repeat: Infinity, ease: "easeInOut" }}
            />

            {/* Cyan orb - bottom left - SECONDARY */}
            <motion.div
                className="absolute w-[500px] h-[500px] rounded-full"
                style={{
                    background: "radial-gradient(circle, rgba(34,211,238,0.1) 0%, transparent 70%)",
                    filter: "blur(60px)",
                    bottom: "10%",
                    left: "-10%",
                }}
                animate={{
                    scale: [1.1, 1, 1.1],
                    opacity: [0.2 * opacityMultiplier, 0.4 * opacityMultiplier, 0.2 * opacityMultiplier],
                }}
                transition={{ duration: 10, repeat: Infinity, ease: "easeInOut" }}
            />

            {/* Pink orb - center - ACCENT */}
            <motion.div
                className="absolute w-[400px] h-[400px] rounded-full"
                style={{
                    background: "radial-gradient(circle, rgba(236,72,153,0.08) 0%, transparent 70%)",
                    filter: "blur(80px)",
                    top: "40%",
                    left: "30%",
                }}
                animate={{
                    x: [0, 50, 0],
                    y: [0, -30, 0],
                    opacity: [0.15 * opacityMultiplier, 0.25 * opacityMultiplier, 0.15 * opacityMultiplier],
                }}
                transition={{ duration: 12, repeat: Infinity, ease: "easeInOut" }}
            />

            {/* Subtle grid overlay */}
            {showGrid && (
                <div
                    className="absolute inset-0 opacity-[0.015]"
                    style={{
                        backgroundImage: `
                            linear-gradient(rgba(139,92,246,0.5) 1px, transparent 1px),
                            linear-gradient(90deg, rgba(139,92,246,0.5) 1px, transparent 1px)
                        `,
                        backgroundSize: '60px 60px'
                    }}
                />
            )}
        </div>
    )
}

export default CosmicAurora
