/**
 * ============================================================================
 * ANIMATIONS — Global Animation Variants for Framer Motion
 * ============================================================================
 *
 * Standardized animation variants used throughout the application.
 * Ensures consistent timing, easing, and motion across all components.
 *
 * @phase A.7 - Polish & Animations
 */

import { Variants } from 'framer-motion';

/* ============================================================================
   FADE ANIMATIONS
   ============================================================================ */

/**
 * Simple fade in/out
 */
export const fadeIn: Variants = {
  initial: { opacity: 0 },
  animate: { opacity: 1 },
  exit: { opacity: 0 },
};

/**
 * Fade in with delay
 */
export const fadeInDelayed: Variants = {
  initial: { opacity: 0 },
  animate: {
    opacity: 1,
    transition: { delay: 0.2, duration: 0.4 },
  },
  exit: { opacity: 0 },
};

/* ============================================================================
   SLIDE ANIMATIONS
   ============================================================================ */

/**
 * Slide up from bottom
 */
export const slideUp: Variants = {
  initial: { opacity: 0, y: 20 },
  animate: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.4, ease: [0.25, 0.46, 0.45, 0.94] },
  },
  exit: { opacity: 0, y: -20 },
};

/**
 * Slide down from top
 */
export const slideDown: Variants = {
  initial: { opacity: 0, y: -20 },
  animate: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.4, ease: [0.25, 0.46, 0.45, 0.94] },
  },
  exit: { opacity: 0, y: 20 },
};

/**
 * Slide in from left
 */
export const slideInLeft: Variants = {
  initial: { opacity: 0, x: -20 },
  animate: {
    opacity: 1,
    x: 0,
    transition: { duration: 0.4, ease: [0.25, 0.46, 0.45, 0.94] },
  },
  exit: { opacity: 0, x: -20 },
};

/**
 * Slide in from right
 */
export const slideInRight: Variants = {
  initial: { opacity: 0, x: 20 },
  animate: {
    opacity: 1,
    x: 0,
    transition: { duration: 0.4, ease: [0.25, 0.46, 0.45, 0.94] },
  },
  exit: { opacity: 0, x: 20 },
};

/* ============================================================================
   SCALE ANIMATIONS
   ============================================================================ */

/**
 * Scale in (grow from center)
 */
export const scaleIn: Variants = {
  initial: { opacity: 0, scale: 0.9 },
  animate: {
    opacity: 1,
    scale: 1,
    transition: { duration: 0.3, ease: [0.25, 0.46, 0.45, 0.94] },
  },
  exit: { opacity: 0, scale: 0.9 },
};

/**
 * Scale up (pop effect)
 */
export const scaleUp: Variants = {
  initial: { scale: 0.8, opacity: 0 },
  animate: {
    scale: 1,
    opacity: 1,
    transition: {
      type: 'spring',
      stiffness: 300,
      damping: 20,
    },
  },
  exit: { scale: 0.8, opacity: 0 },
};

/**
 * Scale bounce (spring effect)
 */
export const scaleBounce: Variants = {
  initial: { scale: 0 },
  animate: {
    scale: 1,
    transition: {
      type: 'spring',
      stiffness: 400,
      damping: 15,
    },
  },
  exit: { scale: 0 },
};

/* ============================================================================
   STAGGER ANIMATIONS
   ============================================================================ */

/**
 * Stagger children with 0.1s delay
 */
export const staggerChildren: Variants = {
  animate: {
    transition: {
      staggerChildren: 0.1,
    },
  },
};

/**
 * Stagger children with 0.05s delay (fast)
 */
export const staggerChildrenFast: Variants = {
  animate: {
    transition: {
      staggerChildren: 0.05,
    },
  },
};

/**
 * Stagger children with 0.15s delay (slow)
 */
export const staggerChildrenSlow: Variants = {
  animate: {
    transition: {
      staggerChildren: 0.15,
    },
  },
};

/* ============================================================================
   HOVER ANIMATIONS
   ============================================================================ */

/**
 * Lift on hover (cards, buttons)
 */
export const lift = {
  rest: { y: 0, scale: 1 },
  hover: {
    y: -4,
    scale: 1.02,
    transition: { duration: 0.2, ease: 'easeOut' },
  },
  tap: { scale: 0.98 },
};

/**
 * Glow on hover
 */
export const glow = {
  rest: { boxShadow: '0 0 0px rgba(0, 0, 0, 0)' },
  hover: {
    boxShadow: '0 0 20px rgba(59, 130, 246, 0.5)',
    transition: { duration: 0.3 },
  },
};

/**
 * Scale on hover (buttons, icons)
 */
export const scaleOnHover = {
  rest: { scale: 1 },
  hover: { scale: 1.05, transition: { duration: 0.2 } },
  tap: { scale: 0.95 },
};

/* ============================================================================
   PAGE TRANSITIONS
   ============================================================================ */

/**
 * Page fade transition
 */
export const pageTransition: Variants = {
  initial: { opacity: 0 },
  animate: {
    opacity: 1,
    transition: { duration: 0.3, ease: 'easeInOut' },
  },
  exit: {
    opacity: 0,
    transition: { duration: 0.2, ease: 'easeInOut' },
  },
};

/**
 * Page slide transition
 */
