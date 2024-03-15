import uvicorn
from fastapi import FastAPI

from app.database import engine
from app.keyword import models, router as keyword_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()  # Dependency
app.include_router(keyword_router.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
