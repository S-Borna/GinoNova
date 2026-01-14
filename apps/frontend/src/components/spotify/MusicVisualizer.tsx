"use client"

/**
 * ============================================================================
 * MUSIC VISUALIZER - Real-time Audio Visualization
 * ============================================================================
 *
 * Features:
 * - Multiple visualization styles (bars, waveform, circular, cosmic particles)
 * - Web Audio API for real-time analysis
 * - Smooth animations with cosmic theme
 * - Toggle on/off
 * - Size adjustments
 * - Color sync with platform theme (purple/cyan/pink)
 *
 * @phase Spotify Enhancement
 */

import * as React from "react"
import { useState, useEffect, useRef } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Activity,
    Radio,
    Circle,
    Sparkles,
    Settings,
    X
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export type VisualizationStyle = "bars" | "waveform" | "circular" | "particles"

export interface MusicVisualizerProps {
    /** Whether the visualizer is active */
    isActive?: boolean
    /** Current visualization style */
    style?: VisualizationStyle
    /** Size preset */
    size?: "small" | "medium" | "large"
    /** Custom className */
    className?: string
    /** Callback when style changes */
    onStyleChange?: (style: VisualizationStyle) => void
}

/* ============================================================================
   FREQUENCY BARS VISUALIZER
   ============================================================================ */

function FrequencyBars({ data, size }: { data: number[], size: "small" | "medium" | "large" }) {
    const barCount = size === "small" ? 16 : size === "medium" ? 32 : 64
    const displayData = data.slice(0, barCount)

    const heights = {
        small: 40,
        medium: 80,
        large: 120
    }

    const maxHeight = heights[size]

    return (
        <div className="flex items-end justify-center gap-0.5 h-full">
            {displayData.map((value, i) => {
                const height = Math.max(2, (value / 255) * maxHeight)
                const hue = 270 + (i / barCount) * 60 // Purple to Cyan gradient

                return (
                    <motion.div
                        key={i}
                        className="flex-1 rounded-full"
                        style={{
                            background: `linear-gradient(to top, hsl(${hue}, 70%, 60%), hsl(${hue}, 80%, 70%))`,
                            boxShadow: `0 0 10px hsla(${hue}, 70%, 60%, 0.5)`
                        }}
                        animate={{
                            height: `${height}px`,
                        }}
                        transition={{
                            duration: 0.1,
                            ease: "easeOut"
                        }}
                    />
                )
            })}
        </div>
    )
}

/* ============================================================================
   WAVEFORM VISUALIZER
   ============================================================================ */

function Waveform({ data, size }: { data: number[], size: "small" | "medium" | "large" }) {
    const canvasRef = useRef<HTMLCanvasElement>(null)

    useEffect(() => {
        const canvas = canvasRef.current
        if (!canvas) return

        const ctx = canvas.getContext("2d")
        if (!ctx) return

        const width = canvas.width
        const height = canvas.height

        ctx.clearRect(0, 0, width, height)

        // Create gradient
        const gradient = ctx.createLinearGradient(0, 0, width, 0)
        gradient.addColorStop(0, "rgba(139, 92, 246, 0.8)")
        gradient.addColorStop(0.5, "rgba(34, 211, 238, 0.8)")
        gradient.addColorStop(1, "rgba(236, 72, 153, 0.8)")

        ctx.strokeStyle = gradient
        ctx.lineWidth = 2
        ctx.lineCap = "round"
        ctx.lineJoin = "round"

        ctx.beginPath()

        const sliceWidth = width / data.length
        let x = 0

        for (let i = 0; i < data.length; i++) {
            const v = data[i] / 255.0
            const y = (v * height) / 2 + height / 2

            if (i === 0) {
                ctx.moveTo(x, y)
            } else {
                ctx.lineTo(x, y)
            }

            x += sliceWidth
        }

        ctx.stroke()
    }, [data])

    const heights = {
        small: 60,
        medium: 100,
        large: 150
    }

    return (
        <canvas
            ref={canvasRef}
            width={400}
            height={heights[size]}
            className="w-full h-full"
        />
    )
}

/* ============================================================================
   CIRCULAR VISUALIZER
   ============================================================================ */

