"""
Task Service - Business logic for task operations
Phase 3.0: Tasks Foundation
"""
from uuid import UUID

from ..schemas.task import TaskCreate, TaskUpdate, TaskPublic
from ..core.exceptions import raise_conflict, raise_not_found
from ..db import task_repository, module_repository


class TaskService:
    """
    Task service handles all task-related business logic.

    Phase 3.0: Uses repository layer with in-memory storage
    Phase 4+: Repository will use SQLAlchemy + PostgreSQL
    """

    def _validate_module_exists(self, module_id: UUID) -> None:
        """
        Validate that a module exists.

        Args:
            module_id: The UUID of the module to validate

        Raises:
            HTTPException 404: If module not found
        """
        module = module_repository.get_module_by_id(module_id)
        if not module:
            raise_not_found(f"Module with id {module_id} not found")

    def get_task_by_id(self, task_id: UUID) -> TaskPublic:
        """
        Get a task by its UUID.

        Args:
            task_id: The UUID of the task to retrieve

        Returns:
            TaskPublic object

        Raises:
            HTTPException 404: If task not found
        """
        task = task_repository.get_task_by_id(task_id)
        if not task:
            raise_not_found(f"Task with id {task_id} not found")

        return TaskPublic(
            id=task.id,
            module_id=task.module_id,
            title=task.title,
            description=task.description,
            difficulty=task.difficulty,
            is_active=task.is_active,
            created_at=task.created_at,
            updated_at=task.updated_at,
        )

    def list_tasks(self) -> list[TaskPublic]:
        """
        List all tasks.

        Returns:
            List of TaskPublic objects
        """
        tasks = task_repository.list_tasks()
        return [
            TaskPublic(
                id=t.id,
                module_id=t.module_id,
                title=t.title,
                description=t.description,
                difficulty=t.difficulty,
                is_active=t.is_active,
                created_at=t.created_at,
                updated_at=t.updated_at,
            )
            for t in tasks
        ]

    def list_tasks_for_module(self, module_id: UUID) -> list[TaskPublic]:
        """
        List all tasks for a specific module.

        Args:
            module_id: The UUID of the module

        Returns:
            List of TaskPublic objects

        Raises:
            HTTPException 404: If module not found
        """
        self._validate_module_exists(module_id)

        tasks = task_repository.list_tasks_by_module(module_id)
        return [
            TaskPublic(
                id=t.id,
                module_id=t.module_id,
                title=t.title,
                description=t.description,
                difficulty=t.difficulty,
                is_active=t.is_active,
                created_at=t.created_at,
                updated_at=t.updated_at,
            )
            for t in tasks
        ]

    def create_task(self, data: TaskCreate) -> TaskPublic:
        """
        Create a new task.

        Args:
            data: TaskCreate schema with task data

        Returns:
            TaskPublic object of the created task

        Raises:
            HTTPException 404: If module not found
            HTTPException 409: If task title already exists for this module
        """
        # Validate module exists
        self._validate_module_exists(data.module_id)

        # Check for duplicate title within module
        existing = task_repository.get_task_by_title_and_module(
            data.title, data.module_id
        )
        if existing:
            raise_conflict(
                f"Task with title '{data.title}' already exists in this module"
            )

        task = task_repository.create_task(data)

        return TaskPublic(
            id=task.id,
            module_id=task.module_id,
            title=task.title,
            description=task.description,
            difficulty=task.difficulty,
            is_active=task.is_active,
            created_at=task.created_at,
            updated_at=task.updated_at,
        )

    def update_task(self, task_id: UUID, data: TaskUpdate) -> TaskPublic:
        """
        Update an existing task.

        Args:
            task_id: The UUID of the task to update
            data: TaskUpdate schema with fields to update

        Returns:
            TaskPublic object of the updated task

        Raises:
            HTTPException 404: If task not found
            HTTPException 409: If new title conflicts with existing task in same module
        """
        # Check if task exists
        existing = task_repository.get_task_by_id(task_id)
        if not existing:
            raise_not_found(f"Task with id {task_id} not found")

        # Check for title conflict if title is being updated
        if data.title is not None and data.title.strip().lower() != existing.title.lower():
            title_conflict = task_repository.get_task_by_title_and_module(
                data.title, existing.module_id
            )
            if title_conflict:
                raise_conflict(
                    f"Task with title '{data.title}' already exists in this module"
                )

        task = task_repository.update_task(task_id, data)
        if not task:
            raise_not_found(f"Task with id {task_id} not found")

        return TaskPublic(
            id=task.id,
            module_id=task.module_id,
            title=task.title,
            description=task.description,
            difficulty=task.difficulty,
            is_active=task.is_active,
            created_at=task.created_at,
            updated_at=task.updated_at,
        )

    def delete_task(self, task_id: UUID) -> bool:
        """
        Delete a task by its UUID.

        Args:
            task_id: The UUID of the task to delete

        Returns:
            True if deleted successfully

        Raises:
            HTTPException 404: If task not found
        """
        # Check if task exists
        existing = task_repository.get_task_by_id(task_id)
        if not existing:
            raise_not_found(f"Task with id {task_id} not found")

        deleted = task_repository.delete_task(task_id)
        if not deleted:
            raise_not_found(f"Task with id {task_id} not found")

        return True


# Singleton instance
task_service = TaskService()
