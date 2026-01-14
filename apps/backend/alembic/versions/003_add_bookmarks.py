"""Add bookmarks table for task starring

Revision ID: 003_add_bookmarks
Revises: 002_add_task_tier_parent
Create Date: 2025-12-01

PROMPT 4: Sidebar Bookmark System
- bookmarks table for user task starring
- Unique constraint on user_id + task_id
- Indexes for efficient queries
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy import inspect


# revision identifiers, used by Alembic.
revision = '003_add_bookmarks'
down_revision = '002_add_task_tier_parent'
branch_labels = None
depends_on = None


def table_exists(table_name):
    """Check if table exists in database."""
    bind = op.get_bind()
    inspector = inspect(bind)
    return table_name in inspector.get_table_names()


def upgrade():
    """Create bookmarks table."""
    if table_exists('bookmarks'):
        return
    op.create_table(
        'bookmarks',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('task_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('tasks.id', ondelete='CASCADE'), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
    )

    # Index for getting all bookmarks for a user
    op.create_index('ix_bookmarks_user_id', 'bookmarks', ['user_id'])

    # Unique constraint: user can only bookmark a task once
    op.create_index('ix_bookmarks_user_task', 'bookmarks', ['user_id', 'task_id'], unique=True)


def downgrade():
    """Drop bookmarks table."""
    op.drop_index('ix_bookmarks_user_task', table_name='bookmarks')
    op.drop_index('ix_bookmarks_user_id', table_name='bookmarks')
    op.drop_table('bookmarks')
