from datetime import datetime
from enum import Enum

from sqlalchemy import Column, DateTime, Enum as SqlEnum, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.core.UUIDType import generate_uuid, UUIDType
from app.database import Base


class NewSourceType(Enum):
    NAVER = "NAVER"


class News(Base):
    __tablename__ = "an_news"

    id = Column(UUIDType, primary_key=True, index=True, default=generate_uuid)
    createdDateTime = Column(DateTime, nullable=False, default=datetime.now())
    lastModifiedDateTime = Column(DateTime, nullable=True)
    newsSourceType = Column(SqlEnum(NewSourceType), nullable=False)
    publishedDateTime = Column(DateTime, nullable=True)
    newsUrl = Column(String(255))
    photoUrl = Column(String(255))
    newsTitle = Column(String(255))
    newsContent = Column(Text())

    keyword_id = Column(UUIDType, ForeignKey('an_keyword.id'))
    keyword = relationship("Keyword", back_populates="news")
