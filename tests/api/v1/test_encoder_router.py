"""
This module contains tests for the encoder router.
"""
from fastapi.testclient import TestClient
from app.main import app
from tests.constants import Constants

client = TestClient(app)

ENCODER_URL = "/v1/encoder/"


def test_invalid_algorithm():
    """
    Test the case when the algorithm is invalid.
    """
    res = client.post(ENCODER_URL,
                      json={"text": Constants.TEXT_1.value,
                            "algorithm": "invalid"})
    assert res.status_code == 400
    assert res.json() == {"detail": "Invalid algorithm"}


def test_missing_text():
    """
    Test the case when the text is missing.
    """
    res = client.post(ENCODER_URL)
    assert res.status_code == 422


def test_encode_text_1():
    """
    Test the case when the text is Constants.TEXT_1.
    """
    res = client.post(ENCODER_URL,
                      json={"text": Constants.TEXT_1.value})
    assert res.status_code == 200
    assert res.json() == {"encoding_map": Constants.ENC_MAP_1.value,
                          "encoded_text": Constants.ENC_TEXT_1.value}


def test_encode_text_2():
    """
    Test the case when the text is Constants.TEXT_2.
    """
    res = client.post(ENCODER_URL,
                      json={"text": Constants.TEXT_2.value})
    assert res.status_code == 200
    assert res.json() == {"encoding_map": Constants.ENC_MAP_2.value,
                          "encoded_text": Constants.ENC_TEXT_2.value}


def test_encode_text_separated_into_syllables():
    """
    Test the case when the text is separated into syllables. In this case, the text is 
    Constants.TEXT_SEPARATE_SYLLABLES.
    """
    res = client.post(ENCODER_URL,
                      json={"separate_syllables": True,
                            "text": Constants.TEXT_SEPARATE_SYLLABLES.value})
    assert res.status_code == 200
    assert res.json() == {"encoding_map": Constants.ENC_MAP_SEPARATE_SYLLABLES.value,
                          "encoded_text": Constants.ENC_TEXT_SEPARATE_SYLLABLES.value}
