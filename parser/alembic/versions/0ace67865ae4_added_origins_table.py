"""Added origins table

Revision ID: 0ace67865ae4
Revises: 2d9f27149827
Create Date: 2024-09-30 23:45:39.841518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '0ace67865ae4'
down_revision: Union[str, None] = '2d9f27149827'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('origins',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('user_origin_association',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('origin_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['origin_id'], ['origins.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('user_id', 'origin_id', name='idx_unique_user_origin')
                    )


def downgrade() -> None:
    op.drop_table('user_origin_association')
    op.drop_table('origins')
