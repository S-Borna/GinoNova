'use client';

/**
 * ============================================================================
 * APP INITIALIZER
 * ============================================================================
 *
 * Client-side initialization for error monitoring and analytics.
 * Wrapped in useEffect to run only on client mount.
 *
 * @phase A.8 - Testing & Launch Prep
 */

import { useEffect } from 'react';
import { initializeErrorMonitoring } from '@/lib/errorMonitoring';
import { initializeAnalytics } from '@/lib/analytics';

export function AppInitializer() {
  useEffect(() => {
    // Initialize error monitoring
    initializeErrorMonitoring();

    // Initialize analytics
    initializeAnalytics();
  }, []);

  // This component doesn't render anything
  return null;
}

export default AppInitializer;
