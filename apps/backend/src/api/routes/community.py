"""
Community API Routes
Phase 16 - Community & Social Layer

Endpoints for:
- Discussion threads
- Comments
- Reactions
- Activity feeds
"""
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime

from fastapi import APIRouter, Response, HTTPException, status
from pydantic import BaseModel

from ...schemas.community import (
    # Thread
    ThreadCreate, ThreadUpdate, ThreadPublic, ThreadInDB, ThreadStatus,
    # Comment
    CommentCreate, CommentPublic, CommentInDB,
    # Reaction
    ReactionCreate, ReactionInDB,
    # Activity
    ActivityPublic, ActivityInDB, ActivityType,
)


router = APIRouter(prefix="/community", tags=["community"])

PHASE_VERSION = "16.0"


def add_phase_header(response: Response) -> None:
    """Add X-Phase header to response"""
    response.headers["X-Phase"] = PHASE_VERSION


# ==============================================================================
# IN-MEMORY STORAGE (Will be PostgreSQL in production)
# ==============================================================================

_threads_db: dict[UUID, ThreadInDB] = {}
_comments_db: dict[UUID, CommentInDB] = {}
_reactions_db: dict[UUID, ReactionInDB] = {}
_activities_db: dict[UUID, ActivityInDB] = {}


# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

def _create_activity(
    activity_type: ActivityType,
    user_id: Optional[UUID] = None,
    thread_id: Optional[UUID] = None,
    thread_title: Optional[str] = None,
    comment_id: Optional[UUID] = None,
    message: str = "",
):
    """Create an activity feed entry"""
    activity = ActivityInDB(
        id=uuid4(),
        type=activity_type,
        user_id=user_id,
        thread_id=thread_id,
        thread_title=thread_title,
        comment_id=comment_id,
        message=message,
    )
    _activities_db[activity.id] = activity
    return activity


def _seed_sample_threads():
    """Seed sample community content for demo"""
    if _threads_db:
        return  # Already seeded

    sample_user_id = uuid4()

    # Sample threads
    sample_threads = [
        {
            "title": "Best practices for Docker compose in production?",
            "body_markdown": """I've been using Docker Compose for development, but I'm wondering about best practices for production.

Should I use:
- Docker Swarm?
- Kubernetes?
- Just plain Compose with restart policies?

What's your experience?

```yaml
version: '3.8'
services:
  app:
    image: myapp:latest
    restart: unless-stopped
```""",
            "tags": ["docker", "production", "best-practices"],
            "module_slug": "docker-fundamentals",
            "comments_count": 5,
            "upvotes_count": 12,
            "views_count": 156,
        },
        {
            "title": "How to debug failing GitHub Actions workflow?",
            "body_markdown": """My CI pipeline keeps failing with this error:

```
Error: Process completed with exit code 1.
```

The logs don't show much. Any tips for debugging GitHub Actions?

Here's my workflow:

```yaml
name: CI
on: push
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm test
```""",
            "tags": ["github-actions", "ci-cd", "debugging"],
            "module_slug": "cicd-pipelines",
            "comments_count": 8,
            "upvotes_count": 7,
            "views_count": 89,
            "status": "solved",
        },
        {
            "title": "Understanding Linux file permissions (chmod 755 vs 644)",
            "body_markdown": """I'm going through the Linux module and I'm confused about file permissions.

What's the difference between:
- `chmod 755 script.sh`
- `chmod 644 script.sh`

When should I use each? And what about `777`?""",
            "tags": ["linux", "permissions", "beginner"],
            "task_id": None,  # Will be set
            "comments_count": 3,
            "upvotes_count": 15,
            "views_count": 234,
            "status": "solved",
        },
    ]

    for thread_data in sample_threads:
        thread_id = uuid4()
        thread = ThreadInDB(
            id=thread_id,
            user_id=sample_user_id,
            author_name="DevOps Learner",
            title=thread_data["title"],
            body_markdown=thread_data["body_markdown"],
            tags=thread_data["tags"],
            module_slug=thread_data.get("module_slug"),
            status=thread_data.get("status", "open"),
            comments_count=thread_data["comments_count"],
            upvotes_count=thread_data["upvotes_count"],
            views_count=thread_data["views_count"],
        )
        _threads_db[thread_id] = thread

        # Create activity
        _create_activity(
            activity_type="thread_created",
            user_id=sample_user_id,
            thread_id=thread_id,
            thread_title=thread_data["title"],
            message=f"New thread: {thread_data['title'][:50]}...",
        )


