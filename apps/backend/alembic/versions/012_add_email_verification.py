"""Add email verification columns

Revision ID: 012_add_email_verification
Revises: 011_add_activity_logs
Create Date: 2026-01-19
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers
revision = '012_add_email_verification'
down_revision = '011_add_activity_logs'
branch_labels = None
depends_on = None


def upgrade():
    """Add verification_code and verification_code_expires_at columns to users table"""
    # Add verification_code column
    op.add_column('users', sa.Column('verification_code', sa.String(6), nullable=True))
    
    # Add verification_code_expires_at column
    op.add_column('users', sa.Column('verification_code_expires_at', sa.DateTime(), nullable=True))
    
    print("✅ Added email verification columns to users table")


def downgrade():
    """Remove email verification columns"""
    op.drop_column('users', 'verification_code_expires_at')
    op.drop_column('users', 'verification_code')
    
    print("✅ Removed email verification columns from users table")
