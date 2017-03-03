"""empty message

Revision ID: fa5b4f15a88c
Revises: 198cbcf1ecd2
Create Date: 2017-02-28 15:18:53.212187

"""

# revision identifiers, used by Alembic.
revision = 'fa5b4f15a88c'
down_revision = '198cbcf1ecd2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('role', 'is_active')
    # ### end Alembic commands ###