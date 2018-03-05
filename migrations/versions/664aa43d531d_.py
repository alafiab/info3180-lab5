"""empty message

Revision ID: 664aa43d531d
Revises: 7fbe40597fea
Create Date: 2018-03-05 04:28:19.873354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '664aa43d531d'
down_revision = '7fbe40597fea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###