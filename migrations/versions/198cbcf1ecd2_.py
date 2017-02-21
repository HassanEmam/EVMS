"""empty message

Revision ID: 198cbcf1ecd2
Revises: 325b8725d85a
Create Date: 2017-02-21 09:14:12.651396

"""

# revision identifiers, used by Alembic.
revision = '198cbcf1ecd2'
down_revision = '325b8725d85a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spread_types')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spread_types',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('code', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('period1', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period2', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period3', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period4', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period5', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period6', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period7', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period8', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period9', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period10', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period11', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period12', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period13', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period14', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period15', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period16', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period17', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period18', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period19', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('period20', mysql.VARCHAR(length=3), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###