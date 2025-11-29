"""
Notion API Integration - DevOpsHub Control Center Sync
Syncs project data with Notion workspace for documentation and tracking
"""
import os
import logging
from datetime import datetime
from typing import Optional, List, Dict, Any
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/notion", tags=["notion"])

# Notion API Configuration
NOTION_API_KEY = os.getenv("NOTION_API_KEY", "")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID", "")
NOTION_API_VERSION = "2022-06-28"
NOTION_BASE_URL = "https://api.notion.com/v1"


# ============ Schemas ============

class NotionPageCreate(BaseModel):
    """Create a new page in Notion database"""
    title: str = Field(..., description="Page title")
    properties: Dict[str, Any] = Field(default_factory=dict, description="Page properties")
    content: Optional[str] = Field(None, description="Page content as markdown")


class NotionPageUpdate(BaseModel):
    """Update an existing Notion page"""
    page_id: str = Field(..., description="Notion page ID")
    properties: Dict[str, Any] = Field(default_factory=dict, description="Properties to update")
    content: Optional[str] = Field(None, description="New content as markdown")


class NotionSyncRequest(BaseModel):
    """Request to sync project data to Notion"""
    sync_type: str = Field(..., description="Type: modules, progress, tasks, all")
    user_id: Optional[str] = Field(None, description="User ID for progress sync")


class NotionWebhookPayload(BaseModel):
    """Incoming webhook from Notion"""
    type: str
    page_id: Optional[str] = None
    database_id: Optional[str] = None
    data: Dict[str, Any] = Field(default_factory=dict)


class NotionConfig(BaseModel):
    """Notion integration configuration"""
    api_key: str = Field(..., description="Notion API key (Internal Integration Token)")
    database_id: str = Field(..., description="Main database ID for sync")
    modules_db_id: Optional[str] = Field(None, description="Modules database ID")
    tasks_db_id: Optional[str] = Field(None, description="Tasks database ID")
    progress_db_id: Optional[str] = Field(None, description="Progress database ID")


# ============ Helper Functions ============

def get_notion_headers() -> Dict[str, str]:
    """Get headers for Notion API requests"""
    if not NOTION_API_KEY:
        raise HTTPException(status_code=500, detail="NOTION_API_KEY not configured")

    return {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_API_VERSION
    }


def is_notion_configured() -> bool:
    """Check if Notion integration is configured"""
    return bool(NOTION_API_KEY and NOTION_DATABASE_ID)


async def notion_request(method: str, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
    """Make a request to Notion API"""
    import httpx

    headers = get_notion_headers()
    url = f"{NOTION_BASE_URL}/{endpoint}"

    async with httpx.AsyncClient() as client:
        if method == "GET":
            response = await client.get(url, headers=headers)
        elif method == "POST":
            response = await client.post(url, headers=headers, json=data)
        elif method == "PATCH":
            response = await client.patch(url, headers=headers, json=data)
        elif method == "DELETE":
            response = await client.delete(url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        if response.status_code >= 400:
            logger.error(f"Notion API error: {response.status_code} - {response.text}")
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Notion API error: {response.json().get('message', 'Unknown error')}"
            )

        return response.json()


def markdown_to_notion_blocks(markdown: str) -> List[Dict[str, Any]]:
    """Convert markdown to Notion blocks (simplified)"""
    blocks = []
    lines = markdown.split('\n')

    for line in lines:
        if not line.strip():
            continue

        # Headers
        if line.startswith('### '):
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"type": "text", "text": {"content": line[4:]}}]
                }
            })
        elif line.startswith('## '):
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": line[3:]}}]
                }
            })
        elif line.startswith('# '):
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{"type": "text", "text": {"content": line[2:]}}]
                }
            })
        # Bullet points
        elif line.startswith('- ') or line.startswith('* '):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{"type": "text", "text": {"content": line[2:]}}]
                }
            })
        # Code blocks (simple)
        elif line.startswith('```'):
            continue  # Skip code fence markers
        # Regular paragraph
        else:
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": line}}]
                }
            })

    return blocks


