"""
Module Service - Business logic for module operations
Phase 2.0: Modules Foundation
"""
from uuid import UUID

from ..schemas.module import ModuleCreate, ModuleUpdate, ModulePublic
from ..core.exceptions import raise_conflict, raise_not_found
from ..db import module_repository


class ModuleService:
    """
    Module service handles all module-related business logic.

    Phase 2.0: Uses repository layer with in-memory storage
    Phase 3+: Repository will use SQLAlchemy + PostgreSQL
    """

    def get_module_by_id(self, module_id: UUID) -> ModulePublic:
        """
        Get a module by its UUID.

        Args:
            module_id: The UUID of the module to retrieve

        Returns:
            ModulePublic object

        Raises:
            HTTPException 404: If module not found
        """
        module = module_repository.get_module_by_id(module_id)
        if not module:
            raise_not_found(f"Module with id {module_id} not found")

        return ModulePublic(
            id=module.id,
            name=module.name,
            slug=getattr(module, 'slug', module.name.lower().replace(' ', '-')),
            description=module.description,
            order_index=getattr(module, 'order_index', 1),
            difficulty=getattr(module, 'difficulty', 'intermediate'),
            estimated_hours=getattr(module, 'estimated_hours', 10.0),
            prerequisites=getattr(module, 'prerequisites', []),
            is_active=module.is_active,
            track_id=getattr(module, 'track_id', None),
            created_at=module.created_at,
            updated_at=module.updated_at,
        )

    def get_module_by_slug(self, slug: str) -> ModulePublic:
        """
        Get a module by its slug.

        Args:
            slug: The slug of the module to retrieve

        Returns:
            ModulePublic object

        Raises:
            HTTPException 404: If module not found
        """
        module = module_repository.get_module_by_slug(slug)
        if not module:
            raise_not_found(f"Module with slug '{slug}' not found")

        return ModulePublic(
            id=module.id,
            name=module.name,
            slug=getattr(module, 'slug', module.name.lower().replace(' ', '-')),
            description=module.description,
            order_index=getattr(module, 'order_index', 1),
            difficulty=getattr(module, 'difficulty', 'intermediate'),
            estimated_hours=getattr(module, 'estimated_hours', 10.0),
            prerequisites=getattr(module, 'prerequisites', []),
            is_active=module.is_active,
            track_id=getattr(module, 'track_id', None),
            created_at=module.created_at,
            updated_at=module.updated_at,
        )

    def list_modules(self) -> list[ModulePublic]:
        """
        List all modules.

        Returns:
            List of ModulePublic objects
        """
        modules = module_repository.list_modules()
        return [
            ModulePublic(
                id=m.id,
                name=m.name,
                slug=getattr(m, 'slug', m.name.lower().replace(' ', '-')),
                description=m.description,
                order_index=getattr(m, 'order_index', 1),
                difficulty=getattr(m, 'difficulty', 'intermediate'),
                estimated_hours=getattr(m, 'estimated_hours', 10.0),
                prerequisites=getattr(m, 'prerequisites', []),
                is_active=m.is_active,
                track_id=getattr(m, 'track_id', None),
                created_at=m.created_at,
                updated_at=m.updated_at,
            )
            for m in modules
        ]

    def create_module(self, data: ModuleCreate) -> ModulePublic:
        """
        Create a new module.

        Args:
            data: ModuleCreate schema with module data

        Returns:
            ModulePublic object of the created module

        Raises:
            HTTPException 409: If module name already exists
        """
        # Check for duplicate name
        existing = module_repository.get_module_by_name(data.name)
        if existing:
            raise_conflict(f"Module with name '{data.name}' already exists")

        module = module_repository.create_module(data)

        return ModulePublic(
            id=module.id,
            name=module.name,
            slug=getattr(module, 'slug', module.name.lower().replace(' ', '-')),
            description=module.description,
            order_index=getattr(module, 'order_index', 1),
            difficulty=getattr(module, 'difficulty', 'intermediate'),
            estimated_hours=getattr(module, 'estimated_hours', 10.0),
            prerequisites=getattr(module, 'prerequisites', []),
            is_active=module.is_active,
            track_id=getattr(module, 'track_id', None),
            created_at=module.created_at,
            updated_at=module.updated_at,
        )

    def update_module(self, module_id: UUID, data: ModuleUpdate) -> ModulePublic:
        """
        Update an existing module.

        Args:
            module_id: The UUID of the module to update
            data: ModuleUpdate schema with fields to update

        Returns:
            ModulePublic object of the updated module

        Raises:
            HTTPException 404: If module not found
            HTTPException 409: If new name conflicts with existing module
        """
        # Check if module exists
        existing = module_repository.get_module_by_id(module_id)
        if not existing:
            raise_not_found(f"Module with id {module_id} not found")

        # Check for name conflict if name is being updated
        if data.name is not None and data.name.strip().lower() != existing.name.lower():
            name_conflict = module_repository.get_module_by_name(data.name)
            if name_conflict:
                raise_conflict(f"Module with name '{data.name}' already exists")

        module = module_repository.update_module(module_id, data)
        if not module:
            raise_not_found(f"Module with id {module_id} not found")

        return ModulePublic(
            id=module.id,
            name=module.name,
            slug=getattr(module, 'slug', module.name.lower().replace(' ', '-')),
            description=module.description,
            order_index=getattr(module, 'order_index', 1),
            difficulty=getattr(module, 'difficulty', 'intermediate'),
            estimated_hours=getattr(module, 'estimated_hours', 10.0),
            prerequisites=getattr(module, 'prerequisites', []),
            is_active=module.is_active,
            track_id=getattr(module, 'track_id', None),
            created_at=module.created_at,
            updated_at=module.updated_at,
        )

    def delete_module(self, module_id: UUID) -> bool:
        """
        Delete a module by its UUID.

        Args:
            module_id: The UUID of the module to delete

        Returns:
            True if deleted successfully

        Raises:
            HTTPException 404: If module not found
        """
        # Check if module exists
        existing = module_repository.get_module_by_id(module_id)
        if not existing:
            raise_not_found(f"Module with id {module_id} not found")

        deleted = module_repository.delete_module(module_id)
        if not deleted:
            raise_not_found(f"Module with id {module_id} not found")

        return True


# Singleton instance
module_service = ModuleService()
