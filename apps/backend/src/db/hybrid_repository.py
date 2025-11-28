"""
Hybrid Repository - Supports both in-memory and PostgreSQL
Automatically uses PostgreSQL if DATABASE_URL is set, otherwise falls back to in-memory
"""
from typing import Optional, List, TypeVar, Generic
from uuid import UUID
from sqlalchemy.orm import Session
from .database import is_db_configured, get_db_context
from . import models

T = TypeVar('T')


class HybridRepository(Generic[T]):
    """Base class for hybrid repositories"""

    def __init__(self, model_class, memory_db: dict):
        self.model_class = model_class
        self.memory_db = memory_db
        self.use_postgres = is_db_configured()

    def _to_dict(self, obj) -> dict:
        """Convert SQLAlchemy model to dict"""
        if hasattr(obj, '__table__'):
            return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
        return obj.__dict__ if hasattr(obj, '__dict__') else {}


# ==============================================================================
# USER REPOSITORY
# ==============================================================================

from .user_repository import _users_db

class UserRepository:
    """Hybrid user repository"""

    def __init__(self):
        self.use_postgres = is_db_configured()

    def get_by_id(self, user_id: UUID) -> Optional[models.User]:
        if self.use_postgres:
            with get_db_context() as db:
                return db.query(models.User).filter(models.User.id == user_id).first()
        else:
            from .user_repository import get_user_by_id
            return get_user_by_id(user_id)

    def get_by_email(self, email: str) -> Optional[models.User]:
        if self.use_postgres:
            with get_db_context() as db:
                return db.query(models.User).filter(models.User.email == email.lower()).first()
        else:
            from .user_repository import get_user_by_email
            return get_user_by_email(email)

    def create(self, user_data: dict) -> models.User:
        if self.use_postgres:
            with get_db_context() as db:
                user = models.User(**user_data)
                db.add(user)
                db.commit()
                db.refresh(user)
                return user
        else:
            from .user_repository import create_user
            from ..schemas.user import UserCreate
            return create_user(UserCreate(**user_data))

    def update(self, user_id: UUID, update_data: dict) -> Optional[models.User]:
        if self.use_postgres:
            with get_db_context() as db:
                user = db.query(models.User).filter(models.User.id == user_id).first()
                if user:
                    for key, value in update_data.items():
                        if value is not None:
                            setattr(user, key, value)
                    db.commit()
                    db.refresh(user)
                return user
        else:
            from .user_repository import update_user
            from ..schemas.user import UserUpdate
            return update_user(user_id, UserUpdate(**update_data))

    def list_all(self) -> List[models.User]:
        if self.use_postgres:
            with get_db_context() as db:
                return db.query(models.User).all()
        else:
            from .user_repository import list_users
            return list_users()


# ==============================================================================
# PROGRESS REPOSITORY
# ==============================================================================

class ProgressRepository:
    """Hybrid progress repository"""

    def __init__(self):
        self.use_postgres = is_db_configured()

    def get_by_user(self, user_id: UUID) -> List[models.Progress]:
        if self.use_postgres:
            with get_db_context() as db:
                return db.query(models.Progress).filter(models.Progress.user_id == user_id).all()
        else:
            from .progress_repository import list_progress_by_user
            return list_progress_by_user(user_id)

    def get_by_user_and_task(self, user_id: UUID, task_id: UUID) -> Optional[models.Progress]:
        if self.use_postgres:
            with get_db_context() as db:
                return db.query(models.Progress).filter(
                    models.Progress.user_id == user_id,
                    models.Progress.task_id == task_id
                ).first()
        else:
            from .progress_repository import get_progress_by_user_and_task
            return get_progress_by_user_and_task(user_id, task_id)

    def create(self, progress_data: dict) -> models.Progress:
        if self.use_postgres:
            with get_db_context() as db:
                progress = models.Progress(**progress_data)
                db.add(progress)
                db.commit()
                db.refresh(progress)
                return progress
        else:
            from .progress_repository import create_progress
            from ..schemas.progress import ProgressCreate
            return create_progress(ProgressCreate(**progress_data))

    def update(self, progress_id: UUID, update_data: dict) -> Optional[models.Progress]:
        if self.use_postgres:
            with get_db_context() as db:
                progress = db.query(models.Progress).filter(models.Progress.id == progress_id).first()
                if progress:
                    for key, value in update_data.items():
                        if value is not None:
                            setattr(progress, key, value)
                    db.commit()
                    db.refresh(progress)
                return progress
        else:
            from .progress_repository import update_progress
            from ..schemas.progress import ProgressUpdate
            return update_progress(progress_id, ProgressUpdate(**update_data))

    def delete_by_user(self, user_id: UUID) -> int:
        """Delete all progress for a user (for reset). Returns count deleted."""
        if self.use_postgres:
            with get_db_context() as db:
                count = db.query(models.Progress).filter(models.Progress.user_id == user_id).delete()
                db.commit()
                return count
        else:
            from .progress_repository import list_progress_by_user, delete_progress
            progress_list = list_progress_by_user(user_id)
            for p in progress_list:
                delete_progress(p.id)
            return len(progress_list)


# ==============================================================================
# MODULE REPOSITORY
# ==============================================================================

class ModuleRepository:
    """Hybrid module repository"""

    def __init__(self):
        self.use_postgres = is_db_configured()

    def get_all(self) -> List[models.Module]:
        if self.use_postgres:
            with get_db_context() as db:
                return db.query(models.Module).order_by(models.Module.order_index).all()
        else:
            from .module_repository import list_modules
            return list_modules()

    def get_by_id(self, module_id: UUID) -> Optional[models.Module]:
        if self.use_postgres:
            with get_db_context() as db:
                return db.query(models.Module).filter(models.Module.id == module_id).first()
        else:
            from .module_repository import get_module_by_id
            return get_module_by_id(module_id)


# ==============================================================================
# TASK REPOSITORY
# ==============================================================================

class TaskRepository:
    """Hybrid task repository"""

    def __init__(self):
        self.use_postgres = is_db_configured()

    def get_all(self) -> List[models.Task]:
        if self.use_postgres:
            with get_db_context() as db:
                return db.query(models.Task).order_by(models.Task.order_index).all()
        else:
            from .task_repository import list_tasks
            return list_tasks()

    def get_by_id(self, task_id: UUID) -> Optional[models.Task]:
        if self.use_postgres:
            with get_db_context() as db:
                return db.query(models.Task).filter(models.Task.id == task_id).first()
        else:
            from .task_repository import get_task_by_id
            return get_task_by_id(task_id)

    def get_by_module(self, module_id: UUID) -> List[models.Task]:
        if self.use_postgres:
            with get_db_context() as db:
                return db.query(models.Task).filter(
                    models.Task.module_id == module_id
                ).order_by(models.Task.order_index).all()
        else:
            from .task_repository import list_tasks_by_module
            return list_tasks_by_module(module_id)


# ==============================================================================
# SINGLETON INSTANCES
# ==============================================================================

user_repo = UserRepository()
progress_repo = ProgressRepository()
module_repo = ModuleRepository()
task_repo = TaskRepository()
