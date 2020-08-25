"""empty message

Revision ID: e6b632dc25c1
Revises: 
Create Date: 2020-08-24 17:30:58.855232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6b632dc25c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.Enum('男', '女', '保密'), nullable=True),
    sa.Column('city', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###