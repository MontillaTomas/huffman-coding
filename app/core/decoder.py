"""
This module provides an abstract base class `Decoder` and a concrete implementation `HuffmanDecoder`
for decoding symbols using Huffman coding.
"""
from abc import ABC, abstractmethod
from app.schemas import UnencodedSymbols, EncodedSymbols, EncodingMap


class Decoder(ABC):
    """
    An abstract base class that defines the interface for decoders.
    """
    @abstractmethod
    def decode(self, encoding_map: EncodingMap, encoded_symbols: EncodedSymbols) -> UnencodedSymbols:
        """
        Decodes a list of symbols using the given encoding map and returns the decoded symbols.

        Args:
            encoding_map (EncodingMap): The encoding map.
            encoded_symbols (EncodedSymbols): The encoded symbols.

        Returns:
            UnencodedSymbols: The decoded symbols.
        """
        pass


class HuffmanDecoder(Decoder):
    """
    A decoder that uses the Huffman coding algorithm to decode a list of symbols.
    """

    def decode(self, encoding_map: EncodingMap, encoded_symbols: EncodedSymbols) -> UnencodedSymbols:
        """
        Decodes a list of symbols using the given encoding map and returns the decoded symbols.

        Args:
            encoding_map (EncodingMap): The encoding map.
            encoded_symbols (EncodedSymbols): The encoded symbols.

        Returns:
            UnencodedSymbols: The decoded symbols.
        """
        decoding_map = {v: k for k, v in encoding_map.map.items()}

        decoded_symbols = [decoding_map[symbol]
                           for symbol in encoded_symbols.encoded]

        return UnencodedSymbols(unencoded=decoded_symbols)
