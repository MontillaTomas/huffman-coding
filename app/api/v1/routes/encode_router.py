"""
Module for the encode router.
"""
from typing import Annotated
from fastapi import APIRouter, Depends, status
from app.dependencies import get_encoder_service
from app.services.encoder_service import EncoderService
from app.schemas import EncodeRequest, EncodeResponse

encode_router = APIRouter(prefix="/encode", tags=["Encode"])


@encode_router.post("/",
                    summary="Encode text",
                    response_description="The encoded text and the encoding map",
                    response_model=EncodeResponse,
                    status_code=status.HTTP_200_OK)
async def test(request: EncodeRequest,
               service: Annotated[EncoderService, Depends(get_encoder_service)]):
    """
    Encode the given text.

    - **request**: The request to encode the text.
        - **algorithm**: The encoding algorithm to use. Default is "huffman".
        - **separate_syllables**: Whether to separate the syllables in the encoded text. Default is 
                                  False.
        - **text**: The text to encode.

    Returns the encoded text and the encoding map.
    """

    return await service.encode(request.text, request.separate_syllables)
