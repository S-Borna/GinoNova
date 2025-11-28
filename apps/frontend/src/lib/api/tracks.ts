/**
 * ============================================================================
 * TRACKS API — Learning Track Operations
 * ============================================================================
 *
 * API client for tracks (Bootcamp v3.0 structure).
 * Tracks contain modules, which contain tasks.
 *
 * @phase A.3 - App Shell & Routing
 */

import { api, type ApiResult } from "./client"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface TrackModule {
    id: string
    slug: string
    title: string
    description: string
    order: number
    isLocked: boolean
    progress: number // 0-100
    taskCount: number
    completedTaskCount: number
}

export interface Track {
    id: string
    slug: string
    title: string
    description: string
    icon: string
    color: string
    order: number
    modules: TrackModule[]
    totalModules: number
    completedModules: number
    progress: number // 0-100
}

export interface TrackSummary {
    id: string
    slug: string
    title: string
    description: string
    icon: string
    color: string
    order: number
    totalModules: number
    completedModules: number
    progress: number
}

/* ============================================================================
   API FUNCTIONS
   ============================================================================ */

/**
 * Get all tracks with summary info
 */
export async function getTracks(): Promise<ApiResult<TrackSummary[]>> {
    return api.get<TrackSummary[]>("/api/v1/tracks")
}

/**
 * Get a single track with its modules
 */
export async function getTrack(slug: string): Promise<ApiResult<Track>> {
    return api.get<Track>(`/api/v1/tracks/${encodeURIComponent(slug)}`)
}

/**
 * Get user's current track progress
 */
export async function getTrackProgress(): Promise<ApiResult<{
    currentTrack: string | null
    currentModule: string | null
    overallProgress: number
    tracks: TrackSummary[]
}>> {
    return api.get("/api/v1/tracks/progress")
}

/* ============================================================================
   MOCK DATA (for development until backend ready)
   ============================================================================ */

