"""Add OAuth fields to users table

Revision ID: 004_add_oauth_fields
Revises: 003_add_bookmarks
Create Date: 2025-12-03

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect


# revision identifiers, used by Alembic.
revision = '004_add_oauth_fields'
down_revision = '003_add_bookmarks'
branch_labels = None
depends_on = None


def column_exists(table_name, column_name):
    """Check if column exists in table."""
    bind = op.get_bind()
    inspector = inspect(bind)
    columns = [c['name'] for c in inspector.get_columns(table_name)]
    return column_name in columns


def upgrade() -> None:
    # Add OAuth provider fields to users table
    if not column_exists('users', 'oauth_provider'):
        op.add_column('users', sa.Column('oauth_provider', sa.String(50), nullable=True))
    if not column_exists('users', 'oauth_provider_id'):
        op.add_column('users', sa.Column('oauth_provider_id', sa.String(255), nullable=True))

    # Make hashed_password nullable for OAuth users
    try:
        op.alter_column('users', 'hashed_password',
                        existing_type=sa.String(255),
                        nullable=True)
    except Exception:
        pass  # Already nullable


def downgrade() -> None:
    # Remove OAuth fields
    op.drop_column('users', 'oauth_provider_id')
    op.drop_column('users', 'oauth_provider')

    # Make hashed_password required again
    op.alter_column('users', 'hashed_password',
                    existing_type=sa.String(255),
                    nullable=False)
