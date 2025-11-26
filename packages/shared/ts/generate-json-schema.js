import { SystemInfoSchema } from "./systemInfo"
import { z } from "zod"
import { writeFileSync } from "fs"

const schema = SystemInfoSchema.toJSON()
writeFileSync("dist/systemInfo.schema.json", JSON.stringify(schema, null, 2))

console.log("Generated systemInfo.schema.json")