# ==============================================================================
# RESPONSE SCHEMAS
# ==============================================================================

class CommunityStatusResponse(BaseModel):
    """Community status response"""
    status: str = "operational"
    phase: str = PHASE_VERSION
    total_threads: int = 0
    total_comments: int = 0
    features: List[str]


class ThreadListResponse(BaseModel):
    """Paginated threads response"""
    threads: List[ThreadPublic]
    total: int
    page: int
    per_page: int
    has_more: bool


class ThreadDetailResponse(ThreadPublic):
    """Thread with comments"""
    comments: List[CommentPublic] = []


class ReactionToggleResponse(BaseModel):
    """Reaction toggle response"""
    action: str  # "added" or "removed"
    new_count: int


# ==============================================================================
# COMMUNITY STATUS
# ==============================================================================

@router.get("/status", response_model=CommunityStatusResponse)
def community_status(response: Response):
    """
    Get community system status.
    """
    add_phase_header(response)
    _seed_sample_threads()

    return CommunityStatusResponse(
        status="operational",
        phase=PHASE_VERSION,
        total_threads=len(_threads_db),
        total_comments=len(_comments_db),
        features=[
            "threads",
            "comments",
            "reactions",
            "activity_feed",
            "module_discussions",
            "task_discussions",
        ]
    )


# ==============================================================================
# THREAD ENDPOINTS
# ==============================================================================

@router.get("", response_model=ThreadListResponse)
@router.get("/", response_model=ThreadListResponse)
def list_threads(
    page: int = 1,
    per_page: int = 20,
    status: Optional[ThreadStatus] = None,
    module_slug: Optional[str] = None,
    task_id: Optional[UUID] = None,
    tag: Optional[str] = None,
    search: Optional[str] = None,
    sort_by: str = "recent",  # recent, popular, unanswered
    response: Response = None,
):
    """
    List community threads with filtering and pagination.
    """
    if response:
        add_phase_header(response)

    _seed_sample_threads()

    # Filter threads
    threads = list(_threads_db.values())
    threads = [t for t in threads if t.is_active]

    if status:
        threads = [t for t in threads if t.status == status]

    if module_slug:
        threads = [t for t in threads if t.module_slug == module_slug]

    if task_id:
        threads = [t for t in threads if t.task_id == task_id]

    if tag:
        tag_lower = tag.lower()
        threads = [t for t in threads if any(tag_lower in tg.lower() for tg in t.tags)]

    if search:
        search_lower = search.lower()
        threads = [
            t for t in threads
            if search_lower in t.title.lower()
            or search_lower in t.body_markdown.lower()
        ]

    # Sort
    if sort_by == "popular":
        threads.sort(key=lambda x: x.upvotes_count, reverse=True)
    elif sort_by == "unanswered":
        threads = [t for t in threads if t.status == "open" and t.comments_count == 0]
        threads.sort(key=lambda x: x.created_at, reverse=True)
    else:  # recent
        threads.sort(key=lambda x: x.created_at, reverse=True)

    # Paginate
    total = len(threads)
    per_page = min(per_page, 50)
    start = (page - 1) * per_page
    end = start + per_page
    page_threads = threads[start:end]

    return ThreadListResponse(
        threads=[ThreadPublic(**t.model_dump()) for t in page_threads],
        total=total,
        page=page,
        per_page=per_page,
        has_more=end < total,
    )


