"""
Main module for the FastAPI application.
"""
from fastapi import FastAPI
from app.api.v1.v1_router import v1_router
from app.exceptions import register_exception_handlers

app = FastAPI()

app.include_router(v1_router)

register_exception_handlers(app)
