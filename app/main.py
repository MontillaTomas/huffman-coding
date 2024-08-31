"""
Main module for the FastAPI application.
"""
from fastapi import FastAPI
from app.api.v1.v1_router import v1_router

app = FastAPI()

app.include_router(v1_router)