@router.get("/thread/{thread_id}", response_model=ThreadDetailResponse)
def get_thread(thread_id: UUID, response: Response):
    """
    Get thread details with comments.
    """
    add_phase_header(response)
    _seed_sample_threads()

    thread = _threads_db.get(thread_id)
    if not thread:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Thread not found"
        )

    # Increment view count
    thread.views_count += 1

    # Get comments for this thread
    comments = [
        CommentPublic(**c.model_dump())
        for c in _comments_db.values()
        if c.thread_id == thread_id and c.is_active and c.parent_id is None
    ]
    comments.sort(key=lambda x: x.created_at)

    # Build nested replies
    for comment in comments:
        comment.replies = [
            CommentPublic(**c.model_dump())
            for c in _comments_db.values()
            if c.parent_id == comment.id and c.is_active
        ]
        comment.replies.sort(key=lambda x: x.created_at)

    return ThreadDetailResponse(
        **thread.model_dump(),
        comments=comments,
    )


@router.post("/thread", response_model=ThreadPublic, status_code=status.HTTP_201_CREATED)
def create_thread(data: ThreadCreate, response: Response):
    """
    Create a new discussion thread.
    """
    add_phase_header(response)

    # TODO: Get actual user from auth
    mock_user_id = uuid4()

    thread = ThreadInDB(
        id=uuid4(),
        user_id=mock_user_id,
        author_name="Anonymous User",  # TODO: Get from user profile
        title=data.title,
        body_markdown=data.body_markdown,
        module_slug=data.module_slug,
        task_id=data.task_id,
        tags=data.tags,
    )
    _threads_db[thread.id] = thread

    # Create activity
    _create_activity(
        activity_type="thread_created",
        user_id=mock_user_id,
        thread_id=thread.id,
        thread_title=thread.title,
        message=f"New thread: {thread.title[:50]}...",
    )

    return ThreadPublic(**thread.model_dump())


@router.put("/thread/{thread_id}", response_model=ThreadPublic)
def update_thread(thread_id: UUID, data: ThreadUpdate, response: Response):
    """
    Update a thread.
    """
    add_phase_header(response)

    thread = _threads_db.get(thread_id)
    if not thread:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Thread not found"
        )

    # TODO: Check ownership

    # Update fields
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if value is not None:
            setattr(thread, field, value)

    thread.updated_at = datetime.utcnow()

    return ThreadPublic(**thread.model_dump())


@router.post("/thread/{thread_id}/solve", response_model=ThreadPublic)
def mark_thread_solved(thread_id: UUID, response: Response):
    """
    Mark a thread as solved.
    """
    add_phase_header(response)

    thread = _threads_db.get(thread_id)
    if not thread:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Thread not found"
        )

    thread.status = "solved"
    thread.solved_at = datetime.utcnow()
    thread.updated_at = datetime.utcnow()

    # Create activity
    _create_activity(
        activity_type="thread_solved",
        user_id=thread.user_id,
        thread_id=thread.id,
        thread_title=thread.title,
        message=f"Thread solved: {thread.title[:50]}...",
    )

    return ThreadPublic(**thread.model_dump())


# ==============================================================================
# COMMENT ENDPOINTS
# ==============================================================================

@router.post("/comment", response_model=CommentPublic, status_code=status.HTTP_201_CREATED)
def create_comment(data: CommentCreate, response: Response):
    """
    Create a new comment on a thread.
    """
    add_phase_header(response)

    # Check thread exists
    thread = _threads_db.get(data.thread_id)
    if not thread:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Thread not found"
        )

    if thread.status == "locked":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Thread is locked"
        )

    # Check parent comment if replying
    if data.parent_id and data.parent_id not in _comments_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parent comment not found"
        )

    # TODO: Get actual user from auth
    mock_user_id = uuid4()

    comment = CommentInDB(
        id=uuid4(),
        thread_id=data.thread_id,
        user_id=mock_user_id,
        parent_id=data.parent_id,
        author_name="Anonymous User",
        body_markdown=data.body_markdown,
    )
    _comments_db[comment.id] = comment

    # Update thread comment count
    thread.comments_count += 1
    thread.updated_at = datetime.utcnow()

    # Create activity
    _create_activity(
        activity_type="comment_created",
        user_id=mock_user_id,
        thread_id=thread.id,
        thread_title=thread.title,
        comment_id=comment.id,
        message=f"New comment on: {thread.title[:50]}...",
    )

    return CommentPublic(**comment.model_dump())


