import pytest

from fuel import convert, gauge

def test_convert_int():
    assert convert("1/1") == 100
    assert convert("50/100") == 50
    assert convert("0/1") == 0

def test_convert_string():
    with pytest.raises(ValueError):
          convert("cat/cat")

def test_convert_divide_by_zero():
     with pytest.raises(ZeroDivisionError):
          convert("1/0")

def test_gauge_empty():
     assert gauge(0) == "E"
     assert gauge(1) == "E"

def test_gauge_number():
     assert gauge(50) == "50%"
     assert gauge(98) == "98%"

def test_gauge_full():
     assert gauge(99) == "F"
     assert gauge(100) == "F"
