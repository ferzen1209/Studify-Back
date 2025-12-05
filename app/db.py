import os
from dotenv import load_dotenv
import sqlalchemy.ext.asyncio as _asyncio
import sqlalchemy.orm as _orm

load_dotenv()

DATABASE_URL = (
    f"postgresql+asyncpg://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}"
    f"@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
)

engine = _asyncio.create_async_engine(DATABASE_URL, echo=True)
SessionLocal = _orm.sessionmaker(
    bind=engine,
    class_=_asyncio.AsyncSession,
    expire_on_commit=False)


Base = _orm.declarative_base()