# Root Cause Analysis: Hands-On Lab Task Content Not Updating

## Problem
Hands-On Lab task content updates from `hands_on.py` are not showing on the website after deployment, despite:
- ✅ Content being updated in `hands_on.py` seed file
- ✅ `seed_content()` being called on startup
- ✅ Code being pushed and deployed

## Data Flow Analysis

### Current Flow (BROKEN):
```
1. seed_content() → Updates PostgreSQL directly ✅
2. API Request → task_service.get_task_by_id() 
3. task_service → task_repository.get_task_by_id()
4. task_repository → Reads from _tasks_db (in-memory dict) ❌
5. _tasks_db is EMPTY at startup → Returns None or old data
```

### Root Cause:
**`task_repository.py` and `module_repository.py` use in-memory storage (`_tasks_db`, `_modules_db`) which is NEVER populated from PostgreSQL.**

## Evidence

### 1. Task Repository Uses In-Memory Storage
```python
# apps/backend/src/db/task_repository.py
_tasks_db: dict[UUID, TaskInDB] = {}  # ← EMPTY at startup

def get_task_by_id(task_id: UUID) -> Optional[TaskInDB]:
    return _tasks_db.get(task_id)  # ← Always returns None (empty dict)
```

### 2. Task Service Uses In-Memory Repository
```python
# apps/backend/src/services/task_service.py
from ..db import task_repository  # ← In-memory version

def get_task_by_id(self, task_id: UUID) -> TaskPublic:
    task = task_repository.get_task_by_id(task_id)  # ← Reads from empty dict
```

### 3. seed_content() Updates PostgreSQL, Not Memory
```python
# apps/backend/src/main.py
if use_postgres:
    # Updates PostgreSQL directly ✅
    existing_task.content = task_data.get("content")
    db.commit()
else:
    # Updates in-memory (but this path never runs on Railway)
    update_task(existing_task.id, TaskUpdate(...))
```

### 4. No Code Loads PostgreSQL → Memory
- ❌ No code syncs PostgreSQL to `_tasks_db` at startup
- ❌ No code loads tasks from database into memory
- ❌ In-memory storage stays empty forever

## Solution Options

### Option A: Make Repositories Hybrid (RECOMMENDED)
Update `task_repository.py` and `module_repository.py` to use PostgreSQL when available, similar to `hybrid_repository.py`.

**Pros:**
- Single source of truth (PostgreSQL)
- No sync issues
- Works immediately

**Cons:**
- Requires refactoring repository functions

### Option B: Load PostgreSQL → Memory at Startup
Add code to load all tasks/modules from PostgreSQL into in-memory storage after `seed_content()`.

**Pros:**
- Minimal changes
- Keeps existing code structure

**Cons:**
- Two sources of truth (sync issues)
- Memory overhead
- Still need to sync on updates

### Option C: Update task_service to Use Hybrid Repository
Change `task_service` to use `hybrid_repository.TaskRepository` instead of `task_repository`.

**Pros:**
- Clean separation
- Uses existing hybrid infrastructure

**Cons:**
- Need to update all service imports
- May break other code

## Recommended Solution: Option A

Update `task_repository.py` and `module_repository.py` to be hybrid repositories that:
1. Check if PostgreSQL is available
2. Use PostgreSQL when available
3. Fall back to in-memory when not available

This ensures:
- ✅ Single source of truth
- ✅ No sync issues
- ✅ Works on both dev (no DB) and production (with DB)
- ✅ Minimal breaking changes

