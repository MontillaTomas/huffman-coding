"""
Module for the decode router.
"""
from fastapi import APIRouter, Depends, status
from app.dependencies import get_decoder_service
from app.schemas import DecodeResponse, DecodeRequest

decoder_router = APIRouter(prefix="/decoder", tags=["Decoder"])


@decoder_router.post("/",
                     summary="Decode text",
                     response_description="The decoded text",
                     response_model=DecodeResponse,
                     status_code=status.HTTP_200_OK)
async def test(request: DecodeRequest,
               service=Depends(get_decoder_service)):
    """
    Decode the given text.

    - **request**: The request to decode the text.
        - **encoded_text**: The text to decode.
        - **encoding_map**: The encoding map to use.

    Returns the decoded text.

    Raises an Exception if the encoding algorithm is unknown.
    """
    return await service.decode(request.encoded_text, request.encoding_map)
