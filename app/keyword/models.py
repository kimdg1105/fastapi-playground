from datetime import datetime
from enum import Enum

from sqlalchemy import Column, String, Enum as SqlEnum, DateTime
from sqlalchemy.orm import relationship

from app.core.UUIDType import UUIDType, generate_uuid
from app.database import Base


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

    news = relationship("News", back_populates="keyword")
