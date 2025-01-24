from plates import is_valid

def test_first_two():
    assert is_valid("AA1234") == True
    assert is_valid("aa1234") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("A12345") == False
    assert is_valid("123456") == False

def test_length():
    assert is_valid("AA") == True
    assert is_valid("AA123") == True
    assert is_valid("A") == False
    assert is_valid("AA12345") == False

def test_letter_after_number():
    assert is_valid("AA11AA") == False

def test_first_number():
    assert is_valid("AAA000") == False

def test_punctuation():
    assert is_valid("AA 123") == False
    assert is_valid("AA123.") == False
