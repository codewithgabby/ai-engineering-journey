"""make product sku unique

Revision ID: bde702294e1b
Revises: ef62d1b9234a
Create Date: 2026-09-14 12:12:11.307685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bde702294e1b'
down_revision: Union[str, Sequence[str], None] = 'ef62d1b9234a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint(
        "uq_products_sku",
        "products",
        ["sku"],
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "uq_products_sku",
        "products",
        type_="unique",
    )