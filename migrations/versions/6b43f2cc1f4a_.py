"""empty message

Revision ID: 6b43f2cc1f4a
Revises: 081901dc4754
Create Date: 2020-08-26 16:13:22.294397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b43f2cc1f4a'
down_revision = '081901dc4754'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pro', sa.Column('date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pro', 'date')
    # ### end Alembic commands ###