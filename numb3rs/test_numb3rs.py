from numb3rs import validate

def test_numbers():
    assert validate("0.0.0.0") == True
    assert validate("100.100.100.100") == True
    assert validate("255.255.255.255") == True
    assert validate("-1.-1.-1.-1") == False
    assert validate("256.256.256.256") == False
    assert validate("1000.1000.1000.1000") == False

def test_position():
    assert validate("100.300.100.100") == False
    assert validate("100.100.300.100") == False
    assert validate("100.100.100.300") == False
    assert validate("300.100.100.100") == False

def test_string():
    assert validate("cat.cat.cat.cat") == False
    assert validate("cat.0.0.0") == False
    assert validate("0.cat.0.0") == False
    assert validate("0.0.cat.0") == False
    assert validate("0.0.0.cat") == False

def test_phrase():
    assert validate("My ip is 0.0.0.0") == False

def test_points():
    assert validate("0") == False
    assert validate("256") == False
    assert validate("cat") == False
    assert validate("0.") == False
    assert validate("0.0") == False
    assert validate("0.0.0") == False
