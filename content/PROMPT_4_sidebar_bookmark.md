# PROMPT 4: Ersätt Sidebar med Bookmark/Star System

## KONTEXT

Nuvarande sidebar i module-vyn visar bara en lista på tasks — ingen funktionalitet.
Användare behöver ett sätt att markera tasks de vill återkomma till.

## UPPDRAG

Ersätt den statiska sidebaren med ett dynamiskt bookmark-system.

## DESIGN

### Sidebar States

**Tom state:**
```
┌─────────────────────┐
│  ⭐ Sparade tasks   │
│                     │
│  Du har inga        │
│  sparade tasks än.  │
│                     │
│  Klicka på ⭐ vid   │
│  en task för att    │
│  spara den här.     │
└─────────────────────┘
```

**Med bookmarks:**
```
┌─────────────────────────────┐
│  ⭐ Sparade tasks (3)       │
│                             │
│  📚 Environment Setup       │
│  └─ Create dotfiles repo    │
│                             │
│  🐳 Docker Fundamentals     │
│  └─ Multi-stage builds      │
│  └─ Docker Compose          │
│                             │
│  [Rensa alla]               │
└─────────────────────────────┘
```

### Task Card med Star

```
┌────────────────────────────────────────┐
│  ⭐  Task 15: Create dotfiles repo     │
│      ◯ 25 min  ⚡ +45 XP  [medium]    │
└────────────────────────────────────────┘
```

Star är klickbar — togglear bookmark status.

## IMPLEMENTATION

### Backend

#### Schema: `apps/backend/src/schemas/bookmark.py`

```python
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class BookmarkCreate(BaseModel):
    task_id: UUID

class BookmarkResponse(BaseModel):
    id: UUID
    user_id: UUID
    task_id: UUID
    created_at: datetime
    
    # Inkludera task-info för display
    task_title: str
    module_slug: str
    module_name: str

class BookmarkList(BaseModel):
    bookmarks: list[BookmarkResponse]
    total: int
```

#### Database Model: `apps/backend/src/db/models/bookmark.py`

```python
from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime

from src.db.base import Base

class Bookmark(Base):
    __tablename__ = "bookmarks"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="bookmarks")
    task = relationship("Task")
    
    # Unique constraint: user can only bookmark a task once
    __table_args__ = (
        UniqueConstraint('user_id', 'task_id', name='unique_user_task_bookmark'),
    )
```

#### Routes: `apps/backend/src/api/routes/bookmarks.py`

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from src.core.deps import get_current_user, get_db
from src.schemas.bookmark import BookmarkCreate, BookmarkResponse, BookmarkList
from src.db.models.bookmark import Bookmark
from src.db.models.task import Task

router = APIRouter(prefix="/api/bookmarks", tags=["bookmarks"])

