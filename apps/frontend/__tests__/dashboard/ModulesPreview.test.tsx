/**
 * ModulesPreview Component Tests
 * Phase 6.5: Dashboard Tests
 */

import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ModulesPreview } from '@/components/dashboard/ModulesPreview';
import type { DashboardModule, DashboardProgress } from '@/lib/dashboard';

// ============================================================================
// MOCK DATA
// ============================================================================

const mockModules: DashboardModule[] = [
    {
        id: 'module-1',
        name: 'DevOps Fundamentals',
        description: 'Learn the basics of DevOps',
        is_active: true,
    },
    {
        id: 'module-2',
        name: 'Docker Mastery',
        description: 'Master containerization with Docker',
        is_active: true,
    },
    {
        id: 'module-3',
        name: 'Kubernetes Deep Dive',
        description: 'Advanced container orchestration',
        is_active: true,
    },
];

const mockProgress: DashboardProgress[] = [
    {
        id: 'progress-1',
        user_id: 'user-1',
        module_id: 'module-1',
        task_id: null,
        studyflow_id: null,
        status: 'completed',
        progress: 100,
    },
    {
        id: 'progress-2',
        user_id: 'user-1',
        module_id: 'module-2',
        task_id: null,
        studyflow_id: null,
        status: 'in_progress',
        progress: 50,
    },
];

const manyModules: DashboardModule[] = [
    ...mockModules,
    { id: 'module-4', name: 'CI/CD Pipelines', description: 'Build automation', is_active: true },
    { id: 'module-5', name: 'Cloud Infrastructure', description: 'AWS, GCP, Azure', is_active: true },
    { id: 'module-6', name: 'Monitoring & Logging', description: 'Observability', is_active: true },
    { id: 'module-7', name: 'Security Practices', description: 'DevSecOps', is_active: true },
];

// ============================================================================
// TESTS
// ============================================================================

describe('ModulesPreview', () => {
    describe('Rendering', () => {
        it('renders the component title', () => {
            render(<ModulesPreview modules={mockModules} />);

            expect(screen.getByText('Learning Modules')).toBeInTheDocument();
        });

        it('renders module count badge', () => {
            render(<ModulesPreview modules={mockModules} />);

            expect(screen.getByText('3 total')).toBeInTheDocument();
        });

        it('renders module emoji icon', () => {
            render(<ModulesPreview modules={mockModules} />);

            expect(screen.getByText('📚')).toBeInTheDocument();
        });
    });

    describe('Module Cards', () => {
        it('renders all module names', () => {
            render(<ModulesPreview modules={mockModules} />);

            expect(screen.getByText('DevOps Fundamentals')).toBeInTheDocument();
            expect(screen.getByText('Docker Mastery')).toBeInTheDocument();
            expect(screen.getByText('Kubernetes Deep Dive')).toBeInTheDocument();
        });

        it('renders module descriptions', () => {
            render(<ModulesPreview modules={mockModules} />);

            expect(screen.getByText('Learn the basics of DevOps')).toBeInTheDocument();
            expect(screen.getByText('Master containerization with Docker')).toBeInTheDocument();
        });

        it('limits displayed modules by maxDisplay prop', () => {
            render(<ModulesPreview modules={manyModules} maxDisplay={3} />);

            // Should show first 3
            expect(screen.getByText('DevOps Fundamentals')).toBeInTheDocument();
            expect(screen.getByText('Docker Mastery')).toBeInTheDocument();
            expect(screen.getByText('Kubernetes Deep Dive')).toBeInTheDocument();

            // Should NOT show module 4+
            expect(screen.queryByText('CI/CD Pipelines')).not.toBeInTheDocument();
        });

        it('shows "View all" link when more modules exist', () => {
            render(<ModulesPreview modules={manyModules} maxDisplay={3} />);

            expect(screen.getByText(/View all 7 modules/i)).toBeInTheDocument();
        });

        it('does not show "View all" when all modules displayed', () => {
            render(<ModulesPreview modules={mockModules} maxDisplay={5} />);

            expect(screen.queryByText(/View all/i)).not.toBeInTheDocument();
        });
    });

    describe('Progress Status', () => {
        it('shows "Completed" badge for 100% progress', () => {
            render(<ModulesPreview modules={mockModules} progress={mockProgress} />);

            expect(screen.getByText('Completed')).toBeInTheDocument();
        });

        it('shows "In Progress" badge for partial progress', () => {
            render(<ModulesPreview modules={mockModules} progress={mockProgress} />);

            expect(screen.getByText('In Progress')).toBeInTheDocument();
        });

        it('shows "Not Started" badge for modules with no progress', () => {
            render(<ModulesPreview modules={mockModules} progress={mockProgress} />);

            // Module 3 has no progress record
            expect(screen.getByText('Not Started')).toBeInTheDocument();
        });

        it('displays progress percentages', () => {
            render(<ModulesPreview modules={mockModules} progress={mockProgress} />);

            // Module 1: 100%, Module 2: 50%, Module 3: 0%
            expect(screen.getByText('100%')).toBeInTheDocument();
            expect(screen.getByText('50%')).toBeInTheDocument();
            expect(screen.getByText('0%')).toBeInTheDocument();
        });
    });

    describe('Action Buttons', () => {
        it('shows "Continue" for modules with progress', () => {
            render(<ModulesPreview modules={mockModules} progress={mockProgress} />);

            // Module 1 (completed) and Module 2 (in progress) both show Continue
            const continueButtons = screen.getAllByText('Continue');
            expect(continueButtons.length).toBeGreaterThanOrEqual(1);
        });

        it('shows "Start" for modules without progress', () => {
            render(<ModulesPreview modules={mockModules} progress={mockProgress} />);

            // Module 3 has no progress
            expect(screen.getByText('Start')).toBeInTheDocument();
        });
    });

    describe('Empty State', () => {
        it('shows empty state message when no modules', () => {
            render(<ModulesPreview modules={[]} />);

            expect(screen.getByText('No modules available')).toBeInTheDocument();
        });

        it('shows helper text in empty state', () => {
            render(<ModulesPreview modules={[]} />);

            expect(screen.getByText('Modules will appear here once created.')).toBeInTheDocument();
        });

        it('shows create module button in empty state', () => {
            render(<ModulesPreview modules={[]} />);

            expect(screen.getByText('Create Module')).toBeInTheDocument();
        });
    });

    describe('Links', () => {
        it('renders module links with correct href', () => {
            render(<ModulesPreview modules={mockModules} progress={mockProgress} />);

            const links = screen.getAllByRole('link');
            // Find module link (not the "View all" link)
            const moduleLinks = links.filter(link =>
                link.getAttribute('href')?.startsWith('/modules/')
            );

            expect(moduleLinks.length).toBeGreaterThan(0);
        });
    });
});