@router.delete("/comment/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment_id: UUID, response: Response):
    """
    Delete a comment (soft delete).
    """
    add_phase_header(response)

    comment = _comments_db.get(comment_id)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )

    # TODO: Check ownership

    comment.is_active = False

    # Update thread comment count
    thread = _threads_db.get(comment.thread_id)
    if thread:
        thread.comments_count = max(0, thread.comments_count - 1)


@router.post("/comment/{comment_id}/solution", response_model=CommentPublic)
def mark_comment_as_solution(comment_id: UUID, response: Response):
    """
    Mark a comment as the solution.
    """
    add_phase_header(response)

    comment = _comments_db.get(comment_id)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )

    # Unmark other solutions in this thread
    for c in _comments_db.values():
        if c.thread_id == comment.thread_id:
            c.is_solution = False

    comment.is_solution = True

    # Mark thread as solved
    thread = _threads_db.get(comment.thread_id)
    if thread:
        thread.status = "solved"
        thread.solved_at = datetime.utcnow()

    return CommentPublic(**comment.model_dump())


# ==============================================================================
# REACTION ENDPOINTS
# ==============================================================================

@router.post("/reaction", response_model=ReactionToggleResponse)
def toggle_reaction(data: ReactionCreate, response: Response):
    """
    Add or remove a reaction (toggle).
    """
    add_phase_header(response)

    # TODO: Get actual user from auth
    mock_user_id = uuid4()

    # Check target exists
    if data.target_type == "thread":
        target = _threads_db.get(data.target_id)
        if not target:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Thread not found"
            )
    else:
        target = _comments_db.get(data.target_id)
        if not target:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Comment not found"
            )

    # Check if user already reacted
    existing_reaction = None
    for r in _reactions_db.values():
        if (r.target_type == data.target_type and
            r.target_id == data.target_id and
            r.user_id == mock_user_id and
            r.reaction == data.reaction):
            existing_reaction = r
            break

    if existing_reaction:
        # Remove reaction
        del _reactions_db[existing_reaction.id]

        # Update count
        if data.reaction == "upvote":
            target.upvotes_count = max(0, target.upvotes_count - 1)

        return ReactionToggleResponse(
            action="removed",
            new_count=target.upvotes_count if hasattr(target, 'upvotes_count') else 0,
        )
    else:
        # Add reaction
        reaction = ReactionInDB(
            id=uuid4(),
            target_type=data.target_type,
            target_id=data.target_id,
            user_id=mock_user_id,
            reaction=data.reaction,
        )
        _reactions_db[reaction.id] = reaction

        # Update count
        if data.reaction == "upvote":
            target.upvotes_count += 1

        return ReactionToggleResponse(
            action="added",
            new_count=target.upvotes_count if hasattr(target, 'upvotes_count') else 1,
        )


# ==============================================================================
# ACTIVITY FEED ENDPOINTS
# ==============================================================================

@router.get("/activity", response_model=List[ActivityPublic])
def get_activity_feed(
    limit: int = 20,
    activity_type: Optional[ActivityType] = None,
    response: Response = None,
):
    """
    Get the activity feed.
    """
    if response:
        add_phase_header(response)

    _seed_sample_threads()

    activities = list(_activities_db.values())

    if activity_type:
        activities = [a for a in activities if a.type == activity_type]

    # Sort by most recent
    activities.sort(key=lambda x: x.created_at, reverse=True)

    return [ActivityPublic(**a.model_dump()) for a in activities[:limit]]


# ==============================================================================
# MODULE/TASK SPECIFIC
# ==============================================================================

@router.get("/module/{module_slug}/threads", response_model=ThreadListResponse)
def get_module_threads(
    module_slug: str,
    page: int = 1,
    per_page: int = 10,
    response: Response = None,
):
    """
    Get threads for a specific module.
    """
    return list_threads(
        page=page,
        per_page=per_page,
        module_slug=module_slug,
        response=response,
    )


@router.get("/task/{task_id}/threads", response_model=ThreadListResponse)
def get_task_threads(
    task_id: UUID,
    page: int = 1,
    per_page: int = 10,
    response: Response = None,
):
    """
    Get threads for a specific task.
    """
    return list_threads(
        page=page,
        per_page=per_page,
        task_id=task_id,
        response=response,
    )
