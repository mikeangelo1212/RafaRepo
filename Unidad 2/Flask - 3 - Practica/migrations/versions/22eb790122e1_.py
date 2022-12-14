"""empty message

Revision ID: 22eb790122e1
Revises: 
Create Date: 2022-10-27 20:39:02.504745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22eb790122e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('perro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('raza', sa.String(length=250), nullable=True),
    sa.Column('edad', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('persona',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido', sa.String(length=250), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('direccion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=True),
    sa.Column('calle', sa.String(length=250), nullable=True),
    sa.Column('idpersona', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['idpersona'], ['persona.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('direccion')
    op.drop_table('persona')
    op.drop_table('perro')
    # ### end Alembic commands ###
