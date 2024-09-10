"""
Module for the views router.
"""
from typing import Optional
import httpx
from fastapi import APIRouter, Request, Form, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

views_router = APIRouter(prefix="", tags=["Views"])

templates = Jinja2Templates(directory="app/templates")


@views_router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Returns the index page.
    """
    return templates.TemplateResponse(name="index.html", request=request)


@views_router.post("/huffman-coding", response_class=HTMLResponse)
async def huffman_coding(request: Request, text: Optional[str] = Form(None)):
    """
    Returns the result of the Huffman coding algorithm.
    """
    if not text:
        text = ""

    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:80/v1/encoder/", json={"text": text})

    if response.status_code != status.HTTP_200_OK:
        encoded_text = "An error occurred"
        encoding_map = {}
    else:
        encoded_text = response.json()["encoded_text"]
        encoding_map = response.json()["encoding_map"]

    return templates.TemplateResponse(
        request=request,
        name="huffman_coding_result.html",
        context={"encoded_text": encoded_text, "encoding_map": encoding_map})
