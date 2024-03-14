import uuid

from sqlalchemy import Column, String

from app.core.UUIDType import UUIDType
from app.database import Base


def generate_uuid():
    return str(uuid.uuid4())


class Keyword(Base):
    __tablename__ = "an_keyword"

    id = Column(UUIDType, primary_key=True, index=True, default=generate_uuid)
    createdDateTime = Column(String(30))
    lastModifiedDateTime = Column(String(30), nullable=True)
    keywordName = Column(String(100))
    keywordStatus = Column(String(30))
