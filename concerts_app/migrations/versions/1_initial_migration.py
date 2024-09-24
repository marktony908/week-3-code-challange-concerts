from alembic import op
import sqlalchemy as sa

revision = '1_initial_migration'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('bands',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('hometown', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venues',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('city', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('concerts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('band_id', sa.Integer(), nullable=True),
        sa.Column('venue_id', sa.Integer(), nullable=True),
        sa.Column('date', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(['band_id'], ['bands.id']),
        sa.ForeignKeyConstraint(['venue_id'], ['venues.id']),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('concerts')
    op.drop_table('bands')
    op.drop_table('venues')
