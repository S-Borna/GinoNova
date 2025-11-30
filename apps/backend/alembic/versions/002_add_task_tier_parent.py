"""Add task_tier and parent_task_id columns for related tasks (fördjupning)

Revision ID: 002_add_task_tier_parent
Revises: 001_initial_tables
Create Date: 2025-01-25

Phase 4.0: Task Tier System
- task_tier: standard (v3 content), advanced (v4 content), deep_dive
- parent_task_id: Links advanced tasks to their parent standard task
- Enables "Vill du fördjupa dig?" feature for optional related content
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_add_task_tier_parent'
down_revision = '001_initial_tables'
branch_labels = None
depends_on = None


def upgrade():
    """Add task_tier and parent_task_id columns to tasks table."""
    
    # Add task_tier column with default 'standard'
    op.add_column(
        'tasks',
        sa.Column(
            'task_tier',
            sa.String(20),
            nullable=False,
            server_default='standard',
            comment='Task tier: standard (v3), advanced (v4), or deep_dive'
        )
    )
    
    # Add parent_task_id for linking related tasks
    op.add_column(
        'tasks',
        sa.Column(
            'parent_task_id',
            sa.UUID(),
            sa.ForeignKey('tasks.id', ondelete='SET NULL'),
            nullable=True,
            comment='Parent task ID for linking fördjupning (advanced) content'
        )
    )
    
    # Add index for efficient parent_task_id lookups
    op.create_index(
        'ix_tasks_parent_task_id',
        'tasks',
        ['parent_task_id']
    )
    
    # Add index for task_tier filtering
    op.create_index(
        'ix_tasks_task_tier',
        'tasks',
        ['task_tier']
    )


def downgrade():
    """Remove task_tier and parent_task_id columns."""
    
    # Drop indexes first
    op.drop_index('ix_tasks_task_tier', table_name='tasks')
    op.drop_index('ix_tasks_parent_task_id', table_name='tasks')
    
    # Drop columns
    op.drop_column('tasks', 'parent_task_id')
    op.drop_column('tasks', 'task_tier')
