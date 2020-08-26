"""empty message

Revision ID: 452b89f3e9be
Revises: 6b43f2cc1f4a
Create Date: 2020-08-26 16:54:38.175566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '452b89f3e9be'
down_revision = '6b43f2cc1f4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('discuss',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uname', sa.String(length=10), nullable=True),
    sa.Column('words', sa.Text(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('discuss')
    # ### end Alembic commands ###
