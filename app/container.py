from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton

from app.keyword.persistence import KeywordSQLAlchemyRepository
from app.keyword.service import KeywordService


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(packages=["app"])

    user_repo = Singleton(KeywordSQLAlchemyRepository)
    user_service = Factory(KeywordService)
