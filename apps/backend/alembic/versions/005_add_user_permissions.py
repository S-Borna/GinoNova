"""Add permissions column to users table

Revision ID: 005_add_user_permissions
Revises: 004_add_oauth_fields
Create Date: 2024-12-08

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision: str = '005_add_user_permissions'
down_revision: Union[str, None] = '004_add_oauth_fields'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def column_exists(table_name, column_name):
    """Check if column exists in table."""
    bind = op.get_bind()
    inspector = inspect(bind)
    columns = [c['name'] for c in inspector.get_columns(table_name)]
    return column_name in columns


def upgrade() -> None:
    # Add permissions JSON column with default value
    if column_exists('users', 'permissions'):
        return
    op.add_column('users', sa.Column(
        'permissions',
        sa.JSON(),
        nullable=True,
        server_default='{"ai_quiz": true, "premium_modules": true, "study_room": true, "skillpath": true}'
    ))

    # Update existing users to have default permissions
    op.execute("""
        UPDATE users
        SET permissions = '{"ai_quiz": true, "premium_modules": true, "study_room": true, "skillpath": true}'::jsonb
        WHERE permissions IS NULL
    """)


def downgrade() -> None:
    op.drop_column('users', 'permissions')
