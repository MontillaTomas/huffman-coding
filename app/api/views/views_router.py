"""
Module for the views router.
"""
from typing import Optional, Annotated
from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.dependencies import get_huffman_enc_service
from app.services.encoder_service import EncoderService

views_router = APIRouter(prefix="", tags=["Views"])

templates = Jinja2Templates(directory="app/templates")


@views_router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Returns the index page.
    """
    return templates.TemplateResponse(name="index.html", request=request)


@views_router.post("/huffman-coding", response_class=HTMLResponse)
async def huffman_coding(request: Request,
                         service: Annotated[EncoderService, Depends(get_huffman_enc_service)],
                         text: Optional[str] = Form(None),
                         separate_syllables: bool = Form(False, alias="separate-syllables")):
    """
    Returns the result of the Huffman coding algorithm.
    """
    if not text:
        text = ""

    enc_response = await service.encode(text, separate_syllables)

    return templates.TemplateResponse(
        request=request,
        name="huffman_coding_result.html",
        context={"encoded_text": enc_response.encoded_text,
                 "encoding_map": enc_response.encoding_map})
