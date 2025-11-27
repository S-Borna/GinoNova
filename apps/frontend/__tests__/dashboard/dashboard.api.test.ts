/**
 * Dashboard API Client Tests
 * Phase 6.5: Dashboard Tests
 */

import '@testing-library/jest-dom';
import { getDashboardSummary, getDashboardStatus } from '@/lib/dashboard';
import type { DashboardSummary } from '@/lib/dashboard';

// ============================================================================
// MOCK DATA
// ============================================================================

const mockSummary: DashboardSummary = {
  user: {
    id: 'user-1',
    email: 'test@example.com',
    full_name: 'Test User',
    is_active: true,
    is_admin: false,
    created_at: '2025-01-01T00:00:00Z',
  },
  modules: [
    { id: 'module-1', name: 'DevOps Fundamentals', description: 'Learn DevOps', is_active: true },
  ],
  tasks: [
    { id: 'task-1', module_id: 'module-1', title: 'Setup Docker', difficulty: 'easy', is_active: true },
  ],
  studyflow: [
    { id: 'study-1', module_id: 'module-1', title: 'Docker Basics', order: 1, is_active: true },
  ],
  progress: [
    { id: 'progress-1', user_id: 'user-1', module_id: 'module-1', task_id: null, studyflow_id: null, status: 'in_progress', progress: 50 },
  ],
  system: {
    service: 'devops-hub',
    version: '1.0.0',
    environment: 'test',
  },
  version: {
    api_version: '1.0.0',
    phase: '6.0',
  },
  stats: {
    total_modules: 10,
    total_tasks: 50,
    total_studyflows: 20,
    total_progress_records: 5,
    active_modules: 8,
    active_tasks: 40,
  },
};

const mockStatus = {
  phase: '6.0',
  feature: 'dashboard',
  status: 'active',
};

// ============================================================================
// TESTS
// ============================================================================

describe('Dashboard API Client', () => {
  // Store original fetch
  const originalFetch = global.fetch;

  beforeEach(() => {
    // Reset fetch mock before each test
    jest.resetAllMocks();
  });

  afterAll(() => {
    // Restore original fetch
    global.fetch = originalFetch;
  });

  describe('getDashboardSummary', () => {
    it('returns success result on successful fetch', async () => {
      global.fetch = jest.fn().mockResolvedValueOnce({
        ok: true,
        json: async () => mockSummary,
      });

      const result = await getDashboardSummary();

      expect(result.ok).toBe(true);
      if (result.ok) {
        expect(result.data.user?.email).toBe('test@example.com');
        expect(result.data.modules.length).toBe(1);
        expect(result.data.stats.total_modules).toBe(10);
      }
    });

    it('calls correct URL without user ID', async () => {
      global.fetch = jest.fn().mockResolvedValueOnce({
        ok: true,
        json: async () => mockSummary,
      });

      await getDashboardSummary();

      expect(global.fetch).toHaveBeenCalledWith(
        'http://localhost:8000/api/dashboard/summary',
        expect.objectContaining({
          method: 'GET',
          headers: { 'Content-Type': 'application/json' },
        })
      );
    });

    it('calls correct URL with user ID', async () => {
      global.fetch = jest.fn().mockResolvedValueOnce({
        ok: true,
        json: async () => mockSummary,
      });

      await getDashboardSummary('user-123');

      expect(global.fetch).toHaveBeenCalledWith(
        'http://localhost:8000/api/dashboard/summary?user_id=user-123',
        expect.any(Object)
      );
    });

    it('returns error result on HTTP error', async () => {
      global.fetch = jest.fn().mockResolvedValueOnce({
        ok: false,
        status: 404,
        json: async () => ({ detail: 'Not found' }),
      });

      const result = await getDashboardSummary();

      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.status).toBe(404);
        expect(result.message).toBe('Not found');
      }
    });

    it('returns error result with default message when detail missing', async () => {
      global.fetch = jest.fn().mockResolvedValueOnce({
        ok: false,
        status: 500,
        json: async () => ({}),
      });

      const result = await getDashboardSummary();

      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.message).toBe('Failed to fetch dashboard');
      }
    });

    it('handles network errors gracefully', async () => {
      global.fetch = jest.fn().mockRejectedValueOnce(new Error('Network error'));

      const result = await getDashboardSummary();

      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.status).toBe(0);
        expect(result.message).toBe('Network error');
      }
    });

    it('handles non-Error exceptions', async () => {
      global.fetch = jest.fn().mockRejectedValueOnce('Unknown error');

      const result = await getDashboardSummary();

      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.message).toBe('Network error');
      }
    });

    it('handles JSON parse errors in error response', async () => {
      global.fetch = jest.fn().mockResolvedValueOnce({
        ok: false,
        status: 500,
        json: async () => { throw new Error('Invalid JSON'); },
      });

      const result = await getDashboardSummary();

      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.message).toBe('Failed to fetch dashboard');
      }
    });
  });

  describe('getDashboardStatus', () => {
    it('returns success result on successful fetch', async () => {
      global.fetch = jest.fn().mockResolvedValueOnce({
        ok: true,
        json: async () => mockStatus,
      });

      const result = await getDashboardStatus();

      expect(result.ok).toBe(true);
      if (result.ok) {
        expect(result.data.phase).toBe('6.0');
        expect(result.data.feature).toBe('dashboard');
        expect(result.data.status).toBe('active');
      }
    });

    it('calls correct URL', async () => {
      global.fetch = jest.fn().mockResolvedValueOnce({
        ok: true,
        json: async () => mockStatus,
      });

      await getDashboardStatus();

      expect(global.fetch).toHaveBeenCalledWith(
        'http://localhost:8000/api/dashboard/status',
        expect.objectContaining({
          method: 'GET',
          headers: { 'Content-Type': 'application/json' },
        })
      );
    });

    it('returns error result on HTTP error', async () => {
      global.fetch = jest.fn().mockResolvedValueOnce({
        ok: false,
        status: 503,
        json: async () => ({ detail: 'Service unavailable' }),
      });

      const result = await getDashboardStatus();

      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.status).toBe(503);
        expect(result.message).toBe('Service unavailable');
      }
    });

    it('handles network errors gracefully', async () => {
      global.fetch = jest.fn().mockRejectedValueOnce(new Error('Connection refused'));

      const result = await getDashboardStatus();

      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.status).toBe(0);
        expect(result.message).toBe('Connection refused');
      }
    });

    it('returns default message when detail missing', async () => {
      global.fetch = jest.fn().mockResolvedValueOnce({
        ok: false,
        status: 500,
        json: async () => ({}),
      });

      const result = await getDashboardStatus();

      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.message).toBe('Failed to fetch status');
      }
    });
  });
});
