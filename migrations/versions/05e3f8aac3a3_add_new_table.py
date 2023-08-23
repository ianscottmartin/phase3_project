"""add new table

Revision ID: 05e3f8aac3a3
Revises: 68a696549d02
Create Date: 2023-08-23 17:00:04.460685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05e3f8aac3a3'
down_revision: Union[str, None] = '68a696549d02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_list',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('book_title', sa.String(), nullable=True),
    sa.Column('publisher', sa.String(length=55), nullable=True),
    sa.PrimaryKeyConstraint('book_id'),
    sa.UniqueConstraint('book_title')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_list')
    # ### end Alembic commands ###
