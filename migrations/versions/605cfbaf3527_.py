"""empty message

Revision ID: 605cfbaf3527
Revises: e594528b9e27
Create Date: 2020-08-26 21:35:01.050495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '605cfbaf3527'
down_revision = 'e594528b9e27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('discuss', sa.Column('pname', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('discuss', 'pname')
    # ### end Alembic commands ###
