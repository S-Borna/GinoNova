"""Add exam_results table

Revision ID: 008_add_exam_results
Revises: 007_add_last_login
Create Date: 2026-01-06

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '008_add_exam_results'
down_revision = '007_add_last_login'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'exam_results',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False),
        
        # Exam configuration
        sa.Column('duration_minutes', sa.Integer(), nullable=False),
        sa.Column('question_count', sa.Integer(), nullable=False),
        sa.Column('sources', sa.JSON(), default=[]),
        sa.Column('include_g', sa.Boolean(), default=True),
        sa.Column('include_vg', sa.Boolean(), default=True),
        sa.Column('grading_mode', sa.String(20), default='live'),
        
        # Results
        sa.Column('correct_answers', sa.Integer(), default=0),
        sa.Column('wrong_answers', sa.Integer(), default=0),
        sa.Column('skipped_answers', sa.Integer(), default=0),
        sa.Column('score_percent', sa.Float(), default=0.0),
        
        # G/VG breakdown
        sa.Column('g_correct', sa.Integer(), default=0),
        sa.Column('g_total', sa.Integer(), default=0),
        sa.Column('vg_correct', sa.Integer(), default=0),
        sa.Column('vg_total', sa.Integer(), default=0),
        
        # Time tracking
        sa.Column('time_spent_seconds', sa.Integer(), default=0),
        sa.Column('started_at', sa.DateTime(), nullable=True),
        sa.Column('completed_at', sa.DateTime(), server_default=sa.func.now()),
        
        # Status
        sa.Column('completed', sa.Boolean(), default=True),
    )
    
    # Create indexes
    op.create_index('ix_exam_results_user_id', 'exam_results', ['user_id'])
    op.create_index('ix_exam_results_completed_at', 'exam_results', ['completed_at'])
    op.create_index('ix_exam_results_score', 'exam_results', ['score_percent'])


def downgrade() -> None:
    op.drop_index('ix_exam_results_score', table_name='exam_results')
    op.drop_index('ix_exam_results_completed_at', table_name='exam_results')
    op.drop_index('ix_exam_results_user_id', table_name='exam_results')
    op.drop_table('exam_results')
