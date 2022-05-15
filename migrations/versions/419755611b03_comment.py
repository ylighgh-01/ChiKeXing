"""comment

Revision ID: 419755611b03
Revises: 08b3553e3c1d
Create Date: 2022-05-15 09:32:01.328406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '419755611b03'
down_revision = '08b3553e3c1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('icon', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'icon')
    # ### end Alembic commands ###