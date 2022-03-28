from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"postgresql://{config('DB_USERNAME')}:{config('DB_PASSWORD')}@" \
                          f"{config('DB_HOST')}:{config('DB_PORT')}/{config('DB_DATABASE')}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
