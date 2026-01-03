/**
 * ============================================================================
 * USE HANDS-ON — Fetch Hands-On Lab content from Backend API
 * ============================================================================
 *
 * React Query hooks for fetching hands-on module and task data.
 * Data source: Backend API (/api/content/module/hands-on-lab)
 * Fallback: Local data from /data/handson-module.ts
 *
 * @phase HANDS-ON-LAB
 */

import { useQuery } from "@tanstack/react-query"
import { API_BASE_URL } from "@/lib/api/client"
import { HANDSON_MODULE, HandsOnTask as LocalHandsOnTask } from "@/data/handson-module"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface ContentBlock {
    type: string
    title?: string
    headline?: string
    explanation?: string
    code?: string
    language?: string
    options?: QuizOption[]
    question?: string
    hint?: string
    pro_tip?: string
    warning?: string
    warning_level?: string
    learning_objectives?: string[]
    scenario_title?: string
    scenario_context?: string
    scenario_symptoms?: string[]
    scenario_solution?: string
    challenge_task?: string
    challenge_commands?: string[]
    expected_output?: string
    diagram?: string
    diagram_caption?: string
    message?: string
    items?: string[]
    compare_items?: CompareItem[]
    summary_title?: string
    key_points?: string[]
    next_step?: string
}

export interface QuizOption {
    text: string
    correct?: boolean
    feedback?: string
}

export interface CompareItem {
    name: string
    pros: string[]
    cons: string[]
    use_case?: string
}

export type TaskDifficulty = 'easy' | 'medium' | 'hard'

export interface HandsOnTask {
    id: string
    title: string
    slug?: string
    description: string
    order_index: number
    estimated_minutes: number
    difficulty: TaskDifficulty
    xp_reward: number
    content?: string  // Markdown content from backend
    content_blocks?: ContentBlock[]  // Interactive blocks
}

export interface HandsOnModule {
    id: string
    name: string
    slug: string
    description: string
    difficulty: string
    estimated_hours: number
    tasks: HandsOnTask[]
    total_tasks: number
}

/* ============================================================================
   QUERY KEYS
   ============================================================================ */

export const handsOnQueryKeys = {
    module: ["hands-on", "module"] as const,
    task: (taskId: string) => ["hands-on", "task", taskId] as const,
}

/* ============================================================================
   FALLBACK DATA - Convert local data to API format
   ============================================================================ */

function getLocalModuleData(): HandsOnModule {
    return {
        id: HANDSON_MODULE.id,
        name: HANDSON_MODULE.name,
        slug: HANDSON_MODULE.slug,
        description: HANDSON_MODULE.description,
        difficulty: HANDSON_MODULE.difficulty,
        estimated_hours: HANDSON_MODULE.estimated_hours,
        tasks: HANDSON_MODULE.tasks.map((task: LocalHandsOnTask) => ({
            id: task.id,
            title: task.title,
            slug: generateSlug(task.title),
            description: task.description,
            order_index: task.order_index,
            estimated_minutes: task.estimated_minutes,
            difficulty: 'medium' as TaskDifficulty, // Local data doesn't have difficulty per task
            xp_reward: 100,
            content: task.content,  // Use markdown content from local data
            content_blocks: task.content_blocks as ContentBlock[],
        })),
        total_tasks: HANDSON_MODULE.tasks.length,
    }
}

function getLocalTaskData(taskId: string): (HandsOnTask & { module_slug?: string; prev_task_id?: string; next_task_id?: string }) | null {
    const tasks = HANDSON_MODULE.tasks
    const taskIndex = tasks.findIndex((t: LocalHandsOnTask) => t.id === taskId)
    
    if (taskIndex === -1) return null
    
    const task = tasks[taskIndex]
    const prevTask = taskIndex > 0 ? tasks[taskIndex - 1] : null
    const nextTask = taskIndex < tasks.length - 1 ? tasks[taskIndex + 1] : null
    
    return {
        id: task.id,
        title: task.title,
        slug: generateSlug(task.title),
        description: task.description,
        order_index: task.order_index,
        estimated_minutes: task.estimated_minutes,
        difficulty: 'medium' as TaskDifficulty,
        xp_reward: 100,
        content: task.content,  // Use markdown content from local data
        content_blocks: task.content_blocks as ContentBlock[],
        module_slug: HANDSON_MODULE.slug,
        prev_task_id: prevTask?.id,
        next_task_id: nextTask?.id,
    }
}

/* ============================================================================
   API FUNCTIONS
   ============================================================================ */

