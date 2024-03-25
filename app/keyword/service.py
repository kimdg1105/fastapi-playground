from datetime import datetime

from core.db.transactional import Transactional
from . import models
from .models import Keyword
from .persistence import KeywordSQLAlchemyRepository
from .schemas import KeywordCreate


class KeywordService:
    def __init__(self, *, repository: KeywordSQLAlchemyRepository):
        self.repository = repository

    async def get_keyword(self, *, keyword_id: str) -> Keyword:
        return await self.repository.get_keyword_by_id(keyword_id=keyword_id)

    async def get_keyword_by_keyword_name(self, *, keyword_name: str) -> Keyword:
        return await self.repository.get_keyword_by_keyword_name(keyword_name=keyword_name)

    async def get_all_keywords(self) -> list[Keyword]:
        return await self.repository.get_all()

    @Transactional()
    async def create_keyword(self, *, keywordCreate: KeywordCreate) -> None:
        db_keyword = models.Keyword(**keywordCreate.model_dump())
        db_keyword.createdDateTime = datetime.now()
        await self.repository.save(keyword=db_keyword)
