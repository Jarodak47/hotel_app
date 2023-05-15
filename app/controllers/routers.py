from fastapi import APIRouter

from . import items, login, users, utils,chambre, stock

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(chambre.router, prefix="/chambre", tags=["chambre"])
api_router.include_router(stock.router, prefix="/stock", tags=["stock"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
