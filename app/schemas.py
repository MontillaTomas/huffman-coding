from pydantic import BaseModel


class UnencodedSymbols(BaseModel):
    unencoded: list[str]


class EncodedSymbols(BaseModel):
    encoded: list[str]


class EncodingMap(BaseModel):
    map: dict[str, str]
