from uuid import uuid4

from sqlalchemy import Column, String

from app.database import Base


class Keyword(Base):
    __tablename__ = "an_keyword"

    id = Column(String(100), primary_key=True, index=True, default=str(uuid4()))
    createdDateTime = Column(String(30))
    lastModifiedDateTime = Column(String(30))
    keywordName = Column(String(100))
    keywordStatus = Column(String(30))
