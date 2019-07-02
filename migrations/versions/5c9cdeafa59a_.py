"""empty message

Revision ID: 5c9cdeafa59a
Revises: 
Create Date: 2019-06-30 17:20:08.058623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c9cdeafa59a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classification',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('alias', sa.String(length=100), nullable=True),
    sa.Column('keyword', sa.String(length=100), nullable=True),
    sa.Column('parentnode', sa.String(length=100), nullable=True),
    sa.Column('describe', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('passwd', sa.String(length=20), nullable=True),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('username')
    )
    op.create_table('content',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('comment', sa.Integer(), nullable=True),
    sa.Column('keyword', sa.String(length=50), nullable=True),
    sa.Column('describe', sa.Text(), nullable=True),
    sa.Column('label', sa.String(length=50), nullable=True),
    sa.Column('img', sa.String(length=200), nullable=True),
    sa.Column('data', sa.DateTime(), nullable=True),
    sa.Column('classification', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classification'], ['classification.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('content')
    op.drop_table('user')
    op.drop_table('classification')
    # ### end Alembic commands ###