async function fetchHandsOnModule(): Promise<HandsOnModule> {
    try {
        const response = await fetch(`${API_BASE_URL}/api/content/module/hands-on-lab`)
        
        if (!response.ok) {
            console.warn(`API returned ${response.status}, falling back to local data`)
            return getLocalModuleData()
        }
        
        const data = await response.json()
        
        // Transform API response to match expected structure
        return {
            id: data.id,
            name: data.name || data.title,
            slug: data.slug,
            description: data.description || "",
            difficulty: data.difficulty || "intermediate",
            estimated_hours: data.estimated_hours || 6,
            tasks: data.tasks?.map((task: Record<string, unknown>, index: number) => ({
                id: task.id as string,
                title: task.title as string,
                slug: generateSlug(task.title as string),
                description: task.description as string || "",
                order_index: (task.order_index as number) ?? index,
                estimated_minutes: (task.estimated_minutes as number) || 30,
                difficulty: mapDifficulty(task.difficulty as string),
                xp_reward: (task.xp_reward as number) || 50,
                content: task.content as string || undefined,
                content_blocks: task.content_blocks as ContentBlock[] || undefined,
                has_content_blocks: task.has_content_blocks as boolean || false,
            })) || [],
            total_tasks: data.total_tasks || data.tasks?.length || 0,
        }
    } catch (error) {
        console.warn('Failed to fetch from API, falling back to local data:', error)
        return getLocalModuleData()
    }
}

async function fetchHandsOnTask(taskId: string): Promise<HandsOnTask & { module_slug?: string; prev_task_id?: string; next_task_id?: string }> {
    try {
        const response = await fetch(`${API_BASE_URL}/api/content/task/${taskId}`)
        
        if (!response.ok) {
            console.warn(`API returned ${response.status} for task, falling back to local data`)
            const localTask = getLocalTaskData(taskId)
            if (localTask) return localTask
            throw new Error(`Task not found: ${taskId}`)
        }
        
        const data = await response.json()
        
        return {
            id: data.id,
            title: data.title,
            slug: generateSlug(data.title),
            description: data.description || "",
            order_index: data.order_index || 0,
            estimated_minutes: data.estimated_minutes || 30,
            difficulty: mapDifficulty(data.difficulty),
            xp_reward: data.xp_reward || 50,
            content: data.content || undefined,
            content_blocks: data.content_blocks || undefined,
            module_slug: data.module_slug,
            prev_task_id: data.prev_task_id,
            next_task_id: data.next_task_id,
        }
    } catch (error) {
        console.warn('Failed to fetch task from API, falling back to local data:', error)
        const localTask = getLocalTaskData(taskId)
        if (localTask) return localTask
        throw new Error(`Task not found: ${taskId}`)
    }
}

/* ============================================================================
   HELPER FUNCTIONS
   ============================================================================ */

function generateSlug(title: string): string {
    return title
        .toLowerCase()
        .replace(/[åä]/g, 'a')
        .replace(/ö/g, 'o')
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-|-$/g, '')
}

/**
 * Map backend difficulty string to TaskDifficulty type
 */
function mapDifficulty(difficulty: string | undefined): TaskDifficulty {
    const normalized = difficulty?.toLowerCase()
    if (normalized === 'easy' || normalized === 'beginner') return 'easy'
    if (normalized === 'hard' || normalized === 'advanced' || normalized === 'expert') return 'hard'
    return 'medium' // Default for 'medium', 'intermediate', or unknown values
}

/**
 * Convert markdown content to content blocks for rendering
 * This allows using the same renderer for both content formats
 */
export function markdownToContentBlocks(markdown: string, title: string): ContentBlock[] {
    const blocks: ContentBlock[] = []
    
    // Add intro block with title
    blocks.push({
        type: "intro",
        headline: title,
        learning_objectives: []
    })
    
    // Add markdown content block
    blocks.push({
        type: "markdown",
        explanation: markdown
    })
    
    return blocks
}

/* ============================================================================
   HOOKS
   ============================================================================ */

/**
 * Fetch the complete Hands-On Lab module with all tasks
 * Falls back to local data if API is unavailable
 */
export function useHandsOnModule() {
    return useQuery({
        queryKey: handsOnQueryKeys.module,
        queryFn: fetchHandsOnModule,
        staleTime: 1000 * 60 * 5, // 5 minutes
        retry: 1, // Only retry once, then fall back to local
    })
}

/**
 * Fetch a single hands-on task by ID
 * Falls back to local data if API is unavailable
 */
export function useHandsOnTask(taskId: string) {
    return useQuery({
        queryKey: handsOnQueryKeys.task(taskId),
        queryFn: () => fetchHandsOnTask(taskId),
        staleTime: 1000 * 60 * 5, // 5 minutes
        retry: 1, // Only retry once, then fall back to local
        enabled: !!taskId,
    })
}

/**
 * Get a task from the module data by ID (for when module is already loaded)
 */
export function getTaskFromModule(module: HandsOnModule | undefined, taskId: string): HandsOnTask | undefined {
    if (!module) return undefined
    return module.tasks.find(t => t.id === taskId)
}