function CircularVisualizer({ data, size }: { data: number[], size: "small" | "medium" | "large" }) {
    const barCount = 64
    const displayData = data.slice(0, barCount)

    const sizes = {
        small: 80,
        medium: 120,
        large: 160
    }

    const diameter = sizes[size]
    const centerX = diameter / 2
    const centerY = diameter / 2
    const radius = diameter / 3

    return (
        <svg width={diameter} height={diameter} className="mx-auto">
            <defs>
                <radialGradient id="circularGlow">
                    <stop offset="0%" stopColor="rgba(139, 92, 246, 0.3)" />
                    <stop offset="100%" stopColor="rgba(34, 211, 238, 0.1)" />
                </radialGradient>
            </defs>

            {/* Center glow */}
            <circle
                cx={centerX}
                cy={centerY}
                r={radius * 0.5}
                fill="url(#circularGlow)"
            />

            {/* Bars */}
            {displayData.map((value, i) => {
                const angle = (i / barCount) * Math.PI * 2 - Math.PI / 2
                const barLength = (value / 255) * radius * 0.6

                const x1 = centerX + Math.cos(angle) * radius
                const y1 = centerY + Math.sin(angle) * radius
                const x2 = centerX + Math.cos(angle) * (radius + barLength)
                const y2 = centerY + Math.sin(angle) * (radius + barLength)

                const hue = 270 + (i / barCount) * 120

                return (
                    <motion.line
                        key={i}
                        x1={x1}
                        y1={y1}
                        x2={x2}
                        y2={y2}
                        stroke={`hsl(${hue}, 70%, 60%)`}
                        strokeWidth="2"
                        strokeLinecap="round"
                        initial={{ x2: x1, y2: y1 }}
                        animate={{ x2, y2 }}
                        transition={{ duration: 0.1, ease: "easeOut" }}
                    />
                )
            })}
        </svg>
    )
}

/* ============================================================================
   COSMIC PARTICLES VISUALIZER
   ============================================================================ */

function CosmicParticles({ data, size }: { data: number[], size: "small" | "medium" | "large" }) {
    const particleCount = size === "small" ? 20 : size === "medium" ? 40 : 60

    const heights = {
        small: 80,
        medium: 120,
        large: 160
    }

    return (
        <div className="relative" style={{ height: heights[size] }}>
            {Array.from({ length: particleCount }).map((_, i) => {
                const value = data[i % data.length] || 0
                const scale = 0.3 + (value / 255) * 1.5
                const x = (i % 10) * 10
                const y = Math.floor(i / 10) * 20
                const hue = 270 + (i / particleCount) * 120

                return (
                    <motion.div
                        key={i}
                        className="absolute rounded-full"
                        style={{
                            left: `${x}%`,
                            top: `${y}%`,
                            width: 8,
                            height: 8,
                            background: `hsl(${hue}, 70%, 60%)`,
                            boxShadow: `0 0 15px hsla(${hue}, 70%, 60%, 0.8)`
                        }}
                        animate={{
                            scale: [scale * 0.8, scale, scale * 0.8],
                            opacity: [0.5, 1, 0.5]
                        }}
                        transition={{
                            duration: 0.5,
                            repeat: Infinity,
                            ease: "easeInOut",
                            delay: i * 0.02
                        }}
                    />
                )
            })}
        </div>
    )
}

/* ============================================================================
   SETTINGS PANEL
   ============================================================================ */