# ============ API Endpoints ============

@router.get("/status")
async def get_notion_status():
    """Check Notion integration status"""
    return {
        "configured": is_notion_configured(),
        "has_api_key": bool(NOTION_API_KEY),
        "has_database_id": bool(NOTION_DATABASE_ID),
        "api_version": NOTION_API_VERSION
    }


@router.get("/databases")
async def list_databases():
    """List accessible Notion databases"""
    if not is_notion_configured():
        raise HTTPException(status_code=400, detail="Notion not configured")

    result = await notion_request("POST", "search", {
        "filter": {"property": "object", "value": "database"}
    })

    databases = []
    for db in result.get("results", []):
        databases.append({
            "id": db["id"],
            "title": db.get("title", [{}])[0].get("plain_text", "Untitled"),
            "url": db.get("url", ""),
            "created_time": db.get("created_time"),
            "last_edited_time": db.get("last_edited_time")
        })

    return {"databases": databases, "count": len(databases)}


@router.get("/database/{database_id}")
async def get_database(database_id: str):
    """Get database details and schema"""
    if not is_notion_configured():
        raise HTTPException(status_code=400, detail="Notion not configured")

    result = await notion_request("GET", f"databases/{database_id}")

    return {
        "id": result["id"],
        "title": result.get("title", [{}])[0].get("plain_text", "Untitled"),
        "properties": result.get("properties", {}),
        "url": result.get("url", "")
    }


@router.post("/pages")
async def create_page(page: NotionPageCreate):
    """Create a new page in Notion database"""
    if not is_notion_configured():
        raise HTTPException(status_code=400, detail="Notion not configured")

    # Build page data
    page_data = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": {
            "title": {
                "title": [{"text": {"content": page.title}}]
            },
            **page.properties
        }
    }

    # Add content blocks if provided
    if page.content:
        page_data["children"] = markdown_to_notion_blocks(page.content)

    result = await notion_request("POST", "pages", page_data)

    return {
        "id": result["id"],
        "url": result.get("url", ""),
        "created_time": result.get("created_time")
    }


@router.patch("/pages/{page_id}")
async def update_page(page_id: str, page: NotionPageUpdate):
    """Update an existing Notion page"""
    if not is_notion_configured():
        raise HTTPException(status_code=400, detail="Notion not configured")

    # Update properties
    if page.properties:
        await notion_request("PATCH", f"pages/{page_id}", {
            "properties": page.properties
        })

    # Update content (append blocks)
    if page.content:
        blocks = markdown_to_notion_blocks(page.content)
        for block in blocks:
            await notion_request("PATCH", f"blocks/{page_id}/children", {
                "children": [block]
            })

    return {"status": "updated", "page_id": page_id}


@router.post("/sync")
async def sync_to_notion(sync_request: NotionSyncRequest, background_tasks: BackgroundTasks):
    """Sync project data to Notion (runs in background)"""
    if not is_notion_configured():
        raise HTTPException(status_code=400, detail="Notion not configured")

    # Add sync task to background
    background_tasks.add_task(
        perform_sync,
        sync_type=sync_request.sync_type,
        user_id=sync_request.user_id
    )

    return {
        "status": "sync_started",
        "sync_type": sync_request.sync_type,
        "message": "Sync running in background"
    }


async def perform_sync(sync_type: str, user_id: Optional[str] = None):
    """Perform the actual sync operation"""
    logger.info(f"Starting Notion sync: type={sync_type}, user_id={user_id}")

    try:
        if sync_type in ["modules", "all"]:
            await sync_modules()

        if sync_type in ["tasks", "all"]:
            await sync_tasks()

        if sync_type in ["progress", "all"] and user_id:
            await sync_progress(user_id)

        logger.info(f"Notion sync completed: {sync_type}")
    except Exception as e:
        logger.error(f"Notion sync failed: {e}")


