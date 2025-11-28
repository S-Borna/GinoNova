'use client';

/**
 * ============================================================================
 * PAGE TRANSITION — Smooth Page Enter/Exit Animations
 * ============================================================================
 *
 * Wrapper component for smooth page transitions with Framer Motion.
 *
 * Features:
 * - Fade in on enter
 * - Optional slide variants
 * - Customizable duration
 * - Maintains scroll position
 *
 * @phase A.7 - Polish & Animations
 */

import { motion, AnimatePresence, type Variants } from 'framer-motion';
import { usePathname } from 'next/navigation';
import { ReactNode } from 'react';

/* ============================================================================
   TYPES
   ============================================================================ */

export type TransitionVariant = 'fade' | 'slideUp' | 'slideLeft' | 'scale' | 'none';

export interface PageTransitionProps {
  children: ReactNode;
  variant?: TransitionVariant;
  duration?: number;
  delay?: number;
  className?: string;
}

/* ============================================================================
   ANIMATION VARIANTS
   ============================================================================ */

const variants: Record<TransitionVariant, Variants> = {
  fade: {
    initial: { opacity: 0 },
    animate: { opacity: 1 },
    exit: { opacity: 0 },
  },
  slideUp: {
    initial: { opacity: 0, y: 20 },
    animate: { opacity: 1, y: 0 },
    exit: { opacity: 0, y: -10 },
  },
  slideLeft: {
    initial: { opacity: 0, x: 20 },
    animate: { opacity: 1, x: 0 },
    exit: { opacity: 0, x: -10 },
  },
  scale: {
    initial: { opacity: 0, scale: 0.98 },
    animate: { opacity: 1, scale: 1 },
    exit: { opacity: 0, scale: 0.98 },
  },
  none: {
    initial: {},
    animate: {},
    exit: {},
  },
};

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function PageTransition({
  children,
  variant = 'fade',
  duration = 0.3,
  delay = 0,
  className = '',
}: PageTransitionProps) {
  const pathname = usePathname();

  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={pathname}
        initial="initial"
        animate="animate"
        exit="exit"
        variants={variants[variant]}
        transition={{
          duration,
          delay,
          ease: [0.25, 0.46, 0.45, 0.94], // easeOutQuad
        }}
        className={className}
      >
        {children}
      </motion.div>
    </AnimatePresence>
  );
}

/* ============================================================================
   STAGGER CHILDREN WRAPPER
   ============================================================================ */

const staggerContainer: Variants = {
  initial: {},
  animate: {
    transition: {
      staggerChildren: 0.1,
      delayChildren: 0.1,
    },
  },
};

const staggerItem: Variants = {
  initial: { opacity: 0, y: 20 },
  animate: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.4,
      ease: [0.25, 0.46, 0.45, 0.94],
    },
  },
};

export function StaggerContainer({
  children,
  className = '',
}: {
  children: ReactNode;
  className?: string;
}) {
  return (
    <motion.div
      initial="initial"
      animate="animate"
      variants={staggerContainer}
      className={className}
    >
      {children}
    </motion.div>
  );
}

export function StaggerItem({
  children,
  className = '',
}: {
  children: ReactNode;
  className?: string;
}) {
  return (
    <motion.div variants={staggerItem} className={className}>
      {children}
    </motion.div>
  );
}

/* ============================================================================
   FADE IN SECTION
   ============================================================================ */

export function FadeInSection({
  children,
  delay = 0,
  className = '',
}: {
  children: ReactNode;
  delay?: number;
  className?: string;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{
        duration: 0.5,
        delay,
        ease: [0.25, 0.46, 0.45, 0.94],
      }}
      className={className}
    >
      {children}
    </motion.div>
  );
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default PageTransition;
