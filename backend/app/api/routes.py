from fastapi import APIRouter
from app.api.controller.CryptoController import cryptorouter

api_router = APIRouter()
api_router.add_router(cryptorouter, prefix="", tags=["crypto-router"])

