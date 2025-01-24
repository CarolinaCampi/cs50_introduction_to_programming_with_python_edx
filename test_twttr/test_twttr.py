from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hola") == "hl"
    assert shorten("aeiou") == ""

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HOLA") == "HL"
    assert shorten("AEIOU") == ""

def test_number():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("hi!") == "h!"
    assert shorten("Why?") == "Why?"

def test_empty():
    assert shorten("") == ""
