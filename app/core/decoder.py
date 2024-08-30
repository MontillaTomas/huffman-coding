from abc import ABC, abstractmethod
from app.schemas import UnencodedSymbols, EncodedSymbols, EncodingMap


class Decoder(ABC):
    @abstractmethod
    def decode(self, encoding_map: EncodingMap, encoded_symbols: EncodedSymbols) -> UnencodedSymbols:
        pass


class HuffmanDecoder(Decoder):
    def decode(self, encoding_map: EncodingMap, encoded_symbols: EncodedSymbols) -> UnencodedSymbols:
        pass
