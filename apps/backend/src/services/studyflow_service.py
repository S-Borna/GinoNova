"""
Studyflow Service - Business logic for studyflow operations
Phase 4.0: Studyflow Foundation
"""
from uuid import UUID

from ..schemas.studyflow import StudyflowCreate, StudyflowUpdate, StudyflowPublic
from ..core.exceptions import raise_conflict, raise_not_found
from ..db import studyflow_repository, module_repository


class StudyflowService:
    """
    Studyflow service handles all studyflow-related business logic.

    Phase 4.0: Uses repository layer with in-memory storage
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

    def _to_public(self, sf: "StudyflowPublic") -> StudyflowPublic:
        """Convert internal model to public schema"""
        return StudyflowPublic(
            id=sf.id,
            module_id=sf.module_id,
            title=sf.title,
            description=sf.description,
            order=sf.order,
            is_active=sf.is_active,
            created_at=sf.created_at,
            updated_at=sf.updated_at,
        )

    def get_studyflow_by_id(self, studyflow_id: UUID) -> StudyflowPublic:
        """
        Get a studyflow by its UUID.

        Args:
            studyflow_id: The UUID of the studyflow to retrieve

        Returns:
            StudyflowPublic object

        Raises:
            HTTPException 404: If studyflow not found
        """
        studyflow = studyflow_repository.get_studyflow_by_id(studyflow_id)
        if not studyflow:
            raise_not_found(f"Studyflow with id {studyflow_id} not found")

        return self._to_public(studyflow)

    def list_studyflows(self) -> list[StudyflowPublic]:
        """
        List all studyflows.

        Returns:
            List of StudyflowPublic objects
        """
        studyflows = studyflow_repository.list_studyflows()
        return [self._to_public(sf) for sf in studyflows]

    def list_studyflows_for_module(self, module_id: UUID) -> list[StudyflowPublic]:
        """
        List all studyflows for a specific module.

        Args:
            module_id: The UUID of the module

        Returns:
            List of StudyflowPublic objects sorted by order

        Raises:
            HTTPException 404: If module not found
        """
        self._validate_module_exists(module_id)

        studyflows = studyflow_repository.list_studyflows_by_module(module_id)
        return [self._to_public(sf) for sf in studyflows]

    def create_studyflow(self, data: StudyflowCreate) -> StudyflowPublic:
        """
        Create a new studyflow.

        Args:
            data: StudyflowCreate schema with studyflow data

        Returns:
            StudyflowPublic object of the created studyflow

        Raises:
            HTTPException 404: If module not found
            HTTPException 409: If (module_id, order) already exists
        """
        # Validate module exists
        self._validate_module_exists(data.module_id)

        # Check for duplicate (module_id, order)
        existing = studyflow_repository.get_studyflow_by_module_and_order(
            data.module_id, data.order
        )
        if existing:
            raise_conflict(
                f"Studyflow with order {data.order} already exists in this module"
            )

        studyflow = studyflow_repository.create_studyflow(data)

        return self._to_public(studyflow)

    def update_studyflow(self, studyflow_id: UUID, data: StudyflowUpdate) -> StudyflowPublic:
        """
        Update an existing studyflow.

        Args:
            studyflow_id: The UUID of the studyflow to update
            data: StudyflowUpdate schema with fields to update

        Returns:
            StudyflowPublic object of the updated studyflow

        Raises:
            HTTPException 404: If studyflow not found
            HTTPException 409: If new order conflicts with existing studyflow in same module
        """
        # Check if studyflow exists
        existing = studyflow_repository.get_studyflow_by_id(studyflow_id)
        if not existing:
            raise_not_found(f"Studyflow with id {studyflow_id} not found")

        # Check for order conflict if order is being updated
        if data.order is not None and data.order != existing.order:
            order_conflict = studyflow_repository.get_studyflow_by_module_and_order(
                existing.module_id, data.order
            )
            if order_conflict:
                raise_conflict(
                    f"Studyflow with order {data.order} already exists in this module"
                )

        studyflow = studyflow_repository.update_studyflow(studyflow_id, data)
        if not studyflow:
            raise_not_found(f"Studyflow with id {studyflow_id} not found")

        return self._to_public(studyflow)

    def delete_studyflow(self, studyflow_id: UUID) -> bool:
        """
        Delete a studyflow by its UUID.

        Args:
            studyflow_id: The UUID of the studyflow to delete

        Returns:
            True if deleted successfully

        Raises:
            HTTPException 404: If studyflow not found
        """
        # Check if studyflow exists
        existing = studyflow_repository.get_studyflow_by_id(studyflow_id)
        if not existing:
            raise_not_found(f"Studyflow with id {studyflow_id} not found")

        deleted = studyflow_repository.delete_studyflow(studyflow_id)
        if not deleted:
            raise_not_found(f"Studyflow with id {studyflow_id} not found")

        return True


# Singleton instance
studyflow_service = StudyflowService()
