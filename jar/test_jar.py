from jar import Jar

def test_init():
    jar_init1 = Jar()
    assert jar_init1.capacity == 12
    assert jar_init1.size == 0
    jar_init2 = Jar(10)
    assert jar_init2.capacity == 10


def test_str():
    jar_str = Jar()
    assert str(jar_str) == ""
    jar_str.deposit(1)
    assert str(jar_str) == "🍪"
    jar_str.deposit(7)
    assert str(jar_str) == "🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar_deposit = Jar()
    jar_deposit.deposit(6)
    assert jar_deposit.size == 6


def test_withdraw():
    jar_withdraw = Jar()
    jar_withdraw.deposit(10)
    jar_withdraw.withdraw(5)
    assert jar_withdraw.size == 5
