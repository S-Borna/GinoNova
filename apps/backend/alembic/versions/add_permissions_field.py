"""Add permissions field to users table

Revision ID: add_permissions_001
Revises:
Create Date: 2025-12-08
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSON

# revision identifiers
revision = 'add_permissions_001'
down_revision = '004_add_oauth_fields'
branch_labels = None
depends_on = None


def upgrade():
    # Add permissions column with default value (safe - check if exists first)
    from sqlalchemy import inspect
    from alembic import op

    conn = op.get_bind()
    inspector = inspect(conn)
    columns = [col['name'] for col in inspector.get_columns('users')]

    if 'permissions' not in columns:
        op.add_column('users', sa.Column('permissions', JSON, nullable=True))

        # Set default permissions for all existing users
        op.execute("""
            UPDATE users
            SET permissions = '{"ai_quiz": true, "premium_modules": true, "study_room": true, "skillpath": true}'::jsonb
            WHERE permissions IS NULL
        """)


def downgrade():
    # Safe downgrade - check if column exists
    from sqlalchemy import inspect
    
    conn = op.get_bind()
    inspector = inspect(conn)
    columns = [col['name'] for col in inspector.get_columns('users')]
    
    if 'permissions' in columns:
        op.drop_column('users', 'permissions')
