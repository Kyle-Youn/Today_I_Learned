import fastapi import APIRouter

api_router = APIRouter()

from api.v1.history import router as history_router
api_router.include_router(history_router, prefix="/v1/history", tags=["history"]