export const pageSlideTransition: Variants = {
  initial: { opacity: 0, x: -20 },
  animate: {
    opacity: 1,
    x: 0,
    transition: { duration: 0.4, ease: [0.25, 0.46, 0.45, 0.94] },
  },
  exit: {
    opacity: 0,
    x: 20,
    transition: { duration: 0.3, ease: [0.25, 0.46, 0.45, 0.94] },
  },
};

/* ============================================================================
   MODAL ANIMATIONS
   ============================================================================ */

/**
 * Modal backdrop fade
 */
export const modalBackdrop: Variants = {
  initial: { opacity: 0 },
  animate: { opacity: 1, transition: { duration: 0.2 } },
  exit: { opacity: 0, transition: { duration: 0.2 } },
};

/**
 * Modal content scale + fade
 */
export const modalContent: Variants = {
  initial: { opacity: 0, scale: 0.95, y: 20 },
  animate: {
    opacity: 1,
    scale: 1,
    y: 0,
    transition: {
      duration: 0.3,
      ease: [0.25, 0.46, 0.45, 0.94],
    },
  },
  exit: {
    opacity: 0,
    scale: 0.95,
    y: 20,
    transition: { duration: 0.2 },
  },
};

/* ============================================================================
   NOTIFICATION ANIMATIONS
   ============================================================================ */

/**
 * Toast slide in from top
 */
export const toastSlideDown: Variants = {
  initial: { opacity: 0, y: -50 },
  animate: {
    opacity: 1,
    y: 0,
    transition: {
      type: 'spring',
      stiffness: 400,
      damping: 25,
    },
  },
  exit: {
    opacity: 0,
    y: -50,
    transition: { duration: 0.2 },
  },
};

/**
 * Toast slide in from right
 */
export const toastSlideLeft: Variants = {
  initial: { opacity: 0, x: 100 },
  animate: {
    opacity: 1,
    x: 0,
    transition: {
      type: 'spring',
      stiffness: 400,
      damping: 25,
    },
  },
  exit: {
    opacity: 0,
    x: 100,
    transition: { duration: 0.2 },
  },
};

/* ============================================================================
   SPECIAL EFFECTS
   ============================================================================ */

/**
 * Shake animation (for errors)
 */
export const shake: Variants = {
  initial: { x: 0 },
  animate: {
    x: [0, -10, 10, -10, 10, 0],
    transition: { duration: 0.5 },
  },
};

/**
 * Pulse animation (for highlights)
 */
export const pulse: Variants = {
  initial: { scale: 1 },
  animate: {
    scale: [1, 1.05, 1],
    transition: {
      duration: 2,
      repeat: Infinity,
      ease: 'easeInOut',
    },
  },
};

/**
 * Bounce animation (for celebrations)
 */
export const bounce: Variants = {
  initial: { y: 0 },
  animate: {
    y: [0, -20, 0],
    transition: {
      duration: 0.6,
      repeat: Infinity,
      ease: 'easeInOut',
    },
  },
};

/**
 * Rotate animation (for loading)
 */
export const rotate: Variants = {
  initial: { rotate: 0 },
  animate: {
    rotate: 360,
    transition: {
      duration: 1,
      repeat: Infinity,
      ease: 'linear',
    },
  },
};

/* ============================================================================
   LIST ITEM ANIMATIONS
   ============================================================================ */

/**
 * List item fade up
 */
export const listItem: Variants = {
  hidden: { opacity: 0, y: 10 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.3, ease: [0.25, 0.46, 0.45, 0.94] },
  },
};

/**
 * List container with stagger
 */
export const listContainer: Variants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.08,
      delayChildren: 0.1,
    },
  },
};

/* ============================================================================
   ACCORDION ANIMATIONS
   ============================================================================ */

/**
 * Accordion expand/collapse
 */
export const accordionContent: Variants = {
  collapsed: { height: 0, opacity: 0 },
  expanded: {
    height: 'auto',
    opacity: 1,
    transition: { duration: 0.3, ease: [0.25, 0.46, 0.45, 0.94] },
  },
};

/* ============================================================================
   CUSTOM EASING CURVES
   ============================================================================ */

/**
 * Smooth ease for general use
 */
export const easeSmooth = [0.25, 0.46, 0.45, 0.94];

/**
 * Bounce ease for playful interactions
 */
export const easeBounce = [0.68, -0.55, 0.265, 1.55];

/**
 * Sharp ease for quick transitions
 */
export const easeSharp = [0.4, 0, 0.6, 1];

/* ============================================================================
   UTILITIES
   ============================================================================ */

/**
 * Create a delay for staggered animations
 */
export const createDelay = (index: number, baseDelay = 0.05) => ({
  transition: { delay: index * baseDelay },
});

/**
 * Create spring transition
 */
export const springTransition = {
  type: 'spring' as const,
  stiffness: 400,
  damping: 25,
};

/**
 * Create smooth transition
 */
export const smoothTransition = {
  duration: 0.3,
  ease: easeSmooth,
};

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default {
  fadeIn,
  fadeInDelayed,
  slideUp,
  slideDown,
  slideInLeft,
  slideInRight,
  scaleIn,
  scaleUp,
  scaleBounce,
  staggerChildren,
  staggerChildrenFast,
  staggerChildrenSlow,
  lift,
  glow,
  scaleOnHover,
  pageTransition,
  pageSlideTransition,
  modalBackdrop,
  modalContent,
  toastSlideDown,
  toastSlideLeft,
  shake,
  pulse,
  bounce,
  rotate,
  listItem,
  listContainer,
  accordionContent,
};
