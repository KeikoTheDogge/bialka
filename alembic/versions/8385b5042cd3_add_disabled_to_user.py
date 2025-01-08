"""Add disabled to User

Revision ID: 8385b5042cd3
Revises: bd274e2d9d43
Create Date: 2025-01-08 22:21:48.110281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8385b5042cd3'
down_revision: Union[str, None] = 'bd274e2d9d43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('disabled', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'disabled')
    # ### end Alembic commands ###
