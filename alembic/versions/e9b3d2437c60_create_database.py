"""Create database

Revision ID: e9b3d2437c60
Revises: 
Create Date: 2024-11-27 23:20:02.275725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9b3d2437c60'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('protein',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('gene_symbol', sa.String(length=10), nullable=True),
    sa.Column('sequence', sa.Text(), nullable=True),
    sa.Column('amino_acid', sa.Integer(), nullable=True),
    sa.Column('organism', sa.String(length=50), nullable=True),
    sa.Column('function', sa.Text(), nullable=True),
    sa.Column('localization', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('protein')
    # ### end Alembic commands ###