export const MOCK_TRACKS: Track[] = [
    {
        id: "1",
        slug: "linux-fundamentals",
        title: "Linux Fundamentals",
        description: "Master the command line and Linux system administration",
        icon: "Terminal",
        color: "#22c55e",
        order: 1,
        totalModules: 6,
        completedModules: 2,
        progress: 33,
        modules: [
            {
                id: "1-1",
                slug: "terminal-basics",
                title: "Terminal Basics",
                description: "Navigate the command line with confidence",
                order: 1,
                isLocked: false,
                progress: 100,
                taskCount: 8,
                completedTaskCount: 8,
            },
            {
                id: "1-2",
                slug: "file-system",
                title: "File System",
                description: "Understand the Linux file hierarchy",
                order: 2,
                isLocked: false,
                progress: 100,
                taskCount: 10,
                completedTaskCount: 10,
            },
            {
                id: "1-3",
                slug: "user-permissions",
                title: "User & Permissions",
                description: "Manage users, groups, and file permissions",
                order: 3,
                isLocked: false,
                progress: 40,
                taskCount: 12,
                completedTaskCount: 5,
            },
            {
                id: "1-4",
                slug: "process-management",
                title: "Process Management",
                description: "Control and monitor system processes",
                order: 4,
                isLocked: true,
                progress: 0,
                taskCount: 8,
                completedTaskCount: 0,
            },
            {
                id: "1-5",
                slug: "networking-basics",
                title: "Networking Basics",
                description: "Configure network interfaces and troubleshoot",
                order: 5,
                isLocked: true,
                progress: 0,
                taskCount: 10,
                completedTaskCount: 0,
            },
            {
                id: "1-6",
                slug: "shell-scripting",
                title: "Shell Scripting",
                description: "Automate tasks with bash scripts",
                order: 6,
                isLocked: true,
                progress: 0,
                taskCount: 15,
                completedTaskCount: 0,
            },
        ],
    },
    {
        id: "2",
        slug: "docker-containers",
        title: "Docker & Containers",
        description: "Build, ship, and run containerized applications",
        icon: "Box",
        color: "#3b82f6",
        order: 2,
        totalModules: 5,
        completedModules: 0,
        progress: 0,
        modules: [
            {
                id: "2-1",
                slug: "docker-basics",
                title: "Docker Basics",
                description: "Introduction to containerization",
                order: 1,
                isLocked: true,
                progress: 0,
                taskCount: 8,
                completedTaskCount: 0,
            },
            {
                id: "2-2",
                slug: "dockerfile",
                title: "Writing Dockerfiles",
                description: "Create custom container images",
                order: 2,
                isLocked: true,
                progress: 0,
                taskCount: 10,
                completedTaskCount: 0,
            },
            {
                id: "2-3",
                slug: "docker-compose",
                title: "Docker Compose",
                description: "Multi-container applications",
                order: 3,
                isLocked: true,
                progress: 0,
                taskCount: 8,
                completedTaskCount: 0,
            },
            {
                id: "2-4",
                slug: "docker-networking",
                title: "Docker Networking",
                description: "Container networking and service discovery",
                order: 4,
                isLocked: true,
                progress: 0,
                taskCount: 6,
                completedTaskCount: 0,
            },
            {
                id: "2-5",
                slug: "docker-volumes",
                title: "Volumes & Storage",
                description: "Persistent data and volume management",
                order: 5,
                isLocked: true,
                progress: 0,
                taskCount: 6,
                completedTaskCount: 0,
            },
        ],
    },
    {
        id: "3",
        slug: "kubernetes",
        title: "Kubernetes",
        description: "Orchestrate containers at scale",
        icon: "Layers",
        color: "#8b5cf6",
        order: 3,
        totalModules: 6,
        completedModules: 0,
        progress: 0,
        modules: [
            {
                id: "3-1",
                slug: "k8s-architecture",
                title: "K8s Architecture",
                description: "Understanding Kubernetes components",
                order: 1,
                isLocked: true,
                progress: 0,
                taskCount: 6,
                completedTaskCount: 0,
            },
            {
                id: "3-2",
                slug: "pods-deployments",
                title: "Pods & Deployments",
                description: "Core workload resources",
                order: 2,
                isLocked: true,
                progress: 0,
                taskCount: 10,
                completedTaskCount: 0,
            },
            {
                id: "3-3",
                slug: "services-ingress",
                title: "Services & Ingress",
                description: "Expose and route traffic to applications",
                order: 3,
                isLocked: true,
                progress: 0,
                taskCount: 8,
                completedTaskCount: 0,
            },
            {
                id: "3-4",
                slug: "configmaps-secrets",
                title: "ConfigMaps & Secrets",
                description: "Manage configuration and sensitive data",
                order: 4,
                isLocked: true,
                progress: 0,
                taskCount: 6,
                completedTaskCount: 0,
            },
            {
                id: "3-5",
                slug: "k8s-storage",
                title: "Storage",
                description: "Persistent volumes and claims",
                order: 5,
                isLocked: true,
                progress: 0,
                taskCount: 6,
                completedTaskCount: 0,
            },
            {
                id: "3-6",
                slug: "helm",
                title: "Helm Charts",
                description: "Package and deploy applications",
                order: 6,
                isLocked: true,
                progress: 0,
                taskCount: 8,
                completedTaskCount: 0,
            },
        ],
    },
    {
        id: "4",
        slug: "ci-cd",
        title: "CI/CD Pipelines",
        description: "Automate build, test, and deployment workflows",
        icon: "GitBranch",
        color: "#f59e0b",
        order: 4,
        totalModules: 5,
        completedModules: 0,
        progress: 0,
        modules: [
            {
                id: "4-1",
                slug: "git-advanced",
                title: "Advanced Git",
                description: "Branching strategies and workflows",
                order: 1,
                isLocked: true,
                progress: 0,
                taskCount: 8,
                completedTaskCount: 0,
            },
            {
                id: "4-2",
                slug: "github-actions",
                title: "GitHub Actions",
                description: "Build CI/CD pipelines with GitHub",
                order: 2,
                isLocked: true,
                progress: 0,
                taskCount: 12,
                completedTaskCount: 0,
            },
            {
                id: "4-3",
                slug: "jenkins",
                title: "Jenkins",
                description: "Enterprise CI/CD with Jenkins",
                order: 3,
                isLocked: true,
                progress: 0,
                taskCount: 10,
                completedTaskCount: 0,
            },
            {
                id: "4-4",
                slug: "argocd",
                title: "ArgoCD",
                description: "GitOps continuous deployment",
                order: 4,
                isLocked: true,
                progress: 0,
                taskCount: 8,
                completedTaskCount: 0,
            },
            {
                id: "4-5",
                slug: "testing-strategies",
                title: "Testing Strategies",
                description: "Unit, integration, and e2e testing",
                order: 5,
                isLocked: true,
                progress: 0,
                taskCount: 10,
                completedTaskCount: 0,
            },
        ],
    },
    {
        id: "5",
        slug: "infrastructure-as-code",
        title: "Infrastructure as Code",
        description: "Provision and manage cloud infrastructure",
        icon: "Cloud",
        color: "#ec4899",
        order: 5,
        totalModules: 4,
        completedModules: 0,
        progress: 0,
        modules: [
            {
                id: "5-1",
                slug: "terraform-basics",
                title: "Terraform Basics",
                description: "Introduction to infrastructure as code",
                order: 1,
                isLocked: true,
                progress: 0,
                taskCount: 10,
                completedTaskCount: 0,
            },
            {
                id: "5-2",
                slug: "terraform-advanced",
                title: "Advanced Terraform",
                description: "Modules, state, and workspaces",
                order: 2,
                isLocked: true,
                progress: 0,
                taskCount: 12,
                completedTaskCount: 0,
            },
            {
                id: "5-3",
                slug: "ansible",
                title: "Ansible",
                description: "Configuration management and automation",
                order: 3,
                isLocked: true,
                progress: 0,
                taskCount: 10,
                completedTaskCount: 0,
            },
            {
                id: "5-4",
                slug: "pulumi",
                title: "Pulumi",
                description: "IaC with programming languages",
                order: 4,
                isLocked: true,
                progress: 0,
                taskCount: 8,
                completedTaskCount: 0,
            },
        ],
    },
]

/**
 * Get mock tracks for development
 */
export function getMockTracks(): TrackSummary[] {
    return MOCK_TRACKS.map(({ modules, ...track }) => track)
}

/**
 * Get mock track by slug
 */
export function getMockTrack(slug: string): Track | undefined {
    return MOCK_TRACKS.find((t) => t.slug === slug)
}
