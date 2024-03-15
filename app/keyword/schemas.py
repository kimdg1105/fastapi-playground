import datetime

from pydantic import BaseModel


class KeywordBase(BaseModel):
    keywordName: str


class KeywordCreate(KeywordBase):
    pass


class KeywordStatusUpdate(KeywordBase):
    id: str
    keywordStatus: str


class Keyword(KeywordBase):
    id: str
    keywordName: str
    createdDateTime: datetime.datetime
    lastModifiedDateTime: datetime.datetime | None

    class Config:
        from_attributes = True
