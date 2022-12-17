"""add user table

Revision ID: 637a908b924c
Revises: 35c8d8f36195
Create Date: 2022-12-17 15:05:58.068931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '637a908b924c'
down_revision = '35c8d8f36195'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email') )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
