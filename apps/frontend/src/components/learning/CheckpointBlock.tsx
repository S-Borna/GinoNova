"use client"

/**
 * ============================================================================
 * CHECKPOINT BLOCK COMPONENT - Progress Milestone Marker
 * ============================================================================
 *
 * Features:
 * - Gradient background (indigo to purple)
 * - Celebration icon
 * - Title and description
 * - XP earned badge
 * - Optional confetti animation
 *
 * @phase ILE Phase 3 - Content Blocks
 */

import * as React from "react"
import { useEffect, useState } from "react"
import { cn } from "@/lib/utils"
import { Trophy, Sparkles, Star, CheckCircle2 } from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface CheckpointBlockProps {
    title: string
    description: string
    xpSoFar?: number
    isReached?: boolean
    className?: string
}

/* ============================================================================
   CONFETTI COMPONENT (Simple CSS Animation)
   ============================================================================ */

function Confetti() {
    const [particles, setParticles] = useState<Array<{ id: number; left: string; delay: string; color: string }>>([])

    useEffect(() => {
        const colors = ["#a855f7", "#6366f1", "#ec4899", "#f59e0b", "#10b981"]
        const newParticles = Array.from({ length: 20 }, (_, i) => ({
            id: i,
            left: `${Math.random() * 100}%`,
            delay: `${Math.random() * 0.5}s`,
            color: colors[Math.floor(Math.random() * colors.length)],
        }))
        setParticles(newParticles)
    }, [])

    return (
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
            {particles.map((particle) => (
                <div
                    key={particle.id}
                    className="absolute top-0 w-2 h-2 rounded-full animate-confetti"
                    style={{
                        left: particle.left,
                        backgroundColor: particle.color,
                        animationDelay: particle.delay,
                    }}
                />
            ))}
            <style jsx>{`
                @keyframes confetti {
                    0% {
                        transform: translateY(-10px) rotate(0deg);
                        opacity: 1;
                    }
                    100% {
                        transform: translateY(300px) rotate(720deg);
                        opacity: 0;
                    }
                }
                .animate-confetti {
                    animation: confetti 2s ease-out forwards;
                }
            `}</style>
        </div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function CheckpointBlock({
    title,
    description,
    xpSoFar = 0,
    isReached = true,
    className,
}: CheckpointBlockProps) {
    const [showConfetti, setShowConfetti] = useState(false)

    useEffect(() => {
        if (isReached) {
            setShowConfetti(true)
            const timer = setTimeout(() => setShowConfetti(false), 2000)
            return () => clearTimeout(timer)
        }
    }, [isReached])

    return (
        <div className={cn(
            "relative rounded-xl overflow-hidden my-6",
            className
        )}>
            {/* Confetti Animation */}
            {showConfetti && <Confetti />}

            {/* Gradient Background */}
            <div className="absolute inset-0 bg-gradient-to-br from-indigo-600/20 via-purple-600/20 to-pink-600/20" />
            <div className="absolute inset-0 bg-gradient-to-t from-neutral-900/80 to-transparent" />

            {/* Content */}
            <div className="relative px-6 py-8 text-center">
                {/* Icon */}
                <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 mb-4 shadow-lg shadow-purple-500/25">
                    <Trophy className="h-8 w-8 text-white" />
                </div>

                {/* Stars */}
                <div className="flex justify-center gap-1 mb-3">
                    {[...Array(3)].map((_, i) => (
                        <Star
                            key={i}
                            className={cn(
                                "h-5 w-5",
                                isReached
                                    ? "text-yellow-400 fill-yellow-400"
                                    : "text-neutral-600"
                            )}
                        />
                    ))}
                </div>

                {/* Title */}
                <h3 className="text-2xl font-bold text-white mb-2">
                    {title}
                </h3>

                {/* Description */}
                <p className="text-neutral-300 max-w-md mx-auto mb-4">
                    {description}
                </p>

                {/* XP Badge */}
                {xpSoFar > 0 && (
                    <div className="inline-flex items-center gap-2 px-4 py-2 bg-yellow-500/20 rounded-full">
                        <Sparkles className="h-4 w-4 text-yellow-400" />
                        <span className="font-semibold text-yellow-400">
                            {xpSoFar} XP Earned
                        </span>
                    </div>
                )}

                {/* Completion Status */}
                {isReached && (
                    <div className="flex items-center justify-center gap-2 mt-4 text-green-400">
                        <CheckCircle2 className="h-5 w-5" />
                        <span className="text-sm font-medium">Checkpoint Reached!</span>
                    </div>
                )}
            </div>

            {/* Bottom Border Glow */}
            <div className="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500" />
        </div>
    )
}

export default CheckpointBlock
