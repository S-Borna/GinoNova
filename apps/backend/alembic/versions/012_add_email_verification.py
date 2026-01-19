"""Add email verification columns

Revision ID: 012_add_email_verification
Revises: 011_add_activity_logs
Create Date: 2026-01-19
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect


# revision identifiers
revision = '012_add_email_verification'
down_revision = '011_add_activity_logs'
branch_labels = None
depends_on = None


def column_exists(table_name, column_name):
    """Check if a column exists in a table"""
    bind = op.get_bind()
    inspector = inspect(bind)
    columns = [c['name'] for c in inspector.get_columns(table_name)]
    return column_name in columns


def upgrade():
    """Add verification_code and verification_code_expires_at columns to users table"""
    # Add verification_code column if it doesn't exist
    if not column_exists('users', 'verification_code'):
        op.add_column('users', sa.Column('verification_code', sa.String(6), nullable=True))
        print("✅ Added verification_code column")
    else:
        print("⏭️  verification_code column already exists")

    # Add verification_code_expires_at column if it doesn't exist
    if not column_exists('users', 'verification_code_expires_at'):
        op.add_column('users', sa.Column('verification_code_expires_at', sa.DateTime(), nullable=True))
        print("✅ Added verification_code_expires_at column")
    else:
        print("⏭️  verification_code_expires_at column already exists")


def downgrade():
    """Remove email verification columns"""
    if column_exists('users', 'verification_code_expires_at'):
        op.drop_column('users', 'verification_code_expires_at')
    if column_exists('users', 'verification_code'):
        op.drop_column('users', 'verification_code')

    print("✅ Removed email verification columns from users table")
