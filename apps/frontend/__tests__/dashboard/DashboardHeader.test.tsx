/**
 * DashboardHeader Component Tests
 * Phase 6.5: Dashboard Tests
 */

import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { DashboardHeader } from '@/components/dashboard/DashboardHeader';
import type { DashboardUser } from '@/lib/dashboard';

// ============================================================================
// MOCK DATA
// ============================================================================

const mockUser: DashboardUser = {
  id: 'user-1',
  email: 'test@example.com',
  full_name: 'Test User',
  is_active: true,
  is_admin: false,
  created_at: '2025-01-01T00:00:00Z',
};

const mockUserNoName: DashboardUser = {
  id: 'user-2',
  email: 'nofullname@example.com',
  full_name: null,
  is_active: true,
  is_admin: false,
  created_at: '2025-01-01T00:00:00Z',
};

// ============================================================================
// TESTS
// ============================================================================

describe('DashboardHeader', () => {
  describe('User Display', () => {
    it('renders user full name in greeting', () => {
      render(<DashboardHeader user={mockUser} />);
      
      expect(screen.getByText(/Welcome back, Test User!/i)).toBeInTheDocument();
    });

    it('renders email when full name is null', () => {
      render(<DashboardHeader user={mockUserNoName} />);
      
      // Should extract name from email
      expect(screen.getByText(/Welcome back, nofullname!/i)).toBeInTheDocument();
    });

    it('renders "Learner" when user is null', () => {
      render(<DashboardHeader user={null} />);
      
      expect(screen.getByText(/Welcome back, Learner!/i)).toBeInTheDocument();
    });

    it('displays user email below name', () => {
      render(<DashboardHeader user={mockUser} />);
      
      expect(screen.getByText('test@example.com')).toBeInTheDocument();
    });

    it('displays first letter as avatar', () => {
      render(<DashboardHeader user={mockUser} />);
      
      // Avatar should show "T" for "Test User"
      expect(screen.getByText('T')).toBeInTheDocument();
    });
  });

  describe('Level System', () => {
    it('displays default level 1 with 0 XP', () => {
      render(<DashboardHeader user={mockUser} currentXP={0} />);
      
      // Should show Level 1
      expect(screen.getByText('Level 1')).toBeInTheDocument();
    });

    it('displays correct level based on XP', () => {
      render(<DashboardHeader user={mockUser} currentXP={2500} />);
      
      // 2500 XP = Level 3 (floor(2500/1000) + 1)
      expect(screen.getByText('Level 3')).toBeInTheDocument();
    });

    it('accepts explicit level prop', () => {
      render(<DashboardHeader user={mockUser} level={5} currentXP={500} />);
      
      // Explicit level should override calculated
      expect(screen.getByText('Level 5')).toBeInTheDocument();
    });
  });

  describe('XP Progress', () => {
    it('displays Total XP', () => {
      render(<DashboardHeader user={mockUser} currentXP={1500} />);
      
      expect(screen.getByText('1500')).toBeInTheDocument();
      expect(screen.getByText('Total XP')).toBeInTheDocument();
    });

    it('displays current level in stats', () => {
      render(<DashboardHeader user={mockUser} level={3} currentXP={1500} />);
      
      // Level shown twice: badge and stats
      const level3Elements = screen.getAllByText('3');
      expect(level3Elements.length).toBeGreaterThanOrEqual(1);
    });

    it('displays XP to next level', () => {
      render(<DashboardHeader user={mockUser} currentXP={1500} />);
      
      // 1500 XP: current in level = 500, to next = 1000 - 500 = 500
      expect(screen.getByText('XP to Next')).toBeInTheDocument();
      expect(screen.getByText('500')).toBeInTheDocument();
    });

    it('shows XP progress bar label', () => {
      render(<DashboardHeader user={mockUser} currentXP={500} />);
      
      expect(screen.getByText('XP Progress')).toBeInTheDocument();
      // Progress text: 500 / 1000
      expect(screen.getByText('500 / 1000')).toBeInTheDocument();
    });
  });

  describe('Custom XP to Next Level', () => {
    it('accepts custom xpToNextLevel prop', () => {
      render(
        <DashboardHeader 
          user={mockUser} 
          currentXP={300} 
          xpToNextLevel={500} 
        />
      );
      
      // Should show 300 / 500 (custom)
      expect(screen.getByText('300 / 500')).toBeInTheDocument();
    });
  });
});
