from app.core.decoder import Decoder


class DecoderService:
    def __init__(self, decoder: Decoder):
        self.decoder = decoder

    def decode(self):
        return ('Decoding')
