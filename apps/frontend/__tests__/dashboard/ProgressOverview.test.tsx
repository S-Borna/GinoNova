/**
 * ProgressOverview Component Tests
 * Phase 6.5: Dashboard Tests
 */

import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProgressOverview } from '@/components/dashboard/ProgressOverview';
import type { DashboardStats } from '@/lib/dashboard';

// ============================================================================
// MOCK DATA
// ============================================================================

const mockStats: DashboardStats = {
    total_modules: 10,
    total_tasks: 50,
    total_studyflows: 20,
    total_progress_records: 5,
    active_modules: 8,
    active_tasks: 40,
};

const emptyStats: DashboardStats = {
    total_modules: 0,
    total_tasks: 0,
    total_studyflows: 0,
    total_progress_records: 0,
    active_modules: 0,
    active_tasks: 0,
};

// ============================================================================
// TESTS
// ============================================================================

describe('ProgressOverview', () => {
    describe('Rendering', () => {
        it('renders the component title', () => {
            render(<ProgressOverview stats={mockStats} />);

            expect(screen.getByText('Bootcamp Progress')).toBeInTheDocument();
        });

        it('renders progress emoji icon', () => {
            render(<ProgressOverview stats={mockStats} />);

            expect(screen.getByText('📊')).toBeInTheDocument();
        });
    });

    describe('Progress Calculation', () => {
        it('displays 0% with no completed modules or tasks', () => {
            render(<ProgressOverview stats={mockStats} completedModules={0} completedTasks={0} />);

            // Overall progress should be 0%
            expect(screen.getByText('0%')).toBeInTheDocument();
        });

        it('calculates correct percentage with completed modules', () => {
            render(
                <ProgressOverview
                    stats={mockStats}
                    completedModules={5}
                    completedTasks={25}
                />
            );

            // Module progress: 5/10 = 50%
            // Task progress: 25/50 = 50%
            // Overall: (50 + 50) / 2 = 50%
            expect(screen.getByText('50%')).toBeInTheDocument();
        });

        it('handles 100% completion', () => {
            render(
                <ProgressOverview
                    stats={mockStats}
                    completedModules={10}
                    completedTasks={50}
                />
            );

            // Should show 100% and completion message
            expect(screen.getByText('100%')).toBeInTheDocument();
            expect(screen.getByText('Complete! 🎉')).toBeInTheDocument();
        });

        it('handles empty stats gracefully', () => {
            render(<ProgressOverview stats={emptyStats} />);

            // Should show 0% without errors
            expect(screen.getByText('0%')).toBeInTheDocument();
        });
    });

    describe('Progress Labels', () => {
        it('shows "Just started" at low progress', () => {
            render(
                <ProgressOverview
                    stats={mockStats}
                    completedModules={1}
                    completedTasks={5}
                />
            );

            // Module: 1/10 = 10%, Task: 5/50 = 10%, Overall = 10%
            expect(screen.getByText('Just started')).toBeInTheDocument();
        });

        it('shows "Keep going!" at 25% progress', () => {
            render(
                <ProgressOverview
                    stats={mockStats}
                    completedModules={2}
                    completedTasks={15}
                />
            );

            // Module: 2/10 = 20%, Task: 15/50 = 30%, Overall = 25%
            expect(screen.getByText('Keep going!')).toBeInTheDocument();
        });

        it('shows "Great progress!" at 50% progress', () => {
            render(
                <ProgressOverview
                    stats={mockStats}
                    completedModules={5}
                    completedTasks={25}
                />
            );

            expect(screen.getByText('Great progress!')).toBeInTheDocument();
        });

        it('shows "Almost there!" at 80% progress', () => {
            render(
                <ProgressOverview
                    stats={mockStats}
                    completedModules={8}
                    completedTasks={40}
                />
            );

            expect(screen.getByText('Almost there!')).toBeInTheDocument();
        });
    });

    describe('Stats Display', () => {
        it('displays module progress fraction', () => {
            render(
                <ProgressOverview
                    stats={mockStats}
                    completedModules={3}
                    completedTasks={0}
                />
            );

            // Should show "3 / 10" for modules
            expect(screen.getByText('3 / 10')).toBeInTheDocument();
        });

        it('displays task progress fraction', () => {
            render(
                <ProgressOverview
                    stats={mockStats}
                    completedModules={0}
                    completedTasks={15}
                />
            );

            // Should show "15 / 50" for tasks
            expect(screen.getByText('15 / 50')).toBeInTheDocument();
        });

        it('displays active modules count', () => {
            render(<ProgressOverview stats={mockStats} />);

            expect(screen.getByText('8')).toBeInTheDocument();
            expect(screen.getByText('Active Modules')).toBeInTheDocument();
        });

        it('displays active tasks count', () => {
            render(<ProgressOverview stats={mockStats} />);

            expect(screen.getByText('40')).toBeInTheDocument();
            expect(screen.getByText('Active Tasks')).toBeInTheDocument();
        });
    });

    describe('Section Labels', () => {
        it('displays Modules label', () => {
            render(<ProgressOverview stats={mockStats} />);

            expect(screen.getByText('Modules')).toBeInTheDocument();
        });

        it('displays Tasks label', () => {
            render(<ProgressOverview stats={mockStats} />);

            expect(screen.getByText('Tasks')).toBeInTheDocument();
        });

        it('displays Overall label in circle', () => {
            render(<ProgressOverview stats={mockStats} />);

            expect(screen.getByText('Overall')).toBeInTheDocument();
        });
    });
});
