"""create user table

Revision ID: fdfa27dfc27b
Revises: 938358671fd8
Create Date: 2023-08-26 23:48:40.863103

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fdfa27dfc27b'
down_revision: Union[str, None] = '938358671fd8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
