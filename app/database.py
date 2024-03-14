from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://admin:password@localhost:3306/botpltmdevdb'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    , echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()