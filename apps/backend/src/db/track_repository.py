"""
Track Repository - In-memory storage for tracks
Phase C.1: Seed Bootcamp v3.0 Content (Redo)
"""
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..schemas.track import TrackInDB, TrackCreate, TrackUpdate, create_track_in_db


# In-memory storage for tracks
_tracks_db: dict[UUID, TrackInDB] = {}


def get_track_by_id(track_id: UUID) -> Optional[TrackInDB]:
    """Get a track by its UUID."""
    return _tracks_db.get(track_id)


def get_track_by_slug(slug: str) -> Optional[TrackInDB]:
    """Get a track by its slug (case-insensitive)."""
    normalized_slug = slug.strip().lower()
    for track in _tracks_db.values():
        if track.slug.lower() == normalized_slug:
            return track
    return None


def list_tracks() -> list[TrackInDB]:
    """List all tracks ordered by order_index."""
    return sorted(_tracks_db.values(), key=lambda t: t.order_index)


def create_track(data: TrackCreate) -> TrackInDB:
    """Create a new track."""
    track = create_track_in_db(
        name=data.name,
        slug=data.slug,
        description=data.description,
        color=data.color,
        icon=data.icon,
        order_index=data.order_index,
    )
    _tracks_db[track.id] = track
    return track


def update_track(track_id: UUID, data: TrackUpdate) -> Optional[TrackInDB]:
    """Update an existing track."""
    existing = _tracks_db.get(track_id)
    if not existing:
        return None

    updated_data = existing.model_dump()
    update_fields = data.model_dump(exclude_unset=True)

    for field, value in update_fields.items():
        if value is not None:
            updated_data[field] = value

    updated_data["updated_at"] = datetime.utcnow()
    updated_track = TrackInDB(**updated_data)
    _tracks_db[track_id] = updated_track
    return updated_track


def delete_track(track_id: UUID) -> bool:
    """Delete a track by its UUID."""
    if track_id in _tracks_db:
        del _tracks_db[track_id]
        return True
    return False


def clear_tracks() -> None:
    """Clear all tracks (for testing/seeding)."""
    _tracks_db.clear()


def get_track_count() -> int:
    """Return number of tracks."""
    return len(_tracks_db)
