"""API User Table Migration

Revision ID: 1909a593a5dd
Revises: c0daee9ed380
Create Date: 2022-07-29 14:02:18.779540

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '1909a593a5dd'
down_revision = 'c0daee9ed380'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_user',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('username', sa.String(), nullable=False, max_length=20),
    sa.Column('password', sa.String(), nullable=False, max_length=50),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'covid_cases_over_time_usa', ['id'])
    op.create_unique_constraint(None, 'covid_data_sets', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'covid_data_sets', type_='unique')
    op.drop_constraint(None, 'covid_cases_over_time_usa', type_='unique')
    op.drop_table('api_user')
    # ### end Alembic commands ###