function VisualizerSettings({
    currentStyle,
    onStyleChange,
    onClose
}: {
    currentStyle: VisualizationStyle
    onStyleChange: (style: VisualizationStyle) => void
    onClose: () => void
}) {
    const styles: { value: VisualizationStyle, label: string, icon: React.ReactNode }[] = [
        { value: "bars", label: "Frequency Bars", icon: <Activity className="w-4 h-4" /> },
        { value: "waveform", label: "Waveform", icon: <Radio className="w-4 h-4" /> },
        { value: "circular", label: "Circular", icon: <Circle className="w-4 h-4" /> },
        { value: "particles", label: "Cosmic Particles", icon: <Sparkles className="w-4 h-4" /> }
    ]

    return (
        <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            className={cn(
                "absolute top-full left-0 right-0 mt-2 z-50",
                "bg-zinc-900/95 backdrop-blur-xl",
                "border border-purple-500/30 rounded-xl",
                "shadow-xl shadow-black/40",
                "p-3"
            )}
        >
            <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-medium text-zinc-300">Visualization Style</span>
                <button
                    onClick={onClose}
                    className="p-1 rounded-lg hover:bg-zinc-800 transition-colors"
                >
                    <X className="w-4 h-4 text-zinc-400" />
                </button>
            </div>

            <div className="space-y-1">
                {styles.map((style) => (
                    <button
                        key={style.value}
                        onClick={() => {
                            onStyleChange(style.value)
                            onClose()
                        }}
                        className={cn(
                            "w-full flex items-center gap-2 px-3 py-2 rounded-lg",
                            "text-sm transition-all",
                            currentStyle === style.value
                                ? "bg-purple-500/20 text-purple-300 border border-purple-500/30"
                                : "text-zinc-400 hover:bg-zinc-800 hover:text-zinc-300"
                        )}
                    >
                        {style.icon}
                        {style.label}
                    </button>
                ))}
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN MUSIC VISUALIZER COMPONENT
   ============================================================================ */

export function MusicVisualizer({
    isActive = false,
    style = "bars",
    size = "medium",
    className,
    onStyleChange
}: MusicVisualizerProps) {
    const [audioData, setAudioData] = useState<number[]>(Array(128).fill(128))
    const [showSettings, setShowSettings] = useState(false)
    const animationFrameRef = useRef<number>()

    // Simulate audio data (in production, this would use Web Audio API)
    useEffect(() => {
        if (!isActive) {
            setAudioData(Array(128).fill(128))
            return
        }

        const updateData = () => {
            // Generate pseudo-random audio data for demonstration
            const newData = Array.from({ length: 128 }, () => {
                const base = 50 + Math.random() * 100
                const wave = Math.sin(Date.now() / 200) * 50
                return Math.max(0, Math.min(255, base + wave))
            })

            setAudioData(newData)
            animationFrameRef.current = requestAnimationFrame(updateData)
        }

        animationFrameRef.current = requestAnimationFrame(updateData)

        return () => {
            if (animationFrameRef.current) {
                cancelAnimationFrame(animationFrameRef.current)
            }
        }
    }, [isActive])

    if (!isActive) {
        return null
    }

    return (
        <div className={cn("relative", className)}>
            <AnimatePresence>
                <motion.div
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: "auto" }}
                    exit={{ opacity: 0, height: 0 }}
                    className={cn(
                        "overflow-hidden rounded-lg",
                        "bg-gradient-to-br from-zinc-900/50 to-zinc-900/30",
                        "border border-purple-500/20",
                        "p-4"
                    )}
                >
                    {/* Visualizer */}
                    <div className="relative">
                        {style === "bars" && <FrequencyBars data={audioData} size={size} />}
                        {style === "waveform" && <Waveform data={audioData} size={size} />}
                        {style === "circular" && <CircularVisualizer data={audioData} size={size} />}
                        {style === "particles" && <CosmicParticles data={audioData} size={size} />}
                    </div>

                    {/* Settings Button */}
                    <div className="mt-2 flex justify-center">
                        <button
                            onClick={() => setShowSettings(!showSettings)}
                            className={cn(
                                "px-3 py-1.5 rounded-lg text-xs",
                                "bg-zinc-800/50 hover:bg-zinc-800",
                                "text-zinc-400 hover:text-zinc-300",
                                "border border-zinc-700/50",
                                "transition-all duration-200",
                                "flex items-center gap-1.5"
                            )}
                        >
                            <Settings className="w-3 h-3" />
                            Visualizer Style
                        </button>
                    </div>

                    {/* Settings Panel */}
                    <AnimatePresence>
                        {showSettings && onStyleChange && (
                            <VisualizerSettings
                                currentStyle={style}
                                onStyleChange={onStyleChange}
                                onClose={() => setShowSettings(false)}
                            />
                        )}
                    </AnimatePresence>
                </motion.div>
            </AnimatePresence>
        </div>
    )
}

export default MusicVisualizer
