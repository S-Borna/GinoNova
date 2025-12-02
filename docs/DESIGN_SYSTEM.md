# 🎨 DevOpsHub Design System

> **"Learn like a pro, feel like home"**
> A premium, gamified learning platform with Apple-inspired polish

<div align="center">

![Version](https://img.shields.io/badge/version-2.0-purple?style=for-the-badge)
![Next.js](https://img.shields.io/badge/Next.js-15.1.8-black?style=for-the-badge&logo=next.js)
![Tailwind](https://img.shields.io/badge/Tailwind-4.1-38bdf8?style=for-the-badge&logo=tailwindcss)
![Framer Motion](https://img.shields.io/badge/Framer_Motion-12.x-ff69b4?style=for-the-badge&logo=framer)

**[Live Demo](https://saids-devopshub.netlify.app) • [Tech Stack](#-tech-stack) • [Color System](#-color-palette) • [Components](#-component-library)**

</div>

---

## 📋 Table of Contents

1. [Philosophy](#-design-philosophy)
2. [Tech Stack](#-tech-stack)
3. [Color Palette](#-color-palette)
4. [Typography](#-typography)
5. [Glassmorphism](#-glassmorphism-design)
6. [Animation System](#-animation-system)
7. [Component Library](#-component-library)
8. [Glow Effects](#-glow-effects--premium-polish)
9. [Code Examples](#-code-examples)
10. [File Structure](#-file-structure)

---

## 🧠 Design Philosophy

DevOpsHub's design follows three core principles:

### 1. **Premium Dark Mode First**

Deep, rich backgrounds that feel luxurious and reduce eye strain during long study sessions.

```
Background Hierarchy:
┌─────────────────────────────────────┐
│  bg-deep     #0a0a0f  (darkest)    │
│  bg-primary  #0f0f17               │
│  bg-secondary #12121c              │
│  bg-tertiary #141420               │
│  bg-elevated #1a1a28  (lightest)   │
└─────────────────────────────────────┘
```

### 2. **Gamification That Motivates**

Every interaction feels rewarding. XP gains glow gold, streaks burn orange, progress shines mint green.

### 3. **Apple-Inspired Polish**

Subtle animations, generous spacing, and attention to micro-interactions that feel native and premium.

---

## 🛠 Tech Stack

### Core Framework

| Technology | Version | Purpose |
|------------|---------|---------|
| **Next.js** | 15.1.8 | React framework with App Router |
| **React** | 18.3.1 | UI library |
| **TypeScript** | Latest | Type safety |

### Styling & Animation

| Technology | Version | Purpose |
|------------|---------|---------|
| **Tailwind CSS** | 4.1.17 | Utility-first CSS |
| **Framer Motion** | 12.23.25 | Animation library |
| **tailwindcss-animate** | 1.0.7 | Animation utilities |
| **tw-animate-css** | 1.4.0 | CSS animation classes |

### UI Components

| Technology | Purpose |
|------------|---------|
| **Radix UI** | Headless accessible components |
| **Lucide React** | Icon library (555+ icons) |
| **class-variance-authority** | Component variants |
| **clsx + tailwind-merge** | Class name utilities |

### Additional Libraries

| Technology | Purpose |
|------------|---------|
| **canvas-confetti** | Celebration animations |
| **react-syntax-highlighter** | Code blocks |
| **xterm.js** | Terminal emulation |
| **sonner** | Toast notifications |

---

## 🎨 Color Palette

### Primary Colors — Purple Signature

The purple gradient is our brand identity, used for primary actions and focus states.

```css
/* Purple Scale */
--primary-50:  #faf5ff;   /* Lightest */
--primary-100: #f3e8ff;
--primary-200: #e9d5ff;
--primary-300: #d8b4fe;
--primary-400: #c084fc;
--primary-500: #a855f7;   /* PRIMARY */
--primary-600: #9333ea;
--primary-700: #7e22ce;
--primary-800: #6b21a8;
--primary-900: #581c87;
--primary-950: #3b0764;   /* Darkest */
```

### Accent Colors — Gamification

Each color serves a specific purpose in the gamification system:

| Color | Hex Code | Use Case | Visual |
|-------|----------|----------|--------|
| **Chill Mint** | `#22D3AC` / `#22c55e` | Success, Progress, Completions | 🟢 |
| **Focus Purple** | `#8B5CF6` / `#a855f7` | Primary accent, Focus states | 🟣 |
| **XP Gold** | `#F59E0B` / `#fbbf24` | XP gains, Rewards, Achievements | 🟡 |
| **Fire Orange** | `#F97316` | Streaks, Energy, Urgency | 🟠 |
| **Info Cyan** | `#06b6d4` | Information, StudyFlow mode | 🔵 |
| **Danger Red** | `#ef4444` | Errors, Warnings | 🔴 |

### Color Usage in Practice

```tsx
// Success state (task completed)
className="text-emerald-400 bg-emerald-500/10 border-emerald-500/20"

// XP gain notification
className="text-amber-400 bg-amber-500/15 shadow-[0_0_20px_rgba(251,191,36,0.25)]"

// Streak counter
className="text-orange-400 bg-orange-500/15 border-orange-500/30"

// Primary button
className="bg-gradient-to-r from-purple-600 to-purple-500 hover:from-purple-500 hover:to-purple-400"
```

### Gradients

```css
/* Primary Gradient - Purple */
--primary-gradient: linear-gradient(135deg, #7c3aed 0%, #a855f7 50%, #c084fc 100%);

/* Hero Gradient */
--gradient-hero: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%);

/* Success Gradient */
--gradient-success: linear-gradient(135deg, #22c55e 0%, #10b981 100%);

/* Card Gradient (subtle) */
--card-gradient: linear-gradient(135deg, rgba(168, 85, 247, 0.1) 0%, rgba(124, 58, 237, 0.05) 100%);
```

---

## ✍️ Typography

### Font Families

```css
/* Primary Font - UI Text */
--font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

/* Monospace - Code Blocks */
--font-mono: 'JetBrains Mono', 'Fira Code', 'SF Mono', monospace;
```

### Font Scale

| Class | Size | Use Case |
|-------|------|----------|
| `text-xs` | 0.75rem (12px) | Labels, Badges |
| `text-sm` | 0.875rem (14px) | Secondary text |
| `text-base` | 1rem (16px) | Body text |
| `text-lg` | 1.125rem (18px) | Emphasized body |
| `text-xl` | 1.25rem (20px) | Section titles |
| `text-2xl` | 1.5rem (24px) | Card titles |
| `text-3xl` | 1.875rem (30px) | Page titles |
| `text-4xl` | 2.25rem (36px) | Hero headings |
| `text-5xl` | 3rem (48px) | Display text |

### Heading Hierarchy Example

```tsx
// Hero heading with gradient
<h1 className="text-4xl md:text-5xl font-black bg-gradient-to-r from-white via-purple-200 to-white bg-clip-text text-transparent">
    Welcome back, {userName}! 🚀
</h1>

// Section heading
<h2 className="text-2xl font-bold text-zinc-100">
    Your Progress
</h2>

// Card title
<h3 className="text-lg font-semibold text-zinc-200">
    Current Module
</h3>

// Label
<span className="text-xs font-medium uppercase tracking-wider text-purple-400">
    Command Center
</span>
```

---

## 🔮 Glassmorphism Design

### What is Glassmorphism?

A design style featuring:

- Semi-transparent backgrounds
- Blur effects (backdrop-filter)
- Subtle borders
- Layered depth

### Implementation

```css
/* Glass Effect Variables */
--glass-bg: rgba(15, 15, 23, 0.8);
--glass-bg-light: rgba(255, 255, 255, 0.05);
--glass-border: rgba(255, 255, 255, 0.08);
--glass-blur: 12px;
--glass-blur-lg: 20px;
```

### Premium Glass Card

```tsx
<div className={cn(
    // Base structure
    "relative overflow-hidden rounded-2xl",
    // Glass background
    "bg-zinc-900/60 backdrop-blur-xl",
    // Border
    "border border-white/10",
    // Padding
    "p-6"
)}>
    {/* Content */}
</div>
```

### Glass Card with Glow Border

```tsx
<motion.div
    className={cn(
        "relative group rounded-2xl overflow-hidden",
        "bg-gradient-to-br from-zinc-900/90 to-zinc-800/50",
        "backdrop-blur-xl",
        "border border-purple-500/20",
        "hover:border-purple-500/40",
        "transition-all duration-300"
    )}
    whileHover={{
        boxShadow: "0 0 30px rgba(168, 85, 247, 0.15)"
    }}
>
    {/* Inner glow effect */}
    <div className="absolute inset-0 bg-gradient-to-br from-purple-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />

    {/* Content */}
    <div className="relative z-10 p-6">
        {children}
    </div>
</motion.div>
```

---

## ⚡ Animation System

### Timing Functions (Easing)

```css
/* Natural movement */
--ease-default: cubic-bezier(0.4, 0, 0.2, 1);
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);

/* Playful bounce */
--ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
--ease-elastic: cubic-bezier(0.68, -0.55, 0.265, 1.55);
```

### Duration Scale

```css
--duration-fastest: 50ms;   /* Micro-interactions */
--duration-faster: 100ms;   /* Hover states */
--duration-fast: 150ms;     /* Button clicks */
--duration-normal: 200ms;   /* Default transitions */
--duration-slow: 300ms;     /* Page elements */
--duration-slower: 400ms;   /* Modal animations */
--duration-slowest: 500ms;  /* Hero animations */
```

### Framer Motion Patterns

#### 1. Staggered Children

```tsx
const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
        opacity: 1,
        transition: {
            staggerChildren: 0.1
        }
    }
}

const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: {
        opacity: 1,
        y: 0,
        transition: { type: "spring", stiffness: 100 }
    }
}

<motion.div
    variants={containerVariants}
    initial="hidden"
    animate="visible"
>
    {items.map(item => (
        <motion.div key={item.id} variants={itemVariants}>
            {item.content}
        </motion.div>
    ))}
</motion.div>
```

#### 2. Hover Lift Effect

```tsx
<motion.div
    whileHover={{
        y: -4,
        boxShadow: "0 20px 40px rgba(0,0,0,0.3)"
    }}
    transition={{ type: "spring", stiffness: 400, damping: 25 }}
>
    Card content
</motion.div>
```

#### 3. Animated Sparkles

```tsx
<motion.div
    className="absolute top-8 right-20 text-purple-400/60"
    animate={{
        rotate: 360,
        scale: [1, 1.2, 1]
    }}
    transition={{
        duration: 4,
        repeat: Infinity
    }}
>
    <Sparkles className="w-6 h-6" />
</motion.div>
```

#### 4. 3D Card Flip

```tsx
<motion.button
    initial={{ opacity: 0, y: 60, rotateX: -15 }}
    animate={{ opacity: 1, y: 0, rotateX: 0 }}
    whileHover={{
        scale: 1.05,
        y: -12,
        rotateY: 5
    }}
    style={{ transformStyle: "preserve-3d" }}
>
    OS Selection Card
</motion.button>
```

### CSS Animation Classes

```css
/* Fade animations */
.animate-fade-in { animation: fadeIn 200ms ease-out forwards; }
.animate-fade-in-up { animation: fadeInUp 300ms ease-out forwards; }

/* Continuous animations */
.animate-pulse-soft { animation: pulseSoft 2s ease-in-out infinite; }
.animate-float { animation: float 3s ease-in-out infinite; }
.animate-glow { animation: glow 2s ease-in-out infinite; }

/* Stagger delays */
.stagger-1 { animation-delay: 0.05s; }
.stagger-2 { animation-delay: 0.10s; }
.stagger-3 { animation-delay: 0.15s; }
/* ... up to .stagger-10 */
```

---

## 🧩 Component Library

### 1. Premium Hero Section

The hero section sets the tone for each page with animated background glows and floating particles.

```tsx
function PremiumHero({ title, subtitle }: HeroProps) {
    return (
        <div className={cn(
            "relative overflow-hidden rounded-3xl",
            "bg-gradient-to-br from-zinc-900 via-purple-950/40 to-zinc-900",
            "border border-purple-500/20",
            "p-8 md:p-10"
        )}>
            {/* Ambient glow effects */}
            <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-purple-500/15 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/4" />
            <div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-emerald-500/10 rounded-full blur-[100px] translate-y-1/2 -translate-x-1/4" />

            {/* Floating sparkles */}
            <motion.div
                className="absolute top-8 right-20 text-purple-400/60"
                animate={{ rotate: 360, scale: [1, 1.2, 1] }}
                transition={{ duration: 4, repeat: Infinity }}
            >
                <Sparkles className="w-6 h-6" />
            </motion.div>

            {/* Content */}
            <div className="relative">
                <h1 className="text-4xl font-black bg-gradient-to-r from-white via-purple-200 to-white bg-clip-text text-transparent">
                    {title}
                </h1>
                <p className="text-zinc-400 text-lg">{subtitle}</p>
            </div>
        </div>
    )
}
```

### 2. Premium Stat Card

Stat cards display key metrics with color-coded glows.

```tsx
function PremiumStatCard({
    icon: Icon,
    value,
    label,
    color,
    glowColor
}: StatCardProps) {
    const colorStyles = {
        gold: "from-amber-500/20 to-amber-600/10 border-amber-500/30 text-amber-400",
        mint: "from-emerald-500/20 to-emerald-600/10 border-emerald-500/30 text-emerald-400",
        purple: "from-purple-500/20 to-purple-600/10 border-purple-500/30 text-purple-400",
        orange: "from-orange-500/20 to-orange-600/10 border-orange-500/30 text-orange-400",
    }

    return (
        <motion.div
            whileHover={{
                scale: 1.02,
                boxShadow: `0 0 30px ${glowColor}`
            }}
            className={cn(
                "relative p-6 rounded-2xl",
                "bg-gradient-to-br",
                "border backdrop-blur-sm",
                colorStyles[color]
            )}
        >
            <div className="flex items-center gap-4">
                <div className={cn(
                    "p-3 rounded-xl",
                    "bg-gradient-to-br from-white/10 to-white/5"
                )}>
                    <Icon className="w-6 h-6" />
                </div>
                <div>
                    <div className="text-3xl font-black">{value}</div>
                    <div className="text-sm text-zinc-400">{label}</div>
                </div>
            </div>
        </motion.div>
    )
}
```

### 3. XP Progress Ring

A circular progress indicator with SVG gradients.

```tsx
function PremiumXPRing({ currentXP, xpToNext, level }: XPRingProps) {
    const progress = (currentXP / xpToNext) * 100
    const circumference = 2 * Math.PI * 54 // radius = 54
    const strokeDashoffset = circumference - (progress / 100) * circumference

    return (
        <div className="relative">
            {/* Glow backdrop */}
            <div className="absolute inset-0 bg-amber-500/20 rounded-full blur-xl animate-pulse" />

            <svg className="w-32 h-32 -rotate-90">
                <defs>
                    <linearGradient id="xp-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stopColor="#F59E0B" />
                        <stop offset="50%" stopColor="#FBBF24" />
                        <stop offset="100%" stopColor="#FCD34D" />
                    </linearGradient>
                </defs>

                {/* Background track */}
                <circle
                    cx="64" cy="64" r="54"
                    fill="none"
                    stroke="rgba(255,255,255,0.1)"
                    strokeWidth="8"
                />

                {/* Progress arc */}
                <circle
                    cx="64" cy="64" r="54"
                    fill="none"
                    stroke="url(#xp-gradient)"
                    strokeWidth="8"
                    strokeLinecap="round"
                    strokeDasharray={circumference}
                    strokeDashoffset={strokeDashoffset}
                    className="transition-all duration-1000"
                />
            </svg>

            {/* Center content */}
            <div className="absolute inset-0 flex items-center justify-center">
                <div className="text-center">
                    <div className="text-4xl font-black text-amber-400">{level}</div>
                    <div className="text-xs text-zinc-400">LEVEL</div>
                </div>
            </div>
        </div>
    )
}
```

### 4. Platform Selector Card

Interactive OS selection with holographic effects.

```tsx
function PlatformCard({ os, isSelected, onClick }: PlatformCardProps) {
    const cardConfig = {
        macos: {
            gradient: "from-zinc-800 via-zinc-900 to-black",
            glow: "rgba(147, 51, 234, 0.4)",
            accent: "from-blue-500 via-purple-500 to-pink-500"
        },
        windows: {
            gradient: "from-blue-900 via-blue-950 to-slate-900",
            glow: "rgba(59, 130, 246, 0.4)",
            accent: "from-cyan-400 via-blue-500 to-indigo-600"
        },
        linux: {
            gradient: "from-orange-900/80 via-amber-950 to-zinc-900",
            glow: "rgba(245, 158, 11, 0.4)",
            accent: "from-orange-400 via-amber-500 to-yellow-500"
        }
    }

    return (
        <motion.button
            whileHover={{ scale: 1.05, y: -12, rotateY: 5 }}
            whileTap={{ scale: 0.98 }}
            className="relative w-full h-[260px] rounded-3xl"
            style={{ transformStyle: "preserve-3d" }}
        >
            {/* Holographic border */}
            <div className={cn(
                "absolute -inset-[2px] rounded-3xl opacity-0 group-hover:opacity-100",
                "bg-gradient-to-r blur-sm",
                cardConfig[os].accent
            )} />

            {/* Animated glow ring */}
            <motion.div
                className="absolute -inset-[1px] rounded-3xl"
                animate={{
                    background: [
                        `linear-gradient(0deg, ${cardConfig[os].glow}, transparent)`,
                        `linear-gradient(180deg, ${cardConfig[os].glow}, transparent)`,
                        `linear-gradient(360deg, ${cardConfig[os].glow}, transparent)`
                    ]
                }}
                transition={{ duration: 3, repeat: Infinity }}
            />

            {/* Main card */}
            <div className={cn(
                "absolute inset-0 rounded-3xl",
                "bg-gradient-to-br",
                cardConfig[os].gradient,
                "border border-white/10",
                isSelected && "border-white/30"
            )}>
                {/* Glassmorphism overlay */}
                <div className="absolute inset-0 rounded-3xl bg-white/5 backdrop-blur-sm" />

                {/* Content */}
            </div>
        </motion.button>
    )
}
```

---

## ✨ Glow Effects & Premium Polish

### Glow Shadow Variables

```css
/* Purple glows (primary) */
--shadow-glow-purple: 0 0 20px rgba(168, 85, 247, 0.2);
--shadow-glow-purple-strong: 0 0 30px rgba(168, 85, 247, 0.35);
--shadow-glow-purple-intense: 0 0 40px rgba(168, 85, 247, 0.5);

/* Accent glows */
--shadow-glow-gold: 0 0 15px rgba(251, 191, 36, 0.25);
--shadow-glow-fire: 0 0 15px rgba(249, 115, 22, 0.25);
--shadow-glow-success: 0 0 20px rgba(34, 197, 94, 0.25);
--shadow-glow-info: 0 0 20px rgba(6, 182, 212, 0.25);
```

### Applying Glows

```tsx
// Static glow
<div className="shadow-[0_0_30px_rgba(168,85,247,0.3)]">
    Purple glow card
</div>

// Animated glow on hover
<motion.div
    whileHover={{
        boxShadow: "0 0 40px rgba(34, 197, 94, 0.4)"
    }}
>
    Success glow on hover
</motion.div>

// Pulsing glow animation
<div className="animate-glow">
    Breathing glow effect
</div>
```

### Ambient Background Glows

Create depth and atmosphere with positioned glow circles:

```tsx
{/* Large purple glow - top right */}
<div className="absolute top-0 right-0 w-[500px] h-[500px] bg-purple-500/15 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/4" />

{/* Mint glow - bottom left */}
<div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-emerald-500/10 rounded-full blur-[100px] translate-y-1/2 -translate-x-1/4" />

{/* Subtle blue center glow */}
<div className="absolute top-1/2 left-1/2 w-[300px] h-[300px] bg-blue-500/5 rounded-full blur-[80px] -translate-x-1/2 -translate-y-1/2" />
```

---

## 💻 Code Examples

### Complete Premium Card Component

```tsx
"use client"

import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { Sparkles } from "lucide-react"

interface PremiumCardProps {
    children: React.ReactNode
    className?: string
    glowColor?: "purple" | "gold" | "mint" | "orange"
}

export function PremiumCard({
    children,
    className,
    glowColor = "purple"
}: PremiumCardProps) {
    const glowStyles = {
        purple: "hover:shadow-[0_0_30px_rgba(168,85,247,0.2)]",
        gold: "hover:shadow-[0_0_30px_rgba(251,191,36,0.2)]",
        mint: "hover:shadow-[0_0_30px_rgba(34,197,94,0.2)]",
        orange: "hover:shadow-[0_0_30px_rgba(249,115,22,0.2)]"
    }

    const borderStyles = {
        purple: "border-purple-500/20 hover:border-purple-500/40",
        gold: "border-amber-500/20 hover:border-amber-500/40",
        mint: "border-emerald-500/20 hover:border-emerald-500/40",
        orange: "border-orange-500/20 hover:border-orange-500/40"
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            whileHover={{ y: -4 }}
            transition={{ type: "spring", stiffness: 100 }}
            className={cn(
                "relative group rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-zinc-900/90 to-zinc-800/50",
                "backdrop-blur-xl",
                "border transition-all duration-300",
                borderStyles[glowColor],
                glowStyles[glowColor],
                className
            )}
        >
            {/* Subtle inner gradient on hover */}
            <div className="absolute inset-0 bg-gradient-to-br from-purple-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

            {/* Floating sparkle decoration */}
            <motion.div
                className="absolute top-4 right-4 text-purple-400/30 opacity-0 group-hover:opacity-100 transition-opacity"
                animate={{ rotate: 360 }}
                transition={{ duration: 8, repeat: Infinity, ease: "linear" }}
            >
                <Sparkles className="w-4 h-4" />
            </motion.div>

            {/* Content */}
            <div className="relative z-10 p-6">
                {children}
            </div>
        </motion.div>
    )
}
```

### Complete Button Variants

```tsx
import { cva, type VariantProps } from "class-variance-authority"

const buttonVariants = cva(
    // Base styles
    "inline-flex items-center justify-center gap-2 rounded-xl font-semibold transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-zinc-900",
    {
        variants: {
            variant: {
                primary: [
                    "bg-gradient-to-r from-purple-600 to-purple-500",
                    "text-white",
                    "hover:from-purple-500 hover:to-purple-400",
                    "shadow-lg shadow-purple-500/25",
                    "hover:shadow-xl hover:shadow-purple-500/30",
                    "focus:ring-purple-500"
                ],
                success: [
                    "bg-gradient-to-r from-emerald-600 to-emerald-500",
                    "text-white",
                    "hover:from-emerald-500 hover:to-emerald-400",
                    "shadow-lg shadow-emerald-500/25",
                    "focus:ring-emerald-500"
                ],
                ghost: [
                    "bg-zinc-800/50",
                    "text-zinc-300",
                    "hover:bg-zinc-700/50",
                    "hover:text-white",
                    "border border-zinc-700/50",
                    "focus:ring-zinc-500"
                ],
                glow: [
                    "bg-gradient-to-r from-purple-600 to-pink-600",
                    "text-white",
                    "shadow-[0_0_20px_rgba(168,85,247,0.4)]",
                    "hover:shadow-[0_0_30px_rgba(168,85,247,0.6)]",
                    "focus:ring-purple-500"
                ]
            },
            size: {
                sm: "h-9 px-4 text-sm",
                md: "h-11 px-6 text-base",
                lg: "h-14 px-8 text-lg"
            }
        },
        defaultVariants: {
            variant: "primary",
            size: "md"
        }
    }
)
```

---

## 📁 File Structure

```
apps/frontend/src/
├── app/
│   ├── globals.css              # Main CSS entry point
│   └── (app)/
│       ├── dashboard/
│       │   └── page.tsx         # Premium dashboard
│       ├── progress/
│       │   └── page.tsx         # Progress tracking
│       ├── studyflow/
│       │   └── page.tsx         # Focus mode
│       ├── modules/
│       │   └── page.tsx         # Module listing
│       └── skillpath-board/
│           └── page.tsx         # Learning paths
│
├── styles/
│   ├── design-tokens.css        # Color, spacing, typography variables
│   └── animations.css           # Keyframes and animation utilities
│
├── components/
│   ├── ui/                      # Base UI components (shadcn/ui)
│   ├── onboarding/
│   │   └── PlatformSelector.tsx # OS selection
│   └── auth/                    # Authentication components
│
└── lib/
    └── utils.ts                 # cn() helper for classnames
```

### Key Files to Study

| File | Purpose | Learn About |
|------|---------|-------------|
| `design-tokens.css` | CSS custom properties | Color system, spacing, shadows |
| `animations.css` | Animation keyframes | Timing functions, effects |
| `tailwind.config.js` | Tailwind configuration | Extended theme, plugins |
| `globals.css` | Global styles | Component classes, utilities |
| `dashboard/page.tsx` | Premium page example | Glassmorphism, glows, motion |
| `PlatformSelector.tsx` | Interactive component | 3D effects, particles |

---

## 🎯 Design Checklist

When creating new components, ensure:

- [ ] **Dark mode first** — Use `bg-zinc-900` base, not white
- [ ] **Glow on focus states** — Add `shadow-glow-*` on hover/focus
- [ ] **Glassmorphism for elevated content** — `backdrop-blur-xl bg-zinc-900/60`
- [ ] **Purple accent for primary actions** — `border-purple-500/20`
- [ ] **Smooth transitions** — 200-300ms with ease-out
- [ ] **Staggered animations for lists** — Use Framer Motion variants
- [ ] **Ambient glows for depth** — Large blurred circles in background
- [ ] **Consistent spacing** — 4px base (p-1, p-2, p-4, p-6, p-8)
- [ ] **Responsive design** — Mobile-first with md: breakpoints

---

## 📚 Resources

### Design Inspiration

- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Vercel Design](https://vercel.com/design)
- [Linear App](https://linear.app)

### Documentation

- [Tailwind CSS v4](https://tailwindcss.com/docs)
- [Framer Motion](https://www.framer.com/motion/)
- [Radix UI](https://www.radix-ui.com/)

### Tools

- [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) — VS Code extension
- [Realtime Colors](https://www.realtimecolors.com/) — Color palette generator
- [Cubic Bezier](https://cubic-bezier.com/) — Easing curve visualizer

---

<div align="center">

**Built with ❤️ by Said Ebadi**

*DevOpsHub — Learn DevOps the modern way*

[🌐 Live Demo](https://saids-devopshub.netlify.app) • [📧 Contact](mailto:said.ebadi@hotmail.com) • [💼 Portfolio](https://github.com/S-Ebadi)

</div>
