"""
Main module for the FastAPI application.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.v1.v1_router import v1_router
from app.api.views.views_router import views_router
from app.exceptions import register_exception_handlers

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router)
app.include_router(views_router)

register_exception_handlers(app)


@app.head("/", include_in_schema=False)
async def read_root():
    """
    Returns the headers for the root endpoint.
    """
    return None
