"""create user table

Revision ID: 938358671fd8
Revises: 0bb70cd98686
Create Date: 2023-08-26 23:40:09.898688

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '938358671fd8'
down_revision: Union[str, None] = '0bb70cd98686'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
