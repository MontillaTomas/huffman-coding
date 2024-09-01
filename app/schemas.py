"""
This module contains the Pydantic schemas for the API.
"""
from pydantic import BaseModel


class UnencodedSymbols(BaseModel):
    """
    Represents a list of unencoded symbols.

    Attributes:
        unencoded (list[str]): The list of unencoded symbols
    """
    unencoded: list[str]


class EncodedSymbols(BaseModel):
    """
    Represents a list of encoded symbols.

    Attributes:
        encoded (list[str]): The list of encoded symbols
    """
    encoded: list[str]


class EncodingMap(BaseModel):
    """
    Represents an encoding map.

    Attributes:
        map (dict[str, str]): The encoding map
    """
    map: dict[str, str]


class EncodeRequest(BaseModel):
    """
    Represents the request to encode a text.

    Attributes:
        algorithm (str): The encoding algorithm to use. Default is "huffman"
        separate_syllables (bool): Whether to separate syllables. Default is False
        text (str): The text to encode
    """
    algorithm: str | None = "huffman"
    separate_syllables: bool | None = False
    text: str


class EncodeResponse(BaseModel):
    """
    Represents the response of an encoding request.

    Attributes:
        encoding_map (dict[str, str]): The encoding map
        encoded_text (str): The encoded text
    """
    encoding_map: dict[str, str]
    encoded_text: str


class DecodeRequest(BaseModel):
    """
    Represents the request to decode a text.

    Attributes:
        algorithm (str): The decoding algorithm to use. Default is "huffman"
        encoded_text (str): The encoded text
        encoding_map (dict[str, str]): The encoding map
    """
    algorithm: str | None = "huffman"
    encoded_text: str
    encoding_map: dict[str, str]


class DecodeResponse(BaseModel):
    """
    Represents the response of a decoding request.

    Attributes:
        decoded_text (str): The decoded text
    """
    decoded_text: str
