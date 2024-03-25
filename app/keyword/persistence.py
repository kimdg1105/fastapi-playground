from sqlalchemy import select

from app.keyword.models import Keyword
from core.db.session import session


class KeywordSQLAlchemyRepository:
    async def get_keyword_by_id(self, *, keyword_id: str) -> Keyword | None:
        query = await session.execute(select(Keyword).where(Keyword.id == keyword_id))
        return query.scalars().first()

    async def get_keyword_by_keyword_name(self, *, keyword_name: str) -> Keyword | None:
        query = await session.execute(select(Keyword).where(Keyword.keywordName == keyword_name))
        return query.scalars().first()

    async def get_all(self) -> list[Keyword]:
        return await session.execute(select(Keyword)).scalars().all()

    async def save(self, *, keyword: Keyword) -> None:
        session.add(keyword)
