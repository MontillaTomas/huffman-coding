"""
This module defines the constants used in the application.
"""
from enum import Enum
from app.core.encoder import HuffmanEncoder
from app.core.decoder import HuffmanDecoder


class Constants(Enum):
    """
    A class that defines the constants used in the application.
    """
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÁÉÍÓÚáéíóúÑñÜü"
    ENCODERS = {
        'huffman': HuffmanEncoder()
    }
    DECODERS = {
        'huffman': HuffmanDecoder()
    }
