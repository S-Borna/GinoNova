import { z } from "zod"

export const SystemInfoSchema = z.object({
    service: z.string(),
    version: z.string()
})

export type SystemInfo = z.infer<typeof SystemInfoSchema>
