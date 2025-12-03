"""
Task Service - Business logic for task operations
Phase 3.0: Tasks Foundation
Phase 4.0: Added related tasks (fördjupning) support
"""
from uuid import UUID
from typing import List

from ..schemas.task import TaskCreate, TaskUpdate, TaskPublic, TaskWithRelated
from ..core.exceptions import raise_conflict, raise_not_found
from ..db import task_repository, module_repository


class TaskService:
    """
    Task service handles all task-related business logic.

    Phase 3.0: Uses repository layer with in-memory storage
    Phase 4.0: Added support for task tiers and related tasks (fördjupning)
    Phase 5+: Repository will use SQLAlchemy + PostgreSQL
    """

    def _to_task_public(self, task) -> TaskPublic:
        """Convert a task model to TaskPublic schema."""
        return TaskPublic(
            id=task.id,
            module_id=task.module_id,
            title=task.title,
            description=task.description,
            content=task.content,
            content_blocks=task.content_blocks,
            requirements=task.requirements,
            order_index=task.order_index,
            difficulty=task.difficulty,
            estimated_minutes=task.estimated_minutes,
            xp_reward=task.xp_reward,
            is_active=task.is_active,
            task_tier=getattr(task, 'task_tier', 'standard'),
            parent_task_id=getattr(task, 'parent_task_id', None),
            created_at=task.created_at,
            updated_at=task.updated_at,
        )

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

        return self._to_task_public(task)

    def list_tasks(self) -> list[TaskPublic]:
        """
        List all tasks.

        Returns:
            List of TaskPublic objects
        """
        tasks = task_repository.list_tasks()
        return [
            self._to_task_public(t)
            for t in sorted(tasks, key=lambda x: x.order_index)
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
            self._to_task_public(t)
            for t in sorted(tasks, key=lambda x: x.order_index)
        ]

    def list_tasks_for_module_slug(self, module_slug: str) -> list[TaskPublic]:
        """
        List all tasks for a module identified by slug.

        Args:
            module_slug: The slug of the module (e.g., 'linux-mastery')

        Returns:
            List of TaskPublic objects

        Raises:
            HTTPException 404: If module not found
        """
        module = module_repository.get_module_by_slug(module_slug)
        if not module:
            raise_not_found(f"Module with slug '{module_slug}' not found")

        tasks = task_repository.list_tasks_by_module(module.id)
        return [
            self._to_task_public(t)
            for t in sorted(tasks, key=lambda x: x.order_index)
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

        return self._to_task_public(task)

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

        return self._to_task_public(task)

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

    def get_related_tasks(self, task_id: UUID) -> List[TaskPublic]:
        """
        Get related advanced/deep-dive tasks for a task.

        Returns tasks where parent_task_id matches the given task_id.
        These are optional "fördjupning" tasks that users can try anytime.

        Args:
            task_id: The UUID of the parent task

        Returns:
            List of related TaskPublic objects (advanced/deep_dive tier)

        Raises:
            HTTPException 404: If task not found
        """
        # Validate task exists
        task = task_repository.get_task_by_id(task_id)
        if not task:
            raise_not_found(f"Task with id {task_id} not found")

        # Get related tasks from repository
        related = task_repository.get_tasks_by_parent_id(task_id)
        return [
            self._to_task_public(t)
            for t in sorted(related, key=lambda x: x.order_index)
        ]

    def get_task_with_related(self, task_id: UUID) -> TaskWithRelated:
        """
        Get a task with its related advanced/deep-dive tasks included.

        Args:
            task_id: The UUID of the task to retrieve

        Returns:
            TaskWithRelated object with task data + related_tasks array

        Raises:
            HTTPException 404: If task not found
        """
        task = task_repository.get_task_by_id(task_id)
        if not task:
            raise_not_found(f"Task with id {task_id} not found")

        related = task_repository.get_tasks_by_parent_id(task_id)
        related_public = [
            self._to_task_public(t)
            for t in sorted(related, key=lambda x: x.order_index)
        ]

        return TaskWithRelated(
            id=task.id,
            module_id=task.module_id,
            title=task.title,
            description=task.description,
            content=task.content,
            content_blocks=task.content_blocks,
            requirements=task.requirements,
            order_index=task.order_index,
            difficulty=task.difficulty,
            estimated_minutes=task.estimated_minutes,
            xp_reward=task.xp_reward,
            is_active=task.is_active,
            task_tier=getattr(task, 'task_tier', 'standard'),
            parent_task_id=getattr(task, 'parent_task_id', None),
            created_at=task.created_at,
            updated_at=task.updated_at,
            related_tasks=related_public,
        )


# Singleton instance
task_service = TaskService()
