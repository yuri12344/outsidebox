"""ok

Revision ID: a428919c1752
Revises: 
Create Date: 2021-04-22 09:40:10.214571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a428919c1752'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=25), nullable=False),
    sa.Column('email', sa.String(length=25), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('address', sa.String(length=25), nullable=False),
    sa.Column('city', sa.String(length=15), nullable=False),
    sa.Column('state', sa.String(length=15), nullable=False),
    sa.Column('cpf_cnpj', sa.String(length=25), nullable=False),
    sa.Column('schedule', sa.String(length=25), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('feedbacks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feedback', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=100), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('state', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('service_catalog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_of_service', sa.String(length=55), nullable=False),
    sa.Column('price', sa.String(length=20), nullable=True),
    sa.Column('service_description', sa.String(length=25), nullable=False),
    sa.Column('id_company', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_company'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('services_specific',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_of_service', sa.String(length=55), nullable=False),
    sa.Column('price', sa.String(length=20), nullable=True),
    sa.Column('service_description', sa.String(length=25), nullable=False),
    sa.Column('client_name', sa.String(length=25), nullable=False),
    sa.Column('id_client', sa.Integer(), nullable=True),
    sa.Column('date_time', sa.String(length=25), nullable=False),
    sa.Column('informations', sa.String(length=255), nullable=False),
    sa.Column('feedback_url', sa.String(length=25), nullable=True),
    sa.Column('aproved', sa.String(length=25), nullable=False),
    sa.Column('responsible', sa.String(length=25), nullable=False),
    sa.Column('id_company', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_company'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('services_specific')
    op.drop_table('service_catalog')
    op.drop_table('user_client')
    op.drop_table('feedbacks')
    op.drop_table('company')
    # ### end Alembic commands ###
