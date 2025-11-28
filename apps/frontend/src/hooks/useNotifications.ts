'use client';

import { useEffect, useCallback, useState, useRef } from 'react';

type NotificationType = 'focus-start' | 'focus-end' | 'break-start' | 'break-end' | 'session-complete';

interface NotificationConfig {
  title: string;
  body: string;
  icon?: string;
  sound?: string;
}

const NOTIFICATION_CONFIGS: Record<NotificationType, NotificationConfig> = {
  'focus-start': {
    title: 'Focus Time Started',
    body: 'Time to concentrate. You got this! 💪',
    sound: '/sounds/focus-start.mp3',
  },
  'focus-end': {
    title: 'Focus Time Complete',
    body: 'Great work! Time for a break. 🎉',
    sound: '/sounds/break-time.mp3',
  },
  'break-start': {
    title: 'Break Time',
    body: 'Relax, stretch, and recharge. ☕',
    sound: '/sounds/break-start.mp3',
  },
  'break-end': {
    title: 'Break Over',
    body: 'Ready to focus again? Let\'s go! 🚀',
    sound: '/sounds/focus-start.mp3',
  },
  'session-complete': {
    title: 'Session Complete!',
    body: 'Amazing work today! Check your stats. 🏆',
    sound: '/sounds/session-complete.mp3',
  },
};

// Storage key for preferences
const STORAGE_KEY = 'studyflow-notifications';

interface NotificationPreferences {
  browserEnabled: boolean;
  soundEnabled: boolean;
  volume: number;
}

const DEFAULT_PREFERENCES: NotificationPreferences = {
  browserEnabled: true,
  soundEnabled: true,
  volume: 0.5,
};

export function useNotifications() {
  const [permission, setPermission] = useState<NotificationPermission>('default');
  const [preferences, setPreferences] = useState<NotificationPreferences>(DEFAULT_PREFERENCES);
  const audioRef = useRef<HTMLAudioElement | null>(null);

  // Load preferences from localStorage
  useEffect(() => {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored) {
        setPreferences({ ...DEFAULT_PREFERENCES, ...JSON.parse(stored) });
      }
    } catch {
      console.warn('Failed to load notification preferences');
    }
  }, []);

  // Save preferences to localStorage
  const savePreferences = useCallback((newPrefs: Partial<NotificationPreferences>) => {
    const updated = { ...preferences, ...newPrefs };
    setPreferences(updated);
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));
    } catch {
      console.warn('Failed to save notification preferences');
    }
  }, [preferences]);

  // Check and request permission
  useEffect(() => {
    if (typeof window !== 'undefined' && 'Notification' in window) {
      setPermission(Notification.permission);
    }
  }, []);

  // Request permission
  const requestPermission = useCallback(async () => {
    if (typeof window === 'undefined' || !('Notification' in window)) {
      return 'denied' as NotificationPermission;
    }

    if (Notification.permission === 'granted') {
      setPermission('granted');
      return 'granted';
    }

    if (Notification.permission !== 'denied') {
      const result = await Notification.requestPermission();
      setPermission(result);
      return result;
    }

    return Notification.permission;
  }, []);

  // Play sound
  const playSound = useCallback((soundUrl: string) => {
    if (!preferences.soundEnabled) return;

    try {
      // Create audio element if not exists
      if (!audioRef.current) {
        audioRef.current = new Audio();
      }
      
      audioRef.current.src = soundUrl;
      audioRef.current.volume = preferences.volume;
      audioRef.current.play().catch(() => {
        // Ignore autoplay restrictions
        console.warn('Sound playback blocked by browser');
      });
    } catch {
      console.warn('Failed to play notification sound');
    }
  }, [preferences.soundEnabled, preferences.volume]);

  // Send notification
  const notify = useCallback((type: NotificationType) => {
    const config = NOTIFICATION_CONFIGS[type];

    // Play sound
    if (config.sound && preferences.soundEnabled) {
      playSound(config.sound);
    }

    // Browser notification
    if (preferences.browserEnabled && permission === 'granted') {
      try {
        new Notification(config.title, {
          body: config.body,
          icon: config.icon || '/icon-192.png',
          tag: `studyflow-${type}`,
        });
      } catch {
        console.warn('Failed to show browser notification');
      }
    }
  }, [permission, preferences.browserEnabled, preferences.soundEnabled, playSound]);

  // Toggle sound
  const toggleSound = useCallback(() => {
    savePreferences({ soundEnabled: !preferences.soundEnabled });
  }, [preferences.soundEnabled, savePreferences]);

  // Toggle browser notifications
  const toggleBrowserNotifications = useCallback(async () => {
    if (!preferences.browserEnabled) {
      // Turning on - request permission if needed
      const perm = await requestPermission();
      if (perm === 'granted') {
        savePreferences({ browserEnabled: true });
      }
    } else {
      // Turning off
      savePreferences({ browserEnabled: false });
    }
  }, [preferences.browserEnabled, requestPermission, savePreferences]);

  // Set volume
  const setVolume = useCallback((volume: number) => {
    savePreferences({ volume: Math.max(0, Math.min(1, volume)) });
  }, [savePreferences]);

  // Test notification
  const testNotification = useCallback(() => {
    notify('focus-start');
  }, [notify]);

  return {
    permission,
    preferences,
    requestPermission,
    notify,
    toggleSound,
    toggleBrowserNotifications,
    setVolume,
    testNotification,
    isSupported: typeof window !== 'undefined' && 'Notification' in window,
  };
}

export default useNotifications;
