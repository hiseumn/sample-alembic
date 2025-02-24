# models.py
from sqlalchemy import Column, Text, create_engine
from sqlalchemy.dialects.postgresql import UUID as UUIDType
from sqlalchemy.ext.declarative import declarative_base
from uuid6 import uuid7

Engine = create_engine(
    url="postgresql+psycopg://postgres:postgres@localhost:5432/almebic",
    echo=False,
)

Base = declarative_base()


class Memo(Base):
    __tablename__ = "memo"
    id = Column(UUIDType(as_uuid=False), primary_key=True, default=uuid7)
    memo = Column(Text)

    def __repr__(self):
        return f"{self.id} {self.memo}"
