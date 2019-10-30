"""empty message

Revision ID: dc4a1c9faa01
Revises: 
Create Date: 2019-10-30 11:26:03.648412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc4a1c9faa01'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('genrebook_junctiontable', 'junction_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('genrebook_junctiontable', sa.Column('junction_id', sa.INTEGER(), autoincrement=True, nullable=False))
    # ### end Alembic commands ###