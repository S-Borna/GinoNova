"""Add last_login_at field to users

Revision ID: 007_add_last_login
Revises: 006_add_ai_usage_logs
Create Date: 2026-01-05
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect

# revision identifiers
revision = '007_add_last_login'
down_revision = '006_add_ai_usage_logs'
branch_labels = None
depends_on = None


def column_exists(table_name, column_name):
    """Check if column exists in table."""
    bind = op.get_bind()
    inspector = inspect(bind)
    columns = [c['name'] for c in inspector.get_columns(table_name)]
    return column_name in columns


def upgrade():
    # Add last_login_at column to users table
    if column_exists('users', 'last_login_at'):
        return
    op.add_column('users', sa.Column('last_login_at', sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column('users', 'last_login_at')
