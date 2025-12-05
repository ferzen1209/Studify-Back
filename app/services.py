from sqlalchemy import select

from Modelos import StockRequest, ReservedStock
import os
import db as db
from db import Base
from helpers.stock_ws import broadcast_stock_update
from schemas import Stock

def añadir_tablas():
    async def create_tables():
        async with db.engine.begin() as conector:

            await conector.run_sync(db.Base.metadata.create_all)

    return create_tables()
    # return _database.Base.metadata.create_all(bind=_database.engine)


async def get_db():
    async with db.SessionLocal() as db:
        yield db