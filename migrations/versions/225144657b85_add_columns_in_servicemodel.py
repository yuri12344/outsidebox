"""add columns in ServiceModel

Revision ID: 225144657b85
Revises: 3145905de31a
Create Date: 2021-04-14 17:14:07.383266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '225144657b85'
down_revision = '3145905de31a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_price', sa.Integer(), nullable=False),
    sa.Column('service_description', sa.Text(), nullable=False),
    sa.Column('date_time', sa.String(length=25), nullable=False),
    sa.Column('link', sa.String(length=255), nullable=True),
    sa.Column('client_name', sa.String(length=55), nullable=False),
    sa.Column('client_email', sa.String(length=55), nullable=False),
    sa.Column('phone', sa.String(length=55), nullable=False),
    sa.Column('service_approval', sa.String(length=55), nullable=False),
    sa.Column('user_client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_client_id'], ['user_client.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('client_email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('services')
    # ### end Alembic commands ###
