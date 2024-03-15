import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import Column, String, Enum as SqlEnum, DateTime

from app.core.UUIDType import UUIDType
from app.database import Base


def generate_uuid():
    return str(uuid.uuid4())


class KeywordStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class Keyword(Base):
    __tablename__ = "an_keyword"

    id = Column(UUIDType, primary_key=True, index=True, default=generate_uuid)
    createdDateTime = Column(DateTime, nullable=False, default=datetime.now())
    lastModifiedDateTime = Column(DateTime, nullable=True)
    keywordName = Column(String(255))
    keywordStatus = Column(SqlEnum(KeywordStatus), default=KeywordStatus.ACTIVE, nullable=False)