@router.get("", response_model=BookmarkList)
async def get_bookmarks(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get all bookmarks for current user, grouped by module"""
    bookmarks = db.query(Bookmark).filter(
        Bookmark.user_id == current_user.id
    ).order_by(Bookmark.created_at.desc()).all()
    
    return BookmarkList(
        bookmarks=[
            BookmarkResponse(
                id=b.id,
                user_id=b.user_id,
                task_id=b.task_id,
                created_at=b.created_at,
                task_title=b.task.title,
                module_slug=b.task.module.slug,
                module_name=b.task.module.name
            ) for b in bookmarks
        ],
        total=len(bookmarks)
    )

@router.post("", response_model=BookmarkResponse)
async def create_bookmark(
    bookmark: BookmarkCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Bookmark a task"""
    # Check if already bookmarked
    existing = db.query(Bookmark).filter(
        Bookmark.user_id == current_user.id,
        Bookmark.task_id == bookmark.task_id
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Task already bookmarked")
    
    task = db.query(Task).filter(Task.id == bookmark.task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
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
        module_slug=task.module.slug,
        module_name=task.module.name
    )

@router.delete("/{task_id}")
async def remove_bookmark(
    task_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Remove bookmark by task_id"""
    bookmark = db.query(Bookmark).filter(
        Bookmark.user_id == current_user.id,
        Bookmark.task_id == task_id
    ).first()
    
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    
    db.delete(bookmark)
    db.commit()
    
    return {"status": "removed"}

@router.get("/check/{task_id}")
async def check_bookmark(
    task_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Check if a task is bookmarked"""
    bookmark = db.query(Bookmark).filter(
        Bookmark.user_id == current_user.id,
        Bookmark.task_id == task_id
    ).first()
    
    return {"is_bookmarked": bookmark is not None}

@router.delete("")
async def clear_all_bookmarks(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Clear all bookmarks for current user"""
    db.query(Bookmark).filter(
        Bookmark.user_id == current_user.id
    ).delete()
    db.commit()
    
    return {"status": "cleared"}
```

### Frontend

#### Hook: `apps/frontend/src/hooks/useBookmarks.ts`

```typescript
import { useState, useEffect, useCallback } from 'react';
import { api } from '@/lib/api';

interface Bookmark {
  id: string;
  task_id: string;
  task_title: string;
  module_slug: string;
  module_name: string;
  created_at: string;
}

export function useBookmarks() {
  const [bookmarks, setBookmarks] = useState<Bookmark[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchBookmarks = useCallback(async () => {
    try {
      const response = await api.get('/api/bookmarks');
      setBookmarks(response.data.bookmarks);
    } catch (error) {
      console.error('Failed to fetch bookmarks:', error);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchBookmarks();
  }, [fetchBookmarks]);

  const toggleBookmark = async (taskId: string) => {
    const isBookmarked = bookmarks.some(b => b.task_id === taskId);
    
    if (isBookmarked) {
      await api.delete(`/api/bookmarks/${taskId}`);
      setBookmarks(prev => prev.filter(b => b.task_id !== taskId));
    } else {
      const response = await api.post('/api/bookmarks', { task_id: taskId });
      setBookmarks(prev => [...prev, response.data]);
    }
  };

  const isBookmarked = (taskId: string) => {
    return bookmarks.some(b => b.task_id === taskId);
  };

  const clearAll = async () => {
    await api.delete('/api/bookmarks');
    setBookmarks([]);
  };

  // Group by module for sidebar display
  const groupedByModule = bookmarks.reduce((acc, bookmark) => {
    const key = bookmark.module_slug;
    if (!acc[key]) {
      acc[key] = {
        module_name: bookmark.module_name,
        tasks: []
      };
    }
    acc[key].tasks.push(bookmark);
    return acc;
  }, {} as Record<string, { module_name: string; tasks: Bookmark[] }>);

  return {
    bookmarks,
    groupedByModule,
    loading,
    toggleBookmark,
    isBookmarked,
    clearAll,
    refresh: fetchBookmarks
  };
}
```

#### Component: `apps/frontend/src/components/BookmarkSidebar.tsx`

```tsx
'use client';

import { Star, Trash2 } from 'lucide-react';
import Link from 'next/link';
import { useBookmarks } from '@/hooks/useBookmarks';

export function BookmarkSidebar() {
  const { groupedByModule, loading, clearAll, bookmarks } = useBookmarks();

  if (loading) {
    return (
      <div className="p-4 text-gray-400">
        Laddar...
      </div>
    );
  }

  if (bookmarks.length === 0) {
    return (
      <div className="p-4 text-center">
        <Star className="w-8 h-8 mx-auto mb-2 text-gray-600" />
        <h3 className="text-sm font-medium text-gray-300 mb-1">
          Sparade tasks
        </h3>
        <p className="text-xs text-gray-500">
          Du har inga sparade tasks än.
          Klicka på ⭐ vid en task för att spara den här.
        </p>
      </div>
    );
  }

  return (
    <div className="p-4">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-sm font-medium text-gray-300 flex items-center gap-2">
          <Star className="w-4 h-4 text-yellow-500" />
          Sparade tasks ({bookmarks.length})
        </h3>
        <button
          onClick={clearAll}
          className="text-xs text-gray-500 hover:text-red-400 flex items-center gap-1"
        >
          <Trash2 className="w-3 h-3" />
          Rensa
        </button>
      </div>

      <div className="space-y-4">
        {Object.entries(groupedByModule).map(([slug, { module_name, tasks }]) => (
          <div key={slug}>
            <h4 className="text-xs font-medium text-gray-400 mb-2">
              {module_name}
            </h4>
            <ul className="space-y-1">
              {tasks.map(task => (
                <li key={task.id}>
                  <Link
                    href={`/modules/${slug}/tasks/${task.task_id}`}
                    className="text-sm text-gray-300 hover:text-white block py-1 px-2 rounded hover:bg-gray-800"
                  >
                    {task.task_title}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}
```

#### Component: `apps/frontend/src/components/BookmarkButton.tsx`

```tsx
'use client';

import { Star } from 'lucide-react';
import { useBookmarks } from '@/hooks/useBookmarks';

interface BookmarkButtonProps {
  taskId: string;
  className?: string;
}

export function BookmarkButton({ taskId, className = '' }: BookmarkButtonProps) {
  const { isBookmarked, toggleBookmark } = useBookmarks();
  const bookmarked = isBookmarked(taskId);

  return (
    <button
      onClick={() => toggleBookmark(taskId)}
      className={`transition-colors ${className}`}
      aria-label={bookmarked ? 'Ta bort bokmärke' : 'Lägg till bokmärke'}
    >
      <Star
        className={`w-5 h-5 ${
          bookmarked
            ? 'text-yellow-500 fill-yellow-500'
            : 'text-gray-500 hover:text-yellow-400'
        }`}
      />
    </button>
  );
}
```

### Migration

```python
# alembic/versions/003_add_bookmarks.py

def upgrade():
    op.create_table(
        'bookmarks',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('task_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('tasks.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.UniqueConstraint('user_id', 'task_id', name='unique_user_task_bookmark')
    )
    op.create_index('ix_bookmarks_user_id', 'bookmarks', ['user_id'])

def downgrade():
    op.drop_table('bookmarks')
```

## SUCCESS CRITERIA

- [ ] Bookmark API endpoints fungerar
- [ ] Star-knapp på varje task card
- [ ] Sidebar visar bookmarkade tasks grupperat per modul
- [ ] Bookmarks persisteras i databasen
- [ ] "Rensa alla" fungerar

## COMMIT MESSAGE

```
feat(bookmarks): add task bookmark/star system

Backend:
- Added Bookmark model and schema
- Created /api/bookmarks endpoints (CRUD)
- Added database migration

Frontend:
- Created useBookmarks hook
- Added BookmarkSidebar component
- Added BookmarkButton component
- Replaced static sidebar with dynamic bookmarks

Closes #XXX
```

## NÄSTA STEG

Fortsätt med PROMPT_5_validation_system.md för att lägga till rättningsfunktion.
