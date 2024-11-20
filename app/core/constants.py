"""
This module defines the constants used in the application.
"""
from enum import Enum


class Constants(Enum):
    """
    A class that defines the constants used in the application.
    """
    @staticmethod
    def get_encoders():
        from app.core.encoder import HuffmanEncoder
        return {'huffman': HuffmanEncoder()}

    @staticmethod
    def get_decoders():
        from app.core.decoder import HuffmanDecoder
        return {'huffman': HuffmanDecoder()}

    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÁÉÍÓÚáéíóúÑñÜü"
    LETTERS_FREQ_IN_SPANISH = {
        'A': 1253,
        'B': 142,
        'C': 468,
        'D': 586,
        'E': 1368,
        'F': 69,
        'G': 101,
        'H': 70,
        'I': 625,
        'J': 44,
        'K': 2,
        'L': 497,
        'M': 315,
        'N': 617,
        'Ñ': 31,
        'O': 868,
        'P': 251,
        'Q': 88,
        'R': 687,
        'S': 798,
        'T': 463,
        'U': 393,
        'V': 90,
        'W': 1,
        'X': 22,
        'Y': 90,
        'Z': 52
    }
