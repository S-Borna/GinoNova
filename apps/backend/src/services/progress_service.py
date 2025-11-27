"""
Progress Service - Business logic for progress tracking
Phase 5.0: Progress Engine Foundation
"""
from uuid import UUID

from ..schemas.progress import ProgressCreate, ProgressUpdate, ProgressPublic
from ..core.exceptions import raise_conflict, raise_not_found
from ..db import progress_repository, module_repository, task_repository, studyflow_repository
from ..models.progress import sync_status_from_progress


class ProgressService:
    """
    Progress service handles all progress-related business logic.

    Phase 5.0: Uses repository layer with in-memory storage
    """

    def _validate_target_exists(
        self,
        module_id: UUID | None,
        task_id: UUID | None,
        studyflow_id: UUID | None,
    ) -> None:
        """
        Validate that the target (module/task/studyflow) exists.

        Args:
            module_id: Optional module UUID
            task_id: Optional task UUID
            studyflow_id: Optional studyflow UUID

        Raises:
            HTTPException 404: If target not found
        """
        if module_id:
            module = module_repository.get_module_by_id(module_id)
            if not module:
                raise_not_found(f"Module with id {module_id} not found")

        if task_id:
            task = task_repository.get_task_by_id(task_id)
            if not task:
                raise_not_found(f"Task with id {task_id} not found")

        if studyflow_id:
            studyflow = studyflow_repository.get_studyflow_by_id(studyflow_id)
            if not studyflow:
                raise_not_found(f"Studyflow with id {studyflow_id} not found")

    def _to_public(self, p: "ProgressPublic") -> ProgressPublic:
        """Convert internal model to public schema"""
        return ProgressPublic(
            id=p.id,
            user_id=p.user_id,
            module_id=p.module_id,
            task_id=p.task_id,
            studyflow_id=p.studyflow_id,
            status=p.status,
            progress=p.progress,
            created_at=p.created_at,
            updated_at=p.updated_at,
        )

    def get_progress_by_id(self, progress_id: UUID) -> ProgressPublic:
        """
        Get a progress record by its UUID.

        Args:
            progress_id: The UUID of the progress record to retrieve

        Returns:
            ProgressPublic object

        Raises:
            HTTPException 404: If progress record not found
        """
        progress = progress_repository.get_progress_by_id(progress_id)
        if not progress:
            raise_not_found(f"Progress record with id {progress_id} not found")

        return self._to_public(progress)

    def list_progress_for_user(self, user_id: UUID) -> list[ProgressPublic]:
        """
        List all progress records for a specific user.

        Args:
            user_id: The UUID of the user

        Returns:
            List of ProgressPublic objects
        """
        records = progress_repository.list_progress_by_user(user_id)
        return [self._to_public(p) for p in records]

    def create_progress(self, data: ProgressCreate) -> ProgressPublic:
        """
        Create a new progress record.

        Args:
            data: ProgressCreate schema with progress data

        Returns:
            ProgressPublic object of the created record

        Raises:
            HTTPException 404: If target not found
            HTTPException 409: If progress already exists for user + target
        """
        # Validate target exists
        self._validate_target_exists(data.module_id, data.task_id, data.studyflow_id)

        # Check for duplicate (user + target)
        existing = progress_repository.get_progress_by_user_and_target(
            user_id=data.user_id,
            module_id=data.module_id,
            task_id=data.task_id,
            studyflow_id=data.studyflow_id,
        )
        if existing:
            target_type = "module" if data.module_id else "task" if data.task_id else "studyflow"
            raise_conflict(f"Progress already exists for this user and {target_type}")

        progress = progress_repository.create_progress(data)

        return self._to_public(progress)

    def update_progress(self, progress_id: UUID, data: ProgressUpdate) -> ProgressPublic:
        """
        Update an existing progress record.

        Args:
            progress_id: The UUID of the progress record to update
            data: ProgressUpdate schema with fields to update

        Returns:
            ProgressPublic object of the updated record

        Raises:
            HTTPException 404: If progress record not found
        """
        # Check if progress exists
        existing = progress_repository.get_progress_by_id(progress_id)
        if not existing:
            raise_not_found(f"Progress record with id {progress_id} not found")

        progress = progress_repository.update_progress(progress_id, data)
        if not progress:
            raise_not_found(f"Progress record with id {progress_id} not found")

        return self._to_public(progress)

    def delete_progress(self, progress_id: UUID) -> bool:
        """
        Delete a progress record by its UUID.

        Args:
            progress_id: The UUID of the progress record to delete

        Returns:
            True if deleted successfully

        Raises:
            HTTPException 404: If progress record not found
        """
        # Check if progress exists
        existing = progress_repository.get_progress_by_id(progress_id)
        if not existing:
            raise_not_found(f"Progress record with id {progress_id} not found")

        deleted = progress_repository.delete_progress(progress_id)
        if not deleted:
            raise_not_found(f"Progress record with id {progress_id} not found")

        return True


# Singleton instance
progress_service = ProgressService()
