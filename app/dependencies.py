"""
This module contains the dependencies for the FastAPI application.
"""
from app.core.encoder import Encoder
from app.core.decoder import Decoder
from app.core.constants import Constants
from app.services.encoder_service import EncoderService
from app.services.decoder_service import DecoderService
from app.schemas import EncodeRequest, DecodeRequest
from .exceptions import InvalidAlgorithm

ENCODERS = Constants.get_encoders()
DECODERS = Constants.get_decoders()


async def get_encoder_service(request: EncodeRequest) -> Encoder:
    """
    Return the encoder service based on the request.

    Args:
        request (EncodeRequest): The request containing the algorithm.

    Returns:
        Encoder: The encoder service.

    Raises:
        ValueError: If the encoding algorithm is unknown.
    """
    algorithm = request.algorithm

    if algorithm not in ENCODERS:
        raise InvalidAlgorithm()

    return EncoderService(ENCODERS[algorithm])


async def get_huffman_enc_service() -> Encoder:
    """
    Return the encoder service for the Huffman algorithm.

    Returns:
        Encoder: The encoder service for the Huffman algorithm.
    """
    return EncoderService(ENCODERS["huffman"])


async def get_decoder_service(request: DecodeRequest) -> Decoder:
    """
    Return the decoder service based on the request.

    Args:
        request (DecodeRequest): The request containing the algorithm.

    Returns:
        Decoder: The decoder service.

    Raises:
        ValueError: If the decoding algorithm is unknown.
    """
    algorithm = request.algorithm

    if algorithm not in DECODERS:
        raise InvalidAlgorithm()

    return DecoderService(DECODERS[algorithm])
