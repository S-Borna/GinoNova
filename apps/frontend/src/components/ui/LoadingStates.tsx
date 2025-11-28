'use client';

/**
 * ============================================================================
 * LOADING STATES — Various Loading Indicators
 * ============================================================================
 *
 * Loading components for different scenarios:
 * - Full page loader
 * - Inline spinners
 * - Dots loader
 * - Progress loader
 *
 * @phase A.7 - Polish & Animations
 */

import { motion } from 'framer-motion';
import { Loader2 } from 'lucide-react';
import { cn } from '@/lib/utils';

/* ============================================================================
   SPINNER LOADER
   ============================================================================ */

export interface SpinnerProps {
  size?: 'sm' | 'md' | 'lg' | 'xl';
  className?: string;
}

const spinnerSizes = {
  sm: 'w-4 h-4',
  md: 'w-6 h-6',
  lg: 'w-8 h-8',
  xl: 'w-12 h-12',
};

export function Spinner({ size = 'md', className }: SpinnerProps) {
  return (
    <Loader2
      className={cn(
        'animate-spin text-primary',
        spinnerSizes[size],
        className
      )}
    />
  );
}

/* ============================================================================
   DOTS LOADER
   ============================================================================ */

export interface DotsLoaderProps {
  size?: 'sm' | 'md' | 'lg';
  className?: string;
}

const dotSizes = {
  sm: 'w-1.5 h-1.5',
  md: 'w-2 h-2',
  lg: 'w-3 h-3',
};

export function DotsLoader({ size = 'md', className }: DotsLoaderProps) {
  return (
    <div className={cn('flex items-center gap-1', className)}>
      {[0, 1, 2].map((i) => (
        <motion.div
          key={i}
          className={cn('rounded-full bg-primary', dotSizes[size])}
          animate={{
            y: [0, -6, 0],
            opacity: [0.5, 1, 0.5],
          }}
          transition={{
            duration: 0.6,
            repeat: Infinity,
            delay: i * 0.15,
            ease: 'easeInOut',
          }}
        />
      ))}
    </div>
  );
}

/* ============================================================================
   PULSE LOADER
   ============================================================================ */

export interface PulseLoaderProps {
  size?: 'sm' | 'md' | 'lg';
  className?: string;
}

const pulseSizes = {
  sm: 'w-8 h-8',
  md: 'w-12 h-12',
  lg: 'w-16 h-16',
};

export function PulseLoader({ size = 'md', className }: PulseLoaderProps) {
  return (
    <div className={cn('relative', pulseSizes[size], className)}>
      <motion.div
        className="absolute inset-0 rounded-full bg-primary/30"
        animate={{
          scale: [1, 1.5, 1],
          opacity: [0.5, 0, 0.5],
        }}
        transition={{
          duration: 1.5,
          repeat: Infinity,
          ease: 'easeInOut',
        }}
      />
      <motion.div
        className="absolute inset-0 rounded-full bg-primary/50"
        animate={{
          scale: [1, 1.3, 1],
          opacity: [0.7, 0, 0.7],
        }}
        transition={{
          duration: 1.5,
          repeat: Infinity,
          ease: 'easeInOut',
          delay: 0.2,
        }}
      />
      <div className="absolute inset-2 rounded-full bg-primary" />
    </div>
  );
}

/* ============================================================================
   FULL PAGE LOADER
   ============================================================================ */

export interface FullPageLoaderProps {
  message?: string;
  showLogo?: boolean;
}

export function FullPageLoader({
  message = 'Loading...',
  showLogo = true,
}: FullPageLoaderProps) {
  return (
    <div className="fixed inset-0 z-50 flex flex-col items-center justify-center bg-background">
      {/* Logo */}
      {showLogo && (
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          className="mb-8"
        >
          <div className="text-3xl font-bold">
            <span className="bg-gradient-to-r from-primary to-purple-500 bg-clip-text text-transparent">
              DevOps
            </span>
            <span className="text-foreground">Hub</span>
          </div>
        </motion.div>
      )}

      {/* Loading Animation */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
        className="flex flex-col items-center gap-4"
      >
        <div className="relative">
          {/* Outer ring */}
          <motion.div
            className="w-16 h-16 rounded-full border-2 border-primary/20"
            animate={{ rotate: 360 }}
            transition={{
              duration: 2,
              repeat: Infinity,
              ease: 'linear',
            }}
          />
          {/* Inner spinning arc */}
          <motion.div
            className="absolute inset-0 w-16 h-16 rounded-full border-2 border-transparent border-t-primary"
            animate={{ rotate: 360 }}
            transition={{
              duration: 1,
              repeat: Infinity,
              ease: 'linear',
            }}
          />
        </div>

        {/* Message */}
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.4 }}
          className="text-sm text-muted-foreground"
        >
          {message}
        </motion.p>
      </motion.div>
    </div>
  );
}

/* ============================================================================
   INLINE LOADER
   ============================================================================ */

export interface InlineLoaderProps {
  text?: string;
  className?: string;
}

export function InlineLoader({ text, className }: InlineLoaderProps) {
  return (
    <div className={cn('flex items-center gap-2', className)}>
      <Spinner size="sm" />
      {text && (
        <span className="text-sm text-muted-foreground">{text}</span>
      )}
    </div>
  );
}

/* ============================================================================
   BUTTON LOADING STATE
   ============================================================================ */

export interface ButtonLoaderProps {
  className?: string;
}

export function ButtonLoader({ className }: ButtonLoaderProps) {
  return (
    <Loader2 className={cn('w-4 h-4 animate-spin', className)} />
  );
}

/* ============================================================================
   SKELETON PULSE
   ============================================================================ */

export function SkeletonPulse({
  className,
  children,
}: {
  className?: string;
  children?: React.ReactNode;
}) {
  return (
    <div className={cn('relative overflow-hidden', className)}>
      {children}
      <motion.div
        className="absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent"
        animate={{
          x: ['-100%', '100%'],
        }}
        transition={{
          duration: 1.5,
          repeat: Infinity,
          ease: 'easeInOut',
        }}
      />
    </div>
  );
}

/* ============================================================================
   PROGRESS LOADER (Linear)
   ============================================================================ */

export interface ProgressLoaderProps {
  progress?: number;
  indeterminate?: boolean;
  className?: string;
}

export function ProgressLoader({
  progress = 0,
  indeterminate = false,
  className,
}: ProgressLoaderProps) {
  return (
    <div
      className={cn(
        'h-1 w-full overflow-hidden rounded-full bg-primary/20',
        className
      )}
    >
      {indeterminate ? (
        <motion.div
          className="h-full w-1/3 bg-primary rounded-full"
          animate={{
            x: ['-100%', '400%'],
          }}
          transition={{
            duration: 1.5,
            repeat: Infinity,
            ease: 'easeInOut',
          }}
        />
      ) : (
        <motion.div
          className="h-full bg-primary rounded-full"
          initial={{ width: 0 }}
          animate={{ width: `${progress}%` }}
          transition={{ duration: 0.3 }}
        />
      )}
    </div>
  );
}

/* ============================================================================
   CONTENT LOADER (with placeholder)
   ============================================================================ */

export function ContentLoader({
  isLoading,
  children,
  fallback,
}: {
  isLoading: boolean;
  children: React.ReactNode;
  fallback?: React.ReactNode;
}) {
  if (isLoading) {
    return (
      fallback || (
        <div className="flex items-center justify-center py-12">
          <Spinner size="lg" />
        </div>
      )
    );
  }
  return <>{children}</>;
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default Spinner;
