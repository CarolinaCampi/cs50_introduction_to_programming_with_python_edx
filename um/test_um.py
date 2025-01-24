from um import count

def test_lowercase():
    assert count("um") == 1
    assert count("um um") == 2
    assert count("um um um") == 3

def test_uppercase():
    assert count("Um") == 1
    assert count("UM") == 1

def test_punctuation():
    assert count("um?") == 1
    assert count("um!") == 1
    assert count(" um ") == 1

def test_mispelled():
    assert count("umm") == 0
    assert count("uum") == 0

def test_phrase():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_containing():
    assert count("Yummy") == 0
    assert count("Um, do you like to drum?") == 1
