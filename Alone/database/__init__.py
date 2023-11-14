#MIT License
#Copyright (c) 2023, ©AloneXBots

from async_pymongo import AsyncClient

from Alone import DB_URL

DBNAME = "ALONE "

mongo = AsyncClient(DB_URL)
dbname = mongo[DBNAME]
