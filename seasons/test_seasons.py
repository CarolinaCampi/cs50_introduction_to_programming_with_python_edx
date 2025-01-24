from seasons import validate_input, calculate
import pytest

def test_input_int():
    assert validate_input("1990-01-01") == "1990-01-01"
    with pytest.raises(ValueError):
        validate_input("1990-01-1")
    with pytest.raises(ValueError):
        validate_input("90-01-01")
    with pytest.raises(ValueError):
        validate_input("1990-1-01")

def test_input_string():
    with pytest.raises(ValueError):
        validate_input("cats-ca-ca")
    with pytest.raises(ValueError):
        validate_input("cats")

def test_input_incomplete():
    with pytest.raises(ValueError):
        validate_input("1")
    with pytest.raises(ValueError):
        validate_input("1990")

def test_calculate():
    assert calculate("2022-11-21") == "One million, fifty-two thousand, six hundred forty minutes"
