from abc import ABC, abstractmethod
from app.schemas import UnencodedSymbols, EncodedSymbols, EncodingMap


class Encoder(ABC):
    @abstractmethod
    def encode(self, list_of_symbols: UnencodedSymbols) -> tuple[EncodingMap, EncodedSymbols]:
        pass


class HuffmanEncoder(Encoder):
    def encode(self, list_of_symbols: UnencodedSymbols) -> tuple[EncodingMap, EncodedSymbols]:
        pass
