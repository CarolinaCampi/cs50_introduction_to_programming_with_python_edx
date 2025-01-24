from bank import value

def test_lowercase():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("bye") == 100

def test_uppercase():
    assert value("HELLO") == 0
    assert value("HI") == 20
    assert value("BYE") == 100


def test_spaces():
    assert value("hello there") == 0
    assert value("hi there") == 20
    assert value("good morning") == 100

def test_number():
    assert value("12345") == 100
    assert value("h12345") == 20
    assert value("hello 12345") == 0
    

