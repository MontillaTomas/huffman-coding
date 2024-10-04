"""
This module contains the EncoderService class.
"""
from syltippy import syllabize
from app.core.constants import Constants
from app.core.encoder import Encoder
from app.schemas import EncodeResponse, UnencodedSymbols


class EncoderService:
    """
    A class that represents the encoder service.

    Attributes:
        encoder (Encoder): The encoder to be used.
    """

    def __init__(self, encoder: Encoder):
        self.encoder = encoder

    def _separate_into_syllables_and_special_chars(self, text: str) -> list[str]:
        """
        Separate the text into syllables and special characters.

        Args:
            text (str): The text to be separated.

        Returns:
            list: A list containing the syllables and special characters.
        """
        unencoded_symbols = []
        index = 0

        while index < len(text):
            if text[index] not in Constants.LETTERS.value:
                unencoded_symbols.append(text[index])
                index += 1
            else:
                word = ""
                while index < len(text) and text[index] in Constants.LETTERS.value:
                    word += text[index]
                    index += 1
                syllabes, _ = syllabize(word)
                unencoded_symbols.extend(syllabes)

        return unencoded_symbols

    def _separate_into_chars(self, text: str):
        """
        Separate the text into characters.

        Args:
            text (str): The text to be separated.

        Returns:
            list: A list containing the characters.
        """
        return list(text)

    async def encode(self, text: str, separate_syllables: bool) -> EncodeResponse:
        """
        Encode the text.

        Args:
            text (str): The text to be encoded.
            separate_syllables (bool): Whether to separate syllables.

        Returns:
            EncodeResponse: The encoding map and the encoded symbols.
        """
        if separate_syllables:
            unenc_symbols = self._separate_into_syllables_and_special_chars(
                text)
        else:
            unenc_symbols = self._separate_into_chars(text)

        unenc_symbols = UnencodedSymbols(unencoded=unenc_symbols)
        enc_map, enc_symbols = self.encoder.encode(unenc_symbols)
        enc_text = " ".join(enc_symbols.encoded)

        return EncodeResponse(encoding_map=enc_map.map, encoded_text=enc_text)
