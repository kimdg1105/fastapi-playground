from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.keyword import schemas, service

router = APIRouter()

router.tags = ["Keyword API"]


@router.post("/keywords/", response_model=schemas.Keyword, summary="키워드 생성")
def create_user(keyword_request: schemas.KeywordCreate, db: Session = Depends(get_db)):
    return service.create_keyword(db=db, keyword=keyword_request)


@router.get("/keywords/", response_model=list[schemas.Keyword], summary="키워드 목록 조회")
def read_users(db: Session = Depends(get_db)):
    keywords = service.get_all(db)
    return keywords


@router.get("/keywords/{keyword_id}", response_model=schemas.Keyword, summary="키워드 상세 조회")
def read_user(keyword_id: str, db: Session = Depends(get_db)):
    db_keyword = service.get_keyword(db, keyword_id=keyword_id)
    if db_keyword is None:
        raise HTTPException(status_code=404, detail="Keyword not found")
    return db_keyword
