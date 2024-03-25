from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.keyword import schemas, service.KeywordService as keyword_service

keyword_router = APIRouter()
keyword_router.tags = ["Keyword API"]


@keyword_router.post("/keywords/", response_model=schemas.Keyword, summary="키워드 생성")
async def create_user(keyword_request: schemas.KeywordCreate):
    return keyword_service.create_keyword(keyword=keyword_request)


@keyword_router.get("/keywords/", response_model=list[schemas.Keyword], summary="키워드 목록 조회")
async def read_users(db: Session = Depends(get_db)):
    keywords = service.get_all(db)
    return keywords


@keyword_router.get("/keywords/{keyword_id}", response_model=schemas.Keyword, summary="키워드 상세 조회")
async def read_user(keyword_id: str, db: Session = Depends(get_db)):
    db_keyword = service.get_keyword(db, keyword_id=keyword_id)
    if db_keyword is None:
        raise HTTPException(status_code=404, detail="Keyword not found")
    return db_keyword
