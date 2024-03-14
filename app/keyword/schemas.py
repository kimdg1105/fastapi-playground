from pydantic import BaseModel


class KeywordBase(BaseModel):
    keywordName: str
    keywordStatus: str


class KeywordCreate(KeywordBase):
    pass


class Keyword(KeywordBase):
    id: str
    keywordName: str
    createdDateTime: str
    lastModifiedDateTime: str

    class Config:
        from_attributes = True
