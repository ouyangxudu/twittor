"""add followers

Revision ID: 5036695ebc4d
Revises: b6db989a46cc
Create Date: 2018-12-14 21:05:04.848496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5036695ebc4d'
down_revision = 'b6db989a46cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
