__all__ = ['get_collection']

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient, AgnosticDatabase, AgnosticCollection
from Alone import DB_URL

print("Connecting to Database ...")

_MGCLIENT: AgnosticClient = AsyncIOMotorClient(DB_URL)

_DATABASE: AgnosticDatabase = _MGCLIENT["ALONE"]


def get_collection(name: str) -> AgnosticCollection:
    """ Create or Get Collection from your database """
    return _DATABASE[name]


def _close_db() -> None:
    _MGCLIENT.close()
