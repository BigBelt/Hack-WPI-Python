"""empty message

Revision ID: 311c62fe5f49
Revises: 3f427be4ce8a
Create Date: 2022-12-06 11:08:18.571528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '311c62fe5f49'
down_revision = '3f427be4ce8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('school', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('school')

    # ### end Alembic commands ###