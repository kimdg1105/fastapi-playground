from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import engine, SessionLocal
from app.keyword import models, schemas, service

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/keywords/", response_model=schemas.Keyword)
def create_user(keyword_request: schemas.KeywordCreate, db: Session = Depends(get_db)):
    return service.create_keyword(db=db, keyword=keyword_request)


@app.get("/keywords/", response_model=list[schemas.Keyword])
def read_users(db: Session = Depends(get_db)):
    keywords = service.get_all(db)
    return keywords


@app.get("/keywords/{keyword_id}", response_model=schemas.Keyword)
def read_user(keyword_id: str, db: Session = Depends(get_db)):
    db_keyword = service.get_keyword(db, keyword_id=keyword_id)
    if db_keyword is None:
        raise HTTPException(status_code=404, detail="Keyword not found")
    return db_keyword