async def sync_modules():
    """Sync modules to Notion"""
    from ...db.module_repository import list_modules

    modules = list_modules()
    logger.info(f"Syncing {len(modules)} modules to Notion")

    for module in modules:
        try:
            await notion_request("POST", "pages", {
                "parent": {"database_id": NOTION_DATABASE_ID},
                "properties": {
                    "title": {"title": [{"text": {"content": module.name}}]},
                    "Type": {"select": {"name": "Module"}},
                    "Status": {"select": {"name": "Active" if module.is_active else "Inactive"}},
                    "Difficulty": {"select": {"name": module.difficulty.capitalize()}},
                    "Order": {"number": module.order_index}
                }
            })
        except Exception as e:
            logger.error(f"Failed to sync module {module.name}: {e}")


async def sync_tasks():
    """Sync tasks to Notion"""
    from ...db.task_repository import list_all_tasks

    tasks = list_all_tasks()
    logger.info(f"Syncing {len(tasks)} tasks to Notion")

    for task in tasks:
        try:
            await notion_request("POST", "pages", {
                "parent": {"database_id": NOTION_DATABASE_ID},
                "properties": {
                    "title": {"title": [{"text": {"content": task.title}}]},
                    "Type": {"select": {"name": "Task"}},
                    "Difficulty": {"select": {"name": task.difficulty.capitalize()}},
                    "XP": {"number": task.xp_reward},
                    "Minutes": {"number": task.estimated_minutes}
                }
            })
        except Exception as e:
            logger.error(f"Failed to sync task {task.title}: {e}")


async def sync_progress(user_id: str):
    """Sync user progress to Notion"""
    from uuid import UUID
    from ...db.progress_repository import get_user_progress

    progress_list = get_user_progress(UUID(user_id))
    logger.info(f"Syncing progress for user {user_id}: {len(progress_list)} entries")

    for progress in progress_list:
        try:
            await notion_request("POST", "pages", {
                "parent": {"database_id": NOTION_DATABASE_ID},
                "properties": {
                    "title": {"title": [{"text": {"content": f"Progress: {progress.id}"}}]},
                    "Type": {"select": {"name": "Progress"}},
                    "Status": {"select": {"name": progress.status.capitalize()}},
                    "XP Earned": {"number": progress.xp_earned},
                    "Completed": {"checkbox": progress.status == "completed"}
                }
            })
        except Exception as e:
            logger.error(f"Failed to sync progress {progress.id}: {e}")


@router.post("/webhook")
async def notion_webhook(payload: NotionWebhookPayload):
    """Handle incoming webhooks from Notion"""
    logger.info(f"Received Notion webhook: type={payload.type}")

    # Process webhook based on type
    if payload.type == "page_updated":
        # Handle page update - could trigger sync back to app
        pass
    elif payload.type == "page_created":
        # Handle new page creation
        pass

    return {"status": "received", "type": payload.type}


@router.get("/query/{database_id}")
async def query_database(
    database_id: str,
    filter_type: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 100
):
    """Query a Notion database with filters"""
    if not is_notion_configured():
        raise HTTPException(status_code=400, detail="Notion not configured")

    query_data: Dict[str, Any] = {"page_size": min(limit, 100)}

    # Build filter
    filters = []
    if filter_type:
        filters.append({
            "property": "Type",
            "select": {"equals": filter_type}
        })
    if status:
        filters.append({
            "property": "Status",
            "select": {"equals": status}
        })

    if len(filters) == 1:
        query_data["filter"] = filters[0]
    elif len(filters) > 1:
        query_data["filter"] = {"and": filters}

    result = await notion_request("POST", f"databases/{database_id}/query", query_data)

    pages = []
    for page in result.get("results", []):
        title_prop = page.get("properties", {}).get("title", {})
        title = ""
        if title_prop.get("title"):
            title = title_prop["title"][0].get("plain_text", "") if title_prop["title"] else ""

        pages.append({
            "id": page["id"],
            "title": title,
            "url": page.get("url", ""),
            "created_time": page.get("created_time"),
            "last_edited_time": page.get("last_edited_time"),
            "properties": page.get("properties", {})
        })

    return {
        "pages": pages,
        "count": len(pages),
        "has_more": result.get("has_more", False)
    }
