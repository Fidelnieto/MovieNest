"""empty message

Revision ID: 958deed18b0b
Revises: 
Create Date: 2024-11-20 15:14:29.022492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '958deed18b0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=256),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)

    # ### end Alembic commands ###
