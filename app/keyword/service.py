from datetime import datetime
from typing import Type

from sqlalchemy.orm import Session

from . import models, schemas
from .models import Keyword


def get_keyword(db: Session, keyword_id: str) -> Type[Keyword]:
    return (db.query(models.Keyword)
            .where(models.Keyword.id == keyword_id)
            .first())


def get_keyword_by_keyword_name(db: Session, keyword_name: str) -> Type[Keyword]:
    return (db.query(models.Keyword)
            .where(models.Keyword.keywordName == keyword_name)
            .first())


def get_all(db: Session) -> list[Type[Keyword]]:
    return db.query(models.Keyword).all()


def create_keyword(db: Session, keyword: schemas.KeywordCreate) -> Keyword:
    db_keyword = models.Keyword(**keyword.model_dump())
    db_keyword.createdDateTime = datetime.now()

    db.add(db_keyword)
    db.commit()
    db.refresh(db_keyword)
    return db_keyword
