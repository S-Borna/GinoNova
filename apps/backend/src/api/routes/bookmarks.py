"""
Bookmark API Routes - PROMPT 4: Sidebar Bookmark System
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from typing import Annotated

from src.core.deps import get_current_user
from src.schemas.user import UserPublic
from src.schemas.bookmark import BookmarkCreate, BookmarkResponse, BookmarkList, BookmarkCheck
from src.db.database import get_db
from src.db.models import Bookmark, Task, Module

router = APIRouter(prefix="/bookmarks", tags=["bookmarks"])


@router.get("", response_model=BookmarkList)
async def get_bookmarks(
    current_user: Annotated[UserPublic, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """Get all bookmarks for current user, with task and module info"""
    bookmarks = db.query(Bookmark).filter(
        Bookmark.user_id == current_user.id
    ).order_by(Bookmark.created_at.desc()).all()
    
    bookmark_responses = []
    for b in bookmarks:
        task = db.query(Task).filter(Task.id == b.task_id).first()
        if task:
            module = db.query(Module).filter(Module.id == task.module_id).first()
            bookmark_responses.append(BookmarkResponse(
                id=b.id,
                user_id=b.user_id,
                task_id=b.task_id,
                created_at=b.created_at,
                task_title=task.title,
                module_slug=module.slug if module else "",
                module_name=module.name if module else ""
            ))
    
    return BookmarkList(
        bookmarks=bookmark_responses,
        total=len(bookmark_responses)
    )


@router.post("", response_model=BookmarkResponse, status_code=status.HTTP_201_CREATED)
async def create_bookmark(
    bookmark: BookmarkCreate,
    current_user: Annotated[UserPublic, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """Bookmark a task"""
    # Check if already bookmarked
    existing = db.query(Bookmark).filter(
        Bookmark.user_id == current_user.id,
        Bookmark.task_id == bookmark.task_id
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Task already bookmarked"
        )
    
    # Get task and module info
    task = db.query(Task).filter(Task.id == bookmark.task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Task not found"
        )
    
    module = db.query(Module).filter(Module.id == task.module_id).first()
    
    # Create bookmark
    new_bookmark = Bookmark(
        user_id=current_user.id,
        task_id=bookmark.task_id
    )
    db.add(new_bookmark)
    db.commit()
    db.refresh(new_bookmark)
    
    return BookmarkResponse(
        id=new_bookmark.id,
        user_id=new_bookmark.user_id,
        task_id=new_bookmark.task_id,
        created_at=new_bookmark.created_at,
        task_title=task.title,
        module_slug=module.slug if module else "",
        module_name=module.name if module else ""
    )


@router.delete("/{task_id}")
async def remove_bookmark(
    task_id: UUID,
    current_user: Annotated[UserPublic, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """Remove bookmark by task_id"""
    bookmark = db.query(Bookmark).filter(
        Bookmark.user_id == current_user.id,
        Bookmark.task_id == task_id
    ).first()
    
    if not bookmark:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Bookmark not found"
        )
    
    db.delete(bookmark)
    db.commit()
    
    return {"status": "removed", "task_id": str(task_id)}


@router.get("/check/{task_id}", response_model=BookmarkCheck)
async def check_bookmark(
    task_id: UUID,
    current_user: Annotated[UserPublic, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """Check if a task is bookmarked"""
    bookmark = db.query(Bookmark).filter(
        Bookmark.user_id == current_user.id,
        Bookmark.task_id == task_id
    ).first()
    
    return BookmarkCheck(is_bookmarked=bookmark is not None)


@router.delete("")
async def clear_all_bookmarks(
    current_user: Annotated[UserPublic, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """Clear all bookmarks for current user"""
    deleted_count = db.query(Bookmark).filter(
        Bookmark.user_id == current_user.id
    ).delete()
    db.commit()
    
    return {"status": "cleared", "deleted_count": deleted_count}
