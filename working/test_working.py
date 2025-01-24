import pytest
from working import convert

def test_hour():
    assert convert("1:23 AM to 1:23 AM") == "01:23 to 01:23"
    assert convert("11:23 AM to 1:23 AM") == "11:23 to 01:23"
    assert convert("1:23 AM to 11:23 AM") == "01:23 to 11:23"
    assert convert("11:23 AM to 11:23 AM") == "11:23 to 11:23"
    with pytest.raises(ValueError):
        convert("13:23 AM to 1:23 AM")
    with pytest.raises(ValueError):
        convert("1:23 AM to 13:23 AM")
    with pytest.raises(ValueError):
        convert("AA:23 AM to 1:23 AM")
    with pytest.raises(ValueError):
        convert("1:23 AM to AA:23 AM")

def test_minutes():
    with pytest.raises(ValueError):
        convert("1:60 AM to 13:23 AM")
    with pytest.raises(ValueError):
        convert("1:23 AM to 13:60 AM")
    with pytest.raises(ValueError):
        convert("1:AA AM to 1:23 AM")
    with pytest.raises(ValueError):
        convert("1:23 AM to 1:AA AM")

def test_no_minutes():
    assert convert("1 AM to 11 AM") == "01:00 to 11:00"
    assert convert("1 AM to 11 PM") == "01:00 to 23:00"

def test_am_pm():
    assert convert("1:23 AM to 1:23 PM") == "01:23 to 13:23"
    assert convert("1:23 PM to 1:23 AM") == "13:23 to 01:23"
    assert convert("1:23 PM to 1:23 PM") == "13:23 to 13:23"
    with pytest.raises(ValueError):
        convert("I work 1:23 AM to 1:23 cat")
    with pytest.raises(ValueError):
        convert("I work 1:23 cat to 1:23 PM")

def test_phrase():
    with pytest.raises(ValueError):
        convert("I work 1:23 AM to 1:23 AM")

def test_to():
    with pytest.raises(ValueError):
        convert("1:23 AM 1:23 AM")
