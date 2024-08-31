"""
Router for version 1 of the API.
"""
from fastapi import APIRouter
from .routes.encode_router import encode_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(encode_router)
