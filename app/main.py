"""
Main module for the FastAPI application.
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1.v1_router import v1_router
from app.api.views.views_router import views_router
from app.exceptions import register_exception_handlers

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(v1_router)
app.include_router(views_router)

register_exception_handlers(app)
