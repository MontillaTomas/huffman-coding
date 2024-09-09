"""
This module contains tests for the decoder router.
"""
from fastapi.testclient import TestClient
from app.main import app
from tests.constants import Constants

client = TestClient(app)

DECODER_URL = "/v1/decoder/"


def test_invalid_algorithm():
    """
    Test the case when the algorithm is invalid.
    """
    res = client.post(DECODER_URL,
                      json={"algorithm": "invalid",
                            "encoding_map": Constants.ENC_MAP_1.value,
                            "encoded_text": Constants.ENC_TEXT_1.value})
    assert res.status_code == 400
    assert res.json() == {"detail": "Invalid algorithm"}


def test_missing_encoding_map():
    """
    Test the case when the encoding map is missing.
    """
    res = client.post(DECODER_URL,
                      json={"encoded_text": Constants.ENC_TEXT_1.value})
    assert res.status_code == 422


def test_missing_encoded_text():
    """
    Test the case when the encoded text is missing.
    """
    res = client.post(DECODER_URL,
                      json={"encoding_map": Constants.ENC_MAP_1.value})
    assert res.status_code == 422


def test_decode_enc_text_1():
    """
    Test the case when the encoded text is Constants.ENC_TEXT_1.
    """
    res = client.post(DECODER_URL,
                      json={"encoding_map": Constants.ENC_MAP_1.value,
                            "encoded_text": Constants.ENC_TEXT_1.value})
    assert res.status_code == 200
    assert res.json() == {"decoded_text": Constants.TEXT_1.value}


def test_decode_enc_text_2():
    """
    Test the case when the encoded text is Constants.ENC_TEXT_2.
    """
    res = client.post(DECODER_URL,
                      json={"encoding_map": Constants.ENC_MAP_2.value,
                            "encoded_text": Constants.ENC_TEXT_2.value})
    assert res.status_code == 200
    assert res.json() == {"decoded_text": Constants.TEXT_2.value}


def test_decode_enc_text_separate_syllables():
    """
    Test the case when the encoded text is Constants.ENC_TEXT_SEPARATE_SYLLABLES.
    """
    res = client.post(DECODER_URL,
                      json={"encoding_map": Constants.ENC_MAP_SEPARATE_SYLLABLES.value,
                            "encoded_text": Constants.ENC_TEXT_SEPARATE_SYLLABLES.value})
    assert res.status_code == 200
    assert res.json() == {
        "decoded_text": Constants.TEXT_SEPARATE_SYLLABLES.value}
