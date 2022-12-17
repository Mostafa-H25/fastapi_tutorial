"""add content column to post table

Revision ID: 35c8d8f36195
Revises: c6929d389871
Create Date: 2022-12-17 15:02:32.368299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35c8d8f36195'
down_revision = 'c6929d389871'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
