"""
Search API - Search across modules, tasks, and labs
Phase FAS 1.4 - Implement search functionality
Phase SECURITY: Added authentication to prevent content scraping

Endpoints:
- GET /api/search?q={query} - Search all content (authentication required)

All endpoints require authentication to prevent unauthorized content scraping.
"""

from fastapi import APIRouter, Query, Response
from typing import List, Optional
from pydantic import BaseModel
import logging

from ...db.module_repository import list_modules
from ...db.task_repository import list_tasks
from ...db.lab_repository import list_labs
from ...core.deps import CurrentUser

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/search", tags=["search"])


# ==============================================================================
# SCHEMAS
# ==============================================================================

class SearchResult(BaseModel):
    """Individual search result"""
    type: str  # 'module', 'task', 'lab'
    id: str
    title: str
    description: Optional[str] = None
    url: str
    module_slug: Optional[str] = None
    track_slug: Optional[str] = None
    relevance_score: float = 1.0


class SearchResponse(BaseModel):
    """Search response with results"""
    query: str
    results: List[SearchResult]
    total: int
    has_more: bool = False


# ==============================================================================
# HELPERS
# ==============================================================================

def calculate_relevance(query: str, title: str, description: Optional[str]) -> float:
    """
    Calculate a simple relevance score based on where the query appears.
    Higher score = more relevant.
    """
    query_lower = query.lower()
    score = 0.0

    # Title match is most important
    title_lower = title.lower()
    if query_lower == title_lower:
        score += 10.0  # Exact match
    elif query_lower in title_lower:
        score += 5.0  # Partial title match
        if title_lower.startswith(query_lower):
            score += 2.0  # Starts with query

    # Description match
    if description:
        desc_lower = description.lower()
        if query_lower in desc_lower:
            score += 2.0

    # Bonus for shorter titles (more specific)
    if len(title) < 30:
        score += 0.5

    return score


# ==============================================================================
# ENDPOINTS
# ==============================================================================

@router.get("", response_model=SearchResponse)
def search(
    response: Response,
    current_user: CurrentUser,
    q: str = Query(..., min_length=2, max_length=100, description="Search query"),
    limit: int = Query(20, ge=1, le=50, description="Max results to return"),
    type_filter: Optional[str] = Query(None, description="Filter by type: module, task, lab"),
) -> SearchResponse:
    """
    Search across modules, tasks, and labs.

    Returns results sorted by relevance score.
    
    **Authentication required**: Must be logged in to search content.

    Args:
        current_user: Authenticated user (injected)
        q: Search query
        limit: Max results to return
        type_filter: Filter by type (module, task, lab)

    Returns:
        SearchResponse with matching results sorted by relevance
        
    Raises:
        401: If not authenticated
    """
    response.headers["X-Phase"] = "FAS-1.4-Search"

    query_lower = q.lower().strip()
    results: List[SearchResult] = []

    # Search modules
    if not type_filter or type_filter == "module":
        for module in list_modules():
            name_lower = module.name.lower() if module.name else ""
            desc_lower = (module.description or "").lower()

            if query_lower in name_lower or query_lower in desc_lower:
                score = calculate_relevance(q, module.name, module.description)
                results.append(SearchResult(
                    type="module",
                    id=str(module.id),
                    title=module.name,
                    description=module.description[:150] + "..." if module.description and len(module.description) > 150 else module.description,
                    url=f"/modules/{module.slug or module.id}",
                    track_slug=str(module.track_id) if module.track_id else None,
                    relevance_score=score,
                ))

    # Search tasks
    if not type_filter or type_filter == "task":
        try:
            for task in list_tasks():
                title_lower = task.title.lower() if task.title else ""
                desc_lower = (task.description or "").lower()

                if query_lower in title_lower or query_lower in desc_lower:
                    score = calculate_relevance(q, task.title, task.description)
                    results.append(SearchResult(
                        type="task",
                        id=str(task.id),
                        title=task.title,
                        description=task.description[:150] + "..." if task.description and len(task.description) > 150 else task.description,
                        url=f"/modules/{task.module_id}/tasks/{task.id}",
                        module_slug=str(task.module_id),
                        relevance_score=score,
                    ))
        except Exception as e:
            logger.warning(f"Error searching tasks: {e}")

    # Search labs
    if not type_filter or type_filter == "lab":
        try:
            for lab in list_labs():
                title_lower = lab.title.lower() if lab.title else ""

                if query_lower in title_lower:
                    score = calculate_relevance(q, lab.title, None)
                    results.append(SearchResult(
                        type="lab",
                        id=str(lab.id),
                        title=lab.title,
                        description=f"Hands-on Lab • {lab.estimated_hours}h",
                        url=f"/modules/{lab.module_id}/labs/{lab.id}",
                        module_slug=str(lab.module_id),
                        relevance_score=score,
                    ))
        except Exception as e:
            logger.warning(f"Error searching labs: {e}")

    # Sort by relevance score (highest first)
    results.sort(key=lambda r: r.relevance_score, reverse=True)

    # Check if there are more results
    has_more = len(results) > limit

    return SearchResponse(
        query=q,
        results=results[:limit],
        total=len(results),
        has_more=has_more,
    )


@router.get("/suggestions")
def get_suggestions(
    response: Response,
    current_user: CurrentUser,
    q: str = Query(..., min_length=1, max_length=50),
    limit: int = Query(5, ge=1, le=10),
) -> List[str]:
    """
    Get search suggestions based on partial query.
    Returns a list of suggested search terms.
    
    **Authentication required**: Must be logged in to get suggestions.

    Args:
        current_user: Authenticated user (injected)
        q: Partial search query
        limit: Max suggestions to return

    Returns:
        List of suggested search terms
        
    Raises:
        401: If not authenticated
    """
    response.headers["X-Phase"] = "FAS-1.4-Search"

    query_lower = q.lower().strip()
    suggestions: set = set()

    # Get module names
    for module in list_modules():
        if module.name and query_lower in module.name.lower():
            suggestions.add(module.name)

    # Get task titles
    try:
        for task in list_tasks():
            if task.title and query_lower in task.title.lower():
                suggestions.add(task.title)
    except:
        pass

    # Sort alphabetically and limit
    sorted_suggestions = sorted(list(suggestions))[:limit]

    return sorted_suggestions
