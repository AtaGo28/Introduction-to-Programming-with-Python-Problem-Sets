from jar import Jar
import pytest


def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


def test_init():
    jar = Jar(2)
    assert jar.capacity == 2
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(3)
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)
    jar.deposit(5)
    assert jar.size == 5
    assert jar.capacity == 12
    with pytest.raises(ValueError):
        jar.deposit(8)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    assert jar.capacity == 12
    with pytest.raises(ValueError):
        jar.withdraw(3)
        
if __name__ == "__main__":
    main()