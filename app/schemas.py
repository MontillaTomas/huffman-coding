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
