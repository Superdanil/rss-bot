"""Created tables

Revision ID: bccb9b61fffb
Revises: 
Create Date: 2024-10-06 17:30:28.099549

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'bccb9b61fffb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('sources',
                    sa.Column('url', sa.String(), nullable=False),
                    sa.Column('id', sa.Uuid(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('url')
                    )
    op.create_table('users',
                    sa.Column('telegram_id', sa.Integer(), nullable=False),
                    sa.Column('id', sa.Uuid(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('telegram_id')
                    )
    op.create_table('news',
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('link', sa.String(), nullable=False),
                    sa.Column('published_at', sa.TIMESTAMP(timezone=True), nullable=False),
                    sa.Column('source_id', sa.Uuid(), nullable=False),
                    sa.Column('id', sa.Uuid(), nullable=False),
                    sa.ForeignKeyConstraint(['source_id'], ['sources.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('link')
                    )
    op.create_table('user_source_association',
                    sa.Column('user_id', sa.Uuid(), nullable=False),
                    sa.Column('source_id', sa.Uuid(), nullable=False),
                    sa.Column('id', sa.Uuid(), nullable=False),
                    sa.ForeignKeyConstraint(['source_id'], ['sources.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('user_id', 'source_id', name='idx_unique_user_source')
                    )


def downgrade() -> None:
    op.drop_table('user_source_association')
    op.drop_table('news')
    op.drop_table('users')
    op.drop_table('sources')
