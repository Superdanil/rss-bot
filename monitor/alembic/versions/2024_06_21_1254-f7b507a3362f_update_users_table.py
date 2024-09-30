"""update users table

Revision ID: f7b507a3362f
Revises: eaa2c428c78f
Create Date: 2024-06-21 12:54:18.009632

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "f7b507a3362f"
down_revision: Union[str, None] = "eaa2c428c78f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("foo", sa.Integer(), nullable=False))
    op.add_column("users", sa.Column("bar", sa.Integer(), nullable=False))
    op.create_unique_constraint(
        op.f("uq_users_foo_bar"), "users", ["foo", "bar"]
    )


def downgrade() -> None:
    op.drop_constraint(op.f("uq_users_foo_bar"), "users", type_="unique")
    op.drop_column("users", "bar")
    op.drop_column("users", "foo")
