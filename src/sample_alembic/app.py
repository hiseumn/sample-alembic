from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'xxxx'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # 新しいテーブルの追加
    op.create_table(
        'memo',
        sa.Column('id', sa.UUID, primary_key=True),
        sa.Column('memo', sa.text, nullable=False)
    )
    