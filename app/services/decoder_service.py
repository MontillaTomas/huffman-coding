"""
This module contains the DecoderService class.
"""
from app.core.decoder import Decoder
from app.schemas import DecodeResponse, EncodedSymbols, EncodingMap


class DecoderService:
    """
    A class that represents the decoder service.

    Attributes:
        decoder (Decoder): The decoder to be used.
    """

    def __init__(self, decoder: Decoder):
        self.decoder = decoder

    async def decode(self, encoded_text: str, encoding_map: dict[str, str]) -> DecodeResponse:
        """
        Decode the given text.

        Args:
            encoded_text (str): The text to decode.
            encoding_map (dict): The encoding map to use.

        Returns:
            DecodeResponse: The decoded text.
        """
        enc_symbols = encoded_text.split()
        enc_symbols = EncodedSymbols(encoded=enc_symbols)
        enc_map = EncodingMap(map=encoding_map)

        dec_symbols = self.decoder.decode(enc_map, enc_symbols)
        dec_text = "".join(dec_symbols.unencoded)

        return DecodeResponse(decoded_text=dec_text)
