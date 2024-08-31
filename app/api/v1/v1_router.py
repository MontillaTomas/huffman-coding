"""
Router for version 1 of the API.
"""
from fastapi import APIRouter
from .routes.encoder_router import encoder_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(encoder_router)
